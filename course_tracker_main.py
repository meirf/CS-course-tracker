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

def get_rendering(var_mapping, html_file_name):
    template = JINJA_ENVIRONMENT.get_template(html_file_name)
    return template.render(var_mapping)    

class MainPage(webapp2.RequestHandler):

    def get(self):       

        template_values = {
            'core_courses' : courses,
            'adv_courses': sorted(list(adv_courses), key=itemgetter(1, 2)),
        }
        
        self.response.write(get_rendering(template_values, 'index.html'))

class Verify2Google(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('google-site-verification: google17bd46c295eec9f7.html')

class DisplayTakenTrackInfo(webapp2.RequestHandler):

    def get(self):
        courses_taken = get_url_param_mappings(str(self.request)).keys()
        template_values = {
            'courses_taken' : courses_taken,
        }
        self.response.write(get_rendering(template_values, 'progress.html'))

application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/taken', DisplayTakenTrackInfo),
     ('/google17bd46c295eec9f7.html', Verify2Google),
     ], debug=True)