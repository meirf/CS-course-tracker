class Course:
    """
    Stores data of a CS course, possibly
    including reference to advanced version
    """

    def __init__(self, dept, course_num, title, adv_vers=None):
        self.dept = dept
        self.course_num = course_num
        self.title = title
        self.adv_vers = adv_vers
        self.title_no_spaces = title.replace(' ', '')

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        if self.dept == other.dept and self.course_num == other.course_num and self.title_no_spaces == other.title_no_spaces:
            return True
        return self.adv_vers == other

    def __hash__(self):
        return hash((self.dept, self.course_num, self.title_no_spaces, self.adv_vers))

    def __repr__(self):
        rep = ' '.join([self.__class__.__name__, ": ", self.dept, str(self.course_num), self.title])
        if self.adv_vers:
            rep += " OR " + repr(self.adv_vers)
        return rep