# Native filament odd-curvature family: dual-parabola tangent arrangement

Status: `FREE_RESEARCH_EXACT_GEOMETRIC_REINTERPRETATION / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on `NATIVE_FILAMENT_ODD_CURVATURE_DEFORMATION_MASTER_THEOREM_20260825.md`.

## 1. Zero lines in dual coordinates

Fix odd positive curvature coefficient `B`, chirality `chi in {+1,-1}`, and write the divisibility parameter plane as

`(x,y)=(b,a)`.

The zero line for coordinate `j` is

`L_j: y=-j*x-(B*j^2+chi*eps(j))/2`.

Split the indices by parity.

## 2. Two sampled dual parabolas

For even `j`, the line is

`y=-j*x-B*j^2/2`.

This is the tangent at

`x_0=-B*j`

to the parabola

`P_0: y=x^2/(2B)`.

For odd `j`, the line is

`y=-j*x-B*j^2/2-chi/2`.

This is the tangent at

`x_0=-B*j`

to the vertically shifted parabola

`P_chi: y=x^2/(2B)-chi/2`.

Thus one chirality sheet is exactly a discrete tangent arrangement sampled from two parallel parabolas separated by vertical distance `1/2`.

Changing chirality reflects which shifted parabola supplies the odd tangent family.

## 3. Intersection of two same-family tangents

Take two same-parity indices `u,v`. Their two tangents have the same vertical offset `c_e=chi*e/2`, where `e=eps(u)=eps(v)`.

Their intersection is

`x_uv=-B*(u+v)/2`,

`y_uv=B*u*v/2-c_e`.

Let `w` have the opposite parity. Its tangent belongs to the other parabola, with offset

`c_opp=chi*(1-e)/2`.

Substituting `(x_uv,y_uv)` into `L_w` gives the exact concurrence equation

`B*(w-u)*(w-v)+chi*(1-2e)=0`.

Over a residue ring `Z/q^a Z` in the distinct-slope regime, the same calculation yields

`L_u,L_v,L_w concurrent mod q^a`

iff

`q^a | B*(w-u)*(w-v)+chi*(1-2e)`.

This is the geometric source of the mixed-parity obstruction in the arithmetic-lift theorem.

## 4. Same-parity degeneration

Three tangents from one sampled parabola are nonconcurrent over characteristic zero.

Their determinant is a Vandermonde factor times `B/2`.

Therefore in characteristic `q>k-1`, three same-parity tangents become concurrent exactly when `q|B`.

So divisors of `B` are precisely the characteristics in which each sampled parabola family itself degenerates.

## 5. Two-chirality discriminant

For one mixed triple put

`A=(w-u)*(w-v)`.

The two chirality obstructions are

`B*A+1`

and

`B*A-1`

up to the parity sign convention.

Their product is

`B^2*A^2-1`.

Thus for `k>=5` the union of exceptional characteristics across both chiralities is controlled by

`mathfrak D_(k,B)=B * product_T (B^2*A_T^2-1)`.

For every prime `q>k-1`:

`q changes the tangent-arrangement intersection type for at least one chirality`

iff

`q | mathfrak D_(k,B)`.

The exact q-adic persistence depth of a concurrence is the valuation of its corresponding tangent-incidence obstruction.

## 6. Native specialization

At `B=3` the sampled tangent parabolas are

`y=x^2/6`

and

`y=x^2/6-chi/2`.

The sharp `k<=9` incidence cap bounds all mixed distance products and forces the post-small exceptional support to end at `53`.

Thus the previously observed `5 -> 9 -> 53` chain can be viewed as

`native tri-sector curvature`

`-> discrete double-parabola tangent family`

`-> mod-5 connectivity tangency`

`-> finite tangent-concurrence discriminant`.

## 7. Prior-art boundary

Duality between a parabola and its tangent-line conic is classical projective/affine geometry. Hyperplane/line-arrangement discriminants and finite-field reductions are classical.

This note does not claim novelty for parabola duality or tangent arrangements in general.

The research-specific candidate is the exact arithmetic coupling of the parity-sampled two-parabola tangent arrangement to the native filament quotient code, transparency transition and p-adic concurrence depth. A quick statement-level search found no direct theorem match for this exact coupled family; that is not a substitute for independent literature review.