# This programe will output the number of days, months and weeks left in your life. Considering that you will live till 90 years age

from datetime import datetime

birth_year, birth_month, birth_day = int(input("Enter your year of birth: ")), int(
    input("Enter your month of birth: ")), int(input("Enter your date of birth: "))

# provides the currennt date
now = datetime.now()

current_year, current_month, current_day = int(now.strftime(
    "%Y-%m-%d")[0:4]), int(now.strftime("%Y-%m-%d")[5:7]), int(now.strftime("%Y-%m-%d")[9:11])

age = current_year - birth_year

months_left, weeks_left, days_left = (
    90 - age) * 12, ((90 - age) * 12) * 4, (((90 - age) * 12) * 4) * 7

print(
    f"You have {months_left} months, {weeks_left} week, and {days_left} days remaining")
