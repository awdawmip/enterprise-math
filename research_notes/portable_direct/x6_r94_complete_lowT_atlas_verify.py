#!/usr/bin/env python3
"""Exact lattice crosscheck for the R94 complete low-T atlas (author check)."""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path

s=(10,-5,1); b=(14,-9,2); c=(24,-14,3)
PORTS=(11,15,16,26,27,38)

def q(a):
    return max(sum(max(t,0) for t in a),sum(max(-t,0) for t in a))

def gaps(a):
    x,y,z=a
    u=x+3*y+6*z; v=3*x+12*y+30*z; h=7*x+39*y+126*z
    return abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)

def expected(p,S,T):
    R=1/(1+T); A=5+6*T; B=6+5*T
    if p>=27 and S>B:
        return 6/(S+T),{c}
    winners={s}
    if p>=16 and S>=A:
        winners.add(b)
    if p>=27 and S==B:
        winners.add(c)
    return R,winners

def test(max_q=38):
    directions=[]
    for a in product(range(-max_q,max_q+1), repeat=3):
        if a==(0,0,0) or next((v for v in a if v),0)<0:
            continue
        qa=q(a)
        if qa<=max_q:
            directions.append((a,qa,gaps(a)))
    assert len(directions)==95133,(len(directions),'expected 95133 for q<=38')
    tests=[]
    for T in (Q(1,4),Q(1,2),Q(3,4)):
        A=5+6*T; B=6+5*T
        for S in (Q(1),Q(4),Q(5),A-Q(1,100),A,A+Q(1,100),B-Q(1,100),B,B+Q(1,100),B+6,Q(100)):
            for p in PORTS:
                eta,winners=expected(p,S,T)
                den=(Q(2),1+S,1+T,1+S,1+T,S+T)
                # All thresholds are rational. Compare integer gaps to exact rational boundaries.
                thresholds=[eta*d for d in den]
                ties=set()
                below=0
                inspected=0
                for a,qa,g in directions:
                    if qa>p:continue
                    inspected+=1
                    le=all(gi<=limit for gi,limit in zip(g,thresholds))
                    if not le:continue
                    if all(gi<limit for gi,limit in zip(g,thresholds)):
                        below+=1
                    else:
                        ties.add(a)
                assert below==0,(p,S,T,'strict competitor',below)
                assert ties==winners,(p,S,T,'ties',ties,'expected',winners)
                tests.append({'p':p,'S':str(S),'T':str(T),'eta':str(eta),'ties':[list(a) for a in sorted(ties)],'directions_checked':inspected})
    return {'schema':'EM_X6_R94_COMPLETE_LOW_T_ATLAS_AUTHOR_CHECK_V1',
        'scientific_pin':'enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json',
        'q_cap':max_q,'unoriented_directions':len(directions),
        't_values':['1/4','1/2','3/4'],'s_cases_per_t':11,'port_cases':list(PORTS),
        'test_cases':len(tests),'direction_comparisons':sum(t['directions_checked'] for t in tests),
        'all_assertions_pass':True,
        'proof_scope':'Unbounded integer lattice proven symbolically in companion R94; finite exact Fraction crosscheck only.',
        'review':'AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED',
        'cases':tests}

if __name__=='__main__':
    result=test()
    out=Path(__file__).with_name('x6_r94_complete_lowT_atlas_results.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},ensure_ascii=False,indent=2))
