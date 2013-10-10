#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from cs_course_pool.core_courses import courses
from cs_course_pool.advanced_courses import adv_courses
from cs_course_pool.course_template import Course
from track_requirements.course_structures import CourseReq, TrackSubsection
from track_requirements.foundations import found_sec_A_courses, found_sec_B_courses


class CourseTest(unittest.TestCase):

    def setUp(self):
        self.intro_honors = Course('COMS', 1007, 'Honors Intro to CS')
        self.intro_basic = Course('COMS', 1004, 'Intro to CS and Prog in Java', self.intro_honors)
    
    def test_course_import(self):
        """
        Make sure both course lists are not empty
        """
        self.assertGreater(len(courses), 0)
        self.assertGreater(len(adv_courses), 0)

    def test_repr_course(self):
        """
        Test repr function
        """
        self.assertEqual(repr(self.intro_basic), 'Course :  COMS 1004 Intro to CS and Prog in Java OR '
                        + repr(self.intro_honors))


class TestGeneralCourseReq(unittest.TestCase):

    def test_course_req_creation(self):
        """
        Ensure insantion occurs
        """
        self.assertIsNotNone(CourseReq('41', ['COMS']))


class TestTrackSubsection(unittest.TestCase):

    def test_track_subsection(self):
        """
        Ensure track subsection created
        """
        self.assertIsNotNone(TrackSubsection(5, None, None))


class TestTrackFull(unittest.TestCase):

    def test_foundations_class_size(self):
        """
        Test specific size for foundations track
        """
        self.assertEqual(len(found_sec_A_courses), 3)
        self.assertEqual(len(found_sec_B_courses), 16)


class TestCourseReqHashable(unittest.TestCase):

    def test_hashable_coursereq(self):
        """
        Ensure coursereq instance is hashable by putting it in dict
        """
        self.assertIsNotNone({CourseReq(1, 2, 3)})