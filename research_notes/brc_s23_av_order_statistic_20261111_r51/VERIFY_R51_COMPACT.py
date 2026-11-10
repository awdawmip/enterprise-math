"""R51 self-contained exact source-rank oracle; stdlib only.
Auxiliary irrational rotation; finite rational enclosure certified by Stern-Brocot.
"""
from math import isqrt
from bisect import bisect_right

def fs(n,m,a,b):
    v=0
    while True:
        if a>=m:v+=(n-1)*n*(a//m)//2;a%=m
        if b>=m:v+=n*(b//m);b%=m
        y=a*n+b
        if y<m:return v
        n,b=divmod(y,m);m,a=a,m

def sb(K,a,d):
    p,i,q,j=0,1,1,1
    while i+j<=K:
        u=i*a-p*d;v=q*d-j*a
        if u>v:
            z=min(u//v,(K-i-j)//j+1);p,i=p+z*q,i+z*j
        else:
            z=min(v//u,(K-i-j)//i+1);q,j=q+z*p,j+z*i
    assert q*i-p*j==1 and i+j>K
    return i*a-p*d,q*d-j*a

def top(K,L,U,D,r):
    a=L+U;d=2*D
    u,v=sb(K,a,d)
    assert min(u,v)>K*(U-L),(u,v,K)
    def cnt(n,t):return fs(n,d,a,a+t)-fs(n,d,a,a)
    left,right=1,d
    while left<right:
        mid=(left+right)//2
        if cnt(K,mid)>=r:right=mid
        else:left=mid+1
    t=left
    assert cnt(K,t)==r and cnt(K,t-1)==r-1
    left,right=1,K
    while left<right:
        mid=(left+right)//2
        if cnt(mid,t)>cnt(mid,t-1):right=mid
        else:left=mid+1
    s=left
    assert d-(s*a%d)==t
    return s

def age(m,H,s,L,D):
    cuts=sorted((z*L%D,z) for z in range(m))
    phases=[v for v,z in cuts];out=[None]*m
    for r in range(1,H+1):
        z=cuts[bisect_right(phases,(s-r)*L%D)-1][1]
        if out[z] is None:out[z]=r
    return tuple(out)

def test(name,m,H,lo,hi,D,k):
    K=m+H-1;s=[];ages=[]
    for r in range(1,k+1):
        j=top(K,lo,hi,D,r);s.append(j)
        ages.append(age(m,H,j,lo,D))
    assert s==sorted(range(1,K+1),key=lambda z:z*lo%D,reverse=True)[:k]
    assert ages==[age(m,H,j,hi,D) for j in s]
    print('PASS',name,'K',K,'top',s,'equal-prefix',next((r-1 for r in range(2,k+1) if ages[r-1]!=ages[0]),k))

if __name__=='__main__':
    q=10**32;s=isqrt(2*q*q);assert s*s<2*q*q<(s+1)**2
    test('S23',128,225,262204504569236716045286,262204504569236716045287,10**24,5)
    test('sqrt2',5,8,s-q,s+1-q,q,7)
    test('sqrt2-m16',16,25,s-q,s+1-q,q,6)
    test('sqrt2-m23',23,31,s-q,s+1-q,q,6)
