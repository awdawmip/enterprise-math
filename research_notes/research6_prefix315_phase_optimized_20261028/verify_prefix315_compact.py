#!/usr/bin/env python3
"""PREFIX315 exact, tagged, complete 6-state BRC witness (Python stdlib)."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

def g(a=0,b=0):return (F(a),F(b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cj(z):return (z[0],-z[1])
def scale(z,s):return (z[0]*s,z[1]*s)
def subtract(a,b):return add(a,scale(b,-1))
def norm2(z):return mul(z,cj(z))[0]
def smul(a,z):return tuple(mul(x,z) for x in a)
def ssub(a,b):return tuple(subtract(x,y) for x,y in zip(a,b))
def d2(a,b):return sum(norm2(x) for x in ssub(a,b))
def inner(a,b):return sum(mul(x,cj(y))[0] for x,y in zip(a,b))
O=g(); ONE=g(1); I=g(0,1)
A=((g(4),g(4),O),(O,g(-4),g(4)),(g(-5,3),O,g(-3,1)),
   (g(-2,-2),g(4,4),g(2,2)),(g(-2),O,g(5,2)))
U=tuple(tuple(scale(z,F(1,8)) for z in row) for row in A)
b0=(g(-2),g(0,-2),g(1));b2=(g(0,2),g(2),g(0,-1))
w=g(F(5,11),F(1,22));v=g(F(60,61),F(-11,61));n=g(F(11,61),F(60,61))
S=tuple(smul(x,w) for x in (b0,smul(b0,I),b2,smul(b2,I),smul(b0,v),smul(b2,n)))
assert len(set(S))==6 and norm2(v)==norm2(n)==1
count=0; pairs=0

def mass(row,a,rho=None):
    global count,pairs
    p=[(f'source:{k+1}',mul(U[row][k],a[k])) for k in range(3)]
    if rho is not None:p.append(('reference',rho))
    assert len({tag for tag,_ in p})==len(p)
    result=O
    for ta,za in p:
        for tb,zb in p:
            result=add(result,mul(za,cj(zb)));pairs+=1
    assert result[1]==0 and result[0]>=0
    count+=1
    return result[0]

q0=tuple(mass(j,S[0]) for j in range(5))
assert q0==(F(101,242),F(505,1936),F(3737,15488),F(2525,3872),F(8585,30976))
for a in S[1:]:assert tuple(mass(j,a) for j in range(5))==q0
reports={}; values={}; widths={}
for label,rho in [('Q1',ONE),('Qi',I)]:
    vv=[]; rr=[]; ww=[]
    for j in range(5):
        x=tuple(mass(j,a,rho) for a in S)
        lo,hi=min(x),max(x)
        assert hi-lo<=2
        y=(lo+hi)/2
        assert all(abs(z-y)<=1 for z in x)
        vv.append(x); rr.append(y); ww.append(hi-lo)
    reports[label]=tuple(rr);values[label]=tuple(vv);widths[label]=tuple(ww)
assert reports=={
 'Q1':(F(343,242),F(2045,1936),F(22041,15488),F(8773,3872),F(3087301,1889536)),
 'Qi':(F(343,242),F(149297,118096),F(19225,15488),F(538497,236192),F(39561,30976))}
# Exact Gram and optimal four-contact Chebyshev certificate.
for k in range(3):
    for l in range(3):
        z=O
        for row in U:z=add(z,mul(cj(row[k]),row[l]))
        assert z==(g((F(31,32),F(1),F(63,64))[k]) if k==l else O)
weights=(F(3539,11868),F(250,989),F(195,989),F(2989,11868))
support=(1,2,3,4)
h=(g(F(-400,989),F(-40,989)),g(F(5050,10879)),g(F(200,989),F(20,989)))
assert all(sum(weights[t]*S[support[t]][k][u] for t in range(4))==h[k][u]
           for k in range(3) for u in range(2))
r=F(697001,478676)
radii=tuple(d2(a,h) for a in S)
assert all(radii[t]==r for t in support)
assert all(x<=r for x in radii)
assert radii[0]<r and radii[5]<r
# Affine rank of positive contacts: independent 3 contact differences.
d=[ssub(S[i],S[1]) for i in (2,3,4)]
G=[[inner(x,y) for y in d] for x in d]
det=(G[0][0]*(G[1][1]*G[2][2]-G[1][2]*G[2][1])
     -G[0][1]*(G[1][0]*G[2][2]-G[1][2]*G[2][0])
     +G[0][2]*(G[1][0]*G[2][1]-G[1][1]*G[2][0]))
assert det==F(183414184020,6591978481)>0
assert F(976,729)<F(6161,4356)<r<F(1062562,458329)
assert count==90 and pairs==1230

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,tuple):return [enc(y) for y in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x
result={'result':'PASS','source_states':S,'common_Q0':q0,'common_Q1_Qi':reports,
        'all_BRC_readings':values,'Q1_Qi_spreads':widths,'MEB_support':support,
        'MEB_positive_weights':weights,'MEB_centre':h,'MEB_r2':r,
        'all_six_radii2':radii,'affine_gram_det':det,
        'direct_BRC_masses':count,'ordered_tagged_path_pairs':pairs,
        'full_model_pair_lower_bound_L':'1062562/458329',
        'native_X6_Detector_attribution':'NOT_ESTABLISHED',
        'formal_Source_Result':'UNREVIEWED_NOT_ADMITTED'}
Path(__file__).with_name('RESULTS_PREFIX315_COMPACT.json').write_text(
    json.dumps(enc(result),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(enc({'result':'PASS','R2':r,'six_states':len(S),'masses':count,
                      'ordered_pairs':pairs,'det':det})))
