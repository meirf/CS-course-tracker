#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import urllib
import os
import jinja2
import webapp2

from course_listing import courses
from course_listing import adv_courses
from operator import itemgetter
from url_manipulation.url_decode import get_url_param_mappings


JINJA_ENVIRONMENT = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                       extensions=['jinja2.ext.autoescape'])

DEFAULT_MEAL_SCHED_NAME = 'default_meal_sched'

class MainPage(webapp2.RequestHandler):

    def get(self):       

        meal_sched_name = self.request.get('meal_sched_name',
                DEFAULT_MEAL_SCHED_NAME)

        template_values = {
            'guestbook_name' : 'gbk_name',
            'core_courses' : courses,
            'adv_courses': sorted(list(adv_courses), key=itemgetter(1, 2)),
            'meal_sched_name': urllib.quote_plus(meal_sched_name),
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class MealSchedule(webapp2.RequestHandler):

    def post(self):

        meal_sched_name = self.request.get('meal_sched_name',
                DEFAULT_MEAL_SCHED_NAME)

        query_params = {'meal_sched_name': meal_sched_name}
        self.redirect('/?' + urllib.urlencode(query_params))

class Verify2Google(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('google-site-verification: google17bd46c295eec9f7.html')

class Test(webapp2.RequestHandler):

    def get(self):
        return webapp2.Response(str(get_url_param_mappings(str(self.request))))

application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/taken', Test),
     ('/google17bd46c295eec9f7.html', Verify2Google),
     ('/test', Test)
     ], debug=True)