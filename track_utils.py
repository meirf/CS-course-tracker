from collections import defaultdict
# TODO make dict that keeps of track which req are fulfilled by which courses
# course_req : [course_a, course_b]

#class Track: title, track_subs=[]
def get_track_req_fulf_pairs(track, courses_taken):
    fulfillments = []
    courses_used = set()
    for subsection in track.track_subs:
        sub_fulf_pairs = get_track_sub_req_fulf_pairs(subsection, courses_taken, courses_used)
        fulfillments.append(sub_fulf_pairs)
    return fulfillments

#class TrackSubsection: num_classes, minimum=True, course_reqs=[]
def get_track_sub_req_fulf_pairs(subsection, courses_taken, courses_used):
    fulfs = defaultdict(list)
    count = 0
    index = 0
    while index < len(subsection.course_reqs) and count < subsection.num_classes:
        course_req = subsection.course_reqs[index]
        index += 1
        for course_taken in courses_taken:
            if course_taken not in courses_used and is_fulfilled(course_taken, course_req):
                fulfs[course_req].append(course_taken)
                courses_used.add(course_taken)
                count += 1
    return fulfs

def is_fulfilled(course, requirement):
    if course.title != requirement.title.replace(' ','') and course.title != requirement.title:
        return False
    if course.dept not in requirement.departments:
        return False
    return str(course.course_num).startswith(requirement.prefix)