# Odd-curvature filament: Legendre-dual unification of breaker coverage and tangent exceptions

Status: `FREE_RESEARCH_EXACT_PRIMAL_DUAL_SYNTHESIS / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_FILAMENT_ODD_CURVATURE_DEFORMATION_MASTER_THEOREM_20260825.md`;
- `NATIVE_FILAMENT_DUAL_PARABOLA_TANGENT_ARRANGEMENT_20260825.md`.

## 1. Two quadratic sheets

Assume q is an odd prime not dividing B.

Define the two quadratic functions over `F_q`:

`Q_e(x)=x^2/(2B)-e/2`, `e in {0,1}`.

Their algebraic Legendre transforms are

`Q_e^*(p)=B*p^2/2+e/2`.

The classical tangent family to Q_e is

`y=p*x-Q_e^*(p)`.

Sampling `p=-j` gives exactly the native zero lines

`y=-j*x-(B*j^2+e)/2`

on the corresponding parity sheet.

Thus the local divisibility arrangement is the sampled tangent family of the two Q_e.

## 2. Global divisibility hit sets are the negative dual images

For the infinite odd-curvature filament

`F_B(H,r)=H+(B*r^2+eps(r))/2`,

a q-divisibility hit on the even branch `r=2m` occurs exactly when

`H=-2B*m^2`.

Since `p=2m` runs over all of `F_q`, the even hit set is

`I_0=-Q_0^*(F_q)`.

On the odd branch `r=2m+1`, put `p=2m+1`; p again runs over all of `F_q`. Then

`H=-(B*p^2+1)/2`,

so the odd hit set is

`I_1=-Q_1^*(F_q)`.

Therefore the global breaker problem is the value-set covering problem for the same two quadratics that generate the local tangent arrangement by Legendre duality.

Freeze:

`LOCAL EXCEPTION = TANGENT-INCIDENCE SIDE OF THE QUADRATIC DUALITY`,

`GLOBAL BREAKER = DUAL-VALUE-COVERING SIDE OF THE SAME QUADRATIC DUALITY`.

## 3. Hit-set sizes

Because q does not divide B, each map

`p -> -Q_e^*(p)`

is a nondegenerate quadratic map. Hence

`|I_0|=|I_1|=(q+1)/2`.

Let T_B(q) be the number of transparent H classes, i.e. the complement of `I_0 union I_1`.

Then inclusion-exclusion gives

`T_B(q)=q-(q+1)+|I_0 intersect I_1|`,

so

`|I_0 intersect I_1|=T_B(q)+1`.

Using the exact character-sum transparency formula:

`|I_0 intersect I_1|`

`=[q+1+Legendre(B/q)+Legendre(-B/q)]/4`.

This converts the character formula into an exact intersection number of the two Legendre-dual quadratic images.

## 4. Breaker = minimal overlap

Since each hit set has `(q+1)/2` elements, they cover all of `F_q` iff their intersection has exactly one point.

Therefore

`q is a universal breaker`

iff

`|I_0 intersect I_1|=1`.

Equivalently, in the nondegenerate odd-prime regime:

`q is a breaker`

iff

`q+1+Legendre(B/q)+Legendre(-B/q)=4`.

This gives a geometric proof of the small-prime cutoff.

For q>=7, the intersection formula is always at least2, so the two dual images cannot cover the whole field.

For q=5, since `Legendre(-1/5)=1`, minimal overlap occurs exactly when

`Legendre(B/5)=-1`.

For q=3 and q not dividing B, the two character terms cancel and the intersection has size1, so channel3 is a breaker.

Channel2 remains the separate parity-degeneration case.

## 5. Tangency channels and the sharp run cap

In a breaker phase the two hit images cover `F_q` with the smallest possible overlap: one H-class belongs to both images.

The extremal long nonzero run occurs when one branch reaches a q-hit with a double quadratic root while the other branch has no root at that H.

For the q=5 nonresidue phase there are exactly two normalized tangency channels:

- H=0, double root on the even branch;
- H=-1/2, double root on the odd branch.

Each produces one zero shell class in the full period 2q=10, hence the sharp run `2q-1=9`.

Thus the sharp cap is the dynamic shadow of a minimal-overlap / tangency configuration of the dual quadratic images.

## 6. Local exceptional characteristics use the tangent side

For a finite window, exceptional characteristics are those in which distinct sampled tangents acquire extra concurrence.

For mixed-parity tangent indices u,v,w, this is controlled by

`B*(w-u)*(w-v)+chi*(1-2e)`.

The union over chiralities is controlled by the finite tangent discriminant

`B * product_T (B^2*A_T^2-1)`.

So the same quadratic pair produces two arithmetic spectra:

- **projection/value spectrum**: breaker characteristics, determined by overlap of `-Q_e^*(F_q)`;
- **incidence/tangent spectrum**: exceptional local characteristics, determined by concurrence among sampled tangents to `Q_e`.

The former is globally bounded by5 in the odd-curvature family; the latter can extend to larger primes such as native53 because it depends on finite-window tangent spacing.

## 7. Native B=3 chain

For the actual tri-sector coefficient B=3:

- the dual hit images have minimal overlap at q=5, so 5 is the first surviving universal breaker after channels2 and3;
- the q=5 tangency channels give the sharp 9-run / 9-Cell island cap;
- finite sampled tangent concurrence produces the later exceptional spectrum ending at53 for k<=9.

Thus the native arithmetic hierarchy separates cleanly into

`5 = GLOBAL DUAL-IMAGE COVERING THRESHOLD`,

`9 = SHARP TANGENCY RUN CAP`,

`53 = FINAL FINITE-WINDOW TANGENT-CONCURRENCE CHARACTERISTIC`.

## 8. Prior-art boundary

Legendre transforms, dual conics/parabolas, tangent-line duality, quadratic value-set sizes and finite-field conic geometry are classical.

No novelty claim is made for those general tools.

A statement-level search found standard conic duality and finite-field tangent theory, but no direct match for the exact coupled family

`periodic-curvature integer filament -> dual quadratic hit images + sampled tangent arrangement -> breaker/tangent-exception split`.

This exact coupling remains a research candidate pending independent literature review.