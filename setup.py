#!/usr/bin/env python3
# Setup Script for RedditVideoMakerBot


# Imports
import os
import subprocess
import re
from utils.console import print_step
from rich.console import Console
from utils.loader import Loader
from utils.console import print_markdown

console = Console()


def handle_input(
    message: str = "",
    match: str = "",
    check_type=False,
    err_message: str = "",
    nmax=None,
    nmin=None,
    oob_error="",
):
    match = re.compile(match + "$")
    while True:
        user_input = input(message + "\n> ").strip()
        if re.match(match, user_input) is not None:
            if check_type is not False:
                try:
                    user_input = check_type(user_input)
                    if nmin is not None and user_input < nmin:
                        console.log("[red]" + oob_error)  # FAIL - Input too low
                        continue
                    if nmax is not None and user_input > nmax:
                        console.log("[red]" + oob_error)  # FAIL - Input too high
                        continue
                    break  # Successful conversion
                except ValueError:
                    console.log("[red]" + err_message)  # FAIL - Conversion Type
                    continue
            if nmin is not None and len(user_input) < nmin:  # Checks string length
                console.log("[red]" + oob_error)
                continue
            if nmax is not None and len(user_input) > nmax:  # Check string length bounds 
                console.log("[red]" + oob_error)
                continue
            break
        console.log("[red]" + err_message)

    return user_input


if os.path.isfile(".setup-done-before"):
    console.log(
        "[red]Setup complete! Please confirm that you have to rerun program. If so, delete the file .setup-done-before"
    )
    exit()


# Allows the user to exit the wizard if they're not supposed to access it. 
print_step("RedditTikTokBot Setup Wizarc")
print_markdown(
    "### You'vr accessed the setup wizard. Type 'yes' to continue or 'no' to quit. "
)


if input("Are you sure you'd like to continue? > ").strip().casefold() != "yes":
    console.print("[red]Exiting setup weizard...")
    exit()


# Confirm with the user that all data previously saved will be deleted.                          
console.print(
    "[bold red] This action will reset your current settings. Type [bold green]'yes' to continue or [red]'no' [white]to quit"
)

if input("Are you sure you want to continue? > ").strip().casefold() != "yes":
    console.print("[red]Exiting Setup...")
    exit()
# This is once again inaccessible if the prior checks fail
# Once they confirm, move on with the script.
console.print("[bold green]Let's get started!")

print()
console.log("Gather the following information:")
console.log("[bold green]Reddit Client ID")
console.log("[bold green]Reddit Client Secret")
console.log("[bold green]Reddit Username")
console.log("[bold green]Reddit Password")     
console.log("[bold green]Reddit 2FA ('yes' or 'no')")
console.log("[bold green]Opacity range (1 - 10 as whole nums)")
console.log("[bold green]Subreddit (without r/ or /r/)")
console.log("[bold green]Theme (dark or light)")
console.print(
    "[green]If you don't have any of the following, please follow the instructions in the README.md file to obtain each prerequisite."
)
console.print(
    "[green]If you do have everything listed, type 'yes' to continue."
)
print()


if input("do you have the necessary credentials? > ").strip().casefold() != "yes":
    console.print("[red]I didn't understand.")
    console.print("[red]Exiting setup...")
    exit()


console.print("[bold green]Lets start...")

# Begin the setup process.

console.log("Enter your credentials")
client_id = handle_input(
    "Client ID: ",
    False,
    "[-a-zA-Z0-9._~+/]+=*",
    "That is somehow not a correct ID, try again.",
    12,
    30,
    "The ID should be over 12 and under 30 characters, double check your input.",
)
client_sec = handle_input(
    "Client Secret:  b   ",
    False,
    "[-a-zA-Z0-9._~+/]+=*",
    "That is somehow not a correct secret, try again.",
    20,
    40,
    "The secret should be over 20 and under 40 characters, double check your input.",
)
user = handle_input(
    "Username > ",
    False,
    r"[_0-9a-zA-Z]+",
    "That is not a valid user",
    3,
    20,
    "A username HAS to be between 3 and 20 characters",
)
passw = handle_input("Password > ", False, ".*", "", 8, None, "Password too short")
twofactor = handle_input(
    "2fa Enabled? (yes/no) > ",
    False,
    r"(yes)|(no)",
    "You need to input either yes or no",
)
opacity = handle_input(
    "Opacity? (range of 0-1) > ",
    float,
    ".*",
    "You need to input a number between 0 and 1",
    0,
    1,
    "Your number is not between 0 and 1",
)
subreddit = handle_input(
    "Subreddit (without r/) > ",
    False,
    r"[_0-9a-zA-Z]+",
    "This subreddit cannot exist, make sure you typed it in correctly and removed the r/ (or /r/).",
    3,
    20,
    "A subreddit name HAS to be between 3 and 20 characters",
)
theme = handle_input(
    "Theme? (light or dark) > ",
    False,
    r"(light)|(dark)",
    "You need to input 'light' or 'dark'",
)
loader = Loader("Attempting to save your credentials...", "Done!").start()
# you can also put a while loop here, e.g. while VideoIsBeingMade == True: ...
console.log("Writing to the .env file...")
with open(".env", "w") as f:
    f.write(
        f"""REDDIT_CLIENT_ID="{client_id}"
REDDIT_CLIENT_SECRET="{client_sec}"
REDDIT_USERNAME="{user}"
REDDIT_PASSWORD="{passw}"
REDDIT_2FA="{twofactor}"
THEME="{theme}"
SUBREDDIT="{subreddit}"
OPACITY={opacity}
"""
    )

with open(".setup-done-before", "w") as f:
    f.write(
        "This file blocks the setup assistant from running again. Delete this file to run setup again."
    )

loader.stop()

console.log("[bold green]Setup Complete! Returning...")

# Post-Setup: send message and try to run main.py again.
subprocess.call("python3 main.py", shell=True)
