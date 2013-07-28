#!/usr/bin/python
# -*- coding: utf-8 -*-
from json import load
from urllib2 import urlopen
import datetime
from shabb_details import ShabbCalendarDetails


def next_weeks_ltd(zipcode, lim):
    return next_weeks(zipcode)[0:lim]


# monday 0 sunday 6

def get_current_day():
    return datetime.datetime.today().weekday()


def get_next_fri_sat_dates():
    today = datetime.date.today()
    FRI = 4
    SAT = 5
    next_fri = today + datetime.timedelta(days=(FRI - today.weekday())
            % 7)
    next_sat = today + datetime.timedelta(days=(SAT - today.weekday())
            % 7)
    return (next_fri, next_sat)


def get_next_weekend_dates(next_fri, next_sat, num_total):
    next_wknds = []
    next_wknds.append((next_fri, next_sat))
    for i in range(num_total - 1):
        next_wknds.append((next_fri + datetime.timedelta(weeks=i + 1),
                          next_sat + datetime.timedelta(weeks=i + 1)))

    return next_wknds


# 11:00 am -> 11:45 am, 12:00 pm -> 12:45 pm
# 1:00 pm -> 10:00pm

def get_times_quarters():
    quarters = []
    quarters.append('11:00 am')
    quarters.append('11:15 am')
    quarters.append('11:30 am')
    quarters.append('11:45 am')
    quarters.append('Noon')
    quarters.append('12:15 pm')
    quarters.append('12:30 pm')
    quarters.append('12:45 pm')
    for hour in range(1, 10):
        quarters.append(str(hour) + ':00 pm')
        quarters.append(str(hour) + ':15 pm')
        quarters.append(str(hour) + ':30 pm')
        quarters.append(str(hour) + ':45 pm')
    quarters.append('10:00 pm')
    return quarters


def get_days_of_week():
    days = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        ]
    return days


# noon
# 1pm -> 11 pm
# midnight
# 1 am -> 11 am

def get_deadline_times():
    full_day = []
    full_day.append('noon')
    for hr in range(1, 12):
        full_day.append(str(hr) + ':00 pm')
    full_day.append('midnight')
    for hr in range(1, 12):
        full_day.append(str(hr) + ':00 am')
    return full_day
