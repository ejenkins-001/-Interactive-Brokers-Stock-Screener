# Interactive Brokers Stock Screener

This project contains a script that connects to the Interactive Brokers (IB) platform using the `ib_insync` library and analyzes the historical data of the top 1000 stocks listed in the Nasdaq stock exchange. It detects buy signals for each stock and sends an SMS alert when a buy signal is detected.

## Requirements

- Python 3.x
- ib_insync library
- pandas
- matplotlib
- smtplib

You can install the required libraries using the following command:

```bash
pip install ib_insync pandas matplotlib

## Usage

1. Replace the "sms_gateway" variable in the script with the actual phone number and SMS gateway you wish to use.
2. Replace the "from_email" and "from_password" variables in the `send_email_to_sms` function with your Gmail email address and app password, respectively.
3. Make sure you have a CSV file containing the top 1000 stock symbols from the Nasdaq stock exchange, and update the path to the file in the `stocks_df` variable in the script.
4. Run the script:

Replace "your_script_name.py" with the name of your script file.

## Features

- Connects to the Interactive Brokers platform using the `ib_insync` library.
- Analyzes historical data for the top 1000 stocks listed on the Nasdaq stock exchange.
- Calculates various metrics, such as moving averages and bar sizes, to detect buy signals.
- Sends SMS alerts when a buy signal is detected.

## License

This project is licensed under the [MIT License](LICENSE).
