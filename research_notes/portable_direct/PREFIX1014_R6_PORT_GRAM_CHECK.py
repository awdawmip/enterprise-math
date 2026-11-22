"""PREFIX-1014: signed X6 BRC Link Gram orbit certificate, exact integers."""
from collections import defaultdict
from functools import lru_cache
from math import comb

ZERO=(0,)*6
unit=lambda j,s=1:tuple(s if i==j else 0 for i in range(6))
mon=lambda j,s=1:{unit(j,s):1}
ONE={ZERO:1}
S={unit(i):1 for i in range(6)}
U={unit(i,-1):1 for i in range(6)}
def mul(a,b):
    c=defaultdict(int)
    for x,v in a.items():
        for y,w in b.items():c[tuple(i+j for i,j in zip(x,y))]+=v*w
    return {x:v for x,v in c.items() if v}
def add(*polys):
    c=defaultdict(int)
    for p in polys:
        for x,v in p.items():c[x]+=v
    return {x:v for x,v in c.items() if v}
def scale(a,v):return {x:y*v for x,y in a.items() if y*v}
SU=mul(S,U)
def short_packet(n,j,positive):
    if positive:
        common=add(scale(mul(S,mon(0,-1)),-6),scale(mul(S,mon(j,-1)),-6))
        an=add(scale(SU,n-1),scale(ONE,-36*(n-3)),common)
        am=add(scale(SU,n-2),scale(ONE,-36*(n-4)),common)
        return mul(mon(j),add(mul(S,an),scale(mul(mon(0),am),-1),scale(mon(0),25)))
    return mul(mon(j,-1),mul(S,mul(add(S,scale(mon(j),-6)),add(S,scale(mon(0),-1)))))
def signature(delta):return tuple(sorted(abs(x) for x in delta))
def aggregate(p):
    c=defaultdict(int);representatives={}
    for a,v in p.items():
        for b,w in p.items():
            d=tuple(x-y for x,y in zip(a,b))
            assert sum(d)==0
            k=signature(d);c[k]+=v*w;representatives[k]=d
    return c,representatives
@lru_cache(None)
def collision(m,delta):
    t=[int(r+delta[0]>=0) for r in range(m+1)]
    total=delta[0]
    for d in delta[1:]:
        total+=d;new=[]
        for r in range(m+1):
            q=r+total
            new.append(0 if q<0 else sum(comb(r,a)*comb(q,a+d)*t[r-a]
                for a in range(max(0,-d),min(r,q-d)+1)))
        t=new
    assert total==0
    return t[m]
def class_value(n,j,positive):
    co,reps=aggregate(short_packet(n,j,positive))
    return sum(v*collision(n-4,reps[k]) for k,v in co.items())
def direct(n):
    directions=[unit(i) for i in range(6)]+[unit(i,-1) for i in range(6)]
    v={(ZERO,unit(0,-1),0):1}
    for _ in range(n):
        w=defaultdict(int)
        for (x,h,k),a in v.items():
            for i,d in enumerate(directions):
                q=k+(i>=6)
                if q>1:continue
                y=tuple(t+u for t,u in zip(x,d))
                if (x==ZERO and y==unit(0)) or (x==unit(0) and y==ZERO):continue
                w[y,tuple(-t for t in d),q]+=a*(1-6*(h==d))
        v={key:a for key,a in w.items() if a}
    return [[sum(a*a for (x,h,k),a in v.items() if k==1 and h==unit(j,-s))
            for j in range(6)] for s in (1,-1)]
if __name__=='__main__':
    signatures=set()
    for kind in (True,False):
        for j in (0,1):signatures.update(aggregate(short_packet(5,j,kind))[0])
    assert len(signatures)==11
    for n in range(5,9):
        p,q=direct(n)
        assert p==[class_value(n,0,True)]+[class_value(n,1,True)]*5
        assert q==[class_value(n,0,False)]+[class_value(n,1,False)]*5
        print('BRC-CHECK',n,p[0],p[1],q[0],q[1])
    for n in (10,12,16,20,30):
        print('ORBIT',n,*[class_value(n,j,kind) for kind in (True,False) for j in (0,1)])
    print('PASS: eleven shared signatures; four orbit classes; exact BRC through n=8')
