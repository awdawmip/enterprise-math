#!/usr/bin/env python3
"""Stage172 external N14 ternary IID exact author verification.
Separate suffix dynamic programming and full ordered history DFS; fractions throughout.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json

N=14
P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12), F(1,12), F(5,6))
K=F(2453276570264541,10128738563455)
L=F(7332367848199016,30386215690365)
R=(10,0,1)
Y=(5,4,1)
A=('P','Q','C')
EXPECTED={R:('Q','C'),Y:('P','C')}
def fmt(x): return str(x.numerator) + ('/'+str(x.denominator) if x.denominator!=1 else '')
def ell(s): return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i): return(s[0]+1, s[1]+(i==0), s[2]+(i==1))

@lru_cache(None)
def bell(s):
    options=[K*ell(s), L]
    if s[0]<N:
        options.append(1+sum((P[i]*bell(child(s,i))[0] for i in range(3)),F(0)))
    m=min(options)
    return m,tuple(a for a,x in zip(A,options) if x==m),options

strict={};ties={};gaps=[]
for n in range(N+1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);m,w,options=bell(s)
            if len(w)>1:ties[s]=w
            else:strict[s]=w[0]
            gaps.extend(x-m for x in options if x>m)
assert ties==EXPECTED,(ties,EXPECTED)
assert len(strict)+len(ties)==680
assert len(gaps)==1238,(len(gaps),min(gaps))
assert min(gaps)==F(3442966771823,273475941213285)
H=bell((0,0,0))[0]
assert H==F(7500321462434479703133415412645,41614318285465632307238928384)

def action(s,r,y):
    if s==R:return 'Q' if r else 'C'
    if s==Y:return 'P' if y else 'C'
    return strict[s]

def suffix(r,y):
    @lru_cache(None)
    def rec(s):
        ac=action(s,r,y)
        if ac=='P':return(F(0),F(1),F(0),F(0))
        if ac=='Q':return(F(1),F(0),F(0),F(0))
        v=[rec(child(s,i)) for i in range(3)]
        return(sum((P[i]*v[i][0] for i in range(3)),F(0)),
               sum((Q[i]*v[i][1] for i in range(3)),F(0)),
               1+sum((P[i]*v[i][2] for i in range(3)),F(0)),
               1+sum((Q[i]*v[i][3] for i in range(3)),F(0)))
    return rec((0,0,0))

def ordered_dfs(r,y):
    pn=(3,1,20);qn=(1,1,10)
    acc=defaultdict(int);hits={R:[0,F(0),F(0)],Y:[0,F(0),F(0)]}; nodes=0
    def walk(n,a,b,p,q):
        nonlocal nodes
        nodes+=1;s=(n,a,b)
        if s in hits:
            h=hits[s];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
        ac=action(s,r,y)
        if ac=='C':
            assert n<N
            for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*pn[i],q*qn[i])
        else:
            acc[n,'ap']+=p;acc[n,'aq']+=q;acc[n,'tp']+=n*p;acc[n,'tq']+=n*q
            if ac=='P':acc[n,'eq']+=q
            else:acc[n,'ep']+=p
    walk(0,0,0,1,1)
    mass=lambda tag,den:sum((F(acc[n,tag],den**n) for n in range(N+1)),F(0))
    assert mass('ap',24)==mass('aq',12)==1
    return (mass('ep',24),mass('eq',12),mass('tp',24),mass('tq',12)),hits,nodes

corners={};nodes={};hits0=None
for r in (0,1):
    for y in (0,1):
        v=suffix(r,y);w,h,n=ordered_dfs(r,y)
        assert v==w,(r,y,v,w)
        corners[r,y]=v;nodes[f'{r}{y}']=n
        if hits0 is None:hits0=h
        else:assert hits0==h,(hits0,h)
assert hits0[R][0]>0 and hits0[Y][0]>0
# Y has four zero-symbol observations by depth 5, while R has zero by depth 10.
# The first-hit sets are disjoint even with later control/stop actions.
assert Y[1]>R[1] and R[1]==0 and Y[0]<R[0]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
base=corners[0,0];dR=sub(corners[1,0],base);dY=sub(corners[0,1],base)
mixed=sub(sub(corners[1,1],corners[1,0]),dY)
assert mixed==(F(0),)*4
D=lambda v:v[0]-v[1]
D0,Dr,Dy=map(D,(base,dR,dY));assert Dr
r0=-D0/Dr;rs=-Dy/Dr
vec=lambda y:tuple(base[i]+(r0+rs*y)*dR[i]+y*dY[i] for i in range(4))
legal=(F(0),F(1))
if rs>0:legal=(max(legal[0],-r0/rs),min(legal[1],(1-r0)/rs))
elif rs<0:legal=(max(legal[0],(1-r0)/rs),min(legal[1],-r0/rs))
y0,y1=legal
left,right=vec(y0),vec(y1)
alpha171=F(882435274780741015735,2530093150022563528704)
V171=F(4191188444229937372757,361441878574651932672)
r171=F(8992237821259453,11823616000000000)
checks={
    'r171_match':r0==r171,
    'alpha171_match':left[0]==left[1]==alpha171,
    'V171_match':left[2]==V171,
    'legal_start_zero':y0==0,
    'legal_end_one':y1==1,
    'r_in_unit':0<=r0<=1 and 0<=r0+rs<=1,
    'balanced_both_endpoints':left[0]==left[1] and right[0]==right[1],
    'timeP_dominates':left[2]>=left[3] and right[2]>=right[3],
    'dual_tightness':all(v[2]+K*v[1]+L*v[0]==H for v in (left,right)),
    'alpha_increases':right[0]>left[0],
    'timeP_decreases':right[2]<left[2],
    'support_slope':right[2]-left[2]==-(K+L)*(right[0]-left[0]),
    'positive_duals':K>0 and L>0,
    'first_hit_disjoint':mixed==(F(0),)*4,
}
for k,v in checks.items():print(k,v)
print('BALANCE','r(y)=',fmt(r0),'+',fmt(rs),'*y; legal',fmt(y0),fmt(y1))
print('BOUNDARY left',(fmt(left[0]),fmt(left[2]),fmt(left[2]-left[3])))
print('BOUNDARY right',(fmt(right[0]),fmt(right[2]),fmt(right[2]-right[3])))
print('WIDTH',fmt(right[0]-left[0]),'SLOPE',fmt(K+L))
print('H',fmt(H),'HITS',{str(k):list(map(fmt,v)) for k,v in hits0.items()},'NODES',nodes)
print('BASE',list(map(fmt,base)),'dR',list(map(fmt,dR)),'dY',list(map(fmt,dY)))
cert={'status':'STAGE172_AUTHOR_EXACT_NOT_NATIVE_CLAIMED',
 'model':{'N':N,'P':list(map(fmt,P)),'Q':list(map(fmt,Q)),'scope':'EXTERNAL_TERNARY_IID_FULL_ORDERED_HISTORIES'},
 'sources':{'stage171_author_commit':'53826073e9b493695cf20f014ead19088fd4d0d6','stage171_dual':'dual172.json','global_snapshot':'656cd167e44f250e1e900e5c903ad96beb8315a5','em_scientific_snapshot':'f990313d69b823ce51e583a26d01d5f7dc08d1d1'},
 'dual':{'K':fmt(K),'L':fmt(L),'sum':fmt(K+L),'H':fmt(H),'states':680,'ties':{str(k):list(v) for k,v in ties.items()},'positive_gaps':len(gaps),'min_gap':fmt(min(gaps))},
 'corners':{f'{r}{y}':list(map(fmt,m)) for (r,y),m in corners.items()},
 'base':list(map(fmt,base)),'dR':list(map(fmt,dR)),'dY':list(map(fmt,dY)),
 'mixed':[fmt(m) for m in mixed],
 'first_hit':{str(s):{'ordered_paths':h[0],'P':fmt(h[1]),'Q':fmt(h[2])}for s,h in hits0.items()},
 'ordered_dfs_nodes':nodes,
 'balance':{'D0':fmt(D0),'Dr':fmt(Dr),'Dy':fmt(Dy),'r0':fmt(r0),'rs':fmt(rs),'y0':fmt(y0),'y1':fmt(y1),'r1':fmt(r0+rs)},
 'left':{'alpha':fmt(left[0]),'V':fmt(left[2]),'tP_minus_tQ':fmt(left[2]-left[3])},
 'right':{'alpha':fmt(right[0]),'V':fmt(right[2]),'tP_minus_tQ':fmt(right[2]-right[3])},
 'width':fmt(right[0]-left[0]),'slope':fmt(K+L),'checks':checks}
Path(__file__).with_name('certificate172.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
assert all(checks.values()),'Stage172 certificate has failed a property: inspect output'
print('STAGE172_AUTHOR_EXACT_FULL_REAL_PASS')
