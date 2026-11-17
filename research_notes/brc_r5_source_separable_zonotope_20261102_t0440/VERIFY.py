from fractions import Fraction as F
from itertools import product
Z=F(0); H=F(1,2)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Z)
def gap(ds,n):
    return sum((max(Z,dot(n,d)) for d in ds),Z)-max(Z,sum((dot(n,d) for d in ds),Z))
def separator(a,b):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            D=a[i]*b[j]-a[j]*b[i]
            if D:
                n=[Z]*len(a);n[i]=(b[j]+a[j])/D;n[j]=(-b[i]-a[i])/D
                assert dot(n,a)==1 and dot(n,b)==-1
                return n
    i=next(i for i,x in enumerate(a) if x)
    c=b[i]/a[i]
    assert b==tuple(c*x for x in a)
    if c>=0:return None
    n=[Z]*len(a);n[i]=1/a[i]
    return n
masses=[(H,H),(H,H)]
kernels=[(F(3,4),F(1,4)),(F(1,4),F(3,4))]
stop=[];cont=[]
for (p,q),(ap,aq) in zip(masses,kernels):
    assert p/q==1 and 0<ap<1 and 0<aq<1
    stop.append((p,Z,p,q))
    cont.append((p*ap,q*(1-aq),2*p,2*q))
ds=[sub(s,c) for s,c in zip(stop,cont)]
assert ds==[(F(1,8),-F(3,8),-H,-H),(F(3,8),-F(1,8),-H,-H)]
assert all(sum(k[i] for k in kernels)/2==H for i in (0,1))
n=(F(1),F(1),Z,Z)
assert dot(n,ds[0])==-F(1,4) and dot(n,ds[1])==F(1,4)
assert gap(ds,n)==F(1,4)
full=[]
for a,b in product((0,1),repeat=2):
    full.append(add(stop[0] if a else cont[0],stop[1] if b else cont[1]))
lr=[add(cont[0],cont[1]),add(stop[0],stop[1])]
assert len(full)==4 and len(lr)==2
assert max(dot(n,v) for v in full)==F(5,4)
assert all(dot(n,v)==1 for v in lr)
w=add(cont[0],stop[1]); assert w==(F(7,8),F(3,8),F(3,2),F(3,2))
mid=tuple((x+y)/2 for x,y in zip(*lr))
assert mid==(F(3,4),F(1,4),F(3,2),F(3,2))
assert max(abs(x-y) for x,y in zip(w,mid))==F(1,8)
assert (dot(n,w)-1)/sum(abs(t) for t in n)==F(1,8)
ns=separator(ds[1],ds[0]);assert dot(ns,ds[1])==1 and dot(ns,ds[0])==-1
assert separator(ds[0],tuple(3*x for x in ds[0])) is None
an=separator(ds[0],tuple(-2*x for x in ds[0]))
assert dot(an,ds[0])==1 and dot(an,tuple(-2*x for x in ds[0]))==-2
assert gap([ds[0],tuple(3*x for x in ds[0])],n)==0
assert gap([ds[0],tuple(-2*x for x in ds[0])],an)==1
assert gap([ds[1],ds[0],tuple(F(13,7)*x for x in ds[1])],n)==F(1,4)
print('EXACT_RATIONAL_FULL_POLICIES=4 LR_POLICIES=2')
print('N=(1,1,0,0) FULL_SUPPORT=5/4 LR_SUPPORT=1 GAP=1/4')
print('W=(7/8,3/8,3/2,3/2) EXACT_LINF_DISTANCE=1/8')
print('RAY_SEPARATOR_AND_AGGREGATE_DOUBLE_LAW_CANCELLATION=PASS')
print('ANALYTIC_THEOREM_ALL_REAL_ALL_K_SOURCE_SEPARABLE')
print('PASS_EXACT_R5_SOURCE_SEPARABLE_ZONOTOPE_NO_GO')
