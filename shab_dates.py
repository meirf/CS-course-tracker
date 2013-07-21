from json import load
from urllib2 import urlopen
from datetime import datetime
from shabb_details import ShabbCalendarDetails

def next_weeks(n):
    list = []
    shab = ShabbCalendarDetails(1,2,3,4,5,6)
    shab.set_candle_time("pm")
    list.append(shab)
    return list

def get_url(month, year, zipcode):
    bare_url = "http://www.hebcal.com/hebcal/?v=1&cfg=json&c=on"
    url = bare_url+"&month=%d&year=%d&zip=%d" %(month, year, zipcode)
    return url

def this_month_year():
    now = datetime.now()
    return (now.month, now.year)

def next_month_year(month=this_month_year()[0], year=this_month_year()[1]):
    if month == 12:
        return (1, year+1)
    else: 
        return (month+1, year)