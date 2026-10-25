"""R286 exact BRC reflection check: raw words, six-edge DP, positive formal series."""
import json
from collections import defaultdict

N = 150
M = N//2+5
T = (((2,-1,-1),(2,1,-1)),((0,-1,-1),(0,1,-1)),((1,1,1),(2,1,-1)))
h = [0]*(M+1)
for n in range(1,M+1):
    h[n] = int(n==4)+sum(c*h[n-j] for j,c in ((1,1),(2,2),(3,1),(4,1)) if n>=j)
    h[n] += sum(c*sum(h[i]*h[n-j-i] for i in range(n-j+1)) for j,c in ((1,1),(2,2),(3,1)) if n>=j)
assert all(h[n]>0 for n in range(4,M+1))

def mul(a,b):
    z=[0]*(M+1)
    for i,ai in enumerate(a):
        if ai:
            for j in range(M+1-i):z[i+j]+=ai*b[j]
    return z

def add(a,b):return [i+j for i,j in zip(a,b)]
def shift(a):return [0]+a[:M]
one=[1]+[0]*M
A=add(one,shift(one))
B=add(one,h)
R=add(shift(one),mul(A,h))
S=add(one,shift(mul(mul(A,B),R)))
plus={}; minus={1:mul(B,R)}
a=b=one
for k in range(1,N+1):
    plus[k]=mul(a,mul(b,B))
    if k>=2:
        minus[k]=mul(mul(a_prev,b),S)
    a_prev=a
    a=mul(a,A); b=mul(b,B)
    assert min(plus[k]+minus[k])>=0

states={(0,1,0,False):1}
checks=positive=words=0
for n in range(N+1):
    P=defaultdict(int)
    for (q,e,k,last),num in states.items():
        if q==0:P[e,k]+=num
    if n<=15:
        brute=defaultdict(int)
        for word in range(1<<n):
            q,e,k,last=0,1,0,False
            for i in range(n):
                bit=(word>>(n-1-i))&1
                if last and bit==0:break
                q1,eta,c=T[q][bit]
                q,e,k,last=q1,eta*e,eta*k+c,bit==0
            else:
                if q==0:brute[e,k]+=1
        assert dict(brute)==dict(P)
        words+=1<<n
    for k in range(1,n+1):
        m=(n-k-2)//2
        ep=plus[k][m] if n>=k+2 and (n-k)%2==0 else 0
        en=(minus[1][(n-5)//2] if n>=5 and n%2 else 0) if k==1 else (minus[k][m] if n>=k+2 and (n-k)%2==0 else 0)
        dp=P[1,-k]-P[1,k]; dn=P[-1,-k]-P[-1,k]
        assert (dp,dn)==(ep,en),(n,k,dp,dn,ep,en)
        checks+=2;positive+=int(dp>0)+int(dn>0)
    nxt=defaultdict(int)
    for (q,e,k,last),num in states.items():
        for bit,(q1,eta,c) in enumerate(T[q]):
            if last and bit==0:continue
            nxt[q1,eta*e,eta*k+c,bit==0]+=num
    states=nxt
print(json.dumps({'schema':'EM_R286_EXACT_REFLECTION_EVIDENCE_V1','max_length_inclusive':N,'raw_words_checked':words,'signed_reflection_exact_checks':checks,'strict_positive_gaps':positive,'h_positive_range':[4,M],'arithmetic':'unbounded exact integers','status':'PASS'},indent=2))
