from time import time
import pyupbit 
import time
access = "ozh77triaynP3bLVcBfDa3eywe57ksBSKxuBNnte"
secret = "KiBBAMxNS5ex81cEfvpU0G43lVHIfmp1jONa4CUb"
upbit = pyupbit.Upbit(access, secret) 


tickers = pyupbit.get_tickers("KRW")

for ticker in tickers:
    if ticker == "KRW-BTC":
        df = pyupbit.get_ohlcv(ticker, interval="day")   
        print(df)
        break
# my_balances = upbit.get_balances()

# for coin_balance in my_balances:
#     ticker =coin_balance['currency']
#     if ticker == "KRW" or ticker == "TRX" or ticker == "APENFT":
#         continue
#     print(ticker, coin_balance['balance'], coin_balance['avg_buy_price'])

#     nowPrice = pyupbit.get_current_price("KRW-" + ticker)
#     print(nowPrice)

#     avg_price = float(coin_balance['avg_buy_price']) 

#     revenu_rate = (nowPrice - avg_price) / avg_price * 100.0
#     print(revenu_rate)

# from pyupbit.exchange_api import Upbit
# Coins = pyupbit.get_tickers(fiat="KRW")

# for coin in Coins:
#     print(coin, pyupbit.get_current_price(coin))
#     time.sleep(0.1)

#     if coin == "KRW-BTC" or coin == "KRW-TRX":
#         Upbit.buy_market_order(coin, 5000)
#         print("Buy Done", coin)