# R284IG — Variable-level linear-budget inversion and rational-slope nonresonance

2026-11-26. Author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer K, not native physical attribution. Own independent continuation of IF (no shared CLAIM, Result or Review mutation). Original own session recovery r1-20261126-0700-own-recovery returned open registration SUCCEEDED, no runs; RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Prior owner read r1-20261126-0606-owner-read now SUCCEEDED, as_of 2026-11-25T22:05:39.622831Z, LEASED list empty at that snapshot; fresh r1-20261126-0700-owner-read last observed RUNNING. Current global main entry blobs verified at fefcd9811ac68061dced817d28c3de9acbdb1be9; project P000 V5, ACTIVE worldview, joint preservation, portable and continuation rules read. Frozen science:
- IF @7302f8a70a9f55075cc495942fc767e2cae0040b:research_notes/portable_direct/R284IF_EFFECTIVE_RATIONAL_LEVEL_AND_SHARP_9_2_ONSET_20261126.md
- HW @8c3bad026fc69c3a685218fc4677433a48310256:research_notes/portable_direct/R284HW_UNIFORM_WEDGE_RESIDUAL_PAYMENT_20261125.md
- HX @1aebe9404d585d9573188649d124a802181131f3:research_notes/portable_direct/R284HX_PARABOLIC_BASELINE_AND_LOGARITHMIC_RESIDUAL_20261125.md
- ID @000fb8cf43bf42509bcb2b90e65fdbb5edc95ca8 through IF (minimum-budget implication conditional on ID author monotonicity).

## Theorem — a different scaling regime

For any fixed rational slope t=a/b>1, gcd(a,b)=1, set the variable target level c(q)=F(t)/q where

F(t)=2(2t+1)(3t+1)^2/(t+2)^2,
B(t)=(192t^5+193t^4-97t^3-126t^2-46t-8)/(6t(t-1)(3t^2+17t+7)).

For all sufficiently large positive integer q, with P=tq+B(t),

K(q,floor(P)) < F(t)/q < K(q,floor(P)+1).

Hence conditional on ID, u_min= floor(tq+B(t))+1. This genuinely uses the linear regime, not the fixed-level quadratic approximation with c replaced by F(t)/q. Explicit examples with sufficient q>=10000 are t=3/2,2,3 (targets 968/(49q),245/(8q),56/q and offsets B=27955/2826,1963/159,5839/306 respectively).

Proof: use HW/HX's rational baseline K0=N/D with the four positive true-count residuals retained in the sandwich. At u=tq+w, the leading degrees of N,D in q are 9,10. Their leading coefficients are 72t^2(t-1)^4(2t+1)(3t+1)^2 and 36t^2(t-1)^4(t+2)^2. Exact coefficient extraction gives

q K0(q,tq+w)=F(t)+F'(t)(w-B(t))/q+O_t,w(q^-2),
F'(t)=4(3t+1)(3t^2+17t+7)/(t+2)^3>0.

For w in any fixed bounded set the rational expansion has uniform remainder. In particular at the finitely many offsets from the rational lattice floor(P)-tq and floor(P)+1-tq, the leading signed gap is nonzero by the nonresonance lemma below. Thus qK0 brackets F(t), with margin at least a positive constant (depending on t) times 1/q. For t>1, d=u-q=(t-1)q+O_t(1) and u=tq+O_t(1). HX's paid residual delta=34u^2/d^2 exp(-d^2/(25u)) is O_t(exp(-k_t q)) for some k_t>0; its hypotheses hold eventually, and (1+delta)^(-2)<=K/K0<=(1+2delta)(1+delta). Multiplying by q transfers both signs. No real extension of the exact combinatorial K is used.

## Rational-slope nonresonance lemma

For every rational t=a/b>1 in lowest terms, tq+B(t) is never integral at any integer q. Indeed bB(t)=J/[6a(a-b)(3a^2+17ab+7b^2)], where J=192a^5+193a^4 b-97a^3 b^2-126a^2 b^3-46ab^4-8b^5. Integrality of tq+B forces bB integer, hence a divides J and a divides 8b^5. Coprimality forces a|8. Since a>b>=1, only a=2,4,8 are possible, with seven coprime pairs. The exact bB values in slope order 2,4,4/3,8,8/3,8/5,8/7 are 1963/159,1100/41,1814/63,175597/2814,110647/2210,35831/698,700955/8922. None is integral. Thus no rational slope resonance, unlike fixed-level IF. The lattice gap to the nearest integer across all q is dist(bB,Z)/b>0; this follows since multiplication by a permutes residues mod b. This supplies a sharper exact gap than a crude denominator.

## Higher correction: sign transition

The local real root of q K0(q,u)=F(t) for fixed real t>1 has expansion u=tq+B(t)+T(t)/q+O_t(q^-2), by the rational function implicit equation in (1/q,u/q) and F'(t)>0. The coefficient is

T(t)=(2t+1)(3t+1)H(t)/(72t^3(t-1)^3(3t^2+17t+7)^3),

H(t)=9216t^11+109920t^10-143880t^9-295914t^8+141793t^7+284879t^6-27648t^5-95924t^4+25424t^3+44400t^2+12448t+896.

This is NOT always positive. The descending coefficients of H(1+x) are [9216,211296,1462200,4876206,8826481,8246910,1916847,-3716604,-3920481,-1492506,-104247,65610], with exactly two sign changes. H(1)=65610>0, H(3/2)=-51338059/64<0, H(2)=16380928>0. Descartes plus continuity proves exactly two simple roots in t>1, one in (1,3/2), the other in (3/2,2). Exact rational root isolation gave intervals (941/817,1070/929) and (1792/1025,257/147). T positive outside and negative between. At t=3/2 T=-9035498384/940383999, at 2 T=8958320/1339893, at 3 T=269792957/9550872. This distinguishes the variable-level regime from IF's uniformly positive fixed-level correction. Rational slope nonresonance means this higher term is not necessary for eventual integer rounding on those slopes; it matters for variable or irrational slope near-grid sequences. No such full irrational-slope theorem claimed.

## Explicit examples, exact symbolic certificate

For t=3/2,2,3, enumerate each distinct lower offset s=floor(t r+B)-t r-B over r mod b. At u=tq+B+s or tq+B+s+1 use signed polynomial g=sign*(qN-FD), sign=-1,+1 respectively. The coefficients of q^2*g-D shifted q=x+10000 are all nonnegative with positive constant. D>0 by HX positive baseline denominators (also its explicit square form). Thus sign*(qK0-F)>1/q^2 for every q>=10000. 8 polynomials, 96 coefficients checked. Offsets: t=3/2: -2521/2826,-554/1413; t=2: -55/159; t=3: -25/306.

Let h=t+1/100, a0=t-1. On these endpoints a0 q<=d and u<=h q because 0<B-1 and B+1<100. Also d>=30, u>=64, d^2>=16q and >=7u. HX delta<=34 h^2/a0^2 exp(-a0^2 q/(25h))<=L/q^16 with L=34 h^2/a0^2*16!*(25h/a0^2)^16 from the positive exponential series. Exact rational checks give 4F L<10000^14 and L<10000^16/10. Thus delta<0.1 and 4F delta<1/q^2; HW/HX sandwich transfers both strict signs (upper multiplier <=1+4delta, inverse lower multiplier <=1+3delta). The onset 10000 is sufficient, not claimed minimal.

## Executed exact replay (Python/SymPy)

The calculation used the HW expressions below, symbolic coefficient extraction, exact rational checks and polynomial shifts. Decimal output, where used, was only illustrative.

```python
import sympy as s
from math import gcd,factorial
u,q,t,b,x=s.symbols('u q t b x')
S=4*u+2*q+4;j=u+2*q+1;d=u-q
f=lambda S,g:(4*(g+2)**2-S)/(S*(S-1))
Q=f(S,d-1);V=j/(S-j+1)*f(S,d)
A=j*(j-1)/(S*(S-1))*f(S-2,d)+j*(S-j)/(S*(S-1))*f(S-2,d-1)
N,D=s.fraction(s.factor(A*Q*(3*u+q+1)**2/((Q+V+q*A)**2*(u+2*q+1))))
n=s.Poly(N,u,q);de=s.Poly(D,u,q)
def co(p,k):
 return s.factor(sum(v*s.binomial(i,k0)*t**k0*b**(i-k0) for (i,j),v in p.terms() for k0 in [k-j] if 0<=k0<=i))
m=n.total_degree();l=de.total_degree()
F=s.factor(co(n,m)/co(de,l))
G=s.factor((co(n,m-1)-F*co(de,l-1))/co(de,l))
B=s.factor(s.solve(G,b)[0])
H2=s.factor(((co(n,m-2)-F*co(de,l-2))/co(de,l)).subs(b,B))
T=s.factor(-H2/s.diff(F,t))
H=s.cancel(s.fraction(T)[0]/((2*t+1)*(3*t+1)))
print(m,l,F,G,B,T)
print(s.Poly(H.subs(t,x+1),x).all_coeffs())
print(s.Poly(H,t).intervals(eps=s.Rational(1,100000)))
for aa in (2,4,8):
 for bb in range(1,aa):
  if gcd(aa,bb)==1:
   print(s.Rational(aa,bb),bb*B.subs(t,s.Rational(aa,bb)))
for v in [s.Rational(3,2),s.Rational(2),s.Rational(3)]:
 c0=F.subs(t,v); b0=B.subs(t,v); den=int(s.denom(v))
 offsets=sorted({s.floor(v*r+b0)-v*r-b0 for r in range(den)})
 cnt=0
 for off0 in offsets:
  for off,sg in [(off0,-1),(off0+1,1)]:
   n0=s.Poly(N.subs(u,v*q+b0+off),q)
   d0=s.Poly(D.subs(u,v*q+b0+off),q)
   pp=((sg*(n0*s.Poly(q,q)-c0*d0))*s.Poly(q*q,q)-d0).shift(10000)
   assert pp.TC()>0 and all(z>=0 for z in pp.all_coeffs())
   cnt+=len(pp.all_coeffs())
 h=v+s.Rational(1,100);a0=v-1
 L=34*h*h/a0**2*factorial(16)*(25*h/a0**2)**16
 assert b0-1>0 and b0+1<100
 assert a0*a0*10000>=max(16,7*h) and a0*10000>=30
 assert 4*c0*L<10000**14 and L<s.Rational(10000**16,10)
 print('cert',v,offsets,cnt)
```

Actual output: degrees 9,10; F,B,T as above; seven candidate resonance values above (none integer); an exploratory exact scan of coprime slopes 1<t<=5 with denominator<=150 also found no resonances, superseded by the proof. Polynomial certificate coefficient counts 48,24,24, all assertions passed. The shifted H coefficients and root intervals printed as above. No direct giant true combinatorial counts generated; signs use inherited HX residual proof. No independent mathematical review.

## Next
Develop the transition to slopes t approaching 1 with q (F(1)=32/3) and the critical regime of target q*c around 32/3. There the fixed-slope expansion and exponential payment are not uniform, so the real joint port law and boundary E must be retained. For fixed irrational slopes the near-integer lattice issue also remains. Keep ID independent review separate.
