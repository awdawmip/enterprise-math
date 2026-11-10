"""Minimum original-word-cost selection inside genuinely certified regions.

The original reserve/bind/release words assign a key-dependent cost
2*popcount(K)+4*(1-bit_(b-1)(K)).  Physical result normalization is a
separate, key-independent term once the actual observation episode is fixed.
This module consumes empty-prefix evidence or the maintained region API; it
does not inspect an exact request table or issue an observation.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'regional'))
from region import RegionEvidence


def round_key_cost(key: int, width: int) -> int:
    """Key-dependent commands for successful reserve, present bind, release."""
    if width < 1 or key < 1:
        raise ValueError('A positive full key and positive low-key width are required')
    return 2*key.bit_count()+4*(1-((key >> (width-1)) & 1))


@dataclass(frozen=True)
class WindowPiece:
    quotient: int
    lower: int
    upper: int
    high_cost: int


@dataclass(frozen=True)
class TargetWindow:
    """Compile-time complete-key interval, split at its possible B boundary."""
    width: int
    start: int
    colors: int
    pieces: tuple[WindowPiece, ...]

    @classmethod
    def make(cls, width: int, start: int, colors: int) -> TargetWindow:
        modulus = 1 << width
        if width < 1 or start < 1 or not 1 <= colors <= modulus:
            raise ValueError('Expected positive key interval of at most B keys')
        finish = start+colors-1
        pieces = []
        current = start
        while current <= finish:
            quotient = current // modulus
            stop = min(finish, (quotient+1)*modulus-1)
            pieces.append(WindowPiece(quotient, current % modulus, stop % modulus,
                                      2*quotient.bit_count()))
            current = stop+1
        return cls(width, start, colors, tuple(pieces))


@dataclass
class CostNode:
    free: int
    best: tuple[int, int] | None
    left: CostNode | None = None
    right: CostNode | None = None


class WeightedFreeIndexTree:
    """Sparse range minimum tree on j, with a negative most significant bit.

    Missing node means that the entire aligned interval is free.  The best
    index in such an interval follows from its fixed high bits and the one
    negative bit; no leaf scan or initial full-tree construction is needed.
    """
    def __init__(self, width: int, *, negative_top=True):
        if width < 0:
            raise ValueError('Index width is nonnegative')
        self.width = width
        self.negative_top = bool(width and negative_top)
        self.size = 1 << width
        self.root = None
        self.events = dict(update_visits=0, query_visits=0, nodes_created=0)

    def cost(self, index: int) -> int:
        return 2*index.bit_count()-(4*((index >> (self.width-1)) & 1)
                                   if self.negative_top else 0)

    def _better(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        return min(first, second)

    def _all_free_best(self, lo, hi):
        # Every range passed here is a binary-aligned tree interval.
        high = 1 << (self.width-1) if self.width else 0
        return high if self.negative_top and lo <= high <= hi and not (lo & high) else lo

    @staticmethod
    def _count(node, size):
        return size if node is None else node.free

    def _free_pair(self, lo, hi, prefix_cost):
        bonus = -2 if self.negative_top and lo == 0 and hi == self.size-1 else 0
        return prefix_cost+bonus, self._all_free_best(lo, hi)

    def _best(self, node, lo, hi, prefix_cost):
        return self._free_pair(lo, hi, prefix_cost) if node is None else node.best

    def _right_cost(self, lo, hi, prefix_cost):
        bit = (hi-lo+1).bit_length()-2
        return prefix_cost+(-2 if self.negative_top and bit == self.width-1 else 2)

    def _node(self, free, best):
        self.events['nodes_created'] += 1
        return CostNode(free, best)

    def set_free(self, index: int, available: bool):
        if not 0 <= index < self.size:
            raise ValueError('Index outside certified region')

        def update(node, lo, hi, prefix_cost):
            self.events['update_visits'] += 1
            size = hi-lo+1
            count = self._count(node, size)
            if (available and count == size) or (not available and count == 0):
                return node
            if lo == hi:
                return None if available else self._node(0, None)
            mid = (lo+hi)//2
            right_cost = self._right_cost(lo, hi, prefix_cost)
            if node is None:
                node = self._node(size, self._free_pair(lo, hi, prefix_cost))
            elif count == 0:
                node.left = self._node(0, None)
                node.right = self._node(0, None)
            if index <= mid:
                node.left = update(node.left, lo, mid, prefix_cost)
            else:
                node.right = update(node.right, mid+1, hi, right_cost)
            node.free = self._count(node.left, mid-lo+1)+self._count(node.right, hi-mid)
            if node.free == size:
                return None
            if node.free == 0:
                node.best = None
                node.left = node.right = None
            else:
                node.best = self._better(self._best(node.left, lo, mid, prefix_cost),
                                         self._best(node.right, mid+1, hi, right_cost))
            return node

        self.root = update(self.root, 0, self.size-1, 0)

    def minimum(self, lower: int, upper: int):
        """Return a free index minimizing (weighted cost, index) in the range."""
        def find(node, lo, hi, prefix_cost):
            self.events['query_visits'] += 1
            if hi < lower or upper < lo or (node is not None and node.free == 0):
                return None
            if lower <= lo and hi <= upper:
                return self._best(node, lo, hi, prefix_cost)
            mid = (lo+hi)//2
            left = None if node is None else node.left
            right = None if node is None else node.right
            return self._better(find(left, lo, mid, prefix_cost),
                                find(right, mid+1, hi, self._right_cost(lo, hi, prefix_cost)))

        pair = None if lower > upper else find(self.root, 0, self.size-1, 0)
        return None if pair is None else pair[1]

    def first(self, lower, upper):
        """Ordinary successor retained for the inherited verifier/interface."""
        def find(node, lo, hi):
            self.events['query_visits'] += 1
            if hi < lower or upper < lo or (node is not None and node.free == 0):
                return None
            if node is None:
                return max(lo, lower)
            if lo == hi:
                return lo
            mid = (lo+hi)//2
            found = find(node.left, lo, mid)
            return found if found is not None else find(node.right, mid+1, hi)

        return None if lower > upper else find(self.root, 0, self.size-1)

    @property
    def free_count(self):
        return self._count(self.root, self.size)


def minimum_in_region(tree: WeightedFreeIndexTree, level: int, prefix: int,
                      window: TargetWindow):
    """Select the cheapest complete legal key, retaining quotient carry costs."""
    if tree.width+level != window.width:
        raise ValueError('Region and target widths differ')
    delta = 1 << level
    modulus = 1 << window.width
    best = None
    fixed_cost = 2*prefix.bit_count()+4
    if level == window.width:
        fixed_cost -= 4*((prefix >> (window.width-1)) & 1)
    for part in window.pieces:
        lower = max(0, (part.lower-prefix+delta-1)//delta)
        upper = min(tree.size-1, (part.upper-prefix)//delta)
        index = tree.minimum(lower, upper)
        if index is None:
            continue
        key = part.quotient*modulus+prefix+delta*index
        cost = part.high_cost+fixed_cost+tree.cost(index)
        candidate = cost, key
        if best is None or candidate < best:
            best = candidate
    return None if best is None else best[1]


def choose_empty_prefix(width: int, level: int, prefix: int, start_full: int,
                        colors: int, *, window=None, metrics=None):
    """Consume one already established empty prefix, with no further read."""
    window = TargetWindow.make(width, start_full, colors) if window is None else window
    tree = WeightedFreeIndexTree(width-level)
    key = minimum_in_region(tree, level, prefix, window)
    if metrics is not None:
        metrics['weighted_query_visits'] = metrics.get('weighted_query_visits', 0)+tree.events['query_visits']
    return key


def choose_observed_prefix(tree, start_full: int, colors: int, *, window=None,
                           metrics=None):
    """Choose among all empty classes proved by an observed low-prefix tree.

    A live label in a node's own bucket can still occupy any descendant, so
    traversal stops there.  Only genuinely empty nodes reached through drained
    ancestors supply certificates.  Known empty full-code labels may conservatively
    block residue zero in the inherited observation representation.
    """
    window = TargetWindow.make(tree.width, start_full, colors) if window is None else window
    best = None
    stack = [(0, 0)]
    visits = 0
    while stack:
        level, prefix = stack.pop()
        visits += 1
        index = tree.index(level, prefix)
        if tree.count[index] == 0:
            key = choose_empty_prefix(tree.width, level, prefix, start_full, colors,
                                      window=window, metrics=metrics)
            if key is not None:
                candidate = round_key_cost(key, tree.width), key
                if best is None or candidate < best:
                    best = candidate
        elif tree.head[index] is None and level < tree.width:
            stack.append((level+1, prefix | (1 << level)))
            stack.append((level+1, prefix))
    if metrics is not None:
        metrics['observed_prefix_visits'] = metrics.get('observed_prefix_visits', 0)+visits
    return None if best is None else best[1]


class WeightedRegionEvidence(RegionEvidence):
    """The existing exact slot/refcount invariant with weighted range queries."""
    def acquire(self, level, prefix):
        super().acquire(level, prefix)
        self.tree = WeightedFreeIndexTree(self.width-level)

    def select_key(self, start_full, colors, *, window=None):
        if self.tree is None:
            return None
        self.events['region_queries'] += 1
        window = TargetWindow.make(self.width, start_full, colors) if window is None else window
        before = self.tree.events['query_visits']
        key = minimum_in_region(self.tree, self.level, self.prefix, window)
        self.events['query_visits'] += self.tree.events['query_visits']-before
        self.events['region_hits' if key is not None else 'region_misses'] += 1
        return key

    def select(self, start_full, colors, preferred=None):
        """Return a color; start_full is the positive complete target start."""
        key = self.select_key(start_full, colors)
        return None if key is None else key-start_full


def fixed_region_schedule(keys, width, rounds, previous=None):
    """Optimal schedule for a fixed target, one overwritten slot, no new reads.

    keys is an explicitly supplied proved-safe set, such as a small reporting
    example. Production range selection uses the weighted tree above.
    """
    ordered = sorted(keys, key=lambda key: (round_key_cost(key, width), key))
    chosen = []
    for _ in range(rounds):
        key = next((key for key in ordered if key != previous), None)
        if key is None:
            return None
        chosen.append(key)
        previous = key
    return chosen


@dataclass(frozen=True)
class MaskSpec:
    """A fixed-bit class; free-bit packing preserves numerical ordering."""
    width: int
    mask: int
    value: int
    free_positions: tuple[int, ...]

    @classmethod
    def make(cls, width, mask, value):
        if width < 1 or not 0 <= mask < (1 << width) or value < 0 or value & ~mask:
            raise ValueError('Mask/value must define a low-width fixed-bit class')
        return cls(width, mask, value,
                   tuple(bit for bit in range(width) if not (mask >> bit) & 1))

    @property
    def size(self):
        return 1 << len(self.free_positions)

    @property
    def negative_top(self):
        return not ((self.mask >> (self.width-1)) & 1)

    def contains(self, residue):
        return (residue & self.mask) == self.value

    def unpack(self, index):
        return self.value+sum(((index >> digit) & 1) << bit
                              for digit, bit in enumerate(self.free_positions))

    def pack(self, residue):
        return sum(((residue >> bit) & 1) << digit
                   for digit, bit in enumerate(self.free_positions))

    def rank_le(self, bound):
        """Number of members <= bound, using at most width bit decisions."""
        if bound < 0:
            return 0
        if bound >= (1 << self.width)-1:
            return self.size
        count = 0
        free_left = len(self.free_positions)
        for bit in range(self.width-1, -1, -1):
            fixed = bool((self.mask >> bit) & 1)
            if not fixed:
                free_left -= 1
            digit = (bound >> bit) & 1
            fixed_digit = (self.value >> bit) & 1
            if digit and (not fixed or not fixed_digit):
                count += 1 << free_left
            if fixed and fixed_digit != digit:
                return count
        return count+1


def minimum_in_mask(tree: WeightedFreeIndexTree, spec: MaskSpec,
                    window: TargetWindow):
    """Cheapest legal free key in any genuinely empty fixed-bit class."""
    modulus = 1 << spec.width
    fixed_cost = 2*spec.value.bit_count()+4-4*((spec.value >> (spec.width-1)) & 1)
    best = None
    for part in window.pieces:
        lower = spec.rank_le(part.lower-1)
        upper = spec.rank_le(part.upper)-1
        index = tree.minimum(lower, upper)
        if index is None:
            continue
        key = part.quotient*modulus+spec.unpack(index)
        candidate = part.high_cost+fixed_cost+tree.cost(index), key
        if best is None or candidate < best:
            best = candidate
    return None if best is None else best[1]


def choose_empty_mask(width, mask, value, start_full, colors, *, window=None,
                      metrics=None):
    spec = MaskSpec.make(width, mask, value)
    window = TargetWindow.make(width, start_full, colors) if window is None else window
    tree = WeightedFreeIndexTree(len(spec.free_positions), negative_top=spec.negative_top)
    key = minimum_in_mask(tree, spec, window)
    if metrics is not None:
        metrics['weighted_query_visits'] = metrics.get('weighted_query_visits', 0)+tree.events['query_visits']
    return key


class MaskedRegionEvidence(RegionEvidence):
    """Exact live occupancy on a certified fixed-bit class, including high halves."""
    def acquire_mask(self, mask, value):
        super().acquire(0, 0)
        self.spec = MaskSpec.make(self.width, mask, value)
        self.mask, self.value = mask, value
        self.level = mask.bit_count() if mask & (mask+1) == 0 else None
        self.prefix = value
        self.delta = None if self.level is None else 1 << self.level
        self.tree = WeightedFreeIndexTree(len(self.spec.free_positions),
                                          negative_top=self.spec.negative_top)

    def acquire(self, level, prefix):
        self.acquire_mask((1 << level)-1, prefix)

    def _set_free(self, residue, available):
        before = self.tree.events.copy()
        self.tree.set_free(self.spec.pack(residue), available)
        for key in ('update_visits', 'nodes_created'):
            self.events[key] += self.tree.events[key]-before[key]

    def bind(self, slot, code):
        if self.tree is None:
            return
        residue = code % self.modulus
        member = residue if code != 0 and self.spec.contains(residue) else None
        self._write(slot, member)

    def contains(self, residue):
        return (self.tree is not None and self.spec.contains(residue)
                and residue not in self.refs)

    def select_key(self, start_full, colors, *, window=None):
        if self.tree is None:
            return None
        self.events['region_queries'] += 1
        window = TargetWindow.make(self.width, start_full, colors) if window is None else window
        before = self.tree.events['query_visits']
        key = minimum_in_mask(self.tree, self.spec, window)
        self.events['query_visits'] += self.tree.events['query_visits']-before
        self.events['region_hits' if key is not None else 'region_misses'] += 1
        return key

    def select(self, start_full, colors, preferred=None):
        key = self.select_key(start_full, colors)
        return None if key is None else key-start_full

    def metrics(self):
        return dict(mask=None if self.tree is None else self.mask,
                    value=None if self.tree is None else self.value,
                    free_count=None if self.tree is None else self.tree.free_count,
                    occupied_residues=len(self.refs), marked_slots=len(self.touched))
