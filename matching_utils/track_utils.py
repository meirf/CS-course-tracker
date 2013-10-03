"""
Gathers data on which requirements are fulfilled by which taken courses
"""


def get_track_req_fulf_pairs(track, courses_taken):
    """
    Return list of dicts, each dict { req -> list of satisfying classes }
    """
    return [get_track_sub_req_fulf_pairs(subsection, courses_taken) for subsection in track.track_subs]


def get_track_sub_req_fulf_pairs(subsection, courses_taken):
    """
    Return dict: { req -> list of satisfying classes }
    """
    fulfs = {req: [] for req in subsection.course_reqs}
    num_req_classes = 0
    req_index = 0
    while req_index < len(subsection.course_reqs) and num_req_classes < subsection.num_classes:
        course_req = subsection.course_reqs[req_index]
        req_index += 1
        for course in courses_taken:
            if is_fulfilled(course, course_req):
                fulfs[course_req].append(course)
                num_req_classes += 1
    return fulfs


def is_fulfilled(course, requirement):
    """
    Return true if courses matches req
    """
    if course.title != requirement.title.replace(' ', '') and course.title != requirement.title:
        return False
    if course.dept not in requirement.departments:
        return False
    return str(course.course_num).startswith(requirement.prefix)