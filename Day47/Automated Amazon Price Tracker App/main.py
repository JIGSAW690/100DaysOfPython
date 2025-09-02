import bs4, os, requests, smtplib

BUY_PRICE = 80.00
ENDPOINT = os.environ.get('ENDPOINT')
response = requests.get(url=ENDPOINT)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())
price = float(soup.find(class_='a-offscreen').getText().split('$')[1])
#print(price)

title = soup.find(id='productTitle').getText().strip()

if price < BUY_PRICE:
    message = f"{title} is on sale for price: {price}$"
    with smtplib.SMTP(os.environ.get('SMTP_ADDRESS'), port=587) as connection:
        connection.starttls()
        connection.login(os.environ.get('EMAIL'), os.environ.get('PASS'))
        connection.sendmail(
            from_addr=os.environ.get('EMAIL'),
            to_addrs=os.environ.get('EMAIL'),
            msg=f"Subject: Amazon Price Alert\n\n{message}\n".encode('utf-8')
        )
