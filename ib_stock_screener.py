import time
from ib_insync import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

def send_email_to_sms(subject, body, to_email):
    from_email = "your_email@example.com"
    from_password = "your_email_password"
    
    # Create the message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", e)

def get_historical_data(stock_symbol):
    stock_contract = Stock(stock_symbol, 'SMART', 'USD')

    bars = ib.reqHistoricalData(
        stock_contract,
        endDateTime='',
        durationStr='30 D',
        barSizeSetting='1 day',
        whatToShow='TRADES',
        useRTH=True,
        formatDate=1
    )

    if bars:
        dates = [bar.date for bar in bars]
        opens = [bar.open for bar in bars]
        highs = [bar.high for bar in bars]
        lows = [bar.low for bar in bars]
        closes = [bar.close for bar in bars]

        df = pd.DataFrame({'Date': dates, 'Open': opens, 'High': highs, 'Low': lows, 'Close': closes})
        df['18_MA'] = df['Close'].rolling(window=18).mean()
        df['Body'] = abs(df['Close'] - df['Open'])
        df['Avg_4_Bodies'] = df['Body'].rolling(window=4).mean() * 1.33
        df['MA_Direction'] = (df['18_MA'].shift(1) <= df['18_MA']) & (df['18_MA'].shift(2) > df['18_MA'].shift(1))   
        df['Signal_Index'] = df.index.where((df['MA_Direction'].shift(1)) & (df['Close'] > df['Open']) & (df['Body'] > df['Avg_4_Bodies'].shift(1)), None)
        df['Previous_Signal'] = df['Signal_Index'].shift(1).ffill()
        df['Signal'] = (df['Signal_Index'].notnull()) & (df['Signal_Index'] != df['Previous_Signal'])
   
        #df['Signal'] = (df['MA_Direction'].shift(1)) & (df['Close'] > df['Open']) & (df['Body'] > df['Avg_4_Bodies'].shift(1))

        today = df.iloc[-1]

        if today['Signal']:
            print(f"Today's buy signal for {stock_symbol}: {today['Signal']}")
            
            # Send SMS alert
            sms_gateway = "recipient_phone_number@sms_gateway.com"  # Replace with the actual phone number and SMS gateway
            send_email_to_sms(subject=f"Buy signal for {stock_symbol}",
                              body=f"A buy signal for {stock_symbol} has been detected today.",
                              to_email=sms_gateway)
            print("SMS alert sent.")
        else:
            print(f"No buy signal for {stock_symbol} today.")            

    else:
        print(f"No historical data is available for {stock_symbol}")

stocks_df = pd.read_csv('nasdaq_screener_1680682414722.csv')
top_1000_stocks = stocks_df['Symbol'].tolist()

def main():
    try:
        print("Connected to IB")
                
        for stock_symbol in top_1000_stocks:
            get_historical_data(stock_symbol)

        print("Exiting the program")
        ib.disconnect()

    except Exception as e:
        print("An exception occurred:", e)
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
