#!/usr/bin/env python3
"""PREFIX-316 exact provenance-tagged ordered BRC checker (Python stdlib)."""
from fractions import Fraction as F
from pathlib import Path
import json

def z(a=0,b=0): return F(a),F(b)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[0],-a[1]
def mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a): return a[0],-a[1]
def sc(a,k): return a[0]*k,a[1]*k
def sub(a,b): return add(a,neg(b))
def norm2(a): return mul(a,conj(a))[0]
def times(s,a): return tuple(mul(s,t) for t in a)
def distance2(a,b): return sum(norm2(sub(x,y)) for x,y in zip(a,b))

A=((z(4),z(4),z()),(z(),z(-4),z(4)),
   (z(-5,3),z(),z(-3,1)),(z(-2,-2),z(4,4),z(2,2)),
   (z(-2),z(),z(5,2)))
U=tuple(tuple(sc(q,F(1,8)) for q in row) for row in A)
b0=(z(-2),z(0,-2),z(1))
b2=(z(0,2),z(2),z(0,-1))
ii=z(0,1); one=z(1)
u=z(F(24,25),F(7,25)); v=z(F(312,313),F(25,313))
r=F(25,54)
assert norm2(u)==norm2(v)==1
S=tuple(tuple(sc(a,r) for a in t) for t in
        (times(neg(u),b0),times(mul(ii,v),b0),
         times(mul(ii,conj(u)),b2),times(neg(conj(v)),b2)))
assert len(set(S))==4

nread=0; npairs=0
def brc_mass(j,a,rho=None):
    global nread,npairs
    p=[('source:'+str(k+1),mul(U[j][k],a[k])) for k in range(3)]
    if rho is not None: p.append(('reference',rho))
    assert len(set(q[0] for q in p))==len(p)
    out=z()
    for tag1,t in p:
        for tag2,s in p:
            out=add(out,mul(t,conj(s))); npairs+=1
    nread+=1
    assert out[1]==0 and out[0]>=0
    return out[0]

for j in range(3):
    for k in range(3):
        v0=z()
        for row in U: v0=add(v0,mul(conj(row[j]),row[k]))
        assert v0 == (z((F(31,32),F(1),F(63,64))[j]) if j==k else z())

base=tuple(brc_mass(j,S[0]) for j in range(5))
assert base==(F(625,1458),F(3125,11664),F(23125,93312),F(15625,23328),F(53125,186624))
for a in S[1:]: assert tuple(brc_mass(j,a) for j in range(5))==base
readings={}; reports={}; spreads={}
for name,rho in [('Q1',one),('Qi',ii)]:
    readings[name]=[]; reports[name]=[]; spreads[name]=[]
    for j in range(5):
        vals=tuple(brc_mass(j,a,rho) for a in S)
        lo,hi=min(vals),max(vals)
        assert hi-lo<=2
        y=(lo+hi)/2
        assert all(abs(x-y)<=1 for x in vals)
        readings[name].append(vals);reports[name].append(y)
        spreads[name].append(hi-lo)
assert max(spreads['Q1']+spreads['Qi'])==2
assert spreads['Q1'][4]==2

weights=(F(1919750,7101273),F(3261773,14202546),
         F(1919750,7101273),F(3261773,14202546))
assert all(w>0 for w in weights) and sum(weights)==1
center=tuple(z(sum(weights[k]*S[k][j][0] for k in range(4)),
               sum(weights[k]*S[k][j][1] for k in range(4))) for j in range(3))
assert center==(z(0,F(-560900,1976643)),z(0,F(1017125,1976643)),z(0,F(280450,1976643)))
R2=F(333788125,213477444)
assert all(distance2(x,center)==R2 for x in S)
assert all(sum(norm2(t) for t in x)==9*r*r for x in S)
assert R2-F(697001,478676)==F(29843403742,277680785283)>0
assert R2<F(1062562,458329)
assert nread==60 and npairs==820

def enc(a):
    if isinstance(a,F): return str(a)
    if isinstance(a,(list,tuple)): return [enc(x) for x in a]
    if isinstance(a,dict): return {k:enc(v) for k,v in a.items()}
    return a

out=dict(status='PASS',model='S7-3 q=1 auxiliary tagged BRC epsilon=1',
         source_shapes=dict(b0=b0,b2=b2),r=r,unit_u=u,unit_v=v,
         source_states=S,common_exact_Q0=base,
         all_tagged_BRC_reference_readings=readings,
         common_noisy_reference_report=reports,reference_spreads=spreads,
         positive_contact_weights=weights,Chebyshev_center=center,
         exact_MEB_squared_radius=R2,
         previous_six_state_squared_radius=F(697001,478676),
         strict_improvement=R2-F(697001,478676),
         full_model_pair_lower_bound=F(1062562,458329),
         exact_Gram_checks=9,direct_tagged_BRC_masses=nread,
         ordered_tagged_path_pairs=npairs,
         native_X6_Detector_correspondence='NOT_ESTABLISHED',
         Source_admission='UNREVIEWED_NOT_ADMITTED_REGISTER_PENDING')
Path(__file__).with_name('RESULTS_PREFIX316.json').write_text(
    json.dumps(enc(out),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(enc({'status':'PASS','MEB_R2':R2,'BRC_masses':nread,'ordered_pairs':npairs})))
