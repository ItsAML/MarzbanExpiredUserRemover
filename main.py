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

# Create a reusable session
session = requests.Session()

def get_access_token(username, password):
    url = f'https://{DOMAIN}:{PORT}/api/admin/token'
    data = {
        'username': username,
        'password': password
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
    url = f'https://{DOMAIN}:{PORT}/api/users?status=expired'
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

def remove_expired_users(access_token, exp_user):
    url = f'https://{DOMAIN}:{PORT}/api/user/{exp_user}'
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
        logging.error(f'Error occurred while modifying user data limit: {e}')
        return False

if __name__ == "__main__":
    access_token = get_access_token(USERNAME, PASSWORD)
    if access_token:
        users_list = get_users_list(access_token)
        if users_list:
            expired_users = []
            for user in users_list.get('users', []):
                match = re.search(r"'username'\s*:\s*'(\w+)'", str(user))
                if match:
                    expired_users.append(match.group(1))

            # Count and print the number of expired users
            num_expired_users = len(expired_users)
            logging.info(f'Total expired users: {num_expired_users}')

            for i in expired_users:
                if remove_expired_users(access_token, i):
                    logging.info(f'User {i} has been successfully removed.')
                else:
                    logging.error(f'Failed to remove user {i}')

            logging.info("All expired users have been processed.")

# @AMLDevelopment in Telegram
# Github : https://github.com/itsAML
