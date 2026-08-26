# Native filament intrinsic hyperbola quotient and breaker symmetry theorem

Status: `FREE_RESEARCH_EXACT_INTRINSIC_QUOTIENT / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent:
`NATIVE_FILAMENT_SPLIT_HYPERBOLA_TANGENT_COVER_BRIDGE_20260825.md`.

## 1. Tangent-side hyperbola only

Fix an odd field `K`, nonzero `B,C`, and the split hyperbola

`H_(B,C)={(a,b): B*a*b=C}`.

In the tangent interpretation,

`a=w-u`,

`b=w-v`,

where `u,v` are the two same-family tangent indices and `w` is the opposite-family index.

No Legendre-dual variables are needed for the definitions below.

## 2. Natural local symmetry group

Define two involutions on `H_(B,C)`:

`S(a,b)=(b,a)`,

`R(a,b)=(-a,-b)`.

They commute and generate

`K_4={id,S,R,SR} ~= C2 x C2`.

These are not artificial algebraic symmetries.

### S = exchange of same-family tangents

Swapping `u` and `v` sends

`(w-u,w-v) -> (w-v,w-u)`.

Thus it is exactly `S`.

### R = reflection of the pair through w

Replace

`u' = 2w-u`,

`v' = 2w-v`.

Then

`w-u' = -(w-u)`,

`w-v' = -(w-v)`.

Thus it is exactly `R`.

For the integer parity-sampled filament, reflection through `w` preserves the parity class of `u,v`, so this remains a legal local incidence symmetry.

Freeze:

`K_4 = EXCHANGE x REFLECTION`.

## 3. Intrinsic quotient map

For the translated-parabola pair

`Q_i(x)=x^2/(2B)-d_i`,

with

`C=2(d_i-d_(1-i))`,

define on the tangent hyperbola

`pi_i(a,b) = -B*(b-a)^2/8 - d_i`.

This formula is intrinsic in `(a,b)`.

It is invariant under both generators:

- swapping `a,b` changes `b-a` to its negative;
- negating both `a,b` also changes `b-a` to its negative.

Hence `pi_i` factors through the quotient

`H_(B,C)/K_4`.

## 4. Quotient theorem

The induced quotient is exactly the common negative-dual value set:

`H_(B,C)/K_4 ~= I_i intersect I_(1-i)`.

Proof:

set

`x=(b-a)/2`,

`y=(a+b)/2`.

Then `B(y^2-x^2)=C`, and

`pi_i(a,b)=-B*x^2/2-d_i`,

which is the common negative Legendre-dual value.

Conversely, if two hyperbola points have the same `pi_i` value, their corresponding `x` coordinates have the same square. The hyperbola equation then forces the `y` coordinates to have the same square. Therefore the two representation pairs differ only by independent sign changes `(x,y)->(+/-x,+/-y)`.

Under the linear bridge `(x,y)->(a,b)=(y-x,y+x)`, these four sign changes become exactly

`id`, `S`, `R`, `SR`.

Thus every fiber of `pi_i` is one `K_4` orbit.

Freeze:

`COMMON DUAL VALUE SET = TANGENT-CONCURRENCE HYPERBOLA / LOCAL INCIDENCE SYMMETRIES`.

## 5. Breaker as a one-orbit theorem

Over `F_q`, `q` odd and `BC != 0`, the hyperbola has exactly

`q-1`

points.

For the full two-branch transparency problem,

`tau(q)=|H_(B,C)/K_4|-1`.

Therefore:

`q is a universal breaker`

iff

`H_(B,C)(F_q)` is a single `K_4` orbit.

This is a purely tangent-incidence quotient statement.

## 6. Symmetry-order bound

Because

`|K_4|=4`,

one orbit contains at most four points.

A universal breaker therefore requires

`q-1<=4`.

Hence every nonsingular translated-quadratic breaker satisfies

`q<=5`.

No quadratic-character sum is required for this terminal bound.

The explicit character formula only decides whether the small eligible cases actually collapse to one orbit.

## 7. Exact q=5 transitivity criterion

At `q=5`, the hyperbola has four points. It is one orbit exactly when the `K_4` action is regular.

The nontrivial stabilizers are:

- `S(a,b)=(a,b)` iff `a=b`, which is solvable iff `C/B` is a square;
- `SR(a,b)=(a,b)` iff `a=-b`, which is solvable iff `-C/B` is a square;
- `R(a,b)=(a,b)` has no solution because `C!=0`.

Therefore the action is regular iff

`Legendre(C/B,5)=-1`

and

`Legendre(-C/B,5)=-1`.

Since `-1` is a square modulo `5`, these are the same condition.

For the native vertical shift `C=+/-1`, this is exactly

`Legendre(B,5)=-1`.

Thus the native `B=3` breaker condition becomes:

`THE FOUR CONCURRENCE-DIFFERENCE SOLUTIONS MOD 5 FORM ONE REGULAR LOCAL-SYMMETRY ORBIT`.

## 8. Native q=5 versus q=53

### q=5

For `B=3`, the hyperbola has four points and one `K_4` orbit.

Hence the dual overlap has one value and transparency count is zero.

### q=53

The same hyperbola has `52` points and therefore at least `13` local-symmetry orbits. In fact the orbit count is exactly `13`.

The finite `k=9` tangent sample contains one hyperbola point represented by difference pair `(7,5)`, because

`3*7*5+1=106=2*53`.

Thus `53` is a local sample-hit characteristic even though the full hyperbola has thirteen symmetry classes and is far from globally breaking.

This gives the cleanest local/global distinction so far:

`5 = ONE GLOBAL INCIDENCE-SYMMETRY CLASS`,

`53 = ONE FINITE WINDOW HITS ONE OF MANY CLASSES`.

## 9. Why this matters for the native selection problem

The previously separate arithmetic objects now form one quotient diagram:

`finite mixed-parity tangent triples`

`-> difference sample D_J`

`-> H_(B,C)`

`-> quotient by exchange/reflection K_4`

`-> dual-overlap values`

`-> transparency / breaker`.

Local arithmetic singularities inspect whether `D_J` hits the hyperbola.

Global connectivity inspects the quotient cardinality of the full hyperbola.

The distinction between the terminal local prime `53` and terminal global breaker `5` is therefore structural, not an accident of two unrelated computations.

## 10. Prior-art boundary

The following ingredients are classical:

- split hyperbolas and split one-dimensional tori;
- Klein-four actions and Burnside's lemma;
- conic/Legendre duality;
- quadratic-residue intersection counts.

A targeted search found no direct theorem statement identifying the dual-overlap set of a parity-sampled translated-parabola pair with the quotient of its tangent-concurrence difference hyperbola by the concrete exchange/reflection incidence group above.

Current classification:

`NO_DIRECT_MATCH_FOUND / NOT PROOF OF NOVELTY`.

The research-specific candidate is the exact incidence quotient selected by the native filament geometry.