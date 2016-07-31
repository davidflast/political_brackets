class Team(object):
    def __init__(self, name):
        assert isinstance(name, basestring)
        self.name = name
    def get_name(self):
        return self.name