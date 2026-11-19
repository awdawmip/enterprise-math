#!/usr/bin/env python3
"""R284BG exact Port star-decoder + exhaustive/census tests; standard library only."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations,product
from math import factorial,isqrt
from random import Random
import hashlib,json

def prime(n):
    p=max(3,n|1)
    while any(p%d==0 for d in range(3,isqrt(p)+1,2)):p+=2
    return p

def controls(n,H,delta=0):
    assert n>=3 and H>=2
    delta=Fraction(delta);assert delta>=0
    p=prime(n);a=[2*p*j+(j*j%p) for j in range(n)];A=max(a)
    R=A+1;Q=4*A+2;e=[Q+v for v in a];S=sum(e)
    t=[0]+[R+2*a[i] for i in range(1,n)]
    L=n*factorial(n)*(1+H)**n
    b=2*L+1 if not delta else 4*L+8*(-(-delta.numerator//delta.denominator))+9
    return dict(n=n,H=H,p=p,a=a,A=A,R=R,Q=Q,e=e,S=S,t=t,b=b,
                d=[b**v for v in e],z=[0]+[b**v for v in t[1:]])

def det(M):
    A=[row[:] for row in M];n=len(A);den=1;sgn=1
    for k in range(n-1):
        if not A[k][k]:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None:return 0
            A[k],A[r]=A[r],A[k];sgn=-sgn
        v=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j],rem=divmod(A[i][j]*v-A[i][k]*A[k][j],den)
                assert rem==0
            A[i][k]=0
        den=v
    return sgn*A[-1][-1]

def observe(C,c):
    n=c['n'];M=[[(c['d'][i] if i==j else 0)-C[i][j] for j in range(n)] for i in range(n)]
    for i in range(1,n):M[0][i]-=c['z'][i]
    return det(M)

def digit(y,b,k):
    assert k>=1
    w=b**k;q=(Fraction(y)+Fraction(w,2))//w
    return (q+b//2)%b-b//2

def decode(y,c):
    n,b,e,S,t=[c[k] for k in ('n','b','e','S','t')]
    C=[[0]*n for _ in range(n)];P={}
    for i in range(n):C[i][i]=-digit(y,b,S-e[i])
    for i,j in combinations(range(n),2):
        P[i,j]=C[i][i]*C[j][j]-digit(y,b,S-e[i]-e[j])
    for i in range(1,n):
        C[i][0]=-digit(y,b,t[i]+S-e[0]-e[i]);assert C[i][0]>0
        C[0][i],r=divmod(P[0,i],C[i][0]);assert not r
    for i in range(1,n):
        for j in range(1,n):
            if i==j:continue
            g=digit(y,b,t[i]+S-e[0]-e[i]-e[j])
            C[i][j],r=divmod(C[i][0]*C[j][j]-g,C[j][0]);assert not r
    assert all(1<=v<=c['H'] for row in C for v in row)
    return C

def census(n):
    c=controls(n,2);e,S,t,a=[c[k] for k in ('e','S','t','a')]
    assert len({a[i]+a[j] for i in range(n) for j in range(i,n)})==n*(n+1)//2
    mon=defaultdict(list)
    for mask in range(1<<n):
        U=tuple(j for j in range(n) if mask>>j&1)
        mon[sum(e[j] for j in U)].append(('F',U))
    for i in range(1,n):
        idx=[j for j in range(1,n) if j!=i]
        for mask in range(1<<(n-2)):
            U=tuple(j for k,j in enumerate(idx) if mask>>k&1)
            mon[t[i]+sum(e[j] for j in U)].append((i,U))
    target=[]
    for i in range(n):target.append((S-e[i],('F',tuple(j for j in range(n) if j!=i))))
    for i,j in combinations(range(n),2):
        target.append((S-e[i]-e[j],('F',tuple(k for k in range(n) if k not in (i,j)))))
    for i in range(1,n):
        idx=tuple(j for j in range(1,n) if j!=i)
        target.append((t[i]+S-e[0]-e[i],(i,idx)))
        for j in range(1,n):
            if i!=j:target.append((t[i]+S-e[0]-e[i]-e[j],(i,tuple(k for k in idx if k!=j))))
    for exp,label in target:assert mon[exp]==[label],(n,exp,label,mon[exp])
    return dict(n=n,unique_target_addresses=len(target),observed_monomial_addresses=len(mon),status='PASS')

def run():
    cases=[];total=0
    for n,H,count in [(3,2,512),(3,3,20),(4,2,18),(4,3,8),(5,2,3),(6,2,1)]:
        c=controls(n,H);rng=Random(284241+17*n+H);h=hashlib.sha256();bits=0
        seq=(product(range(1,H+1),repeat=n*n) if (n,H)==(3,2) else
             ([rng.randint(1,H) for _ in range(n*n)] for _ in range(count)))
        for flat in seq:
            flat=list(flat);C=[flat[i*n:i*n+n] for i in range(n)]
            y=observe(C,c);assert decode(y,c)==C
            h.update(bytes(flat));h.update(b'-' if y<0 else b'+')
            h.update(abs(y).to_bytes((abs(y).bit_length()+7)//8,'big'))
            bits=max(bits,abs(y).bit_length())
        old_Q=2*c['A']+1;old_exp=sum(old_Q+x for x in c['a'])+1+2*c['A']
        cases.append(dict(n=n,H=H,count=count,coverage='exhaustive' if (n,H)==(3,2) else 'fixed_seed',
             max_control_bits_BG=max(x.bit_length() for x in c['d']+c['z'][1:]),
             max_control_bits_BF=(c['b']**old_exp).bit_length(),max_readout_bits_BG=bits,
             sha256_inputs_outputs=h.hexdigest(),status='PASS'))
        total+=count
    c=controls(3,2,delta=Fraction(7000));rng=Random(284241);noise=0
    for _ in range(32):
        flat=[rng.randint(1,2) for _ in range(9)];C=[flat[3*i:3*i+3] for i in range(3)]
        y=observe(C,c)
        for eps in (-7000,7000,Fraction(6999,2),Fraction(-6999,2)):
            assert decode(y+eps,c)==C;noise+=1
    return dict(schema='R284BG_INTERLEAVED_SIDON_PORT_CHECK_V1',status='PASS',
      scope='author-side exact finite tests, not independent review',
      arithmetic='Python integer Bareiss determinant and Fraction noise',
      reconstruction_tests=total,noise_tests=noise,census=[census(n) for n in range(3,13)],cases=cases)

if __name__=='__main__':print(json.dumps(run(),indent=2,ensure_ascii=False))
