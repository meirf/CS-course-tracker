class CourseReq:

    def __init__(self, prefix, departments, title=None, 
                 adv_approv=False, multip=1):        
        self.prefix = prefix
        self.departments = departments
        self.title = title
        self.adv_approv = adv_approv
        self.multip = multip

    def __eq__(self, other):
        return all([other.prefix == self.prefix, 
               other.departments == self.departments,
               other.title == self.title,
               other.adv_approv == self.adv_approv,
               other.multip == self.multip
               ])

    def __hash__(self):
        return hash((self.prefix, self.title, self.adv_approv, self.multip))


class TrackSubsection:

    def __init__(self, num_classes, minimum=True, course_reqs=[]):
        self.num_classes = num_classes
        self.minimum = minimum


class Track:

    def __init__(self, title, track_subs=[]):
        self.title = title
        self.track_subs = track_subs