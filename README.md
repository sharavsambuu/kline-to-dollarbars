# kline-to-dollarbars

    Just a simple dollarbar generation script from the klines with lower granularities like 1m or 5m etc


# prepare environment

    virtualenv -p python3.9 env && source env/bin/activate && pip install -r requirements.txt


# klines requirements

    csv file with lower granularity must have following columns

    datetime (ie 2018-01-12 06:00:00 etc)
    Open
    High
    Low
    Close
    Volume


# usage

    python generate_dollarbar.py <klines_path.csv> <dollar amount>

    python generate_dollarbar.py /home/sambu/data/BTCUSDT.csv 13000000


    

