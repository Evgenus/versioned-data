from collections import namedtuple


CmdDict = namedtuple(
    "CmdDictObject", [
        "type",
        "uid"
    ])


CmdList = namedtuple(
    "CmdListObject", [
        "type",
        "uid"
    ])


CmdDictKey = namedtuple(
    "CmdDictKey", [
        "key"
    ])


CmdValue = namedtuple(
    "CmdValue", [
        "value"
    ])


CmdRef = namedtuple(
    "CmdRef", [
        "ref"
    ])


def get_type_dotted_name(t):
    return "{}.{}".format(t.__module__, t.__name__)

class Serializer:
    CMD_DICT = CmdDict
    CMD_LIST = CmdList
    CMD_DICT_KEY = CmdDictKey
    CMD_VALUE = CmdValue
    CMD_REF = CmdRef

    def __init__(self):
        self._output = []

    @property
    def output(self):
        return self._output

    def _emit(self, command):
        self._output.append(command)        

    def emit_dict(self, obj, descriptor):
        self._emit(self.CMD_DICT(
            get_type_dotted_name(type(obj)),
            descriptor.uid))

    def emit_list(self, obj, descriptor):
        self._emit(self.CMD_LIST(
            get_type_dotted_name(type(obj)),
            descriptor.uid))

    def emit_key(self, key):
        self._emit(self.CMD_DICT_KEY(key))

    def emit_value(self, obj):
        self._emit(self.CMD_VALUE(obj))

    def emit_ref(self, descriptor):
        self._emit(self.CMD_REF(descriptor.uid))

    def serialize(self, entity):
        for uid, obj in entity.iterate_scope():
            descriptor = entity.get_descriptor(obj)
            if isinstance(obj, list):
                self.emit_list(obj, descriptor)
                for item in obj:
                    if entity.has_descriptor(item):
                        descriptor = entity.get_descriptor(obj)
                        self.emit_ref(descriptor)
                    else:
                        self.emit_value(item)
            elif isinstance(obj, dict):
                self.emit_dict(obj, descriptor)
                for key, value in obj.items():
                    self.emit_key(key)
                    if entity.has_descriptor(value):
                        descriptor = entity.get_descriptor(value)
                        self.emit_ref(descriptor)
                    else:
                        self.emit_value(value)
