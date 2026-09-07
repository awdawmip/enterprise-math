# BRC Boundary Phase = Classical Linear-Combination Factor Bridge

Status: `RESEARCH FRONTIER / EXACT PRIOR-ART IDENTIFICATION + ROUTE CLOSURE / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parents:
- `research_notes/BRC_EULER_PHASE_SHADOW_TRACE_COLLAPSE_20260908.md`
- `research_notes/BRC_MULTIPLIER_FACTOR_BRIDGE_20260906.md`
Source snapshot before write: `main@d8ca3c235f1ad65378e6197595032164ab6f21c3`

## 0. Purpose

The remaining phase-BRC question was whether hidden multiplier boundaries furnish a candidate family structurally different from the Lehman/Hittmeir/Harvey linear-combination searches used in modern deterministic factoring.

They do not: the hidden BRC boundary exponent is literally the same integer linear form. The corresponding modulo-one-factor phase bridge is also exact and N-only on the public side. This identifies the direct multiplier-phase continuation as prior-art-equivalent at the level of its search object.

---

## 1. Boundary exponent identity

For odd split parameters `a,b`, the hidden boundary is

`L_(a,b)=(a*p+b*q-2)/2`.

Therefore

`X_(a,b):=2*L_(a,b)+2=a*p+b*q`.

So every BRC boundary candidate is exactly one Lehman-type linear form in the unknown factors.

Exchange of the split gives

`X_(b,a)=b*p+a*q`.

In `(S,g)` coordinates, with

`d=(a+b)/2`, `c=(a-b)/2`,

one has

`X_(a,b)=d*S-c*g`,

`X_(b,a)=d*S+c*g`.

Thus the composite multiplier lattice is simply a public integer family of linear combinations of the same two hidden coordinates.

---

## 2. Exact public phase bridges modulo the two factors

Fix any unit

`alpha in (Z/NZ)^*`, `N=pq`.

Let

`X=a*p+b*q`.

Modulo `p-1`, we have

`p == 1`, `N=pq == q`.

Hence

`X=a*p+b*q == a+b*N (mod p-1)`.

By Fermat/Euler on the p-component,

`alpha^X == alpha^(a+b*N) (mod p)`.

Similarly, modulo `q-1`,

`q == 1`, `N == p`,

so

`X == a*N+b (mod q-1)`

and

`alpha^X == alpha^(a*N+b) (mod q)`.

Therefore the two public N-only phase anchors are

`P_p(a,b)=alpha^(a+b*N) mod N`,

`P_q(a,b)=alpha^(a*N+b) mod N`,

with the exact hidden-factor congruences

`alpha^X == P_p(a,b) (mod p)`,

`alpha^X == P_q(a,b) (mod q)`.

---

## 3. Factor witness from the correct linear-form exponent

If a candidate integer `x` equals the hidden linear form

`x=X=a*p+b*q`,

then

`p | alpha^x-P_p(a,b)`

and

`q | alpha^x-P_q(a,b)`.

Hence

`gcd(alpha^x-P_p(a,b),N)`

contains `p`, and the analogous second gcd contains `q`. In nondegenerate cases the first gcd is exactly `p` and the second exactly `q`; a total gcd is a collision/degeneracy requiring the usual separate handling.

So once the hidden boundary exponent is found, the phase bridge returns a factor without reconstructing the actual boundary geometry.

This is precisely the kind of modular-factor collision exploited in deterministic linear-combination factoring methods.

---

## 4. Relation to the diagonal Euler phase

When `a=b`,

`X=a*S`.

The two public anchors coincide:

`a+b*N = a*N+b` only modulo the respective factor-order relations, and globally the phase reduces to the Euler relation

`alpha^(a*S)=alpha^(a*(N+1))`.

For `a!=b`, the public phase splits into two factor-specific anchors. The missing information is exactly the hidden gap/orientation component

`c*g`.

This explains why the diagonal `S` phase is globally N-only while non-diagonal boundary phases are not: the latter separate into different p- and q-component exponent reductions.

---

## 5. Exchange pair and hidden gap phase

For the exchange pair,

`X_-=d*S-c*g`,

`X_+=d*S+c*g`.

Their phase product is globally known through the Euler shadow:

`alpha^(X_-+X_+)=alpha^(2*d*S)=alpha^(2*d*(N+1))`.

But the quotient

`alpha^(X_+-X_-)=alpha^(2*c*g)`

contains the hidden gap phase.

So product/symmetric collapse removes precisely the orientation-bearing phase that distinguishes the two factor components. This is the group analogue of the square-gap sign loss already proved in the integer BRC bridge.

---

## 6. Prior-art identity and route classification

Harvey's exponent-one-fifth paper explicitly reviews deterministic factoring based on:

- Lehman-type small linear combinations `a*q+b*p`;
- modular power relations derived from Fermat/Euler;
- global baby-step/giant-step collision searches over candidate linear forms.

Up to exchanging the coefficient names, the BRC boundary exponent

`a*p+b*q`

is exactly that object.

Therefore the following continuations are **not** new candidate families:

- increasing the composite multiplier horizon `(a,b)` and searching the associated boundaries by group phase;
- applying ordinary BSGS to `2L_(a,b)+2`;
- replacing the explicit phase by its exchange-pair trace and then using Lucas/Chebyshev recurrence;
- applying the previously explored cyclic/Frobenius multiresolution machinery to the same linear-form phase family without a new scale theorem.

They may still be useful implementation lenses, but they inherit the established deterministic factorisation baseline.

---

## 7. Existing Frobenius/X6 boundary reinforces the closure

The project already contains a dedicated X6/Frobenius multiresolution factorisation frontier. Its generic-semiprime experiments and exact reductions found:

- scalar cyclic periods fall into multiplicative-order/Pollard-p-1 territory;
- cyclic/Frobenius layer width empirically tracks the smaller factor (`R=Theta(p)`) on generic balanced semiprimes;
- multiresolution divisor/cyclotomic reuse is useful for special families but does not provide a generic factoring breakthrough;
- the generic route is closed unless the factor-scale width wall is broken.

The new exchange-trace proposal lies inside the same Lucas/Frobenius/multiplicative-order semantic family and does not currently break that scale wall.

---

## 8. What would count as genuinely new candidate compression

Since the direct boundary family is prior-art-identical, a BRC advance must prove a theorem that changes the **guaranteed population** before phase collision.

Examples of qualifying progress would be:

1. a strict N-only rule selecting a subset of coefficient pairs `(a,b)` whose cardinality is asymptotically smaller than the best known Harvey/Hittmeir parameterization while still guaranteeing a factor-bearing linear form;
2. a new BRC relation that combines many `(a,b)` directions into one phase/gcd test with construction cost sublinear in the covered candidate population;
3. a magnitude/order invariant that narrows the factor ratio by a growing power and thereby shrinks the linear-combination family before BSGS;
4. a non-classical implicit phase operator beating the explicit `sqrt(C)` support wall.

Merely proving that `a/b` approximates `q/p`, or that some multiplier has a small square gap, is already the classical Lehman/Lawrence balancing mechanism.

---

## 9. Route decision

Freeze:

`BRC_HIDDEN_BOUNDARY_EXPONENT = LEHMAN_TYPE_LINEAR_FORM`.

`DIRECT_BOUNDARY_PHASE_SEARCH = CLASSICAL_LINEAR_COMBINATION_PHASE_SEARCH`.

`COMPOSITE_MULTIPLIER_EXPANSION_WITHOUT_NEW_SELECTION_THEOREM -> NO_NEW_CANDIDATE_DIMENSION`.

Therefore the direct phase continuation is closed at the present frontier. The two still-open algorithmic possibilities are:

- a genuinely new N-only candidate-selection/preconditioning theorem; or
- a genuinely new collective/implicit collision constructor crossing the quantitative phase boundary already derived.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.