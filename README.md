# Discord-Call-Ip-Sniffer


### 🕵️‍♂️ VoIP-Sentinel: Advanced UDP Voice Packet SnifferVoIP-Sentinel is an advanced, high-performance network research utility engineered in Python. It is specifically designed to facilitate the monitoring, interception, and analysis of UDP-based voice traffic within real-time communication (RTC) architectures.📖 Table of ContentsProject OverviewTechnical ArchitectureSafety & EthicsPrerequisitesDetailed InstallationConfiguration GuideThe Science of VoIP SniffingTroubleshootingAPI DocumentationRoadmapContribution🔍 Project OverviewModern VoIP applications utilize complex obfuscation to protect user data. VoIP-Sentinel aims to deconstruct these layers by analyzing packet headers and identifying specific RTP (Real-time Transport Protocol) signatures.


## ⚙️ Technical Core1. Raw Socket LayerThe engine utilizes socket.SOCK_RAW to bypass the standard transport layer abstractions. This allows the tool to read every bit of data entering the Network Interface Card (NIC) before the OS filters it.2. Intelligent Protocol FilteringBy targeting the UDP High-Port Range (50000-65535), the tool ignores irrelevant noise (HTTP/S, DNS, etc.) and focuses solely on potential voice streams.3. RTP Pattern MatchingOur algorithm scans the first 16 bits of the UDP payload for the \x00\x01 magic byte sequence, a common identifier for Discord's proprietary voice encapsulation.4. Concurrency ModelThe sniffer operates on a non-blocking, multi-threaded architecture:Thread A: Discord Gateway Monitoring (WebSocket).Thread B: Low-level UDP Sniffing.Thread C: Real-time console logging and I/O.⚠️ Safety & DisclaimerTerms of Service: The use of automation on user accounts (self-bots) is a violation of Discord's ToS and will lead to account termination.Legal: This tool is for educational research only. 



### Unauthorized interception of data is illegal in many jurisdictions.System Integrity: Running raw sockets requires Root/Admin privileges, which grants the script full access to your network stack.🛠️ PrerequisitesRequirementSpecificationOSWindows 10/11 or Linux (Kernel 4.x+)Python3.8 or higherPrivilegesAdministrator / Sudo accessNetworkEthernet recommended (WiFi may drop packets)📝 The Science of VoIP SniffingTo understand how this tool works, one must understand the OSI Model. While most apps live at Layer 7, VoIP-Sentinel peers into Layer 3 and 4.The Capture Flow:Handshake Detection: Identifying the initial STUN/ICE requests.Traffic Analysis: Sorting packets by length (Voice packets are usually small and consistent).IP Extraction: Stripping the IP header to reveal the source and destination nodes.🚀 Installation & SetupStep 1: Clone the RepositoryBashgit clone https://github.com/YOUR_USER/VoIP-Sentinel.git
### cd VoIP-Sentinel
### Step 2: Virtual EnvironmentBashpython -m venv venv
### source venv/bin/activate  # Linux
### venv\Scripts\activate     # Windows
### Step 3: DependenciesBashpip install -r requirements.txt 


``📈 Development Roadmap[ ] Phase 1: Core Sniffing Logic (Completed).[ ] Phase 2: Multi-Platform Support (Completed).[ ] Phase 3: Geo-IP Mapping (In Progress).[ ] Phase 4: Discord Token Encryption.[ ] Phase 5: Packet Injection Testing.🤝 ContributionContributions are what make the open-source community an amazing place to learn and create.Fork the Project.Create your Feature Branch (git checkout -b feature/AmazingFeature).Commit your Changes (git commit -m 'Add some AmazingFeature').Push to the Branch (git push origin feature/AmazingFeature).Open a Pull Request.📄 LicenseDistributed under the MIT License. See LICENSE for more information.

>⚠️ Educational purposets only>!


# Usage

### 1️⃣ Environment Setup
### It is highly recommended to use a virtual environment to prevent dependency conflicts with other Python projects.

Bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

### 2️⃣ Library InstallationYou must install the specific dependencies required for network sniffing and Discord API interaction.Bash# Note: We use discord.py 1.7.3 for self-bot compatibility
### pip install discord.py==1.7.3 netifaces psutil
### discord.py 1.7.3: Essential for the self-bot connection.netifaces: Used to detect your local network adapters.psutil: Helps manage system processes during sniffing.3️⃣ Configuration (Token & Gateway)Open the discord_call_ip_sniffer.py file in your editor and modify the following lines at the top:TOKEN: Replace "YOUR_USER_TOKEN_HERE" with your account token.GATEWAY_IP: Set to your router's IP (e.g., 192.168.1.1) to filter out local noise, or leave as 127.0.0.1 for general testing.4️⃣ Launch with Elevated PrivilegesBecause this tool uses Raw Sockets to "listen" to network traffic, it requires kernel-level permissions.Windows: Right-click your Terminal/CMD and select "Run as Administrator".Linux: You must use sudo:Bashsudo python discord_call_ip_sniffer.py


### 5️⃣ Interception ProcessStart the Script: The console should display Connected as [YourUser].Join a Voice Call: Enter any Discord channel or start a private call.Monitor Traffic: The script will automatically trigger when it detects you are in a voice state.Capture: Look for the [VOICE] logs. These show the <IP:Port> pairs currently sending audio data to your machine.Stop: Use Ctrl+C to terminate the session safely.🛠️ Execution SummaryRequirementDescriptionWhy?Admin/RootElevated PrivilegesTo open SOCK_RAW interfacesAuthUser TokenTo link the sniffer to your Discord accountNetworkActive Voice CallTraffic only exists during an active streamSafetyVirtual MachineRecommended to protect your host OS
