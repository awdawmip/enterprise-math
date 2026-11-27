from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import gcd, floor, ceil
import json, hashlib
# Replay the exact finite lattice domain of PREFIX-1128, without redoing its original scans.
exec(Path('prefix1128_verify.py').read_text().split('L0=10**90')[0])
L=10**100; Q=3*10**60
lines, ranges, volume=scan(L,Q,V2)
assert len(lines)==115 and volume==620
assert lines==[tuple(map(int,row)) for row in json.load(open('prefix1128_result.json'))['runs'][-1]['lines']]
results=[json.loads(row) for row in open('direct_all.jsonl')]
assert len(results)==len(lines)
d0=sum(d)/2
margins=[]
for (q,p,h),r in zip(lines,results):
    assert (q,p,h)==tuple(int(r[k]) for k in ('q','p','h')) and int(r['L'])==L
    rr=tuple(map(F,r['rho']));cs=tuple(map(F,r['c']));tr=tuple(map(F,r['t']))
    assert rr==(F(p,q),F(p,q)+d0/L**2) and cs==(F(h,q)-2*d0/L,F(h,q))
    assert R[0]<=rr[0]<=rr[1]<=R[1] and C[0]<=cs[0]<=cs[1]<=C[1]
    assert T[0]<=tr[0]<=tr[1]<=T[1] and tr[0]**2<=36/(1+rr[1])<=36/(1+rr[0])<=tr[1]**2
    center=tuple(map(F,r['cent'])); cols=[tuple(map(F,z)) for z in r['cols']]; error=tuple(map(F,r['error']))
    assert len(cols)==12 and all(v>=0 for v in error)
    assert any(u*z-v*w for u,v in cols for w,z in cols)
    # For full-dimensional midpoint zonotope, normals perpendicular to generators contain every facet normal.
    # Including axis normals is redundant but useful for checking the coordinate payments.
    margins_row=[]
    for u,v in cols+[(F(1),F(0)),(F(0),F(1))]:
        if u or v:
            n=(-v/max(abs(u),abs(v)),u/max(abs(u),abs(v)))
            margins_row.append(sum(abs(dot(n,z)) for z in cols)-abs(dot(n,center))-dot(tuple(map(abs,n)),error))
    margin=min(margins_row);assert margin==F(r['margin']) and margin>F(9671,10**89)
    assert F(r['slope'][1])<0 and q<L/3 and gcd(p,q)==1
    margins.append(margin)
assert min(margins)>0
print('full compact model:',len(lines),'positive certificates; min',float(min(margins)),'row',margins.index(min(margins))+1,'first',float(margins[0]))
# Two explicit sharp-window witnesses; d is a separately retained scalar, not a derived jet constraint here.
q,p,h=lines[0];r0=(-h*pow(p,-1,q))%q
L3=L2=10**8
while L3<=d[0]*q*q/(4*E): L3*=2
while L2<q*q: L2*=2
witnesses=[]
for kind,S in [('triple',L3),('sqrt_pair',L2)]:
    z=2*S-1-((2*S-1-r0)%q);a=z-(2 if kind=='triple' else 1)*q;b=a+q
    assert L<=S<=a<b<=z<2*S
    lam=d0*q*q/(2*a*b*z) if kind=='triple' else F(0)
    rho=F(p,q)+d0/(a*z);c=F(h,q)-d0*(F(1,a)+F(1,z))+lam
    assert F(p,q)<=rho<=F(p,q)+d0/L**2 and F(h,q)-2*d0/L<=c<=F(h,q)
    ms=[a,b,z] if kind=='triple' else [a,z];payments=[]
    for m in ms:
        assert (p*m+h)%q==0
        e=rho*m+c+d0/m-(p*m+h)//q
        assert abs(e)*m*m<=E
        payments.append(abs(e)*m*m/E)
    if kind=='sqrt_pair': assert q*q<=S and max(payments)==0
    print(kind,'first L',S,'maximum budget',float(max(payments)))
    witnesses.append({'kind':kind,'L':str(S),'m':list(map(str,ms)),'rho':str(rho),'c':str(c),'d':str(d0),'max_budget':str(max(payments))})
Path('prefix1129_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
