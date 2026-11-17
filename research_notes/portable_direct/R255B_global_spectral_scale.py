#!/usr/bin/env python3
"""R255B exact rational spectral-scaling theorem: exhaustive finite spot checks."""
from fractions import Fraction as F
from math import gcd
import hashlib, json
from pathlib import Path
from R255_padics import sources, spectral_scale, v, PIN

def predict(s, t):
    return (13 if v(s,13) is not None and v(s,13)<=-2 else 1) * (23 if v(t,23) is not None and v(t,23)<=-2 else 1)

def get(s):
    a,b=sources(s);e,t,polys=spectral_scale(a,b)
    ratio=e//t
    expected=predict(s,a[6])
    assert ratio==expected,(s,a[6],ratio,expected)
    return {'s':str(s),'t':str(a[6]),'E':str(e),'T_min':str(t),'ratio':ratio,
            'predicted_ratio':expected,'v13_s':v(s,13),'v23_t':v(a[6],23),
            'mask_count':len(polys),'coefficient_count':sum(len(q)-1 for q in polys)}

def main():
    special=[F(2,5),F(46,117),F(66,169),F(67,169),F(857,2197),F(770,1973),F(767,1966),F(866,2197)]
    cases=[get(s) for s in special]
    assert {c['ratio'] for c in cases}=={1,13,23,299}
    finite=[]
    for q in range(1,501):
        for p in range(39*q//100,41*q//100+2):
            if gcd(p,q)!=1:continue
            s=F(p,q)
            if F(39,100)<s<F(41,100):finite.append(get(s))
    assert len(finite)==1522,len(finite)
    counts={str(f):sum(c['ratio']==f for c in finite) for f in (1,13,23,299)}
    grid=[get(F(j,1000)) for j in range(390,411)]
    assert all(c['ratio']==1 for c in grid)
    out={
        'schema':'EM_R255B_COMPLETE_RATIONAL_SPECTRAL_SCALE_LAW_V1',
        'frozen_science_pin':PIN,
        'domain':'rational 39/100<s<41/100; t(s)=(1691s-2615)/(2615s-3539)',
        'theorem':'T_min(s)=E(s)/(13^(v_13(s)<=-2)*23^(v_23(t(s))<=-2))',
        'arithmetic':'exact Fraction/integers; sample verification is independent of all-parameter proof',
        'verified_all_q_upto':500,
        'unique_reduced_parameters':len(finite),
        'complete_denominator_bounded_counts':counts,
        'grid_21_all_quotients_one':True,
        'special_examples':cases,
        'theorem_argument':'pair-plus-singleton traces force the input-entry denominator at p away from 13/23; R255 p-adic coefficient and trace laws resolve both exceptional primes',
        'scope':'minimal common integral characteristic scaling of all 63 labelled masks, not minimal reduced output denominator',
        'review':'AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED',
        'passed':True,
    }
    raw=json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    target=Path(__file__).with_name('R255B_verification.json')
    target.write_text(raw)
    print('PASS',len(finite),'reduced rational parameters (q<=500); ratio counts:',counts)
    print('special',[(x['s'],x['ratio']) for x in cases])
    print('SHA256',hashlib.sha256(raw.encode()).hexdigest())
if __name__=='__main__':main()
