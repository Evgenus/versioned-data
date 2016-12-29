from .types import get_registry

class List(list):
    def __hash__(self):
        return id(self)


get_registry().register(list, List)


class Dict(dict):
    def __hash__(self):
        return id(self)


get_registry().register(dict, Dict)
