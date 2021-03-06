from course_template import Course

""" List of all core classes required for all track. """

courses = []

intro_honors = Course('COMS', "1007", 'Honors Intro to CS')
intro_basic = Course('COMS', "1004", 'Intro to CS and Prog in Java', intro_honors)
dsa_honors = Course('COMS', "3137", 'Honors Data Structures')
dsa_basic = Course('COMS', "3134", 'Data Structures in Java', dsa_honors)
stat_adv = Course('SIEO', "3600", 'Prob and Stats')
stat_basic = Course('SIEO', "4150", 'Prob and Stats', stat_adv)

courses.append(intro_basic)
courses.append(dsa_basic)

courses.append(Course('COMS', "3157", 'Advanced Programming'))
courses.append(Course('COMS', "3203", 'Discrete Math'))
courses.append(Course('COMS', "3251", 'Computational Linear Algebra'))
courses.append(Course('COMS', "3261", 'CS Theory'))
courses.append(Course('CSEE', "3827", 'Fundamentals of Computer Systems'))
courses.append(stat_basic)