from sentinels import NOTHING


__all__ = [
    "TypesRegistry",
    "get_registry"
]


class TypesRegistry:
    def __init__(self):
        self._mapping = {}
        self._back = {}

    def register(self, type_, alias):
        assert isinstance(type_, type)
        assert isinstance(alias, type)
        self._mapping[type_] = alias
        self._back[alias] = type_

    def get_alias(self, type_, default=NOTHING):
        if default is NOTHING:
            return self._mapping[type_]
        else:
            return self._mapping.get(type_, default)

    def get_type(self, alias, default=NOTHING):
        if default is NOTHING:
            return self._back[alias]
        else:
            return self._back.get(alias, default)


_registry = TypesRegistry()


def get_registry():
    return _registry
