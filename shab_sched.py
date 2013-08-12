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
    jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

    def get(self):       

        template_values = {
            'core_courses' : courses,
            'adv_courses': sorted(list(adv_courses), key=itemgetter(1, 2)),
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class Verify2Google(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('google-site-verification: google17bd46c295eec9f7.html')

class DisplayTakenTrackInfo(webapp2.RequestHandler):

    def get(self):
        taken_courses = str(get_url_param_mappings(str(self.request)).keys())
        return webapp2.Response(taken_courses)

application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/taken', DisplayTakenTrackInfo),
     ('/google17bd46c295eec9f7.html', Verify2Google),
     ], debug=True)