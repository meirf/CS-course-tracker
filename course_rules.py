from course_structures import CourseReq, TrackSubsection, Track

track_names = ("Foundations of Computer Science", "Software Systems", "Digital Systems",
               "Artificial Intelligence", "Applications", "Vision and Graphics")


'''
Foundations of Computer Science
'''
found_sec_A_courses = []

found_sec_A_courses.append(CourseReq("4231", ["CSOR"], "Analysis of Algorithms, I"))
found_sec_A_courses.append(CourseReq("4236", ["COMS"], "Intro to Computational Complexity"))
found_sec_A_courses.append(CourseReq("4241", ["COMS"], "Numerical Algorithms and Complexity"))

found_sec_A = TrackSubsection(3, minimum=True, course_reqs=found_sec_A_courses)

found_sec_B_courses = []

found_sec_B_courses.append(CourseReq("4203", ["COMS"], "Graph Theory"))
found_sec_B_courses.append(CourseReq("4205", ["COMS"], "Combinatorial Theory"))
found_sec_B_courses.append(CourseReq("4252", ["COMS"], "Intro to Computational Learning Theory"))
found_sec_B_courses.append(CourseReq("4261", ["COMS"], "Intro to Cryptography"))
found_sec_B_courses.append(CourseReq("4281", ["COMS"], "Intro to Quantum Computing"))
found_sec_B_courses.append(CourseReq("4444", ["COMS"], "Prog and Problem Solving"))
found_sec_B_courses.append(CourseReq("4771", ["COMS"], "Machine Learning"))
found_sec_B_courses.append(CourseReq("4772", ["COMS"], "Advanced Machine Learning"))
found_sec_B_courses.append(CourseReq("4995", ["COMS"], "Math Foundations of Machine Learning"))
found_sec_B_courses.append(CourseReq("6232", ["COMS"], "Analysis of Algorithms II"))
found_sec_B_courses.append(CourseReq("6261", ["COMS"], "Advanced Cryptography"))
found_sec_B_courses.append(CourseReq("6717", ["COMS"], "Information Theory"))

found_sec_B_courses.append(CourseReq("3902", ["COMS"], "Undergraduate Thesis", True, 2))
found_sec_B_courses.append(CourseReq("3998", ["COMS"], "Projects in CS", True, 2))
found_sec_B_courses.append(CourseReq("4901", ["COMS"], "Projects in CS", True, 2))
found_sec_B_courses.append(CourseReq("6901", ["COMS"], "Projects in CS", True, 2))

found_sec_B = TrackSubsection(4, minimum=True, course_reqs=found_sec_B_courses)

found_track = Track(track_names[0], track_subs=[found_sec_A, found_sec_B])