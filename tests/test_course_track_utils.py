#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from matching_utils.track_utils import is_fulfilled
from matching_utils.course_utils import get_convert_to_course
from cs_course_pool.course_template import Course
from cs_course_pool.core_courses import courses
from track_requirements.course_structures import CourseReq
from matching_utils.compute_fulfill_main import get_unfulfilled_core_classes
from url_manipulation.url_decode import get_url_param_mappings
from matching_utils import course_utils

class TestTrackUtils(unittest.TestCase):

    def setUp(self):
        self.req_a = CourseReq("4901", ["COMS"], "Projects in CS", True, 2)
        self.intro_honors = Course('COMS', "1007", 'Honors Intro to CS', None)
        self.req_b = CourseReq("6232", ["COMS"], "Analysis of Algorithms II")
        self.ana_algo_II = Course('COMS', "6232", 'Analysis of Algorithms II', None)

    def test_single_fulfillment_return_correct_type(self):
        """
        Making sure method output is boolean. Note bool is subtype of int.
        """
        self.assertIsInstance(is_fulfilled(self.intro_honors, self.req_a) , bool)

    def test_single_fulfillment_result_non_match(self):
        """
        Ensuring output of False for fulfillment function with a
        specific input of a requirement not fulffilled by given course
        """
        self.assertFalse(is_fulfilled(self.intro_honors, self.req_a))

    def test_single_fulfillment_result_match(self):
        """
        Ensuring output of True for fulfillment function with a
        specific input of a requirement that is fulfilled by given course

        """
        self.assertTrue(is_fulfilled(self.ana_algo_II, self.req_b))


class TestCourseUtil(unittest.TestCase):

    def setUp(self):
        self.course_from_input = "COMS1004IntrotoCSandProginJava"

    def test_get_convert_to_course(self):
        """
        Check instantiation successful
        """
        self.assertIsInstance(get_convert_to_course(self.course_from_input), Course)

    def test_course_fields(self):
        """
        Ensure parsing is correct
        """
        crs = get_convert_to_course(self.course_from_input)
        self.assertEqual(crs.dept, 'COMS')
        self.assertEqual(crs.course_num, '1004')
        self.assertEqual(crs.title, 'IntrotoCSandProginJava')

class TestCoreClassesNotFulfilled(unittest.TestCase):

    def setUp(self):
        req = "GET /taken?COMS1004IntrotoCSandProginJava=on&COMS3134DataStructuresinJava=on&COMS3157" \
              "AdvancedProgramming=on&COMS4117CompilersandInterpreters=on&COMS4203GraphTheory=on&CSOR" \
              "4231AnalysisofAlgorithms%2CI=on&COMS4236IntrotoComputationalComplexity=on HTTP/1.1 " \
              "Accept: text/html,application/"
        courses_taken_input = get_url_param_mappings(req).keys()
        self.courses_taken = course_utils.get_conversion_for_all_inputted_elements(courses_taken_input)

    def test_core_classes_not_taken_not_none(self):
        self.assertIsNotNone(get_unfulfilled_core_classes(self.courses_taken))
        self.assertNotEqual(get_unfulfilled_core_classes(self.courses_taken), {})
        self.assertEqual(len(get_unfulfilled_core_classes(self.courses_taken)), 8-3)

class CourseEqualMatcher(unittest.TestCase):
    """
    Test Course's __eq__ function
    """

    def setUp(self):
        self.course_a = Course('COMS', "3157", 'Advanced Programming')
        self.course_b = Course('COMS', "3157", 'Advanced Programming')
        self.course_c = Course('COMS', "3902", 'Undergraduate Thesis')
        self.stat_adv = Course('SIEO', "3600", 'Prob and Stats')
        self.stat_basic = Course('SIEO', "4150", 'Prob and Stats', self.stat_adv)

    def test_none_input(self):
        self.assertNotEqual(self.course_a, None)

    def test_no_advanced_version(self):
        self.assertEqual(self.course_a, self.course_b)
        self.assertEqual(self.course_b, self.course_a)

    def test_with_adv_version(self):
        self.assertEqual(self.stat_basic, self.stat_adv)
        self.assertNotEqual(self.stat_adv, self.stat_basic)

    def test_legit_class_but_not_match(self):
        self.assertNotEqual(self.course_a, self.course_c)