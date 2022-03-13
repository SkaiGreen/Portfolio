#importing our libraries

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import time
import datetime
import smtplib


def current_value():

    #Adding the website

    URL = 'https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQK9DK5/ref=sr_1_5?keywords=apple&qid=1647200026&sr=8-5'
    #URL = input("Enter the Amazon orodyct URL here:")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-622e432e-2e3825a718eff40c1593fd80"}

    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id = 'productTitle').get_text().strip()
    price = soup2.find(id = 'price_inside_buybox').get_text()
    price = price.strip()[1:]

    #print(title)
    #print(price)
    today = datetime.date.today()
    csv_header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonScraper.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerow(data)

    df = pd.read_csv(r'AmazonScraper.csv')
    print(df)
    return price


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    # server.starttls()
    server.ehlo()
    server.login('skai.a.o.green@green-sky.org', 'xxxxxxxxxxxxxx')

    subject = "The laptop you want is below $2100! Now is your chance to buy!"
    body = "Mr Green, This is the moment we have been waiting for. Now is your chance to pick up the laptop of your dreams. Don't mess it up! Link here: https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQK9DK5/ref=sr_1_5?keywords=apple&qid=1647200026&sr=8-5&th=1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'skai.a.o.green@green-sky.org',
        msg

    )

if float(current_value()[2:]) < 400:
    send_mail()


while(True):
    current_value()
    time.sleep(86400)




