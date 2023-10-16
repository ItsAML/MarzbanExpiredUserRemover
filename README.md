# Marzban Expired Users Remover

Simplify user management by effortlessly purging expired users using this script.

## Table of Contents
- [About](#about)
- [Prerequisites](#prerequisites)
- [Linux](#Linux)
- [Windows](#windows)
- [PHP](#php)

Make Sure To Change these variables before runing the script.
```python
DOMAIN = 'YOUR_DOMAIN'
PORT = 'YOUR_PORT'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
USER_STATUS = 'E'  # Set E for Expired, L for Limited, D for Disabled, A for Active
HTTPS = True  # Set this to True for HTTPS, False for HTTP
```

## About

This script is designed to automate the management of users using marzban api. It securely logs in to an admin panel, retrieves a list of expired users, and removes them from the system, all while providing detailed logging for each operation. It is a valuable tool for efficiently managing user accounts in a web-based environment.

Feel free to modify and expand upon this description to better suit your project's specific goals and context.

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

# Run the Script
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
# Support This Project

If you find my GitHub repository helpful and would like to support my work, you can make a donation using the following cryptocurrencies:

- **USDT (TRC20):** TPXehJNLDqhHBAfs6v5KKHKXX4fZ3uhVGK
- **TRX (TRC20):** TPXehJNLDqhHBAfs6v5KKHKXX4fZ3uhVGK

Your contributions are greatly appreciated and will help me continue developing and maintaining this project. Thank you for your support! 🙌


