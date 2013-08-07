import unittest
from course_listing import courses, adv_courses

class CourseTest(unittest.TestCase):

    def test_course_import(self):
        self.failUnless(len(courses)>0 and 
                    len(adv_courses)>0)



def main():
    unittest.main()

if __name__ == "__main__":
    main()