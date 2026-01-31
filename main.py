# discord_call_ip_sniffer.py
# Python 3.8+  |  pip install discord.py voice-ip-extractor netifaces psutil
# ------------------------------------------------------------
# Self-bot leve: apenas monitora o tráfego UDP local enquanto estiver
# em canal de voz e imprime os pares <IP:porta> que enviam pacotes de voz.
# ------------------------------------------------------------

import discord, netifaces, psutil, socket, threading, time, ipaddress

TOKEN      = "YOUR_USER_TOKEN_HERE"   # token da tua conta (user self-bot)
GATEWAY_IP = "127.0.0.1"              # opcional – filtra LAN se quiser

UDP_RANGE  = range(50000, 65535)      # portas usadas pelo Discord
VOICE_PKT  = b"\x00\x01"              # magic byte inicial RTP comum

class VoIPMap:
    def __init__(self):
        self.seen = set()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
        self.sock.setblocking(False)
        self.running = True
        threading.Thread(target=self.sniff, daemon=True).start()

    def sniff(self):
        while self.running:
            try:
                raw, _ = self.sock.recvfrom(65535)
                ip_hdr_len = (raw[0] & 0x0F) * 4
                udp_offs   = ip_hdr_len
                src_ip     = socket.inet_ntoa(raw[12:16])
                dst_ip     = socket.inet_ntoa(raw[16:20])
                src_port   = int.from_bytes(raw[udp_offs:udp_offs+2], 'big')
                dst_port   = int.from_bytes(raw[udp_offs+2:udp_offs+4], 'big')
                # mantém só fluxos Discord (porta alta)
                if src_port in UDP_RANGE or dst_port in UDP_RANGE:
                    # verifica se payload começa com byte típico de voz Discord
                    if len(raw) > udp_offs+8 and raw[udp_offs+8:udp_offs+10] == VOICE_PKT:
                        key = f"{src_ip}:{src_port}"
                        if key not in self.seen:
                            self.seen.add(key)
                            print("[VOICE]", key)
            except: pass
            time.sleep(0.001)

    def stop(self): self.running = False

# ---------- CLIENTE DISCORD (self-bot) ----------
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents, self_bot=True)

voip = None

@client.event
async def on_ready():
    global voip
    print(f"Conectado como {client.user}  –  aguardando entrada num canal de voz…")
    voip = VoIPMap()

@client.event
async def on_voice_state_update(member, before, after):
    # dispara sempre que alguém (inclusive você) entra/sai de canal
    if after.channel and member == client.user:
        print(f"\n[VOCÊ ENTROU] {after.channel.guild}  ->  {after.channel}")
        print("Capturando IPs de voz… (Ctrl+C para parar)\n")
    if before.channel and not after.channel and member == client.user:
        print("\n[VOCÊ SAIU] Parando sniff…")
        voip.stop()

client.run(TOKEN, bot=False)
