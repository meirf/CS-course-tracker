from json import load
from urllib2 import urlopen
from datetime import datetime
from shabb_details import ShabbCalendarDetails

def next_weeks_ltd(zipcode, lim):
    return next_weeks(zipcode)[0:lim]

def next_weeks(zipcode):
    upcoming_sh_json = get_all_upcoming_shabs(zipcode)
    upcoming_shabs = []
    now = datetime.now()
    for index, item in enumerate(upcoming_sh_json):
        if index%2 == 0:
            shab = convert2shab_obj(upcoming_sh_json[index],    
                                    upcoming_sh_json[index+1])
            
            if now.month < shab.fri_mon or (now.month == shab.fri_mon and now.day<=shab.fri_day): 
                upcoming_shabs.append(shab)    

    return upcoming_shabs

def convert2shab_obj(friday_dict, saturday_dict):
    fri_ti = datetime.strptime(friday_dict['date'].split('T')[0], '%Y-%m-%d')
    sat_ti = datetime.strptime(saturday_dict['date'].split('T')[0], '%Y-%m-%d') 
    shab = ShabbCalendarDetails(fri_ti.month, fri_ti.day, fri_ti.year,
                                sat_ti.month, sat_ti.day, sat_ti.year)
    shab.set_candle_time(friday_dict['title'][-7:])
    shab.set_havdalah_time(saturday_dict['title'][-7:])
    return shab

def get_all_upcoming_shabs(zipcode):
    this_mo, this_yr = this_month_year()
    next_mo, next_yr = next_month_year(this_mo, this_yr)
    items_now = get_all_upcoming_items(this_mo, this_yr, 90210)
    items_next = get_all_upcoming_items(next_mo, next_yr, 90210)
    return items_now + items_next

def get_all_upcoming_items(month, year, zipcode):
     return get_shab_from_json(get_url(month, year, zipcode))

def get_shab_from_json(url):
    return load(urlopen(url))['items']

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