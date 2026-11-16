"""Exact two-event observations of the conditional R762CA/CB authorization model.

Run with Python 3 and no external dependencies. Ports 0, 1, 2 form a
directed Link cycle. Native-axis names are 0..5 (software indices).
An event replaces the axis at the named Port and records its full source.
Keeping the other two assignments is precisely V17/V38 slot inheritance.
The calculation counts legal sources, without imposing a physical branch law.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations, product


PORTS = range(3)
AXES = range(6)
START = (0, 1, 2)
TARGET_AXIS = 3
REPRESENTATIVES = ((1, 1, 1), (-1, -1, -1), (-1, 1, 1), (1, -1, -1))
EXCLUDED = -1
HOMOGENEOUS = (EXCLUDED, 0, 7)
MIXED = tuple(range(EXCLUDED, 8))


def rotate(word, amount):
    return word[amount:] + word[:amount]


def bits(mask):
    return tuple((mask >> p) & 1 for p in PORTS)


def mask_of(enabled):
    return sum(bit << p for p, bit in enumerate(enabled))


def moves(frame, enabled):
    for p, allowed in enumerate(enabled):
        if allowed:
            for new_axis in AXES:
                if new_axis not in frame:
                    after = frame[:p] + (new_axis,) + frame[p + 1:]
                    yield (p, frame[p], new_axis), after


def signed_end(frame, signs):
    return {axis: signs[p] for p, axis in enumerate(frame)}


@lru_cache(maxsize=None)
def observe_word(signs, mask):
    """Keep each ordered pair of source events before evaluating its end."""
    enabled = bits(mask)
    k = sum(enabled)
    support_counts = []
    same_signed_end = 0
    root_sign_counts = Counter()
    rooted_link_counts = Counter()
    for p in PORTS:
        direct = START[:p] + (TARGET_AXIS,) + START[p + 1:]
        support = frozenset(direct)
        histories = []
        for first, middle in moves(START, enabled):
            for second, end in moves(middle, enabled):
                if frozenset(end) == support:
                    histories.append((first, second, end))
        assert len({(a, b) for a, b, _ in histories}) == len(histories)
        if not enabled[p]:
            assert not histories
            continue
        names_match = sum(end == direct for _, _, end in histories)
        signs_match = sum(signed_end(end, signs) == signed_end(direct, signs)
                          for _, _, end in histories)
        same_sign_enabled = sum(enabled[q] for q in PORTS if signs[p] == signs[q])
        assert (len(histories), names_match, signs_match) == (k + 1, 2, same_sign_enabled + 1)
        support_counts.append(len(histories))
        same_signed_end += signs_match
        root_sign_counts[signs[p]] += len(histories)
        rooted_link_counts[signs[p], signs[(p + 1) % 3]] += len(histories)
    # Nonzero support counts identify the active roots even when signs coincide.
    rooted_presence = tuple(p for p in PORTS if enabled[p])
    assert len(support_counts) == len(rooted_presence)
    return (sum(support_counts), same_signed_end,
            tuple(sorted(root_sign_counts.items())), tuple(sorted(rooted_link_counts.items())))


def sector_observation(rep, mask):
    """Quotient by cyclic rotations only, retaining sector and Link direction."""
    if mask == EXCLUDED:
        return None
    rotations = {rotate(rep, r): mask_of(rotate(bits(mask), r)) for r in PORTS}
    observations = {observe_word(signs, moved_mask) for signs, moved_mask in rotations.items()}
    assert len(observations) == 1
    return observations.pop()


def classify():
    histograms = {name: Counter() for name in
                  ("returns", "support", "signed_agreement", "root_sign",
                   "root_and_successor_sign", "full_positive_sources")}
    closures = set()
    for policy in product(HOMOGENEOUS, HOMOGENEOUS, MIXED, MIXED):
        n = [0] * 4
        signatures = [[], [], [], []]
        for rep, mask in zip(REPRESENTATIVES, policy):
            obs = sector_observation(rep, mask)
            if obs is None:
                for signature in signatures:
                    signature.append(None)
                continue
            multiplicity = len({rotate(rep, r) for r in PORTS})
            n[sum(bits(mask))] += multiplicity
            # In a closed sector, empty permission has zero sources. At depth
            # zero the observer can read the selected sector's closure status.
            total, signed_agree, root_sign, link_sign = obs
            for signature, value in zip(signatures, (total, (total, signed_agree),
                                                     (total, root_sign), (total, link_sign))):
                signature.append(value)
        closures.add(tuple(mask != EXCLUDED for mask in policy))
        n = tuple(n)
        histograms["returns"][n] += 1
        for name, signature in zip(
            ("support", "signed_agreement", "root_sign", "root_and_successor_sign"), signatures
        ):
            histograms[name][tuple(signature)] += 1
        # For this observer only n (incl. total zero-length availability)
        # is retained at length zero. At positive length, sector-tagged,
        # directed two-sign roots identify each nonempty permission mask.
        # An excluded sector and a closed sector with no move both lack paths.
        positive = tuple(() if not sector else sector[1] for sector in signatures[3])
        histograms["full_positive_sources"][n, positive] += 1
    assert len(closures) == 16
    expected = {
        "returns": (90, {1: 9, 2: 18, 4: 9, 6: 18, 9: 6, 12: 18, 18: 9, 36: 3}),
        "support": (225, {1: 81, 3: 108, 9: 36}),
        "signed_agreement": (324, {1: 144, 2: 72, 3: 72, 4: 9, 6: 18, 9: 9}),
        "root_sign": (441, {1: 225, 2: 180, 4: 36}),
        "root_and_successor_sign": (729, {1: 729}),
        "full_positive_sources": (640, {1: 553, 2: 86, 4: 1}),
    }
    for name, hist in histograms.items():
        assert sum(hist.values()) == 729
        sizes = dict(sorted(Counter(hist.values()).items()))
        assert (len(hist), sizes) == expected[name]
        print(name, "classes", len(hist), "fiber size -> number of classes", sizes)


def agreement_at_depth_two(signs, enabled, root):
    """Expand both sides of every permitted midpoint, then replay all events."""
    direct = START[:root] + (TARGET_AXIS,) + START[root + 1:]
    start_support, end_support = frozenset(START), frozenset(direct)
    fixed_axes = {START[i] for i in PORTS if not enabled[i]}
    vertices = [frozenset(triad) for triad in combinations(AXES, 3)
                if fixed_axes.issubset(triad)]

    def middle_vertices(left, right):
        return [v for v in vertices if len(v & left) == len(v & right) == 2]

    matching, total = 0, 0
    for middle in middle_vertices(start_support, end_support):
        for first in middle_vertices(start_support, middle):
            for last in middle_vertices(middle, end_support):
                frame = START
                for target in (first, middle, last, end_support):
                    # For adjacent supports the old and new axes determine
                    # at most one event. Its changing Port must be enabled.
                    event, frame = next((event, end) for event, end in moves(frame, enabled)
                                        if frozenset(end) == target)
                    assert enabled[event[0]]
                matching += signed_end(frame, signs) == signed_end(direct, signs)
                total += 1
    assert total == (1 + sum(enabled)) ** 3
    return matching


def aggregated_observers():
    # Aggregate all closed sign words. The root's directed two-sign label
    # remains visible, while the sector and its zero-length identity do not.
    two_counts = {}
    for signs in product((1, -1), repeat=3):
        for mask in range(1, 8):
            enabled = bits(mask)
            for p in PORTS:
                if enabled[p]:
                    ell = sum(enabled[q] for q in PORTS if signs[p] == signs[q])
                    key = (sum(enabled), ell)
                    value = agreement_at_depth_two(signs, enabled, p)
                    assert two_counts.setdefault(key, value) == value
    assert two_counts == {(1, 1): 8, (2, 1): 14, (2, 2): 27,
                          (3, 1): 24, (3, 2): 34, (3, 3): 64}

    counts = {observer: Counter() for observer in ("one", "two", "both", "all_depths")}
    cells_from_two = {}
    examples = {}
    two_signs = tuple(product((1, -1), repeat=2))
    for policy in product(HOMOGENEOUS, HOMOGENEOUS, MIXED, MIXED):
        n = [0] * 4
        cells = Counter()
        one = Counter()
        two = Counter()
        for rep, mask in zip(REPRESENTATIVES, policy):
            if mask == EXCLUDED:
                continue
            multiplicity = len({rotate(rep, r) for r in PORTS})
            enabled = bits(mask)
            k = sum(enabled)
            n[k] += multiplicity
            for p in PORTS:
                if enabled[p]:
                    pair = rep[p], rep[(p + 1) % 3]
                    ell = sum(enabled[q] for q in PORTS if rep[p] == rep[q])
                    cells[pair, k, ell] += multiplicity
                    one[pair] += multiplicity * (1 + ell)
                    two[pair] += multiplicity * two_counts[k, ell]
        n = tuple(n)
        one_signature = tuple(one[label] for label in two_signs)
        two_signature = tuple(two[label] for label in two_signs)
        cell_signature = tuple(sorted(cells.items()))
        # All depths factor through (n,cells). For each root, renaming axes
        # and permuting the active slots while preserving the root and its
        # same-sign class gives a source-preserving bijection. Comparing only
        # signed agreement permits simultaneous color reversal. Inactive
        # slots keep their initial axes. Thus (k,ell) determines the signed
        # agreement count on every recursively subdivided tree. At depth two
        # we test the converse on the entire finite policy space below.
        assert cells_from_two.setdefault((n, two_signature), cell_signature) == cell_signature
        counts["one"][n, one_signature] += 1
        counts["two"][n, two_signature] += 1
        counts["both"][n, one_signature, two_signature] += 1
        counts["all_depths"][n, cell_signature] += 1
        if policy in ((0, 0, 2, 5), (0, 0, 3, 1)):
            examples[policy] = n, one_signature, two_signature

    for observer, hist in counts.items():
        sizes = dict(sorted(Counter(hist.values()).items()))
        expected = {1: 399, 2: 141, 4: 12} if observer == "one" else {1: 427, 2: 131, 4: 10}
        assert sizes == expected and sum(hist.values()) == 729
        print("pooled directed sign pairs", observer, "classes", len(hist), "fibers", sizes)
    assert examples == {
        (0, 0, 2, 5): ((2, 3, 3, 0), (6, 6, 6, 0), (24, 42, 42, 0)),
        (0, 0, 3, 1): ((2, 3, 3, 0), (6, 6, 6, 0), (42, 24, 42, 0)),
    }
    print("all-sector example (return vector, depth one, depth two)", examples)


if __name__ == "__main__":
    classify()
    aggregated_observers()
