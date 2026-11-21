"""Exact R5 primitive-23/25 phase vectors, genuine intersecting load constraints.
Python 3 + numpy; int64 arithmetic with proven bound < 2**63 for m <= 100.
"""
import numpy as np

S=({214,215,216,217,218},{214,216,217,218,219,220,221},
   {215,216,217,218,219,220,221})

def roll(v,n):return np.roll(v,n%len(v))
def mul(a,b):
    z=np.zeros(len(a),dtype=np.int64)
    for k,v in enumerate(a):
        if v:z+=v*roll(b,k)
    return z

def geom(d,p,n):
    v=np.zeros(d,dtype=np.int64)
    for i in range(n+1):v[(i*p)%d]+=1
    return v

def homogeneous(d,prices,M):
    h=np.zeros((M+1,d),dtype=np.int64);h[0,0]=1
    for p in prices:
        for n in range(1,M+1):h[n]+=roll(h[n-1],p)
    return h

def factor(d,prices):
    z=np.zeros(d,dtype=np.int64);z[0]=1
    for p in sorted(prices):z-=roll(z,p)
    return z

def vectors(d,T):
    M=2*T;a,b=214,215
    J=homogeneous(d,[219,220,221],M)
    U=np.cumsum(homogeneous(d,[216,217,218],M),axis=0)
    Jsum=np.cumsum(J,axis=0)
    B={i:np.zeros((M+1,d),dtype=np.int64) for i in range(1,8)}
    for n in range(M+1):
        for x in range(n+1):B[1][n,(a*x+b*(n-x))%d]+=1
        B[2][n]=J[n]+(roll(B[2][n-1],a) if n else 0)
        B[4][n]=J[n]+(roll(B[4][n-1],b) if n else 0)
        for mask,outer,inner in [(3,a,b),(5,b,a)]:
            v=roll(Jsum[n],inner*n)
            if n:v+=mul(J[n],geom(d,inner,n-1))
            B[mask][n]=v+(roll(B[mask][n-1],outer) if n else 0)
        for j in range(n+1):
            r=n-j
            w=roll(geom(d,b,r),a*r)
            if r:w+=roll(geom(d,a,r-1),b*r)
            B[6][n]+=mul(w,J[j])
            w=np.zeros(d,dtype=np.int64)
            y=n-j
            for x in range(min(j,y)+1):w[(a*x+b*y)%d]+=1
            x=n-j
            for y in range(min(j,x-1)+1):w[(a*x+b*y)%d]+=1
            if n>=2*j+2:
                for x in range(j+1,n-j):w[(a*x+b*(n-x))%d]+=1
            B[7][n]+=mul(w,J[j])
    signed=np.zeros((M+1,d),dtype=np.int64)
    for mask in range(1,8):
        selected=[S[i] for i in range(3) if mask>>i&1]
        c=factor(d,set.union(*selected))
        sgn=1 if mask.bit_count()%2 else -1
        for n in range(M+1):signed[n]+=sgn*mul(c,B[mask][n])
    result=[]
    for m in range(1,M+1):
        v=np.zeros(d,dtype=np.int64)
        for n in range(m):v+=mul(signed[n],U[m-1-n])
        result.append(v)
    return result

def normal(v,d):
    if d==23:return [int(v[j]-v[22]) for j in range(22)]
    return [int(v[j]-v[(j%5)+20]) for j in range(20)]

if __name__=='__main__':
    for d,T,zeros in [(23,46,[42,43,44,45,46]),(25,50,[46,47,48,49,50])]:
        vals=vectors(d,T)
        assert all(np.array_equal(vals[i],vals[i+T]) for i in range(T))
        assert [i+1 for i in range(T) if not any(normal(vals[i],d))]==zeros
        if d==23:assert [int(vals[0][j]) for j in (0,1)]==[1,6]
        else:assert [int(vals[0][j]) for j in (0,5)]==[4,-3]
        print('PASS',d,'period',T,'nonzero',T-5,'zeros',zeros)
