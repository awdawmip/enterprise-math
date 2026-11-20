#!/usr/bin/env python3
"""Exact author audit of natural (1+6 theta_t)J at same-t reciprocal CM sheets.
Only standard-library modular arithmetic; imports predecessor checked ring,
does not run native H0/B0 and does not claim independent review.
"""
import json
from pathlib import Path
from d25_single_weighted_j_source_observer_20261027 import Quadratic, primes_below

COEFF = -77704704  # -2^9 * 3^3 * 7 * 11 * 73

def natural_H(r, x):
    fac = r.div(r.mul(x, r.add(r.one, x)), r.sub(r.one, x))
    return r.add(r.J(x), r.mul(r.z(6), r.mul(fac, r.Jprime(x))))

def check(p):
    r = Quadratic(p**3)
    xp = (3 % r.n, 2 % r.n)
    xm = r.inv(xp)
    assert xm == (3 % r.n, -2 % r.n)
    assert r.t(xp) == r.t(xm) == (pow(216, -1, r.n), 0)
    delta = r.sub(natural_H(r, xp), natural_H(r, xm))
    assert delta == (0, COEFF % r.n)
    for a, b in ((0,0),(1,0),(0,1),(2,3)):
        x = r.add(xp, (a*p, b*p))
        y = r.inv(x)
        assert r.t(x) == r.t(y)
        d = r.sub(natural_H(r,x),natural_H(r,y))
        assert d[0] % p == 0 and d[1] % p == COEFF % p, (p,a,b,d)
    return {"p":p, "difference_mod_p":COEFF % p}

def main():
    assert COEFF == -2**9 * 3**3 * 7 * 11 * 73
    target=[p for p in primes_below(5000) if p % 24 in (13,19)]
    assert len(target) == 166
    rows = [check(p) for p in target]
    assert all(r["difference_mod_p"] for r in rows)
    assert check(73)["difference_mod_p"] == 0
    result = {
      "status":"AUTHOR_EXACT_CHECK_PASS",
      "target_primes_below_5000":len(target),
      "same_t_local_deformation_checks":4*len(target),
      "exact_CM_difference":"-77704704*s=-2^9*3^3*7*11*73*s",
      "out_of_scope_p73_zero":True,
      "sample_residues":[r for r in rows if r["p"] in (13,19,37,373)],
      "arithmetic_dependency":"d25_single_weighted_j_source_observer_20261027.py",
      "admission":"AUTHOR_ONLY_UNREVIEWED_NOT_ADMITTED",
      "native_H0_B0_executed":False
    }
    Path(__file__).with_name("d25_natural_weighted_j_single_scalar_author_check_20261027.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__ == "__main__":
    main()
