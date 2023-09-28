# Marzban Expired Users Remover

Remove all the expired users easily by just runing this script

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Linux](#Linux)
- [Windows](#windows)
- [PHP](#php)

Make Sure To Change these variables before runing the script.
```python
DOMAIN = 'YOUR_DOMAIN'
PORT = 443
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
```

## About

This script is designed to automate the management of users in marzban api. It securely logs in to an admin panel, retrieves a list of expired users, and removes them from the system, all while providing detailed logging for each operation. It is a valuable tool for efficiently managing user accounts in a web-based environment.

Feel free to modify and expand upon this description to better suit your project's specific goals and context.

## Getting Started

First of all you need to enable Marzban API which you can use this command below
```bash
echo 'DOCS=True' | sudo tee -a /opt/marzban/.env
```
or manually open the .env file with this command
```bash
nano /opt/marzban/.env
```
and then manually add this line to the file
```python
DOCS=True
```
### Prerequisites
Python 3.0+ with requests library required. you cant run the script on python 2.0
### Linux
```bash
# Clone the Repository
git clone https://github.com/ItsAML/MarzbanExpiredUserRemover.git

# Change Directory
cd MarzbanExpiredUserRemover

# Install pip (if not already installed)
wget -qO- https://bootstrap.pypa.io/get-pip.py | python3 -

# Install Dependencies
python3 -m pip install -r requirements.txt

# Run the Script
python3 main.py
```
### Windows
```bash
# Clone the Repository
git clone https://github.com/ItsAML/MarzbanExpiredUserRemover.git

# Navigate to the Repository Directory
cd MarzbanExpiredUserRemover

# Install Python (if not already installed)
# Download and install Python from https://www.python.org/downloads/
# Ensure you add Python to your system's PATH during installation

# Install Dependencies
pip install -r requirements.txt

# Run the Script (replace 'flow.py' with the actual script filename)
python main.py
```
### PHP
if you wanna run the script with php simply change the variables inside the php file and then run the script
```php
// Constants
define('DOMAIN', 'YOUR_DOMAIN');
define('PORT', 443);
define('USERNAME', 'YOUR_USERNAME');
define('PASSWORD', 'YOUR_PASSWORD');
```
```bash
# Navigate to the Script Directory
cd MarzbanExpiredUserRemover

# Run the PHP Script (make sure to change the variables before runing the script so you wont run into any issue)
php main.php

```

