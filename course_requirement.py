class CourseReq:

    def __init__(self, prefix, departments, title=None, 
                 adv_approv=False, multip=1):        
        self.prefix = prefix
        self.departments = departments
        self.title = title
        self.adv_approv = adv_approv
        self.multip = multip


class TrackSubsection:

    def __init__(self, num_classes, minimum=True, course_reqs=[]):
        self.num_classes = num_classes
        self.minimum = minimum

class Track:

    def __init__(self, title, track_subs=[]):
        self.title = title
        self.track_subs = track_subs



track_names = ("Foundations of Computer Science", 
                "Software Systems",
                "Digital Systems",
                "Artificial Intelligence",
                "Applications",
                "Vision and Graphics")

#"Foundations of Computer Science"
found_courses = []
found_courses.append(CourseReq("4231", ["CSOR"], "Analysis of Algorithms, I"))
found_courses.append(CourseReq("4236", ["COMS"], "Intro to Computational Complexity"))
found_courses.append(CourseReq("4241", ["COMS"], "Numerical Algorithms and Complexity"))
found_courses.append(CourseReq("4203", ["COMS"], "Graph Theory"))
found_courses.append(CourseReq("4205", ["COMS"], "Combinatorial Theory"))
found_courses.append(CourseReq("4252", ["COMS"], "Intro to Computational Learning Theory"))
found_courses.append(CourseReq("4261", ["COMS"], "Intro to Cryptography"))
found_courses.append(CourseReq("4281", ["COMS"], "Intro to Quantum Computing"))
found_courses.append(CourseReq("4444", ["COMS"], "Prog and Problem Solving"))
found_courses.append(CourseReq("4771", ["COMS"], "Machine Learning"))
found_courses.append(CourseReq("4772", ["COMS"], "Advanced Machine Learning"))
found_courses.append(CourseReq("4995", ["COMS"], "Math Foundations of Machine Learning"))
found_courses.append(CourseReq("6232", ["COMS"], "Analysis of Algorithms II"))
found_courses.append(CourseReq("6261", ["COMS"], "Advanced Cryptography"))
found_courses.append(CourseReq("6717", ["COMS"], "Information Theory"))

found_courses.append(CourseReq("3902", ["COMS"], "Undergraduate Thesis", True, 2))
found_courses.append(CourseReq("3998", ["COMS"], "Projects in CS", True, 2))
found_courses.append(CourseReq("4901", ["COMS"], "Projects in CS", True, 2))
found_courses.append(CourseReq("6901", ["COMS"], "Projects in CS", True, 2))