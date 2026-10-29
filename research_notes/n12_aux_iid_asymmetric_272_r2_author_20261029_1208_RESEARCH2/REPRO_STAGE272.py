#!/usr/bin/env python3
"""Stage272 exact rational Bellman/ordered-history certificate, no external dependencies."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6)); N=12
Z=[(i,j,n-i-j) for n in range(13) for i in range(n+1) for j in range(n-i+1)]
T=(0,0,5); U=(1,2,3); S=(1,2,4); S2=(1,2,5); root=(0,0,0)
A=F(2401128349757,31701690482688); D=F(288133328335,371504185344)
L0=(F(7566375964672,51849608449),F(4026978326268,51849608449))

def nxt(s,k):
    a=list(s);a[k]+=1;return tuple(a)
def mass(s):
    i,j,k=s;return P[0]**i*P[1]**j*P[2]**k,Q[0]**i*Q[1]**j*Q[2]**k
def dp(lp,lq):
    v={};cs={};ties={};gap=[]
    for s in Z[::-1]:
        p,q=mass(s);c={'P':lq*q,'Q':lp*p}
        if sum(s)<N:c['C']=q+sum(v[nxt(s,k)] for k in range(3))
        best=min(c.values());v[s]=best;cs[s]=c
        eq=tuple(k for k in c if c[k]==best)
        if len(eq)>1:ties[s]=eq
        gap += [x-best for x in c.values() if x>best]
    return v,cs,ties,gap
def flow(pol):
    counts=defaultdict(int);counts[root]=1;o=[F(0)]*4;end=[F(0)]*2
    for s in Z:
        m=counts[s]
        if not m:continue
        p,q=mass(s);a=pol[s]
        if a=='P':o[1]+=m*q
        if a=='Q':o[0]+=m*p
        if a=='C':
            assert sum(s)<N
            o[2]+=m*p;o[3]+=m*q
            for k in range(3):counts[nxt(s,k)]+=m
        else:end[0]+=m*p;end[1]+=m*q
    assert end==[1,1]
    return tuple(o),counts
def ordered(pol):
    o=[F(0)]*4;end=[F(0)]*2;nodes=leaves=0
    def go(w,p,q):
        nonlocal nodes,leaves
        nodes+=1;s=tuple(w.count(k) for k in range(3));a=pol[s]
        if a=='P':o[1]+=q
        if a=='Q':o[0]+=p
        if a=='C':
            assert len(w)<N
            o[2]+=p;o[3]+=q
            for k in range(3):go(w+(k,),p*P[k],q*Q[k])
        else:end[0]+=p;end[1]+=q;leaves+=1
    go((),F(1),F(1));assert end==[1,1]
    return tuple(o),nodes,leaves
def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

old,ca,ot,_=dp(*L0)
assert ot=={U:('Q','C'),T:('P','C')}
bas={s:next(k for k in ca[s] if ca[s][k]==old[s]) for s in Z}
assert bas[S]=='Q';bas[U]='C'
pol={};obs={};nall=lall=0
for r,u in product((0,1),repeat=2):
    pol[r,u]=bas.copy();pol[r,u][T]='C' if r else 'P';pol[r,u][S]='C' if u else 'Q'
    obs[r,u],cnt=flow(pol[r,u]);direct,n,l=ordered(pol[r,u]);assert direct==obs[r,u]
    assert (cnt[T],cnt[S])==(1,35) and obs[r,u][3]>obs[r,u][2]
    nall+=n;lall+=l
G,H,Gp,Hp=(obs[0,0],obs[1,0],obs[0,1],obs[1,1])
dT=tuple(H[i]-G[i] for i in range(4));dS=tuple(Gp[i]-G[i] for i in range(4))
assert tuple(Hp[i]-H[i] for i in range(4))==dS
assert tuple(Hp[i]-Gp[i] for i in range(4))==dT
det=dT[0]*dS[1]-dT[1]*dS[0];assert det!=0
lp=(dS[3]*dT[1]-dT[3]*dS[1])/det
lq=(dT[3]*dS[0]-dT[0]*dS[3])/det
assert (lp,lq)==(F(7694718574592,50961738459),F(1351613187036,16987246153))
v,cs,ties,gap=dp(lp,lq);h=v[root]
assert h==F(1945350813734366428859,24651691575422902272)
assert ties=={T:('P','C'),S:('Q','C')} and len(Z)==455
assert sum(len(x) for x in cs.values())==1274 and len(gap)==817
assert min(gap)==F(110379031,934938228638261182464)
for key in pol:
    assert all(cs[s][pol[key][s]]==v[s] for s in Z)
    assert lp*obs[key][0]+lq*obs[key][1]+obs[key][3]==h
oldE=(F(1133161305691,15850845241344),F(146231594105,185752092672))
assert abs(det)==F(1161237529990234375,276030719456218208796672)
assert orient(G,H,oldE)>0 and det<0 and T[2]>S[2] and sum(T)<sum(S)
r=((A-G[0])*dS[1]-(D-G[1])*dS[0])/det
u=(dT[0]*(D-G[1])-dT[1]*(A-G[0]))/det
assert (r,u)==(F(49,100),F(1,50))
w=tuple(G[i]+r*dT[i]+u*dS[i] for i in range(4))
assert w[:2]==(A,D) and w[3]>w[2]
assert w[2]==F(6452413254061,1320903770112)
assert w[3]==h-lp*A-lq*D==F(535594465735,92876046336)
assert nall==27304 and lall==18204
# Stage273 strictly exterior feasible policy and independent ordered-word check.
pk=pol[0,1].copy();assert pk[S2]=='Q' and flow(pk)[1][S2]==55
pk[S2]='C';k,_=flow(pk);kd,kn,kl=ordered(pk);assert k==kd
assert (kn,kl)==(8953,5969)
assert k==tuple(map(F,('557277756283/7925422620672','4579991515/5804752896',
  '13841471030731/2972033482752','64078877045/11609505792')))
x=tuple(F(49,100)*Gp[i]+F(49,100)*Hp[i]+F(1,50)*k[i] for i in range(4))
assert x==tuple(map(F,('298591185079/3962711310336','48058313785/61917364224',
  '807441417617/165112971264','89462343935/15479341056')))
assert orient(Gp,Hp,x)==F(-14900090626953125,138015359728109104398336)<0
assert orient(Gp,Hp,G)>0 and x[3]>x[2]
assert lp*k[0]+lq*k[1]+k[3]-h==F(267636139496515625,197213532603383218176)
print('STAGE272_EXACT_ALL_REAL_FACE_PASS')
print('dual',lp,lq,h,'ties',ties,'states',len(Z),'actions',sum(len(x) for x in cs.values()),
  'positive_gaps',len(gap),'minimum_gap',min(gap))
print('R272 area',abs(det),'old_side',orient(G,H,oldE),'new_side',det)
for label,key in [('G',(0,0)),('Hcorner',(1,0)),('Gplus',(0,1)),('Hplus',(1,1))]:
    print(label,','.join(map(str,obs[key])))
print('witness',','.join(map(str,w)),'r,u',r,u,'V',w[3],'delta_t',w[3]-w[2])
print('ordered_nodes',nall,'ordered_leaves',lall,'sources_P_Q_mass_one',True)
print('STAGE273_FEASIBLE_EXTERIOR_PASS','K',','.join(map(str,k)),'mix',','.join(map(str,x)),
  'next_nodes_leaves',kn,kl)
