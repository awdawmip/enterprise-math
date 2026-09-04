#!/usr/bin/env python3
"""Complete weighted-Pluecker shell audit P(Omega)<=15 for #1160.

Scope:
- rational atom denominator height H=1,000,000;
- primitive decomposable rank-two exterior states with at least three active split
  prime coordinates;
- weighted primitive Pluecker height <=15;
- search only for support-three endpoint circuits whose generalized Lehmer cost
  beats the current leader 1.2096120143032323.

The combinatorial classification is complete:
- 5+ active primes are impossible under P<=15 by the weighted spanning-tree bound;
- 4 active primes are forced to {5,13,17,r}, r in {29,37,41}, with a star
  centered at 5 and all three primitive minors of magnitude one (12 sign states);
- all 3-prime primitive Pluecker states are enumerated dynamically from the budget.
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_rational_support3_primeplane_h1m_20260904.py"
spec = importlib.util.spec_from_file_location("pp", BASE)
pp = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(pp)

g2 = pp.g2
H = 1_000_000
L = math.log(2 * H * H)
P_CAP = 15.0
MU_BOUND = 1.2096120143032323


def three_prime_states():
    # For three active primes p<q<r, at least two Pluecker coordinates are
    # nonzero. The two cheapest edge weights are log(p)log(q), log(p)log(r).
    # Thus log 5 (log 13 + log r) <= P_CAP gives a universal r bound.
    rmax = math.floor(math.exp(P_CAP / math.log(5) - math.log(13))) + 2
    split = [p for p in pp.primes_upto(rmax) if p % 4 == 1]
    out = []
    for i, p in enumerate(split):
        lp = math.log(p)
        for j in range(i + 1, len(split)):
            q = split[j]
            lq = math.log(q)
            for r in split[j + 1 :]:
                lr = math.log(r)
                weights = (lp * lq, lp * lr, lq * lr)
                if sum(sorted(weights)[:2]) > P_CAP + 1e-12:
                    break
                bounds = [int(P_CAP // w) for w in weights]
                for A in range(-bounds[0], bounds[0] + 1):
                    for B in range(-bounds[1], bounds[1] + 1):
                        for C in range(-bounds[2], bounds[2] + 1):
                            if sum(x != 0 for x in (A, B, C)) < 2:
                                continue
                            cost = abs(A) * weights[0] + abs(B) * weights[1] + abs(C) * weights[2]
                            if cost > P_CAP + 1e-12:
                                continue
                            if math.gcd(math.gcd(abs(A), abs(B)), abs(C)) != 1:
                                continue
                            if next(x for x in (A, B, C) if x) < 0:
                                continue
                            out.append((cost, (p, q, r), (A, B, C)))
    return rmax, out


def plane_atoms_3(primes, omega):
    p, q, r = primes
    A, B, C = omega
    # x wedge Omega=0 => C*x_p - B*x_q + A*x_r=0.
    normal = (C, -B, A)
    logs = [math.log(x) for x in primes]
    bounds = [int((L - 1e-12) // lg) for lg in logs]
    solve = max((i for i, n in enumerate(normal) if n), key=lambda i: abs(normal[i]))
    other = [i for i in range(3) if i != solve]
    atoms = {}
    for x0 in range(-bounds[other[0]], bounds[other[0]] + 1):
        for x1 in range(-bounds[other[1]], bounds[other[1]] + 1):
            numerator = -(normal[other[0]] * x0 + normal[other[1]] * x1)
            if numerator % normal[solve]:
                continue
            vec = [0, 0, 0]
            vec[other[0]] = x0
            vec[other[1]] = x1
            vec[solve] = numerator // normal[solve]
            if vec == [0, 0, 0]:
                continue
            if sum(abs(vec[i]) * logs[i] for i in range(3)) >= L:
                continue
            raw = (1, 0)
            for prime, exponent in zip(primes, vec):
                if exponent:
                    raw = g2.pair_mul(
                        raw,
                        pp.ipow(pp.gaussian_prime(prime, 1 if exponent > 0 else -1), abs(exponent)),
                    )
            for atom, free, eps in pp.fold_vector(raw, tuple(vec)):
                if atom[0] <= H:
                    atoms[atom] = (free, eps)
    return atoms


def star_atoms_4(r: int, signs):
    # Primitive star Omega=e_5 wedge (s13 e13+s17 e17+sr er).
    primes = (5, 13, 17, r)
    leaf = (signs[0], signs[1], signs[2])
    X0 = math.log(5)
    X1 = math.log(13) + math.log(17) + math.log(r)
    bx = int((L - 1e-12) // X0)
    by = int((L - 1e-12) // X1)
    atoms = {}
    for x in range(-bx, bx + 1):
        for y in range(-by, by + 1):
            if x == 0 and y == 0:
                continue
            vec = (x, y * leaf[0], y * leaf[1], y * leaf[2])
            if abs(x) * X0 + abs(y) * X1 >= L:
                continue
            raw = (1, 0)
            for prime, exponent in zip(primes, vec):
                if exponent:
                    raw = g2.pair_mul(
                        raw,
                        pp.ipow(pp.gaussian_prime(prime, 1 if exponent > 0 else -1), abs(exponent)),
                    )
            for atom, free, eps in pp.fold_vector(raw, vec):
                if atom[0] <= H:
                    atoms[atom] = (free, eps)
    return atoms


def atom_mu(atom):
    b, a = atom
    return 1.0 / math.log10(b / a)


def endpoint_coeff(triple):
    vecs = [row[2] for row in triple]
    eps = [row[3] for row in triple]
    rows = [tuple(vecs[j][i] for j in range(3)) for i in range(len(vecs[0]))]

    def cross(a, b):
        return (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        )

    r1 = next((row for row in rows if any(row)), None)
    r2 = next((row for row in rows if cross(r1, row) != (0, 0, 0)), None)
    if r2 is None:
        return None
    c = cross(r1, r2)
    g = math.gcd(math.gcd(abs(c[0]), abs(c[1])), abs(c[2]))
    if g == 0:
        return None
    c = tuple(x // g for x in c)
    if 0 in c or any(sum(row[j] * c[j] for j in range(3)) for row in rows):
        return None
    if c[0] < 0:
        c = tuple(-x for x in c)
    torsion = sum(c[j] * eps[j] for j in range(3)) % 8
    if torsion % 2 == 0:
        return None
    scale = min((torsion, torsion - 8), key=abs)
    return tuple(scale * x for x in c)


def low_mu_audit(atoms):
    rows = sorted((atom_mu(atom), atom, vec, eps) for atom, (vec, eps) in atoms.items())
    tested = endpoints = 0
    for i in range(len(rows) - 2):
        if rows[i][0] + rows[i + 1][0] + rows[i + 2][0] >= MU_BOUND:
            break
        for j in range(i + 1, len(rows) - 1):
            if rows[i][0] + rows[j][0] + rows[j + 1][0] >= MU_BOUND:
                break
            for k in range(j + 1, len(rows)):
                total = rows[i][0] + rows[j][0] + rows[k][0]
                if total >= MU_BOUND:
                    break
                tested += 1
                if endpoint_coeff((rows[i], rows[j], rows[k])) is not None:
                    endpoints += 1
    return tested, endpoints


def main():
    rmax, states3 = three_prime_states()
    atom_instances = tested = endpoints = 0
    for _, primes, omega in states3:
        atoms = plane_atoms_3(primes, omega)
        atom_instances += len(atoms)
        t, e = low_mu_audit(atoms)
        tested += t
        endpoints += e

    # Complete four-active-prime classification under P<=15.
    # A decomposable Pluecker support graph is complete multipartite and connected.
    # The weighted MST lower bound forces active primes {5,13,17,r}, r=29,37,41.
    # Any fourth edge would exceed the budget, so the graph is K_{1,3} centered at 5.
    # Coefficient magnitude >1 also exceeds the budget. Overall sign is quotiented,
    # leaving four sign states for each r.
    states4 = []
    for r in (29, 37, 41):
        for s17, sr in itertools.product((1, -1), repeat=2):
            states4.append((r, (1, s17, sr)))
    for r, signs in states4:
        atoms = star_atoms_4(r, signs)
        atom_instances += len(atoms)
        t, e = low_mu_audit(atoms)
        tested += t
        endpoints += e

    # Five active primes already exceed P=15 even at the minimum connected-tree cost.
    min5 = math.log(5) * (math.log(13) + math.log(17) + math.log(29) + math.log(37))
    assert min5 > P_CAP

    print(f"dynamic_rmax={rmax}")
    print(f"three_prime_states={len(states3)}")
    print(f"four_prime_states={len(states4)}")
    print(f"total_exterior_states={len(states3)+len(states4)}")
    print(f"generated_atom_instances={atom_instances}")
    print(f"low_mu_triples={tested}")
    print(f"endpoint_circuits={endpoints}")

    assert rmax == 868
    assert len(states3) == 518
    assert len(states4) == 12
    assert atom_instances == 59636
    assert tested == 2
    assert endpoints == 0
    print("complete P<=15 multi-prime exterior-shell certificate: PASS")


if __name__ == "__main__":
    main()
