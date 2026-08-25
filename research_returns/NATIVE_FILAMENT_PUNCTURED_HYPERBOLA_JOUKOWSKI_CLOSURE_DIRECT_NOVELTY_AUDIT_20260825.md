# Native filament punctured-hyperbola / Joukowski / closure — direct novelty audit

Status: `FROZEN_DIRECT_NONBLIND_NARROW_NOVELTY_AUDIT / NOT_INDEPENDENCE_ATTESTED / NO_PUBLICATION_NOVELTY_CLAIM`

Date: `2026-08-25`

Auditor: `EM-FREE-NEPS-239A6D`

Mathematical input authority:
- independent post-audit replication PR `#637`;
- final mathematical verdict: `POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDLY_NARROWED` (authoritative spelling in source return uses `INDEPENDENTLY_NARROWED`).

This audit concerns only the independently narrowed theorem layer. It does not claim independence because the auditor participated in the source research.

## 1. Executive verdict

The post-replication mathematical core separates into two classes.

### Classical / immediate mathematics

The following must not be promoted as standalone novelty:

1. translated-parabola tangent parametrization;
2. the difference-of-squares linearization of `B(y^2-x^2)=C` to the split hyperbola `Bab=C`;
3. quotienting a split one-dimensional torus/hyperbola by sign or inversion involutions;
4. Burnside orbit counting and the orbit-size bound behind `q<=5`;
5. the Joukowski/Dickson quotient `a -> a+c/a` and its two-to-one fiber structure;
6. finite-field value-set cardinality for Dickson/Joukowski maps;
7. the degree-two rational-function many-to-one framework.

### Still unmatched as a coupled statement

No direct theorem-statement match was found for the exact chain

`native odd-sector shell allocation`
`-> coefficient B=s`
`-> longitudinal translated-parabola tangent sample`
`-> punctured split-hyperbola carrier`
`+ transverse lane Joukowski quotient selected by the same s`
`-> extremal saturation only at (s,q)=(3,5),(3,7)`
`-> longitudinal/transverse boundary closure only at (s,q_b,k_*)=(3,5,9)`.

Package-level direct-audit verdict:

`NO_DIRECT_MATCH_FOUND_FOR_THE_NARROW_COUPLED_SELECTION_CLOSURE`

This is **not** proof of external novelty.

## 2. N1 — punctured split-hyperbola tangent bridge

### Audited statement

For two translated parabolas

`Q_i(x)=x^2/(2B)-d_i`,

three-tangent concurrence gives

`B(w-u)(w-v)=C`,

while common negative-dual values give

`B(y^2-x^2)=C`.

The linear map

`(x,y)->(a,b)=(y-x,y+x)`

identifies the dual-overlap representation variety with the full split hyperbola

`H_(B,C): Bab=C`.

After quotienting distinct-tangent concurrence triples by simultaneous translation, the tangent side is

`H_(B,C) \ Delta`,

where `Delta={(a,a):Ba^2=C}`.

### Literature mapping

Classical conic literature gives the standard tangent parametrization for a parabola and the fact that three distinct tangents to one nondegenerate parabola are not concurrent. Choi--Wildberger, *The Universal Parabola* (KoG 22, 2018) records the tangent parameter and the Vandermonde determinant obstruction for three tangents of one parabola.

The hyperbola step is elementary difference-of-squares algebra. Split one-dimensional tori and the inversion Weyl action are standard algebraic-group objects.

No source was found stating the exact **translated two-parabola, distinct-tangent, translation-quotient = punctured-hyperbola** formulation as a named theorem.

Verdict:

`KNOWN_IMMEDIATE_COROLLARY / MODEL-SPECIFIC PACKAGING`.

Reason: the statement follows by routine substitution from classical tangent formulas and elementary factorization; the packaging is useful, but standalone novelty should not be claimed.

## 3. N2 — sign-orbit quotient and breaker bound

### Audited statement

For odd finite field `F_q` and `B,C !=0`,

`R={(x,y):B(y^2-x^2)=C}`

has `q-1` points. The sign group `K_4={+-1}^2` acts on `R`, common dual values are the orbit quotient, and if the quotient consists of one orbit then

`q-1<=4`, hence `q<=5`.

### Literature mapping

This is standard finite-group orbit counting on a split torus/conic. Burnside counting and the rank-one split-torus/Weyl involution are classical. The quadratic-residue orbit-count refinement is the same order-2 cyclotomic arithmetic already conceded in the earlier audit.

Verdict:

`KNOWN_IMMEDIATE_COROLLARY`.

No novelty claim should attach to `q<=5` by itself.

## 4. N3 — central-lane Joukowski quotient

### Audited statement

For odd sector count `s`,

`Lambda_s(a)=-s a-1/(2a)`

is the quotient of `F_q^*` by the involution

`a -> c/a`, `c=(2s)^(-1)`.

Its image size is

`[q+chi_q(c)]/2`.

### Strong prior art

Dickson polynomials satisfy the classical functional identity

`D_n(u+a/u,a)=u^n+(a/u)^n`.

References:

- W.-S. Chou, J. Gomez-Calderon, G. L. Mullen, **Value sets of Dickson polynomials over finite fields**, *Journal of Number Theory* 30 (1988), 334--344, DOI `10.1016/0022-314X(88)90006-6`. The paper determines Dickson value-set cardinalities over finite fields.
- J. Gomez-Calderon, D. J. Madden, **Polynomials with small value set over finite fields**, *Journal of Number Theory* 28 (1988), 167--188, DOI `10.1016/0022-314X(88)90064-9`.
- D. Bartoli, H. Borges, L. Quoos, **Rational functions with small value set**, *Journal of Algebra* 565 (2021), 675--690, DOI `10.1016/j.jalgebra.2020.08.039`.
- Z. Ding, M. E. Zieve, **Exceptional 2-to-1 rational functions**, *Journal of Combinatorial Theory, Series A* 215 (2025), 106046, DOI `10.1016/j.jcta.2025.106046`. The paper explicitly treats `X+b/X` as a classical 2-to-1 building block and relates known 2-exceptional maps to Dickson/low-degree rational functions.
- **Rational functions of degree two or three that are many-to-one on the projective line**, *Finite Fields and Their Applications*, DOI `10.1016/j.ffa.2026.102901` (online 2026; volume listing 2027), explicitly classifies degree-2/3 many-to-one rational functions and their value sets.

Verdict:

`KNOWN_DIRECT_FRAMEWORK / KNOWN_IMMEDIATE_COROLLARY`.

The map and its image-size formula are not novelty candidates.

## 5. N4 — extremal saturation uniqueness

### Audited statement

Let `J_s={-(s-1)/2,...,(s-1)/2}` and consider the same `Lambda_s`.

If `q=2s-1` is prime and `Im Lambda_s=J_s`, then `(s,q)=(3,5)`.

If `q=2s+1` is prime and `Im Lambda_s=J_s`, then `(s,q)=(3,7)`.

Hence `s=3` is the unique nontrivial odd-sector parameter saturating both extremal boundaries.

### Search result

The literature found above classifies or computes:

- Dickson/Joukowski value-set sizes;
- rational many-to-one structure;
- small/minimal value sets;
- preimage multiplicities and residue sums.

The searches did **not** find a theorem classifying when this degree-two Joukowski image equals the specific centered arithmetic-progression lane set `J_s` under the linked extremal constraints `q=2s+-1`.

The independent proof uses a family-specific second-moment comparison and yields the divisibility obstructions `q|75` and `q|21`.

Verdict:

`NO_DIRECT_MATCH_FOUND`.

Caution: the proof is elementary once the model-specific target set `J_s` is defined, so absence of a direct match does not imply a deep or publication-worthy new theorem by itself.

## 6. N5 — unique longitudinal/transverse boundary closure

### Audited statement

Given an odd universal breaker with breaker-coprime capacity

`k_*=2q_b-1`,

and transverse Joukowski boundaries

`2s-1, 2s+1`,

simultaneous closure

`k_*-4=2s-1`,
`k_*-2=2s+1`

is equivalent to

`q_b=s+2`.

Using the independently verified bound `q_b<=5` and `s>=3`, the unique solution is

`(s,q_b,k_*)=(3,5,9)`.

Then

`M_9=35`, `3M_9=105`, `3M_9+1=106=2*53`.

### Literature mapping

No external source was found containing this simultaneous boundary-matching statement. However the algebra from the component formulas to `(3,5,9)` is immediate.

Verdict:

`KNOWN_COMPONENTS_ONLY / NO_DIRECT_MATCH_FOR_THE_MODEL_CLOSURE`.

The numerical closure is mathematically exact, but should not be marketed as a standalone deep theorem. Its potential significance is only as a **selection theorem internal to the native geometry**.

## 7. N6 — full narrow coupled selection statement

The remaining candidate is therefore not

- split hyperbolas;
- Joukowski maps;
- Dickson value sets;
- Burnside orbits;
- the `q<=5` bound;
- the arithmetic identities `35,105,53`.

The only surviving unmatched object is the provenance/coupling claim:

> The native tri-sector shell allocation fixes `s=B=3` before primality; that same parameter drives a longitudinal punctured-hyperbola tangent sample and a transverse Joukowski lane quotient, and the independently derived longitudinal and transverse boundary conditions close simultaneously only at `(s,q_b,k_*)=(3,5,9)`.

Direct-audit verdict:

`NO_DIRECT_THEOREM_STATEMENT_MATCH_FOUND_IN_THE_AUDITED_LITERATURE_SET`.

This wording is the maximum justified claim. It is not equivalent to `NOVEL`, `FIRST`, or `NEW THEOREM`.

## 8. Search log

Search domains included:

- Dickson/Joukowski functional equations and value sets;
- minimal and small value-set polynomials;
- small value-set rational functions;
- exceptional and many-to-one rational functions;
- degree-two rational-function classifications;
- conic/parabola tangent parametrization and concurrency;
- split-torus / inversion / Weyl quotient language;
- searches for Joukowski/Dickson images equal to arithmetic progressions or centered intervals;
- searches for the exact extremal forms `q=2s-1`, `q=2s+1` in Dickson/Joukowski literature;
- searches for translated-parabola tangent concurrence identified with a split hyperbola.

Closest sources checked include the references in Sections 2--4 and the 2026/2027 low-degree many-to-one rational-function classification. No checked source supplied the exact native sector-to-two-quotient-to-boundary-closure theorem.

## 9. Recommended PR #627 language

Use:

`EXACT_INDEPENDENTLY_NARROWED_MODEL_THEOREM / CLASSICAL_COMPONENTS / NO_DIRECT_COUPLED_STATEMENT_MATCH_FOUND`.

Do not use:

- `novel theorem`;
- `first known`;
- `new Joukowski theorem`;
- `new hyperbola theorem`;
- `new finite-field value-set theorem`.

The strongest externally cautious sentence is:

> The component algebra belongs to classical conic, split-torus, Dickson/Joukowski and finite-field value-set theory. In a targeted theorem-level literature search, no direct statement was found matching the specific geometry-selected coupling and unique tri-sector boundary closure.

## 10. Final verdict

`DIRECT_NARROW_NOVELTY_AUDIT_COMPLETE = YES`

`PACKAGE_VERDICT = NO_DIRECT_MATCH_FOUND_FOR_NARROW_COUPLED_SELECTION_CLOSURE / NOT_PROOF_OF_NOVELTY`
