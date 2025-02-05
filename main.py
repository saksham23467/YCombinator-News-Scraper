import yfinance as yf

aapl = yf.Ticker("AAPL")

data = aapl.history()
print(data.head())

# print(data.at_time())
# get all stock info
