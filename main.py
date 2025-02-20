import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


client = WebClient(os.environ["SLACK_BOT_TOKEN"])

try:
    response = client.chat_postMessage(channel='#updates', text="Hello world!") # channel ID is: C01RMDXV20K
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")