# R284HK — Moving-diagonal-band monotonicity and drift-adaptive BRC residual payment

2026-11-25. Author proof plus exact coefficient certificate, NOT_REVIEWED. Auxiliary binary-tag word-count observer; no new native physical attribution. Own registration r1-20261124-0256-r284gd-session-v1, own recovery r1-20261125-0901-own-recovery: same open MCP-8cd6c4fa26b9459d923ff73ba0082220, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4, no runs. Owner read r1-20261125-0901-owner-read RUNNING/error=null at last pre-publication observation; independent research without shared CLAIM. Current GK entry snapshot ba133846f01f0a0224e2aea4b72bb53be8337654, current EM control 5c489fc73fef7d1fe5b4545bc6c393ce7cc0ac77; P000 V5, ACTIVE worldview, joint relation and residual contracts read. Scientific dependencies frozen: HJ c1588db28b5160d50260477b82ee7c866e1b6712:research_notes/portable_direct/R284HJ_ONE_THIRD_STRIP_PAID_MULTI_IMAGE_MONOTONICITY_20261125.md; HE 0e4f8d4318f145100959ca9ec3f41c0e219090d5:research_notes/portable_direct/R284HE_EXPONENTIAL_PORT_STRIP_AND_EVENTUAL_EXACT_ROUNDING_20261125.md; HA/HH as pinned in HJ/HE. Conditional on their original safe-word corridor and exact moment identities. The theorem and its certificate extend HJ, not a repeat of finite sign classification.

## Theorem

Write d=u-q, H=u+2q+1, J=3u+q, K=PQ(J+1)^2/(S^2 H) as in the frozen sources. Let the moving region be u>=16, 0<=q<u, d^2>=256*u*log(u) (natural logarithm). For any two adjacent integer parameters in this region,
- K(q,u)>K(q+1,u) in the q direction;
- K(q,u+1)>K(q,u) in the u direction.

In particular every fixed fractional band q<=alpha*u, 0<alpha<1, has both strict monotonicities for all sufficiently large u (both endpoints in the band). This moving region is stronger than any single fixed fractional band. The excluded near-diagonal width is O(sqrt(u log u)), not a fixed fraction of u. HJ's all-budget one-third region and HB's fixed diagonal strips remain separate complementary results.

## 1. Corridor cut without a fixed fractional assumption

Reuse the exact HE corridor with e=A-2q, s=2u+1-(C-2q), t=e-s and h=B-q-s for S=(H,J,H), P=(H-1,J+1,H), Q=(H,J+1,H-1). Then h>=2u, t=1 for S and 0 for P,Q. For q>=1 cut just after the q-th B, with r_cut<=t A's and multiplicity binom(q+r_cut-1,r_cut); every such prefix is safe since b<=q<=u and a<=t. For q=0 cut at initial point. Thus the four post-cut orientations (a,b,x,t) remain (H,3u,1,1), (H-1,3u,0,1), (H-1,3u+1,0,0), (H,3u+1,0,0), with weights 1,q,1,1 respectively. The HE stronger strip has height in [0,W], W=b-a+x+t, period w=W+2. The exact full strip count R and four-term approximation L are the HJ image sum and its j=0,1 terms. The safe count O contains R. Its excluded corners require a forward or reversed segment of length at least u with more A's than B's: e-r_cut>=u and A-q>=u. This is the same corner argument as HE, with the bounds verified for all 0<=q<u. No assumption of zero extra images is made.

For u,d>=8 set n=a+b, p=a/n, r=a/(b+1). From a<=3u-2d+1, 3u<=b<=3u+1, n<=6u+2, b-a>=2d-1, obtain 1/2-p >= d/(8u), 1-r>=d/(2u), and w>=2d+1. In particular r<1 and the drift now explicitly depends on d.

## 2. Drift-adaptive residual payments

For the signed image tail, C(n,a-k)/C(n,a)<=r^k (k>=0, out-of-support count zero). As in HJ, for j<=-1 both indices are <=a-|j|w; for j>=2 use complement indices <=a-(j-1)w. Hence |R-L|/C(n,a)<=4*r^w/(1-r^w). Since r^w<=exp(-d^2/u), when d^2>=u this is <=8 exp(-d^2/u).

For the positive corner mass, in a uniformly shuffled post-cut word the number X of A's in a segment of length l has factorial-product bound E[z^X]<=(1-p+pz)^l for z>=1, by expansion of product(1+(z-1)indicator_A) and sampling-without-replacement probabilities <=p^j. Optimize at z=(1-p)/p>1 instead of the fixed z=2: Pr(X>l/2)<=(2 sqrt(p(1-p)))^l <= exp(-d^2*l/(32*u^2)). Union over forward and reversed lengths l>=u. Put beta=d^2/(32*u^2)<=1. Since 1-exp(-beta)>=beta/2,
0<= (O-R)/C(n,a) <=128*u^2/d^2 * exp(-d^2/(32*u)).
These two residuals are separately retained.

Pay against L, not the total unrestricted count. With R_k=product_{i=0..k-1}(a-i)/(b+i+1), T=L/C(n,a)=1-R_(x+1)-R_(t+1)+R_(x+t+2). Each factor r_i=(a-i)/(b+i+1) lies in [0,r] for 0<=i<=3; r-r_i=i(1+r)/(b+i+1). Telescoping products, 0<=r^k-R_k<=k(k-1)(1+r)/(2(b+1)) for k<=4. Thus
T >= (1-r^(x+1))(1-r^(t+1)) - 6(1+r)/(b+1)
  >= d^2/(4*u^2)-4/u >= d^2/(8*u^2) when d^2>=32*u.
Consequently (u,d>=8, d^2>=32*u)
|O-L|/L <=1088*u^4/d^4 * exp(-d^2/(32*u)).
Positive cut weights transfer this same relative payment to S,P,Q against S0,P0,Q0. This is a BRC total-count approximation with two explicitly paid error types; other joint path observers are not collapsed. Let eps denote the bound. If eps<1, K0*((1-eps)/(1+eps))^2 <= K <= K0*((1+eps)/(1-eps))^2, K0 the HE/HJ four-term rational quotient.

## 3. Parabolic-coordinate polynomial positivity

Use frozen HJ N,B in the d,q coordinates u=d+q. Define A=N B_q-N_q B (derivatives at fixed original u) and C=N_u B-N B_u (fixed q). Certify N,B,(q+3)A-NB,(u+1)C-NB strictly positive for real d>=8, q>=0, d^2>=8q. Unlike the earlier fixed fractional substitution, some coefficients are negative. For each negative monomial -v*d^i*q^j allocate to one positive monomial a*d^h*q^k with k<=j, h>=i+2(j-k), and distinct powers. Since q<=d^2/8 and d>=8,
d^i*q^j <= d^h*q^k / 8^(h-i-(j-k)).
This holds also at q=0 directly as a monomial inequality. Choose the eligible positive monomial maximizing (h-i-(j-k), positive coefficient), with ties resolved by the deterministic Poly.terms order. For each allocated positive monomial require sum(v/8^exponent)<its coefficient. All unallocated positive terms stay intact. At least one positive monomial has k=0, so the resulting lower bound is strict even for q=0.

Executed exact SymPy/Fraction certificate:
polynomial | positive terms | negative terms | receiving groups | maximum spent fraction
N | 31 | 17 | 5 | 3/8
B | 42 | 14 | 4 | 93597/131072
(q+3)A-NB | 154 | 33 | 5 | 1069/1536
(u+1)C-NB | 152 | 32 | 5 | 137/256
All 96 negative monomials are paid, all 19 groups strictly under budget. Thus -partial_q log K0>1/(q+3) and partial_u log K0>1/(u+1) on this parabolic region. This is a reusable positive-coefficient allocation certificate for anisotropic polynomial domains, without requiring every original coefficient positive.

## 4. Transfer to exact integer K

For endpoints in the moving region, d^2>=256*u*log(u) implies all bounds in Sections 2 and 3. Along a real q interval at fixed u, the minimum d is at the larger q; along a real u interval at fixed q, d increases and d^2>=8q remains true. Integrate only the smooth rational surrogate, yielding strict gaps K0(q,u)/K0(q+1,u)>(q+4)/(q+3) and K0(q,u+1)/K0(q,u)>(u+2)/(u+1). Both exceed or equal 1+1/(u+1) as lower bounds because d>=2.

At each endpoint in the moving region, eps<=1088*u^-6 (use d^2>=u and exponential factor <=u^-8). For a pair use the smaller u, so relative endpoint payment factor <=((1+eps)/(1-eps))^4. For eps<=1/100, the identity ((1+eps)/(1-eps))^4-1=8eps(1+eps^2)/(1-eps)^4<10eps holds. For u>=16, eps<=1088/16^6<1/100 and 10880/u^6<1/(u+1). Thus paid endpoint gap is smaller than the certified surrogate gap, proving the strict inequalities for original K. No finite scan is needed for this moving-band theorem; the region may be empty for small u. For a fixed alpha<1, d^2/u >= (1-alpha)^2 u eventually exceeds 256 log u, proving the stated corollary. For the u direction the moving criterion at the smaller u implies it at the next u, because (u-q)^2/(u log u) is increasing for u>=16 at fixed q>=0.

## Reproduction (executed exact integer and rational certificates)

```python
import sympy as s
from fractions import Fraction as F
from math import comb
u,q,d=s.symbols('u q d');D=u-q
N=2*(3*u+4)**2*(q+2*u+1)*(q+3*u+1)**2*(2*D*D-5*q+2*u)*(2*D*D-7*q+4*u+3)
z=12*q**4*u+24*q**4-18*q**3*u**2-44*q**3*u-56*q**3-33*q*q*u*u-111*q*q*u-54*q*q+6*q*u**4-6*q*u**3-63*q*u*u-55*q*u-10*q+32*u**4+104*u**3+124*u*u+64*u+12
n=s.Poly(N.subs(u,d+q),d,q); b=s.Poly(z.subs(u,d+q),d,q)**2
a=n*(b.diff(q)-b.diff(d))-(n.diff(q)-n.diff(d))*b
c=n.diff(d)*b-n*b.diff(d)
for name,p in [('N',n),('B',b),('A',s.Poly(q+3,d,q)*a-n*b),('C',s.Poly(d+q+1,d,q)*c-n*b)]:
    pos={m:int(v) for m,v in p.terms() if v>0};neg={m:-int(v) for m,v in p.terms() if v<0};alloc={}
    for (i,j),v in neg.items():
        cand=[(h,k) for h,k in pos if k<=j and h>=i+2*(j-k)]
        h,k=max(cand,key=lambda m:(m[0]-i-(j-m[1]),pos[m]))
        exponent=h-i-(j-k)
        assert exponent>=1
        alloc.setdefault((h,k),[]).append((v,exponent))
    assert any(k==0 for h,k in pos)
    for m,g in alloc.items():assert sum(F(v,8**e) for v,e in g)<pos[m]
    print(name,len(pos),len(neg),len(alloc),max((sum(F(v,8**e) for v,e in g)/pos[m] for m,g in alloc.items()),default=0))

def moments(n,g):
    out=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        out.append(out[-1]*(k+2)*(n-k)//((k+1)*(n+k+3)) if k<n else 0)
    return out

def counts(u,q):
    d=u-q;m=u+q;g=d+1
    A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
    def C(a,b,g):return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0
    Q=C(A,B,d-1);S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1))
    P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
    return S,P,Q

def K(u,q):
    S,P,Q=counts(u,q)
    return F(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))

def K0(u,q):
    H=u+2*q+1; D=H+3*u
    def T(a,b,x,t):
        def R(k):
            p=F(1)
            for j in range(k):p*=F(a-j,b+j+1)
            return p
        return 1-R(x+1)-R(t+1)+R(x+t+2)
    S=T(H,3*u,1,1)+q*F(H,D)*T(H-1,3*u,0,1)
    P=F(H,3*u+1)*T(H-1,3*u+1,0,0)
    Q=F(D+1,3*u+1)*T(H,3*u+1,0,0)
    return P*Q*F((3*u+q+1)**2,H)/S**2
for U,Q in [(256,128),(512,384),(1024,768),(4096,1100),(8192,3700)]:
    k=K(U,Q);kq=K(U,Q+1);ku=K(U+1,Q);r=K0(U,Q)
    assert k>kq and ku>k
    assert r==F(int(n.eval({d:U-Q,q:Q})),int(b.eval({d:U-Q,q:Q})))
    print('exact',U,Q,'qgap',float(k/kq-1),'ugap',float(ku/k-1),'relerr',float(abs(k/r-1)))
```
Executed output:
N 31 17 5 3/8
B 42 14 4 93597/131072
A 154 33 5 1069/1536
C 152 32 5 137/256
exact 256 128 qgap 0.019271294899939347 ugap 0.005953240745623922 relerr 3.269155708838959e-12
exact 512 384 qgap 0.006605266464700091 ugap 0.003048154763478647 relerr 5.907941821669011e-07
exact 1024 768 qgap 0.0032955412650379 ugap 0.0015069977517374344 relerr 2.4539439042643475e-10
exact 4096 1100 qgap 0.0021898439540022313 ugap 0.0003456336130277992 relerr 0.0
exact 8192 3700 qgap 0.0006760603127244013 ugap 0.00018352554581465546 relerr 2e-322
The 0.0 is float underflow in display, not an equality assertion. Five independent base samples, 15 exact K calculations, 10 strict integer comparisons and 5 rational-expression crosschecks, all passed. Samples outside the moving-band hypotheses are only observations; no extrapolation from them is used in the theorem.

## Next

The unresolved region for all-budget q monotonicity is now primarily d=O(sqrt(u log u)) beyond HB's fixed d strips plus the finite complement of HJ/HK. The exponential residual scale d^2/u connects directly to GZ's joint-deficit critical scale d~sqrt(u). Seek an exact moment transport comparison across this scale, or a sharper local correlated payment of adjacent residuals (rather than paying each endpoint independently). Do not repeat all-budget sign classification or fixed-fraction strip proofs. The independent proof review and Activity observation audit remain separate.
