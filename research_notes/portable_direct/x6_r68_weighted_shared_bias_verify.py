"""Exact checks for X6 R68: weighted common-bias positive-BRC moments.

Only conditional, named positive-branch observer models; no native-triad inference.
Requires Python 3 standard library. Integer and Fraction arithmetic throughout.
"""
from fractions import Fraction as F
from itertools import product
import json


def moment_z(a):
    D = len(a) + 1
    return tuple([0] + [sum(a[d - 2] * (d**t - d) for d in range(2, D + 1)) for t in range(2, D + 1)])


def q(a):
    return max(sum(max(x, 0) for x in a), sum(max(-x, 0) for x in a))


def radius(z, w):
    assert len(z) == len(w)
    return max((F(abs(z[i] - z[j]), 2) / (w[i] + w[j]) for i in range(len(z)) for j in range(i + 1, len(z))), default=F(0))


def predicted_plateau(w):
    return 1 / min(w[i] + w[j] for i in range(len(w)) for j in range(i + 1, len(w)) if (i - j) % 2)


def canonical_a(D):
    from math import comb
    return tuple((-1)**d * comb(D + 1, d + 1) for d in range(2, D + 1))


def exhaustive(D, p, w):
    minimum = None
    winners = []
    tested = 0
    feasible = 0
    for a in product(range(-p, p + 1), repeat=D - 1):
        tested += 1
        if not any(a) or q(a) > p:
            continue
        feasible += 1
        r = radius(moment_z(a), w)
        if minimum is None or r < minimum:
            minimum, winners = r, [a]
        elif r == minimum:
            winners.append(a)
    return {"D":D,"p":p,"weights":[str(x) for x in w],"tested":tested,"feasible":feasible,"minimum":str(minimum),"winner_count":len(winners),"sample_winners":[list(x) for x in winners[:4]]}


def bound_check():
    # Exact constructive witness for the all-D plateau theorem, with nonuniform weights.
    W = {
        2:(F(1),F(3,2)),
        3:(F(1),F(6,5),F(4,5)),
        4:(F(1),F(6,5),F(4,5),F(11,10)),
        6:(F(1),F(6,5),F(4,5),F(11,10),F(9,10),F(1)),
    }
    examples = []
    for D, w in W.items():
        a = canonical_a(D)
        z = moment_z(a)
        p = max(D, 2**D-D-1)
        assert q(a) <= p
        assert z == tuple(2 if (t % 2 == 0) else 0 for t in range(1, D+1))
        assert max(w) < 2*min(w)
        assert radius(z,w) == predicted_plateau(w)
        examples.append({"D":D,"p":p,"weights":[str(x) for x in w],"a":list(a),"z":list(z),"radius":str(radius(z,w))})
    return examples


def counterexample():
    w=(F(1), F(1), F(100), F(100))
    a0=canonical_a(4)
    a1=(3,-1,0)
    assert q(a0)<=11 and q(a1)<=11
    r0=radius(moment_z(a0),w)
    r1=radius(moment_z(a1),w)
    assert r0==F(1,2) and r1==F(18,101) and r1<r0
    return {"D":4,"p":11,"weights":[str(x) for x in w],"plateau":{"a":list(a0),"z":list(moment_z(a0)),"radius":str(r0)},"competitor":{"a":list(a1),"z":list(moment_z(a1)),"radius":str(r1)}}


def main():
    examples=bound_check()
    cases=[
        (2,2,(F(1),F(3,2))),
        (3,4,(F(1),F(6,5),F(4,5))),
        (4,11,(F(1),F(6,5),F(4,5),F(11,10))),
        (4,11,(F(1),F(1),F(100),F(100))),
    ]
    checks=[]
    for D,p,w in cases:
        out=exhaustive(D,p,w)
        if max(w)<2*min(w):
            assert F(out['minimum']) == predicted_plateau(w)
            assert out['winner_count']==2
        checks.append(out)
    result={"schema":"X6_R68_HETEROSCEDASTIC_BIAS_MINIMAX_V1","scientific_status":"CONDITIONAL_AUTHOR_PROOF_EXACT_FINITE_CHECK_NOT_INDEPENDENTLY_REVIEWED", "frozen_p000":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json","model":"m_t=sum c_d d^t, y_t=m_t+b+e_t, |e_t|<=eta*w_t, w_t>0 rational","theorem":"eta_pair=1/2 max_{i<j}|z_i-z_j|/(w_i+w_j); when p>=max(D,2^D-D-1), max(w)<2min(w): eta_star=1/min_{odd-even pair}(w_i+w_j)","constructive_checks":examples,"finite_exhaustive_checks":checks,"unequal_precision_counterexample":counterexample()}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
