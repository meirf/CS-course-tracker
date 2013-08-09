import unittest
from course_listing import courses, adv_courses
from course_requirement import CourseReq, TrackSubsection
from course_requirement import track_names, found_courses


class CourseTest(unittest.TestCase):

    def test_course_import(self):
        self.failUnless(len(courses)>0 and 
                    len(adv_courses)>0)

class TestGeneralCourseReq(unittest.TestCase):

    def test_course_req_creation(self):
        self.failUnless(CourseReq("41", ["COMS"]))


class TestTrackSubsection(unittest.TestCase):

    def test_track_subsection(self):
        self.failUnless(TrackSubsection(5))

class TestTrackFull(unittest.TestCase):

    def test_track_titles(self):
        self.failUnless(len(track_names)==6)

    def test_foundations_class_size(self):
        self.failUnless(len(found_courses)>10)    

def main():
    unittest.main()

if __name__ == "__main__":
    main()