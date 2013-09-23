class Course:
    """
    Stores data of a CS course possibly 
    including reference to advanced version
    """

    def __init__(self, dept, course_num, title, adv_vers=None):
        self.dept = dept
        self.course_num = course_num
        self.title = title
        self.adv_vers = adv_vers
        self.title_no_spaces = title.replace(' ','')

    def __repr__(self):
        rep = ' '.join([self.__class__.__name__, ": ", self.dept, str(self.course_num), self.title])
        if self.adv_vers:
            rep += " OR " + repr(self.adv_vers)
        return rep


"""
Two lists of both basic courses and advanced.
Since size is small, db would not add much for efficiency.
However, due to possibility of new course offering,
db may be used for adding courses with admin page
as a non-programmatic course addition/drop portal. 
"""
courses = []

intro_honors = Course('COMS',1007,'Honors Intro to CS')
intro_basic = Course('COMS',1004,'Intro to CS and Prog in Java',intro_honors)
dsa_honors = Course('COMS',3137,'Honors Data Structures')
dsa_basic = Course('COMS',3134,'Data Structures in Java', dsa_honors)
stat_adv = Course('SIEO',3600,'Prob and Stats')
stat_basic = Course('SIEO',4150,'Prob and Stats',stat_adv)

courses.append(intro_basic)
courses.append(dsa_basic)
courses.append(Course('COMS',3157,'Advanced Programming'))
courses.append(Course('COMS',3203,'Discrete Math'))
courses.append(Course('COMS',3251,'Computational Linear Algebra'))
courses.append(Course('COMS',3261,'CS Theory'))
courses.append(Course('CSEE',3827,'Fundamentals of Computer Systems'))
courses.append(stat_basic)

adv_courses = set()

aml_advanced = Course('COMS',6772,'Adv Machine Learning')
aml_basic = Course('COMS',4772,'Adv Machine Learning', aml_advanced)

adv_courses.add(aml_basic)
adv_courses.add(aml_advanced)

bio_adv = Course('COMS',6737,'Biometrics')
bio_basic = Course('COMS',4737,'Biometrics',bio_adv)

adv_courses.add(bio_basic)
adv_courses.add(bio_adv)

adv_courses.add(Course('COMS',3902,'Undergraduate Thesis'))
adv_courses.add(Course('COMS',3998,'Projects in CS'))
adv_courses.add(Course('ECBM',4060,'Introduction to Genomic Information'))
adv_courses.add(Course('COMS',4111,'Introduction to Databases'))
adv_courses.add(Course('COMS',4112,'Database System Implementation'))
adv_courses.add(Course('COMS',4115,'Prog Languages and Translators'))
adv_courses.add(Course('COMS',4117,'Compilers and Interpreters'))
adv_courses.add(Course('COMS',4118,'Operating Systems'))
adv_courses.add(Course('CSEE',4119,'Computer Networks'))
adv_courses.add(Course('COMS',4130,'Parallel Programming'))
adv_courses.add(Course('CSEE',4140,'Networking Laboratory'))
adv_courses.add(Course('COMS',4156,'Advanced Software Engineering'))
adv_courses.add(Course('COMS',4160,'Computer Graphics'))
adv_courses.add(Course('COMS',4162,'Advanced Computer Graphics'))
adv_courses.add(Course('COMS',4165,'Computational Techniques in Pixel Processing'))
adv_courses.add(Course('COMS',4167,'Computer Animation'))
adv_courses.add(Course('COMS',4170,'User Interface Design'))
adv_courses.add(Course('COMS',4172,'3D User Interfaces and Augmented Reality'))
adv_courses.add(Course('COMS',4180,'Network Security'))
adv_courses.add(Course('COMS',4187,'Security Architecture and Engineering'))
adv_courses.add(Course('COMS',4203,'Graph Theory'))
adv_courses.add(Course('COMS',4205,'Combinatorial Theory'))
adv_courses.add(Course('CSOR',4231,'Analysis of Algorithms, I'))
adv_courses.add(Course('COMS',4236,'Intro to Computational Complexity'))
adv_courses.add(Course('COMS',4241,'Numerical Algorithms and Complexity'))
adv_courses.add(Course('COMS',4252,'Intro to Computational Learning Theory'))
adv_courses.add(Course('COMS',4261,'Intro to Cryptography'))
adv_courses.add(Course('COMS',4281,'Intro to Quantum Computing'))
adv_courses.add(Course('EECS',4340,'Computer Hardware Design'))
adv_courses.add(Course('COMS',4444,'Prog and Problem Solving'))
adv_courses.add(Course('COMS',4460,'Principles of Innovation and Entrepreneurship'))
adv_courses.add(Course('COMS',4560,'Introduction to Computer Applications in Health Care and Biomedicine'))
adv_courses.add(Course('COMS',4701,'Artificial Intelligence'))
adv_courses.add(Course('COMS',4705,'Natural Language Processing'))
adv_courses.add(Course('COMS',4706,'Spoken Language Processing'))
adv_courses.add(Course('COMS',4731,'Computer Vision'))
adv_courses.add(Course('COMS',4733,'Computational Aspects of Robotics'))
adv_courses.add(Course('COMS',4725,'Knowledge Representation and Reasoning'))
adv_courses.add(Course('COMS',4735,'Visual Interfaces to Computers'))
adv_courses.add(Course('CBMF',4761,'Computational Genomics'))
adv_courses.add(Course('COMS',4771,'Machine Learning'))
adv_courses.add(Course('CSEE',4823,'Advanced Logic Design'))
adv_courses.add(Course('CSEE',4824,'Computer Architecture'))
adv_courses.add(Course('CSEE',4840,'Embedded Systems'))
adv_courses.add(Course('COMS',4901,'Projects in CS'))
adv_courses.add(Course('COMS',4910,'Curricular Practical Training'))
adv_courses.add(Course('COMS',4995,'Math Foundations of Machine Learning'))
adv_courses.add(Course('COMS',4995,'Special Topics in CS (Video Game Technology and Design)'))
adv_courses.add(Course('COMS',4995,'Special projects in CS I'))
adv_courses.add(Course('COMS',4996,'Special projects in CS II'))
adv_courses.add(Course('COMS',4999,'Computing and the Humanities'))
adv_courses.add(Course('COMS',6121,'Reliable Software'))
adv_courses.add(Course('COMS',6232,'Analysis of Algorithms II'))
adv_courses.add(Course('COMS',6261,'Advanced Cryptography'))
adv_courses.add(Course('COMS',6717,'Information Theory'))
adv_courses.add(Course('COMS',6732,'Computational Imaging'))
adv_courses.add(Course('CSEE',6824,'Parallel Computer Architecture'))
adv_courses.add(Course('CSEE',6847,'Distributed Embedded Systems'))
adv_courses.add(Course('COMS',6861,'CAD of Digital Systems'))
adv_courses.add(Course('CSEE',6868,'System-on-Chip Platforms'))
adv_courses.add(Course('COMS',6900,'Tutorial in CS'))
adv_courses.add(Course('COMS',6901,'Projects in CS'))
adv_courses.add(Course('COMS',6902,'Thesis'))
adv_courses.add(Course('COMS',6998,'Topics in CS I'))
adv_courses.add(Course('COMS',6999,'Topics in CS II'))