#!/usr/bin/env python3
"""Independent exact integer raw-moment DP of the original 96-port BRC paths.
All six labelled actions retained. Separate from the rational resolvent certificate.
"""
from itertools import product
from math import comb
from fractions import Fraction
from pathlib import Path
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple((-1 if c>0 else 1)*k for k in STARS[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STARS[a] for sgn in (-1,1) for p in near(a,sgn*k))
ids={x:i for i,x in enumerate(phases)}
def succ(i):
    a,p,c=phases[i]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(ids[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(succ(i) for i in range(48)); TARGET=ids[(0,1,-3)]
ACTIONS=tuple(product(range(3),(0,1)))
E=[]
for i in range(96):
    ph,bit=divmod(i,2)
    row=[]
    for slot,newbit in ACTIONS:
        nx=NEXT[ph][slot]
        axis=abs(phases[ph][2])-1
        gate=int(bit==newbit==1 and nx==TARGET)
        row.append((2*nx+newbit,axis,gate))
    E.append(row)
assert all(len(row)==6 for row in E)
assert sum(g for row in E for _,_,g in row)==3

def raw_fourth_at_depths(coeff, depths=(16,32,64,128)):
    depths=tuple(sorted(depths));max_d=depths[-1]
    m=[[0]*5 for _ in range(96)]
    for i in range(96):m[i][0]=1
    n_paths=96; out={}
    for d in range(1,max_d+1):
        nxt=[[0]*5 for _ in range(96)]
        for i,row in enumerate(E):
            for j,axis,gate in row:
                r=coeff[axis]+coeff[6]*gate
                for k in range(5):
                    nxt[j][k]+=sum(comb(k,h)*r**(k-h)*m[i][h] for h in range(k+1))
        m=nxt;n_paths*=6
        if d in depths:
            e=[Fraction(sum(row[k] for row in m),n_paths) for k in range(5)]
            u,v,w,z=e[1:]
            k4=z-4*w*u-3*v*v+12*v*u*u-6*u**4
            out[str(d)]={'finite_rate_decimal':format(float(k4/d),'.12f'),
                         'finite_rate_exact':str(k4/d),'n_paths':str(n_paths)}
    return out

tests={'R1+K':(1,0,0,0,0,0,1),
       'R2+K':(0,1,0,0,0,0,1),
       'R1-R3+K':(1,0,-1,0,0,0,1)}
results={k:raw_fourth_at_depths(v) for k,v in tests.items()}
assert results['R1+K']['128']['finite_rate_exact']!=results['R2+K']['128']['finite_rate_exact']
result={'model':'frozen native 96 ports and six actions; all six axis rewards remain typed',
        'kind':'independent finite-depth exact integer raw-moment check',
        'results':results,'status':'ALL_ASSERTIONS_PASS'}
Path(__file__).with_name('PREFIX581_R2_independent_native_dp_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:{d:v['finite_rate_decimal'] for d,v in val.items()} for k,val in results.items()},indent=2))
print('ALL_ASSERTIONS_PASS')
