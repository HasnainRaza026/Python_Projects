import smtplib
import random
from datetime import datetime

MY_EMAIL = "your_email"
PASSWORD = "your_password or your_app_password"
RECEIVERS_EMAIL = "receivers_email"


def send_motivation_email():
    week_day = datetime.now().weekday()
    if week_day == 0:
        try:
            with open("quotes.txt", encoding="utf-8") as file:
                quotes = file.readlines()
                quote = random.choice(quotes)
                print(quote)
        except Exception as e:
            print(f"Error reading text file: {e}")
            return

        try:
            # Add your own email provider server's information and TLS port
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECEIVERS_EMAIL,
                    msg=f"Subject:Monday Motivation\n\n{quote}"
                )
                print("Email sent successfully.")
        except Exception as e:
            print(f"Error in sending mail: {e}")


send_motivation_email()
