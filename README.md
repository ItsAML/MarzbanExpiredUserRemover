# Marzban Expired Users Remover

Remove all the expired users easily by just runing this script

```python
DOMAIN = 'YOUR_DOMAIN'
PORT = 443
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
```


## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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


### Installation

Step-by-step instructions on how to install and configure your project.

## Usage

Provide examples and instructions on how to use your project. Include code snippets and explanations if necessary.

## Configuration

Explain any configuration options or settings that users might need to customize.

## Contributing

Explain how others can contribute to your project. Include guidelines for code contributions, bug reporting, and feature requests.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Mention any third-party libraries, tools, or resources you used or were inspired by in your project.

You can also include badges (e.g., build status, license, etc.) and contact information as needed.

