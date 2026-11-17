#!/usr/bin/env python3
"""PREFIX-879: exact representative witnesses for all signed sparse gaps and eight lines."""
Q=(1<<19)-1
P=32
rep={}
for i in range(1,22):
    rep.setdefault(1<<i,(i,-1,0))
for i in range(2,22):
    for j in range(1,i):
        rep.setdefault((1<<i)+(1<<j),(i,j,1))
        rep.setdefault((1<<i)-(1<<j),(i,j,-1))
assert len(rep)==402

def witness(a,b):
    if a<b:
        x,y=witness(b,a)
        return ((x[1],x[0]),(y[1],y[0]))
    d=a-b
    i,j,t=rep[d]
    if j<0:
        x=(0,1<<i)
        y=(a,a)
    else:
        low=1<<(j+1)
        target=(1<<j) if t==1 else 0
        u=(target-a)%low
        x=(u,u+(1<<i))
        y=(u+a,u+a-t*(1<<j))
    assert x[0]>=0 and y[0]>=0
    return x,y

n=0
for k in (5,7,9,11):
    for delta in sorted(rep):
        for sign in (-1,1):
            d=sign*delta
            for orientation in (0,1):
                if orientation==0:
                    start=max(1,(d+1+k-1)//k)
                    finish=min(Q,(Q+d)//k)
                else:
                    start=max(1,(1-d+k-1)//k)
                    finish=min(Q,(Q-d)//k)
                start+=start%2==0
                if start>finish:
                    continue
                t=start
                x,y=(t,k*t-d) if orientation==0 else (k*t+d,t)
                a,b=(k*x,y) if orientation==0 else (x,k*y)
                v0,v1=witness(a,b)
                assert v0!=v1
                assert all(0<=z<(1<<P) for row in (v0,v1) for z in row)
                for u,v in (v0,v1):
                    z=u^v
                    assert z==0 or (z&(z-1))==0
                assert v0[0]%x==v1[0]%x and v0[1]%y==v1[1]%y
                n+=1
assert n==5648
print('ALL_EXACT_XOR_WITNESSES_PASSED',n)
print('example_5_1',witness(85,93))
