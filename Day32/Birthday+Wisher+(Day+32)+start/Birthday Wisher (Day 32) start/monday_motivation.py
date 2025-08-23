import datetime as dt
import smtplib
import random

#Monday --> 0
#Tuesday --> 1
#Sunday --> 6

email = "debkankan.b@gmail.com"
app_password = "tvctwwvkpxhxkjgp"

if dt.datetime.today().weekday() == 0:
    with open('quotes.txt', 'r') as f:
        contents = f.read().splitlines()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=app_password)
        connection.sendmail(
            from_addr=email,
            to_addrs="banerjeedebkankan@gmail.com",
            msg=f"Subject:MONDAY MOTIVATION!!\n\n{random.choice(contents)}"
        )