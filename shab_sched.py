import cgi
import urllib 
import os
import jinja2
import webapp2

from google.appengine.api import users, urlfetch
from google.appengine.ext import ndb
from shab_dates import next_weeks_ltd
from shab_dates import get_times_quarters

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

DEFAULT_MEAL_SCHED_NAME = 'default_meal_sched'

DEFAULT_INVITATION_MESSAGE = "Yo snitch, please join my Shabbat meal.\nSign in at"#+users.get_current_user().email()#+"<a href=\"http://shobbus.appspot.com/\">shobbus.appspot.com</a>"
   #"\n-"#+users.get_current_user().nickname()

#DEFAULT_INVITATION_MESSAGE = "Yo snitch, please join my Shabbat meal.\nSign in at"+"<a href=\"http://shobbus.appspot.com/\">shobbus.appspot.com</a>"
 # "\n-"+users.get_current_user().nickname()


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

        upcoming_shab_dates = next_weeks_ltd(90210, 4)
        times = get_times_quarters()

        template_values = {
            'default_invite': DEFAULT_INVITATION_MESSAGE,
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


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', MealSchedule),
], debug=True)
