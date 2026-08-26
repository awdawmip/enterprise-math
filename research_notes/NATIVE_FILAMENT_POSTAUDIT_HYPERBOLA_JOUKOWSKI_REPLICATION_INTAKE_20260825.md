# Post-audit hyperbola/Joukowski blind replication intake

Status: `FROZEN_AUDIT_INTAKE / SOURCE_REPAIR_REQUIRED`

Date: `2026-08-25`

Originating Researcher-ID: `EM-FREE-NEPS-239A6D`

Independent replication:
- PR `#637`
- Researcher-ID `EM-POSTHJ-EE1141`
- return: `research_returns/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_RETURN_20260825.md`
- return branch head at intake: `6e128df1f6bda6ab000f78cd07b99ef01d3dbaa4`

Frozen independent verdict:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`.

## Surviving exact core

The independent replication verified at exact statement strength, subject to the narrowings below:

- H1a tangent concurrence equation;
- H1b negative-dual overlap equation;
- H1c linear split-hyperbola isomorphism;
- H2 finite-field point count / sign-orbit count / `q<=5` orbit-capacity breaker bound;
- J1 lane-label Joukowski quotient and image-size theorem;
- J2 extremal saturation uniqueness `(s,q)=(3,5)` and `(3,7)`;
- C1 unique boundary closure `(s,q_b,k_*)=(3,5,9)` and arithmetic `35 -> 105 -> 106=2*53`.

## Mandatory narrowing N1 — distinct tangent quotient is punctured hyperbola

The dual-overlap representation variety is the full split hyperbola

`H_(B,C)={(a,b):Bab=C}`.

For distinct tangents `u!=v`, after quotienting concurrence triples by simultaneous translation, the tangent-concurrence side is only

`H_(B,C) \ Delta`,

where

`Delta={(a,a):Ba^2=C}`.

Thus the previous unqualified wording

`TANGENT EXCEPTION <-> SAME FULL SPLIT HYPERBOLA <-> DUAL COVER`

is too strong.

Correct wording:

- dual-overlap representations = full `H_(B,C)`;
- distinct-tangent concurrence modulo translation = `H_(B,C)\Delta`;
- equality with the full hyperbola occurs iff `Delta(K)=empty`, or if repeated tangents are explicitly allowed.

## Mandatory narrowing N2 — finite-field character notation

For arbitrary odd finite fields `F_q`, use the quadratic character `chi_q`.

Literal Legendre-symbol notation is restricted to odd prime `q`.

The exact orbit formula is

`|R/{+/-1}^2|=[q+1+chi_q(BC)+chi_q(-BC)]/4`.

## Mandatory narrowing N3 — C2 provenance

The independent replication proves exactly:

- `s=3`, lanes `j=-1,0,1` give
  `6m^2-2m+1`, `6m^2+1`, `6m^2+2m+1`;
- the longitudinal closure integer satisfies `3*M_9=105`.

It does not, from the blind packet alone, certify a stronger causal/genealogical statement that the historical native `105` bouquet gate and the longitudinal `105` arise from one previously defined mechanism.

Safe statement:

`THE TWO INDEPENDENTLY DEFINED QUANTITIES COINCIDE EXACTLY AS THE INTEGER 105`.

A stronger provenance theorem requires separate input tying both definitions to one common native structure.

## Independent counterexample to the pre-audit full-torsor wording

Over `K=Q`, take `B=1`, `C=1` (e.g. shifts `d_i=1/2`, `d_(1-i)=0`).

The dual-overlap point `(x,y)=(0,1)` maps by `Phi` to `(a,b)=(1,1)` on `ab=1`.

But a tangent-difference realization would require

`w-u=1=w-v`,

hence `u=v`, contradicting the distinct-tangent hypothesis.

So the diagonal deletion is mathematically necessary, not editorial preference.

## Promotion rule

Any post-audit theorem package must use the narrowed theorem wording from the #637 return.

Do not promote the pre-replication split-hyperbola bridge verbatim.

External novelty remains unresolved; this intake is mathematical statement-strength control only.
