import track_utils
import course_utils
from track_requirements.foundations import found_track

# currently only checking progress on foundations track
tracks = [found_track]


def get_all_track_fulfillments(courses_taken_input):
    """
    Returns for each track the courses taken that match
    the requirements for that track (including all track subsections.)
    """
    courses_taken = course_utils.get_conversion_for_all_inputted_elements(courses_taken_input)
    return [(track, track_utils.get_track_req_fulf_pairs(track, courses_taken)) for track in tracks]