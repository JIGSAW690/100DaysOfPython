##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random

email = "debkankan.b@gmail.com"
app_password = "tvctwwvkpxhxkjgp"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
dataframe = pandas.read_csv("C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/birthdays.csv")
data_dict = dataframe.to_dict(orient='records')
#print(data_dict)
month_today = dt.datetime.today().month
day_today = dt.datetime.today().day
letter_files = ["C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/letter_templates/letter_1.txt", "C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/letter_templates/letter_2.txt", "C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day32/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/letter_templates/letter_3.txt"]
new_mail_list = []
new_mail = ""
for item in data_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if item['month'] == month_today and item['day'] == day_today:
        with open(random.choice(letter_files), 'r') as file:
            content = file.readlines()
            #print(content)
            new_mail_list = [line.replace('[NAME]', item['name']) for line in content]
            new_mail = "".join(new_mail_list)
            #print(new_mail)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=app_password)
            connection.sendmail(
                from_addr=email,
                to_addrs=item['email'],
                msg=f"Subject:MANY MANY HAPPY RETURNS OF THE DAY!!\n\n{new_mail}"
            )










