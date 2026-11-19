"""Exact Path/BRC extension for X6 relational V39 packet readout.

Entry point: run().  No numerical physical model or classical reference is used.
Every input leaf retains its three named signed reads and ordered packet word.
Each packet retains its full directed-ring expansion.  Only the declared
observer groups leaves, after composition in V39's exact frame action.
See V39_RELATIONAL_PACKET_COMPRESSION.md for the composition/observer proof.
"""

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations, permutations, product
import json
from pathlib import Path


SOURCE_REVISION = "ef720decf4a35a276e509964250571a55421b9f8"
R757_REVISION = "ed0b15b4ba948a21150969478d8a6941db76b11f"
NATIVE_CONTEXT = {
    "world": "HEARTBEAT_WORLD_NATIVE_X6",
    "cell_anchor": "fixed symbolic native Cell c",
    "selected_oriented_support": "three distinct native axes 0->1->2->0",
    "detector": "one fixed spatial axis j in the selected support",
    "window": "three consecutive shell reads with known first shell",
    "input_bridge": "prior fixed-port readout; common detector reference and delta=+1",
    "scope": "readout-to-loop extension; raw native force state is retained by the upstream carrier",
}
IDENTITY = (0, 1, 2)
RING_FRAME = {"A+": (0, 2, 1), "A-": (0, 2, 1),
              "B+": (1, 0, 2), "B-": (1, 0, 2)}
MACRO_RINGS = {"A": ("A+",), "B": ("B+",), "C": ("B-", "A-")}
RING_CURRENT = {"A+": (1, 0), "A-": (-1, 0),
                "B+": (0, 1), "B-": (0, -1)}
WORDS = tuple("".join(p) for p in permutations("ABC"))
SIGNS = tuple(product((-1, 1), repeat=3))


def after(later, earlier):
    """V39: h(path;next) = h(next) composed with h(path)."""
    return tuple(later[i] for i in earlier)


@dataclass(frozen=True)
class Packet:
    word: str
    directed_rings: tuple
    frame: tuple
    current: tuple


def make_packet(word):
    rings = tuple(ring for macro in word for ring in MACRO_RINGS[macro])
    frame = IDENTITY
    current = (0, 0)
    for ring in rings:
        frame = after(RING_FRAME[ring], frame)
        shift = RING_CURRENT[ring]
        current = (current[0] + shift[0], current[1] + shift[1])
    return Packet(word, rings, frame, current)


PACKETS = {word: make_packet(word) for word in WORDS}
MACROS = {word: make_packet(word) for word in "ABC"}
G = PACKETS["ACB"].frame
FRAMES = (IDENTITY, G, after(G, G))


@dataclass(frozen=True)
class Branch:
    """A labelled Path/BRC leaf; packet factors can be unfolded losslessly."""
    named_signed_reads: tuple
    controller: str
    ordered_packets: tuple
    source_dependencies: tuple
    frame_snapshots: tuple

    @property
    def full_ring_history(self):
        return tuple((step, ring)
                     for step, packet in enumerate(self.ordered_packets)
                     for ring in packet.directed_rings)

    @property
    def relation(self):
        y = tuple(item[1] for item in self.named_signed_reads)
        return (y[0] * y[1], y[1] * y[2], -y[0] * y[2])

    @property
    def current(self):
        return tuple(sum(p.current[i] for p in self.ordered_packets) for i in (0, 1))


def branch(signs, controller, words, dependencies):
    history = tuple(PACKETS[word] if word in PACKETS else MACROS[word] for word in words)
    now = IDENTITY
    snapshots = []
    for packet in history:
        now = after(packet.frame, now)
        snapshots.append(now)
    return Branch(tuple(zip(("shell_0", "shell_1", "shell_2"), signs)),
                  controller, history, dependencies, tuple(snapshots))


def separated_branch(signs, pairs):
    bits = tuple(sign == 1 for sign in signs)
    words = tuple(pair[bit] for pair, bit in zip(pairs, bits))
    return branch(signs, "source_separable", words,
                  (("shell_0",), ("shell_1",), ("shell_2",)))


def relational_branch(signs):
    # The machine stores precisely the previous sign between sample arrivals.
    # The external finite-window schedule says when samples 0, 1, 2 arrive.
    previous = signs[0]
    words = []
    for current in signs[1:]:
        words.append("ABC" if previous == current else "ACB")
        previous = current
    return branch(signs, "adjacent_relation", tuple(words),
                  (("shell_0", "shell_1"), ("shell_1", "shell_2")))


SINGLE_BLOCK_WORD = {(False, False): "ABC", (False, True): "ACB",
                     (True, False): "BAC", (True, True): "BCA"}


def single_block_branch(signs):
    """Three named shell signs -> one ABC-permutation Path/BRC branch.

    Query frame_snapshots[1] after the SECOND completed based macro, then
    complete the last macro. Online source memory is (first_change, previous)
    after read 1: two source bits. No hidden internal frame query is used.
    The observation decodes adjacent products, independent of the upstream
    fixed-generator versus feedback conversion from those products to r.
    """
    previous = signs[0]
    first_change = previous != signs[1]
    previous = signs[1]
    second_change = previous != signs[2]
    word = SINGLE_BLOCK_WORD[first_change, second_change]
    return branch(signs, "single_ABC_block_relational", tuple(word),
                  (("shell_0", "shell_1"),
                   ("shell_0", "shell_1", "shell_2"),
                   ("shell_0", "shell_1", "shell_2")))


SINGLE_BLOCK_DECODE = {
    make_packet(word[:2]).frame: (1 if not d1 else -1, 1 if not d2 else -1)
    for (d1, d2), word in SINGLE_BLOCK_WORD.items()
}


SINGLE_BLOCK_TWO_QUERY_DECODE = {
    (make_packet(word[:1]).frame, PACKETS[word].frame):
    (1 if not d1 else -1, 1 if not d2 else -1)
    for (d1, d2), word in SINGLE_BLOCK_WORD.items()
}


def decode_single_block(observed_second_macro_frame):
    """Return (y0*y1, y1*y2), using only the second-macro frame read."""
    return SINGLE_BLOCK_DECODE[tuple(observed_second_macro_frame)]


def decode_single_block_two_queries(first_macro_frame, final_frame):
    """Compatible two-read variant: after first macro and completed block."""
    return SINGLE_BLOCK_TWO_QUERY_DECODE[tuple(first_macro_frame), tuple(final_frame)]


def fibers(branches, observation):
    result = defaultdict(list)
    for leaf in branches:
        result[observation(leaf)].append(leaf)
    return result


def sufficient(branches, observation):
    return all(len({b.relation for b in f}) == 1
               for f in fibers(branches, observation).values())


def run():
    common = Counter({"A+": 1, "A-": 1, "B+": 1, "B-": 1})
    assert all(Counter(p.directed_rings) == common and p.current == (0, 0)
               for p in PACKETS.values())
    assert tuple(FRAMES.index(PACKETS[w].frame) for w in WORDS) == (0, 1, 2, 0, 0, 2)

    subsets = tuple(c for size in (1, 2, 3) for c in combinations(range(3), size))
    standard = [separated_branch(s, (("ABC", "ACB"),) * 3) for s in SIGNS]
    standard_rows = {}
    for keep in subsets:
        groups = fibers(standard, lambda b: tuple(b.frame_snapshots[k] for k in keep))
        bad = next((f for f in groups.values() if len({b.relation for b in f}) > 1), None)
        standard_rows["".join(str(k + 1) for k in keep)] = {
            "sufficient": bad is None, "output_count": len(groups),
            "largest_relation_fiber": max(len({b.relation for b in f}) for f in groups.values()),
            "witness": None if bad is None else [
                {"reads": b.named_signed_reads, "relation": b.relation,
                 "packets": [p.word for p in b.ordered_packets]} for b in bad]
        }
    assert [k for k, v in standard_rows.items() if v["sufficient"]] == ["123"]
    assert standard_rows["3"]["largest_relation_fiber"] == 3
    assert all(len({b.relation for b in f}) == 2
               for f in fibers(standard, lambda b: b.frame_snapshots[1]).values())
    assert sufficient(standard, lambda b: (b.frame_snapshots[1],
                                         b.named_signed_reads[1][1] * b.named_signed_reads[2][1]))
    assert sufficient(standard, lambda b: (b.frame_snapshots[1:],
                                         b.named_signed_reads[0][1] * b.named_signed_reads[2][1]))

    # Full source-separable six-word language; factors remain ordered Path data.
    option_pairs = tuple(product(WORDS, repeat=2))
    successful = Counter({"".join(str(k + 1) for k in c): 0 for c in subsets})
    encoding_count = 0
    for pairs in product(option_pairs, repeat=3):
        leaves = [separated_branch(s, pairs) for s in SIGNS]
        encoding_count += 1
        for keep in subsets:
            if sufficient(leaves, lambda b: tuple(b.frame_snapshots[k] for k in keep)):
                successful["".join(str(k + 1) for k in keep)] += 1
    assert encoding_count == 46656
    assert successful["123"] == 10648
    assert all(v == 0 for k, v in successful.items() if k != "123")

    relative = [relational_branch(s) for s in SIGNS]
    assert sufficient(relative, lambda b: b.frame_snapshots)
    assert not sufficient(relative, lambda b: b.frame_snapshots[-1])
    assert len(fibers(relative, lambda b: b.frame_snapshots)) == 4
    gauge_pairs = 0
    for leaf in relative:
        signs = tuple(sign for _, sign in leaf.named_signed_reads)
        mate = relational_branch(tuple(-x for x in signs))
        assert leaf.relation == mate.relation
        assert leaf.ordered_packets == mate.ordered_packets
        assert leaf.frame_snapshots == mate.frame_snapshots
        assert leaf.full_ring_history == mate.full_ring_history
        assert leaf.current == (0, 0)
        assert Counter(ring for _, ring in leaf.full_ring_history) == {
            "A+": 2, "A-": 2, "B+": 2, "B-": 2}
        gauge_pairs += 1

    # V39 future composition can append every S3 transport. These 6 cases
    # check the frame component; the proof also covers arbitrary future j.
    future_checks = 0
    for group in fibers(relative, lambda b: b.relation).values():
        for later in permutations(range(3)):
            assert len({after(later, b.frame_snapshots[-1]) for b in group}) == 1
            future_checks += 1

    single_block = [single_block_branch(s) for s in SIGNS]
    assert len(SINGLE_BLOCK_DECODE) == 4
    assert len(SINGLE_BLOCK_TWO_QUERY_DECODE) == 4
    assert sufficient(single_block, lambda b: b.frame_snapshots[1])
    assert sufficient(single_block, lambda b: (b.frame_snapshots[0], b.frame_snapshots[-1]))
    assert not sufficient(single_block, lambda b: b.frame_snapshots[-1])
    single_block_rows = []
    for leaf in single_block:
        signs = tuple(sign for _, sign in leaf.named_signed_reads)
        expected = (signs[0] * signs[1], signs[1] * signs[2])
        assert decode_single_block(leaf.frame_snapshots[1]) == expected
        assert decode_single_block_two_queries(leaf.frame_snapshots[0], leaf.frame_snapshots[-1]) == expected
        mate = single_block_branch(tuple(-s for s in signs))
        assert mate.ordered_packets == leaf.ordered_packets
        assert mate.frame_snapshots == leaf.frame_snapshots
        assert leaf.current == (0, 0)
        assert Counter(ring for _, ring in leaf.full_ring_history) == common
        single_block_rows.append({
            "reads": leaf.named_signed_reads,
            "adjacent_products": expected,
            "ordered_macros": [p.word for p in leaf.ordered_packets],
            "source_dependencies": leaf.source_dependencies,
            "full_directed_ring_history": leaf.full_ring_history,
            "frame_after_each_macro": leaf.frame_snapshots,
            "single_observation": leaf.frame_snapshots[1],
            "final_current": leaf.current,
        })
    for group in fibers(single_block, lambda b: b.relation).values():
        for later in permutations(range(3)):
            assert len({after(later, b.frame_snapshots[-1]) for b in group}) == 1
            future_checks += 1

    rows = []
    for leaf in relative:
        rows.append({
            "reads": leaf.named_signed_reads,
            "relation": leaf.relation,
            "ordered_packets": [p.word for p in leaf.ordered_packets],
            "source_dependencies": leaf.source_dependencies,
            "full_directed_ring_history": leaf.full_ring_history,
            "frame_snapshots": leaf.frame_snapshots,
            "frame_indices_in_e_g_g2": [FRAMES.index(h) for h in leaf.frame_snapshots]
        })
    return {
        "schema": "X6_V39_RELATIONAL_PATH_BRC_CHECK_V1",
        "source_revision": SOURCE_REVISION,
        "historical_R757_revision": R757_REVISION,
        "native_context": NATIVE_CONTEXT,
        "entrypoint": "check_v39_relational_packets.py:run",
        "input_carrier": "Eight named signed-shell Path/BRC leaves; source-separable code is an outer finite parameter, not a physical probability.",
        "operation_semantics": "Append source-defined ABC permutations, expand C as B-;A-, compose exact V39 frame actions, retain directed histories.",
        "observer_and_future_scope": "Fixed-window adjacent-sign relation; at the new controller's completion, all V39 L_JH based-loop futures.",
        "old_standard_frame_subsets": standard_rows,
        "all_source_separable_encoding_count": encoding_count,
        "successful_encodings_by_frame_subset": dict(successful),
        "new_controller_rows": rows,
        "single_block_controller_rows": single_block_rows,
        "single_block_decoder": [{"second_macro_frame": h, "adjacent_products": q}
                                 for h, q in SINGLE_BLOCK_DECODE.items()],
        "single_block_query_count": 1,
        "single_block_query_location": "after the second completed based macro, before the last macro",
        "single_block_source_memory_bits_without_internal_frame_queries": 2,
        "single_block_directed_loop_histogram": dict(common),
        "new_controller_source_memory_bits": 1,
        "new_controller_accumulated_xor_memory_bits": 0,
        "new_controller_uses_known_window_schedule": True,
        "all_sign_flip_checks": gauge_pairs,
        "all_S3_future_frame_checks": future_checks,
        "output_relation_states": 4,
        "residual_certificate": "Exact zero target ambiguity for both new packet-boundary frames; exact fiber witnesses for every old proper checkpoint subset. Physical event bridge remains an input condition.",
        "status": "PASS"
    }


if __name__ == "__main__":
    result = run()
    destination = Path(__file__).with_name("v39_relational_packet_results.json")
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "encodings": result["all_source_separable_encoding_count"],
                      "successful": result["successful_encodings_by_frame_subset"],
                      "relation_states": result["output_relation_states"],
                      "single_block_decoder": result["single_block_decoder"],
                      "result_path": str(destination)}, ensure_ascii=False))
