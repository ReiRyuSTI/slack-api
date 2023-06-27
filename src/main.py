import csv
from slack_sdk import WebClient
from dotenv import load_dotenv
import os

load_dotenv()

client_secret = os.getenv("CLIENT_SECRET")
client = WebClient(client_secret)

CHANNEL_ID = 'C0585C16MJ5'

response = client.conversations_history(channel=CHANNEL_ID)

messages = response.get('messages')
message_list = [message["text"] for message in messages]

message_one_line = ",".join(message_list)
print(message_one_line)
message_one_line_replace = message_one_line.replace(",","\n")

message_list = message_one_line_replace.split("\n")

with open("data.csv", "w", encoding="UTF-8") as file:
    writer = csv.writer(file)
    for message in message_list:
        writer.writerow([message])
