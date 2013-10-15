import os
import jinja2
import webapp2
import string

from cs_course_pool.core_courses import courses
from cs_course_pool.advanced_courses import adv_courses
from operator import attrgetter
from matching_utils import course_utils
from url_manipulation.url_decode import get_url_param_mappings
from matching_utils.compute_fulfill_main import get_all_track_fulfillments, get_unfulfilled_core_classes, get_rem_req_count_per_tracksub

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
        courses_taken_preformatted = get_url_param_mappings(str(self.request)).keys()
        courses_taken = course_utils.get_conversion_for_all_inputted_elements(courses_taken_preformatted)
        unfulfilled_core_classes = get_unfulfilled_core_classes(courses_taken)
        fulfill_pairs_list = get_all_track_fulfillments(courses_taken)
        remaining_course_count_requirement_per_tracksub = get_rem_req_count_per_tracksub(fulfill_pairs_list)
        template_values = {
            'unfulfilled_core_classes': unfulfilled_core_classes,
            'fulfill_pairs_list': fulfill_pairs_list,
            'remaining_course_count_requirement_per_tracksub': remaining_course_count_requirement_per_tracksub,
            'letters': string.uppercase,
        }
        self.response.write(get_rendering(template_values, 'progress.html'))

application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/taken', DisplayTakenTrackInfo),
     ], debug=True)