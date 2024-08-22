# Discord-Message-Copier
This Discord selfbot copies messages from one channel to another or from one server to another no limit in how many channels should be copied and you dont need admin rights on the source channel!

!HOW TO SETUP!

**Disclaimer**: Discord's Terms of Service prohibit the use of selfbots, which are bots that run under a user's account. Using a selfbot can lead to your account being banned. Proceed with caution and at your own risk.

### Step 1: Prerequisites 🛠️

1. **Python Installation**:
   - **Windows**:
     - Download Python from the [official Python website](https://www.python.org/downloads/).
     - Run the installer, and during installation, make sure to check the box that says "Add Python to PATH".
   - **MacOS/Linux**:
     - Open your terminal and type:
       ```bash
       brew install python3  # MacOS with Homebrew
       ```
       ```bash
       sudo apt-get install python3  # Ubuntu/Debian
       ```

2. **Text Editor**: 
   - Install a text editor to write and edit your code, such as [Visual Studio Code](https://code.visualstudio.com/) or [Sublime Text](https://www.sublimetext.com/).

3. **PIP Installation**:
   - Ensure you have PIP (Python's package installer). To check, run:
     ```bash
     pip --version
     ```
     If not installed, you can install it by running:
     ```bash
     python -m ensurepip --upgrade
     ```

4. **Python Requests Library**:
   - Install the `requests` library, which is used to make HTTP requests in Python:
     ```bash
     pip install requests
     ```

### Step 2: Create the Script 🖥️

1. **Create a Python File**:
   - Open your text editor and create a new file. Name it something like `discord_selfbot.py`.

2. **Copy the Script**:
   - Copy the script provided in here as "message copier.py into this file.

### Step 3: Configure the Script ⚙️

1. **Discord User Token**:
   - **Warning**: Sharing your Discord user token can give full access to your account, so keep it secure.
   - To get your user token:
     - Open Discord in a web browser and log in.
     - Press `Ctrl+Shift+I` (Windows) or `Cmd+Option+I` (Mac) to open the Developer Tools.
     - Go to the "Network" tab and filter by "XHR".
     - Send a message or navigate somewhere in Discord, and look for a request called `messages`.
     - Click on it and scroll down to the "Headers" tab, then look for "authorization". The value next to it is your token.
     - Copy your token and paste it into the `TOKEN` variable in your script:
       ```python
       TOKEN = 'YOUR_DISCORD_TOKEN_HERE'
       ```

2. **Channel Map Configuration**:
   - In the `CHANNEL_MAP` dictionary, specify the source channel ID and the target channel ID where you want messages to be forwarded.
     ```python
     CHANNEL_MAP = {
         'SOURCE_CHANNEL_ID': 'TARGET_CHANNEL_ID',
     }
     ```
   - You can add multiple source-target pairs:
     ```python
     CHANNEL_MAP = {
         '123456789012345678': '987654321098765432',  # Example 1
         '234567890123456789': '876543210987654321',  # Example 2
     }
     ```

### Step 4: Run the Script 🚀

1. **Open Terminal/Command Prompt**:
   - Navigate to the directory where your script is saved. For example, if your script is on your Desktop:
     ```bash
     cd Desktop
     ```

2. **Run the Script**:
   - Execute the script by typing:
     ```bash
     python discord_selfbot.py
     ```
   - The script will start fetching and forwarding messages from your specified channels.

3. **Monitor the Script**:
   - Watch the terminal for output. If it says "Rate limited," the script will wait and retry. Any successful message forwarding will also be shown.

### Step 5: Keep the Script Running 🕒

- **Keep the Terminal/Command Prompt Open**: 
  - As long as the terminal is open, the script will keep running. If you close it, the script will stop.
  
- **Use a VPS (Optional)**:
  - If you want the script to run 24/7, consider running it on a Virtual Private Server (VPS) like [DigitalOcean](https://www.digitalocean.com/) or [AWS](https://aws.amazon.com/).

### Common Issues & Troubleshooting 🛠️

1. **Invalid Token Error**: 
   - Ensure your token is correctly copied and not expired. You may need to re-copy it from Discord if it changes.

2. **Rate Limiting**:
   - Discord has rate limits to prevent spamming. The script handles rate limits by pausing and retrying, but heavy use may cause delays.

3. **Permission Errors**:
   - Ensure your account has permissions to read and send messages in the specified channels.
