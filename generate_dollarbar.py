#%%
import os
import csv
import sys
import time
import math
import glob
import zipfile
import pandas as pd
import numpy  as np
from collections import deque


#%%


#%%
csv_file_path = sys.argv[1]
dollar_amount = sys.argv[2]


if not csv_file_path:
    print("please supply csv file")
    sys.exit()

if not os.path.exists(csv_file_path):
    print(f"{csv_file_path} file doesn't exists.")
    sys.exit()

if not dollar_amount:
    print("please supply dollar amount")
    sys.exit()


csv_base_name = os.path.basename(csv_file_path)
dollar_amount = float(dollar_amount)

#%%
print(f"reading {csv_base_name}")
df = pd.read_csv(csv_file_path, parse_dates=True, index_col=0)

df['MidPrice'] = (df['High']+df['Low'])/2.0

print(df)

#%%
df.info(verbose=True)

#%%


#%%


#%%
dollar_bars         = []
running_volume      = 0.0
running_dollar      = 0.0
running_high        = 0.0
running_low         = math.inf
last_price          = 0.0


for idx in range(0, len(df)):
    row              = df.iloc [idx]
    timestamp        = df.index[idx]
    price            = row['MidPrice']
    quantity         = row['Volume'  ]
    running_high, running_low = max(running_high, price), min(running_low, price)

    dollar_volume = quantity*price

    if dollar_volume+running_dollar>=dollar_amount:
        bar_timestamp = timestamp
        open_price    = last_price
        high_price    = running_high
        low_price     = running_low
        close_price   = price
        volume        = running_volume+quantity
        dollar        = running_dollar+dollar_volume
        new_bar       = [bar_timestamp, open_price, high_price, low_price, close_price, volume, dollar]
        print(new_bar)
        dollar_bars.append(new_bar)
        running_volume, running_dollar, running_high, running_low, last_price = 0.0, 0.0, 0.0, math.inf, price
    else:
        running_volume += quantity
        running_dollar += dollar_volume


#%%
dollarbar_df = pd.DataFrame(dollar_bars, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dollar'])
dollarbar_df = dollarbar_df.set_index("timestamp")
dollarbar_df.index = pd.DatetimeIndex(dollarbar_df.index)

print(dollarbar_df)


#%%
os.makedirs("./data/", exist_ok=True)

#%%
csv_base_name = os.path.splitext(csv_base_name)[0]
output_path = f"./data/{csv_base_name}-dollarbar-{int(dollar_amount)}.csv"
print(f"saving result to {output_path}")
dollarbar_df.to_csv(output_path, header=True)

#%%
print("DONE.")


#%%


#%%


#%%


#%%

