import discord
import urllib.request
import json
import os
from datetime import datetime
from dotenv import load_dotenv
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import requests
from discord import Webhook, RequestsWebhookAdapter
import sys
from datetime import datetime

load_dotenv()

webhook_url = os.getenv('WEBHOOK')
log_path = os.getenv('LOGPATH')

client = discord.Client()

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):

        if event.src_path == log_path:

            try:
        
                with open(log_path, 'r') as f:

                    # Get last line
                    lines = f.read().splitlines()
                    last_line = lines[-1]

                    # Check if someone has joined the game
                    if "joined the game" in last_line:
                        player_joined = last_line[33:]
                        print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {player_joined}")
                        send_message(player_joined)
                
                    # Check if someone has left the game
                    if "left the game" in last_line:
                        player_left = last_line[33:]
                        print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {player_left}")
                        send_message(player_left)

                    # Check if server is starting
                    if 'For help, type "help"' in last_line:
                        print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] The server is starting...")
                        send_message("The server is starting...")

                    # Check if server is shutting down
                    if "Saving chunks for level 'ServerLevel[world]'/minecraft:overworld" in last_line:
                        print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] The server is shutting down...")
                        send_message("The server is shutting down...")
                        sys.exit()


            except SystemExit:
                sys.exit()

            except:
                print("\nError\n")

def send_message(message):
    print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Sending message to Discord channel: {message}")
    webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
    webhook.send(message) 

print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Starting: Minecraft Server Discord Bot Alerts")

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=log_path[:-11], recursive=False)

observer.start()

try:
    print(f"[INFO][{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Detecting changes to log file...")
    while True:
        sleep(1)
        f = open(log_path, "r")
except KeyboardInterrupt:
    observer.stop()
observer.join()

