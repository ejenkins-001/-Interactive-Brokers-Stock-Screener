# Interactive Brokers Stock Screener

This project contains a script that connects to the Interactive Brokers (IB) platform using the `ib_insync` library and analyzes the historical data of stocks listed in the Nasdaq stock exchange. It detects buy signals for each stock and sends an SMS alert when a buy signal is detected.

## Requirements

- Python 3.x
- ib_insync library
- pandas
- matplotlib
- smtplib
- Trader Workstation (TWS) or IB Gateway
- Market data subscription: Cboe One - Trader Workstation

You can install the required libraries using the following command:

pip install ib_insync pandas matplotlib

```bash
pip install pandas ib_insync

Download the "nasdaq_screener_1680682414722.csv" file from the repository's main page by clicking on it and then clicking the "Download" button. Save it in the same directory as your script.

## Usage

1. Before running the script, make sure that Trader Workstation or IB Gateway is open and running on your machine. The script connects to TWS or IB Gateway using the TWS API, so it requires TWS or IB Gateway to be running and configured correctly.
2. Ensure that the socket port in TWS settings matches the port specified in the script (usually 7497 for live accounts or 7496 for paper trading accounts). To check or change the socket port, go to the settings menu in Trader Workstation and look for the API settings.
3. Replace the "sms_gateway" variable in the script with the actual phone number and SMS gateway you wish to use.
4. Replace the "from_email" and "from_password" variables in the `send_email_to_sms` function with your email address and app password, respectively.
5. Make sure you have a CSV file containing stock symbols from the Nasdaq stock exchange, and update the path to the file in the `stocks_df` variable in the script.
6. Run the script using the following command: ib_stock_screener.py

## Features

- Connects to the Interactive Brokers platform using the `ib_insync` library.
- Analyzes historical data for stocks listed on the Nasdaq stock exchange.
- Calculates various metrics, such as moving averages and bar sizes, to detect buy signals.
- Sends SMS alerts when a buy signal is detected.

## Market Data Subscription
To run this script, you will need the following market data subscription from Interactive Brokers: Cboe One - Trader Workstation. This subscription provides the necessary data for the script to function correctly.

To subscribe, log in to your Interactive Brokers account, go to the "Account Management" section, and navigate to the "Market Data Subscriptions" page. Find "Cboe One - Trader Workstation" in the list of available subscriptions and follow the instructions to subscribe.

## Connecting to a Demo Account
By default, the script connects to a live trading account using port 7497. If you want to use a demo account, you will need to change the port number to 7496.

Update the following line in the script:

python
Copy code
ib.connect('127.0.0.1', 7497, clientId=1)
to

python
Copy code
ib.connect('127.0.0.1', 7496, clientId=1)
Keep in mind that the data received from a demo account might not be as accurate or up-to-date as a live trading account.

## Disclaimer

This script is for educational purposes only. The user is responsible for any potential risks and losses associated with using this script in a live trading environment. Always test your strategies and algorithms with historical data and paper trading before using them in a live environment.
