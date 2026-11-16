from .collection import Collection as _Collection


class Collection(_Collection):

    def contains(self, item) -> bool:
        return item in self._items

    def size(self) -> int:
        return len(self._items)

    @classmethod
    def zip(cls, l1: 'Collection', l2: 'Collection') -> 'Collection':
        result = cls()
        items1 = list(l1)
        items2 = list(l2)
        for i in range(min(len(items1), len(items2))):
            result.add((items1[i], items2[i]))
        return result

    def pset(self) -> list:
        items = list(self)
        result = []
        def _bt(start, current):
            result.append(frozenset(current))
            for i in range(start, len(items)):
                _bt(i + 1, current + [items[i]])
        _bt(0, [])
        return result

    def pset_gen(self):
        items = list(self)
        def _gen(start, current):
            yield frozenset(current)
            for i in range(start, len(items)):
                yield from _gen(i + 1, current + [items[i]])
        yield from _gen(0, [])

    def perm(self) -> list:
        items = list(self)
        result = []
        def _bt(remaining, current):
            if not remaining:
                result.append(list(current))
                return
            for i in range(len(remaining)):
                _bt(remaining[:i] + remaining[i+1:], current + [remaining[i]])
        _bt(items, [])
        return result

    def perm_gen(self):
        items = list(self)
        def _gen(remaining, current):
            if not remaining:
                yield list(current)
                return
            for i in range(len(remaining)):
                yield from _gen(remaining[:i] + remaining[i+1:], current + [remaining[i]])
        yield from _gen(items, [])
