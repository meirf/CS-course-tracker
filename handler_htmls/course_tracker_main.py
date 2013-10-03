import os
import jinja2
import webapp2

from cs_course_pool.core_courses import courses
from cs_course_pool.advanced_courses import adv_courses
from operator import attrgetter
from url_manipulation.url_decode import get_url_param_mappings
from matching_utils.compute_fulfill_main import get_all_track_fulfillments

JINJA_ENVIRONMENT = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'])


def get_rendering(var_mapping, html_file_name):
    template = JINJA_ENVIRONMENT.get_template(html_file_name)
    return template.render(var_mapping)    


class MainPage(webapp2.RequestHandler):
    """
    Retrieves courses data and displays main page.
    """

    def get(self):
        template_values = {
            'core_courses': courses,
            'adv_courses': sorted(list(adv_courses), key=attrgetter('course_num', 'title')),
        }
        
        self.response.write(get_rendering(template_values, 'index.html'))


class DisplayTakenTrackInfo(webapp2.RequestHandler):
    """
    Gets course requirement matching info for progress display page.
    """

    def get(self):
        courses_taken = get_url_param_mappings(str(self.request)).keys()

        template_values = {
            'fulfill_pairs_list': get_all_track_fulfillments(courses_taken),
        }
        self.response.write(get_rendering(template_values, 'progress.html'))

application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/taken', DisplayTakenTrackInfo),
     ], debug=True)