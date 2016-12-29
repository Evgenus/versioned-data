from versioned import HostEntity
from versioned import Serializer

entity = HostEntity()

data = {
    "items": [1, 2, 3, {"a": 1, "b": 2}]
}

identified_data1 = entity.identify(data)

serializer1 = Serializer()
serializer1.serialize(entity)

identified_data1["items"][3]["c"] = {"new": ["asdfasd", {"subdata": [5,6,7]}]}
identified_data2 = entity.identify(identified_data1)

serializer2 = Serializer()
serializer2.serialize(entity)

import difflib

a = serializer1.output
b = serializer2.output
s = difflib.SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(
        tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))



# TODO 
# find diff of change set and acesstor
# create two child set of chages and find diff