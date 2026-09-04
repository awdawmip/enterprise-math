#!/usr/bin/env python3
"""Exact audit of the new exterior topologies entering near P=25.89 in #1160.

This is NOT a complete P<=26 shell census.  It completely classifies and checks
only the topologies that do not occur at P<=20:
- four-prime K_{2,2};
- six-prime K_{1,5} star.

Within P<=26 these are forced to 4 and 16 primitive exterior states respectively.
All H=1,000,000 atoms in those 20 planes are generated exactly before the current
Lehmer threshold is applied.
"""

from __future__ import annotations

import importlib.util
import itertools
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "gregory_machin_exterior_shell_p20_check_20260904.py"
spec = importlib.util.spec_from_file_location("p20", BASE)
p20 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(p20)

pp = p20.pp
g2 = p20.g2
H = p20.H
L = p20.L
P_CAP = 26.0


def generic_plane_atoms(primes, u, v):
    Xu = sum(abs(c) * math.log(p) for p, c in zip(primes, u))
    Xv = sum(abs(c) * math.log(p) for p, c in zip(primes, v))
    bx = int((L - 1e-12) // Xu)
    by = int((L - 1e-12) // Xv)
    atoms = {}
    for x in range(-bx, bx + 1):
        for y in range(-by, by + 1):
            if x == 0 and y == 0:
                continue
            vec = tuple(x * a + y * b for a, b in zip(u, v))
            if sum(abs(e) * math.log(p) for p, e in zip(primes, vec)) >= L:
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


def main():
    # First non-star four-prime topology: K_{2,2}.  On the smallest split-prime
    # set the least partition is {5,13}|{17,29}; the other partitions exceed 26,
    # and replacing 29 by 37 also exceeds 26.  Any coefficient magnitude >1 is
    # far above the remaining budget.  Relative signs within the two parallel
    # classes give 2x2=4 distinct planes.
    k22_cost = (math.log(5) + math.log(13)) * (math.log(17) + math.log(29))
    assert k22_cost < P_CAP
    assert (math.log(5) + math.log(17)) * (math.log(13) + math.log(29)) > P_CAP
    assert (math.log(5) + math.log(13)) * (math.log(17) + math.log(37)) > P_CAP

    k22_states = []
    k22_atoms = k22_tested = k22_endpoints = 0
    for s13, s29 in itertools.product((1, -1), repeat=2):
        u = (1, s13, 0, 0)
        v = (0, 0, 1, s29)
        k22_states.append((u, v))
        atoms = generic_plane_atoms((5, 13, 17, 29), u, v)
        k22_atoms += len(atoms)
        t, e = p20.p15.low_mu_audit(atoms)
        k22_tested += t
        k22_endpoints += e

    # First six-active-prime topology. The minimum star is uniquely the first six
    # split primes, centered at 5. Replacing 41 by 53 exceeds 26; all edge
    # magnitudes are forced to one. Fix one overall sign, leaving 2^4=16 states.
    leaves = (13, 17, 29, 37, 41)
    base = math.log(5) * sum(math.log(p) for p in leaves)
    next_base = math.log(5) * sum(math.log(p) for p in (13, 17, 29, 37, 53))
    assert base < P_CAP < next_base

    star_states = []
    star_atoms = star_tested = star_endpoints = 0
    for tail in itertools.product((1, -1), repeat=4):
        coeffs = (1, *tail)
        star_states.append(coeffs)
        atoms = p20.star_atoms(leaves, coeffs)
        star_atoms += len(atoms)
        t, e = p20.p15.low_mu_audit(atoms)
        star_tested += t
        star_endpoints += e

    print(f"K22_cost={k22_cost:.15f}")
    print(f"six_star_cost={base:.15f}")
    print(f"K22_states={len(k22_states)} atoms={k22_atoms} low_mu={k22_tested} endpoints={k22_endpoints}")
    print(f"six_star_states={len(star_states)} atoms={star_atoms} low_mu={star_tested} endpoints={star_endpoints}")

    assert len(k22_states) == 4
    assert k22_atoms == 236
    assert k22_tested == 0
    assert k22_endpoints == 0
    assert len(star_states) == 16
    assert star_atoms == 998
    assert star_tested == 0
    assert star_endpoints == 0
    print("P<=26 new-topology onset certificate: PASS")


if __name__ == "__main__":
    main()
