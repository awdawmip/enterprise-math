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

The accepted `h=0` fixed locus is reduced exactly to an elliptic (genus-one) fiber after complete Euclidean parameterization of the base right triangle. The reduction also proves that the strict fixed locus has no zero-root stratum and falsifies the hypothesis that every primitive point is a common scaling of the known witness.

No claim is made about native orientation, Pfaffian-slot choice, P000 dimension reduction, factorization semantics, Full-Cell dynamics, Working Truth, Foundation/L4 status, canonical promotion, or historical novelty.

## 1. Exact fixed-locus system and AP reconstruction

Put
\[
p=x+y,\qquad q=x-y.
\]
The parent `h=0` theorem specializes necessarily and sufficiently to
\[
x^2+y^2=b^2,\qquad x>y>0,
\]
\[
d^2+\mu^2=p^2,\qquad d^2+\nu^2=q^2,\qquad d>0,
\]
with
\[
p\equiv b\equiv q\equiv d\pmod 2,\qquad \mu\equiv\nu\equiv0\pmod2.
\]
Conversely any sextuple satisfying these equations and parity conditions reconstructs the accepted `h=0` normal form.

The coupled system implies
\[
p^2+q^2=2b^2,\qquad \mu^2-\nu^2=p^2-q^2=4xy.
\]
For an integer Pythagorean triangle `p,q,b` have one common parity, so the fixed-locus parity is equivalently `d≡p (mod 2)`; the two square equations then force `mu,nu` even.

Set
\[
e=\frac{xy}{2},\qquad t=\frac{d^2-b^2}{4}.
\]
Then
\[
H=(-d,0,d),\qquad T=(t-e,t,t+e)
\]
and
\[
4(t-e)=-\mu^2,\qquad 4(t+e)=-\nu^2.
\]

## 2. Exact primitive quotient

The sixteen recovered outer roots are obtained from
\[
\frac{-d\pm p}{2},\quad \frac{-d\pm b}{2},\quad \frac{-d\pm q}{2},
\quad \pm\frac{\mu}{2},\quad \pm\frac{\nu}{2},
\]
and
\[
\frac{d\pm p}{2},\quad \frac{d\pm b}{2},\quad \frac{d\pm q}{2}.
\]
Hence the exact common recovered-root gcd is
\[
m=\gcd\!\left(
\left|\frac{d\pm p}{2}\right|,
\left|\frac{d\pm b}{2}\right|,
\left|\frac{d\pm q}{2}\right|,
\frac{|\mu|}{2},\frac{|\nu|}{2}
\right),
\]
with both choices of every `±`.

If `m>1`, division of all recovered roots by `m` divides every row sum and discriminant by `m`, every product by `m^2`, and therefore divides `(x,y,b,d,mu,nu)` compatibly with the same homogeneous equations. Conversely common root scaling multiplies these coordinates by the same factor. Thus `m=1` is necessary and sufficient for the task's primitive quotient. This is strictly finer than the naive gcd of the six displayed coordinates.

## 3. Complete Euclidean base parameterization

Choose
\[
r>s>0,\qquad \gcd(r,s)=1,\qquad r\not\equiv s\pmod2,
\]
and define
\[
A=r^2-s^2,\qquad B=2rs,\qquad C=r^2+s^2.
\]
Every integer base triangle is, for a unique primitive core and an integer `k>=1`,
\[
\{x,y\}=\{kA,kB\},\qquad b=kC,
\]
with `x>y` fixing the order. Put
\[
P=A+B,\qquad Q=|A-B|.
\]
Then `P>Q>0`, `P,Q,C` are odd, and
\[
p=kP,\qquad q=kQ.
\]
Normalize
\[
D=d/k,\qquad U=\mu/k,\qquad V=\nu/k.
\]
The residual arithmetic is exactly
\[
U^2+D^2=P^2,\qquad V^2+D^2=Q^2,
\]
plus denominator clearing, `d≡k (mod 2)`, positivity, and the recovered-root-gcd filter.

## 4. Exact genus-one obstruction

For each primitive Euclidean core define
\[
C_{P,Q}:\quad
U^2+D^2=P^2Z^2,\qquad
V^2+D^2=Q^2Z^2
\subset\mathbf P^3.
\]

### Theorem

`C_{P,Q}` is a smooth complete intersection of two quadrics, hence has genus one. It contains `[D:U:V:Z]=[0:P:Q:1]`, so after choosing that rational point as origin it is an elliptic curve over `Q`.

### Proof

The two gradients are
\[
(2D,2U,0,-2P^2Z),\qquad (2D,0,2V,-2Q^2Z).
\]
If they were dependent at a projective point, neither dependence coefficient could vanish; hence `U=V=0`. The two quadrics would then give
\[
D^2=P^2Z^2=Q^2Z^2.
\]
Since `P>Q>0`, this forces `Z=D=0`, impossible projectively. Thus the intersection is smooth. A smooth complete intersection of two quadrics in `P^3` has genus one, and the displayed rational point supplies an origin. QED.

An explicit birational quartic avatar follows by setting
\[
T=U+V,\qquad Y=2TD.
\]
Since `U^2-V^2=P^2-Q^2` and `T\ne0`,
\[
U=\frac12\left(T+\frac{P^2-Q^2}{T}\right),\qquad
V=\frac12\left(T-\frac{P^2-Q^2}{T}\right),
\]
and
\[
Y^2=\bigl((P+Q)^2-T^2\bigr)\bigl(T^2-(P-Q)^2\bigr).
\]
The roots `±(P+Q), ±(P-Q)` are distinct. Thus the global fixed-locus problem is exactly a family of elliptic rational-point problems indexed by primitive Euclidean cores, with explicit integral/parity/primitive filters. No uniform Mordell-Weil classification is claimed.

The Euclidean Pythagorean parameterization, genus formula for a smooth intersection of two quadrics, elliptic-curve rational-point theory, and Fermat's classical `n=4` descent used below are prior mathematics. The task-specific result is their exact specialization to this frozen P11 fixed locus.

## 5. The zero-root boundary is empty

From
\[
d^2+\nu^2=q^2
\]
one has `d<=q`. If `d=q`, then `nu=0` and, in primitive-core coordinates,
\[
(\mu/k)^2=P^2-Q^2=4AB.
\]
Hence `AB` is a square. Since the primitive Euclidean legs `A,B` are coprime, each is a square: `A=u^2`, `B=v^2`. But
\[
A^2+B^2=C^2
\]
would give
\[
u^4+v^4=C^2,
\]
contradicting Fermat's classical `n=4` infinite descent. Therefore
\[
0<d<q=x-y.
\]
Since `q<b<p`, it follows that
\[
t-e<t<t+e<0.
\]
A recovered outer root could be zero only if `d` equalled one of `p,b,q` or if `mu=0` or `nu=0`; all are excluded. Hence the strict `h=0` fixed locus has no zero-root stratum and lies entirely in the strictly negative-product chamber. The rational point `D=0` used as elliptic origin is outside the task because `d>0`.

## 6. Known witness and a new primitive witness

The known point
\[
(176,57,185;105,208,56)
\]
comes from Euclidean core `(r,s)=(11,8)` and therefore appears naturally on `C_{233,119}`.

The precommitted exact control finds the new primitive point
\[
(2720,165,2725;1533,2444,2044).
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
It reconstructs
\[
H=(-1533,0,1533),
\]
\[
T=(-1493284,-1268884,-1044484),
\]
with outer root pairs
\[
\begin{array}{ccc}
(-2209,676)&(-2129,596)&(-2044,511)\\
(-1222,1222)&\text{center omitted}&(-1022,1022)\\
(-676,2209)&(-596,2129)&(-511,2044).
\end{array}
\]
The gcd of all sixteen recovered roots is exactly one. Since both this point and the known witness are primitive and distinct, the new point is not a nontrivial common scaling of the known witness. On `h=0`, the parent triangle-swap involution is the identity, and unordered pair presentation swaps do not change the fixed-locus coordinates. Thus the seed-scaling hypothesis is strictly false.

## 7. Precommitted exhaustive control

Before inspection, scheduler comment `5540961965` froze the control: exhaust every integer base right triangle with `b<=100000`, every `0<d<=x-y` satisfying both shared-leg square equations, exact fixed-locus parity, and exact recovered-root gcd. The census was predeclared as regression/falsification evidence only.

Exact standard-library replay gives:

| quantity | count |
|---|---:|
| integer base Pythagorean triangles `b<=100000` | 161,436 |
| shared-leg square candidates before parity | 700 |
| parity-valid fixed-locus points | 645 |
| recovered-root-gcd-one primitive points | 19 |

The checker reconstructs and verifies all eight outer AP root pairs and the quartic identity for every valid hit. All 19 primitive control points are frozen in the certificate.

Replay line:

`PASS P000 P11 diagonal shared-leg control: B=100000 base_triangles=161436 shared_candidates=700 parity_valid=645 primitive_root_gcd_hits=19 new_primitive=(2720,165,2725;1533,2444,2044)`

## 8. Exact scope

Frozen outputs:

- `research_returns/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE_RETURN_20260904.md`
- `research_checks/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE_CHECK_20260904.py`
- `research_artifacts/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE/control_certificate_20260904.json`

The result proves the exact fixed-locus equivalence and parity, the exact recovered-root primitive quotient, complete Euclidean reduction, a smooth genus-one/elliptic residual fiber for every primitive Euclidean core, emptiness of the zero-root boundary, strict negativity of the AP product chamber, and a second primitive point not generated from the known seed by common scaling or fixed-locus presentation symmetry.

It does not prove a uniform Mordell-Weil classification of all fibers or a finite global list of primitive points. The terminal class is exactly:

`DIAGONAL_FIXED_LOCUS_REDUCED_TO_EXACT_NONRATIONAL_OR_HIGHER_ARITHMETIC_COMPONENT`.
