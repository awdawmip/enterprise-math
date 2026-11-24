# R284GV — Exact two-cut count and fixed-diagonal-gap flexibility law

2026-11-24. Author proof, NOT_REVIEWED. Independent informed continuation of the auxiliary four-phase fixed binary tag model. P000 and ACTIVE worldview unchanged. Existing own registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Current owner inventory r1-20261124-1900-owner-inventory-read RUNNING at derivation; no shared CLAIM or formal Task mutation. Verified current normative entry snapshots GK 4969d4809534d005294f87c18c0355e793164d34, EM aceb80d27535d6a566b617e33075547bf5467036. Frozen science: GU f14ef36840c37d78c1537c930f192fdb43d3b094:research_notes/portable_direct/R284GU_UNIFORM_FLEXIBILITY_AND_CRITICAL_SHIFT_20261124.md and GS 66a518fef06384f130ecd16912ef5a2231ebc960:research_notes/portable_direct/R284GS_LOW_OMISSION_ASYMMETRIC_PATH_COUNTS_20261124.md, with their GL/GQ/GR dependencies. No repinning or native physical attribution.

## 1. Exact two-cut theorem (all low-omission parameters)

For integers u>=1, 0<=q<u, H=2q+u+1, J=q+3u, take the three GS orientations (A,B,C)=(H,J,H),(H-1,J+1,H),(H,J+1,H-1). Let s=2u+1-(C-2q), t=A-2q-s in {0,1}, m=q+s, g=B-2m. In all three orientations g>=0. Denote the count of safe mode words by N(A,B,C). With binom(n,k)=0 outside 0<=k<=n, define

L_i = sum_{k=0..min(i,t)} binom(q+k-1,k) [binom(i-k+s-1,i-k)-binom(i-k+s-1,i-t-1)] for q>=1;
L_i = binom(i+s-1,i)-binom(i+s-1,i-t-1) for q=0;
R_j = binom(j+m-1,j)-binom(j+m-1,j-t-1).

Then the exact positive port-composition formula is

N(A,B,C) = sum_{0<=i<s+t, 0<=j<m+t, i+j<=A} L_i R_j binom(A-i-j+g,g).

This replaces the two-barrier reflection kernel by two one-barrier kernels and an unrestricted middle. It covers q=0 and the endpoint g=0, and preserves both integer port inventories. The count is a BRC positive-branch composition with multiplicities, not a statement that the underlying history can be erased for arbitrary observers.

Proof: from the frozen GL/GS criterion at cumulative counts a,b, safety is exactly [A-2q-a]_+ + [b-q]_+ >= s and b<=B-q-s+[a-q]_+. Hence the lower rule is automatic at b>=m, and the upper rule is automatic at b<=B-m. Because g>=0, split at the first m-th B from the left and the first m-th B from the right. The two marked B steps are distinct even when g=0. At the left cut let the number of A steps already consumed be i; at the reversed right cut let it be j. The middle lies entirely in m<=b<=B-m, so its only conditions are its fixed inventory A-i-j of A steps and g of B steps.

Before the left cut, the lower rule is precisely a<=t when b<q, and a<=t+b-q when q<=b<m. Upper is automatic. Thus i<=s+t-1. For q>=1 mark the q-th B, at A count k<=min(i,t); its prefix has binom(q+k-1,k) words. From (k,q) to (i,m-1) the height t+b-q-a must stay nonnegative. Reflection across the first forbidden height -1 counts the surviving words by the displayed binomial difference; append the m-th B. For q=0 the first segment is already that one-barrier walk with initial height t. In reverse coordinates a'=A-a,b'=B-b, the upper rule becomes b'>=min(a'-t,m), because A=2q+s+t. Before the reversed m-th B, it reduces to t+b'-a'>=0, giving j<=m+t-1 and the stated R_j by the same reflection argument. All cuts and their connecting inventories are unique and sufficient, so multiplying and summing counts every safe word exactly once. No independence approximation.

## 2. Fixed-gap theorem

Let d=u-q be any fixed positive integer. Define S=N(H,J,H), P=N(H-1,J+1,H), Q=N(H,J+1,H-1), K=PQ(J+1)^2/(S^2 H) as in GS/GU. Then

lim_{u->infinity, q=u-d} u K
= F(d)
= 32 d (2d^2+6d+7) / [3(d+1)(d+2)(2d+3)].

In particular the symmetric code eventually wins labeled cycle counts, with asymmetric/symmetric ratio K^2 asymptotic to F(d)^2/u^2. F(1)=16/3; F(d) increases strictly to 32/3. The limit matches the endpoint lambda->1 of GU's interior linear-regime constant; this is a fixed-d theorem, not uniform over arbitrary d=o(u).

Proof: write s=u+c, with (c,t,g)=(0,1,d),(0,0,d+1),(1,0,d-1) for S,P,Q respectively. Introduce nonnegative deficits I=s+t-1-i and J0=m+t-1-j (J0 distinct from the mode inventory J). Then A-i-j=I+J0+2-d-c-t. Normalize by U=binom(2u,u), V=binom(4u,2u). For each fixed I,J0 the preceding exact formulas yield

L_i / (U u^(t-1)) -> (I+1) 2^(2c-2-I),
R_j / (V/u) -> (t+1)(J0+1) 2^(2(c-d)+t-3-J0).

Details: for fixed integers a,b, binom(2n+a,n+b)/binom(2n,n)->2^a by factorial cancellation. In L_i the k=t term has binom(q+t-1,t)~u^t (t=0,1). Its reflected difference equals its first binomial times (I+1)/s. The k=0 term when t=1 has reflection factor O((I+1)/u) and lacks the factor q, so is lower order. In R_j, put n=j+m-1. The subtracted/first ratio is (j)_(t+1)/(m)^(rising t+1). Thus the reflection factor is asymptotic to (t+1)(J0+1)/m (direct for t=0; for t=1 use 1-(m-J0)(m-J0-1)/(m(m+1))). Since m/u->2, the second limit follows.

Justification of summation: extend each deficit summand by zero off its actual finite domain. For each fixed d and orientation, every relevant first binomial is bounded relative to U or V by C_d 2^(-I) or C_d 2^(-J0): decreasing a down-step inventory by I at fixed up-step inventory has binomial ratio (i0)_I/(n0)_I <=(i0/n0)^I with i0/n0=1/2+O_d(1/u) and I=O(u), and likewise on the right. The reflected differences are bounded by these binomials times C_d(I+1)/u or C_d(J0+1)/u: the reflection factor is 1 minus a product of at most two ratios with denominators of order u, each deficit from 1 bounded by the corresponding linear deficit divided by u; if the reflected term is zero the same bound holds after enlarging the constant because the deficit is then of order u. On the left sum at most two terms with prefactor bounded by C u^t. The unrestricted middle binomial is at most C_d(1+I+J0)^g, since g is fixed. Hence the normalized terms are dominated by a summable polynomial times 2^(-I-J0), proving termwise limiting summation (e.g. finite truncation and uniform geometric-polynomial tail). This bound retains the joint residual inventory, not separated independent endpoints.

Grouping by z=I+J0 uses sum_{I=0..z}(I+1)(z-I+1)=binom(z+3,3). Consequently

N/(UV u^(t-2)) -> (t+1)2^(4c-2d+t-5) * sum_{z>=0, z+2-d-c-t>=0} binom(z+3,3)2^(-z)binom(z+2-d-c-t+g,g).

For S,P,Q the sums are respectively weighted by binom(z+1,d), binom(z+3,d+1), binom(z,d-1); all automatically enforce the middle nonnegative condition. The constant powers of 2 in PQ/S^2 cancel. The series generating function sum_{z>=0} binom(z+3,3)2^(-z)(1+x)^z=16/(1-x)^4, analytic near x=0, gives the three sums as 16 times

a=binom(d+3,3)+binom(d+2,3),
b=sum_{k=0..3} binom(3,k)binom(d+4-k,3),
c0=binom(d+2,3).

Therefore u^2 PQ/S^2 -> b c0/a^2, and (J+1)^2/(uH)->16/3, proving F. Algebra: a=(d+1)(d+2)(2d+3)/6, b=(2d+3)(2d^2+6d+7)/3, c0=d(d+1)(d+2)/6. Also F(d+1)-F(d)=32(2d^3+8d^2+15d+15)/[(d+1)(d+2)(d+3)(2d+3)(2d+5)]>0 and F(d)->32/3. The fixed-gap limit arises from the full port convolution; the iid endpoint approximation in GU is not used.

## 3. Executed exact evidence

Python arbitrary-precision integers, exact Fraction ratios; decimal output only. Cross-checked the new double sum against original GL residual-distance DP for all 759 orientation cases u=1..22 and q=0..u-1, zero mismatch. Also computed 16 fixed-gap comparisons, d in {1,2,4,8}, u in {32,64,128,256}. Actual uK (columns u ascending) and exact limit:

d=1: 4.50435083343719, 4.877932241560862, 5.093902845843232, 5.210465913952067; limit 16/3.
d=2: 6.256721304797417, 6.522909411665125, 6.68031575474291, 6.766125600519374; limit 48/7.
d=4: 8.757202986062099, 8.407726052294356, 8.265089901523698, 8.202296754511291; limit 448/55.
d=8: 14.064612334713882, 11.190535630372302, 10.075658257495453, 9.584057674114165; limit 7808/855.

These numbers cross-check the analytic result; the fixed-d convergence need not be monotone in u. Executed checker:

```python
from math import comb
from fractions import Fraction

def C(n,k): return comb(n,k) if 0<=k<=n else 0

def split(q,u,A,B,D):
    s=2*u+1-(D-2*q);t=A-2*q-s;m=q+s;g=B-2*m
    assert g>=0 and t in (0,1)
    L=[];R=[]
    for i in range(s+t):
        if q==0: v=C(i+s-1,i)-C(i+s-1,i-t-1)
        else: v=sum(C(q+k-1,k)*(C(i-k+s-1,i-k)-C(i-k+s-1,i-t-1)) for k in range(min(i,t)+1))
        L.append(v)
    for j in range(m+t): R.append(C(j+m-1,j)-C(j+m-1,j-t-1))
    return sum(v*w*C(A-i-j+g,g) for i,v in enumerate(L) for j,w in enumerate(R) if i+j<=A)

def dp(q,u,A,B,D):
    r=2*u+1;M=max(0,D-q);p=lambda x:max(0,x);v=[0]*(B+1)
    for a in range(A+1):
        for b in range(B+1):
            D2=p(A-a-2*q)+p(p(b-q)+M-q)
            D3=max(0,D-2*q,p(a-q)-q,B-b+p(a-q)-2*q+M)
            v[b]=0 if min(D2,D3)<r else 1 if a==b==0 else v[b]+(v[b-1] if b else 0)
    return v[B]

def configs(q,u):
    H=2*q+u+1;J=q+3*u
    return [(H,J,H),(H-1,J+1,H),(H,J+1,H-1)]

def limit(d):
    a=C(d+3,3)+C(d+2,3)
    b=sum(C(3,k)*C(d+4-k,3) for k in range(4))
    c=C(d+2,3)
    return Fraction(16*b*c,3*a*a)

def calc(u,d):
    q=u-d;H=2*q+u+1;J=q+3*u
    S,P,Q=[split(q,u,*c) for c in configs(q,u)]
    return Fraction(u*P*Q*(J+1)**2,S*S*H)
if __name__=='__main__':
    n=0
    for u in range(1,23):
        for q in range(u):
            for c in configs(q,u):
                assert split(q,u,*c)==dp(q,u,*c),(q,u,c)
                n+=1
    print('exact comparisons',n,flush=True)
    for d in [1,2,4,8]:
        print('d',d,'limit',limit(d),'decimal',float(limit(d)),flush=True)
        for u in [32,64,128,256]:
            print(u, float(calc(u,d)),flush=True)
```

## 4. Next questions

Uniform near-diagonal d->infinity, d=o(u) remains open. The positive port convolution identifies the relevant deficit scale z~O(d), suggesting a uniform expansion for d=o(sqrt(u)), then a saddle/large-deviation analysis across the larger window. The exact count is also available for investigating P<S and finite-u unique crossing without repeating capacity searches. GP/GQ independent proof certificates and the middle-regime optimum remain separate. No formal Result or Review claimed.
