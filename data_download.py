import pandas as pd
from binance.client import Client
import datetime as dt

# client configuration
api_key = 'https://api.binance.com/api/v3/klines' 
api_secret = '128.0.0.0.1'
client = Client(api_key, api_secret)

symbol = "CREAMBUSD"
interval='1h'
Client.KLINE_INTERVAL_15MINUTE 
klines = client.get_historical_klines(symbol, interval, "1 Jan,2021")
data = pd.DataFrame(klines)
 # create colums name
data.columns = ['open_time','open', 'high', 'low', 'close', 'volume','close_time', 'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']
            
# change the timestamp
data.index = [dt.datetime.fromtimestamp(x/1000.0) for x in data.close_time]
data.to_csv(symbol+'.csv', index = None, header=True)
