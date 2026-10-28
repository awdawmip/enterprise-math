#!/usr/bin/env python3
"""N4 one-bit provenance exact Fraction witness checker.
Dependency: pinned research_notes/brc_n4_provenance_refined_tv_exact_20261028_r1/VERIFY.py
Run from the checked-out enterprise-math repository.
"""
from fractions import Fraction as R
import importlib.util
from pathlib import Path
import json

ancestor = (Path(__file__).resolve().parent.parent /
            'brc_n4_provenance_refined_tv_exact_20261028_r1' / 'VERIFY.py')
spec = importlib.util.spec_from_file_location('n4_source', ancestor)
assert ancestor.is_file() and spec is not None and spec.loader is not None
N4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(N4)
N, make = N4.N, N4.policy
Z = R(0)

def distribution(d, binary=True):
    ans = {'P': {}, 'Q': {}}
    for leaf, (q, lr, _) in N[4].items():
        live = R(1)
        for t, hist in enumerate((leaf[:1], leaf[:2], leaf[:3], leaf), 1):
            p, qq, cont = d[t, hist]
            assert min(p, qq, cont) >= 0 and p+qq+cont == 1
            assert t != 4 or cont == 0
            label = ('AU_REACH3' if t >= 3 and hist.startswith('AU') else 'OTHER')
            for decision, mass in (('P', p), ('Q', qq)):
                key = (t, decision, label) if binary else (t, decision)
                for law, weight in (('Q', q), ('P', q*lr)):
                    ans[law][key] = ans[law].get(key, Z) + weight*live*mass
            live *= cont
        assert live == 0
    for law in ans:
        assert sum(ans[law].values(), Z) == 1
    return ans

def tv(a,b,law):
    return sum((abs(a[law].get(k,Z)-b[law].get(k,Z))
                for k in a[law].keys()|b[law].keys()), Z)/2

def check_info(d, times):
    for t in times:
        seen = {}
        for h, (_, lr, _) in N[t].items():
            if lr in seen: assert d[t,h] == seen[lr]
            seen[lr] = d[t,h]

def main():
    a=b=R(3,4)
    ca,cb=R(5,12),R(1,3)
    alpha,beta=a/6,b/4
    delta=beta*(ca-cb)
    cs=(alpha*ca+beta*cb)/(alpha+beta)
    F=make(a,b,ca,cb)
    G=make(a,b,cs,cs)
    H=make(a,b,cs,cs,repair_B=R(1,11))
    check_info(F,(3,4))
    check_info(G,(2,3,4))
    check_info(H,(2,3,4))
    assert distribution(F,False)==distribution(H,False)
    O,OO=distribution(F),distribution(G)
    assert all(tv(O,OO,law)==R(1,160) for law in ('P','Q'))
    assert delta==R(1,64) and cs==R(11,30)
    # From the universal proof: Delta <= 5/2 TV_Q + TV_P <= 7/2 E.
    lower=delta/R(7,2)
    assert lower==R(1,224)
    assert sum(v for k,v in O['Q'].items() if k[2]=='AU_REACH3')==a*ca/6
    print(json.dumps({'status':'PASS_EXACT_N4_BINARY_PROVENANCE_WITNESS',
                      'binary_labels':2,'constant_tag_zero_TD':True,
                      'upper_TV_P':str(tv(O,OO,'P')),
                      'upper_TV_Q':str(tv(O,OO,'Q')),
                      'universal_analytic_lower_from_PROOF':str(lower),
                      'symbolic_theorem_not_inferred_from_finite_checks':True,
                      'admission':'AUTHOR_UNREVIEWED_NOT_ADMITTED'},sort_keys=True))

if __name__=='__main__': main()
