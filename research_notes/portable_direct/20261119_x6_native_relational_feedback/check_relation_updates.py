#!/usr/bin/env python3
"""Exact author checks for the V5 three-source relational observer.

All arithmetic uses signs in {-1, +1}; no floating-point approximation.
The model is a named three-axis observer embedded in Heartbeat X6.
This checker does not decide native TRIADIC_CLOSURE_E event permission.
"""

from collections import defaultdict
from dataclasses import dataclass
from itertools import permutations, product
import json
from pathlib import Path


SIGNS = tuple(product((-1, 1), repeat=3))
TWISTS = tuple(x for x in SIGNS if x[0] * x[1] * x[2] == -1)
CHANGES = tuple(x for x in SIGNS if x[0] * x[1] * x[2] == 1)


@dataclass(frozen=True)
class Token:
    source: str
    axis: int
    sign: int


@dataclass(frozen=True)
class TokenBranch:
    source: str
    ingress: tuple
    egress: tuple
    primitive_steps: tuple
    branch_name: str = "INNER"
    multiplicity: int = 1


@dataclass(frozen=True)
class AtomicScatter:
    generator: tuple
    joint_branches: tuple


@dataclass(frozen=True)
class ReferenceTransport:
    edge_signs: tuple


@dataclass(frozen=True)
class NamedTriadBRC:
    """Source-preserving atomic-III sublanguage of the signed-X6 BRC lift.

    The anchor is a chosen X6 Cell; axes 0,1,2 are a declared embedded
    observer. Each token branch has unit nonnegative multiplicity while
    radial signs remain typed attributes, never signed branch masses.
    History order is relational event order, not a physical heartbeat unit.
    """

    anchor: tuple
    sources: tuple
    tokens: tuple
    history: tuple = ()

    @classmethod
    def lift(cls, s, token_axes=(0, 1, 2)):
        tokens = tuple(Token(f"source-{k}", axis, s[axis])
                       for k, axis in enumerate(token_axes))
        return cls((0, 0, 0, 0, 0, 0), tokens, tokens)

    def read_signs(self):
        out = [0, 0, 0]
        for token in self.tokens:
            out[token.axis] = token.sign
        return tuple(out)

    def apply(self, a):
        next_tokens = []
        branches = []
        for token in self.tokens:
            target_axis = (token.axis + 1) % 3
            target_sign = a[token.axis] * token.sign
            next_tokens.append(Token(token.source, target_axis, target_sign))
            branches.append(TokenBranch(
                source=token.source,
                ingress=(token.axis, token.sign),
                egress=(target_axis, target_sign),
                primitive_steps=((token.axis, -token.sign),
                                 (target_axis, target_sign)),
            ))
        return NamedTriadBRC(
            self.anchor, self.sources, tuple(next_tokens),
            self.history + (AtomicScatter(a, tuple(branches)),),
        )

    def reframe(self, temporal_signs):
        tokens = tuple(Token(t.source, t.axis, temporal_signs[t.axis] * t.sign)
                       for t in self.tokens)
        return NamedTriadBRC(
            self.anchor, self.sources, tokens,
            self.history + (ReferenceTransport(temporal_signs),),
        )


def rotate(x, amount=1):
    return tuple(x[(i - amount) % 3] for i in range(3))


def multiply(x, y):
    return tuple(x[i] * y[i] for i in range(3))


def scatter(s, a):
    # This projection is justified by the carrier correspondence in README.
    # The complete two-event observer below composes on one retained carrier.
    return NamedTriadBRC.lift(s).apply(a).read_signs()


def relations(s, a):
    return tuple(s[i] * a[i] * s[(i + 1) % 3] for i in range(3))


def edge_gauge(a, epsilon):
    return tuple(epsilon[i] * a[i] * epsilon[(i + 1) % 3]
                 for i in range(3))


def observation(s, a, b, j):
    c0 = NamedTriadBRC.lift(s)
    c1 = c0.apply(a)
    c2 = c1.apply(b)
    return c0.read_signs()[j], c1.read_signs()[j], c2.read_signs()[j]


def check_carrier_correspondence():
    candidate_joint_branches = 0
    retained_histories = 0
    for s, a in product(SIGNS, TWISTS):
        carrier = NamedTriadBRC.lift(s)
        result = carrier.apply(a)
        expected = tuple(a[(i - 1) % 3] * s[(i - 1) % 3] for i in range(3))
        assert result.read_signs() == expected
        assert result.sources == carrier.sources
        # Verify the common-Cell selector on all eight original BRC branches.
        selected = []
        for outer_bits in product((0, 1), repeat=3):
            midpoints = []
            for token, outer in zip(carrier.tokens, outer_bits):
                point = [0] * 6
                if outer:
                    point[token.axis] = token.sign
                    point[(token.axis + 1) % 3] = a[token.axis] * token.sign
                midpoints.append(tuple(point))
            if len(set(midpoints)) == 1:
                selected.append(outer_bits)
            candidate_joint_branches += 1
        assert selected == [(0, 0, 0)]
        for b in TWISTS:
            two = result.apply(b)
            assert two.sources == carrier.sources
            assert len(two.history) == 2
            assert tuple(e.generator for e in two.history) == (a, b)
            assert all(tuple(branch.source for branch in event.joint_branches)
                       == tuple(token.source for token in carrier.sources)
                       for event in two.history)
            for j in range(3):
                assert two.read_signs()[j] == (
                    b[(j - 1) % 3] * a[(j - 2) % 3] * s[(j - 2) % 3])
            retained_histories += 1
    return {"joint_branch_candidates": candidate_joint_branches,
            "retained_two_event_histories": retained_histories,
            "only_common_cell_branch": "III",
            "source_names_signs_generator_order_and_paths_preserved": True}


def decode(y, delta, j):
    r = [0, 0, 0]
    r[(j - 1) % 3] = y[0] * y[1]
    r[(j - 2) % 3] = delta * y[1] * y[2]
    r[j] = -delta * y[0] * y[2]
    return tuple(r)


def classify_update_functions():
    """Exhaust the 4^4 functions on gauge orbits, then impose C3."""
    answers = []
    for outputs in product(CHANGES, repeat=4):
        table = dict(zip(TWISTS, outputs))
        if all(table[rotate(r)] == rotate(table[r]) for r in TWISTS):
            answers.append(table)
    assert len(answers) == 4
    formulas = {
        "persistent": {r: (1, 1, 1) for r in TWISTS},
        "ingress_sector": {r: tuple(-r[i] for i in range(3))
                           for r in TWISTS},
        "egress_sector": {r: tuple(-r[(i - 1) % 3] for i in range(3))
                          for r in TWISTS},
        "stationary_relation": {
            r: tuple(-r[(i + 1) % 3] for i in range(3)) for r in TWISTS
        },
    }
    assert {tuple(table[r] for r in TWISTS) for table in answers} == {
        tuple(table[r] for r in TWISTS) for table in formulas.values()
    }
    return formulas


def check_unrestricted():
    summaries = []
    count = 0
    for j in range(3):
        fibers = defaultdict(list)
        for s, a, b in product(SIGNS, TWISTS, TWISTS):
            y = observation(s, a, b, j)
            delta = a[(j - 1) % 3] * b[(j - 1) % 3]
            r = relations(s, a)
            assert decode(y, delta, j) == r
            fibers[y].append((r, delta))
            count += 1
        assert len(fibers) == 8
        assert all(len(fiber) == 16 for fiber in fibers.values())
        assert all(len({r for r, delta in fiber}) == 2
                   for fiber in fibers.values())
        assert all(sum(delta == 1 for r, delta in fiber) == 8
                   for fiber in fibers.values())
        summaries.append({"axis": j, "read_words": 8,
                          "microstates_per_read_word": 16,
                          "initial_relations_per_read_word": 2})
    return {"cases": count, "axes": summaries}


def check_updates(formulas):
    summary = {}
    for name, table in formulas.items():
        readable = name in ("persistent", "ingress_sector")
        by_axis = []
        covariance_count = 0
        for s, a in product(SIGNS, TWISTS):
            r = relations(s, a)
            delta = table[r]
            b = multiply(a, delta)
            assert b in TWISTS
            s1 = scatter(s, a)
            r1 = relations(s1, b)
            if name == "persistent":
                assert r1 == rotate(r)
            elif name == "ingress_sector":
                assert b == tuple(-s[i] * s[(i + 1) % 3]
                                  for i in range(3))
                assert r1 == rotate(r, -1)
            elif name == "egress_sector":
                assert b == tuple(-s1[i] * s1[(i + 1) % 3]
                                  for i in range(3))
                assert r1 == (-1, -1, -1)
            else:
                assert r1 == r
            for epsilon in SIGNS:
                gs = multiply(epsilon, s)
                ga = edge_gauge(a, epsilon)
                gb = multiply(ga, table[relations(gs, ga)])
                assert gb == edge_gauge(b, epsilon)
                covariance_count += 1
            for shift in range(3):
                rs, ra = rotate(s, shift), rotate(a, shift)
                rb = multiply(ra, table[relations(rs, ra)])
                assert rb == rotate(b, shift)
        for j in range(3):
            fibers = defaultdict(set)
            for s, a in product(SIGNS, TWISTS):
                r = relations(s, a)
                b = multiply(a, table[r])
                y = observation(s, a, b, j)
                fibers[y].add(r)
                if name == "ingress_sector":
                    assert a[(j - 1) % 3] * b[(j - 1) % 3] == -y[0] * y[1]
            assert len(fibers) == (8 if readable else 4)
            assert {len(value) for value in fibers.values()} == ({1} if readable else {2})
            # Six observations independently check the all-horizon symbolic maps.
            longer = defaultdict(set)
            for s, a in product(SIGNS, TWISTS):
                r0 = relations(s, a)
                carrier, twist = NamedTriadBRC.lift(s), a
                ys = [s[j]]
                for _ in range(5):
                    state = carrier.read_signs()
                    r = relations(state, twist)
                    next_twist = multiply(twist, table[r])
                    carrier = carrier.apply(twist)
                    twist = next_twist
                    ys.append(carrier.read_signs()[j])
                longer[tuple(ys)].add(r0)
            assert {len(value) for value in longer.values()} == ({1} if readable else {2})
            by_axis.append({"axis": j, "three_read_words": len(fibers),
                            "initial_relations_per_word": 1 if readable else 2,
                            "six_read_words": len(longer)})
        summary[name] = {"gauge_covariance_cases": covariance_count,
                         "complete_three_read_recovery": readable,
                         "axes": by_axis}
    return summary


def check_temporal_transport():
    count = 0
    for s, a, b, k0, k1, j in product(
            SIGNS, TWISTS, TWISTS, SIGNS, SIGNS, range(3)):
        c0 = NamedTriadBRC.lift(s)
        c1 = c0.apply(a).reframe(k0)
        c2 = c1.apply(b).reframe(k1)
        s1, s2 = c1.read_signs(), c2.read_signs()
        y = (s[j], s1[j], s2[j])
        i = (j - 1) % 3
        delta_cov = a[i] * b[i] * k0[i] * k0[j]
        z01, z12 = k0[j] * y[0] * y[1], k1[j] * y[1] * y[2]
        recovered = [0, 0, 0]
        recovered[i] = z01
        recovered[(j - 2) % 3] = delta_cov * z12
        recovered[j] = -delta_cov * z01 * z12
        assert tuple(recovered) == relations(s, a)
        count += 1
    return {"transport_cases": count,
            "same_time_generator_product_constraint": -1,
            "temporal_reference_changes_require_explicit_k": True}


def check_cycles(formulas):
    report = {}
    for name, table in formulas.items():
        mapping = {}
        for s, a in product(SIGNS, TWISTS):
            carrier = NamedTriadBRC.lift(s)
            r = relations(s, a)
            mapping[(s, a)] = (carrier.apply(a).read_signs(), multiply(a, table[r]))
        image = set(mapping.values())
        preimages = {target: sum(value == target for value in mapping.values())
                     for target in image}
        cycles = set()
        transient_lengths = []
        for start in mapping:
            path, seen, current = [], {}, start
            while current not in seen:
                seen[current] = len(path)
                path.append(current)
                current = mapping[current]
            transient_lengths.append(seen[current])
            cycles.add(frozenset(path[seen[current]:]))
        histogram = {length: sum(len(cycle) == length for cycle in cycles)
                     for length in sorted({len(cycle) for cycle in cycles})}
        full_frame_periods = set()
        for token_axes, s, a in product(permutations(range(3)), SIGNS, TWISTS):
            carrier = NamedTriadBRC.lift(s, token_axes)
            initial_tokens, twist = carrier.tokens, a
            states = [(carrier.tokens, twist)]
            for _ in range(6):
                r = relations(carrier.read_signs(), twist)
                next_twist = multiply(twist, table[r])
                carrier = carrier.apply(twist)
                twist = next_twist
                states.append((carrier.tokens, twist))
            assert len(carrier.history) == 6
            assert carrier.sources == NamedTriadBRC.lift(s, token_axes).sources
            if name in ("persistent", "ingress_sector"):
                third_tokens, third_twist = states[3]
                assert third_twist == a
                assert third_tokens == tuple(Token(t.source, t.axis, -t.sign)
                                              for t in initial_tokens)
                assert states[6] == states[0]
            if name != "egress_sector":
                full_frame_periods.add(next(k for k in range(1, 7)
                                            if states[k] == states[0]))
        if name == "egress_sector":
            assert len(image) == 8
            assert set(preimages.values()) == {4}
        else:
            assert len(image) == 32
            assert set(preimages.values()) == {1}
            assert full_frame_periods == {6}
        report[name] = {
            "occupancy_twist_states": 32,
            "image_states": len(image),
            "preimage_cardinalities": sorted(set(preimages.values())),
            "occupancy_twist_cycles": histogram,
            "max_transient_length": max(transient_lengths),
            "named_frame_inputs": 192,
            "named_frame_periods_when_bijective": sorted(full_frame_periods),
            "history_not_quotiented_as_periodic": True,
        }
    return report


def check_generator_only_relations():
    pairs = tuple(product(TWISTS, TWISTS))
    # Source-independent relations give every observation word for each pair.
    # Thus fixed delta across allowed pairs is necessary and sufficient.
    single_axis_counts = [0, 0, 0]
    all_axis_count = 0
    cyclic_all_axis = []
    for mask in range(1, 1 << len(pairs)):
        chosen = tuple(pairs[i] for i in range(16) if mask & (1 << i))
        deltas = [multiply(a, b) for a, b in chosen]
        passes = [len({d[i] for d in deltas}) == 1 for i in range(3)]
        for i in range(3):
            single_axis_counts[i] += passes[i]
        if all(passes):
            all_axis_count += 1
            pair_set = set(chosen)
            if all((rotate(a), rotate(b)) in pair_set for a, b in chosen):
                cyclic_all_axis.append(chosen)
                assert all(a == b for a, b in chosen)
    assert single_axis_counts == [510, 510, 510]
    assert all_axis_count == 60
    # Without gauge covariance there are three nonempty rotation-invariant
    # subsets of the four diagonal pairs: canonical, its other-three orbit, both.
    assert len(cyclic_all_axis) == 3
    return {"nonempty_relations": 65535,
            "readable_for_each_fixed_axis": single_axis_counts,
            "readable_for_all_axes": all_axis_count,
            "cyclic_readable_relations": len(cyclic_all_axis),
            "cyclic_readable_relations_are_diagonal": True}


def main():
    formulas = classify_update_functions()
    result = {
        "model": "V5 named three-axis observer within Heartbeat X6",
        "status": "AUTHOR_EXACT_CHECK; native event permission unresolved",
        "gauge_orbit_functions_examined": 4 ** 4,
        "cyclic_gauge_equivariant_deterministic_updates": len(formulas),
        "brc_carrier_correspondence": check_carrier_correspondence(),
        "source_revision": "enterprise-math@ef720decf4a35a276e509964250571a55421b9f8",
        "brc_extension_entrypoint": "NamedTriadBRC.apply",
        "brc_input_carrier": "three named unit source tokens at signed X6 ports; joint III path history",
        "brc_future_language": "V5 signed-cycle atomic III scatterings; explicit reference transports when declared",
        "brc_observers": "fixed-axis radial signs, initial link triple, retained named branch history",
        "residual_classification": "exact observer-fiber ambiguity; no numerical approximation or physics residual attribution",
        "unrestricted_two_scatterings": check_unrestricted(),
        "update_classification": check_updates(formulas),
        "cycle_classification": check_cycles(formulas),
        "temporal_transport": check_temporal_transport(),
        "generator_only_relations": check_generator_only_relations(),
    }
    destination = Path(__file__).with_name("relation_update_results.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
