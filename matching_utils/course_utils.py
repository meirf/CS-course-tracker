import re
from cs_course_pool.course_template import Course


def get_convert_to_course(course_taken_string_from_checkbox):
    """
    Sets courses title same as title with no spaces
    so that  course.title == course.title_no_spaces

        DEPT     CNUM TITLE
    '([A-Z]{4})(\d{4})(\S*)'

    """
    match = re.search('([A-Z]{4})(\d{4})(\S*)', course_taken_string_from_checkbox)
    if match:
        course_params = match.groups()
        return Course(course_params[0], course_params[1], course_params[2])
    return None


def get_conversion_for_all_inputted_elements(list_of_taken):
    return [get_convert_to_course(taken) for taken in list_of_taken]