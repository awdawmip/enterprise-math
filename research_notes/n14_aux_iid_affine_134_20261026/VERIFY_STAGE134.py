"""N14 Stage134 portable exact author-side Bellman/primal checker.
Only the external iid model. Requires Python stdlib Fraction.
No native CLAIM, formal review or automated remote execution inferred.
"""
from fractions import Fraction as R
from functools import cache
from itertools import product
N=14
P=(R(1,8),R(1,24),R(5,6))
K=R(48012912,81457); L=R(45307624,81457)
B=(11,0,1); G=(9,3,3); ROOT=(0,0,0)
def kids(s):
    n,a,b=s
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
ratio=lambda s:R(2**(s[1]+s[2]),3**s[1])
h={};choices={};positive=[]
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b)
            offers={'P':K*ratio(s),'Q':L}
            if n<N:
                offers['C']=1+sum(P[j]*h[t] for j,t in enumerate(kids(s)))
            best=min(offers.values())
            h[s]=best
            choices[s]=tuple(action for action,v in offers.items() if v==best)
            positive.extend(v-best for v in offers.values() if v>best)
assert len(h)==680 and len(positive)==1238
assert min(positive)==R(129758627,4504246272)
assert {s:v for s,v in choices.items() if len(v)>1}=={B:('Q','C'),G:('Q','C')}
assert h[ROOT]==R(2442656918158809916870213,5949675882197721022464)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,t):return tuple(x*t for x in a)
declP=(R(0),R(1),R(0),R(0))
declQ=(R(1),R(0),R(0),R(0))
@cache
def m(s,w,z):
    def cont():
        ch=[m(t,w,z) for t in kids(s)]
        return (
            sum(P[j]*v[0] for j,v in enumerate(ch)),
            sum((R(1,12),R(1,12),R(5,6))[j]*v[1] for j,v in enumerate(ch)),
            1+sum(P[j]*v[2] for j,v in enumerate(ch)),
            1+sum((R(1,12),R(1,12),R(5,6))[j]*v[3] for j,v in enumerate(ch)))
    if s==B:return add(mul(declQ,w),mul(cont(),1-w))
    if s==G:return add(mul(declQ,z),mul(cont(),1-z))
    action=choices[s][0]
    return declP if action=='P' else declQ if action=='Q' else cont()
corners={(w,z):m(ROOT,R(w),R(z)) for w,z in product((0,1),repeat=2)}
base=corners[0,0];dB=sub(corners[1,0],base);dG=sub(corners[0,1],base)
assert corners[1,1]==add(add(base,dB),dG)
err=lambda v:v[0]-v[1]
w0=-err(base)/err(dB); slope=-err(dG)/err(dB)
assert w0==R(29148450914061437,81438720000000000)
assert slope==-R(4650723,19280000000)
assert 0<w0+slope<w0<1
path=lambda z:add(add(base,mul(dB,w0+slope*z)),mul(dG,z))
s,e=path(R(0)),path(R(1))
assert s[0]==s[1] and e[0]==e[1]
assert s[0]==R(36703010861169506695,105616844785075617792)
assert s[2]==R(656403116242184147227,52808422392537808896)
assert e[0]==R(36703016772992738695,105616844785075617792)
assert e[2]==R(656399729826573779227,52808422392537808896)
assert e[0]-s[0]==R(71274875,1273351234387968)
assert (s[2]-e[2])/(e[0]-s[0])==K+L==R(93320536,81457)
for v in (s,e):
    assert v[2]>v[3]
    assert v[2]+L*v[0]+K*v[1]==h[ROOT]
assert s[2]-s[3]==R(88899829683689096807,158425267177613426688)
assert e[2]-e[3]==R(88912023540183944807,158425267177613426688)
print("PASS: author exact N14 Stage134 Bellman and full-real primal interval")
print("states",len(h),"strict gaps",len(positive),"min gap",min(positive))
print("M00",base,"dB",dB,"dG",dG)
print("w0",w0,"w_slope",slope,"end",e)
