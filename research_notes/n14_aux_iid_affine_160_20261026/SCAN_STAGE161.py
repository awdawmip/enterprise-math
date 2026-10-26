"""Stage161 author dual-only exact ray scan, not a primal theorem."""
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6));N=14
K=F(2521611,8218);L=F(1229640,4109)
dK=F(-1);dL=-F(25280,14751)
@lru_cache(None)
def affine(n,a,b):
    ratio=F(2**(a+b),3**a)
    v={'P':(K*ratio,dK*ratio),'Q':(L,dL)}
    if n<N:
        c=[affine(*st)[0] for st in ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))]
        v['C']=(1+sum(P[i]*c[i][0] for i in range(3)),sum(P[i]*c[i][1] for i in range(3)))
    m=min(z[0] for z in v.values())
    slope=min(z[1] for z in v.values() if z[0]==m)
    return (m,slope),tuple(a for a,z in v.items() if z==(m,slope)),v
states=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
cross=[]; ties=[]
for st in states:
    (v,s),chosen,acts=affine(*st)
    if len(chosen)>1:ties.append((st,chosen))
    for act,(a,b) in acts.items():
        assert a>=v and (a!=v or b>=s)
        if a>v and b<s:cross.append(((a-v)/(s-b),st,act))
assert ties==[((10,2,0),('P','C'))]
assert affine(13,5,2)[1]==('C',)
t,st,act=min(cross)
assert t==F(16778244681,4559354618) and st==(10,0,1) and act=='Q'
k=K+t*dK;l=L+t*dL
assert k==F(168193485,554801) and l==F(162528200,554801)
@lru_cache(None)
def check(n,a,b):
    v={'P':k*F(2**(a+b),3**a),'Q':l}
    if n<N:
        v['C']=1+sum(P[i]*check(*[(n+1,a+1,b),(n+1,a,b+1),(n+1,a,b)][i])[0] for i in range(3))
    m=min(v.values());return m,tuple(z for z in v if v[z]==m),[x-m for x in v.values() if x>m]
gaps=[x for st in states for x in check(*st)[2]]
assert len(gaps)==1238 and min(gaps)==F(1055356088281,238554274922496)
assert {st:check(*st)[1] for st in states if len(check(*st)[1])>1}=={
 (10,2,0):('P','C'),(10,0,1):('Q','C')}
print('STAGE161_DUAL_ONLY_PASS',t,k,l, 'gaps=',len(gaps),'min=',min(gaps))
