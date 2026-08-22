#!/usr/bin/env python3
"""
R064 Phase A deterministic validator.

Evidence boundary: this checker encodes only the N0 declarations frozen from the
five Phase-A allowed sources. It uses exact finite/integer/relational operations.
It does not import a downstream interaction table or target state count.
"""

from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations, permutations, product
from collections import Counter
import json
import hashlib

ALLOWED_SOURCES = {
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md": {
        "commit": "d16877c3b62a7d3b7568780c732f610c260c13c1",
        "blob": "393060ebfd6a86ad45f258747d78a14d9c8ac153",
    },
    "definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md": {
        "commit": "d16877c3b62a7d3b7568780c732f610c260c13c1",
        "blob": "b631242db84c5bd3640e6dc554b19a1d04d464f3",
    },
    "FOUNDATIONAL_LOGIC.md": {
        "commit": "d16877c3b62a7d3b7568780c732f610c260c13c1",
        "blob": "f089400136341efbf10a5e24e8f0729800b942cd",
    },
    "foundational_logic.json": {
        "commit": "d16877c3b62a7d3b7568780c732f610c260c13c1",
        "blob": "6875d84746ee369ea222fd32bdcd92206c2db9b2",
    },
    "native_semantics_admissibility.json": {
        "commit": "d16877c3b62a7d3b7568780c732f610c260c13c1",
        "blob": "58ad0af8c2e3df56b353575bf0004095507bffbf",
    },
}

# The cardinality and labels below are substrate declarations, not a target state count.
AXES = ("E1", "E2", "E3")
SECTORS = tuple(tuple(sorted(s)) for s in combinations(AXES, 2))
MAX_WORD_LENGTH = 5

@dataclass(frozen=True, order=True)
class Source:
    sector: tuple[str, str]
    word: tuple[str, ...]

@dataclass(frozen=True, order=True)
class Event:
    source: Source
    pos: int
    tag: str

def perm_maps():
    out = []
    for p in permutations(AXES):
        out.append(dict(zip(AXES, p)))
    return out

def map_sector(sector, g):
    return tuple(sorted(g[x] for x in sector))

def admitted_automorphisms():
    sector_set = set(SECTORS)
    good = []
    for g in perm_maps():
        if {map_sector(s, g) for s in SECTORS} == sector_set:
            good.append(g)
    return good

AUT = admitted_automorphisms()

def map_source(src: Source, g):
    return Source(map_sector(src.sector, g), tuple(g[x] for x in src.word))

def map_event(e: Event, g):
    return Event(map_source(e.source, g), e.pos, g[e.tag])

def generate_sources_events():
    sources, events = [], []
    for sector in SECTORS:
        for n in range(1, MAX_WORD_LENGTH + 1):
            for word in product(sector, repeat=n):
                src = Source(sector, tuple(word))
                sources.append(src)
                for pos, tag in enumerate(word):
                    events.append(Event(src, pos, tag))
    return sources, events

SOURCES, EVENTS = generate_sources_events()

CONTEXT_CLASSES = (
    "SS_EQ_SAME",
    "SS_LT_SAME",
    "SS_LT_DIFF",
    "SS_GT_SAME",
    "SS_GT_DIFF",
    "DS_SAMESECTOR_SAME",
    "DS_SAMESECTOR_DIFF",
    "DS_DIFFSECTOR_SHARED_SHARED",
    "DS_DIFFSECTOR_SHARED_PRIVATE",
    "DS_DIFFSECTOR_PRIVATE_SHARED",
    "DS_DIFFSECTOR_PRIVATE_PRIVATE",
)

def context_class(e1: Event, e2: Event) -> str:
    s1, s2 = e1.source.sector, e2.source.sector
    if e1.source == e2.source:
        assert s1 == s2
        if e1.pos == e2.pos:
            assert e1.tag == e2.tag
            return "SS_EQ_SAME"
        rel = "LT" if e1.pos < e2.pos else "GT"
        eq = "SAME" if e1.tag == e2.tag else "DIFF"
        return f"SS_{rel}_{eq}"
    if s1 == s2:
        eq = "SAME" if e1.tag == e2.tag else "DIFF"
        return f"DS_SAMESECTOR_{eq}"
    shared = set(s1).intersection(s2)
    assert len(shared) == 1
    shared_axis = next(iter(shared))
    r1 = "SHARED" if e1.tag == shared_axis else "PRIVATE"
    r2 = "SHARED" if e2.tag == shared_axis else "PRIVATE"
    return f"DS_DIFFSECTOR_{r1}_{r2}"

def abstract_contexts():
    """
    Minimal pair-local relational reduct: source equality/order when meaningful,
    ordered sector membership, and component tags. Whole source words are not
    retained in this reduct.
    """
    out = []
    for s1 in SECTORS:
        for order in ("EQ", "LT", "GT"):
            for t1 in s1:
                for t2 in s1:
                    if order == "EQ" and t1 != t2:
                        continue
                    out.append(("SAME", order, s1, s1, t1, t2))
        for t1 in s1:
            for t2 in s1:
                out.append(("DIFF", "NONE", s1, s1, t1, t2))
        for s2 in SECTORS:
            if s2 == s1:
                continue
            for t1 in s1:
                for t2 in s2:
                    out.append(("DIFF", "NONE", s1, s2, t1, t2))
    return tuple(out)

ABSTRACT_CONTEXTS = abstract_contexts()

def map_abstract(c, g):
    src_rel, order, s1, s2, t1, t2 = c
    return (src_rel, order, map_sector(s1, g), map_sector(s2, g), g[t1], g[t2])

def abstract_orbits():
    domain = set(ABSTRACT_CONTEXTS)
    seen = set()
    orbits = []
    for c in ABSTRACT_CONTEXTS:
        if c in seen:
            continue
        orb = {map_abstract(c, g) for g in AUT}
        assert orb <= domain
        seen |= orb
        orbits.append(orb)
    return orbits

ABSTRACT_ORBITS = abstract_orbits()

def component_complement(x: str, y: str) -> str:
    if x == y:
        return x
    remaining = [z for z in AXES if z != x and z != y]
    assert len(remaining) == 1
    return remaining[0]

def coaxis_in_sector(tag: str, sector: tuple[str, str]) -> str:
    remaining = [z for z in sector if z != tag]
    assert len(remaining) == 1
    return remaining[0]

def alt_context_sensitive_law(e1: Event, e2: Event) -> str:
    """
    Explicit N0-definable inequivalent law:
    on same-source forward same-tag distinct pairs, return the other axis in the
    source sector; elsewhere use component complement.
    """
    if (
        e1.source == e2.source
        and e1.pos < e2.pos
        and e1.tag == e2.tag
    ):
        return coaxis_in_sector(e1.tag, e1.source.sector)
    return component_complement(e1.tag, e2.tag)

def canonical_event_law(e1: Event, e2: Event) -> str:
    return component_complement(e1.tag, e2.tag)

def abstract_component_law(c):
    _, _, _, _, t1, t2 = c
    return component_complement(t1, t2)

def abstract_alt_law(c):
    src_rel, order, s1, _, t1, t2 = c
    if src_rel == "SAME" and order == "LT" and t1 == t2:
        return coaxis_in_sector(t1, s1)
    return component_complement(t1, t2)

def is_equivariant_abstract_law(law):
    for g in AUT:
        for c in ABSTRACT_CONTEXTS:
            lhs = law(map_abstract(c, g))
            rhs = g[law(c)]
            if lhs != rhs:
                return False, (g, c, lhs, rhs)
    return True, None

def component_equivariant_laws():
    """
    Enumerate the three S3-equivariant A x A -> A laws without hard-coding a
    target table. Pick F(E1,E2), propagate by equivariance; diagonal output is
    forced by the diagonal stabilizer.
    """
    laws = []
    for offdiag_value in AXES:
        table = {}
        # diagonal forced: any equivariant output at (x,x) must be fixed by the
        # stabilizer of x; for three axes the only such axis is x.
        for x in AXES:
            table[(x, x)] = x

        base_pair = ("E1", "E2")
        base_value = offdiag_value
        for g in AUT:
            pair = (g[base_pair[0]], g[base_pair[1]])
            value = g[base_value]
            if pair in table and table[pair] != value:
                raise AssertionError("inconsistent equivariant propagation")
            table[pair] = value
        assert len(table) == len(AXES) ** 2
        laws.append(table)
    return laws

def classify_component_law(table):
    left = all(table[(x,y)] == x for x in AXES for y in AXES)
    right = all(table[(x,y)] == y for x in AXES for y in AXES)
    comp = all(table[(x,y)] == component_complement(x,y) for x in AXES for y in AXES)
    if left:
        return "LEFT_PROJECTION"
    if right:
        return "RIGHT_PROJECTION"
    if comp:
        return "COMPONENT_COMPLEMENT"
    return "OTHER"

def first_associativity_counterexample():
    for x in AXES:
        for y in AXES:
            for z in AXES:
                lhs = component_complement(component_complement(x,y), z)
                rhs = component_complement(x, component_complement(y,z))
                if lhs != rhs:
                    return {"x":x,"y":y,"z":z,"lhs":lhs,"rhs":rhs}
    return None

def identity_counterexamples():
    out = {}
    for e in AXES:
        witness = None
        for x in AXES:
            if component_complement(e,x) != x or component_complement(x,e) != x:
                witness = {
                    "candidate_identity": e,
                    "x": x,
                    "left": component_complement(e,x),
                    "right": component_complement(x,e),
                }
                break
        out[e] = witness
    return out

def first_context_nonuniqueness_witness():
    # deterministic implementation order only; not used to select a theorem.
    ordered_events = sorted(EVENTS, key=lambda e: (
        len(e.source.word), e.source.sector, e.source.word, e.pos, e.tag
    ))
    for e1 in ordered_events:
        for e2 in ordered_events:
            a = canonical_event_law(e1,e2)
            b = alt_context_sensitive_law(e1,e2)
            if a != b:
                return {
                    "sector": e1.source.sector,
                    "word": e1.source.word if e1.source == e2.source else None,
                    "pos1": e1.pos,
                    "pos2": e2.pos,
                    "tag1": e1.tag,
                    "tag2": e2.tag,
                    "context_class": context_class(e1,e2),
                    "component_only_output": a,
                    "context_sensitive_output": b,
                }
    return None

def event_lift_ambiguity():
    # Pick any distinct component pair in a common sector by implementation order.
    sector = SECTORS[0]
    x, y = sector
    k = component_complement(x,y)
    candidate_sectors = [s for s in SECTORS if k in s]
    return {
        "input_sector": sector,
        "input_tags": [x,y],
        "component_output": k,
        "admissible_output_sectors": candidate_sectors,
        "count": len(candidate_sectors),
    }

def family_size_on_full_local_context():
    # Every abstract local-context orbit has trivial stabilizer (checked below);
    # hence each orbit independently permits any axis output.
    return len(AXES) ** len(ABSTRACT_ORBITS)

def sha256_json(obj):
    payload = json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=True).encode()
    return hashlib.sha256(payload).hexdigest()

def main():
    mismatches = []

    # 1. N0 inventory and automorphism classification.
    if len(AXES) != 3:
        mismatches.append("substrate axis inventory mismatch")
    if len(SECTORS) != 3 or set(SECTORS) != {
        ("E1","E2"),("E1","E3"),("E2","E3")
    }:
        mismatches.append("substrate sector inventory mismatch")
    if len(AUT) != 6:
        mismatches.append("automorphism group is not S3")

    # 2. Exhaustive path-event regression through length 5.
    context_counts = Counter()
    for e1 in EVENTS:
        for e2 in EVENTS:
            c = context_class(e1,e2)
            context_counts[c] += 1
    if set(context_counts) != set(CONTEXT_CLASSES):
        mismatches.append(("unclassified_contexts", set(context_counts), set(CONTEXT_CLASSES)))

    # Abstract local-context quotient: exact 11 orbits, each size 6 -> trivial stabilizer.
    if len(ABSTRACT_ORBITS) != 11:
        mismatches.append(("abstract_orbit_count", len(ABSTRACT_ORBITS)))
    orbit_sizes = sorted(len(o) for o in ABSTRACT_ORBITS)
    if orbit_sizes != [6] * 11:
        mismatches.append(("nontrivial_context_stabilizer_detected", orbit_sizes))
    # Every relabeling is checked on every abstract local context; because each
    # of the 599,076 event pairs was mapped to exactly one such reduct above,
    # this covers the theorem-critical relabeling action without repeating
    # millions of isomorphic checks.
    for g in AUT:
        for c in ABSTRACT_CONTEXTS:
            if map_abstract(c, g) not in set(ABSTRACT_CONTEXTS):
                mismatches.append(("abstract_context_not_closed_under_aut", c, g))

    # 3-5. Candidate state provenance/closure/equivariance.
    provenance_failures = []
    for x in AXES:
        for y in AXES:
            out = component_complement(x,y)
            if out not in AXES:
                provenance_failures.append((x,y,out,"not_N0_axis"))
            elif x == y and out != x:
                provenance_failures.append((x,y,out,"diagonal_not_common_input"))
            elif x != y and not (out != x and out != y and set((x,y,out)) == set(AXES)):
                provenance_failures.append((x,y,out,"not_unique_complement"))
    if provenance_failures:
        mismatches.append(("provenance_failures", provenance_failures))

    for g in AUT:
        for x in AXES:
            for y in AXES:
                if component_complement(g[x],g[y]) != g[component_complement(x,y)]:
                    mismatches.append(("component_equivariance",g,x,y))

    # Component law and one inequivalent context-sensitive law are checked
    # for equivariance on the complete abstract local-context carrier.
    ok_a, witness_a = is_equivariant_abstract_law(abstract_component_law)
    ok_b, witness_b = is_equivariant_abstract_law(abstract_alt_law)
    if not ok_a:
        mismatches.append(("canonical_event_law_non_equivariant", witness_a))
    if not ok_b:
        mismatches.append(("alt_event_law_non_equivariant", witness_b))

    # 6. Derived algebraic laws.
    commutative = all(
        component_complement(x,y) == component_complement(y,x)
        for x in AXES for y in AXES
    )
    idempotent = all(component_complement(x,x) == x for x in AXES)
    derived_involution = all(
        component_complement(x, component_complement(x,y)) == y
        for x in AXES for y in AXES
    )
    assoc_cex = first_associativity_counterexample()
    identity_cex = identity_counterexamples()
    if not commutative or not idempotent or not derived_involution:
        mismatches.append("claimed positive algebraic law failed")
    if assoc_cex is None:
        mismatches.append("expected associativity rejection has no witness")
    if any(v is None for v in identity_cex.values()):
        mismatches.append("identity unexpectedly exists")

    # Component-only law family: exactly left, right, complement.
    comp_laws = component_equivariant_laws()
    comp_classes = [classify_component_law(t) for t in comp_laws]
    if sorted(comp_classes) != sorted([
        "LEFT_PROJECTION","RIGHT_PROJECTION","COMPONENT_COMPLEMENT"
    ]):
        mismatches.append(("component_family_classification", comp_classes))

    # Full local-context family count and nonuniqueness witness.
    full_family_size = family_size_on_full_local_context()
    nonunique_witness = first_context_nonuniqueness_witness()
    if full_family_size != 3 ** 11:
        mismatches.append(("full_family_size", full_family_size))
    if nonunique_witness is None:
        mismatches.append("no context-dependence nonuniqueness witness")

    lift = event_lift_ambiguity()
    if lift["count"] != 2:
        mismatches.append(("event_lift_ambiguity_count", lift))

    regression = {
        "schema": "R064_PHASEA_REGRESSION_V1",
        "max_word_length": MAX_WORD_LENGTH,
        "axes": list(AXES),
        "sectors": [list(s) for s in SECTORS],
        "automorphism_count": len(AUT),
        "automorphism_group": "S3",
        "source_word_count": len(SOURCES),
        "event_occurrence_count": len(EVENTS),
        "ordered_event_pair_count": len(EVENTS) ** 2,
        "local_context_class_count": len(context_counts),
        "local_context_counts": dict(sorted(context_counts.items())),
        "abstract_local_context_orbit_count": len(ABSTRACT_ORBITS),
        "abstract_orbit_sizes": orbit_sizes,
        "full_context_axis_output_equivariant_family_size": full_family_size,
        "component_only_equivariant_law_count": len(comp_laws),
        "component_only_law_classes": comp_classes,
        "candidate_state_count": len(AXES),
        "candidate_states_are_preexisting_n0_axes": True,
        "closure": True,
        "commutative": commutative,
        "idempotent": idempotent,
        "derived_involution_x_x_y_eq_y": derived_involution,
        "associative": assoc_cex is None,
        "associativity_counterexample": assoc_cex,
        "identity_exists": not any(v is not None for v in identity_cex.values()),
        "identity_counterexamples": identity_cex,
        "context_nonuniqueness_witness": nonunique_witness,
        "event_level_sector_lift_ambiguity": lift,
        "provenance_failures": provenance_failures,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "allowed_sources": ALLOWED_SOURCES,
    }
    regression["deterministic_digest"] = sha256_json(regression)
    print(json.dumps(regression, indent=2, sort_keys=True))
    return 0 if not mismatches else 1

if __name__ == "__main__":
    raise SystemExit(main())
