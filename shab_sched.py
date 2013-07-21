import cgi
import urllib

from google.appengine.api import users, urlfetch

from google.appengine.ext import ndb

import os
import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

DEFAULT_MEAL_SCHED_NAME = 'default_meal_sched'

# We set a parent key on the 'Meals' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def meal_sched_key(meal_sched_name=DEFAULT_MEAL_SCHED_NAME):
    """Constructs a Datastore key for a MealSchedule entity with meal_sched_name."""
    return ndb.Key('MealSchedule', meal_sched_name)


class Meal(ndb.Model):
    """Models an individual MealSchedule entry with author, location, and date."""
    author = ndb.UserProperty()
    location = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        meal_sched_name = self.request.get('meal_sched_name',
                                          DEFAULT_MEAL_SCHED_NAME)
        meals_query = Meal.query(
            ancestor=meal_sched_key(meal_sched_name)).order(-Meal.date)
        meals = meals_query.fetch(3)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        
        # eventuall move to separate function; set url up top
        #form_fields = {
        #  "oauth_consumer_key": "shobbus.appspot.com",
        #  "oauth_nonce": "Johnson",
        #  "oauth_signature_method": "Albert.Johnson@example.com",
        #  "oauth_signature": "Albert.Johnson@example.com",
        #  "oauth_timestamp": "Albert.Johnson@example.com",
        #  "scope": "Albert.Johnson@example.com",
        #  "oauth_callback": "Albert.Johnson@example.com",
        #}
        #form_data = urllib.urlencode(form_fields)
        #esult = urlfetch.fetch(url="https://www.google.com/accounts/OAuthGetRequestToken",
        #                        payload=form_data,
        #                        method=urlfetch.POST,
        #                        headers={'Content-Type': 'application/x-www-form-urlencoded'})
        #    

        template_values = {
            'meals': meals,
            'meal_sched_name': urllib.quote_plus(meal_sched_name),
            'url': url,
            'url_linktext': url_linktext,
            #'response': response,
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


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', MealSchedule),
], debug=True)
