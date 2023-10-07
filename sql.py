import sqlite3

# Database Location
db_location = "/var/lib/marzban/db.sqlite3"

# Connect to your SQLite database
conn = sqlite3.connect(db_location)
cursor = conn.cursor()

def delete_all_users():
    try:
        cursor.execute("DELETE FROM users WHERE status IN ('expired', 'limited', 'disabled')")
        conn.commit()
        print("Users with 'expired', 'limited', and 'disabled' statuses deleted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {str(e)}")

def delete_expired_users():
    try:
        cursor.execute("DELETE FROM users WHERE status = 'expired'")
        conn.commit()
        print("Expired users deleted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {str(e)}")

def delete_limited_users():
    try:
        cursor.execute("DELETE FROM users WHERE status = 'limited'")
        conn.commit()
        print("Limited users deleted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {str(e)}")

def delete_disabled_users():
    try:
        cursor.execute("DELETE FROM users WHERE status = 'disabled'")
        conn.commit()
        print("Disabled users deleted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {str(e)}")

while True:
    print("Menu: (Developed By AML)")
    print("1. Delete all users with 'expired', 'limited', or 'disabled' status")
    print("2. Delete expired users")
    print("3. Delete limited users")
    print("4. Delete disabled users")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        delete_all_users()
    elif choice == '2':
        delete_expired_users()
    elif choice == '3':
        delete_limited_users()
    elif choice == '4':
        delete_disabled_users()
    elif choice == '5':
        print("Exiting the script.")
        conn.close()
        break
    else:
        print("Invalid choice. Please select a valid option.")
