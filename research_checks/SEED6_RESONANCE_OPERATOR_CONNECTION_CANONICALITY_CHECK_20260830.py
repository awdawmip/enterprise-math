#!/usr/bin/env python3
from __future__ import annotations

import sys
from itertools import permutations, product
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.finite_symmetry import (  # noqa: E402
    canonical_choice_obstruction,
    global_fixed_points,
    orbit_partition,
    stabilizer,
    validate_finite_group_action,
)

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def compose(p, q):
    # p o q
    return tuple(p[q[i]] for i in range(len(p)))

def inverse(p):
    out = [None] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def perm_action(elements, actions):
    return {
        name: {x: action[x] for x in elements}
        for name, action in actions.items()
    }

S3 = tuple(permutations(range(3)))
E3 = (0, 1, 2)

# ---------------------------------------------------------------------------
# A/B. Exact S3 transport torsors and the marked Seed-6 residual C2 obstruction.
# ---------------------------------------------------------------------------

def lr_action(gx, gy, t):
    return compose(compose(gy, t), inverse(gx))

full_actions = {}
for gx in S3:
    for gy in S3:
        name = (gx, gy)
        full_actions[name] = {t: lr_action(gx, gy, t) for t in S3}

validate_finite_group_action(S3, full_actions)
check(len(full_actions) == 36, "full independent-frame action must have 36 elements")
check(canonical_choice_obstruction(S3, full_actions), "unmarked six-map transport torsor must have no canonical point")
check(global_fixed_points(S3, full_actions) == frozenset(), "unmarked transport fixed set must be empty")
full_orbits = orbit_partition(S3, full_actions)
check(len(full_orbits) == 1 and len(full_orbits[0]) == 6, "full S3xS3 frame action must be transitive on transports")
for t in S3:
    check(len(stabilizer(S3, full_actions, t)) == 6, "each unmarked transport must have stabilizer order 6")

# Seed-6 supplies a distinguished carrier/seed state M0, but M1/M2 stay unordered.
FLIP = (0, 2, 1)
C2 = (E3, FLIP)
marked_candidates = tuple(t for t in S3 if t[0] == 0)
check(set(marked_candidates) == {E3, FLIP}, "mark-preserving inter-cell identifications must be a two-element torsor")

marked_raw_actions = {}
for gx in C2:
    for gy in C2:
        name = (gx, gy)
        marked_raw_actions[name] = {t: lr_action(gx, gy, t) for t in marked_candidates}

check(len(marked_raw_actions) == 4, "raw independent marked-frame group must have four elements")
for t in marked_candidates:
    check(sum(action[t] == t for action in marked_raw_actions.values()) == 2, "raw marked transport stabilizer must be diagonal C2")

# T7 consumes the distinct permutation image, so quotient the diagonal kernel.
marked_actions = {}
seen_signatures = set()
for name, action in marked_raw_actions.items():
    signature = tuple(action[t] for t in marked_candidates)
    if signature not in seen_signatures:
        seen_signatures.add(signature)
        marked_actions[name] = action

validate_finite_group_action(marked_candidates, marked_actions)
check(len(marked_actions) == 2, "effective marked-frame action must be C2 after quotienting the diagonal kernel")
check(canonical_choice_obstruction(marked_candidates, marked_actions), "Seed-marked two-map torsor must still have no canonical point")
check(global_fixed_points(marked_candidates, marked_actions) == frozenset(), "marked transport fixed set must be empty")
marked_orbits = orbit_partition(marked_candidates, marked_actions)
check(len(marked_orbits) == 1 and len(marked_orbits[0]) == 2, "effective marked-frame C2 must be transitive on the two transports")

# A target-only change of the M1/M2 frame changes every candidate.
target_flip = {t: lr_action(E3, FLIP, t) for t in marked_candidates}
for t in marked_candidates:
    check(target_flip[t] != t, "minimal target-frame flip must move each mark-preserving transport")

# ---------------------------------------------------------------------------
# D. S4 -> S3, V4, atom-transposition lifts, and section torsor.
# ---------------------------------------------------------------------------

ATOMS = tuple(range(4))
S4 = tuple(permutations(ATOMS))
E4 = ATOMS

MATCHINGS = (
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
)

def act_matching(p, matching):
    out = []
    for edge in matching:
        i, j = tuple(edge)
        out.append(frozenset((p[i], p[j])))
    return frozenset(out)

def quotient_map(p):
    return tuple(MATCHINGS.index(act_matching(p, m)) for m in MATCHINGS)

PHI = {p: quotient_map(p) for p in S4}
image = set(PHI.values())
V4 = tuple(p for p in S4 if PHI[p] == E3)

check(len(S4) == 24, "S4 order")
check(image == set(S3), "S4 pairing action must surject onto S3")
check(len(V4) == 4, "kernel must be V4")
for v in V4:
    check(compose(v, v) == E4, "every V4 element has order dividing 2")

fibres = {s: tuple(p for p in S4 if PHI[p] == s) for s in S3}
for s in S3:
    check(len(fibres[s]) == 4, "every quotient fibre must be a V4 torsor of size 4")

def is_transposition(p):
    moved = [i for i in range(len(p)) if p[i] != i]
    return len(moved) == 2 and p[moved[0]] == moved[1] and p[moved[1]] == moved[0]

s3_transpositions = tuple(s for s in S3 if is_transposition(s))
check(len(s3_transpositions) == 3, "S3 must have three transpositions")
for s in s3_transpositions:
    check(sum(is_transposition(p) for p in fibres[s]) == 2, "each pairing transposition has exactly two single-atom-transposition lifts")

# Enumerate homomorphic sections q:S4->S3. Identity must map to identity.
nonidentity = tuple(s for s in S3 if s != E3)
sections = []
for chosen in product(*(fibres[s] for s in nonidentity)):
    section = {E3: E4, **dict(zip(nonidentity, chosen))}
    if all(section[compose(a, b)] == compose(section[a], section[b]) for a in S3 for b in S3):
        sections.append(section)

check(len(sections) == 4, "the split extension has exactly four homomorphic sections")

section_sigs = tuple(tuple(section[s] for s in S3) for section in sections)
check(len(set(section_sigs)) == 4, "section signatures must be distinct")

def conjugate(v, p):
    return compose(compose(v, p), inverse(v))

section_actions = {}
for v in V4:
    mapping = {}
    for sig in section_sigs:
        section = dict(zip(S3, sig))
        transformed = tuple(conjugate(v, section[s]) for s in S3)
        mapping[sig] = transformed
    section_actions[v] = mapping

validate_finite_group_action(section_sigs, section_actions)
check(canonical_choice_obstruction(section_sigs, section_actions), "V4 conjugation must forbid a canonical homomorphic section")
section_orbits = orbit_partition(section_sigs, section_actions)
check(len(section_orbits) == 1 and len(section_orbits[0]) == 4, "V4 must act transitively on the four splittings")

# A homomorphic section has zero factor set, so there is no non-split extension obstruction.
def factor(section, a, b):
    return compose(compose(section[a], section[b]), inverse(section[compose(a, b)]))

for section in sections:
    check(all(factor(section, a, b) == E4 for a in S3 for b in S3), "homomorphic section factor set must vanish")

# Perturb one lift by V4: the resulting set-theoretic section stays a section but
# acquires nonzero V4 residue. Hence such residue is section/gauge dependent.
perturbed = dict(sections[0])
tau = s3_transpositions[0]
nontrivial_v = next(v for v in V4 if v != E4)
perturbed[tau] = compose(nontrivial_v, perturbed[tau])
check(PHI[perturbed[tau]] == tau, "V4 perturbation must preserve quotient lift")
residues = {factor(perturbed, a, b) for a in S3 for b in S3}
check(residues <= set(V4), "all factor residues must lie in V4")
check(any(v != E4 for v in residues), "a nonhomomorphic section can carry nonzero V4 residue")

# ---------------------------------------------------------------------------
# C/E. Resonance strata, row C2, and absence of induced S3 holonomy.
# ---------------------------------------------------------------------------

def prime_factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def reduced(a, b):
    d = gcd(a, b)
    return d, a // d, b // d

def stratum(a, b):
    if a == b:
        return "E_EQUALITY"
    d, A, B = reduced(a, b)
    fa, fb = prime_factors(a), prime_factors(b)
    if d == 1:
        if len(fa) == len(fb) == 1:
            ea = next(iter(fa.values()))
            eb = next(iter(fb.values()))
            if ea == eb == 1:
                return "C0_DISTINCT_PRIME_PAIR"
            return "C1_COPRIME_PRIME_POWER_THICK"
        return "C2_COPRIME_MULTISUPPORT"
    ps = sorted(set(fa) | set(fb))
    cols = [(fa.get(p, 0), fb.get(p, 0)) for p in ps]
    rank1 = all(x1 * y2 == y1 * x2 for x1, y1 in cols for x2, y2 in cols)
    return "O1_OVERLAP_COMMON_BASE_RANK1" if rank1 else "O2_OVERLAP_RANK2"

def resonance_count(a, b, R):
    if a == b:
        return 0
    _, A, B = reduced(a, b)
    R = set(R)
    max_r = max(R, default=0)
    return sum(1 for t in range(1, max_r + 1) if A * t in R and B * t in R)

samples = {
    "C0_DISTINCT_PRIME_PAIR": (2, 3, (1, 4), (2, 3)),
    "C1_COPRIME_PRIME_POWER_THICK": (4, 9, (1, 10), (4, 9)),
    "C2_COPRIME_MULTISUPPORT": (6, 35, (1, 36), (6, 35)),
    "O1_OVERLAP_COMMON_BASE_RANK1": (4, 8, (1, 3), (1, 2)),
    "O2_OVERLAP_RANK2": (6, 10, (1, 6), (3, 5)),
}
for expected, (a, b, clean_R, resonant_R) in samples.items():
    check(stratum(a, b) == expected, f"stratum sample mismatch for {expected}")
    check(resonance_count(a, b, clean_R) == 0, f"{expected} clean control must have no resonance")
    check(resonance_count(a, b, resonant_R) == 1, f"{expected} resonant control must have one typed resonance")

check(stratum(6, 6) == "E_EQUALITY", "equality control")
check(resonance_count(6, 6, (1, 2, 3, 6)) == 0, "equality is duplicate-row degeneration, not cross-column resonance")
check(resonance_count(2, 3, (2, 3, 4, 6)) == 2, "C0 multi-resonance control must have exactly two independent resonance generators")

# The accepted wedge normal form supplies a free S1 for each resonance pinch.
# A chosen mark-preserving connection may assign either identity or FLIP to that
# free generator. Both live over the same intrinsic carrier-row odd period.
check(E3 != FLIP and FLIP in marked_candidates, "same odd carrier loop admits two distinct mark-preserving holonomy choices")
check(compose(FLIP, FLIP) == E3, "mark-preserving structure group is C2")
check(compose(E3, FLIP) == compose(FLIP, E3), "mark-preserving holonomies commute")

# If one drops the seed-mark-preserving restriction, the larger S3 model admits
# noncommuting choices on two independent resonance circles, but they are choices,
# not induced by the frozen data.
tau_a, tau_b = s3_transpositions[0], s3_transpositions[1]
check(compose(tau_a, tau_b) != compose(tau_b, tau_a), "unrestricted S3 model space contains noncommuting holonomy choices")

print(
    "PASS "
    f"checks={CHECKS} "
    "unmarked_transport_orbit=6 "
    "marked_transport_orbit=2 "
    "V4=4 "
    "homomorphic_sections=4 "
    "strata=5+E"
)
