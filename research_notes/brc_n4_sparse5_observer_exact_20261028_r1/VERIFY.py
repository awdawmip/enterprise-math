#!/usr/bin/env python3
"""Exact Fraction verifier for 5-label observer; uses pinned N4 ancestor.
Run from an enterprise-math checkout: python research_notes/brc_n4_sparse5_observer_exact_20261028_r1/VERIFY.py
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util
import json

ancestor = Path(__file__).resolve().parent.parent / 'brc_n4_provenance_refined_tv_exact_20261028_r1' / 'VERIFY.py'
spec = importlib.util.spec_from_file_location('n4_pinned_predecessor', ancestor)
assert spec and spec.loader and ancestor.is_file(), str(ancestor)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
N, policy = module.N, module.policy
zero, one = F(0), F(1)


def check23(pol):
    for t in (2,3,4):
        info = {}
        for h, (_, r, _) in N[t].items():
            if r in info: assert pol[t,h] == info[r]
            else: info[r] = pol[t,h]


def tag(t, hist):
    if t == 1:
        return hist[0] + '_STOP1'
    if t >= 3 and hist.startswith('AU'):
        return 'AU_REACH3'
    if t >= 3 and hist.startswith('BU'):
        return 'BU_REACH3'
    return 'OTHER'


def dist(pol, margin=False):
    out = {'Q': {}, 'P': {}}
    for leaf, (q, lr, _) in N[4].items():
        alive = one
        for t, hist in enumerate((leaf[:1], leaf[:2], leaf[:3], leaf), 1):
            stop_p, stop_q, cont = pol[t, hist]
            for dec, stop in (('P', stop_p), ('Q', stop_q)):
                key = tag(t, hist) if margin else (t, dec, tag(t, hist))
                for law, mass in (('Q', q), ('P', q * lr)):
                    out[law][key] = out[law].get(key, zero) + mass * alive * stop
            alive *= cont
        assert alive == zero
    for law in out:
        assert sum(out[law].values(), zero) == one
    return out


def tv(p, q, law):
    return sum((abs(p[law].get(k, zero) - q[law].get(k, zero))
                for k in p[law].keys() | q[law].keys()), zero) / 2


def marginal(a, b, c):
    ans = {'A_STOP1': (one-a)/2, 'B_STOP1': (one-b)/2,
           'AU_REACH3': a*c/6, 'BU_REACH3': b*c/4}
    ans['OTHER'] = one - sum(ans.values(), zero)
    return ans


def case(delta, theta, c0, c1, extra=False):
    a, b = one-theta*delta, one-(one-theta)*delta
    xA = (one-theta)*c0 + theta*(one-delta)*c1
    xB = (one-theta)*(one-delta)*c0 + theta*c1
    cA, cB = xA/a, xB/b
    D = xA*b-xB*a
    assert D == theta*(one-theta)*delta*(2-delta)*(c0-c1)
    alpha, beta = a/6, b/4
    cstar = (alpha*cA+beta*cB)/(alpha+beta)
    optimum = alpha*beta/(alpha+beta)*abs(cA-cB)
    assert optimum == abs(D)/(4*a+6*b)
    target = policy(a, b, cA, cB)
    shared = policy(a, b, cstar, cstar)
    check23(shared)
    o, p = dist(target), dist(shared)
    assert tv(o, p, 'Q') == tv(o, p, 'P') == optimum
    qm = dist(target, True)['Q']
    assert qm['A_STOP1'] == (one-a)/2
    assert qm['B_STOP1'] == (one-b)/2
    assert qm['AU_REACH3'] == a*cA/6
    assert qm['BU_REACH3'] == b*cB/4
    if extra:
        for aa, bb, c in product((zero, F(1,3), a, one),
                                 (zero, F(1,2), b, one),
                                 (zero,F(1,4),F(1,3),cA,cB,cstar,F(3,4),one)):
            trial = policy(aa, bb, c, c)
            check23(trial)
            d = dist(trial, True)['Q']
            assert d == marginal(aa, bb, c)
            assert tv(o, dist(trial), 'Q') >= optimum
        # Test a genuinely competing history policy, not a frozen-tail assumption.
        trial = policy(F(3,5),F(4,5),F(2,5),F(2,5))
        trial[1,'A'] = (F(1,5), F(1,5), F(3,5))
        trial[1,'B'] = (F(1,8), F(3,40), F(4,5))
        trial[2,'AV'] = (F(1,4), F(1,4), F(1,2))
        trial[2,'BV'] = (F(1,5), F(3,10), F(1,2))
        assert dist(trial, True)['Q'] == marginal(F(3,5),F(4,5),F(2,5))
    return dict(D=str(D),a=str(a),b=str(b),cA=str(cA),cB=str(cB),
                cstar=str(cstar),d2_d23=str(optimum),d3='0')


def main():
    values = (zero,F(1,4),F(1,2),F(3,4),one)
    n = 0
    for delta,theta,c0,c1 in product(values[:-1],values,values,values):
        case(delta,theta,c0,c1,n%25==0)
        n += 1
    witness = case(F(1,2),F(1,2),F(1,2),F(1,4),True)
    assert witness['d2_d23']=='1/160' and witness['cstar']=='11/30'
    print(json.dumps({'status':'PASS_EXACT_N4_SPARSE5_GLOBAL_MINIMAX',
                      'sample_cases':n,'sample_competitors_per_slice':128,
                      'real_parameter_claim':'PROOF.md analytic universal argument',
                      'witness':witness,'admission':'AUTHOR_UNREVIEWED_NOT_ADMITTED'},
                     sort_keys=True,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
