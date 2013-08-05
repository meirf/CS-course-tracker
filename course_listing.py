from collections import namedtuple

Course = namedtuple('Course','dept course_num title adv_vers')
courses = []

intro_honors = Course('COMS',1007,'Honors Intro to CS', None)
intro_basic = Course('COMS',1004,'Intro to CS and Programming in Java',intro_honors)

dsa_honors = Course('COMS',3137,'Honors Data Structures', None)
dsa_basic = Course('COMS',3134,'Data Structures in Java', dsa_honors)

stat_adv = Course('SIEO',3600,'Probability and Statistics',None)
stat_basic = Course('SIEO',4150,'Probability and Statistics',stat_adv)


courses.append(intro_basic)
#courses.append(intro_honors)
courses.append(dsa_basic)
#courses.append(dsa_honors)
courses.append(Course('COMS',3157,'Advanced Programming',None))
courses.append(Course('COMS',3203,'Discrete Mathematics',None))
courses.append(Course('COMS',3251,'Computational Linear Algebra',None))
courses.append(Course('COMS',3261,'Computer Science Theory',None))
courses.append(Course('CSEE',3827,'Fundamentals of Computer Systems',None))
courses.append(stat_basic)
#courses.append(stat_adv)