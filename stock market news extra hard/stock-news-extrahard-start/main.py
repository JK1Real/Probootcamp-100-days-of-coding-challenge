import smtplib
import vonage
import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_stock_api_key = "3SERQ199W0725HYU"
my_stock_news_api_key = "9f70a6e2f7ab4389b8ad5f3d17e94b3f"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_url = "https://www.alphavantage.co/query"

parameters = {'function':'TIME_SERIES_DAILY',
               'symbol':STOCK,
                'apikey':my_stock_api_key
                }
response1 = requests.get(url=stock_url, params=parameters)
data = response1.json()["Time Series (Daily)"]

data = {date:float(info['2. high']) for date, info in list(data.items())[:2]}
print(data)
values = data.values()
list_values=list(values)
print(list_values) 

percentage_change = ((list_values[0]-list_values[1])/list_values[1])*100
print(percentage_change)

news_url = "https://newsapi.org/v2/everything"
parameters = {
            "q":COMPANY_NAME, 
            "from":"2024-05-10",
            "sortBy":"publishedAt",
            "apiKey":my_stock_news_api_key}
response = requests.get(url=news_url, params=parameters)

news_title =    response.json()
#news_content =  [response.json()["articles"][0]['content'] for i in range(0,1)]
print(news_title)
# print(news_content)

if percentage_change>5: 
    pass
elif percentage_change<-5:
    pass

def send_sms(text):
    client = vonage.Client(key="b5e49697", secret="m17lpyyvRe1wWLTS")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "917034669451",
            "text": "A text message sent using the Nexmo SMS API",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")