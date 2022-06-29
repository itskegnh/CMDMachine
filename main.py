#  ██████ ███    ███ ██████  ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
# ██      ████  ████ ██   ██ ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
# ██      ██ ████ ██ ██   ██ ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
# ██      ██  ██  ██ ██   ██ ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
#  ██████ ██      ██ ██████  ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 

import json
import os
import requests, time

class stdio:
    def println(*args, end="\n"):
        args = " ".join(args).split("\n")
        for i, line in enumerate(args):
            if i == len(args) - 1:
                print(line + end, end="")
            else: print(line)
            time.sleep(0.05)

def title():
    # clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # stdio.println the header
    stdio.println("""
  ██████ ███    ███ ██████  ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
 ██      ████  ████ ██   ██ ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
 ██      ██ ████ ██ ██   ██ ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
 ██      ██  ██  ██ ██   ██ ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
  ██████ ██      ██ ██████  ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
                                    © 2022 William Jackson. All rights reserved.
    """)

def boot():
    title()

    # Check for updates
    stdio.println("Checking for updates...", end="")
    ENDPOINT = "https://raw.githubusercontent.com/itskegnh/CMDMachine/master/dat.json"
    FILEPATH = os.path.dirname(os.path.realpath(__name__))
    try:
        response = requests.get(ENDPOINT)
        if response.status_code == 200:
            with open(f"{FILEPATH}/dat.json", "r") as f:
                dat = json.load(f)
            gitdat = response.json()
            if dat["version"] != gitdat["version"]:
                stdio.println(f"\r\033[93mWARNING: \033[0mYou are running an outdated version of CMDMachine.\n\tYour Version: \033[91m{dat['version']}\033[0m\n\tLatest Version: \033[92m{gitdat['version']}\033[0m\n\tRun command: \033[94mupdate\033[0m")
            else:
                stdio.println("\rYou're running the latest version of CMDMachine!")
        else:
            stdio.println("\r\033[91mERROR: \033[0mCould not check for updates.")
    except requests.exceptions.ConnectionError:
        stdio.println("\r\033[91mERROR: \033[0mYou aren't connected to wifi.")
    stdio.println("\n")

    stdio.println("Type \033[94mhelp \033[0mfor a list of commands.")

boot()

commands = {
    "reboot": {
        "func": boot,
        "desc": "reboot CMDMachine"
    },
    "clear": {
        "func": title,
        "desc": "clear the screen"
    },
    "update": {
        "func": lambda: stdio.println("Download the Source at \033[94mhttps://github.com/itskegnh/CMDMachine/\033[0m"),
        "desc": "Update your CMDMachine Client."
    }
}

commands["help"] = {
    "func": lambda: [stdio.println(command, "-", commands[command]["desc"]) for command in commands.keys()],
    "desc": "Shows this page."
}

while True:
    cmdin = input("> ")
    if cmdin.split(" ")[0] in commands:
        if len(cmdin.split(" ")) == 1:
            commands[cmdin.split(" ")[0]]["func"]()
        else:
            commands[cmdin.split(" ")[0]]["func"](cmdin.split(" ")[1])
