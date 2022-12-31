# Import necessary modules
import shutil
import time
import os
from configparser import ConfigParser

# Read configuration file
file = "config.ini"
config = ConfigParser()
config.read(file)

# If configuration file does not have SETTINGS section, add it with default values
if not config.has_section("SETTINGS"):
    config.add_section("SETTINGS")
    config.set("SETTINGS", "source", "E:\MoviesSource/")
    config.set("SETTINGS", "destination", "E:\Movies/")
    config.set("SETTINGS", "sleep_timer", "5")

# Write changes to configuration file
with open(file, 'w') as configfile:
    config.write(configfile)

# Display logo in console
def logo():
    print(logo)

# Display menu in console
def menu():
    print(options)

# Clear console
def clear():
    os.system('cls')

# Allow user to adjust settings in configuration file
def settings_menu():
    logo()
    print(instructions)
    source_inp = input("Enter your source path: ")
    dest_inp = input("Enter your destination path: ")
    sleep_timer_inp = input("Enter your sleep_timer: ")

    config.set("SETTINGS", "source", source_inp)
    config.set("SETTINGS", "destination", dest_inp)
    config.set("SETTINGS", "sleep_timer", sleep_timer_inp)
    with open(file, 'w') as configfile:
        config.write(configfile)
    
    clear()
    logo()
    menu()

# Transfer files from source to destination
def main_app(r):
    # If r is True, transfer files
    if r:
        # Get source and destination directories from configuration file
        source = config.get("SETTINGS", "source")
        destination = config.get("SETTINGS", "destination")
        # Transfer files from source to destination
        shutil.move(source, destination)
        # Wait for specified amount of time
        time.sleep(int(config.get("SETTINGS", "sleep_timer")))
        # Send notification
        notification()

# Placeholder function for sending notification
def notification():
    print("Notification not implemented")

# Main program loop
while True:
    # Display menu and get user input
    logo()
    menu()
    option = int(input("Enter your option: "))

    # If user selects "Run", transfer files
    if option == 1:
        main_app(True)
    # If user selects "Settings", allow user to adjust settings
    elif option == 2:
        settings_menu()
    # If user selects "Exit", exit program
    elif option == 3:
        break
    # If user enters invalid option, display error message
    else:
        print("Invalid option")