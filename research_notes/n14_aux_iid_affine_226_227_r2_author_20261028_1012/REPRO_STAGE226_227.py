#!/usr/bin/env python3
"""Exact external N14 IID author reproduction, not native P000 evidence."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

PN=(3,1,20);QN=(2,2,20);P=tuple(F(x,24) for x in PN);Q=tuple(F(x,24) for x in QN)
S=(0,0,0);Z=(14,0,0)
states=tuple((n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1))
assert len(states)==680
nxt=lambda s,j:(s[0]+1,s[1]+(j==0),s[2]+(j==1))
rows={
226:((5,3,1),F(22581264879576,259377559703),F(7932877273030669030641345071,111006546064102353706942464),F(312728966121555653,876488338465357824),F(511537461689062799,54780521154084864),F(469096691401829767,1314732507698036736),F(255756969769073287,27390260577042432),22636),
227:((4,3,1),F(45953726534712,538227241171),F(493933159371125439911699,7029621308010268532736),F(469096691401829767,1314732507698036736),F(255756969769073287,27390260577042432),F(938194997485383047,2629465015396073472),F(511508195322329735,54780521154084864),20128),
}
def check(i,row):
    T,K,H,al,vl,ar,vr,expected=row
    @lru_cache(None)
    def B(s):
        n,a,b=s
        opts={'P':K*F(2**(a+b),3**a),'Q':K}
        if n<14:opts['C']=1+sum(P[j]*B(nxt(s,j))[0] for j in range(3))
        val=min(opts.values())
        return val,tuple(k for k,v in opts.items() if v==val),opts
    assert B(S)[0]==H
    assert {s:B(s)[1] for s in states if len(B(s)[1])>1}=={T:('P','C'),Z:('P','Q')}
    gaps=[v-B(s)[0] for s in states for v in B(s)[2].values() if v>B(s)[0]]
    assert len(gaps)==1238 and min(gaps)>0
    def act(s,u,z):
        if s==T:return 'P' if u else 'C'
        if s==Z:return 'P' if z else 'Q'
        a=B(s)[1];assert len(a)==1
        return a[0]
    @lru_cache(None)
    def dp(s,u,z):
        choice=act(s,u,z)
        if choice!='C':return (F(0),F(1),F(0),F(0)) if choice=='P' else (F(1),F(0),F(0),F(0))
        children=[dp(nxt(s,j),u,z) for j in range(3)]
        return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*children[j][k] for j in range(3)) for k in range(4))
    def dfs(u,z):
        stack=[(0,0,0,1,1)];tot=[0]*4;vis=0
        while stack:
            n,a,b,p,q=stack.pop();vis+=1
            c=act((n,a,b),u,z)
            if c=='C':
                for j in range(3):stack.append((n+1,a+(j==0),b+(j==1),p*PN[j],q*QN[j]))
            else:
                w=24**(14-n)
                if c=='P':tot[1]+=q*w
                else:tot[0]+=p*w
                tot[2]+=n*p*w;tot[3]+=n*q*w
        return tuple(F(v,24**14) for v in tot),vis
    obs={};vis=0
    for u,z in product((0,1),repeat=2):
        x=dp(S,u,z);y,n=dfs(u,z);assert x==y
        obs[u,z]=x;vis+=n
    sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    o=obs[0,0];du=sub(obs[1,0],o);dz=sub(obs[0,1],o)
    assert sub(sub(obs[1,1],obs[1,0]),dz)==(F(0),)*4
    assert T[1]>Z[1] and Z[0]==14
    z0=-(o[0]-o[1])/(dz[0]-dz[1]);zs=-(du[0]-du[1])/(dz[0]-dz[1])
    assert 0<=z0<=1 and 0<=z0+zs<=1
    r=lambda u:tuple(o[j]+u*du[j]+(z0+zs*u)*dz[j] for j in range(4))
    l,h=r(F(0)),r(F(1))
    assert l[0]==l[1]==al and h[0]==h[1]==ar and ar>al
    assert l[2]==vl and h[2]==vr and l[2]>l[3] and h[2]>h[3]
    assert vl+2*K*al==vr+2*K*ar==H and vis==expected
    print(f'STAGE{i}_COMBINED_REPRO_PASS',vis,'z0',z0,'zs',zs,'delta',ar-al)
for i,row in rows.items():check(i,row)
assert rows[226][5]==rows[227][3] and rows[226][6]==rows[227][4]
assert rows[227][2]==rows[226][2]+2*rows[226][5]*(rows[227][1]-rows[226][1])
K228=F(22177458672696,263038955731)
H228=F(238775201049969851829137,3435471315090760605696)
@lru_cache(None)
def dual228(s):
    n,a,b=s
    opts={'P':K228*F(2**(a+b),3**a),'Q':K228}
    if n<14:opts['C']=1+sum(P[j]*dual228(nxt(s,j))[0] for j in range(3))
    v=min(opts.values())
    return v,tuple(k for k,x in opts.items() if x==v)
assert dual228(S)[0]==H228
assert {s:dual228(s)[1] for s in states if len(dual228(s)[1])>1}=={(4,2,2):('Q','C'),Z:('P','Q')}
assert H228==rows[227][2]+2*rows[227][5]*(K228-rows[227][1])
print('STAGE228_DUAL_ONLY_PASS',K228)
