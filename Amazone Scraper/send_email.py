import smtplib
import random
from datetime import datetime

MY_EMAIL = "your_email"
PASSWORD = "your_password or your_app_password"
RECEIVERS_EMAIL = "receivers_email"


def send_alert_email(price):
    try:
        # Add your own email provider server's information and TLS port
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVERS_EMAIL,
                msg=f"The product price is now ${price}, below your targeted price. Buy Now!"
            )
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error in sending mail: {e}")
