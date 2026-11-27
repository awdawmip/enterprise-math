# R284JF — Offset-adaptive joint denominator height and local exception budget
2026-11-27. Author proof and executed exact rational checks; NOT_REVIEWED. Auxiliary binary-tag joint-count observer; no native spatial transfer, formal Task/Result/Review or shared owner mutation. Continuation of the existing direct line RA-B82240E8488EF5A1DA5186C4. Original own session metadata recovered, no runs. Current owner inventory r1-20261127-0800-owner RUNNING at last prepublication observation; prior r1-20261127-0700-owner SUCCEEDED with no LEASED entries as of 2026-11-26T23:02:44Z. P000 V5, ACTIVE worldview and joint observer contract read. Frozen inputs:
- JE a43a497a2b7872dc73b4b960bae5c68334abaf60:research_notes/portable_direct/R284JE_DETERMINISTIC_WINDOW_WITNESSES_20261127.md, sections 1–3.
- JD 673771a11b75db41a98bbaaebba8305fe8f28e30:research_notes/portable_direct/R284JD_DENSITY_ONE_COMMON_CERTIFICATES_20261127.md, blob 7860e972da93f5b90594287214998f875c176a14.
- JC f4abd4b538f733777dc34f187b5236916806a72c:research_notes/portable_direct/R284JC_UNIFORM_GROWING_OFFSET_CERTIFICATES_20261127.md, blob d1ff271ebe73d9ec1f1509eea29459d1b128efa7.
- JB e92de4ef4680b68015e53c4c702fbf929dada0a0:research_notes/portable_direct/R284JB_FIXED_OFFSET_INTERIOR_POLE_FAMILY_20261127.md, blob 9ac16b9644637a8416a050c701568463acb70248.
The full joint observer and endpoint residual E are retained. Natural logs are derived height readouts. No new external analytic theorem is needed.

## 1. Offset-adaptive integerization theorem
Let d>=10, 1<=r<=floor(d/10), j=d-r, q0=-2d+r-2, u0=q0+d, m0=2q0+d=-M, n=M-3=3d-2r+1. Use precisely JB/JC's normalized fiber: R_m(l)=prod_(i=0..l-1)(m-i)/(m+i+3), c_h=(-1)^h binom(2j+h+1,h), k=j+h, l=r-h, a_h=(k+1)(l+1)c_h R_m0(l), b_h=(k+1)l c_h R_m0(l-1) (zero for l=0), v_h=(u0-k)(u0+k+2)/(2u0(2u0+1)). Set V*=sum a_h, Q*=sum b_h, A*=sum v_h(a_h+b_h). Retain E*=c_r (u0-d)[(d+1)(u0+d+2)+(d+2)(u0-1-d)](m0+2)/[2u0(2u0+1)(4m0+2)], W*=A*+E*, Z*=q0 A*+Q*+V*. The full cross-residue is G=3q0(4q0+3d+1)^2 W*Q*-32(3q0+d+1)(Z*)^2.

Define L_r=lcm_{0<=l<=r} binom(r,l), C_r=binom(n,r), ext=|2u0(2u0+1)(4m0+2)| and D_r=ext C_r L_r. Then D_r clears all six rational observers V*,Q*,A*,E*,W*,Z*, and P_r=D_r^2 G is a positive integer. Every prime >20d+20 is a unit in D_r. Moreover
log P_r = O(r log(ed/r) + log d)
uniformly on the whole triangle. Consequently the number of distinct exceptional primes >20d+20 dividing the reduced numerator of G is
O(1 + r log(ed/r)/log d).

Proof. JD gave R_{-M}(l)=binom(M+l-1,l)/binom(n,l). The exact nested binomial identity
binom(n,r) binom(r,l)=binom(n,l) binom(n-l,r-l)
shows that each denominator divides C_r L_r, not just the full L(n). The external observer and E denominators divide ext; all c_h are integers. JC proves G>0. All prime divisors of C_r L_r and ext are <=20d+20, so replacing the denominator preserves the exceptional-prime set under the JB cross-residue observer. In particular no denominator factor can introduce a false exceptional large prime. Further L_r divides lcm(1,...,r) by Legendre carry bounds; log L_r=O(r) by the elementary Chebyshev bound (as in JD/JE). Also C_r<= (en/r)^r. Thus log D_r=O(log d + r log(ed/r)).
For the numerator use JC's explicit mass estimates: |A*|<=d|c_r|/10, |E*|<=d|c_r|, |V*|+|Q*|<=1.5d|c_r|, |Q*|<=d|c_r|. These imply |W*|<=2d|c_r|, |Z*|<=d^2|c_r|. Since |q0|<=3d, |4q0+3d+1|<=6d and |3q0+d+1|<=9d, we obtain 0<G<=936 d^5 c_r^2 <1000 d^5 c_r^2. With |c_r|=binom(2d-r+1,r)<=(e(2d+1)/r)^r the claimed logarithmic bound follows. Each exceptional prime contributes >log(20d+20) to log P_r. The new denominator even divides JC's product denominator: L_r|r! and C_r r!=n(n-1)...(n-r+1). One may additionally take gcd with JD's ext*lcm(1,...,n) (both clear all observers). This preserves exact rational reconstruction for the same six outputs; the original joint fibers remain the source for other observers. This is not a complexity bound for factor discovery.

## 2. Strengthened common-window theorem
Fix 0<s<2, X large, d0=floor(s sqrt(q)), q in [X,2X]. Let k>=0 integer, |d-d0|<=k. As in JE take R=floor(C0 sqrt(X)/log X), C0 a sufficiently large absolute constant, k<=R/8. Common coordinates N=q+2d0-r+2, 2k+1<=r<=R-2k, form H=R-4k>=R/2 consecutive integers. Each represents r_d=r+2(d-d0) in [1,R] and R<=d/10 for large X. B=ceil(100 sqrt X) exceeds 20d+20 and sqrt(max N). JE's deterministic binomial window lemma gives >=H/3 coordinates with p=P+(N)>B in EVERY window at sufficiently large X.

For fixed d,r_d, the admissible q form a subset of an interval of length O_s((k+1)sqrt X) by inversion of d0, and each exceptional prime >B hits O_s(k+1) q. There are O_s(sqrt X) different d. By section 1, summing r_d<=R yields at most
O_s((k+1)sqrt X [R+R^2 log(e sqrt X/R)/log X])
exceptional triples (q,d,r_d). Indeed r log(ed/r) is increasing for r<=d, and d is comparable to sqrt X, so the sum is bounded by R^2 log(e d/R) up to a uniform constant. Charge each spoiled common coordinate to a failing d; distinct coordinates at a fixed q give distinct triples. Divide the triple bound by H/6. Except
O_s((k+1)sqrt X [1+R log(e sqrt X/R)/log X])
budgets, every window has >=H/6 surviving common witnesses. Substituting R=Theta(sqrt X/log X) gives the sharper exception bound
O_s((k+1) X log log X/(log X)^2).
Each surviving witness proves Y(q,d)!=32/3 simultaneously for the entire band via JB. This strengthens JE's O_s((k+1)X/log X), using the same deterministic supply and shorter window. For fixed k, dyadic summation gives the same improved bound for possible equality budgets <=X. Density-one simultaneous certification now permits k=o((log X)^2/log log X). For example k=floor((log X)^(3/2)) is allowed and the exception bound becomes O_s(X log log X/sqrt(log X)). The underlying raw supply remains deterministic; the surviving certificate count retains a zero-density exception set.

## 3. Local fiber sharpening
For one fixed d and any interval of legal q with length O(d), take R=floor(C d/log d) and the offsets 1..R, with q comparable to d^2. Choose C sufficiently large for the comparability constants and B a suitable constant times d, exceeding 20d+20 and sqrt(max N). JE supplies >=R/3 raw witnesses in each q-window. Each exceptional prime hits O(1) q in the fixed interval. The same incidence argument now needs no sum over d, so all but O(1+R log(ed/R)/log d)=O(d log log d/(log d)^2) of these q have >=R/6 valid witnesses. This is a per-d uniform local bound, not just a global average. It leaves unresolved the pointwise simultaneous exceptional divisibility across r for a particular q.

## 4. Executed exact checks
Python Fraction, integer binomial and lcm. Exhaustive d=10..200, 1<=r<=floor(d/10): 1920 checks; six additional cases. Verified exact JD ratio identity, nested denominator divisibility, L_r divisibility, joint integerization of all six outputs, positive integer cross-residue and the explicit height inequality, division of JC product denominator, and optional gcd with JD denominator. Output columns are JC D bits, new D bits, JC P bits, new P bits, and when computed JD D bits, gcd D bits, gcd P bits.
1000 100 [1178, 789, 3528, 2750, 4107, 777, 2727]
10000 1000 [14793, 7691, 40944, 26741, 40453, 7209, 25777]
100000 100 [1875, 1486, 6300, 5521, 432101, 1486, 5521]
1000000 500 [10824, 7771, 35136, 29031]
10^30 40 [4355, 4248, 16852, 16638]
10^60 60 [12658, 12469, 49617, 49238]
All assertions passed. This was not a rerun of JE's raw window enumeration or the JB full primal observer. The asymptotic exception theorem is analytic. Executed code:
```python
from fractions import Fraction as F
from math import comb, lcm, prod, gcd

def check(d,r,linear=True):
    j=d-r; q=-2*d+r-2; u=q+d; m=2*q+d; n=-m-3
    R=[F(1)]
    for l in range(r):
        R.append(R[-1]*F(m-l,m+l+3))
    V=Q=A=F(0)
    for h in range(r+1):
        k=j+h; l=r-h; c=(-1)**h*comb(2*j+h+1,h)
        a=(k+1)*(l+1)*c*R[l]
        b=(k+1)*l*c*R[l-1] if l else F(0)
        v=F((u-k)*(u+k+2),2*u*(2*u+1))
        V+=a; Q+=b; A+=v*(a+b)
    c=(-1)**r*comb(2*j+r+1,r)
    E=c*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V; W=A+E
    G=3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
    ext=abs(2*u*(2*u+1)*(4*m+2)); L=lcm(*(comb(r,l) for l in range(r+1)))
    C=comb(n,r); D=ext*C*L
    assert lcm(*range(1,r+1))%L==0
    for l in range(r+1):
        assert R[l]==F(comb(-m+l-1,l),comb(n,l))
        assert C*comb(r,l)%comb(n,l)==0
        assert C*L%R[l].denominator==0
    assert all((D*x).denominator==1 for x in (V,Q,A,E,Z,W))
    P=D**2*G
    assert P.denominator==1 and 0<P<=1000*d**5*D**2*c*c
    old=ext*prod(abs(m+l+3) for l in range(r))
    assert all((old*x).denominator==1 for x in (V,Q,A,E,Z,W))
    assert old%D==0 # C*L divides falling product since L|r!
    out=[old.bit_length(), D.bit_length(), int(old**2*G).bit_length(), int(P).bit_length()]
    if linear:
        long=ext*lcm(*range(1,n+1))
        assert all((long*x).denominator==1 for x in (V,Q,A,E,Z,W))
        hybrid=gcd(D,long)
        assert all((hybrid*x).denominator==1 for x in (V,Q,A,E,Z,W))
        out += [long.bit_length(), hybrid.bit_length(), int(hybrid**2*G).bit_length()]
    return out

if __name__=='__main__':
    count=0
    for d in range(10,201):
        for r in range(1,d//10+1):
            check(d,r);count+=1
    print('exhaustive',count)
    for d,r in [(1000,100),(10000,1000),(100000,100),(10**6,500),(10**30,40),(10**60,60)]:
        print(d,r,check(d,r,linear=d<=100000))
```
Next: pointwise cross-offset divisibility or complementary second-branch certificates for the remaining q. An exact height-only bound still does not control simultaneous exceptional divisibility at one specific q; no all-budget exclusion or real inverse-polynomial gap is claimed.
