# P000 P11 diagonal shared-leg Pythagorean triple-of-triples — Return

- Task: `RS-P000-SIX-AXIS-P11-DIAGONAL-SHARED-LEG-PYTHAGOREAN-TRIPLE`
- Publication: `TP2-51DFEBDCCCB1C845F8EF`
- Parent accepted Result: `RR-DA840CA11911B721506F`
- Researcher: `EM-P000P11D2-9C3167`
- Claim: `chatgpt-p000p11d2-20260904-2111-7a41c9`
- Execution branch: `research/p000-six-axis-p11-diagonal-shared-leg-em-p000p11d2-9c3167`
- Execution branch base: `3a0268264f8c660fcc599eddc1b838eba2b99f45`

## Terminal verdict

`SUCCESS / DIAGONAL_FIXED_LOCUS_REDUCED_TO_EXACT_NONRATIONAL_OR_HIGHER_ARITHMETIC_COMPONENT`

The accepted `h=0` fixed locus admits a complete Euclidean reduction, but after the primitive base Pythagorean triangle is frozen the shared-leg problem is a smooth genus-one curve. Thus the exact remaining arithmetic is elliptic rather than a third independent Pythagorean parameter.

The reduction also produces two new exact facts that were not frozen in the parent:

1. the zero-root/sign boundary is empty on the strict fixed locus: every valid datum has `0 < d < x-y`, hence all three AP product coordinates are strictly negative;
2. the hypothesis that every primitive fixed-locus datum is a common scaling of the known witness is false. In the precommitted exact control `b<=100000`, there are 19 recovered-root-gcd-one points. The smallest point after the known witness is

\[
(x,y,b;d,\mu,\nu)=(2720,165,2725;1533,2444,2044).
\]

The bounded census is used only as regression/falsification evidence. The terminal classification is the symbolic genus-one reduction below.

No native orientation, Pfaffian slot, dimension reduction, factorization semantics, Full-Cell dynamics, Working Truth, Foundation authority, L4 status, canonical promotion, or novelty claim is made.

---

## 1. Exact fixed-locus equivalence and parity

Put

\[
p=x+y,\qquad q=x-y.
\]

The parent fixed-locus theorem says `h=0` iff the two equal-area Pythagorean factors coincide. Therefore its normal form specializes exactly to

\[
x^2+y^2=b^2,\qquad x>y>0,
\]
\[
d^2+\mu^2=p^2,
\]
\[
d^2+\nu^2=q^2,
\qquad d>0,
\]

with fixed-locus parity

\[
p\equiv b\equiv q\equiv d\pmod 2,\qquad
\mu\equiv\nu\equiv0\pmod2.
\]

Conversely, any integer sextuple satisfying these equations and parity conditions reconstructs the parent normal form with

\[
(X,Y,g)=(x,y,b),\qquad h=0,
\]

so it is an exact `h=0` simultaneous datum. Thus the three displayed quadratic equations plus parity are necessary and sufficient.

The first equation gives

\[
p^2+q^2
=(x+y)^2+(x-y)^2
=2(x^2+y^2)
=2b^2,
\]

and subtraction of the two shared-leg equations gives the exact secondary identity

\[
\mu^2-\nu^2=p^2-q^2=4xy.
\]

For an integer Pythagorean triangle, `p,q,b` have one common parity. Hence the full fixed-locus parity may be compressed to

\[
d\equiv p\pmod2.
\]

Indeed if `p,d` are both odd, `p^2-d^2` and `q^2-d^2` are divisible by eight, so `mu,nu` are even; if `p,d` are even, their square differences are divisible by four, again forcing `mu,nu` even.

Define

\[
e=\frac{xy}{2},\qquad
t=\frac{d^2-b^2}{4}.
\]

The parity just proved makes both integers. The reconstructed AP datum is

\[
H=(-d,0,d),\qquad T=(t-e,t,t+e).
\]

Moreover

\[
4(t-e)=d^2-(x+y)^2=-\mu^2,
\]
\[
4(t+e)=d^2-(x-y)^2=-\nu^2.
\]

These formulas determine the sign boundary exactly.

---

## 2. Exact recovered-root gcd and primitive quotient

The top and bottom discriminants are

\[
p,\ b,\ q
\]

and the two middle-row discriminants are `mu,nu`. Consequently the sixteen outer recovered roots are, up to duplication between the top and bottom rows,

\[
\frac{-d\pm p}{2},\quad
\frac{-d\pm b}{2},\quad
\frac{-d\pm q}{2},\quad
\pm\frac{\mu}{2},\quad
\pm\frac{\nu}{2},
\]

and

\[
\frac{d\pm p}{2},\quad
\frac{d\pm b}{2},\quad
\frac{d\pm q}{2}.
\]

Therefore the exact common recovered-root gcd is

\[
m=
\gcd\!\left(
\left|\frac{d\pm p}{2}\right|,
\left|\frac{d\pm b}{2}\right|,
\left|\frac{d\pm q}{2}\right|,
\frac{|\mu|}{2},
\frac{|\nu|}{2}
\right),
\]

where each `±` contributes both signs.

This is not the same as the naive gcd of `(x,y,b,d,mu,nu)`. For example the new primitive witness below has a base Pythagorean triangle with common factor five, but its recovered-root gcd is one.

If `m>1`, division of all sixteen roots by `m` divides every row sum and every discriminant by `m`, and every product by `m^2`. Hence it induces

\[
(p,q,b,d,\mu,\nu)\mapsto
(p,q,b,d,\mu,\nu)/m
\]

and, because the scaled discriminants retain the row parity,

\[
(x,y)\mapsto(x,y)/m.
\]

The three homogeneous quadratic equations remain valid. Conversely common root scaling by `m` multiplies exactly these fixed-locus coordinates by `m`. Thus `m=1` is necessary and sufficient for the task's primitive quotient.

---

## 3. Complete Euclidean parameterization of the base triangle

Classical Euclidean Pythagorean parameterization gives every integer base triangle uniquely up to the declared leg ordering as follows.

Choose

\[
r>s>0,\qquad \gcd(r,s)=1,\qquad r\not\equiv s\pmod2,
\]

and put

\[
A=r^2-s^2,\qquad B=2rs,\qquad C=r^2+s^2.
\]

Then for some integer `k>=1`,

\[
\{x,y\}=\{kA,kB\},\qquad b=kC,
\]

with `x>y` fixing the order. Define

\[
P=A+B,\qquad Q=|A-B|.
\]

Since `A,B` are positive and unequal,

\[
P>Q>0,
\]

and independent of which Pythagorean leg is larger,

\[
p=kP,\qquad q=kQ.
\]

The entire residual fixed-locus arithmetic is therefore

\[
d^2+\mu^2=k^2P^2,\qquad
d^2+\nu^2=k^2Q^2,
\]

together with

\[
d\equiv k\pmod2
\]

because `P,Q,C` are odd.

Normalize

\[
D=\frac d k,\qquad U=\frac\mu k,\qquad V=\frac\nu k.
\]

Then

\[
U^2+D^2=P^2,\qquad
V^2+D^2=Q^2.
\]

Conversely, for any rational point `(D,U,V)` on these two quadrics with `D>0`, any positive integer `k` clearing denominators and satisfying the fixed parity reconstructs an integer shared-leg datum; the root-gcd formula of Section 2 then performs the exact primitive quotient.

Thus no independent treatment of the three Pythagorean equations is needed: after the complete Euclidean base parameterization, the remaining problem is the rational-point problem on one explicit curve.

---

## 4. The residual curve is elliptic

For a fixed primitive Euclidean core `(r,s)`, consider the projective curve

\[
C_{P,Q}:\quad
U^2+D^2=P^2Z^2,\qquad
V^2+D^2=Q^2Z^2
\subset\mathbf P^3.
\]

### Theorem 4.1 — smooth genus-one fiber

For every `P>Q>0`, `C_{P,Q}` is a smooth complete intersection of two quadrics, hence has genus one. It contains the rational point

\[
[D:U:V:Z]=[0:P:Q:1],
\]

so after choosing this degenerate `d=0` point as origin it is an elliptic curve over `Q`.

### Proof

The gradients of the two quadrics in coordinates `(D,U,V,Z)` are

\[
(2D,2U,0,-2P^2Z),
\]
\[
(2D,0,2V,-2Q^2Z).
\]

Suppose they are linearly dependent at a projective point. If either dependence coefficient vanishes, the other gradient equations force `D,V,Z` or `D,U,Z` to vanish and then the remaining quadric forces the last coordinate to vanish, impossible in projective space. Hence both coefficients are nonzero, so `U=V=0`. The two quadratic equations then give

\[
D^2=P^2Z^2=Q^2Z^2.
\]

Since `P^2!=Q^2`, this forces `Z=0` and then `D=0`, again impossible. Thus the intersection is smooth.

A smooth complete intersection of two quadrics in `P^3` has genus one. The displayed rational point supplies the rational origin. QED.

This already isolates a genuine nonrational curve (in the algebraic-geometric sense `genus=1`, not “having no rational points”) as the exact residual arithmetic.

### Explicit quartic avatar

Subtracting the two affine equations gives

\[
U^2-V^2=P^2-Q^2.
\]

Set

\[
T=U+V.
\]

Since `P^2-Q^2!=0`, one has `T!=0`, and therefore

\[
U=\frac12\left(T+\frac{P^2-Q^2}{T}\right),\qquad
V=\frac12\left(T-\frac{P^2-Q^2}{T}\right).
\]

With

\[
Y=2TD
\]

the first quadratic equation becomes exactly

\[
Y^2=
\bigl((P+Q)^2-T^2\bigr)
\bigl(T^2-(P-Q)^2\bigr).
\]

Conversely this formula recovers `(D,U,V)` by the displayed rational inverse. The four quartic roots

\[
\pm(P+Q),\qquad \pm(P-Q)
\]

are distinct because `P>Q>0`, so this is the same smooth genus-one curve.

Hence the complete fixed-locus classification is reduced, for every Euclidean core, to rational points on an explicit elliptic fiber plus denominator, parity, positivity and recovered-root-gcd filters. This is the exact arithmetic obstruction authorized by the task's third terminal class. No assertion is made that Mordell-Weil groups for all fibers have been uniformly computed.

The Euclidean Pythagorean parameterization, the genus formula for a smooth intersection of two quadrics, elliptic-curve rational-point theory, and Fermat's classical `n=4` infinite descent used below are prior mathematics. The task-specific contribution is their exact specialization to the frozen P11 fixed locus.

---

## 5. Zero-root boundary is empty; product chamber is strictly negative

From

\[
d^2+\nu^2=q^2
\]

one has `d<=q`. Equality would give `nu=0` and

\[
\mu^2=p^2-q^2.
\]

In primitive Euclidean-core coordinates this means

\[
\left(\frac{\mu}{k}\right)^2
=P^2-Q^2
=(A+B)^2-(A-B)^2
=4AB.
\]

Therefore `AB` is a square. Since the primitive Euclidean legs `A,B` are coprime, each would itself be a square:

\[
A=u^2,\qquad B=v^2.
\]

But `A^2+B^2=C^2` would then give

\[
u^4+v^4=C^2,
\]

contradicting Fermat's classical `n=4` infinite descent for positive integers. Hence equality cannot occur and

\[
0<d<q=x-y.
\]

It follows that

\[
\mu>0,\qquad\nu>0
\]

and, because `q<b<p`,

\[
4(t-e)=-\mu^2<0,
\]
\[
4t=d^2-b^2<0,
\]
\[
4(t+e)=-\nu^2<0.
\]

Thus

\[
t-e<t<t+e<0.
\]

Every outer cell product is strictly negative. A recovered outer root could be zero only if one of the relevant discriminants equalled `d` or if `mu=0` or `nu=0`; all are excluded by `0<d<q<b<p`. Therefore:

`THE STRICT h=0 FIXED LOCUS HAS NO ZERO-ROOT STRATUM.`

The degenerate rational point `D=0` used as the elliptic origin is not a valid AP datum because the task requires `d>0`.

---

## 6. Known witness and a new primitive witness

### Known witness

The accepted witness

\[
(176,57,185;105,208,56)
\]

has

\[
p=233,\qquad q=119,
\]

and satisfies the three coupled equations. Its Euclidean core is

\[
(r,s)=(11,8),
\]

because

\[
176=2\cdot11\cdot8,\qquad
57=11^2-8^2,\qquad
185=11^2+8^2.
\]

Thus it appears naturally as a nondegenerate rational point on the explicit fiber

\[
C_{233,119}.
\]

It is not inserted as an exceptional case.

### New primitive witness

The precommitted control certifies

\[
(x,y,b;d,\mu,\nu)
=(2720,165,2725;1533,2444,2044).
\]

Directly,

\[
2720^2+165^2=2725^2,
\]
\[
1533^2+2444^2=2885^2=(2720+165)^2,
\]
\[
1533^2+2044^2=2555^2=(2720-165)^2.
\]

The reconstructed AP data are

\[
H=(-1533,0,1533),
\]
\[
T=(-1493284,-1268884,-1044484).
\]

Its outer root pairs are

\[
\begin{array}{ccc}
(-2209,676)&(-2129,596)&(-2044,511)\\
(-1222,1222)&\text{center omitted}&(-1022,1022)\\
(-676,2209)&(-596,2129)&(-511,2044).
\end{array}
\]

The gcd of the absolute values of all sixteen recovered roots is exactly one. Hence the point is primitive in the task's actual quotient, even though the base triple itself has a factor five.

Both this point and the known witness have recovered-root gcd one. Therefore neither can be a nontrivial common scaling of the other. On the `h=0` fixed locus the parent triangle-swap involution is the identity, and unordered root-pair presentation swaps do not change `(p,b,q,d,mu,nu)`, so the new point is not a presentation image of the known point.

This strictly falsifies the seed-scaling hypothesis.

---

## 7. Precommitted exact control

Before inspecting the formal control outcome, scheduler comment `5540961965` froze:

- every Euclidean integer base triangle with `b<=100000`;
- every integer `0<d<=x-y` satisfying both shared-leg square cuts;
- exact fixed-locus parity;
- exact recovered-root gcd;
- no promotion of the bounded census to global completeness.

The standard-library checker exhausts this range through complete Euclidean generation, not random sampling.

Exact counts:

| quantity | count |
|---|---:|
| integer base Pythagorean triangles `b<=100000` | 161,436 |
| common-leg square candidates before fixed parity | 700 |
| parity-valid fixed-locus points | 645 |
| recovered-root-gcd-one points | 19 |

The checker additionally reconstructs all eight AP root pairs for every valid hit and verifies the genus-one quartic identity exactly.

The first two primitive points ordered by base hypotenuse are

\[
(176,57,185;105,208,56),
\]
\[
(2720,165,2725;1533,2444,2044).
\]

All 19 primitive control points are frozen in the certificate artifact.

Again, these counts are finite regression/falsification evidence only. The global terminal statement is the symbolic reduction of Sections 1–5.

---

## 8. Frozen artifacts and exact scope

Checker:

`research_checks/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE_CHECK_20260904.py`

Control certificate:

`research_artifacts/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE/control_certificate_20260904.json`

Fresh exact replay:

`PASS P000 P11 diagonal shared-leg control: B=100000 base_triangles=161436 shared_candidates=700 parity_valid=645 primitive_root_gcd_hits=19 new_primitive=(2720,165,2725;1533,2444,2044)`

The result proves exactly:

- necessary-and-sufficient fixed-locus coupled equations and parity;
- exact recovered-root primitive normalization;
- complete Euclidean base parameterization;
- exact reduction of every primitive-core residual problem to a smooth genus-one/elliptic fiber;
- emptiness of the zero-root boundary and strict negativity of all fixed-locus AP products;
- existence of a second primitive point not obtained from the known seed by common scaling or the fixed-locus presentation symmetries.

It does **not** prove a uniform Mordell-Weil classification of every fiber, a finite list of all global primitive points, or any claim outside the frozen derived-arithmetic P11 facade.

The terminal class is therefore

`DIAGONAL_FIXED_LOCUS_REDUCED_TO_EXACT_NONRATIONAL_OR_HIGHER_ARITHMETIC_COMPONENT`.
