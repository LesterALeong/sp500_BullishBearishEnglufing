import yfinance as yf

ticker = 'AAPL'
slack = yf.Ticker(str(ticker))

history = slack.history(period='max')

# Dataframe format
##print(history)

# CSV format
print(history.to_csv(str(ticker)+'.csv'))