# R284HA — Exact binomial port moments and fixed-gap first correction

2026-11-25. Author proof, NOT_REVIEWED. Independent auxiliary four-phase binary-tag model, not native physical attribution. Frozen inputs: R284GZ at 976ccb8b2ee5d0bd4fbde8db8ef8b905f5a1c957 (blob 250d7230370f23ec87f0197df14100964463aeac), R284GY at 431a4173ec6387393a3ab0c8a928843a7babb0ce (blob 1091b1f6ce65f944c2fff2b8790a7f2cfb9f3fd9), R284GX at dff580f539319ddcfd5f521a2cb65bd0f783c4c0 (blob 681b2f41eb4df9f633f01dc1dccecd06f66e140c), with their original GV/GL/GS pins. Current GitHub global entry files verified at 2950a3d7efff543e39f6fe688cf58f9b135b2aa2; current portable and continuation protocols, P000 V5, ACTIVE worldview, joint observer, heartbeat and residual-fidelity contracts, weighted BRC startup and project research method read. Gateway em_status succeeded; old owner request r284gz-20261124-2300-owner-read-v1 SUCCEEDED/error=null, no LEASED tasks on its snapshot; fresh read r284ha-20261125-0000-owner-read-v1 RUNNING on last observation. Historical EM-DIRECT-0C386E and RA-B82240E8488EF5A1DA5186C4 are provenance only; current own research authority unconfirmed. No shared CLAIM or protected mutation. Independent nonoverwriting note.

## 1. Exact port transform

For n>=0 let U_n(x)=C(2n-x,n-x)-C(2n-x,n-x-1) for 0<=x<=n, zero otherwise. C(n,k)=0 outside valid nonnegative binomial domain. The GY primitive kernel l_n is exactly U_(n-1). Define the binomial moment

M_n(k)=sum_x C(x,k) U_n(x).

Theorem: for all n,k>=0,
M_n(k)=(k+1)/(n+1) C(2n+2,n-k).

Proof: let C(t)=1+t C(t)^2 be the formal Catalan series with constant 1. The ballot coefficient formula (from Lagrange inversion, or the ordinary ballot reflection identity) gives U_n(x)=[t^(n-x)] C(t)^(x+1). Thus sum_n U_n(x)t^n=t^x C(t)^(x+1). All coefficients involve only finite sums. Summing C(x,k) over x gives
sum_n M_n(k)t^n=C(t)(t C(t))^k/(1-t C(t))^(k+1)=t^k C(t)^(2k+2).
Applying the same coefficient formula yields the stated binomial expression. In particular M_n(0)=Catalan_(n+1), and for k<n the exact adjacent recurrence is
M_n(k+1)/M_n(k)=(k+2)(n-k)/[(k+1)(n+k+3)].

## 2. Exact S,P,Q using only a few short positive convolutions

Let d=u-q>=1, m=u+q, H=2q+u+1, J=q+3u, and B_(n,m)(g)=sum_{k=0}^g M_n(k)M_m(g-k), with zero for g<0. Vandermonde gives for any nonnegative integer a,g:
sum_{I,J0} U_n(I)U_m(J0) C(I+J0+a,g)
= sum_{j=0}^a C(a,j) B_(n,m)(g-j).
This is an exact positive observer factorization, not an independent allocation approximation. Substitute the three distinct middle inventories from GY:
Q=B_(u,m)(d-1);
S=B_(u,m)(d)+B_(u,m)(d-1)+q[B_(u-1,m)(d)+B_(u-1,m)(d-1)];
P=sum_{j=0}^3 C(3,j) B_(u-1,m-1)(d+1-j).
The formulas hold at u=1 and q=0, including U_0. After the four initial Catalan numbers are obtained, only O(d+1) exact integer arithmetic operations and O(d+1) integer slots are needed; bit lengths and initial binomial computation still grow with u. This is particularly useful near the diagonal. The compression is exact for the declared count observer and the associated K=PQ(J+1)^2/(S^2 H), not for the full joint distribution or the individual path provenance. Preserve the original GY/GZ kernel for those observers.

## 3. New fixed-gap first correction

For each fixed positive integer d, let u tend to infinity and q=u-d. Then
uK=F(d)+A(d)/u+O_d(u^(-2)),
where
F(d)=32 d(2d^2+6d+7)/[3(d+1)(d+2)(2d+3)]
(the prior GV limit), and
A(d)=8d(314d^3-115d^2-2072d-3578)/[45(d+1)(d+2)(2d+3)].

Proof: normalize M_n(k) by M_n(0). Its exact product is (k+1)(n falling k)/(n+3 rising k), hence for fixed k
M_n(k)/M_n(0)=(k+1)[1-k(k+2)/n+O_k(n^-2)].
For n=u or u-1, and l=2u-d or 2u-d-1, put b_g=C(g+3,3), c_g=C(g+4,5), both zero at negative g. The normalized convolution is
B_(n,l)(g)/[M_n(0)M_l(0)] = b_g-9c_g/u+O_d(u^-2)
for the finitely many g used above. Indeed sum_k (k+1)(g-k+1)=b_g, and sum_k (k+1)k(k+2)(g-k+1)=6c_g by multiplying the generating series 6t/(1-t)^4 and 1/(1-t)^2. Symmetry supplies the coefficient 6(1+1/2)=9.

Let L=b_d+b_(d-1), L1=-9(c_d+c_(d-1)), p0=sum_j C(3,j)b_(d+1-j), p1=-9 sum_j C(3,j)c_(d+1-j), Q1=-9c_(d-1). Let T=M_u(0)M_m(0). The exact ratio M_(n-1)(0)/M_n(0)=(n+2)/(4n+2) gives
S/T=(u/4)L[1+(11/2-d+L1/L)/u+O_d(u^-2)];
P/T=(p0/16)[1+(9/4+p1/p0)/u+O_d(u^-2)];
Q/T=b_(d-1)[1+Q1/(u b_(d-1))+O_d(u^-2)].
Also (J+1)^2/H=(16u/3)[1+(d+1)/(6u)+O_d(u^-2)].
Multiplying these expansions gives F=(16/3)p0 b_(d-1)/L^2, and
A/F=(26d-103)/12+p1/p0+Q1/b_(d-1)-2L1/L.
Substitution of the finite binomial polynomials yields the displayed rational formulas (also simplified with SymPy during this run). They apply at d=1 because negative-index terms vanish. The numerator cubic in A has values negative at d=1,2,3, positive at d=4, and forward difference 942d^2+712d-1873 positive for d>=2. Thus for each fixed d=1,2,3 the limit is approached from below for sufficiently large u; for each fixed d>=4 it is approached from above. This is a new sign transition, not a claim of finite-u monotonicity. The O_d bound is for fixed d only.

## 4. Executed evidence

Python exact integers and Fraction:
- 3,402 direct binomial-moment comparisons (n=0..80, k=0..n+1).
- 975 original GL residual DP comparisons (all three counts, u=1..25, q=0..u-1).
- 32,896 parameter pairs u=1..256, q=0..u-1, with S>P+Q; all 32,640 adjacent K comparisons strictly decreasing, no K=1 ties. Previous GX covered only u<=64. Largest q with K>1 at u=1,2,4,8,16,32,64,128,256: 0,0,2,5,9,16,27,43,67. This is finite evidence, not the unbounded monotonicity theorem.
- Large examples (u,d,uK,bit length of S): (256,1,5.210465913952067,1520), (1024,1,5.30199920005187,6124), (4096,4,8.148828375076144,24549), (16384,16,9.819991061013535,98254), (65536,32,10.214349405804159,393133). Last computation took about 4.24 s in the local environment including initial binomial computation; not a cross-platform speed claim.
- Fixed-gap correction check: columns d, theoretical A, u*(uK-F) at u=256,1024,4096:
1, -32.302222, -31.454059, -32.086152, -32.247947
2, -24, -23.300418, -23.821874, -23.955262
3, -6.965926, -6.349303, -6.809165, -6.926569
4, 13.769697, 14.551606, 13.967206, 13.819206
8, 110.828538, 115.684846, 112.023092, 111.126012
16, 324.010109, 355.926958, 331.556125, 325.871672.
All displayed ratios computed from exact integers then converted to decimals. Formula F(3)=344/45=7.644444... and F(16)=10496/1071=9.800186... correct the previous chat summary's displayed approximate values; the prior GV rational theorem itself is unchanged.

Reproduction (same exact algorithm and scan, no optional dependencies):
```python
from math import comb
from fractions import Fraction
def C(n,k): return comb(n,k) if 0<=k<=n else 0
def U(n,x): return C(2*n-x,n-x)-C(2*n-x,n-x-1) if 0<=x<=n else 0
def moments(n,g):
    out=[C(2*n+2,n)//(n+1)]
    for k in range(min(n,g)):
        num=out[-1]*(k+2)*(n-k); den=(k+1)*(n+k+3)
        assert num%den==0
        out.append(num//den)
    return out+[0]*max(0,g+1-len(out))
def counts(q,u):
    d=u-q;m=u+q;g=d+1
    A=moments(u,g); a=moments(u-1,g); B=moments(m,g); b=moments(m-1,g)
    def T(X,Y,g): return sum(X[k]*Y[g-k] for k in range(g+1)) if g>=0 else 0
    Q=T(A,B,d-1)
    S=Q+T(A,B,d)+q*(T(a,B,d)+T(a,B,d-1))
    P=sum(comb(3,j)*T(a,b,d+1-j) for j in range(4))
    return S,P,Q
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
def K(q,u):
    S,P,Q=counts(q,u);return Fraction(P*Q*(q+3*u+1)**2,S*S*(2*q+u+1))
if __name__=='__main__':
    for n in range(81):
        M=moments(n,n+1)
        for k in range(n+2): assert M[k]==sum(C(x,k)*U(n,x) for x in range(n+1))
    for u in range(1,26):
        for q in range(u): assert counts(q,u)==tuple(dp(q,u,*c) for c in configs(q,u))
    for u in range(1,257):
        prev=None
        for q in range(u):
            S,P,Q=counts(q,u); assert S>P+Q
            k=Fraction(P*Q*(q+3*u+1)**2,S*S*(2*q+u+1))
            assert prev is None or k<prev
            assert k!=1
            prev=k
    for d in (1,2,3,4,8,16):
        F=Fraction(32*d*(2*d*d+6*d+7),3*(d+1)*(d+2)*(2*d+3))
        A=Fraction(8*d*(314*d**3-115*d*d-2072*d-3578),45*(d+1)*(d+2)*(2*d+3))
        print(d,float(F),float(A),[float(u*(u*K(u-d,u)-F)) for u in (256,1024,4096)])
```

## 5. Next

Use the positive moment coefficients and the adjacent rational recurrence to compare K(q+1,u) with K(q,u) without reconstructing the double-cut path sets. A direct stochastic-order proof on the marginal Z cannot assume nested one-sided support: for Q the support is [d-1,u+m] and changing q to q+1 expands both ends to [d-2,u+m+1], with positive new mass at both endpoints. Therefore neither global first-order stochastic dominance holds for Q's Z distributions, even though conditional allocation comparisons may hold. Retain both ports for allocation questions. The full finite K monotonicity question and current Activity association remain open. No formal Result or review asserted.
