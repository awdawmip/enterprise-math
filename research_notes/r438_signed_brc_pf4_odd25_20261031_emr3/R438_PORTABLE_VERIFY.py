"""R438 r23 signed-BRC exact complementary verifier.

The separate R438_PF4_R23_FAST.cpp is the complete certified 4th-order
enumerator. This Python file uses ONLY integer arithmetic for raw coefficients,
complete 1st-3rd order minors, PF5 witness, and independent 4th-order spots.
"""
from math import comb, gcd
from functools import reduce
from itertools import permutations

R=25
N=23

def signed_coefficient(r,s):
    if s<2 or s>r:return 0
    z=0
    for j in range(r-s+1):
        m=r-2*j
        if 0<=m<=2*s:z+=comb(r-s,j)*comb(2*s,m)
        m-=1
        if 0<=m<=2*s:z-=comb(r-s,j)*comb(2*s,m)
    return comb(r+s,2*s)*z

def polynomial_coefficient(r,s):
    if s<2 or s>r:return 0
    p=[1]
    for degree,repeats in ((1,2*s),(2,r-s)):
        for _ in range(repeats):
            q=[0]*(len(p)+degree)
            for k,x in enumerate(p):
                q[k]+=x
                q[k+degree]+=x
            p=q
    return comb(r+s,2*s)*(p[r]-p[r-1])

raw=[signed_coefficient(R,R-h) for h in range(R-1)]
g=reduce(gcd,raw)
a=[n//g for n in raw]
assert g==12 and all(x>0 for x in a) and max(a)<2**64
assert raw==[polynomial_coefficient(R,R-h) for h in range(R-1)]

def odd_catalan_coeff(r,s):
    k=(r-1)//2
    C=lambda n:comb(2*n,n)//(n+1)
    return comb(r+s,2*s)*sum((comb(s-1,2*t) if 2*t<=s-1 else 0)*4**t*C(k-t) for t in range(k+1))
assert raw==[odd_catalan_coeff(R,R-h) for h in range(R-1)]

def val(h):return a[h] if 0<=h<=N else 0

def det3(u,v):
    a,b,c=[val(t) for t in v]
    d,e,f=[val(t-u[1]) for t in v]
    g,h,i=[val(t-u[2]) for t in v]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def bareiss(M):
    M=[row[:] for row in M]
    n=len(M);den=1
    for k in range(n-1):
        x=M[k][k]
        if not x:
            j=next((j for j in range(k+1,n) if M[j][k]),None)
            if j is None:return 0
            M[k],M[j]=M[j],M[k]
            den=-den
            x=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q=x*M[i][j]-M[i][k]*M[k][j]
                assert q%den==0
                M[i][j]=q//den
            M[i][k]=0
        den=x
    return M[-1][-1]

lower={1:{"positive":len(a),"zero":0,"negative":0}}
q={"positive":0,"zero":0,"negative":0}
for u1 in range(1,N+1):
    for v0 in range(N+1):
        for v1 in range(max(v0+1,u1),u1+N+1):
            d=val(v0)*val(v1-u1)-val(v1)*val(v0-u1)
            q["positive" if d>0 else "negative" if d<0 else "zero"]+=1
lower[2]=q
q={"positive":0,"zero":0,"negative":0}
for u1 in range(1,N+1):
    for u2 in range(u1+1,u1+N+1):
        for v0 in range(N+1):
            for v1 in range(max(v0+1,u1),u1+N+1):
                for v2 in range(max(v1+1,u2),u2+N+1):
                    d=det3((0,u1,u2),(v0,v1,v2))
                    q["positive" if d>0 else "negative" if d<0 else "zero"]+=1
lower[3]=q
assert lower[2]=={"positive":10948,"zero":0,"negative":0}
assert lower[3]=={"positive":4839476,"zero":0,"negative":0}

m5=[[signed_coefficient(R,R-(c-u)) for c in range(22,27)] for u in range(5)]
E=bareiss(m5)
assert E==-811734564107657248002278461009278028997592967065600000
independent=0
for p in permutations(range(5)):
    z=(-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
    for i,j in enumerate(p):z*=m5[i][j]
    independent+=z
assert independent==E

spots=0
for u1 in (1,2,3,5,8,13,23):
 for u2 in (u1+1,u1+2,u1+6,u1+23):
  for u3 in (u2+1,u2+2,u2+23):
   u=(0,u1,u2,u3)
   for v0 in (0,1,5,11,23):
    for t1 in (0,1,3,7,23):
     v1=max(v0+1,u1)+t1
     if v1>u1+N:continue
     for t2 in (0,1,3,7,23):
      v2=max(v1+1,u2)+t2
      if v2>u2+N:continue
      for t3 in (0,1,3,7,23):
       v3=max(v2+1,u3)+t3
       if v3>u3+N:continue
       v=(v0,v1,v2,v3)
       assert bareiss([[val(c-r) for c in v] for r in u])>0
       spots+=1
assert spots==30989
print("R438_EXACT_PASS",lower,"spot4",spots,"negative_E25",E)
