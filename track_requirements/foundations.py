from course_structures import CourseReq, TrackSubsection, Track

track_names = ("Foundations of Computer Science", "Software Systems", "Digital Systems",
               "Artificial Intelligence", "Applications", "Vision and Graphics")


'''
Foundations of Computer Science
Contains two track subsections
'''
found_sec_A_courses = [CourseReq("4231", ["CSOR"], "Analysis of Algorithms, I"),
                       CourseReq("4236", ["COMS"], "Intro to Computational Complexity"),
                       CourseReq("4241", ["COMS"], "Numerical Algorithms and Complexity")]

found_sec_A = TrackSubsection(3, found_sec_A_courses, True)

found_sec_B_courses = [CourseReq("4203", ["COMS"], "Graph Theory"),
                       CourseReq("4205", ["COMS"], "Combinatorial Theory"),
                       CourseReq("4252", ["COMS"], "Intro to Computational Learning Theory"),
                       CourseReq("4261", ["COMS"], "Intro to Cryptography"),
                       CourseReq("4281", ["COMS"], "Intro to Quantum Computing"),
                       CourseReq("4444", ["COMS"], "Prog and Problem Solving"),
                       CourseReq("4771", ["COMS"], "Machine Learning"),
                       CourseReq("4772", ["COMS"], "Advanced Machine Learning"),
                       CourseReq("4995", ["COMS"], "Math Foundations of Machine Learning"),
                       CourseReq("6232", ["COMS"], "Analysis of Algorithms II"),
                       CourseReq("6261", ["COMS"], "Advanced Cryptography"),
                       CourseReq("6717", ["COMS"], "Information Theory"),
                       CourseReq("3902", ["COMS"], "Undergraduate Thesis", True, 2),
                       CourseReq("3998", ["COMS"], "Projects in CS", True, 2),
                       CourseReq("4901", ["COMS"], "Projects in CS", True, 2),
                       CourseReq("6901", ["COMS"], "Projects in CS", True, 2)]

found_sec_B = TrackSubsection(4, found_sec_B_courses, True)

found_track = Track(track_names[0], [found_sec_A, found_sec_B])