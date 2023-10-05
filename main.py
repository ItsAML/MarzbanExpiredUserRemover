import requests
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
DOMAIN = 'YOUR_DOMAIN'
PORT = 'YOUR_PORT'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
USER_STATUS = 'E'  # Set E for Expired, L for Limited, D for Disabled, A for Active
HTTPS = True  # Set this to True for HTTPS, False for HTTP

# Create a reusable session
session = requests.Session()

# Yay!
STATUS_MAPPING = {
    'E': 'Expired',
    'L': 'Limited',
    'D': 'Disabled',
    'A': 'Active'
}


def get_access_token(username, password):
    use_protocol = 'https' if HTTPS else 'http'
    url = f'{use_protocol}://{DOMAIN}:{PORT}/api/admin/token'
    data = {
        'username': USERNAME,
        'password': PASSWORD
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = session.post(url, data=data)
        response.raise_for_status()
        access_token = response.json()['access_token']
        logging.info(".:Logged in Successfully:.")
        return access_token
    except requests.exceptions.RequestException as e:
        logging.error(f'Error occurred while obtaining access token: {e}')
        return None


def get_users_list(access_token):
    use_protocol = 'https' if HTTPS else 'http'
    if USER_STATUS.upper() == 'E':
        url = f'{use_protocol}://{DOMAIN}:{PORT}/api/users?status=expired'
    elif USER_STATUS.upper() == 'L':
        url = f'{use_protocol}://{DOMAIN}:{PORT}/api/users?status=limited'
    elif USER_STATUS.upper() == 'D':
        url = f'{use_protocol}://{DOMAIN}:{PORT}/api/users?status=disabled'
    elif USER_STATUS.upper() == 'A':
        url = f'{use_protocol}://{DOMAIN}:{PORT}/api/users?status=active'
    else:
        logging.error(f'Invalid USER_STATUS: {USER_STATUS}')
        return None

    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        users_list = response.json()
        return users_list
    except requests.exceptions.RequestException as e:
        logging.error(f'Error occurred while retrieving users list: {e}')
        return None


def remove_users(access_token, user):
    use_protocol = 'https' if HTTPS else 'http'
    url = f'{use_protocol}://{DOMAIN}:{PORT}/api/user/{user}'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    try:
        response = session.delete(url, headers=headers)
        response.raise_for_status()
        user_details = response.json()
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f'Error occurred while removing user: {e}')
        return False


if __name__ == "__main__":
    access_token = get_access_token(USERNAME, PASSWORD)
    if access_token:
        users_list = get_users_list(access_token)
        if users_list:
            users = []
            for user in users_list.get('users', []):
                match = re.search(r"'username'\s*:\s*'(\w+)'", str(user))
                if match:
                    users.append(match.group(1))

            # Count and print the number of users based on USER_STATUS
            num_users = len(users)
            status_text = STATUS_MAPPING.get(USER_STATUS.upper(), 'Unknown')
            logging.info(f'Total {status_text} Users: {num_users} Found.')

            for i in users:
                if remove_users(access_token, i):
                    logging.info(f'User {i} has been successfully removed.')
                else:
                    logging.error(f'Failed to remove user {i}')

            logging.info(f'All {status_text} users have been processed.')

# @AMLDevelopment in Telegram
# Github : https://github.com/itsAML
