"""PREFIX-446 compact exact reproducer, q-sector path moment BRC."""
from fractions import Fraction as F
from math import comb, factorial

def obs(c,n,q,d):
    return tuple(sum((F(v)*(n-2*k)**j for k,v in c.items() if k%q==r),F())
                 for r in range(q) for j in range(d))+(sum((F(v)*(n-2*k)**d for k,v in c.items()),F()),)

def step(c,q,a,b):
    out={}
    for k,v in c.items():
        r=k%q
        out[k]=out.get(k,F())+v*a[r]
        out[k+1]=out.get(k+1,F())+v*b[r]
    return out

def witness(n,q,d):
    assert q>=2 and d>=1 and n>=q*d+1
    A={};B={}
    for r in (0,1):
        for j in range(d+1):
            k=r+q*j; z=(-1)**(r+j)*comb(d,j)
            (A if z>0 else B)[k]=abs(z)
    return A,B

def rank(rows):
    x=[[F(v) for v in row] for row in rows];i=0
    if not x:return 0
    for j in range(len(x[0])):
        p=next((r for r in range(i,len(x)) if x[r][j]),None)
        if p is None:continue
        x[i],x[p]=x[p],x[i]; pivot=x[i][j]
        x[i]=[v/pivot for v in x[i]]
        for r in range(i+1,len(x)):
            z=x[r][j]
            if z:x[r]=[v-z*w for v,w in zip(x[r],x[i])]
        i+=1
        if i==len(x):break
    return i

def rows(columns):
    return list(zip(*columns))

def main():
    ranks=closures=witnesses=0
    for q in (2,3,4):
        for d in (1,2,3):
            for n in range(q*d+q+4):
                h=[len(range(r,n+1,q)) for r in range(q)]
                active=[r for r in range(q) if h[r]>=d+1]
                M=rows([obs({k:F(1)},n,q,d) for k in range(n+1)])
                assert rank(M)==sum(min(z,d) for z in h)+bool(active)
                ranks+=1
                for mode in (0,1,2):
                    a=tuple(F(2+r,3+r) for r in range(q))
                    b=[F(5,4)-v for v in a]
                    if mode==1:b[0]+=F(1,7)
                    if mode==2:b[-1]+=F(1,7)
                    out=rows([obs(step({k:F(1)},q,a,b),n+1,q,d) for k in range(n+1)])
                    assert (rank(M+out)==rank(M))==(len({a[r]+b[r] for r in active})<=1)
                    closures+=1
            for n in range(q*d+1,q*d+6):
                A,B=witness(n,q,d)
                assert sum(A.values())==sum(B.values())==2**d
                assert all(v<=comb(n,k) for C in (A,B) for k,v in C.items())
                assert obs(A,n,q,d)==obs(B,n,q,d)
                v0=sum((w*(n-2*k)**d for k,w in A.items() if k%q==0))-sum((w*(n-2*k)**d for k,w in B.items() if k%q==0))
                assert v0==(2*q)**d*factorial(d)
                witnesses+=1
    a=(F(2,3),F(1,2),F(4,5));b=(F(3,5),F(1,3),F(7,10));A,B=witness(7,3,2)
    assert obs(step(A,3,a,b),8,3,2)[-1]-obs(step(B,3,a,b),8,3,2)[-1]==F(156,5)
    print('PASS: rank',ranks,'one-step closure',closures,'unit path witnesses',witnesses,'q3-example 156/5')

if __name__=='__main__':main()
