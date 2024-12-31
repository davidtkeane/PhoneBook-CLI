# PhoneBook CLI Application

## Github

[![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-blue)](https://github.com/davidtkeane/PhoneBook-CLI)


![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) 
![Version](https://img.shields.io/badge/Version-2.0-orange)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/PhoneBook-CLI?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/davidtkeane/PhoneBook-CLI?authorFilter=davidtkeane)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/PhoneBook-CLI?style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/davidtkeane)

### Other Scripts from me.

[![CodeTime Badge](https://img.shields.io/endpoint?style=social&color=222&url=https%3A%2F%2Fapi.codetime.dev%2Fshield%3Fid%3D26388%26project%3D%26in=0)](https://codetime.dev)

[![Gmail Multi-Account CLI](https://img.shields.io/badge/Gmail-Multi--Account%20CLI-green?logo=gmail&logoColor=white&labelColor=EA4335)](https://github.com/davidtkeane/gmail-multi-cli)
[![Gmail CLI](https://img.shields.io/badge/Gmail-CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=gray)](https://github.com/davidtkeane/gmail-multi-cli)
[![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-blue?style=flat&logo=gmail&logoColor=white&labelColor=red)](https://github.com/davidtkeane/gmail-multi-cli)
[![Sleep CLI](https://img.shields.io/badge/Sleep-CLI-blue)](https://github.com/davidtkeane/Sleep-CLI)
[![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-blue)](https://github.com/davidtkeane/PhoneBook-CLI)
[![Kermit ScreenSaver](https://img.shields.io/badge/kermit-screensaver-blue)](https://github.com/davidtkeane/kermit)

![Discord](https://img.shields.io/discord/815701213827301396)

<div align="left">
<a href="https://github.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://twitter.com/davidtkeane" target="_blank">
<img src=https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white alt=twitter style="margin-bottom: 5px;" />
</a>
<a href="https://linkedin.com/in/sami-hindi-b31435248/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
<br>
<p align="left">
  <img src="https://img.shields.io/badge/Microsoft-Windows%2011-0078D6?logo=windows&logoColor=0078D6&labelColor=white" alt="Windows 11">
  <img src="https://img.shields.io/badge/Apple-macOS-000000?logo=apple&logoColor=white&labelColor=black" alt="macOS">
  <img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&labelColor=white" alt="Linux">
</p>
</div>

![Buy me a coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=davidtkeanek&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)

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

