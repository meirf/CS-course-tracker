#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import urllib
import os
import jinja2
import webapp2

from random import randint
from mail_tool import Mailer
from google.appengine.api import users, urlfetch
from google.appengine.ext import ndb
from shab_dates import next_weeks_ltd
from shab_dates import get_times_quarters
from shab_dates import get_days_of_week
from shab_dates import get_deadline_times
from shab_dates import get_next_fri_sat_dates
from shab_dates import get_next_weekend_dates
from course_listing import courses

JINJA_ENVIRONMENT = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                       extensions=['jinja2.ext.autoescape'])

DEFAULT_MEAL_SCHED_NAME = 'default_meal_sched'


# We set a parent key on the 'Meals' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def meal_sched_key(meal_sched_name=DEFAULT_MEAL_SCHED_NAME):
    """Constructs a Datastore key for a MealSchedule entity with meal_sched_name."""

    return ndb.Key('MealSchedule', meal_sched_name)


class Meal(ndb.Model):

    """Models an individual MealSchedule entry with author, location, and date. """

    author = ndb.UserProperty()
    location = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):

    def get(self):       

        mail_list = ("meirfischer@gmail.com", "mf8191@aol.com")
        subject = "Your welcome" + str(randint(2,10000))
        mess = "Dear Bro[ette],"
        Mailer.send_mail(mail_list, subject, mess)

        meal_sched_name = self.request.get('meal_sched_name',
                DEFAULT_MEAL_SCHED_NAME)
        meals_query = \
            Meal.query(ancestor=meal_sched_key(meal_sched_name)).order(-Meal.date)
        meals = meals_query.fetch(3)

        nickname = ''
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            nickname = users.get_current_user().nickname()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        (fri, sat) = get_next_fri_sat_dates()
        upcoming_shab_dates = get_next_weekend_dates(fri, sat, 4)
        times = get_times_quarters()

        deadline_days = get_days_of_week()
        deadline_times = get_deadline_times()

        template_values = {
            'courses' : courses,
            'deadline_times': deadline_times,
            'deadline_days': deadline_days,
            'nickname': nickname,
            'times': times,
            'dates': upcoming_shab_dates,
            'meals': meals,
            'meal_sched_name': urllib.quote_plus(meal_sched_name),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class MealSchedule(webapp2.RequestHandler):

    def post(self):

        # We set the same parent key on the 'Meal' to ensure each Meal
        # is in the same entity group. Queries across the single entity group
        # will be consistent. However, the write rate to a single entity group
        # should be limited to ~1/second.

        meal_sched_name = self.request.get('meal_sched_name',
                DEFAULT_MEAL_SCHED_NAME)
        meal = Meal(parent=meal_sched_key(meal_sched_name))

        if users.get_current_user():
            meal.author = users.get_current_user()

        meal.location = self.request.get('location')
        meal.put()

        query_params = {'meal_sched_name': meal_sched_name}
        self.redirect('/?' + urllib.urlencode(query_params))

class Verify2Google(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('google-site-verification: google17bd46c295eec9f7.html')

class Photo(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('uploader.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication(
    [('/', MainPage), 
     ('/sign', MealSchedule),
     ('/google17bd46c295eec9f7.html', Verify2Google),
     ('/test', Photo)
     ], debug=True)
