"""External ternary IID N14 Stage217 author exact rational full-policy-tree certificate.

BRC usage: ordered positive integer P/Q path masses and provenance; count quotient
is confined to IID Bellman suffixes and independently audited via an unmerged DFS.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json

N = 14
PN, QN = (3, 1, 20), (2, 2, 20)
P, Q = tuple(F(v,24) for v in PN), tuple(F(v,24) for v in QN)
K = F(157464, 1631)
H = F(13979469720797262916799, 178694060004624826368)
AL = F(7504698785088745369, 21035720123168587776)
VL = F(4095371032631387677, 438244169232678912)
T, Z, ROOT = (13, 8, 4), (14, 0, 0), (0, 0, 0)
STATES = [(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]

def next_state(s,j): return s[0]+1, s[1]+int(j==0), s[2]+int(j==1)
def rho(s): return F(2**(s[1]+s[2]), 3**s[1])

@lru_cache(None)
def bell(s):
    vals = {'P': K*rho(s), 'Q':K}
    if s[0]<N: vals['C'] = 1+sum(P[j]*bell(next_state(s,j))[0] for j in range(3))
    lo = min(vals.values())
    return lo, tuple(a for a,v in vals.items() if v==lo), tuple(v-lo for v in vals.values() if v>lo)

assert len(STATES)==680 and bell(ROOT)[0]==H
TIES = {s:bell(s)[1] for s in STATES if len(bell(s)[1])>1}
assert TIES == {T:('P','C'), Z:('P','Q')}, TIES
GAPS = [g for s in STATES for g in bell(s)[2]]
assert len(GAPS)==1238 and min(GAPS)==F(294667,12682656) and all(g>0 for g in GAPS)

def choose(s,u,z):
    if s==T: return 'P' if u else 'C'
    if s==Z: return 'P' if z else 'Q'
    a=bell(s)[1]
    assert len(a)==1, (s,a)
    return a[0]

@lru_cache(None)
def suffix(s,u,z):
    a=choose(s,u,z)
    if a=='P': return (F(0),F(1),F(0),F(0))
    if a=='Q': return (F(1),F(0),F(0),F(0))
    ch=[suffix(next_state(s,j),u,z) for j in range(3)]
    return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*ch[j][k] for j in range(3)) for k in range(4))

def ordered(u,z):
    mass=[0,0,0,0]; visits=0; leaves=0
    def dfs(s,pm,qm):
        nonlocal visits,leaves
        visits+=1
        a=choose(s,u,z)
        if a=='C':
            assert s[0]<N
            for j in range(3): dfs(next_state(s,j), pm*PN[j],qm*QN[j])
        else:
            leaves+=1
            multiplier=24**(N-s[0]);n=s[0]
            mass[0]+=int(a=='Q')*pm*multiplier
            mass[1]+=int(a=='P')*qm*multiplier
            mass[2]+=n*pm*multiplier
            mass[3]+=n*qm*multiplier
    dfs(ROOT,1,1)
    return tuple(F(m,24**N) for m in mass),visits,leaves

def sub(x,y):return tuple(a-b for a,b in zip(x,y))
CORNER={};VISITS={};LEAVES={}
for u,z in product((0,1),repeat=2):
    obs,count,leaves=ordered(u,z)
    assert obs==suffix(ROOT,u,z),(u,z,obs,suffix(ROOT,u,z))
    CORNER[u,z]=obs
    VISITS[f'{u}{z}']=count
    LEAVES[f'{u}{z}']=leaves
O=CORNER[0,0]; DT=sub(CORNER[1,0],O);DZ=sub(CORNER[0,1],O)
M=sub(sub(CORNER[1,1],CORNER[1,0]),DZ)
assert M==(F(0),)*4,M
err=lambda x:x[0]-x[1]
assert err(DZ)!=0
z0=-err(O)/err(DZ)
zs=-err(DT)/err(DZ)
z1=z0+zs
assert 0<=z0<=1 and 0<=z1<=1,(z0,z1)

def balanced(u):
    z=z0+zs*u
    return tuple(O[i]+u*DT[i]+z*DZ[i] for i in range(4))
L,R=balanced(F(0)),balanced(F(1))
assert L[0]==L[1] and R[0]==R[1]
assert L[0]==AL and L[2]==VL,(L,AL,VL)
assert R[0]>L[0],(L,R)
assert L[2]>L[3] and R[2]>R[3]
assert L[2]+2*K*L[0]==H and R[2]+2*K*R[0]==H
assert R[2]-L[2]==-2*K*(R[0]-L[0])
CERT={
    'schema':'EM_STAGE217_AUTHOR_EXACT_V1',
    'classification':'PORTABLE_AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED',
    'model':{'N':N,'P_num':list(PN),'Q_num':list(QN),'den':24},
    'K217':str(K),'H217':str(H),'tie_actions':{str(s):list(a) for s,a in TIES.items()},
    'Bellman_states':len(STATES),'positive_alternative_gaps':len(GAPS),'minimum_gap':str(min(GAPS)),
    'corners':{f'{u}{z}':list(map(str,CORNER[u,z])) for u,z in product((0,1),repeat=2)},
    'O':list(map(str,O)),'DT':list(map(str,DT)),'DZ':list(map(str,DZ)),'mixed':list(map(str,M)),
    'ordered_visits':VISITS,'ordered_leaves':LEAVES,'total_visits':sum(VISITS.values()),
    'z0':str(z0),'zs':str(zs),'z1':str(z1),
    'alpha216':str(AL),'V216':str(VL),'alpha217':str(R[0]),'V217':str(R[2]),
    'width217':str(R[0]-AL),'slope217':str(2*K),
    'tP_minus_tQ_left':str(L[2]-L[3]),'tP_minus_tQ_right':str(R[2]-R[3]),
    'all_real_interval_from_affine_randomization':True,
}
Path(__file__).with_name('certificate217.json').write_text(json.dumps(CERT,indent=2)+'\n',encoding='utf-8')
print('STAGE217_AUTHOR_EXACT_FULL_REAL_PASS',sum(VISITS.values()))
for x in ('K217','H217','width217','slope217','z0','zs','z1','alpha217','V217','tP_minus_tQ_left','tP_minus_tQ_right','ordered_visits'):
    print(x,CERT[x])
