"""Reusable absence evidence for one certified low-bit prefix.

The region starts free of nonempty requests.  Controlled slot writes then make
its membership known without inspecting any old request.  Reference counts keep
exactly the currently available part of that region, including restored points.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import MutableMapping


class ResidueCounts(MutableMapping):
    """Counters on a fixed finite universe, with constant-time active removal.

    Indexed storage gives deterministic word costs.  Only active entries need
    clearing at a region change; allocation of the two arrays occurs once.
    """

    def __init__(self, modulus):
        self.values = [0]*modulus
        self.positions = [0]*modulus
        self.active = []

    def __getitem__(self, key):
        value = self.values[key]
        if value == 0:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        if self.values[key] == 0:
            self.positions[key] = len(self.active)
            self.active.append(key)
        self.values[key] = value

    def __delitem__(self, key):
        if self.values[key] == 0:
            raise KeyError(key)
        position = self.positions[key]
        last = self.active.pop()
        if position < len(self.active):
            self.active[position] = last
            self.positions[last] = position
        self.values[key] = 0

    def __iter__(self):
        return iter(self.active)

    def __len__(self):
        return len(self.active)

    def clear(self):
        for key in self.active:
            self.values[key] = 0
        self.active.clear()


@dataclass
class Node:
    free: int
    left: Node | None = None
    right: Node | None = None


class FreeIndexTree:
    """Sparse binary successor tree; a missing node denotes a fully free range."""

    def __init__(self, size):
        self.size = size
        self.root = None
        self.events = dict(update_visits=0, query_visits=0, nodes_created=0)

    @staticmethod
    def _count(node, size):
        return size if node is None else node.free

    def _node(self, free):
        self.events['nodes_created'] += 1
        return Node(free)

    def set_free(self, index, available):
        def update(node, lo, hi):
            self.events['update_visits'] += 1
            size = hi-lo+1
            count = self._count(node, size)
            if (available and count == size) or (not available and count == 0):
                return node
            if lo == hi:
                return None if available else self._node(0)
            mid = (lo+hi)//2
            if node is None:
                node = self._node(size)
            elif count == 0:
                node.left = self._node(0)
                node.right = self._node(0)
            if index <= mid:
                node.left = update(node.left, lo, mid)
            else:
                node.right = update(node.right, mid+1, hi)
            node.free = self._count(node.left, mid-lo+1)+self._count(node.right, hi-mid)
            if node.free == size:
                return None
            if node.free == 0:
                node.left = node.right = None
            return node

        self.root = update(self.root, 0, self.size-1)

    def first(self, lower, upper):
        def find(node, lo, hi):
            self.events['query_visits'] += 1
            if hi < lower or lo > upper or (node is not None and node.free == 0):
                return None
            if node is None:
                return max(lo, lower)
            mid = (lo+hi)//2
            found = find(node.left, lo, mid)
            return found if found is not None else find(node.right, mid+1, hi)

        return None if lower > upper else find(self.root, 0, self.size-1)

    @property
    def free_count(self):
        return self._count(self.root, self.size)


class RegionEvidence:
    """One prefix region plus exact live request occupancy inside it.

    acquire() consumes an already proved empty prefix.  bind() consumes an
    original business program's complete code; copy() and drop() use their
    explicit slot effects.  There is no request-table access in this module.
    """

    def __init__(self, slots, width):
        self.slots = slots
        self.width = width
        self.modulus = 1 << width
        self.level = self.prefix = None
        self.delta = None
        self.tree = None
        self.members = [None]*slots
        self.marked = [False]*slots
        self.touched = []
        self.refs = ResidueCounts(self.modulus)
        self.events = dict(acquisitions=0, slot_writes=0, member_changes=0,
                           first_references=0, last_releases=0,
                           region_queries=0, region_hits=0, region_misses=0,
                           query_visits=0, update_visits=0, nodes_created=0,
                           retired_slot_marks=0)

    def acquire(self, level, prefix):
        for slot in self.touched:
            self.members[slot] = None
            self.marked[slot] = False
        self.events['retired_slot_marks'] += len(self.touched)
        self.touched.clear()
        self.refs.clear()
        self.level, self.prefix = level, prefix
        self.delta = 1 << level
        self.tree = FreeIndexTree(1 << (self.width-level))
        self.events['acquisitions'] += 1

    def _set_free(self, residue, available):
        before = self.tree.events.copy()
        self.tree.set_free((residue-self.prefix)//self.delta, available)
        for key in ('update_visits', 'nodes_created'):
            self.events[key] += self.tree.events[key]-before[key]

    def _write(self, slot, member):
        if self.tree is None:
            return
        self.events['slot_writes'] += 1
        previous = self.members[slot]
        if previous == member:
            return
        if not self.marked[slot]:
            self.marked[slot] = True
            self.touched.append(slot)
        if previous is not None:
            remaining = self.refs[previous]-1
            if remaining:
                self.refs[previous] = remaining
            else:
                del self.refs[previous]
                self._set_free(previous, True)
                self.events['last_releases'] += 1
        if member is not None:
            count = self.refs.get(member, 0)
            if count == 0:
                self._set_free(member, False)
                self.events['first_references'] += 1
            self.refs[member] = count+1
        self.members[slot] = member
        self.events['member_changes'] += 1

    def bind(self, slot, code):
        if self.tree is None:
            return
        residue = code % self.modulus
        member = residue if code != 0 and residue % self.delta == self.prefix else None
        self._write(slot, member)

    def copy(self, destination, source):
        if self.tree is not None:
            self._write(destination, self.members[source])

    def drop(self, slot):
        self._write(slot, None)

    def contains(self, residue):
        return (self.tree is not None and residue % self.delta == self.prefix
                and residue not in self.refs)

    def select(self, start, colors, preferred=None):
        if self.tree is None:
            return None
        self.events['region_queries'] += 1
        if (preferred is not None and self.contains(preferred)
                and (preferred-start) % self.modulus < colors):
            self.events['region_hits'] += 1
            return (preferred-start) % self.modulus
        first = (self.prefix-start) % self.delta
        if first >= colors:
            self.events['region_misses'] += 1
            return None
        count = 1+(colors-1-first)//self.delta
        residue = (start+first) % self.modulus
        index = (residue-self.prefix)//self.delta
        end = index+count-1
        before = self.tree.events['query_visits']
        found = self.tree.first(index, min(self.tree.size-1, end))
        if found is None and end >= self.tree.size:
            found = self.tree.first(0, end-self.tree.size)
        self.events['query_visits'] += self.tree.events['query_visits']-before
        if found is None:
            self.events['region_misses'] += 1
            return None
        self.events['region_hits'] += 1
        return (self.prefix+found*self.delta-start) % self.modulus

    def metrics(self):
        return dict(prefix=None if self.tree is None else [self.level, self.prefix],
                    free_count=None if self.tree is None else self.tree.free_count,
                    occupied_residues=len(self.refs), marked_slots=len(self.touched))
