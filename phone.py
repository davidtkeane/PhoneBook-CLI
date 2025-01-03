#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Title: PhoneBook App for Python and CLI
#
# Created by Ranger (Dec 2024) Version 1.0.0
# Modified by David Keane (Dec 31st 2024) Version 2.0.1
#
# Instructions for running the application:
# 1. After downloading the file, run the following command to make it executable:
#    chmod +x phone
# 2. Copy or move the file to a directory in your PATH to run it from anywhere.
#    For example, 
#    A: Copy the phone file to /usr/local/bin/phone to run from the terminal.
#    sudo cp phone /usr/local/bin/phone
# 3. Run the application using the following command if not in the PATH:
#    ./phone
# 4. Run the application using the following command if in the PATH:
#    phone
#
# Note: The application requires sudo to run commands that require elevated privileges.
#
# Description:
# This is a simple phonebook application that allows you to add, search, view, edit, and delete contacts.
# It uses SQLite to store the contacts and a password file to store the password.
# The password is hashed using SHA-256 before storing it in the file.
# The application also uses sudo to run commands that require elevated privileges.
# The application is designed to run on Unix-based systems.
#
# Features:
# The application has the following features:
# - Add a new contact with name, phone number, email, and address.
# - Search for a contact by name or phone number.
# - View all contacts in the phonebook.
# - Edit a contact's details.
# - Delete a contact from the phonebook.
# - Set a new password for the phonebook.
#
# Decription:
# The application has the following functions:
# - The application allows the user to add a new contact with name, phone number, email, and address.
# - The application allows the user to search for a contact by name or phone number.
# - The application allows the user to view all contacts in the phonebook.
# - The application allows the user to edit a contact's details.
# - The application allows the user to delete a contact from the phonebook.
# - The application allows the user to set a new password for the phonebook.
# - The application uses colorama to add color to the output.
# - The application uses subprocess to run system commands.
# - The application uses getpass to get the password from the user without echoing it.
# - The application uses hashlib to hash the password before storing it.
# - The application has nice exit messages.
# - This application is designed to run on Unix-based systems.
#
# Modules:
# The application uses the following modules:
# - sqlite3: to interact with the SQLite database.
# - os: to interact with the operating system.
# - subprocess: to run system commands.
# - getpass: to get the password from the user without echoing it.
# - hashlib: to hash the password before storing it.
# - sys: to exit the application.
# - colorama: to add color to the output.
#
# Instructions for the application:
# The application has the following instructions:
# - The application displays a welcome banner when it starts.
# - The application prompts the user for the sudo password to run commands that require elevated privileges.
# - The application prompts the user for the phonebook password to access the phonebook.
# - If the password file does not exist, the application prompts the user to set a new password.
# - The application hashes the password using SHA-256 before storing it in the file.
#
#
# PhoneBook App for Python and CLI

# Import the necessary modules
import sqlite3
import os
import subprocess
import getpass
import hashlib
import sys
import platform

# Password file path
PASSWORD_FILE = "/Users/Ranger/db/password.txt"

# This is the banner for the bot
def banner():
    Banner = """
            ____  ___    _   __________________       _____ __  _____  __________  __
           / __ \/   |  / | / / ____/ ____/ __ \     / ___//  |/  /\ \/ /_  __/ / / /
          / /_/ / /| | /  |/ / / __/ __/ / /_/ /_____\__ \/ /|_/ /  \  / / / / /_/ /
         / _, _/ ___ |/ /|  / /_/ / /___/ _, _/_____/__/ / /  / /   / / / / / __  /
        /_/ |_/_/  |_/_/ |_/\____/_____/_/ |_|     /____/_/  /_/   /_/ /_/ /_/ /_/
"""
    print(Banner)  # This line is crucial to actually display the banner

def bunny():
    print(r"""
            % 💀

           /\ /|
          |||| |
           \ | \
       _ _ /  ()()
     /    \   =>*<=
   /|      \   /
   \|     /__| |
     \_____) \__)


I hope this helps!% 💀
    """)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 2.0.0\n")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def run_sudo_command(command):
    """Runs a command with sudo and logs the output."""
    try:
        # If the command is a chown, replace "root:root" with the current user:group
        if command[0] == 'chown' and 'root:root' in command[1]:
            user = os.getlogin()
            group_name = subprocess.check_output(['id', '-gn', user]).decode().strip()
            command[1] = command[1].replace('root:root', f"{user}:{group_name}")

        result = subprocess.run(['sudo'] + command, check=True, capture_output=True, text=True)
        if result.stderr:
            print(f"Sudo command stderr: {result.stderr}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        print(f"Sudo command failed: {e}. Check that sudo is configured.")
        return False

def ask_sudo_password():
    """Prompts for a sudo password and validates it, forcing a new check."""
    try:
        # Invalidate existing sudo credentials
        subprocess.run(['sudo', '-k'], check=True, capture_output=True)
        # Now validate the password
        subprocess.run(['sudo', '-v'], check=True, input=b'')
        print("Thank you. Sudo password is correct.")
    except subprocess.CalledProcessError:
        print(Fore.BLUE + "Incorrect sudo password. See you next time!" + Style.RESET_ALL)
        sys.exit(1)

def set_password():
    print("Enter New Password for Phone")
    password = getpass.getpass("Set a new password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match. Try again.")
        return set_password()
    hashed_password = hash_password(password)
    try:
        with open(PASSWORD_FILE, 'w') as f:
            f.write(hashed_password)
        if not run_sudo_command(['chown', f"{os.getlogin()}:{os.getlogin()}", PASSWORD_FILE]):
             print("Failed to set permissions on password file.")
        else:
              print("Password set successfully.")
    except PermissionError:
        print(f"Permission denied: Unable to write to {PASSWORD_FILE}. Please run the script with sudo to set the password.")
        subprocess.run(['sudo', sys.executable, __file__, '--set-password'], check=True)
        exit(0)

def check_password():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        if not os.path.exists(PASSWORD_FILE):
            print("No password set. Please set a password.")
            set_password()
            return
        password = getpass.getpass("Enter password: ")
        hashed_password = hash_password(password)
        with open(PASSWORD_FILE, 'r') as f:
            stored_password = f.read().strip()
        if hashed_password == stored_password:
            return  # Correct
        else:
            attempts += 1
            print("Incorrect password. Try again.")
    print(Fore.BLUE + "Too many incorrect attempts. See you next time!" + Style.RESET_ALL)
    sys.exit(1)

def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            email2 TEXT,
            address TEXT
            
        )
    ''')

def add_contact(conn, name, phone, email, address, email2=None):
    conn.execute("INSERT INTO contacts (name, phone, email, address, email2) VALUES (?, ?, ?, ?, ?)", (name, phone, email, address, email2))
    conn.commit()

def search_contact(conn, query):
    results = conn.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", ('%' + query + '%', '%' + query + '%')).fetchall()
    return results

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    # Use 6 columns for ID, Name, Phone, Email, Address, Email2
    widths = [5, 15, 15, 25, 30, 30]
    if contacts:
        for contact in contacts:
            for i in range(len(contact)):
                widths[i] = max(widths[i], len(str(contact[i])))

    header_format = ""
    row_format = ""
    separator = ""
    total_width = 0
    for w in widths:
        header_format += "{:<" + str(w) + "} "
        row_format += "{:<" + str(w) + "} "
        separator += "-" * w + " "
        total_width += w + 1

    print("-" * total_width)
    print(header_format.format("ID", "Name", "Phone", "Email", "Address", "Email2"))
    print("-" * total_width)

    for contact in contacts:
        print(row_format.format(*contact))

    print("-" * total_width)

def edit_contact(conn, contact_id=None):
    contacts = conn.execute("SELECT * FROM contacts").fetchall()
    if not contacts:
        print("No contacts found. Cannot edit.")
        return

    print("")
    print("Available contacts:")
    display_contacts(contacts)
    print("")

    try:
        contact_id = input("Enter the ID of the contact to edit, or Enter to go back: ")
        contact_id = int(contact_id)
    except ValueError:
        print("Invalid contact ID. Please enter a number.")
        return

    contact = conn.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,)).fetchone()
    if not contact:
        print("Contact not found.")
        return

    print("")
    print("Current contact details:")
    display_contacts([contact])
    print("")

    name = input("Enter new name (leave blank to keep current): ") or contact[1]
    phone = input("Enter new phone (leave blank to keep current): ") or contact[2]
    email = input("Enter new email (leave blank to keep current): ") or contact[3]
    address = input("Enter new address (leave blank to keep current): ") or contact[4]
    email2 = input("Enter second email (leave blank to keep current): ") or contact[5]

    conn.execute("UPDATE contacts SET name = ?, phone = ?, email = ?, address = ?, email2=? WHERE id = ?", (name, phone, email, address, email2, contact_id))
    conn.commit()
    print("Contact updated successfully!")

def delete_contact(conn, contact_id=None):
    contacts = conn.execute("SELECT * FROM contacts").fetchall()
    if not contacts:
        print("No contacts found. Cannot delete.")
        return

    print("")
    print("Available contacts:")
    display_contacts(contacts)
    print("")

    try:
        contact_id = input("Enter the ID of the contact to delete, or Enter to go back: ")
        contact_id = int(contact_id)
    except ValueError:
        print("Invalid contact ID.")
        return

    contact = conn.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,)).fetchone()
    if not contact:
        print("Contact not found.")
        return

    print("")
    print("Current contact details:")
    display_contacts([contact])  # Now you can display the contact
    print("")

    conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print("Contact deleted successfully.")

def ensure_db_exists(db_path):
    """Ensures that the database file and its directory exist."""
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
           if not run_sudo_command(['mkdir', '-p', db_dir]):
                print(f"Failed to create database directory: {db_dir}")
                exit(1)
           if not run_sudo_command(['chown', f"{os.getlogin()}:{os.getlogin()}", db_dir]):
                print("Failed to set permissions on database directory.")
                exit(1)
    if not os.path.exists(db_path):
            if not run_sudo_command(['touch', db_path]):
                   print("Failed to create the database file.")
                   exit(1)
            if not run_sudo_command(['chown', f"{os.getlogin()}:{os.getlogin()}", db_path]):
                print("Failed to set permissions on database file.")
                exit(1)

def ensure_password_dir_exists():
    password_dir = os.path.dirname(PASSWORD_FILE)
    if not os.path.exists(password_dir):
        if not run_sudo_command(['mkdir', '-p', password_dir]):
            print(f"Failed to create the password file directory: {password_dir}")
            sys.exit(1)
        if not run_sudo_command(['chown', f"{os.getlogin()}:{os.getlogin()}", password_dir]):
            print("Failed to set permissions on password file directory.")
            sys.exit(1)


# --- Colors ---
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'

# --- Functions ---

# Get the current user's username
def get_username():
    """Gets the current user's username."""
    try:
        username = subprocess.check_output(['whoami']).decode().strip()
        return username
    except subprocess.CalledProcessError:
        return "Unknown User"

# Check the OS and report if it's macOS
def check_os():
    """Checks the OS and reports if it's macOS."""
    os_name = platform.system()
    if os_name == "Darwin":
        return f"{GREEN}MacBook{NC}"
    else:
        return f"{RED}{os_name}{NC}"

# Display the user information
def display_user_info():
    """Displays the user information within a block of "code"."""
    username = get_username()
    os_type = check_os()
    print(f"""
{YELLOW}--- System Information ---{NC}

    Operating System: {os_type}

    {BLUE}Current User:{NC} {GREEN} ┌──────────────────────────────┐
                   │  {username:<28}│
                   └──────────────────────────────┘{NC}""")

# Display the user information
def main():
    bunny()
    print("")
    display_user_info()
    print("")
    print(f"{GREEN}Welcome to the Phonebook CLI!{NC}")
    print("")
    print(f"{GREEN}Please enter your sudo password to continue.{NC}")
    print(f"{GREEN}Please enter your PhoneBook password to continue.{NC}")
    print("")
    print(f"{GREEN}If you are a new user, please set a new PhoneBook password.{NC}")
    print("")
    ensure_password_dir_exists()
    db_path = "/Users/Ranger/db/phonebook.db"  # Default database path
    if not os.path.exists(PASSWORD_FILE): # check if password file exists first.
        ask_sudo_password()
        set_password()
    else:
        ask_sudo_password()
    ensure_db_exists(db_path)
    check_password()

    conn = sqlite3.connect(db_path)
    create_table(conn)

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Set Password")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number (optional): ")
            email = input("Enter email (optional): ")
            email2 = input("Enter second email (optional): ")
            address = input("Enter address (optional): ")
            add_contact(conn, name, phone, email, address, email2)
            print("Contact added successfully!")
        elif choice == '2':
            query = input("Enter search term: ")
            results = search_contact(conn, query)
            display_contacts(results)
        elif choice == '3':
            results = conn.execute("SELECT * FROM contacts").fetchall()
            display_contacts(results)
        elif choice == '4':
           edit_contact(conn)
        elif choice == '5':
           delete_contact(conn)
        elif choice == '6':
            set_password()
        elif choice == '0':
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")
            bunny()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting gracefully...")
        bunny()
        sys.exit(0)
    clear_screen()
    banner()