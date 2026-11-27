# R284JH — Removable exterior pole at r=2 and half-window second-branch positivity
2026-11-27. Author proof and exact replay; NOT_REVIEWED. Independent continuation of own directed auxiliary binary-tag joint observer (no native spatial transfer), RA-B82240E8488EF5A1DA5186C4, recovered original researcher EM-DIRECT-0C386E / TASK_RESEARCH, own session has no runs. Owner inventory r1-20261127-1003-owner RUNNING at last observation; no shared Task claim or owner changes. P000 V5, ACTIVE worldview, joint relation and residual-fidelity contracts consulted.
Frozen input: c7853ca73cbf8d3c4e85fd3810293d63a485c000:research_notes/portable_direct/R284JG_SECOND_BRANCH_GROWING_OFFSET_CERTIFICATES_20261127.md (JG, full exact read). JG defines the full original observer and proves reduction for 3<=r<d and positivity for 3<=r<=d/10. We retain all original inputs and E for higher jets. New results below are author proof, not independent review.

## 1. Repair the r=2 coupled coordinate
Use JG's notation: q>=64, d>=3, d^2<=4q, u=q+d, m=2q+d, R_n(k)=prod_{i<k}(n-i)/(n+i+3), l=d-k. a=(k+1)(l+1)R_u(k)R_m(l), b=(k+1)l R_u(k)R_m(l-1) (zero for l=0); v=(u-k)(u+k+2)/(2u(2u+1)), V=sum a, Q=sum b, A=sum v(a+b), E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/(2u(2u+1)(4m+2)). Z=qA+Q+V, W=A+E, Y=q(4q+3d+1)^2 WQ/[(3q+d+1)Z^2], C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2. Z>0 in the primal domain by JG/JB.

Take r=2, N=2u, j=d-2, T=R_m(j), p|u, p>2d+1 prime, t=v_p(u). At q0=-d, u0=0, m0=-d, the denominator at index j-1 of R_m is 2u. All other second-branch factors are p-units: their formal nonzero integers have absolute value <=2d+1. Thus v_p(T)=-t. R_m(j+h)/T reduces to c_h=(-1)^h binom(2j+h+1,h) for h>=0; earlier positions reduce to zero.

The apparent exterior pole 1/u is removable in the complete weighted fiber, not in v alone. Define U_k=R_u(k), B_k=v_k U_k on the primal domain; exact rational identities B_0=(u+2)/(2(2u+1)), B_{k+1}=B_k (u-k-1)/(u+k+2). These are regular at u=0, and at u0=0 give U_0=1, U_k=0 (k>=1), B_k=(-1)^k/(k+1). E is regular because R_u(d)/u is regular (d>=1); its other exterior factors 2u+1,4m+2 are units at p>2d+1 (4m+2=-2(2d-1) formally). All U/B denominators have formal nonzero factors <=d+2<=2d+1. Thus E/T vanishes mod p but no higher-jet erasure is claimed. In particular the naive substitution U_k=0 into v_k U_k for k>=1 is invalid at u=0.

For k=0,1,2 write h=2-k. The reduced fibers are (k+1)(l+1)U_k c_h, (k+1)l U_k c_(h-1), and the A terms use B_k in place of U_k. c_0=1,c_1=-2(d-1),c_2=(d-1)(2d-1). Direct summation yields
V*=A*=(d-1)(d+1)(2d-1), Q*=-2d(d-1), E*=0,
Z*=-(d-1)(2d^3-d^2+1).
The three A summands (including both fibers) are (d+1)c2+d c1, -d c1-(d-1), d-1, so the extra weighted fibers restore A*=V*. Consequently
C/T^2 = G_2(d) mod p,
G_2(d)=2(d-1)^2(2d-1) H(d),
H(d)=64d^6-61d^5+13d^4+61d^3-29d^2+16.
Expansion follows by substituting the above values into 3q0(4q0+3d+1)^2 A*Q* -32(3q0+d+1)Z*^2. H>0 for d>=3: group 64d^6-61d^5 and 61d^3-29d^2, both positive. All displayed prefactors are p-units. Hence p|q+d, p>2d+1, p not dividing H(d) implies Y!=32/3. This fills r=2 (JG excluded it), with lower prime threshold than JG's generic family. H<128d^6 for d>=3, so at most six distinct p>2d+1 divide H: seven such primes have product >(2d)^7>=128d^6. For fixed d, any exceptional prime accounts for O(1) q in any interval of length O(d). Also if Z*=0 mod p, A*,Q*,q0,4q0+3d+1 are units, so G_2 is nonzero; the denominator cancellation cannot hide equality. r=1 remains JA's different coupled pole.
The observer scope of this compression is first-layer normalized residues V,Q,A,E,Z,C. The original observer, all positions, and E are retained as provenance for higher jets.

## 2. Extend JG's second-branch positivity from d/10 to d/2
Theorem: for d>=6, 3<=r<=floor(d/2), JG's reduced V*, Q*, A* have signs (-1)^r, (-1)^(r-1), (-1)^r respectively, and G2_r(d)>0. Retain JG's congruence hypothesis p>4d+6 (no change). Let j=d-r, u0=(r-2)/2, q0=u0-d, c_h=(-1)^h binom(2j+h+1,h), U_k=R_u0(k), B_k=v*_k U_k. Use the two recurrences from JG, including their exact zero-safe product form. Let x=r/(2d-r+1)<1/3. For h<=r, |c_(h-1)/c_h|<=x. The V,Q term absolute ratios are at most ((k+2)/(k+1)) x times |U_(k+1)/U_k|, when the predecessor is nonzero. In particular <2/3, and zero tails persist for even r. For A combine the two fibers at each k BEFORE bounding their mass:
A_k=B_k (k+1)(l+1)c_h f_k,
f_k=1-[l/(l+1)] h/(2j+h+1), including f_r=1. Then 1-x<=f_k<=1 and A_k has sign B_k times (-1)^h. Its successive absolute ratio is <=((k+2)/(k+1)) x/(1-x) times |B_(k+1)/B_k|, hence <1, and for k>=1 is <3/4. These bounds retain the actual signed combined mass; we do not replace joint state by absolute mass.

For even r=2a, u0=a-1 integer. U_k positive up to k=a-1 then zero. B_k positive up to k=a-2 then zero (r>=4); both follow the recurrences. Each signed sum is a strictly decreasing alternating sequence up to its zero tail, so the sign is that of the first term by adjacent pairs.

For odd r=2a+1, a>=1, u0=a-1/2. U_k positive through k=a, then changes sign at every step. Thus relative to the first term, the V,Q sequences alternate up to k=a, and the tail from k=a onward has constant sign (-1)^a. If a even, the alternating prefix pairs into positive contributions and the tail is positive. If a odd, pair the earlier terms through k=a-2, leaving the positive k=a-1 term and the negative tail. The transition ratio |U_a/U_(a-1)|=(1/2)/(2a+3/2)<=1/7. Therefore the total absolute tail from a onward is at most (2/3)/7 times 1/(1-2/3)=2/7 of the preceding positive term. (Finite Q ends at k=r-1, shortening the same bound.) The sum has the required strict sign.

For A, B_k positive through k=a-1, then changes sign at every step. Relative signs alternate through k=a-1 and are constant (-1)^(a-1) thereafter. If a odd, positive tail and positive paired prefix give the first-term sign, including a=1. If a even, a>=2, negative tail starts k=a-1, preceded by positive k=a-2. Transition ratio |B_(a-1)/B_(a-2)|=(1/2)/(2a-1/2)<=1/7; the A term ratio at that transition is <=1/7, and all subsequent ratios are <3/4 since k>=1. The absolute negative tail is <=4/7 of the preceding positive term. Earlier pairs are positive. This proves strict sign in all cases. Since q0<0, 3q0+d+1<0 and 4q0+3d+1=-d+2r-3<=-3, the first term of G2 is strictly positive (A*Q*<0), the second nonnegative. This proves G2>0 throughout the half-window.

JG's denominator proof Dbar=8(r-2)(r-1)L(3r+2) remains valid for these offsets: it used only the factor ranges and arithmetic-progression counts, not the d/10 restriction. The new absolute ratios also give |V*|,|Q*|<=3 times first magnitudes; |A*|<=sum_{k>=0}(k+1)x^k v0(d+1)|c_r| <=(9/4)v0(d+1)|c_r| (f_k<=1, |B_k|<=B0). Hence G2=O(d^5 c_r^2) and log(2Dbar^2 G2)=O(r log(ed/r)+log d), uniformly on the enlarged range. All prior smaller-window conclusions remain valid; no claim of a smaller double-failure set follows merely from widening.

## 3. Executed exact checks
Python Fraction, math.comb, sympy.primerange. 7744 widened triangle cases d=6..180, r=3..floor(d/2), all three signs and positivity. Three additional cases (d,r)=(1000,500),(10^30,100),(10^60,100), exact G numerator/denominator bit lengths (3356,564),(19658,76),(40109,97). r=2 symbolic closed form checked for d=3..50; 6724 primal crosschecks of all six normalized quantities for p>2d+1, p<400, u in {p,2p,p^2} subject to legal q. 26 zero residues, e.g. (q,d,p)=(271,6,277),(99,7,53),(242,9,251),(147,10,157). Not equality examples. All assertions passed. Unbounded results use the written proof. Replay:
```python
from fractions import Fraction as F
from math import comb
from sympy import primerange

def rr(n,h):
    a=[F(1)]
    for k in range(h): a.append(a[-1]*(n-k)/(n+k+3))
    return a

def reduced(d,r):
    q=F(r-2,2)-d; u=q+d; j=d-r
    c=[(-1)**h*comb(2*j+h+1,h) for h in range(r+1)]
    U=rr(u,r); B=[(u+2)/(2*(2*u+1))]
    for k in range(r): B.append(B[-1]*(u-k-1)/(u+k+2))
    V=Q=A=F(0)
    for k in range(r+1):
        l=d-k; h=r-k
        a=(k+1)*(l+1)*c[h]; b=(k+1)*l*c[h-1] if h else 0
        V+=U[k]*a; Q+=U[k]*b; A+=B[k]*(a+b)
    Z=q*A+Q+V; G=3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
    return V,Q,A,F(0),Z,G

def full(q,d,r):
    q=F(q); u=q+d; m=2*q+d; U=rr(u,d); M=rr(m,d); T=M[d-r]; V=Q=A=F(0)
    for k in range(d+1):
        l=d-k; a=(k+1)*(l+1)*U[k]*M[l]; b=(k+1)*l*U[k]*M[l-1] if l else F(0)
        v=(u-k)*(u+k+2)/(2*u*(2*u+1)); V+=a; Q+=b; A+=v*(a+b)
    E=U[d]*(u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2)/(2*u*(2*u+1)*(4*m+2))
    Z=q*A+Q+V; G=3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
    return V/T,Q/T,A/T,E/T,Z/T,G/T**2

def pol(d): return 64*d**6-61*d**5+13*d**4+61*d**3-29*d**2+16
def mod(a,p): return a.numerator*pow(a.denominator,-1,p)%p

n=0
for d in range(6,181):
    for r in range(3,d//2+1):
        V,Q,A,E,Z,G=reduced(d,r)
        assert (-1)**r*V>0 and (-1)**(r-1)*Q>0 and (-1)**r*A>0 and G>0
        n+=1
print('widened checks',n)
n=exc=0; examples=[]
for d in range(3,51):
    V,Q,A,E,Z,G=reduced(d,2)
    assert V==A==(d-1)*(d+1)*(2*d-1) and Q==-2*d*(d-1)
    assert Z==-(d-1)*(2*d**3-d**2+1) and G==2*(d-1)**2*(2*d-1)*pol(d)>0
    for p in primerange(2*d+2,400):
        for u in (p,2*p,p*p):
            q=u-d
            if q<64 or d*d>4*q: continue
            a=reduced(d,2); b=full(q,d,2)
            assert [mod(x,p) for x in a]==[mod(x,p) for x in b]
            n+=1
            if mod(G,p)==0:
                exc+=1
                if len(examples)<10: examples.append((q,d,p))
print('r2 crosschecks',n,'zero residues',exc,'examples',examples)
for d,r in [(1000,500),(10**30,100),(10**60,100)]:
    V,Q,A,E,Z,G=reduced(d,r); assert (-1)**r*A>0 and (-1)**(r-1)*Q>0 and G>0
    print('large',d,r,G.numerator.bit_length(),G.denominator.bit_length())
```

## 4. Next question
Use the regularized B_k recurrence for r=2 higher jets and investigate H(d) exceptional primes, particularly simultaneous failure with first-branch coordinates. For enlarged offsets r>d/2, 4q0+3d+1 can vanish at special parameters and the geometric ratio changes; need new sign/cross-residual argument. Do not infer all-budget equality exclusion or inverse-polynomial real separation. No shared task ownership or review disposition changed.
