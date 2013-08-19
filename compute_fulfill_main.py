import track_utils
import course_utils
from course_rules import found_track

def get_all_track_fulfillments(courses_taken_input):
    courses_taken = course_utils.get_conversion_for_all_inputted_elements(courses_taken_input)
    print track_utils.get_track_req_fulf_pairs(found_track, courses_taken)