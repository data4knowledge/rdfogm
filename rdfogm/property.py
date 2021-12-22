class Property(object):

    def __init__(self, name, predicate=None, default=None):
        self.name = name
        self.predicate = predicate
        self.default = default

    def __repr__(self) -> str:
        return super().__repr__()