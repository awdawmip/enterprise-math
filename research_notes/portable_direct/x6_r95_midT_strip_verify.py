#!/usr/bin/env python3
"""R95 exact Fraction author checker: 1<=T<11 strip and T=11 sharp endpoint."""
from itertools import product
from fractions import Fraction as Q
from pathlib import Path
import json
s=(10,-5,1); b=(14,-9,2); c=(24,-14,3)
ports=(11,15,16,26,27,38)

def port(a):return max(sum(max(z,0) for z in a),sum(max(-z,0) for z in a))
def gaps(a):
    x,y,z=a; u=x+3*y+6*z; v=3*x+12*y+30*z; h=7*x+39*y+126*z
    return abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)
def predict(p,S,T):
    if p>=27 and S>11:return Q(6)/(S+1),{c}
    ties={s}
    if p>=16 and S>=11:ties.add(b)
    if p>=27 and S==11:ties.add(c)
    return Q(1,2),ties

def test(max_q=38):
    a_list=[]
    for a in product(range(-max_q,max_q+1),repeat=3):
        if not any(a) or next((v for v in a if v),0)<0:continue
        q=port(a)
        if q<=max_q:a_list.append((a,q,gaps(a)))
    assert len(a_list)==95133
    tests=0; comparisons=0
    for T in (Q(1),Q(3),Q(8),Q(109,10)):
        for S in (Q(1),Q(5),Q(1099,100),Q(11),Q(1101,100),Q(100)):
            for p in ports:
                eta,winners=predict(p,S,T)
                bounds=[eta*d for d in (Q(2),1+S,1+T,1+S,1+T,S+T)]
                actual=set()
                for a,q,g in a_list:
                    if q>p:continue
                    comparisons+=1
                    if all(x<=limit for x,limit in zip(g,bounds)):
                        assert any(x==limit for x,limit in zip(g,bounds)),(a,p,S,T,'lower than claimed optimum')
                        actual.add(a)
                assert actual==winners,(p,S,T,actual,winners)
                tests+=1
    # Sharpness: at T=11, S=5, the old single-winner region already gains two directions.
    edge=set(); edge_bounds=[Q(1,2)*d for d in (Q(2),Q(6),Q(12),Q(6),Q(12),Q(16))]
    for a,q,g in a_list:
        if q<=11 and all(x<=limit for x,limit in zip(g,edge_bounds)):
            edge.add(a)
    assert edge=={s,(5,-4,1),(9,-5,1)},edge
    return {'schema':'EM_X6_R95_MID_T_STRIP_AUTHOR_CHECK_V1','q_cap':max_q,
            'unoriented_directions':len(a_list),'t_values':['1','3','8','109/10'],
            's_values':['1','5','1099/100','11','1101/100','100'],
            'port_cases':list(ports),'test_cases':tests,'direction_comparisons':comparisons,
            'edge_case':{'S':'5','T':'11','p':11,'ties':[list(x) for x in sorted(edge)]},
            'all_assertions_pass':True,'review':'AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED'}
if __name__=='__main__':
    result=test()
    Path(__file__).with_name('x6_r95_midT_strip_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))
