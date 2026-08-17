# R059D Stage AL — Canonical Native Resolver Rigidity Proof

Researcher-ID: `EM-R059D-AL-5A9D31`

Task: `RS-R059D-STAGE-AL-CANONICAL-NATIVE-RESOLVER-RIGIDITY`

## 1. Why A0–A7 do not imply uniqueness

The target fixed-length semantics, locality, finite state, sampling freedom, translation/D6 covariance, simple closure and axis-anchor completeness do not determine a unique orbit.

For every `r>=1`, the pure-axis sector word

`H_r = 2^r`

runs from `(r,0)` to `(0,r)` by primitive adjacency moves. Six D6 transports form a simple hexagonal cycle. The rule is radius-uniform, constant-state, sampling-free and translation/D6 covariant. It preserves the abstract anchor class `r`. Therefore it satisfies A0–A7. At `r=5`, however,

`W_N(5)=212232 != 22222=H_5`.

So A0–A7 are insufficient.

Even adding the exact AG count/period does not select the internal arrangement. Put `J=J_N(r)` and define

`P_r = 1^J 2^(r-J) 3^J`.

This is a nonnegative single-peak Motzkin sector path with exactly the accepted counts and sector length `r+J`, hence the same full period `C_N(r)`. At `r=5`,

`P_5=122223 != 212232=W_N(5)`.

Thus fixed length, locality, D6, simple closure, monotonicity and even the exact circumference count still leave a genuine path ambiguity.

## 2. Native primitive-support index

We now construct the extra target structure without inserting the N word or residual recurrence.

Let a quadratic form on Enterprise coordinates be

`Q(a,b)=A a^2+B ab+C b^2`.

Require invariance under the native 60-degree transport

`R(a,b)=(-b,a+b)`.

Expanding `Q(R(a,b))=Q(a,b)` gives

`C=A`, `-B+2C=B`, and `A-B=0`.

Hence `A=B=C`. Primitive normalization `Q(1,0)=1` yields the unique integral D6-invariant quadratic incidence grading

`Q_E(a,b)=a^2+ab+b^2`.

This object is typed only as a **support/incidence index**. It is not `L_E`, not an endpoint norm and not a Euclidean equal-distance premise.

For an elementary triangular cell `t` with vertices `v1,v2,v3`, define its barycentric numerator

`c(t)=v1+v2+v3`

and its primitive support rank

`rank(t)=Q_E(c(t))`.

For a primitive edge `e` incident to a lattice vertex `p`, let `t_e^+` and `t_e^-` be the two elementary triangles adjacent to `e`. Define

`rank(e)=max(rank(t_e^+),rank(t_e^-))`.

Finally define the vertex support rank

`SUP(p)=min_{e incident to p} rank(e)`.

The radius-r anchor support level is

`SUP_anchor(r)=Q_E(3r,0)=9r^2`.

The target primitive-support carrier is therefore

`K_E(r)={p : SUP(p)<=9r^2}`.

This definition uses only triangular incidence, barycentric integer addition, D6 transport and primitive normalization. No source circle or Euclidean distance occurs in the target construction.

## 3. Coordinate certificate from the accepted support theorem

The accepted AG edge-support theorem supplies a coordinate certificate for the abstract support rank. In the first sector `a,b>=0`, enumerating the six incident edge pairs gives

`SUP(a,b)=9(a^2+ab+b^2)-9 max(a,b)+3`.

Equivalently, on the left half-sector `a>=b`, put

`L(a,b)=3(a^2+ab+b^2)-3a+1`.

Then

`(a,b) in K_E(r) iff L(a,b)<=3r^2`.

The exact finite differences are

`L(a,b+1)-L(a,b)=3(a+2b+1)>0`,

and

`L(a-1,b+1)-L(a,b)=3(b-a+2)<=0` whenever `a-b>=2`.

Hence, before the bisector:

1. outward vertical candidates become unsupported monotonically;
2. if the vertical candidate is unsupported, the inward-diagonal successor is still supported;
3. each relevant carrier column is an inward initial interval.

Reflection gives the symmetric statements on `a<=b`.

The AG formula is used here as a **proof-side coordinate identity for SUP**. It is not the runtime definition of the AK turn law and is not promoted to an Enterprise length metric.

## 4. A8 — Primitive-Support Frontier Maximality

The final admissibility axiom A8 is:

> In each directed sector, the circle path is the oriented outer monotone frontier of `K_E(r)`. At a state before the bisector, if the outward vertical successor remains in the carrier the path must take it; otherwise it takes the unique supported inward-diagonal successor. The reflected rule applies after the bisector. The bisector crossing is the unique move compatible with D6/reflection transport.

This is not the N recurrence. It is a geometric/frontier selection rule on an independently defined target carrier.

## 5. Sector uniqueness

Fix `r>=1`. Let `F_r` be the outer frontier from `(r,0)` to `(0,r)`.

Suppose an admissible sector path `P` satisfying A0–A8 agrees with `F_r` through a vertex `p` and differs at the next move.

There are only two possibilities.

- `P` takes an outward candidate that is not in `K_E(r)`. Then `P` leaves the required support carrier, contradicting A8.
- The outward candidate is in `K_E(r)` but `P` takes the inward candidate. Then `P` is not the outer frontier, again contradicting A8.

At the bisector, D6/reflection compatibility leaves one crossing convention, so no third option appears.

Therefore a first divergence is impossible. By induction,

`|ADM_E^sector(r)|=1`.

The accepted AH/AK N path satisfies the same frontier rule by the support finite-difference theorem, so the unique sector path is exactly `W_N(r)`.

## 6. Full-orbit uniqueness

A5 transports the unique sector path by one D6 law. A6 and A7 fix orientation and joins at the six axis anchors. Thus the full simple endpoint orbit is unique and equals the accepted AK/AH N D6 orbit.

The uniqueness statement is geometric/orbit-level. Different constant-size register encodings of the same one-step orbit are not ruled out.

## 7. Period and canonical constant

AK proved that the accepted N orbit has no endpoint repeat before closure and minimal positive turn period

`T_r=C_N(r)=6(r+J_N(r))`.

AG gives

`J_N(r)=floor(alpha*r+1/3)`,

where `alpha` is the unique positive root of

`3alpha^2+6alpha-1=0`.

Since the admissible orbit is unique, these become canonical Enterprise-native consequences:

`C_E(r)=T_r=C_N(r)`

and

`lim T_r/(2r)=kappa_E`,

with

`kappa_E^2=12`, `kappa_E>0`.

AI endpoint-convention robustness and AJ finite-sampling readout robustness remain unchanged.

## 8. C_s typing

The inherited AD/AJ resolver `C_s` evaluates an explicit subdivision parameter `s` and majority comparison `2K_s>=s^2`. Hence it fails the sampling-free target axiom A3 as a primitive native law.

The distinction is operational. At `r=5`, exact inherited replay yields

`J_C_1=1`, `J_C_2=1`, `J_C_3=0`,

while `J_N=1`.

Thus the pointwise resolver depends on finite readout precision. AJ nevertheless proves

`J_C_s=J_N-chi_s`, `chi_s in {0,1}`,

and

`0<=C_N-C_C_s<=6`,

uniformly for every `s>=1`; all `C_s` share `kappa_E`. Sharing the asymptotic constant does not make a sampling-indexed readout law a co-equal primitive resolver.

No unproved sampling-free `s->infinity` resolver is introduced.

## 9. BRC consequence

The BRC/orthogonal side may remain a teacher and compatibility surface. But once A0–A8 are imposed, target collapse is not an arbitrary rasterization choice: the target primitive-support carrier has one outer frontier, and its fixed-length turn orbit is the canonical target circle in the frozen admissible class.

This is not a theorem about every imaginable discretization. It is a rigidity theorem for the explicit Enterprise-native class `ADM_E`.

## 10. Semantic firewalls

The theorem does not:

- define admissibility as equality with N;
- place the N word, residual sign sequence or step table in A8;
- use Euclidean equal-distance as target length;
- identify `kappa_E` with the standard real number `pi`;
- claim uniqueness among rules that reject the frozen native admissibility axioms;
- claim a unique internal machine encoding.

The canonical runtime remains the AK integer local `tau`; it does not evaluate `Q_E`, `SUP`, source geometry, floating point, square roots, trigonometry or lookup tables.
