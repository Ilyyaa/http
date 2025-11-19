import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('localhost', version=3)
print(response.offset)
print(ctime(response.tx_time))