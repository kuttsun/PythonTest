# https://kapibara-sos.net/archives/705

from influxdb import InfluxDBClient
import datetime

client = InfluxDBClient(host='', port='', database='')

# データベースの作成
client.create_database('')
client.create_retention_policy("mypolicy", "100w", 1, default=True)

# データの書き込み
data_ = [
    {
        'fields':
        {
            'metric1': 1.0,
            'metric2': -1
        },
        'measurement': 'testms',
        'time': datetime.datetime.utcnow(),
        'tags': {'cat1': 'aaa'}
    },
]
res= client.write_points(data_)
print(res)
