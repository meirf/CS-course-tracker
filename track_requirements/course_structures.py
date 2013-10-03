class CourseReq:
    """
    Note on prefix: A course requirement may only
    specify the first 2 digits of a fulfilling course's id.
    Includes DEPT, title, whether advisor approval is
    required and how many times it may be fulfilled.
    """

    def __init__(self, prefix, departments, title=None, adv_approv=False, multip=1):
        self.prefix = prefix
        self.departments = departments
        self.title = title
        self.adv_approv = adv_approv
        self.multip = multip

    def __eq__(self, other):
        return all([other.prefix == self.prefix, other.departments == self.departments, other.title == self.title,
                    other.adv_approv == self.adv_approv, other.multip == self.multip])

    def __hash__(self):
        return hash((self.prefix, self.title, self.adv_approv, self.multip))

    def __repr__(self):
        return '\n\t\t'.join([self.prefix, str(self.departments), self.title, "Approval required: " +
                                           str(self.adv_approv), "mult:"+str(self.multip)])


class TrackSubsection:
    """
    Each track has 2 to 5 subsections
    with specific restrictions for their containing requirements
    """

    def __init__(self, num_classes, course_reqs, minimum):
        self.num_classes = num_classes
        self.minimum = minimum
        self.course_reqs = course_reqs

    def __repr__(self):
        return '\n\t'.join(['\n'+str(self.num_classes), "Min: "+str(self.minimum), repr(self.course_reqs)])


class Track:

    def __init__(self, title, track_subs):
        self.title = title
        self.track_subs = track_subs

    def __repr__(self):
        return '\n'.join([str(self.title), repr(self.track_subs)])