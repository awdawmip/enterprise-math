#!/usr/bin/env python3
"""Complete rational source family for the exact tree-depth obstruction."""
from fractions import Fraction
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent
SCALE=10**40

def energy(raw,den,first,mode='full'):
    lo=hi=0
    for k,v in enumerate(raw):
        if mode=='positive': v=max(v,0)
        d=den*den*(first+k)**2
        num=SCALE*v*v
        lo+=num//d
        hi+=(num+d-1)//d
    return lo,hi

def rec(v):
    return {'integer_bounds':[str(v[0]),str(v[1])],
            'denominator_power_of_10':40}

rows=[]
for s in [8,12,16]:
    X=s**4;h=s**3;den=h**3
    y=[j*j for j in range(s)]+[0]
    q=[];rem=[]
    for k in range(X+1):
        if k==X:
            q.append(0);rem.append(0);continue
        j,r=divmod(k,h)
        inc=y[j+1]-y[j]
        smooth=3*r*r*h-2*r*r*r
        raw=y[j]*den+inc*smooth
        q.append(raw)
        rem.append(inc*(smooth-r*h*h))
    assert len(q)==X+1 and q[0]==q[-1]==0 and min(q)>=0
    assert all(q[j*h]==y[j]*den for j in range(s+1))
    ext=[0]+q+[0]
    f=[2*ext[k+1]-ext[k]-ext[k+2] for k in range(X+1)]
    assert all(abs(v)*X<=6*den for v in f)
    forced=0
    for k in range(s-1):
        for j in range(k+2,s):
            chord=Fraction(y[k]*(j-k-1)+y[j],j-k)
            assert chord>y[k+1]
            forced+=1
    eq=energy(q,den,X)
    ep=energy(rem,den,X)
    epp=energy(rem,den,X,'positive')
    bound=Fraction(1,16*s)+Fraction(1,12*s*s)
    assert eq[0]*256>=SCALE and eq[1]<=2*SCALE
    assert Fraction(ep[1],SCALE)<=bound
    rows.append({'s':s,'X':X,'fine_step':h,'fine_cells':s,
                 'required_occupied_depth':s-1,'complete_integer_count':X+1,
                 'max_source_exact':str(Fraction(max(map(abs,f)),den)),
                 'uniform_source_bound':'6/X <= 12/n',
                 'strict_forced_root_comparisons':forced,
                 'actual_positive_energy':rec(eq),'fine_full_remainder_energy':rec(ep),
                 'fine_positive_remainder_energy':rec(epp),
                 'fine_remainder_proved_bound':str(bound)})

result={'status':'PASS','scope':'Auxiliary general-source family, not the actual arithmetic road',
        'method':'exact rational values and source; outward integer energy intervals',
        'infinite_family_proof':'TREE_DEPTH_OBSTRUCTION.md','rows':rows}
(OUT/'tree_depth_obstruction_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','s_values':[r['s'] for r in rows],
                  'complete_integer_count':sum(r['complete_integer_count'] for r in rows)}))
