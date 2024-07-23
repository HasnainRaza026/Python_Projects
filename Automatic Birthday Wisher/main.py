import json
import smtplib
import random
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Using environment variables for sensitive information
# Add your own email and password
MY_EMAIL = os.getenv("MY_EMAIL", "your_email")
PASSWORD = os.getenv("PASSWORD", "your_password or your_app_password")

LETTERS = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt"
]


# Load birthday data from JSON file
def load_birthdays(file_path):
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        logging.error(f"Error opening the JSON file: {e}")
        return None


# Check if today is someone's birthday
def check_birthday(data):
    today = datetime.now()
    for key, value in data.items():
        if value["month"] == today.month and value["day"] == today.day:
            return key
    return None


# Send birthday email
def send_birthday_letter(key, data):
    try:
        letter = random.choice(LETTERS)
        with open(letter, encoding="utf-8") as t:
            text = t.read()
            text = text.replace("[NAME]", key)
    except Exception as e:
        logging.error(f"Error opening the letter file: {e}")
        return

    try:
        # Add your own email provider server's information and TLS port
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=data[key]["email"],
                msg=f"Subject:Happy Birthday\n\n{text}"
            )
            logging.info("Email sent successfully.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except Exception as e:
        logging.error(f"Error in sending mail: {e}")


def main():
    data = load_birthdays("birthdays.json")
    if data:
        key = check_birthday(data)
        if key:
            send_birthday_letter(key, data)
        else:
            logging.info("No birthdays today.")
    else:
        logging.error("Failed to load birthday data.")


if __name__ == "__main__":
    main()
