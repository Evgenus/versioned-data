class List(list):
    def __hash__(self):
        return id(self)

class Dict(dict):
    def __hash__(self):
        return id(self)
