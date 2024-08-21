import requests
import time

# Your Discord user token
TOKEN = 'YOUR_DISCORD_TOKEN_HERE'

# List of source channels and corresponding target channels
CHANNEL_MAP = {
    'SOURCE_CHANNEL_ID': 'TARGET_CHANNEL_ID', # The Discord API wont detect this
    'SOURCE_CHANNEL_ID': 'TARGET_CHANNEL_ID', # Create as many as you want!!!
}

# Set up the request headers with your token
headers = {
    'Authorization': TOKEN,  # Use token directly for self-bot
    'Content-Type': 'application/json'
}

def forward_message(content, target_channel_id):
    """Forward each line of the message content to the target channel as a separate message."""
    lines = content.splitlines()  # Split content by line breaks
    for line in lines:
        if line.strip():  # Only send non-empty lines
            # Prepare the payload with the content preserving the formatting
            payload = {'content': line.strip()}
            url = f'https://discord.com/api/v9/channels/{target_channel_id}/messages'
            
            # Send the text message with exact formatting
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                print(f"Line forwarded successfully to channel {target_channel_id}: {line.strip()}")
            elif response.status_code == 429:
                retry_after = response.json().get('retry_after', 1)
                print(f"Rate limited. Waiting for {retry_after} seconds.")
                time.sleep(retry_after)
                forward_message(line.strip(), target_channel_id)  # Retry
            else:
                print(f"Failed to forward line to channel {target_channel_id}: {response.status_code}")
            
            # Delay between each line to ensure correct order and avoid rate limits
            time.sleep(1)

def fetch_old_messages():
    """Fetch and forward all old messages from the source channels."""
    for source_channel_id, target_channel_id in CHANNEL_MAP.items():
        last_message_id = None
        url = f'https://discord.com/api/v9/channels/{source_channel_id}/messages'
        
        while True:  # Remove message limit, fetch all messages
            params = {'limit': 100}
            if last_message_id:
                params['before'] = last_message_id
            
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                messages = response.json()
                if not messages:
                    break  # No more messages to fetch
                
                for message in messages:
                    content = message['content']
                    forward_message(content, target_channel_id)
                    last_message_id = message['id']
                    
                    # Delay between each message to ensure correct order and avoid rate limits
                    time.sleep(2)
            elif response.status_code == 429:
                retry_after = response.json().get('retry_after', 1)
                print(f"Rate limited. Waiting for {retry_after} seconds.")
                time.sleep(retry_after)
            else:
                print(f"Failed to retrieve messages from channel {source_channel_id}: {response.status_code} - {response.json()}")
                break

def listen_for_new_messages():
    """Listen for and forward new messages from the source channels."""
    last_message_id = {source_channel_id: None for source_channel_id in CHANNEL_MAP.keys()}
    
    while True:
        for source_channel_id, target_channel_id in CHANNEL_MAP.items():
            url = f'https://discord.com/api/v9/channels/{source_channel_id}/messages'
            
            params = {
                'limit': 1
            }
            if last_message_id[source_channel_id]:
                params['after'] = last_message_id[source_channel_id]
            
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                messages = response.json()
                if messages:
                    for message in messages:
                        content = message['content']
                        forward_message(content, target_channel_id)
                        last_message_id[source_channel_id] = message['id']
                        
                        # Delay between each message to ensure correct order and avoid rate limits
                        time.sleep(2)
            elif response.status_code == 429:
                retry_after = response.json().get('retry_after', 1)
                print(f"Rate limited. Waiting for {retry_after} seconds.")
                time.sleep(retry_after)
            else:
                print(f"Failed to retrieve new messages from channel {source_channel_id}: {response.status_code} - {response.json()}")
                time.sleep(5)  # Delay before retrying

if __name__ == "__main__":
    # Fetch and forward all old messages
    fetch_old_messages()  # No limit on old message fetching
    
    # Then listen for and forward new messages
    listen_for_new_messages()
