from cs_course_pool.course_template import Course
import track_utils
import course_utils
from track_requirements.foundations import found_track
from cs_course_pool.core_courses import courses as core_courses

# currently only checking progress on foundations track
tracks = [found_track]


def get_all_track_fulfillments(courses_taken):
    """
    Returns for each track the courses taken that match
    the requirements for that track (including all track subsections.)
    Returns list of (track, fulfillment) tuples;
            each fulfillment is list of dicts, one dict per track subsection
            each dict maps course subsection req -> list of sat courses
    """
    return [(track, track_utils.get_track_req_fulf_pairs(track, courses_taken)) for track in tracks]


def get_rem_req_count_per_tracksub(fulfill_pairs_list):
    """
    Returns list of elements;
            each element is a list of counts;
            each count is the number of remaining courses required in the
            ith subsection where the count's index is the ith value in that element
    """
    rem_req_counts = []
    for track, fulfillment in fulfill_pairs_list:
        count_list = []
        for i, sub_fulf in enumerate(fulfillment):
            num_reqs_satisfied = len(filter(lambda x:len(sub_fulf[x])>0, sub_fulf.keys()))
            count =  track.track_subs[i].num_classes - num_reqs_satisfied
            count_list.append(count)
        rem_req_counts.append(count_list)
    return rem_req_counts


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