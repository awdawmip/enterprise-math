#!/usr/bin/env python3
"""Exact signed X6 typed-BRC finite-horizon Link flux and Gram-rank checker.
No standard Euclidean geometric interpretation of P000's native angle is used.
"""
from collections import defaultdict
import json

DIRECTIONS = []
for sign in (1,-1):
    for j in range(6):
        d=[0]*6;d[j]=sign;DIRECTIONS.append(tuple(d))
ZERO=(0,)*6
E1=DIRECTIONS[0]
CHANS=((ZERO,0),(E1,6))

def plus(x,d): return tuple(a+b for a,b in zip(x,d))
def neg_index(k): return (k+6)%12
def w(h,d): return 1-6*(h==d)

def apply(v, absorbing=True):
    o=defaultdict(int)
    for (x,h),a in v.items():
        for d,step in enumerate(DIRECTIONS):
            if absorbing and ((x==ZERO and d==0) or (x==E1 and d==6)):
                continue
            y=plus(x,step)
            o[(y,neg_index(d))]+=w(h,d)*a
    return {k:a for k,a in o.items() if a}

def flux(v):
    f=[]
    for x,d in CHANS:
        f.append(sum(w(h,d)*v.get((x,h),0) for h in range(12)))
    return tuple(f)

def norm(v): return sum(a*a for a in v.values())
def inner(v,u): return sum(a*u.get(k,0) for k,a in v.items())

def seed(s,orientation):
    assert s>=0
    x=[0]*6;x[1]=s
    if orientation=="plus":
        h=6
    else:
        x[0]=1;h=0
    return {(tuple(x),h):1}

def check(H):
    witnesses=[seed(s,side) for s in range(H) for side in ('plus','minus')]
    paths=[v for v in witnesses]
    B=[]
    for t in range(H):
        B += [[flux(v)[j] for v in paths] for j in range(2)]
        paths=[apply(v) for v in paths]
    for t in range(H):
        for s in range(H):
            for a in range(2):
                for b in range(2):
                    observed=B[2*t+a][2*s+b]
                    if t<s: assert observed==0,(t,s,a,b,observed)
                    if t==s: assert observed==int(a==b),(t,s,a,b,observed)
    for i in range(2*H):
        for j in range(2*H):
            orig=36**H*inner(witnesses[i],witnesses[j])
            final=inner(paths[i],paths[j])
            lossy=sum(36**(H-1-t)*sum(B[2*t+a][i]*B[2*t+a][j] for a in range(2)) for t in range(H))
            assert orig-final==lossy,(H,i,j,orig,final,lossy)
    return {'H':H,'rank':2*H,'det_B':1,'last_row_plus':B[2*(H-1)],'last_row_minus':B[2*(H-1)+1],
            'states_last_step_max':max(len(p) for p in paths),
            'gram_identity':'PASS','B_diagonal_identity':'PASS',
            'first_basis_H_norm':norm(paths[0]),'last_basis_H_norm':norm(paths[-1])}

if __name__=='__main__':
    results=[]
    for H in range(1,6):
        r=check(H);results.append(r);print('H',H,'rank',r['rank'],'max states',r['states_last_step_max'],'identity OK',flush=True)
    v={((0,0,0,0,0,0),6):2,((0,1,0,0,0,0),1):-1,((1,0,0,0,0,0),0):3}
    dissip=[]
    for t in range(6):
        f=flux(v);n=norm(v);v2=apply(v)
        assert norm(v2)==36*n-(f[0]**2+f[1]**2)
        dissip.append({'t':t,'norm':n,'phi_plus':f[0],'phi_minus':f[1],'norm_after':norm(v2)})
        v=v2
    result={'model':'X6 signed typed BRC Stage46 Link {0,e1}; numerator W=J_12-6I_12','checks':results,'dissipation':dissip,'arithmetic':'exact Python integers','claim':'B_H rows full rank 2H for every integer H>=1 by triangular witness proof; numeric verified H=1..5'}
    out='PREFIX1020_R6_EXACT_CERTIFICATE.json'
    with open(out,'w') as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print('WROTE',out)
