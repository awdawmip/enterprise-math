# R284HI — All-budget strict monotonicity in both quarter-strip directions

2026-11-25. Author proof with exact computational certificates; NOT_REVIEWED. Same auxiliary binary-tag word-count observer, no native physical attribution. Frozen input: HH f9b8351559e49b13fbe70faad67d87e1b84fa9b9:research_notes/portable_direct/R284HH_ALL_BUDGET_SIGN_CLASSIFICATION_20261125.md, including its HA, HE, HF count identities and explicit quarter-strip payment. Current control entries read at EM a5f7005b1ebcf3b05053f7cb57ad5e1752ced159 and GK 9a9abd8586235d6dcb751c8412ed9b035a8c77fb; P000 V5/ACTIVE worldview retained. Own registration r1-20261124-0256-r284gd-session-v1 verified, recovery r1-20261125-0801-own-recovery returned open own session, no runs; EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Owner query r1-20261125-0802-owner-read was RUNNING at last pre-publication observation. Independent continuation, no shared CLAIM.

## Result and scope

For all integers u>=1, q>=0:
* If 4(q+1)<=u, K(q,u)>K(q+1,u).
* If 4q<=u, K(q,u+1)>K(q,u).

These conclusions hold for the original exact counts, not only the rational compressed observer. HH established sign-transition uniqueness over all budgets but did not prove original K monotonicity in this entire quarter-strip. HF established the original adjacent inequalities only at u>=10000 in the narrower eighth-strip. This result removes the lower budget cutoff and extends both directions to the quarter-strip. Remaining global q-monotonicity outside the quarter-strip and previously proved diagonal strips is open.

## Quantitative rational separation

Retain HH definitions H=u+2q+1, J=3u+q, D=H+3u, T(a,b,x,t)=1-R_(x+1)-R_(t+1)+R_(x+t+2), R_k=product_(j=0..k-1)(a-j)/(b+j+1).
Set S0=T(H,3u,1,1)+q H/D T(H-1,3u,0,1), P0=H/(3u+1) T(H-1,3u+1,0,0), Q0=(D+1)/(3u+1) T(H,3u+1,0,0). The common binomial factor cancels, so K0=N/B=P0 Q0 (J+1)^2/(S0^2 H), with N,B from the exact factored rational expression. In u=4q+x, N and B have respectively 54 and 63 nonzero coefficients, all positive (minima 192,36).

For the q edge let L=N(u,q)B(u,q+1), R=N(u,q+1)B(u,q). Use the exact joint coordinate u=4(q+1)+x, x>=0. Then G=L-R has 189 positive coefficients (minimum 93312); uG-R has 209 positive coefficients (minimum 93312). Thus K0(q,u)/K0(q+1,u)>1+1/u.

For the u edge let L=N(u+1,q)B(u,q), R=N(u,q)B(u+1,q), using u=4q+x. G=L-R has 187 positive coefficients (minimum 46656); (u+1)G-R has 204 positive coefficients (minimum 132192). Thus K0(q,u+1)/K0(q,u)>1+1/(u+1).

All four coefficient claims are exact polynomial identities/inequalities; reproduction below. No differentiation of unknown original residuals. The finite-difference coordinate keeps both endpoint inventories in the allowed strip.

## Residual payment and infinite tail

By frozen HH, epsilon(u)=200*(19/20)^u and K0/(1+epsilon)^2<=K<=K0*(1+epsilon)^2 for u>=22, 4q<=u. For either edge the true ratio in the desired direction is strictly greater than (1+1/(u+1))/(1+epsilon(u))^4, since epsilon decreases with u. At u=238, exact rational arithmetic gives (1+epsilon)^4-1<1/(u+1); the first such u>=22 is 238 (using this common sufficient bound). Approximate display only: epsilon=0.0009982700793338126, left gap 0.003999063556512951, right gap 0.0041841004184100415.

To propagate to every u>=238, expand (1+epsilon)^4-1 as a polynomial in epsilon with positive coefficients and no constant. With epsilon(u+1)=19 epsilon(u)/20, this expression decreases by at least a factor 19/20 at each step. Multiplying by u+1 changes the successive ratio by at most (19/20)*(u+2)/(u+1)<1. Hence the common payment inequality persists indefinitely. This is a BRC observer-specific paid separation: the exact gap of the compressed joint endpoint comparison dominates both endpoints' omitted positive branch mass. No claim of equality of the original and strip path families or of lossless compression for other observers.

## Finite complement

For u<238 use HA's exact port moments and the original S,P,Q. Compute rows U=1..238, Q=0..floor(U/4); compare adjacent q within each row and adjacent u at common q, via exact cross multiplication, never floating point. Actual execution: 7021 q-edge comparisons (including overlap row 238) and 7199 u-edge comparisons; zero non-strict edges. Thus both asserted directions hold in the entire valid quarter-strip. This is a finite certificate plus an unbounded proof, conditional on the frozen count/payment identities, not a sampled extrapolation.

## Executed reproduction (Python/SymPy, arbitrary precision)

The following compact reproduction contains the executed arithmetic and equivalent assertions. The original exploratory run also checked derivative coefficient bounds; these are unnecessary for the result.

```python
import sympy as s
from fractions import Fraction as F
from math import comb
from functools import lru_cache
u,q,x=s.symbols('u q x');H=u+2*q+1;D=H+3*u;J=3*u+q
def T(a,b,x,t):
    def R(k):return s.prod((a-j)/(b+j+1) for j in range(k))
    return 1-R(x+1)-R(t+1)+R(x+t+2)
S=T(H,3*u,1,1)+q*H/D*T(H-1,3*u,0,1)
P=H/(3*u+1)*T(H-1,3*u+1,0,0)
Q=(D+1)/(3*u+1)*T(H,3*u+1,0,0)
N,B=map(s.expand,s.fraction(s.factor(P*Q*(J+1)**2/(S*S*H))))
def p(a,v):return s.Poly(a.subs(u,v),x,q)
def check(a):
    assert min(a.coeffs())>0
    print(len(a.terms()),min(a.coeffs()))
v=4*q+x
A,C=p(N,v),p(B,v);check(A);check(C)
v=4*q+4+x
L=p(N,v)*p(B.subs(q,q+1),v)
R=p(N.subs(q,q+1),v)*p(B,v)
G=L-R;check(G);check(s.Poly(v,x,q)*G-R)
v=4*q+x
L=p(N.subs(u,u+1),v)*C
R=A*p(B.subs(u,u+1),v)
G=L-R;check(G);check(s.Poly(v+1,x,q)*G-R)
for u0 in range(22,1000):
    e=200*F(19,20)**u0
    if (1+e)**4<1+F(1,u0+1):break
assert u0==238
@lru_cache(None)
def moments(n):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(n):
        z,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3))
        assert not r
        a.append(z)
    return a
def counts(u,q):
    d=u-q;m=u+q
    A,a,B,b=(moments(n) for n in (u,u-1,m,m-1))
    def C(a,b,g):
        return sum(a[k]*b[g-k] for k in range(max(0,g-len(b)+1),min(g,len(a)-1)+1)) if g>=0 else 0
    Q=C(A,B,d-1)
    S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1))
    P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
    return P*Q*(3*u+q+1)**2,S*S*(u+2*q+1)
prev=[];qc=uc=0
for U in range(1,u0+1):
    row=[counts(U,Q) for Q in range(U//4+1)]
    for (a,b),(c,d) in zip(row,row[1:]):
        qc+=1;assert a*d>c*b
    for (a,b),(c,d) in zip(prev,row):
        uc+=1;assert a*d<c*b
    prev=row
assert (qc,uc)==(7021,7199)
print(qc,uc)
```

Actual original run outputs: N,B 54,63 minima 192,36; q G 189 min 93312; q certificate 209 min 93312; u G 187 min 46656; u certificate 204 min 132192; threshold 238; finite checks 7021,7199 bad [] []. Reproduction uses identical expressions with assertions. No external numerical data.

## Next

Seek exact adjacent moment-ratio transport beyond 4q<=u, especially the central belt between quarter-strip and HB diagonal strips. One alternative is a paid multi-image corridor extension beyond the four-image region, retaining the additional images with their actual branch weights, or proving the corresponding combined P*Q/S^2 inequality without separate P/S monotonicity (HC supplies counterexamples to the latter). Do not repeat HH's full sign classification or the now completed quarter-strip comparisons. Independent review of frozen dependencies remains appropriate.
