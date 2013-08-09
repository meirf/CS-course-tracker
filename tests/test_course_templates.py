#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from course_listing import courses, adv_courses
from course_structures import CourseReq, TrackSubsection
from course_rules import found_sec_A_courses, found_sec_B_courses


class CourseTest(unittest.TestCase):

    def test_course_import(self):
        self.failUnless(len(courses) > 0 and len(adv_courses) > 0)


class TestGeneralCourseReq(unittest.TestCase):

    def test_course_req_creation(self):
        self.failUnless(CourseReq('41', ['COMS']))


class TestTrackSubsection(unittest.TestCase):

    def test_track_subsection(self):
        self.failUnless(TrackSubsection(5))


class TestTrackFull(unittest.TestCase):

    def test_foundations_class_size(self):
        self.failUnless(len(found_sec_A_courses) == 3
                        and len(found_sec_B_courses) == 16)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
