# Native filament split-hyperbola bridge: tangent exceptions and dual covering are one quadratic torsor

Status: `FREE_RESEARCH_EXACT_COUPLING_THEOREM / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on the post-audit V2 statement layer of PR #627.

## 1. Abstract translated-parabola pair

Work over a field `K` of characteristic not equal to `2`.

Fix `B in K^*` and two vertical shifts `d_0,d_1 in K`, `d_0 != d_1`.

Define

`Q_i(x)=x^2/(2B)-d_i`, `i=0,1`.

The tangent to `Q_i` at the sampled point `x=-B u` is

`T_(i,u): y=-u x - B u^2/2 - d_i`.

Put

`C_i=2(d_i-d_(1-i))`.

Then `C_1=-C_0`.

## 2. Tangent-concurrence equation

Take two distinct tangents `T_(i,u),T_(i,v)` from one parabola and one tangent `T_(1-i,w)` from the other.

The first two tangents meet at

`x_uv=-B(u+v)/2`,

`y_uv=Buv/2-d_i`.

Substitution into the third tangent gives

`B(w-u)(w-v)=C_i`.

Therefore the complete three-tangent concurrence condition is

`(w-u,w-v) in H_(B,C_i)`,

where

`H_(B,C)={(a,b) in K^2 : B a b = C}`.

For `C != 0`, this is a split hyperbola / one-dimensional split-torus torsor.

Freeze:

`LOCAL TANGENT CONCURRENCE = FINITE DIFFERENCE SAMPLE HITTING ONE SPLIT HYPERBOLA`.

## 3. Negative Legendre-dual value sets

The Legendre transform of `Q_i` is

`Q_i^*(p)=B p^2/2+d_i`.

Define the negative dual image

`I_i={-Q_i^*(p): p in K}`.

A value belongs to both `I_i` and `I_(1-i)` exactly when there are parameters `x,y` such that

`-B x^2/2-d_i = -B y^2/2-d_(1-i)`.

Equivalently,

`B(y^2-x^2)=C_i`.

Factor the difference of squares:

`B(y-x)(y+x)=C_i`.

Thus dual-image overlap is controlled by the same split hyperbola.

## 4. Exact linear bridge

Define

`Phi(x,y)=(a,b)=(y-x,y+x)`.

Since characteristic is not `2`, `Phi` is invertible with

`x=(b-a)/2`,

`y=(a+b)/2`.

Therefore

`Phi : {(x,y): B(y^2-x^2)=C_i} -> H_(B,C_i)`

is an exact linear isomorphism.

Under this isomorphism:

- the tangent-concurrence difference pair is
  `(a,b)=(w-u,w-v)`;
- the dual-overlap representation pair maps to the same `(a,b)` coordinates.

Hence the local tangent-exception equation and the global dual-overlap representation equation are not merely analogous. They are the same split-hyperbola torsor in two linear coordinate systems.

Freeze:

`TANGENT EXCEPTION <-> SPLIT HYPERBOLA <-> DUAL-COVER OVERLAP`.

## 5. Finite-field sign-orbit theorem

Now let `K=F_q`, with `q` odd and `B,C_i != 0`.

The representation variety

`R_i={(x,y): B(y^2-x^2)=C_i}`

has exactly `q-1` points, because `Phi` identifies it with `ab=C_i/B`.

Let

`G={+/-1} x {+/-1}`

act by independent sign changes

`(x,y)->(s x,t y)`.

Two representation pairs give the same common dual value exactly when they lie in the same `G`-orbit, because the common value depends only on `x^2` (equivalently `y^2`).

Thus

`I_i intersect I_(1-i) ~= R_i/G`.

Burnside's lemma gives

`|I_i intersect I_(1-i)|`

`=1/4 * [(q-1) + (1+Legendre(C_i/B,q)) + (1+Legendre(-C_i/B,q))]`

`=[q+1+Legendre(B C_i,q)+Legendre(-B C_i,q)]/4`.

This recovers the classical order-2 cyclotomic intersection count directly from the same hyperbola that governs tangent concurrence.

The orbit-count formula itself is not claimed new; the structural bridge selecting it is the research object.

## 6. Native parity specialization

For the audited odd-curvature sheet,

`Q_e^(chi)(x)=x^2/(2B)-chi e/2`, `e=0,1`.

Take `i=e`. Then

`C_e=2(d_e-d_(1-e))=-chi(1-2e)`.

The tangent equation becomes exactly

`B(w-u)(w-v)+chi(1-2e)=0`.

The orbit-count expression is independent of chirality because changing `chi` changes `C` to `-C`, which only swaps the two Legendre terms:

`|I_0 intersect I_1|=[q+1+(B/q)+(-B/q)]/4`.

Hence

`tau_B(q)=|I_0 intersect I_1|-1`.

So the audited S3 and S6 layers are unified by one object:

`H_(B,+/-1)`.

## 7. Local sample versus global orbit quotient

This gives a precise local/global separation.

### Local exceptional characteristic

For a finite index window `J`, define its mixed-parity difference sample

`D_J={(w-u,w-v): u,v in one parity class, w in the other}`.

A good odd characteristic `q` changes the sampled tangent arrangement type exactly when

`D_J mod q`

intersects the appropriate split hyperbola

`H_(B,+/-1)(F_q)`.

Thus local exception support is a **finite-sample incidence problem on the hyperbola**.

### Global breaker

The full infinite transverse problem uses all finite-field square parameters. Its obstruction is controlled by the orbit quotient

`R_i/G`.

Since each dual image has `(q+1)/2` points,

`tau_B(q)=|R_i/G|-1`.

Thus a universal breaker occurs exactly when

`|R_i/G|=1`.

So global breaking is a **full-hyperbola orbit-collapse problem**.

Freeze the distinction:

`LOCAL EXCEPTION = SAMPLE HITS HYPERBOLA`,

`GLOBAL BREAKER = HYPERBOLA HAS MINIMAL SIGN-ORBIT QUOTIENT`.

## 8. Why global breakers stop at 5

For `q>=7` and nonzero `B,C`, Burnside gives

`|R_i/G| >= 2`.

Hence no such characteristic can be a universal breaker.

At `q=5`, the orbit quotient has size `1` exactly when the relevant quadratic character is negative.

This gives the conceptual reason the global-breaker spectrum terminates at `5`: it is a statement about the smallest possible sign-orbit quotient of the complete split hyperbola, not about the size of a finite tangent sample.

## 9. Native B=3: 5 and 53 acquire different roles on the same hyperbola

For the native specialization `B=3`:

### q=5 — global orbit collapse

`(3/5)=(-3/5)=-1`, so

`|R/G|=(5+1-1-1)/4=1`.

Therefore

`tau_3(5)=0`.

Channel `5` is a global breaker because the complete split hyperbola forms one sign orbit at the dual-value level.

### q=53 — finite-window sample hit, but no breaker

For the sharp `k=9` tangent window, one extremal mixed triple is

`u=0, v=2, w=7`,

so

`(a,b)=(7,5)`,

`ab=35`.

Then

`3ab+1=106=2*53`.

Thus the finite difference sample hits the concurrence hyperbola modulo `53`, producing the terminal sampled-tangent exceptional characteristic.

But

`(3/53)=(-3/53)=-1`,

so

`|R/G|=(53+1-1-1)/4=13`,

and

`tau_3(53)=12`.

Hence `53` is strongly nonbreaking globally.

This cleanly separates the previously observed constants:

`5 = COMPLETE-HYPERBOLA ORBIT COLLAPSE`,

`53 = FINITE k=9 DIFFERENCE-SAMPLE HIT`.

They arise from the same split-hyperbola equation but from two different functors applied to it.

## 10. Finite-window cutoff restated

Let

`M_J=max |(w-u)(w-v)|`

over the finite mixed-parity index sample.

For odd integer `B`, any odd sampled-tangent exceptional prime away from divisors of `B` divides an even integer

`B A +/-1`

with `|A|<=M_J`.

Therefore

`q <= (B M_J+1)/2`.

For the native `B=3`, `k=9` window,

`M_J=35`,

so

`q<=53`,

and the `(7,5)` sample above attains the bound.

The cutoff is therefore a finite-sampling property of the same hyperbola whose global orbit quotient already stabilized against breaking after `q=5`.

## 11. Prior-art boundary

Classical components include:

- duality of a nondegenerate conic with its tangent-line conic;
- Legendre transform of a quadratic;
- difference-of-squares factorization;
- split hyperbolas / split tori over finite fields;
- Burnside orbit counting;
- order-2 cyclotomic numbers and quadratic-residue translate intersections.

A targeted theorem-level search found sources for those components but no direct statement matching the exact chain

`PARITY-SAMPLED PARALLEL PARABOLAS`

`-> TANGENT-DIFFERENCE SAMPLE ON H_(B,C)`

`-> LINEAR IDENTIFICATION WITH DUAL-OVERLAP REPRESENTATIONS`

`-> SIGN-ORBIT QUOTIENT CONTROLLING BREAKING`.

This is `NO_DIRECT_MATCH_FOUND`, not proof of external novelty.

## 12. Current research significance

The strongest surviving coupled object is no longer best described as two separate observations S3 and S6.

It is one split-hyperbola bridge theorem with two readouts:

1. **sample incidence** — arithmetic arrangement exceptions;
2. **orbit quotient** — global transparency / breaker phase.

For the native tri-sector model this gives a unified interpretation of the chain

`3 -> 5 -> 9 / 53`

while keeping the distinct roles of `9` (breaker-coprime/native incidence capacity) and `53` (finite-window local exception) explicit.