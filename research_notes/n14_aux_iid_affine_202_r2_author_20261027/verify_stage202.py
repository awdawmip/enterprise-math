"""Stage202 external N14 IID exact primal checker; author-side, no source claim.

All arithmetic is fractions.Fraction or integer positive P/Q path masses.
Bellman compresses only IID suffix states. Independent DFS retains every ordered prefix.
"""
from fractions import Fraction as F
from functools import cache
from itertools import product
from pathlib import Path
import json

N=14
P=(F(3,24),F(1,24),F(20,24))
Q=(F(2,24),F(2,24),F(20,24))
K=F(94363551,741293)
H_EXPECT=F(18568821153724089963922211,185638477110285856407552)
B=(6,0,1) # Q versus continue
Z=(14,0,0) # report P versus Q
S=(0,0,0)
ALPHA201=F(3705289910272792345,10517860061584293888)
V201=F(2265238509513884573,219122084616339456)
STATES=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
assert len(STATES)==680

def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
def ratio(s):return F(2**(s[1]+s[2]),3**s[1])
@cache
def bell(s):
    costs={'P':K*ratio(s), 'Q':K}
    if s[0]<N:
        costs['C']=1+sum(P[i]*bell(child(s,i))[0] for i in range(3))
    v=min(costs.values())
    return v,tuple(a for a,c in costs.items() if c==v),tuple(c-v for c in costs.values() if c>v)
assert bell(S)[0]==H_EXPECT,(bell(S)[0],H_EXPECT)
ties={s:bell(s)[1] for s in STATES if len(bell(s)[1])>1}
assert ties=={B:('Q','C'),Z:('P','Q')},ties
gaps=[d for s in STATES for d in bell(s)[2]]
assert len(gaps)==1238 and min(gaps)==F(16319029,1441073592),(len(gaps),min(gaps))

def action(s,b,z):
    if s==B:return 'Q' if b else 'C'
    if s==Z:return 'P' if z else 'Q'
    return bell(s)[1][0]
@cache
def dp(s,b,z):
    a=action(s,b,z)
    if a=='P':return (F(0),F(1),F(0),F(0))
    if a=='Q':return (F(1),F(0),F(0),F(0))
    c=[dp(child(s,i),b,z) for i in range(3)]
    return tuple(sum((P if j%2==0 else Q)[i]*c[i][j] for i in range(3))+int(j>=2) for j in range(4))

def integer_dfs(b,z):
    total=[0]*4;calls=0;arrivals=[0,0,0]
    def visit(s,p,q,visited_b=False):
        nonlocal calls
        calls+=1;n=s[0]
        if s==B:arrivals[0]+=1;visited_b=True
        if s==Z:arrivals[1]+=1;arrivals[2]+=visited_b
        a=action(s,b,z)
        if a=='C':
            for i in range(3):
                visit(child(s,i),p*(3,1,20)[i],q*(2,2,20)[i],visited_b)
        else:
            m=24**(N-n)
            if a=='P':total[1]+=q*m
            if a=='Q':total[0]+=p*m
            total[2]+=n*p*m
            total[3]+=n*q*m
    visit(S,1,1)
    return tuple(F(t,24**N) for t in total),calls,arrivals

corners={};counts={};arrivals={}
for b,z in product((0,1),repeat=2):
    key=f'{b}{z}'
    corners[key]=dp(S,b,z)
    x,n,ar=integer_dfs(b,z)
    assert x==corners[key],(key,x,corners[key])
    counts[key]=n;arrivals[key]=ar
O=corners['00'];DB=tuple(corners['10'][i]-O[i] for i in range(4))
DZ=tuple(corners['01'][i]-O[i] for i in range(4))
M=tuple(corners['11'][i]-corners['10'][i]-corners['01'][i]+O[i] for i in range(4))
assert M==(F(0),)*4,M
assert all(a[2]==0 for a in arrivals.values()),arrivals
err=lambda x:x[0]-x[1]
z0=-err(O)/err(DZ)
zs=-err(DB)/err(DZ)
assert err(DZ)!=0

def balanced(b):
    z=z0+zs*b
    return tuple(O[i]+DB[i]*b+DZ[i]*z for i in range(4))
left,right=balanced(F(0)),balanced(F(1))
print('coins',z0,zs,z0+zs)
print('left error and Ptime',left[0],left[2]);print('right error and Ptime',right[0],right[2])
print('time diff',left[2]-left[3],right[2]-right[3]);print('errors derivative',right[0]-left[0])
print('arrivals',arrivals,'counts',counts)
assert 0<=z0<=1 and 0<=z0+zs<=1,(z0,zs)
assert left[0]==left[1] and right[0]==right[1]
# endpoint order established from exact signs, not assumed
assert (left[0]==ALPHA201 and left[2]==V201) or (right[0]==ALPHA201 and right[2]==V201),('contact',left,right)
assert left[2]>left[3] and right[2]>right[3]
assert all(x[2]+K*(x[0]+x[1])==H_EXPECT for x in (left,right))
fmt=lambda x:str(x)
fmtr=lambda x:[fmt(v) for v in x]
cert={
 'schema':'EM_STAGE202_EXACT_PRIMAL_CERTIFICATE_V1',
 'status':'PORTABLE_AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED',
 'source':{'Global_Knowledge_V1':'main@f4ef844a208d4774467436397c4ee4b0481b7ba6','Enterprise_Math':'main@d8b1a8272420500b67ddc04033ca9577f7c1f3f8','scientific_parent_PR_1571':'feb4b102a0d8796cb47723baf6024cb640314c4d'},
 'model':{'N':N,'P':fmtr(P),'Q':fmtr(Q),'observables':['P(report Q)','Q(report P)','E_P(T)','E_Q(T)']},
 'dual':{'K':fmt(K),'L':fmt(K),'H':fmt(H_EXPECT),'states':len(STATES),'positive_gaps':len(gaps),'minimum_positive_gap':fmt(min(gaps)),'ties':{str(s):list(v) for s,v in ties.items()}},
 'corners':{k:fmtr(v) for k,v in corners.items()},
 'affine':{'O00':fmtr(O),'DB':fmtr(DB),'DZ':fmtr(DZ),'mixed':fmtr(M)},
 'coins':{'z0':fmt(z0),'zs':fmt(zs),'z1':fmt(z0+zs)},
 'endpoints':{'b0':{'alpha':fmt(left[0]),'V':fmt(left[2]),'P_minus_Q_time':fmt(left[2]-left[3])},'b1':{'alpha':fmt(right[0]),'V':fmt(right[2]),'P_minus_Q_time':fmt(right[2]-right[3])},'stage201_alpha':fmt(ALPHA201),'stage201_V':fmt(V201)},
 'ordered_dfs':{'calls':counts,'total':sum(counts.values()),'arrivals_B_Z_intersection':arrivals},
 'checks':['bellman_680_exact','positive_gaps_1238','full_integer_ordered_dfs_4corners','zero_mixed_structural_nonancestor','all_real_balanced_coin','strict_P_time_dominance','stage201_exact_contact','dual_equalities'],
 'scope':'finite ternary IID observer only; not P000 native physical theorem or formal review'
}
Path('/mnt/data/em_stage202/certificate202.json').write_text(json.dumps(cert,indent=2)+'\n')
print('STAGE202_AUTHOR_EXACT_PASS',sum(counts.values()))
