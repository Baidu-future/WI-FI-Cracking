import pandas as pd
import datetime

ts1 = pd.Timestamp('2021-01-01 10:20:30')
ts2 = pd.Timestamp('2021-01-01 10:00:00')
dt1 = datetime.datetime.fromtimestamp(ts1.timestamp())
dt2 = datetime.datetime.fromtimestamp(ts2.timestamp())

dt1 > dt2
# 输出 True