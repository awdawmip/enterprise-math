# Driver Review — Native Filament Post-audit Hyperbola/Joukowski Independent Replication

Status: `DRIVER_ACCEPTED_WITH_NARROWING / INDEPENDENT_POSTAUDIT_CLOSURE_VERIFIED / SOURCE_V2_REPAIR_PRESENT / NOT_CANONICAL_PROMOTION`

Date: `2026-08-25`

Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`

Task:
`RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`

Audit PR:
`#637`

Owner branch/head:
`audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825@6e128df1f6bda6ab000f78cd07b99ef01d3dbaa4`

Researcher-ID:
`EM-POSTHJ-EE1141`

Taskbook blob:
`0e461007e74be40ee0bc783fb0273cb96ece1866`

Blind packet blob:
`6ce9ea10f02fded1959c55a1b78044ada434360f`

Frozen return blob:
`3c9937897aafccef8a26836b58be949fa6ecb0e4`

Independent checker blob:
`aaa302d24f300f178a4a09ad665766e8a62beb4d`

## 1. Driver verdict

The frozen hard-target verdict

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`

is accepted.

The post-audit algebraic closure survives independent blind reconstruction, but only after three controlling statement repairs:

1. distinct-tangent concurrence modulo simultaneous translation is a **punctured** split hyperbola, not unconditionally the full split hyperbola;
2. for arbitrary odd finite fields, H2 must use the field quadratic character `chi_q`; literal Legendre notation is restricted to odd prime fields;
3. the blind C3/105 replication establishes exact lane formulas and the integer coincidence `3 M_9=105`, but not a stronger historical/genealogical common-provenance claim absent additional native input.

No further narrowing is required for J1, J2, or C1.

## 2. H1 split-hyperbola bridge

For `char(K) != 2`, `B != 0`, `d_i != d_(1-i)`, and

`C_i=2(d_i-d_(1-i))`,

the independent derivation correctly proves:

- tangent concurrence for distinct slopes:
  `B(w-u)(w-v)=C_i`;
- negative-dual overlap:
  `B(y^2-x^2)=C_i`;
- the linear isomorphism
  `(x,y) -> (a,b)=(y-x,y+x)`
  from the dual-overlap variety to
  `H_(B,C_i)={(a,b):Bab=C_i}`.

The original final bridge was too strong. If

`X_i={(u,v,w):u!=v, B(w-u)(w-v)=C_i}`,

then quotienting by simultaneous translation gives exactly

`X_i / G_a ~= H_(B,C_i) \ Delta_i`,

where

`Delta_i={(a,a):Ba^2=C_i}`.

The reason is exact:

`u!=v <=> (w-u)!=(w-v) <=> a!=b`.

The return's rational counterexample is valid: with `K=Q`, `B=1`, `d_i=1/2`, `d_(1-i)=0`, the dual-overlap point `(x,y)=(0,1)` maps to `(a,b)=(1,1)` on `ab=1`, but any tangent-difference realization with `a=b` forces `u=v`.

Thus the controlling wording is:

`DISTINCT_TANGENT_BRIDGE = PUNCTURED_SPLIT_HYPERBOLA`.

The full hyperbola is recovered only when the diagonal has no `K`-points or when repeated tangents are explicitly admitted.

## 3. H2 finite-field sign quotient

For odd finite field `F_q` and nonzero `B,C`, the return correctly establishes

`|R|=q-1`,

where

`R={(x,y):B(y^2-x^2)=C}`.

For the sign group `G={+/-1}^2`, Burnside gives

`|R/G|=[q+1+chi_q(BC)+chi_q(-BC)]/4`.

The common-dual-value interpretation requires the shift relation

`C=2(d_0-d_1)`

or an explicit choice of such shifts.

The independent orbit-capacity argument is also exact and does not depend on the character formula:

if `|R/G|=1`, then one orbit contains all `q-1` points while every orbit has size at most four, hence

`q-1<=4`,

so

`q<=5`.

The notation narrowing is mandatory: for general odd prime powers use `chi_q`; a Legendre symbol is appropriate only when `q` is an odd prime.

## 4. J1 exact Joukowski quotient

For odd `s>=3`, odd prime `q` with `q∤2s`, and

`P_(s,j)(m)=2s m^2+2jm+1`,

the lane condition at nonzero residue `a` is exactly

`j=Lambda_s(a)=-sa-1/(2a)`.

With

`c=(2s)^(-1)`,

`Lambda_s(a)=-s(a+c/a)`

and the fibers are exactly the orbits of the involution

`a -> c/a`.

Therefore

`|Im Lambda_s|=[q+Legendre(c,q)]/2`.

The saturation criterion against the central lane set `J_s` is accepted exactly at this stated prime-field scope.

## 5. J2 extremal saturation uniqueness

The independent second-moment argument is accepted.

For the lower extremal boundary `q_-=2s-1` prime, saturation forces

`q_- | 75`,

and the stated congruence conditions leave only

`(s,q_-)=(3,5)`.

For the upper extremal boundary `q_+=2s+1` prime, saturation forces

`q_+ | 21`,

leaving only

`(s,q_+)=(3,7)`.

Direct finite-field pressure confirms both saturations occur for `s=3`; the checker reports no additional prime extremal saturation through `s<=101` and no saturation in its composite raw-boundary pressure set. These finite checks support the proof but do not replace it.

Thus the exact surviving theorem is:

`TRI_SECTOR_S3_IS_THE_UNIQUE_NONTRIVIAL_ODD_SECTOR_PARAMETER_SATURATING_BOTH_PRIME_EXTREMAL_JOUKOWSKI_BOUNDARIES`.

## 6. C1 longitudinal/transverse boundary closure

Assume an odd universal breaker `q_b` has breaker-coprime capacity

`k_*=2q_b-1`

and the independently established bound `q_b<=5`.

The two closure equations

`k_*-4=2s-1`,
`k_*-2=2s+1`

are each equivalent to

`q_b=s+2`.

With odd `s>=3` and `q_b<=5`, the unique solution is

`(s,q_b,k_*)=(3,5,9)`.

The exact arithmetic chain is

`M_9=(9-4)(9-2)=35`,
`3M_9=105`,
`3M_9+1=106=2*53`.

This remains a breaker-coprime capacity statement; it does not by itself establish an unrestricted prime-run theorem and does not replace the separate native typed-Cell prime-incidence theorem.

## 7. C2 provenance narrowing

At `s=3`, the three central lane polynomials are exactly

`6m^2-2m+1`,
`6m^2+1`,
`6m^2+2m+1`.

The arithmetic identity `3M_9=105` is exact.

What the blind packet does **not** establish is a stronger statement that the bouquet-gate `105` and the longitudinal closure `105` arise from one previously proved historical/genealogical mechanism. The independent result certifies exact formula-level and integer-level coincidence only.

Any stronger native-provenance identification requires additional explicitly admitted native input.

## 8. Independence and source-repair audit

The audit branch contains the statement-only packet/taskbook, an independently written standard-library checker, and the frozen return. The return attests that PR #627/source proofs/checkers were not read before freeze.

The Driver found no evidence contradicting that frozen independence boundary.

Post-freeze comparison is now permitted. The source branch has already absorbed the independent corrections in:

`research_notes/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_V2_STATEMENT_FREEZE_20260825.md`

with blob

`f45780b5d93bbde446c9b19abdc49ec13f09e4f1`.

That source authority correctly freezes:

- the punctured-hyperbola distinct-tangent statement;
- finite-field quadratic-character notation;
- the C3/105 provenance narrowing;
- exact J1/J2/C1 surviving statements.

Therefore:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_SOURCE_REPAIR = CLOSED`.

## 9. Scope / promotion boundary

Accepted:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION = PASS_WITH_NARROWING`

`H1_SPLIT_HYPERBOLA_CORE = VERIFIED`

`H2_SIGN_ORBIT_CORE = VERIFIED_WITH_CHARACTER_SCOPE`

`J1_JOUKOWSKI_QUOTIENT = VERIFIED`

`J2_EXTREMAL_UNIQUENESS = VERIFIED`

`C1_UNIQUE_359_CLOSURE = VERIFIED`

`C2_LANE_AND_105_COINCIDENCE = VERIFIED_WITH_PROVENANCE_NARROWING`

Not accepted by this review:

- publication-level historical novelty;
- a claim that all split-hyperbola points are distinct-tangent concurrence classes;
- use of Legendre notation over arbitrary prime-power fields without translation to the quadratic character;
- a stronger native genealogy for `105` not supplied by the blind packet;
- unrestricted prime-run interpretation of the capacity `9`;
- Foundation/canonical promotion of PR #637 itself.

PR #637 should remain a Draft independent-evidence surface.

## 10. Closure

`HARD_TARGET = SATISFIED_WITH_NARROWING`

`DRIVER_REVIEW = PASS_WITH_NARROWING`

`INDEPENDENT_RETURN_ACCEPTED = true`

`SOURCE_V2_REPAIR_PRESENT = true`

`EXTERNAL_NOVELTY_RESOLVED = false`

`SUCCESSOR_AUTOMATICALLY_OPENED = false`

This closes Driver review of the post-audit Hyperbola/Joukowski mathematical replication only.