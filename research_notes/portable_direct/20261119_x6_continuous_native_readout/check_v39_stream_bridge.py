"""Exact named Path/BRC verifier for the repeatable one-query V39 code.

Run: python check_v39_stream_bridge.py
No external dependencies or scratch-only paths. Source-defined A/B paths and
V39 transport actions are expanded explicitly; complete source and path names
are retained in each leaf. Only the declared observation projects that carrier.
"""

from collections import Counter
from dataclasses import asdict, dataclass
from itertools import product
import json
from pathlib import Path


E = (0, 1, 2)
A = (0, 2, 1)
B = (1, 0, 2)
G = (2, 0, 1)
T = (2, 1, 0)
G2 = (1, 2, 0)
PHASE_FRAME = (E, G)
WORDS = ("ABC", "ACB", "BAC", "BCA", "CAB", "CBA")
MACRO_RINGS = {"A": ("A+",), "B": ("B+",), "C": ("B-", "A-")}
RING_PATH = {
    "A+": ("012", "013", "023", "012"),
    "A-": ("012", "023", "013", "012"),
    "B+": ("012", "023", "123", "012"),
    "B-": ("012", "123", "023", "012"),
}
RING_FRAME = {"A+": A, "A-": A, "B+": B, "B-": B}
RING_CURRENT = {"A+": (1, 0), "A-": (-1, 0), "B+": (0, 1), "B-": (0, -1)}
RELATIONS = tuple(product((1, -1), repeat=2))
CODE = {
    (0, (1, 1)): "ABC", (1, (1, 1)): "BAC",
    (0, (1, -1)): "ACB", (1, (1, -1)): "CAB",
    (0, (-1, 1)): "BCA", (1, (-1, 1)): "CBA",
    (0, (-1, -1)): "CAB", (1, (-1, -1)): "BCA",
}
DECODE = {G2: (1, 1), T: (1, -1), A: (-1, 1), B: (-1, -1)}
NEXT_PHASE = {
    (0, (1, 1)): 0, (1, (1, 1)): 0,
    (0, (1, -1)): 1, (1, (1, -1)): 1,
    (0, (-1, 1)): 0, (1, (-1, 1)): 0,
    (0, (-1, -1)): 0, (1, (-1, -1)): 1,
}


def after(later, earlier):
    return tuple(later[i] for i in earlier)


def transport(word):
    h = E
    for macro in word:
        for ring in MACRO_RINGS[macro]:
            h = after(RING_FRAME[ring], h)
    return h


@dataclass(frozen=True)
class NamedRead:
    name: str
    source_event: int
    sign: int


@dataclass(frozen=True)
class RingOccurrence:
    window: str
    macro_position: int
    within_macro: int
    direction: str
    based_support_path: tuple


@dataclass(frozen=True)
class WindowBranch:
    window: str
    named_reads: tuple
    initial_phase: int
    initial_frame: tuple
    relation: tuple
    macro_word: str
    directed_history: tuple
    frame_after_macros: tuple
    decoded_relation: tuple
    final_phase: int
    current: tuple


def execute_window(window, named_reads, phase, initial_frame=None):
    """Append one complete, source-tagged block to the actual frame carrier."""
    if len(named_reads) != 3:
        raise ValueError("Three consecutive named samples are required")
    first = named_reads[0].source_event
    if tuple(x.source_event for x in named_reads) != (first, first + 1, first + 2):
        raise ValueError("Delivery adjacency does not replace consecutive source indices")
    if any(x.sign not in (-1, 1) for x in named_reads):
        raise ValueError("Sample sign must be exact +1 or -1")
    h = PHASE_FRAME[phase] if initial_frame is None else initial_frame
    if h != PHASE_FRAME[phase]:
        raise ValueError("Carried phase must match actual accumulated frame")
    y = tuple(x.sign for x in named_reads)
    q = (y[0] * y[1], y[1] * y[2])
    word = CODE[phase, q]
    initial = h
    history = []
    snapshots = []
    current = (0, 0)
    for macro_position, macro in enumerate(word):
        for within_macro, ring in enumerate(MACRO_RINGS[macro]):
            path = RING_PATH[ring]
            assert path[0] == path[-1] == "012"
            history.append(RingOccurrence(window, macro_position, within_macro, ring, path))
            h = after(RING_FRAME[ring], h)
            change = RING_CURRENT[ring]
            current = (current[0] + change[0], current[1] + change[1])
        snapshots.append(h)
    decoded = DECODE[snapshots[1]]
    final_phase = NEXT_PHASE[phase, q]
    assert decoded == q
    assert h == PHASE_FRAME[final_phase]
    assert current == (0, 0)
    assert Counter(x.direction for x in history) == {"A+": 1, "A-": 1, "B+": 1, "B-": 1}
    return WindowBranch(window, tuple(named_reads), phase, initial, q, word,
                        tuple(history), tuple(snapshots), decoded, final_phase, current)


def reads_for_relation(q, start, label, initial_sign=1):
    signs = (initial_sign, initial_sign * q[0], initial_sign * q[0] * q[1])
    return tuple(NamedRead(f"{label}:source_{start + i}", start + i, s)
                 for i, s in enumerate(signs))


def repeated_word_query_orbit(word):
    h = E
    seen = set()
    for _ in range(3):
        seen.add(after(transport(word[:2]), h))
        h = after(transport(word), h)
    return seen


def anti_periodic_sign(initial_word, t):
    return initial_word[t % 3] * (-1 if (t // 3) % 2 else 1)


def run():
    # BRC branch population: full named signs at each source-event triple.
    leaves = []
    sign_reversal_checks = 0
    for phase, signs in product((0, 1), product((-1, 1), repeat=3)):
        reads = tuple(NamedRead(f"source_{i}", i, sign) for i, sign in enumerate(signs))
        leaf = execute_window(f"phase_{phase}_word_{signs}", reads, phase)
        mate = execute_window("reversed", tuple(NamedRead(x.name, x.source_event, -x.sign)
                                               for x in reads), phase)
        assert leaf.relation == mate.relation
        assert leaf.macro_word == mate.macro_word
        assert leaf.frame_after_macros == mate.frame_after_macros
        assert [(x.direction, x.based_support_path) for x in leaf.directed_history] == [
            (x.direction, x.based_support_path) for x in mate.directed_history]
        assert leaf.named_reads != mate.named_reads
        leaves.append(leaf)
        sign_reversal_checks += 1

    # Composition never resets to E: the actual previous final frame is passed.
    pair_stream_checks = 0
    joint_boundary_states = set()
    for phase, q0, q1 in product((0, 1), RELATIONS, RELATIONS):
        first = execute_window("first", reads_for_relation(q0, 0, "first"), phase)
        second = execute_window("second", reads_for_relation(q1, 3, "second", -1),
                                first.final_phase, first.frame_after_macros[-1])
        full_history = first.directed_history + second.directed_history
        assert len(full_history) == 8
        assert {x.window for x in full_history} == {"first", "second"}
        assert Counter(x.direction for x in full_history) == {"A+": 2, "A-": 2, "B+": 2, "B-": 2}
        if phase == 0:
            joint_boundary_states.add((second.decoded_relation, second.final_phase))
        pair_stream_checks += 1
    assert len(joint_boundary_states) == 5

    stateless_encoders = 0
    stateless_successes = 0
    for words in product(WORDS, repeat=4):
        orbits = [repeated_word_query_orbit(w) for w in words]
        disjoint = all(orbits[i].isdisjoint(orbits[j]) for i in range(4) for j in range(i))
        stateless_encoders += 1
        stateless_successes += disjoint
    assert stateless_encoders == 1296 and stateless_successes == 0

    # Repeated disjoint and sliding windows of the exact source recurrence.
    native_stream_windows = 0
    native_joint_boundary_states = set()
    for initial_word in product((-1, 1), repeat=3):
        for spacing in (1, 3):
            p = 0
            h = E
            q_previous = None
            for k in range(8):
                start = spacing * k
                reads = tuple(NamedRead(f"source_{start+i}", start+i,
                                       anti_periodic_sign(initial_word, start+i)) for i in range(3))
                leaf = execute_window(f"spacing_{spacing}_window_{k}", reads, p, h)
                if q_previous is not None:
                    expected = q_previous if spacing == 3 else (q_previous[1], -q_previous[0]*q_previous[1])
                    assert leaf.decoded_relation == expected
                q_previous = leaf.decoded_relation
                p, h = leaf.final_phase, leaf.frame_after_macros[-1]
                assert p == int(leaf.decoded_relation == (1, -1))
                native_joint_boundary_states.add((leaf.decoded_relation, p))
                native_stream_windows += 1
    assert len(native_joint_boundary_states) == 4

    # Source-event adjacency is a typed input condition, not a wall-clock assumption.
    bad_reads = (NamedRead("s0", 0, 1), NamedRead("s1", 1, 1), NamedRead("s3", 3, 1))
    rejected_gap = False
    try:
        execute_window("gap", bad_reads, 0)
    except ValueError:
        rejected_gap = True
    assert rejected_gap

    table = []
    for phase, q in product((0, 1), RELATIONS):
        row = execute_window(f"table_{phase}_{q}", reads_for_relation(q, 0, "table"), phase)
        table.append({"initial_phase": phase, "q": q, "word": row.macro_word,
                      "observed_frame": row.frame_after_macros[1], "final_phase": row.final_phase})
    return {
        "schema": "X6_V39_REPEATABLE_ONE_QUERY_CODE_V1",
        "status": "PASS",
        "source_revision": "ef720decf4a35a276e509964250571a55421b9f8",
        "r757_revision": "ed0b15b4ba948a21150969478d8a6941db76b11f",
        "input_carrier": "Named signed samples at consecutive source-event indices; ordered actual directed based-ring paths",
        "operation_semantics": "Exact V39 later-after-earlier composition; append one named ABC permutation without reset",
        "observer_scope": "One absolute S3 frame query after the second completed macro, every completed window",
        "retained_provenance": "All named sample leaves, source-event indices, macro order and directed ring support paths",
        "controller_memory_scope": "One carried network phase bit plus two current source bits; stage/handshake/provenance separate",
        "timing_scope": "Conditional paced/retained-window interface; no native clock synchronization or force permission inferred",
        "counts": {"signed_window_branches": len(leaves), "sign_reversal_checks": sign_reversal_checks,
                   "two_window_compositions": pair_stream_checks, "stateless_encoders": stateless_encoders,
                   "successful_stateless_encoders": stateless_successes,
                   "anti_periodic_source_stream_windows": native_stream_windows,
                   "general_joint_relation_frame_classes": len(joint_boundary_states),
                   "single_source_joint_relation_frame_classes": len(native_joint_boundary_states)},
        "source_index_gap_rejected": rejected_gap,
        "table": table,
        "example_full_named_brc_branch": asdict(leaves[5]),
        "residual_certificate": "Zero decoder ambiguity at either carried phase; exact closure in two final phases; every stateless encoder has a repeated-constant-input collision",
    }


if __name__ == "__main__":
    result = run()
    path = Path(__file__).with_name("v39_stream_bridge_results.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], **result["counts"]}, ensure_ascii=False))
