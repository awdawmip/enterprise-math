#!/usr/bin/env python3
"""R4-EC15 standalone author-side exact checks; analytic theorem in companion proof.
Requires sympy. Grade-count data use integer arithmetic, not Monte Carlo.
"""
from collections import defaultdict
from math import comb, log
import sympy as S

STATES=((0,0,-1),(0,0,1),(1,1,-1),(1,1,1),(2,0,-1),(2,0,1),(2,1,-1),(2,1,1))
POS={s:i for i,s in enumerate(STATES)}
EDGES={0:{0:(2,-1,-1),1:(2,1,-1)},1:{0:(0,-1,-1),1:(0,1,-1)},2:{0:(1,1,1),1:(2,1,-1)}}
def child(s,bit):
    q,r,e=s
    qq,eta,b=EDGES[q][bit]
    ee=e*eta
    assert ee*b==e*(1-2*bit)
    rr=2 if r==2 or (bit==0 and r==1) else (0 if bit==1 else 1)
    return (qq,rr,ee),int(ee*b==-1)

def check_symbolic():
    x,u=S.symbols('x u')
    M=S.zeros(8)
    for i,s in enumerate(STATES):
        for bit in (0,1):
            ss,j=child(s,bit)
            if ss[1]!=2:M[POS[ss],i]+=u**j
    v=S.zeros(8,1);v[POS[(0,0,1)],0]=1
    N=(1-u*x**2)*(1-u*x**3)
    D=1-(1+u)*x+2*u**2*x**4-u**3*x**6
    a=u*x-1;b=u*x**3+x-1;c=u**2*x**5-u*x**3-x+1
    H=S.Matrix((-u*x**4*a,a*b,-u*x**3*a,u*x**2*c,-x**2*a,u*x*c,x*a*b,-u**2*x**5*a))
    assert all(S.expand(y)==0 for y in (S.eye(8)-x*M)*H-(1+u*x**2)*D*v)
    assert S.expand(sum(H)-(1+u*x**2)*N)==0
    L=1+u-2*u**2+7*u**3-29*u**4+135*u**5-670*u**6
    P=S.expand(L**6-(1+u)*L**5+2*u**2*L**2-u**3)
    assert all(P.coeff(u,k)==0 for k in range(7))
    f=S.series(S.log(L),u,0,5).removeO()
    g=S.expand(u*S.diff(f,u))
    alpha=S.symbols('alpha')
    uu=alpha+5*alpha**2+22*alpha**3+86*alpha**4+276*alpha**5
    target=S.series(g.subs(u,uu)-alpha,alpha,0,5).removeO()
    assert S.expand(target)==0
    dI=S.series(S.log((1-alpha)*(uu/alpha)),alpha,0,4).removeO().expand()
    assert [dI.coeff(alpha,k) for k in (1,2,3)]==[4,9,S.Rational(52,3)]
    # Pole-residue amplitude is 1-2u+12u²-65u³+...
    rho=S.series(1/L,u,0,4).removeO()
    A=S.series((-N/(x*S.diff(D,x))).subs(x,rho),u,0,4).removeO().expand()
    assert [A.coeff(u,k) for k in range(4)]==[1,-2,12,-65]
    return 'PASS: exact eight-state matrix, rational F, lambda, saddle, I coefficients and residue'

def exact_counts():
    # Separate eight-state path DP, then check recurrence derived from rational F.
    d={((0,0,1),0):1}
    dp={}
    for n in range(151):
        row=defaultdict(int)
        for (_,j),v in d.items():row[j]+=v
        dp[n]=dict(row)
        nd=defaultdict(int)
        for (s,j),v in d.items():
            for bit in (0,1):
                ss,k=child(s,bit)
                if ss[1]!=2:nd[ss,j+k]+=v
        d=nd
    src={(0,0):1,(2,1):-1,(3,1):-1,(5,2):1}
    ring=[[0]*401 for _ in range(6)]
    for n in range(3001):
        row=[0]*401
        def old(ni,j):return ring[ni%6][j] if ni>=0 and 0<=j<=400 else 0
        for j in range(min(n,400)+1):
            row[j]=old(n-1,j)+old(n-1,j-1)-2*old(n-4,j-2)+old(n-6,j-3)+src.get((n,j),0)
            assert row[j]>=0
        if n<=150:
            assert all(row[j]==dp[n].get(j,0) for j in range(n+1)),n

        if n in (1000,3000):
            j=70 if n==1000 else 200
            p=log(row[j])-log(comb(n,j))
            print('sample',n,j,'log_exact',round(p,10),'two_term',round(-2*j*j/n-3*j**3/n**2,10))
        ring[n%6]=row
    for n in range(13):
        bins=defaultdict(int)
        for word in range(1<<n):
            s=(0,0,1);j=0
            for i in range(n):
                s,k=child(s,(word>>i)&1);j+=k
            if s[1]!=2:bins[j]+=1
        assert all(bins[j]==dp[n].get(j,0) for j in range(n+1)),n

    return 'PASS: 8191 exhaustive words n<=12; 11476 exact DP-vs-recurrence coefficients n<=150; recurrence n<=3000,j<=400'

if __name__=='__main__':
    print(check_symbolic())
    print(exact_counts())
    print('CLAIM SCOPE: Author-side finite checker; uniform analytic theorem requires the proof in the companion markdown; no native X6 or Driver acceptance.')
