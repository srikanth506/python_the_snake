import datetime as dt
import pytz
# utcnow = print(dt.datetime.now(pytz.UTC))
# utcnow = print(utc .astimezone(pytz.timezone("US/Eastern")))
for tz in pytz.all_timezones:
    print(tz)