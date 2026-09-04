#!/usr/bin/env python3
"""Complete weighted-Pluecker shell audit P(Omega)<=20 for #1160.

Extends the exact P<=15 shell.  At weighted height 20:
- six active split primes remain impossible by the spanning-tree lower bound;
- five active primes are forced to the unique set {5,13,17,29,37}, with a K1,4
  star centered at 5 and primitive edge magnitudes one;
- four active primes are still forced to K1,3 stars centered at 5, but their
  leaf set and primitive coefficients are enumerated completely from the budget;
- all three-active-prime primitive exterior states are dynamically enumerated.

For every plane, all H=1,000,000 atom columns are generated and only triples with
mu<1.2096120143032323 are sent to exact rank-two+C8 endpoint certification.
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_exterior_shell_p15_check_20260904.py"
spec = importlib.util.spec_from_file_location("p15", BASE)
p15 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(p15)

pp = p15.pp
g2 = p15.g2
H = p15.H
L = p15.L
MU_BOUND = p15.MU_BOUND
P_CAP = 20.0


def three_prime_states():
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


def star_atoms(leaves, coeffs):
    primes = (5, *leaves)
    X0 = math.log(5)
    X1 = sum(abs(c) * math.log(p) for p, c in zip(leaves, coeffs))
    bx = int((L - 1e-12) // X0)
    by = int((L - 1e-12) // X1)
    atoms = {}
    for x in range(-bx, bx + 1):
        for y in range(-by, by + 1):
            if x == 0 and y == 0:
                continue
            vec = (x, *(y * c for c in coeffs))
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


def four_prime_states():
    # K_{2,2} already has minimum weighted edge cost >20.  Hence every four-prime
    # state is a K_{1,3} star.  A center at 13 already exceeds the budget, so the
    # center is forced to 5.
    assert (
        math.log(5) * math.log(17)
        + math.log(5) * math.log(29)
        + math.log(13) * math.log(17)
        + math.log(13) * math.log(29)
    ) > P_CAP
    assert math.log(13) * (math.log(5) + math.log(17) + math.log(29)) > P_CAP

    leaf_budget = P_CAP / math.log(5)
    rmax = math.floor(math.exp(leaf_budget - math.log(13) - math.log(17))) + 2
    split = [p for p in pp.primes_upto(rmax) if p % 4 == 1 and p != 5]
    out = []
    for i, p in enumerate(split):
        lp = math.log(p)
        for j in range(i + 1, len(split)):
            q = split[j]
            lq = math.log(q)
            for r in split[j + 1 :]:
                lr = math.log(r)
                if lp + lq + lr > leaf_budget + 1e-12:
                    break
                ba = int(leaf_budget // lp)
                bb = int(leaf_budget // lq)
                bc = int(leaf_budget // lr)
                for a in range(1, ba + 1):  # overall sign fixes first leaf positive
                    for b in range(-bb, bb + 1):
                        if b == 0:
                            continue
                        for c in range(-bc, bc + 1):
                            if c == 0:
                                continue
                            if a * lp + abs(b) * lq + abs(c) * lr > leaf_budget + 1e-12:
                                continue
                            if math.gcd(math.gcd(a, abs(b)), abs(c)) != 1:
                                continue
                            out.append(((p, q, r), (a, b, c)))
    return rmax, out


def five_prime_states():
    # Minimum connected-tree support is the 5-centered star.  The first five
    # split primes fit just below 20; replacing 37 by 41 exceeds it.
    base = math.log(5) * (math.log(13) + math.log(17) + math.log(29) + math.log(37))
    next_base = math.log(5) * (math.log(13) + math.log(17) + math.log(29) + math.log(41))
    assert base < P_CAP < next_base
    # Any extra edge or coefficient magnitude >1 also exceeds the budget.
    return [(13, 17, 29, 37)], [(1, *tail) for tail in itertools.product((1, -1), repeat=3)]


def main():
    rmax3, states3 = three_prime_states()
    rmax4, states4 = four_prime_states()
    leaves5, coeffs5 = five_prime_states()

    # Six active primes are impossible even at the minimum spanning-tree weight.
    min6 = math.log(5) * (
        math.log(13) + math.log(17) + math.log(29) + math.log(37) + math.log(41)
    )
    assert min6 > P_CAP

    atom_instances = tested = endpoints = 0

    # Reuse exact plane recovery / endpoint routines from the P15 checker.
    for _, primes, omega in states3:
        atoms = p15.plane_atoms_3(primes, omega)
        atom_instances += len(atoms)
        t, e = p15.low_mu_audit(atoms)
        tested += t
        endpoints += e

    for leaves, coeffs in states4:
        atoms = star_atoms(leaves, coeffs)
        atom_instances += len(atoms)
        t, e = p15.low_mu_audit(atoms)
        tested += t
        endpoints += e

    for coeffs in coeffs5:
        atoms = star_atoms(leaves5, coeffs)
        atom_instances += len(atoms)
        t, e = p15.low_mu_audit(atoms)
        tested += t
        endpoints += e

    total_states = len(states3) + len(states4) + len(coeffs5)
    print(f"three_prime_rmax={rmax3}")
    print(f"four_prime_rmax={rmax4}")
    print(f"three_prime_states={len(states3)}")
    print(f"four_prime_states={len(states4)}")
    print(f"five_prime_states={len(coeffs5)}")
    print(f"total_exterior_states={total_states}")
    print(f"generated_atom_instances={atom_instances}")
    print(f"low_mu_triples={tested}")
    print(f"endpoint_circuits={endpoints}")

    assert rmax3 == 19184
    assert rmax4 == 1130
    assert len(states3) == 13374
    assert len(states4) == 2336
    assert len(coeffs5) == 8
    assert total_states == 15718
    assert atom_instances == 1337555
    assert tested == 172
    assert endpoints == 0
    print("complete P<=20 multi-prime exterior-shell certificate: PASS")


if __name__ == "__main__":
    main()
