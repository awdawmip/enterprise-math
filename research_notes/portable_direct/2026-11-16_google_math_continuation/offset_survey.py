"""Exact survey of six physical offsets for nearest-template, max norm, M=K=2.

Tail uses scalar R749SSA bound for q>=1350; every finite nonzero gap here
is >= 210/36, so the strict half-gap test suffices on that tail.
"""
from fractions import Fraction
from itertools import combinations, product
from math import lcm
import json

P = (455, -295, -25, 185, -25, -295)
errors = list(product(range(-2,3), repeat=2))
models = ('common', 'independent')
ss = list(range(6))
masks = {m: [j for j in ss if m & (1<<j)] for m in range(1,64)}
phase_pairs = list(combinations(ss,2))
gaps = {m:min(max(abs(P[(a+j)%6]-P[(b+j)%6]) for j in js)
                 for a,b in phase_pairs) for m,js in masks.items()}
assert set(gaps.values()) == {0,210,270}
assert 2*Fraction(63374339249936,28025208984321) < Fraction(210,36)

def counts(top):
    # C generating series before q shift is reciprocal of this polynomial.
    poly = [1]
    for w in (1,1,1,2,3,6):
        new = poly + [0]*w
        for i,coeff in enumerate(poly):
            new[i+w] -= coeff
        poly = new
    c,t = [0]*(top+1),[0]*(top+1)
    c[1] = 1
    for q in range(2,top+1):
        c[q] = -sum(poly[h]*c[q-h] for h in range(1,min(q,len(poly)-1)+1))
        t[q] = t[q-1]+c[q-1]
    return c,t

C,T=counts(1355)
def signal(q):
    base = 18*q**4+54*q**3-345*q*q+2070*q-16315
    # 36Y = [108 q^3(T+e) - base (C+d)]/[3(C+d)].
    return [(108*q**3*(T[q]+e)-base*(C[q]+d),3*(C[q]+d))
            if C[q]+d>0 else None for e,d in errors]
obs = [None]+[signal(q) for q in range(1,1356)]

def tables(r):
    y = obs[r:r+6]
    scale = lcm(*(v[1] for col in y for v in col if v))
    D = [[[None if v is None else abs(v[0]*(scale//v[1])-P[(b+j)%6]*scale)
           for v in col] for j,col in enumerate(y)] for b in ss]
    return scale,D

def masks_failed(r):
    a = r%6
    scale,D=tables(r)
    out = {'common':{},'independent':{}}
    if all(x is None or 2*x<210*scale for col in D[a] for x in col):
        return out
    def record(model,b,i,E,idx):
        if not E & (1<<i):
            return
        # Every subset of E containing anchor i admits this witness.
        sub=E
        while sub:
            if sub in live[model] and sub & (1<<i) and sub not in out[model]:
                js=masks[sub]
                choices=[idx[j] for j in js]
                true=max(D[a][j][idx[j]] for j in js)
                rival=max(D[b][j][idx[j]] for j in js)
                assert rival<=true
                out[model][sub] = dict(r=r,phase=a,rival=b,
                    errors=[errors[k] for k in choices],
                    true_distance=str(Fraction(true,36*scale)),
                    rival_distance=str(Fraction(rival,36*scale)))
            sub=(sub-1)&E
    for b in ss:
        if a==b: continue
        if live['common']:
            for k in range(len(errors)):
                local=[D[b][j][k] for j in ss]
                for i in ss:
                    anchor=D[a][i][k]
                    if anchor is None or local[i]>anchor:
                        continue
                    E=sum(1<<j for j in ss if local[j] is not None and local[j]<=anchor)
                    record('common',b,i,E,[k]*6)
        if live['independent']:
            # For a designated competing phase b, minimize its local
            # distances at all positions except the true-distance witness i.
            best=[min((u,k) for k,u in enumerate(col) if u is not None) for col in D[b]]
            for i in ss:
                good=[(u,k) for k,u in enumerate(D[a][i]) if u is not None and D[b][i][k]<=u]
                if not good:continue
                anchor,k=max(good)
                E=sum(1<<j for j in ss if best[j][0]<=anchor)
                ks=[p[1] for p in best];ks[i]=k
                record('independent',b,i,E,ks)
    return out

live={mode:{m for m in masks if gaps[m]} for mode in models}
wr={mode:{} for mode in models}
for r in range(1349,0,-1):
    out=masks_failed(r)
    for mode in models:
        wr[mode].update(out[mode])
        live[mode].difference_update(out[mode])
    if not any(live.values()):break
assert not any(live.values())
rows=[]
for m,J in masks.items():
    row={'J':J,'scaled_gap':gaps[m]}
    if gaps[m]:
        for mode in models:
            row[mode]=wr[mode][m]
    else:
        row['identical_phases']=next((a,b) for a,b in phase_pairs if all(P[(a+j)%6]==P[(b+j)%6] for j in J))
    rows.append(row)
if __name__=='__main__':
    for row in rows:
        J=row['J']
        print(''.join(map(str,J)),*(row[x]['r']+1 for x in models) if row['scaled_gap'] else ['inf','inf'])
    with open('offset_survey.json','w') as f:
        json.dump(rows,f,indent=2)
