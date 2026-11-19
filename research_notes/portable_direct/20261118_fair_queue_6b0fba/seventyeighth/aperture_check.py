#!/usr/bin/env python3
"""Finite-duration event models of the frozen three-channel recorder."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1
from itertools import combinations, product
from math import comb
import json
from pathlib import Path
import sys

PINS = {
    "research_tasks/RS-EULER-RECORDER-A02-FINITE-DURATION-20261012.md":
        "37b1dafa904bf09a4b225d7341aa057d848604a6",
    "research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md":
        "03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b",
    "research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md":
        "bd80290c259cc60995069613a5f4b5f5b41a13d1",
    "research_notes/chatgpt_direct/20261010_EULER_CONTROLLER_RELATIONAL_MEMORY.md":
        "22a7d072e54f40c52a94e91dac7f68f63371436c",
    "research_notes/chatgpt_direct/20261009_EULER_RECIPROCAL_ORIENTED_TRANSPORT.md":
        "63c37a1119032aca8720c853196abd26582151a3",
    "research_notes/chatgpt_direct/20261009_EULER_CONTACT_INTERLEAVED_HOLONOMY.md":
        "260ae808c4f5d567c2a8c2a77c74198af0ff6c64",
    "src/enterprise_math/brc_weighted.py": "3f205696709e847909958a153f8fe10d3f6b70f0",
    "src/enterprise_math/brc_logarithm.py": "4732e5fc381ce613d240c4381ccbef03c27a69c7",
    "src/enterprise_math/exact_arithmetic.py": "35ea95b0916494b83a92386e3e313928362dd79e",
}


def source(repo):
    if repo is None:
        repo = next((p for p in (Path.cwd(), *Path(__file__).resolve().parents)
                     if (p / next(iter(PINS))).is_file()), None)
    if repo is None:
        raise SystemExit("Pass --repo PATH to a checkout of the public source.")
    for name, digest in PINS.items():
        s = (repo / name).read_bytes()
        assert sha1(b"blob " + str(len(s)).encode() + b"\0" + s).hexdigest() == digest
    sys.path.insert(0, str(repo / "src"))
    from enterprise_math import brc_weighted
    return brc_weighted


def pulse(i, d, v, p, q):
    return (d == 1 and i == v) or (d == 2 and i in (p, q))


def timed_run(j, final_j, a, r, L, cut, v, p, q, sign=1):
    log = []
    channel = j
    reference = a
    for i in range(1, L + 1):
        if i == cut + 1:
            channel = final_j
            log.append("T")
        if pulse(i, (sign*(channel - reference)) % 3, v, p, q):
            log.append("contact")
            r = (r + sign) % 3
        else:
            log.append("hold")
    if cut == L:
        channel = final_j
        log.append("T")
    return channel, reference, r, log


def static_and_witness():
    tested = 0
    for v, j, a, r, sign in product((1, 2), range(3), range(3), range(3), (-1,1)):
        end, ref, result, log = timed_run(j, j, a, r, 2, 1, v, 1, 2, sign)
        assert (end, ref, result) == (j, a, (r + j - a) % 3)
        assert log.count("contact") == (sign*(j - a)) % 3
        tested += 1
    witness = []
    for cut in (0, 1, 2):
        end, ref, r, log = timed_run(0, 1, 1, 1, 2, cut, 1, 1, 2)
        witness.append(dict(cut=cut, events=log, end_source=end, reference=ref, receiver=r))
    assert [row["receiver"] for row in witness] == [1, 2, 0]
    tables = {}
    for v in (1, 2):
        tables[str(v)] = [[timed_run(x, y, 0, 0, 2, 1, v, 1, 2)[2]
                           for y in range(3)] for x in range(3)]
    return {"static_input_schedules": tested, "actual_frozen_source_transition": [0, 1],
            "reference_and_receiver_initially": [1, 1], "schedules": witness,
            "one_step_increments_by_first_then_second_difference": tables}


def source_atom(atom, command):
    j, sheet, F, w, theta = atom   # F1,F2,F3 from high to low bits
    if command == "H":
        if w in (0, 3) and theta == 0:
            return j, sheet, F ^ 3, 3-w, theta
        return atom
    if command == "U":
        return j, sheet ^ ((F >> 1) & 1), F ^ 7, w, theta ^ int(w in (1, 3))
    if command == "C":
        return (j + (-1)**sheet) % 3, sheet, F, w, theta
    raise ValueError(command)


def published_cycle(atom):
    j, s, F, w, theta = atom
    active = int(w in (0, 3) and theta == 0)
    new_w = 3-w if active else w
    new_sheet = s ^ ((F >> 1) & 1) ^ active
    return ((j + (-1)**new_sheet) % 3, new_sheet, F ^ (7 ^ (3*active)),
            new_w, theta ^ int(new_w in (1, 3)))


def interleaved_source():
    orders = []
    for slot_positions in combinations(range(5),2):
        src = iter("HUC")
        scans = iter("12")
        orders.append("".join(next(scans) if i in slot_positions else next(src) for i in range(5)))
    hist = Counter()
    tested = 0
    for atom in product(range(3),range(2),range(8),range(4),range(2)):
        expected = published_cycle(atom)
        for a, r0, v, sign in product(range(3), range(3), (1, 2), (-1,1)):
            for order in orders:
                cur = atom
                observed = {cur[0]}
                reg = r0
                for op in order:
                    if op in "HUC":
                        prev = cur
                        cur = source_atom(cur, op)
                        assert (prev[0] != cur[0]) == (op == "C")
                        observed.add(cur[0])
                    else:
                        reg = (reg + sign*pulse(int(op),(sign*(cur[0]-a))%3,v,1,2)) % 3
                assert cur == expected and observed == {atom[0],expected[0]}
                equivalent_channel = (reg-r0+a)%3
                failed = equivalent_channel not in observed
                assert failed == (order.index("1") < order.index("C") < order.index("2")
                                  and {(sign*(atom[0]-a))%3,(sign*(expected[0]-a))%3} == {0,2})
                hist[order] += failed
                tested += 1
    assert Fraction(sum(hist.values()),tested) == Fraction(1,10)
    for L in range(2,10):
        for m in range(1,7):
            counter = Counter()
            for slots in combinations(range(m+L),L):
                last_source = max(set(range(m+L))-set(slots))
                counter[sum(i < last_source for i in slots)] += 1
            assert all(counter[h] == comb(m+h-1,m-1) for h in range(L+1))
    return {"published_source_atoms":384, "combined_histories":tested,
            "nonserializable_by_order":dict(sorted(hist.items())),
            "failures":sum(hist.values()), "uniform_order_and_reference":"1/10",
            "atom_example_H_U_C": [list(atom) for atom in witness_atom_history()]}


def witness_atom_history():
    atom = (0, 0, 0, 1, 0)
    yield atom
    for op in "HUC":
        atom = source_atom(atom, op)
        yield atom


def all_single_jumps():
    rows = []
    cuts_tested = 0
    for L in range(2, 11):
        bad_counts = Counter()
        for p, q in combinations(range(1, L + 1), 2):
            for v in range(1, L + 1):
                bad_over_cuts_and_references = 0
                for h in range(L + 1):
                    bad_pairs = set()
                    for x, y in product(range(3), repeat=2):
                        end, _, result, _ = timed_run(x, y, 0, 0, L, h, v, p, q)
                        assert end == y
                        predicted = (({x, y} == {0, 2} and p <= h < q) or
                                     ({x, y} == {1, 2} and (v <= h < p or q <= h < v)))
                        assert (result not in (x, y)) == predicted
                        if predicted:
                            bad_pairs.add((x, y))
                        cuts_tested += 1
                    for i, j in product(range(3), repeat=2):
                        if i != j:
                            bad = sum(((i-a) % 3, (j-a) % 3) in bad_pairs for a in range(3))
                            assert bad == int(min(v,p) <= h < max(v,q))
                            if (i, j) == (0, 1):
                                bad_over_cuts_and_references += bad
                span = max(v, q) - min(v, p)
                assert span == bad_over_cuts_and_references
                bad_counts[span] += 1
        assert min(bad_counts) == 1 and max(bad_counts) == L - 1
        # Hide a uniformly chosen adjacent pulse pair from an oblivious schedule.
        for h in range(1, L):
            assert sum(p <= h < p+1 for p in range(1, L)) == 1
        rows.append(dict(slots=L, programs=sum(bad_counts.values()),
                         span_histogram=dict(sorted(bad_counts.items())),
                         best_uniform_reference_and_cut=str(Fraction(1, 3*(L-1))),
                         random_pair_oblivious_worst_case=str(Fraction(1, L-1))))
    return {"cases": cuts_tested, "slot_lengths": rows}


def general_histories(brc):
    cases = 0
    for L in range(2, 7):
        for p,q in combinations(range(L), 2):
            for v in range(L):
                for path in product(range(3), repeat=L):
                    count = sum(pulse(i, d, v,p,q) for i,d in enumerate(path))
                    direct = (int(path[v]==1) + int(path[p]==2) + int(path[q]==2)) % 3
                    assert direct == count % 3
                    missing_one = set(path) == {0, 2} and (path[p] == 2) != (path[q] == 2)
                    missing_zero = (set(path) == {1, 2} and path[p] == path[q]
                                    and path[v] != path[p])
                    assert (direct not in path) == (missing_one or missing_zero)
                    cases += 1
    # A common positive mass per history, intentionally correlated with readiness.
    words = list(product(range(3), repeat=5))  # a, j1, j2, j3, readiness error
    bins = defaultdict(lambda: brc.CWM_ZERO)
    norm = len(words) * (len(words) + 1) // 2
    for index, (a, j1, j2, j3, error) in enumerate(words, 1):
        reg = (a + error) % 3
        weight = brc.cwm_edge(Fraction(index, norm))
        for i, j in enumerate((j1, j2, j3), 1):
            reg = (reg + pulse(i, (j-a)%3, 2, 1, 3))%3
            weight = brc.cwm_propagate(weight, brc.cwm_edge(1))
        dup = (int((j2-a)%3 == 1)+int((j1-a)%3 == 2)+int((j3-a)%3 == 2))%3
        assert (reg-j3)%3 == (error + dup - (j3-a))%3
        bins[(reg-j3)%3] = brc.cwm_recoalesce(bins[(reg-j3)%3], weight)
    assert sum(b.total for b in bins.values()) == 1
    return {"arbitrary_sample_words_and_schedules": cases,
            "positive_weight_worlds": len(words),
            "end_error_mass": {str(k): str(b.total) for k,b in sorted(bins.items())}}


def latch_sufficiency_and_necessity():
    census = Counter()
    for first in product((0, 1), repeat=3):
        for last in product((0, 1), repeat=6):
            # The second slot is even allowed to read the first action / ready receiver.
            out = lambda x,y: first[x]+last[3*first[x]+y]
            if all(out(x,x) == x for x in range(3)):
                bad = sum(out(x,y) not in (x,y) for x,y in product(range(3), repeat=2))
                census[bad] += 1
    assert min(census) >= 1
    general = []
    for n in range(2, 65):
        states = {}
        for d in range(n):
            act = d%2
            if n%2 and d==n-1:
                act = 1
            state = d//2
            remain = d-act
            assert 0 <= remain <= n-2
            assert states.setdefault(state, remain) == remain
            assert (act+remain)%n == d
        assert len(states) == (n+1)//2
        general.append({"labels":n, "scratch_states":len(states)})
    return {"two_slot_programs_with_receiver_feedback": 8*64,
            "static_exact_programs_by_number_of_nonserializable_ordered_inputs":
                dict(sorted(census.items())),
            "first_snapshot_latch_generalization":general}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--repo", type=Path)
    cli.add_argument("--out", type=Path)
    args = cli.parse_args()
    brc = source(args.repo)
    data = {"pinned_public_blobs": PINS, "native_adapter_replayed": False,
            "two_slots":static_and_witness(), "old_source_commands":interleaved_source(),
            "single_jump":all_single_jumps(),
            "multiple_updates":general_histories(brc), "latch":latch_sufficiency_and_necessity()}
    out = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)

if __name__ == "__main__":
    main()
