import unittest
from course_listing import courses

class CourseTest(unittest.TestCase):

    def test_course_import(self):
        self.failUnless(len(courses))

def main():
    unittest.main()

if __name__ == "__main__":
    main()