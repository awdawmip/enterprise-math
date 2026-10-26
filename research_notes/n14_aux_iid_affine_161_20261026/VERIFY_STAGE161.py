#!/usr/bin/env python3
"""Stage161 external finite-horizon ternary iid author checker.
Exact fractions, independent conditional suffix and literal unmerged ordered DFS.
No P000/X6/native Driver status is asserted.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json
from pathlib import Path

N = 14
P = (F(1,8), F(1,24), F(5,6))
Q = (F(1,12), F(1,12), F(5,6))
K, L = F(168193485,554801), F(162528200,554801)
J, R = (10,2,0), (10,0,1)
TIES = {J: ('P','C'), R: ('Q','C')}
ACTS = 'PQC'

def rat(x): return [x.numerator,x.denominator]
def fmt(x): return str(x.numerator) + ('/'+str(x.denominator) if x.denominator!=1 else '')
def ratio(s): return F(2)**(s[1]+s[2]) / F(3)**s[1]
def child(s, x): return s[0]+1, s[1]+(x==0), s[2]+(x==1)

@lru_cache(None)
def val(s):
    options=[K*ratio(s),L]
    if s[0]<N:
        options.append(1+sum(P[x]*val(child(s,x))[0] for x in range(3)))
    return min(options),tuple(options)

strict={};ties={};gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=n,a,b; low,cands=val(s); opts=tuple(ACTS[x] for x,v in enumerate(cands) if v==low)
            if len(opts)>1: ties[s]=opts
            else: strict[s]=opts[0]
            gaps.extend(v-low for v in cands if v>low)
assert len(strict)+len(ties)==680
assert ties==TIES,("unexpected tie set",ties)
assert len(gaps)==1238 and min(gaps)==F(1055356088281,238554274922496)

def action(s,j,rcoin):
    if s==J: return 'P' if j else 'C'
    if s==R: return 'Q' if rcoin else 'C'
    return strict[s]

def suffix(j,rcoin):
    @lru_cache(None)
    def out(state):
        x=action(state,j,rcoin)
        if x=='P': return (F(0),F(1),F(0),F(0))
        if x=='Q': return (F(1),F(0),F(0),F(0))
        xs=[out(child(state,k)) for k in range(3)]
        return (sum(P[k]*xs[k][0] for k in range(3)),
                sum(Q[k]*xs[k][1] for k in range(3)),
                1+sum(P[k]*xs[k][2] for k in range(3)),
                1+sum(Q[k]*xs[k][3] for k in range(3)))
    return out((0,0,0))

def ordered_dfs(j,rcoin):
    pn=(3,1,20);qn=(1,1,10)
    counts=defaultdict(int)
    hits={J:[0,F(0),F(0)],R:[0,F(0),F(0)]}
    count=0
    def visit(n,a,b,p,q):
        nonlocal count
        count+=1;state=n,a,b
        if state in hits:
            hits[state][0]+=1
            hits[state][1]+=F(p,24**n)
            hits[state][2]+=F(q,12**n)
        selected=action(state,j,rcoin)
        if selected!='C':
            counts[n,'allp']+=p;counts[n,'allq']+=q
            counts[n,'tp']+=n*p;counts[n,'tq']+=n*q
            if selected=='P':counts[n,'eq']+=q
            else:counts[n,'ep']+=p
            return
        for x in range(3):visit(n+1,a+(x==0),b+(x==1),p*pn[x],q*qn[x])
    visit(0,0,0,1,1)
    def tot(tag,base):return sum((F(counts[n,tag],base**n) for n in range(N+1)),F(0))
    assert tot('allp',24)==tot('allq',12)==1
    return (tot('ep',24),tot('eq',12),tot('tp',24),tot('tq',12)),hits,count

corners={};counts={};reference=None
for j in (0,1):
    for rcoin in (0,1):
        m0=suffix(j,rcoin)
        m1,first,nodes=ordered_dfs(j,rcoin)
        assert m0==m1,(j,rcoin,m0,m1)
        corners[j,rcoin]=m0;counts[f'{j}{rcoin}']=nodes
        if reference is None:reference=first
        else:assert first==reference

def sub(u,v):return tuple(x-y for x,y in zip(u,v))
base=corners[0,0]
dJ=sub(corners[1,0],base)
dR=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),sub(corners[0,1],base))
assert mixed==(0,0,0,0)

# Equal errors: eP-eQ = D0 + DJ*j + DR*rcoin
err_diff=lambda vec: vec[0]-vec[1]
D0,DJ,DR=err_diff(base),err_diff(dJ),err_diff(dR)
print('base',*[fmt(x) for x in base],sep='\n')
print('dJ',*[fmt(x) for x in dJ],sep='\n')
print('dR',*[fmt(x) for x in dR],sep='\n')
print('error coeff',*[fmt(x) for x in (D0,DJ,DR)],sep='\n')
print('first hits', {str(k):[x[0],fmt(x[1]),fmt(x[2])] for k,x in reference.items()})
print('nodes',counts)
print('Bellman Hroot',fmt(val((0,0,0))[0]),'positive gaps',len(gaps),'min',fmt(min(gaps)))

# two possible coordinate compensation forms
j0,jSlope= -D0/DJ, -DR/DJ
r0,rSlope= -D0/DR, -DJ/DR
print('j(r)=',fmt(j0),'+',fmt(jSlope),'r')
print('r(j)=',fmt(r0),'+',fmt(rSlope),'j')
print('j(0),j(1)',fmt(j0),fmt(j0+jSlope))
print('r(0),r(1)',fmt(r0),fmt(r0+rSlope))

def at_j(j):return tuple(base[k]+j*dJ[k]+(r0+rSlope*j)*dR[k] for k in range(4))
def at_r(rcoin):return tuple(base[k]+(j0+jSlope*rcoin)*dJ[k]+rcoin*dR[k] for k in range(4))

for name,vec in [('right_j=1',at_j(F(1))),('left_r=0',at_r(F(0)))]:
    print(name,' / '.join(fmt(x) for x in vec),'dual',fmt(vec[2]+K*vec[1]+L*vec[0]), 'time gap',fmt(vec[2]-vec[3]))

ALPHA160=F(381586508350717329445,1096459521159585595392)
V160=F(13167218152253362815857,1096459521159585595392)
print('alpha160',fmt(ALPHA160),'V160',fmt(V160))

# Exact primal interval assertions, inherited left endpoint and new sharp right endpoint.
assert reference[J]==[45,F(1953125,11943936),F(1953125,26873856)]
assert reference[R]==[10,F(9765625,120932352),F(9765625,60466176)]
assert j0==F(107743801834549,461157120000000)
assert jSlope==F(923720,360279)
rmax=(F(1)-j0)/jSlope
assert rmax==F(353413318165451,1182361600000000)
assert F(0)<rmax<F(1) and F(0)<j0<F(1)
left=at_r(F(0)); right=at_r(rmax)
ALPHA161=F(440625016346358918245,1265046575011281764352)
V161=F(2138967403739208846181,180720939287325966336)
ETA161=F(4901851558287759506275,16880359814758873436258304)
assert left[0]==left[1]==ALPHA160 and left[2]==V160
assert right[0]==right[1]==ALPHA161 and right[2]==V161
assert right[0]-left[0]==ETA161 and K+L==F(330721685,554801)
assert right[2]-left[2]==-(K+L)*ETA161
for v in (left,right):
    assert v[2]>v[3]
    assert v[2]+K*v[1]+L*v[0]==val((0,0,0))[0]
assert left[2]-left[3]==F(505710367439141258645,1096459521159585595392)
assert right[2]-right[3]==F(526231060559760430495,1265046575011281764352)
print('PASS Stage161: full-real exact interval, dual equality, legal coins, sharp-right witness')
print('alpha161',fmt(ALPHA161),'V161',fmt(V161),'eta161',fmt(ETA161),'rmax',fmt(rmax))

# Structured provenance/certificate for further independent verification.
CERT={'status':'AUTHOR_EXACT_COMPUTATION_ASSISTED','model':{'N':N,'P':['1/8','1/24','5/6'],'Q':['1/12','1/12','5/6']},
      'dual':{'K':fmt(K),'L':fmt(L),'Hroot':fmt(val((0,0,0))[0]),'states':680,
              'ties':{str(x):list(y) for x,y in ties.items()},'positive_gaps':len(gaps),'min_gap':fmt(min(gaps))},
      'first_hits':{str(k):{'count':v[0],'Pmass':fmt(v[1]),'Qmass':fmt(v[2])} for k,v in reference.items()},
      'ordered_dfs_nodes':counts,'corners':{f'{j}{r}':[fmt(x) for x in corners[j,r]] for j,r in corners},
      'M00':[fmt(x) for x in base],'dJ':[fmt(x) for x in dJ],'dR':[fmt(x) for x in dR],
      'mixed':[fmt(x) for x in mixed],
      'compensation':{'j_at_r0':fmt(j0),'j_slope':fmt(jSlope),'rmax':fmt(rmax)},
      'left':{'alpha':fmt(ALPHA160),'V':fmt(V160),'time_gap':fmt(left[2]-left[3])},
      'right':{'alpha':fmt(ALPHA161),'V':fmt(V161),'time_gap':fmt(right[2]-right[3])},
      'width':fmt(ETA161),'slope':fmt(K+L)}
with open(Path(__file__).with_name('certificate161.json'),'w') as f: json.dump(CERT,f,indent=2,ensure_ascii=False)
