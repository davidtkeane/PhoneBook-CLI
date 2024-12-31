# PhoneBook CLI Application

![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/PhoneBook-CLI?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/davidtkeane/PhoneBook-CLI?authorFilter=davidtkeane)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/PhoneBook-CLI?style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/davidtkeane)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green) 

## Description 

This is a simple phonebook application that allows you to add, search, view, edit, and delete contacts. It uses SQLite to store the contacts and a password file to store the password. The password is hashed using SHA-256 before storing it in the file. The application also uses `sudo` to run commands that require elevated privileges. The application is designed to run on Unix-based systems.

## Features

- Add a new contact with name, phone number, email, and address.
- Search for a contact by name or phone number.
- View all contacts in the phonebook.
- Edit a contact's details.
- Delete a contact from the phonebook.
- Set a new password for the phonebook.
- Uses `colorama` to add color to the output.
- Uses `subprocess` to run system commands.
- Uses `getpass` to get the password from the user without echoing it.
- Uses `hashlib` to hash the password before storing it.
- Displays nice exit messages.

## Prerequisites

- Python 3.x
- Unix-based system (Linux, macOS)
- `sudo` privileges

## Installation

Instructions for running the application:

## Phone.py
1. Run the application using the following command:

```bash
python phone.py
```

## Phone
## Installation to be able to run in the terminal.

1. **Download the file:**
A:
```
git clone https://github.com/yourusername/phonebook-cli/phone
```
B:
```bash
pip install requirements.txt
```

2. After downloading the file, run the following command to make it executable:

```bash
chmod +x phone
```
3. Copy or move the file to a directory in your PATH to run it from anywhere:

```bash
sudo cp phone /usr/local/bin/phone
```
4. Run the application using the following command if not in the PATH:

```bash
./phone
```
5. Run the application using the following command if in the PATH:

```bash
phone
```

## Why sudo is needed:

The application requires sudo to run commands that need elevated privileges, such as creating directories and files in system-protected locations (e.g., bin). It also ensures that the password file and database file have the correct permissions to prevent unauthorized access.

<br>

## Screenshots:

<p>
    <img alt="PhoneBook CLI" src="https://img.shields.io/badge/PhoneBook-CLI-blue">
</p>
<br>

## License:

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgment:

Created by Ranger (Dec 2024) Version 1.0.0
Modified by David Keane (Dec 31st 2024) Version 2.0.1

Feel free to customize the content as needed.

