import requests

# Replace with your TikTok user ID
USER_ID = "USER_ID"

# Reason for reporting the user
REASON = "REASON"

# Description of why you are reporting the user
DESCRIPTION = "DESCRIPTION"

# TikTok API endpoint for reporting a user
REPORT_ENDPOINT = "https://api.tiktok.com/aweme/v1/user/report/"

# TikTok API access token (replace with your own)
ACCESS_TOKEN = "ACCESS_TOKEN"

# Prepare the request payload
payload = {
    "reason": REASON,
    "description": DESCRIPTION,
    "user_id": USER_ID
}

# Prepare the request headers
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Send the POST request to the TikTok API
response = requests.post(REPORT_ENDPOINT, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("User reported successfully.")
else:
    print("Failed to report the user.")
