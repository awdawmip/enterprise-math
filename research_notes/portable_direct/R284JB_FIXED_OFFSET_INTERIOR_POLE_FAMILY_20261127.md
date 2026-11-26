# R284JB — Arbitrary fixed-offset first-branch pole certificate
2026-11-27. Author proof and executed exact finite checks; NOT_REVIEWED. Auxiliary binary-tag joint-count observer, not a native spatial transfer. Frozen input: R284JA at d3f6557d2b9e1438f9165d399a9a7f20c2835d41:research_notes/portable_direct/R284JA_INTERIOR_POLE_PAIR_CERTIFICATES_20261127.md (blob 4ec7225a2966e06876ce7e3852abec848408559c). Own existing activity RA-B82240E8488EF5A1DA5186C4, recovery_status confirms original registered own session, no runs. Owner inventory r1-20261127-0403-owner still RUNNING at last observation before publication; no claim or shared owner mutation. Current P000 V5, ACTIVE worldview, joint observer constraint and portable protocol consulted.

## 1. Original observer
Integers q>=64, 2<=d<=2sqrt(q), u=q+d, m=2q+d, l=d-k. R_n(a)=prod_{i=0}^{a-1}(n-i)/(n+i+3).
a_k=(k+1)(l+1)R_u(k)R_m(l), b_k=(k+1)l R_u(k)R_m(l-1) for l>=1 and zero otherwise, v_k=(u-k)(u+k+2)/(2u(2u+1)).
V=sum a, Q=sum b, A=sum v(a+b),
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/(2u(2u+1)(4m+2)).
W=A+E, Z=qA+Q+V, Y=q(4q+3d+1)^2 WQ/[(3q+d+1)Z^2], F=Y-32/3. Z>0 on the actual domain (JA/IZ).
C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2.

## 2. Exact local compression for every offset 1<=r<d
Set j=d-r, N=q+2d-r+2=u+j+2, T=R_u(j). Suppose prime p|N, p>20d+20, t=v_p(N). Use formal coordinate q0=-2d+r-2, u0=-j-2, m0=-3d+2r-4. The only nonunit among raw R denominators is the factor N at index i=j-1 in the first branch. All raw numerators, other denominators, and the exterior factors 2u,2u+1,4m+2 are units: at q0 their nonzero integer residues have absolute value <=20d+20. In particular m0<=-d-6 (r<=d-1); m0+i+3 never vanishes for i<d. Hence v_p(T)=-t; every branch with k<j has unit first factor, and division by T sends it to zero mod p. For k=j+h (0<=h<=r), l=r-h, the exact tail recurrence gives
c_h = (R_u(j+h)/T)|_{q=q0} = (-1)^h binom(2j+h+1,h).
This is an evaluation of a regular ratio after cancelling the pole, not a substitution into the singular full product.
Define the finite reduced fiber
a_h=(j+h+1)(r-h+1)c_h R_{m0}(r-h),
b_h=(j+h+1)(r-h)c_h R_{m0}(r-h-1) for h<r, else 0,
v_h=(u0-j-h)(u0+j+h+2)/(2u0(2u0+1)).
Let V*=sum a_h, Q*=sum b_h, A*=sum v_h(a_h+b_h),
E*=c_r (u0-d)[(d+1)(u0+d+2)+(d+2)(u0-1-d)](m0+2)/(2u0(2u0+1)(4m0+2)),
Z*=q0 A*+Q*+V*, W*=A*+E*.
Then (V,Q,A,E,Z)/T reduces componentwise to (V*,Q*,A*,E*,Z*) mod p. In particular
C/T^2 = G_r(d) mod p,
G_r(d)=3q0(4q0+3d+1)^2 W*Q*-32(3q0+d+1)(Z*)^2.
If G_r(d) is nonzero mod p, F is nonzero. This remains true when Z* vanishes. No assertion of aggregate valuation beyond this cross-residue is made. The full composite population stays the source; the discarded fibers vanish only under the stated normalized mod-p observer. The reduction uses r+1 terms rather than d+1, with O(r) modular operations for fixed r using recurrence for c and R, and no enumeration of p digits; finding p/factorization is separate.

## 3. Every fixed offset yields an unbounded certificate family
For fixed r>=1, write a=(-2)^r/r!, b=(-2)^(r-1)/(r-1)!. As d tends to infinity:
V*=a d^(r+1)+O_r(d^r), Q*=b d^r+O_r(d^(r-1)),
A*=-(r/2)a d^r+O_r(d^(r-1)), E*=(a/4)d^(r+1)+O_r(d^r),
Z*=(r+1)a d^(r+1)+O_r(d^r).
Proof: each c_h=(-2)^h d^h/h!+O_r(d^(h-1)) (c_0=1), R_m0(l)=1+O_r(1/d); the maximum h=r supplies V's leading term, h=r-1 supplies Q's. v_h=-h/(2d)+O_r(d^-2); the full term h=r supplies A's leading term, all shifted and smaller h terms are lower order. In E the rational prefactor is d/4+O_r(1): its leading numerator is (-2d)(-2d^2)(-3d)=-12d^4, denominator -48d^3. q0=-2d+O_r(1) gives Z. Consequently
G_r(d)=-(75/2)ab d^(2r+4)+O_r(d^(2r+3))
= [75*2^(2r-2)/(r!(r-1)!)] d^(2r+4)+O_r(d^(2r+3)).
In particular G_r is not identically zero and is eventually positive for each fixed r. This proves the existence of only finitely many integer zeros for fixed r (no claim of a uniform onset in r).
For an explicit integer polynomial choose H_r=r! 2u0(2u0+1)(4m0+2) prod_{i=0}^{r-1}(m0+i+3). Each H_r times the reduced observer is in Z[d], because c_h has denominator dividing h!, and all R_{m0} denominators divide the displayed product. Hence P_r=H_r^2 G_r is an integer polynomial of exact degree 4r+10 (degree H_r=r+3 and nonzero leading coefficient). H_r(d) is a p-unit under the hypotheses. For large d the number of distinct exceptional primes p>20d+20 dividing P_r(d) is O_r(1), in fact at most 4r+10 for sufficiently large d since |P_r(d)|=O_r(d^(4r+10)) and (20d+20)^(4r+11) eventually dominates. The same finite-exception conclusion is true using a reduced numerator.
For r=1 the rational expression exactly recovers JA: d^2 P(d)/(2(3d-1)^2).
For r=2 it is
2(5d-1)(810d^10+23787d^9-196056d^8+579513d^7-775044d^6+382794d^5+66068d^4-60672d^3+2432d^2+2304d-256)/[(3d-4)^2(6d-1)].
These special symbolic expansions are supplementary to the general proof.

## 4. Density
For every fixed r>=1 and eventually nondecreasing integer d(q)=s sqrt(q)+O(1), 0<s<2, the certificate event
exists prime p | q+2d(q)-r+2 with p>20d(q)+20 and p not dividing P_r(d(q))
has natural density log 2. Indeed the map q -> q+2d(q)-r+2 is eventually increasing and misses O(sqrt X) integers up to X+O(sqrt X). On [epsilon X,X] threshold is between fixed positive multiples of sqrt X. The large-prime-factor count from JA (Mertens reciprocal-prime estimate and floor-count above sqrt X, then constant-factor threshold squeeze) gives log 2 after epsilon->0. Remove O_r(sqrt X) exceptional q: for each fixed d large there are O_r(1) exceptional primes and q occupies an interval of length O(d) by inversion of the candidate bound; each prime >20d+20 hits O(1) q. Finitely many small d contribute finitely many q. Thus infinitely many distinct affine coordinates now have separately proven density log 2, not a proven increase in their joint union. No independence assumption.

## 5. Executed finite verification
Python Fraction and SymPy. Full-domain crosscheck: d=2..22, r=1..d-1, primes 20d+20<p<850, N in {p,2p,p^2}, q=N-2d+r-2, retain q>=64,d^2<=4q. 55,495 comparisons of all six normalized residues with the full uncompressed source; 99 cases with zero cross-residue mod p; no G_r(d)=0 rationally among tested (d,r). No claim of real equality for the 99 mod-p exceptions. All assertions passed. Symbolic factorizations for r=1,2,3,4 computed. The following executed core reproduces the numeric check (symbolic expansion can be obtained by replacing d with a SymPy symbol and binom with product / factorial).

```python
from fractions import Fraction as F
from math import comb
from sympy import primerange
def residues(d,r):
    j=d-r; q=-2*d+r-2;u=q+d;m=2*q+d
    def R(n,l):
        z=F(1)
        for i in range(l): z*=F(n-i,n+i+3)
        return z
    V=Q=A=F(0)
    for h in range(r+1):
        k=j+h;l=r-h;c=(-1)**h*comb(2*j+h+1,h)
        a=(k+1)*(l+1)*c*R(m,l)
        b=(k+1)*l*c*R(m,l-1) if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=a;Q+=b;A+=v*(a+b)
    E=(-1)**r*comb(2*j+r+1,r)*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V
    C=3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
    return V,Q,A,E,Z,C
def obs(q,d,r):
    u=q+d;m=2*q+d
    def rr(n):
        x=[F(1)]
        for i in range(d):x.append(x[-1]*F(n-i,n+i+3))
        return x
    a,b=rr(u),rr(m);T=a[d-r];V=Q=A=F(0)
    for k in range(d+1):
        l=d-k;w0=(k+1)*(l+1)*a[k]*b[l];w1=(k+1)*l*a[k]*b[l-1] if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1));V+=w0;Q+=w1;A+=v*(w0+w1)
    E=a[d]*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V;C=3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
    return V/T,Q/T,A/T,E/T,Z/T,C/T**2
def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p
count=exception=0;zero=[]
for d in range(2,23):
    for r in range(1,d):
        a=residues(d,r)
        if not a[-1]:zero.append((d,r))
        for p in primerange(20*d+21,850):
            for N in (p,2*p,p*p):
                q=N-2*d+r-2
                if q<64 or d*d>4*q:continue
                b=obs(q,d,r)
                assert [mod(x,p) for x in a]==[mod(x,p) for x in b]
                if mod(a[-1],p):assert b[-1]
                else:exception+=1
                count+=1
assert (count,exception,zero)==(55495,99,[])
print(count,exception,zero)
```

Next: prove uniform bounds as r grows with d (not obtained by the fixed-r asymptotic), classify second-branch offsets including exterior-coupled and numerator-zero cases, and study correlation/coverage of the resulting consecutive affine coordinates. Exact equality exclusion on all budgets and real inverse-polynomial separation remain open. No formal result or review claimed.
