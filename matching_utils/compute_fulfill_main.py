from cs_course_pool.course_template import Course
import track_utils
import course_utils
from track_requirements.foundations import found_track
from cs_course_pool.core_courses import courses as core_courses

# currently only checking progress on foundations track
tracks = [found_track]


def get_all_track_fulfillments(courses_taken_input):
    """
    Returns for each track the courses taken that match
    the requirements for that track (including all track subsections.)
    """
    courses_taken = course_utils.get_conversion_for_all_inputted_elements(courses_taken_input)
    return [(track, track_utils.get_track_req_fulf_pairs(track, courses_taken)) for track in tracks]


def get_unfulfilled_core_classes(courses_taken):
    """
    Returns core classes that have not been taken
    """
    core_classes_pool = set(core_courses)
    core_classes_taken = set()

    for core_course in core_courses:
        for course_took in courses_taken:
            if core_course == course_took:
                core_classes_taken.add(core_course)
                break

    return core_classes_pool - core_classes_taken