import os
import time
import pygetwindow as gw
from pypresence import Presence

# Define the path to the configuration file
config_file_path = "config.txt"

# Check if the configuration file exists, and if not, prompt for the Client ID
if not os.path.exists(config_file_path):
    client_id = input("Enter your Discord application's Client ID: ")
    with open(config_file_path, "w") as config_file:
        config_file.write(client_id)
else:
    with open(config_file_path, "r") as config_file:
        client_id = config_file.read()

# Initialize Discord presence
RPC = Presence(client_id)
RPC.connect()

while True:
    try:
        # Get the currently focused window
        focused_window = gw.getWindowsWithTitle(gw.getActiveWindow().title)[0]

        # Set the Discord Rich Presence data
        presence_data = {
            "state": focused_window.title,
            "large_text": "https://assets-global.website-files.com/646218c67da47160c64a84d5/6463428fbecdbd5e3e1ba1c7_29.png",
            "large_image": "https://assets-global.website-files.com/646218c67da47160c64a84d5/6463428fbecdbd5e3e1ba1c7_29.png",
        }

        # Update the Discord status
        RPC.update(**presence_data)

    except IndexError:
        # If no window is focused, set a default presence
        RPC.update(state="Idle")

    time.sleep(5)  # Adjust the update interval as needed
