"""Extra Hard Starting Project"""
import smtplib
import datetime as dt
import random
import pandas

"""Task1. Update the birthdays.csv"""
MY_EMAIL = "akdjsjhsk@gmail.com"
PASSWORD = "jjhelulseuilwe"
"""Task:2. Check if today matches a birthday in the birthdays.csv"""
now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday = birthday_dict[today_tuple]
    """Task:3. If step 2 is true, pick a random letter from letter templates and replace the 
    [NAME] with the person's actual name from birthdays.csv"""
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_choice:
        content = letter_choice.read()
        valid_letter = content.replace("[NAME]", birthday["name"])
    """Task:4. Send the letter generated in step 3 to that person's email address."""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday["email"],
                            msg=f"subject: Happy Birthday\n\n{valid_letter}")
