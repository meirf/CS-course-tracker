#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from cs_course_pool.core_courses import courses
from cs_course_pool.advanced_courses import adv_courses
from cs_course_pool.course_listing import Course
from track_requirements.course_structures import CourseReq, TrackSubsection
from track_requirements.foundations import found_sec_A_courses, found_sec_B_courses
from url_manipulation.url_decode import get_url_param_mappings
from matching_utils.track_utils import is_fulfilled
from matching_utils.course_utils import get_convert_to_course


class CourseTest(unittest.TestCase):

    def setUp(self):
        self.intro_honors = Course('COMS', 1007, 'Honors Intro to CS')
        self.intro_basic = Course('COMS', 1004, 'Intro to CS and Prog in Java', self.intro_honors)
    
    def test_course_import(self):
        self.assertGreater(len(courses), 0)
        self.assertGreater(len(adv_courses), 0)

    def test_repr_course(self):
        self.assertEqual(repr(self.intro_basic), 'Course :  COMS 1004 Intro to CS and Prog in Java OR '
                        + repr(self.intro_honors))


class TestGeneralCourseReq(unittest.TestCase):

    def test_course_req_creation(self):
        self.assertIsNotNone(CourseReq('41', ['COMS']))


class TestTrackSubsection(unittest.TestCase):

    def test_track_subsection(self):
        self.assertIsNotNone(TrackSubsection(5, None, None))


class TestTrackFull(unittest.TestCase):

    def test_foundations_class_size(self):
        self.assertEqual(len(found_sec_A_courses), 3)
        self.assertEqual(len(found_sec_B_courses), 16)


class TestUrlDecode(unittest.TestCase):

    def setUp(self):
        self.x = "GET /taken?content=hey!!&a=xyz HTTP/1.1 Accept: text/html,application/"
        self.y = "GET /taken?content=hey HTTP/1.1 Accept: text/html,application/"
        self.z = "GET /taken? HTTP/1.1 Accept: text/html,application/"

    def test_url_decode_2_params(self):
        self.assertEqual(get_url_param_mappings(self.x), {'content': 'hey!!', 'a': 'xyz'})

    def test_url_decode_1_params(self):
        self.assertEqual(get_url_param_mappings(self.y), {'content': 'hey'})

    def test_url_decode_0_params(self):
        self.assertEqual(get_url_param_mappings(self.z), {})


class TestTrackUtils(unittest.TestCase):


    def setUp(self):
        self.req_a = CourseReq("4901", ["COMS"], "Projects in CS", True, 2)
        self.intro_honors = Course('COMS', 1007, 'Honors Intro to CS', None)
        self.req_b = CourseReq("6232", ["COMS"], "Analysis of Algorithms II")
        self.ana_algo_II = Course('COMS', 6232, 'Analysis of Algorithms II', None)

    def test_single_fulfillment_return_correct_type(self):
        self.assertIsInstance(is_fulfilled(self.intro_honors, self.req_a) , int)

    def test_single_fulfillment_result_non_match(self):
        self.assertFalse(is_fulfilled(self.intro_honors, self.req_a))

    def test_single_fulfillment_result_match(self):
        self.assertTrue(is_fulfilled(self.ana_algo_II, self.req_b))


class TestCourseUtil(unittest.TestCase):

    def setUp(self):
        self.course_from_input = "COMS1004IntrotoCSandProginJava"

    def test_get_convert_to_course(self):
        self.assertIsInstance(get_convert_to_course(self.course_from_input), Course)
 
    def test_course_fields(self):
        crs = get_convert_to_course(self.course_from_input)
        self.assertEqual(crs.dept, 'COMS')
        self.assertEqual(crs.course_num, '1004')
        self.assertEqual(crs.title, 'IntrotoCSandProginJava')


class TestCourseReqHashable(unittest.TestCase):

    def test_hashable_coursereq(self):
        self.assertIsNotNone({CourseReq(1, 2, 3)})