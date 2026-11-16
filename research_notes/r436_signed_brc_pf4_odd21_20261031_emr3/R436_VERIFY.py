"""R436: integer verification of original signed BRC r=21, lower-order minors,
exact fifth-order witness, independent fourth-order checks.
Complete fourth-order enumeration is in R436_PF4_R21_FAST.cpp.
"""
from math import comb, gcd
from functools import reduce
from itertools import permutations
import json

R,N=21,19
def H(r,s):
    if s<2 or s>r:return 0
    q=0
    for j in range(r-s+1):
        m=r-2*j
        if 0<=m<=2*s:q+=comb(r-s,j)*comb(2*s,m)
        m-=1
        if 0<=m<=2*s:q-=comb(r-s,j)*comb(2*s,m)
    return comb(r+s,2*s)*q
def H_poly(r,s):
    if s<2 or s>r:return 0
    p=[1]
    for step,repeat in ((1,2*s),(2,r-s)):
        for _ in range(repeat):
            q=[0]*(len(p)+step)
            for i,x in enumerate(p):q[i]+=x;q[i+step]+=x
            p=q
    return comb(r+s,2*s)*((p[r] if r<len(p) else 0)-(p[r-1] if r-1<len(p) else 0))
raw=[H(R,R-h) for h in range(R-1)]
G=reduce(gcd,raw);A=[x//G for x in raw]
assert G==92 and max(A)<2**44 and all(x>0 for x in A)
assert raw==[H_poly(R,R-h) for h in range(R-1)]
assert [H(19,19-h)//2 for h in range(18)]==[883631595,15021737115,118215578250,570420017475,1885199008440,4516469666280,8099050221360,11069635101525,11635491988575,9424350050115,5858143180890,2766367523205,975765719500,250607657300,45153996888,5398847454,394777383,14549535]
def a(h):return A[h] if 0<=h<=N else 0
def det3(u,v):
    b,c,d=(a(j) for j in v)
    e,f,g=(a(j-u[1]) for j in v)
    h,i,k=(a(j-u[2]) for j in v)
    return b*(f*k-g*i)-c*(e*k-g*h)+d*(e*i-f*h)
def det(m):
    n=len(m);D=0
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n):sign*=m[i][p[i]]
        D+=sign
    return D
counts={1:20,2:0,3:0}
for u1 in range(1,N+1):
    for v0 in range(N+1):
        for v1 in range(max(v0+1,u1),u1+N+1):
            d=a(v0)*a(v1-u1)-a(v1)*a(v0-u1)
            assert d>0
            counts[2]+=1
for u1 in range(1,N+1):
    for u2 in range(u1+1,u1+N+1):
        for v0 in range(N+1):
            for v1 in range(max(v0+1,u1),u1+N+1):
                for v2 in range(max(v1+1,u2),u2+N+1):
                    assert det3((0,u1,u2),(v0,v1,v2))>0
                    counts[3]+=1
assert counts=={1:20,2:6270,3:1903534}
rows=(0,1,2,3,4);cols=(18,19,20,21,22)
E=det([[H(R,R-c+r) for c in cols] for r in rows])
assert E==-12890242975052687549013416749816254638339557376
spot=0
for u1 in [1,2,3,5,8,13,19]:
    for u2 in [u1+1,u1+2,u1+5,u1+19]:
        for u3 in [u2+1,u2+2,u2+19]:
            u=(0,u1,u2,u3)
            for v0 in [0,1,5,10,19]:
                for t1 in [0,1,3,7,19]:
                    v1=max(v0+1,u1)+t1
                    if v1>u1+N:continue
                    for t2 in [0,1,3,7,19]:
                        v2=max(v1+1,u2)+t2
                        if v2>u2+N:continue
                        for t3 in [0,1,3,7,19]:
                            v3=max(v2+1,u3)+t3
                            if v3>u3+N:continue
                            v=(v0,v1,v2,v3)
                            assert det([[a(c-r) for c in v] for r in u])>0
                            spot+=1
assert spot==30625
assert det([[H(6,6-(c-r)) if 0<=c-r<=4 else 0 for c in (1,4,5,6)] for r in range(4)])==-4117994496
print("R436_EXACT_PASS lower",counts,"spot4",spot,"negative_E21",E)
