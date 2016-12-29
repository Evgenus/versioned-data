from weakref import WeakKeyDictionary
from weakref import WeakValueDictionary

from .placeholders import Dict
from .placeholders import List


class DataDescriptior:
    def __init__(self, uid):
        self._uid = uid

    @property
    def uid(self):
        return self._uid


class HostEntity:
    def __init__(self):
        self._next_id = 0
        self._descriptors = WeakKeyDictionary()
        self._scope = WeakValueDictionary()

    def create_decriptor(self):
        descriptor = DataDescriptior(self._next_id)
        self._next_id += 1
        return descriptor        

    def has_descriptor(self, obj):
        return obj in self._descriptors

    def get_descriptor(self, obj):
        return self._descriptors[obj]

    def set_descriptor(self, obj, descriptor):
        self._descriptors[obj] = descriptor
        self._scope[descriptor.uid] = obj

    def identify(self, obj):

        if isinstance(obj, list):
            identified = List()            
            for item in obj:
                identified.append(self.identify(item))
        elif isinstance(obj, dict):
            identified = Dict()
            for key, value in obj.items():
                identified[key] = self.identify(value)
        else:
            identified = obj

        if isinstance(obj, (dict, list)):
            if not self.has_descriptor(obj):
                descriptor = self.create_decriptor()
            else:
                descriptor = self.get_descriptor(obj)

            self.set_descriptor(identified, descriptor)

        return identified

    def iterate_scope(self):
        for uid, obj in self._scope.items():
            yield uid, obj
