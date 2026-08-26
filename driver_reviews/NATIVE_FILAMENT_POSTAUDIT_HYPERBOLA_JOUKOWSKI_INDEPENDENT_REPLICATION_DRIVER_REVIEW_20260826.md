# Driver Review — Native Filament Post-audit Hyperbola/Joukowski Independent Replication

Status: `DRIVER_ACCEPTED_WITH_NARROWING / HARD_TARGET_CLOSED / SOURCE_REPAIR_PRESENT / NOT_CANONICAL_PROMOTION`

Date: `2026-08-26`

Driver-ID: `EM-DVR-R63A21 / CONTROL_PLANE`

Task:
`RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`

Audit PR: `#637`

Audit branch/head:
`audit/native-filament-postaudit-hyperbola-joukowski-replication-20260825@6e128df1f6bda6ab000f78cd07b99ef01d3dbaa4`

Researcher-ID:
`EM-POSTHJ-EE1141`

Frozen return:
`research_returns/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_RETURN_20260825.md`

Return blob:
`3c9937897aafccef8a26836b58be949fa6ecb0e4`

Blind packet blob:
`6ce9ea10f02fded1959c55a1b78044ada434360f`

Taskbook blob:
`0e461007e74be40ee0bc783fb0273cb96ece1866`

Independent checker:
`research_checks/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_CHECKER_20260825.py`

Checker Git blob:
`aaa302d24f300f178a4a09ad665766e8a62beb4d`

Checker SHA256 recorded by the return:
`03cd9a185dab0eacdf65b927a9c4c629d764d6289959b99c4524f187b230d52d`

## 1. Driver verdict

The frozen independent verdict

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_NARROWED`

is accepted.

The hard target

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

is satisfied by a mathematically substantive `PASS_WITH_NARROWING` outcome.

Accepted row classification:

- `H1 = VERIFIED_WITH_NARROWING`;
- `H2 = VERIFIED_WITH_NARROWING`;
- `J1 = VERIFIED_EXACT`;
- `J2 = VERIFIED_EXACT`;
- `C1 = VERIFIED_EXACT`;
- `C2 = VERIFIED_WITH_NARROWING`.

No additional theorem-strength upgrade is authorized by this review.

## 2. H1 — mandatory full-torsor repair

The algebraic subclaims are exact:

1. for distinct `u,v`, tangent concurrence is equivalent to
   `B(w-u)(w-v)=C_i`;
2. common negative-dual values are represented by
   `B(y^2-x^2)=C_i`;
3. `Phi(x,y)=(y-x,y+x)` identifies the dual-overlap representation variety with
   `H_(B,C_i)={(a,b):Bab=C_i}`.

However the original concluding bridge was too strong.

For

`X_i={(u,v,w):u!=v, B(w-u)(w-v)=C_i}`

and simultaneous translation by `G_a`, the difference map gives exactly

`X_i/G_a ~= H_(B,C_i) \ Delta_i`,

where

`Delta_i={(a,a):Ba^2=C_i}`.

The reason is structural, not computational:

`u!=v <=> (w-u)!=(w-v) <=> a!=b`.

The return's rational pressure witness is valid:

`K=Q, B=1, d_i=1/2, d_(1-i)=0, C_i=1`.

The dual pair `(x,y)=(0,1)` maps to `(a,b)=(1,1)` on the hyperbola, but any tangent-difference realization of `(1,1)` forces `u=v`, contradicting the distinct-tangent hypothesis.

Therefore the controlling statement is:

`DISTINCT_TANGENT_QUOTIENT = PUNCTURED_SPLIT_HYPERBOLA`.

The full hyperbola is recovered only when the diagonal has no `K`-points, or when repeated tangents are explicitly admitted with the corresponding semantics.

## 3. H2 — finite-field domain / common-dual repair

The finite-field hyperbola count and sign-orbit calculation are exact after making the domain precise.

For an odd finite field `F_q` and `B,C != 0`:

`|R|=q-1`,

and with the quadratic character `chi_q`,

`|R/G|=[q+1+chi_q(BC)+chi_q(-BC)]/4`.

If `q` is an odd prime, `chi_q` may be written as the Legendre symbol. A literal Legendre-symbol formulation must not be presented as covering arbitrary odd prime powers.

The phrase “common dual-value set” additionally requires shifted quadratics satisfying

`C=2(d_0-d_1)`

(or an explicitly equivalent choice). The bare pair `(B,C)` does not by itself name those two dual maps.

The orbit-capacity consequence remains exact and independent of the explicit character formula:

`|R/G|=1 => q-1<=4 => q<=5`.

## 4. J1/J2 — accepted exactly

The lane map

`Lambda_s(a)=-sa-1/(2a)`

is exactly the quotient of `F_q^*` by the involution

`a -> c/a`, `c=(2s)^(-1)`

under the stated good-prime assumptions. Hence

`|Im Lambda_s|=[q+Legendre(c,q)]/2`

for odd prime `q`, and complete lane saturation is equivalent to

`Im Lambda_s subseteq J_s`.

The extremal uniqueness proof is also exact. Under lower-extremal saturation `q=2s-1`, the independent second-moment calculation forces `q|75`, hence `(s,q)=(3,5)`. Under upper-extremal saturation `q=2s+1`, it forces `q|21`, hence `(s,q)=(3,7)`. Direct pressure confirms both saturations at `s=3`.

The Driver independently re-enumerated prime extremals for every odd `3<=s<=301`; the only saturating pairs remained `(3,5)` and `(3,7)`. This is supporting pressure only; the universal result is carried by the second-moment proof.

## 5. C1 — exact boundary closure

The two boundary equations

`k_*-4=2s-1`,
`k_*-2=2s+1`

with

`k_*=2q_b-1`

are equivalent to

`q_b=s+2`.

Under the inherited nontrivial odd-sector condition `s>=3` and the independently established odd-breaker bound `q_b<=5`, the unique solution is

`(s,q_b,k_*)=(3,5,9)`.

At that solution:

`M_9=35`,
`3M_9=105`,
`3M_9+1=106=2*53`.

This remains explicitly a breaker-coprime-capacity closure. It does not become an unrestricted nine-prime-run theorem and does not replace the separate native typed-Cell prime-incidence island theorem.

## 6. C2 — evidence-strength narrowing, not refutation of the broader source note

From the blind packet's own lane polynomial,

`P_(s,j)(m)=2sm^2+2jm+1`,

specializing `s=3`, `j=-1,0,1` gives exactly

`6m^2-2m+1`,
`6m^2+1`,
`6m^2+2m+1`.

The packet also gives the even-shell `h=0` central-filament value `6m^2+1`, so the middle-lane equality is independently certified.

Likewise

`3M_9=105`

is exact.

What this blind replication does **not** certify is a stronger genealogical/causal statement that the bouquet-gate definition and tangent-extremum definition arise from one already-specified native mechanism. That requires additional native shell-fiber/slot inputs not included as proof data in the blind packet.

This is an evidence-scope narrowing. It does not refute the broader source note, which separately supplies additional native carrier definitions and may prove a stronger C3-unfolding statement from those extra inputs.

## 7. Checker and pressure evidence

The frozen return records an actual standard-library execution of

`python3 research_checks/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_CHECKER_20260825.py`

with terminal output

`INDEPENDENT_CHECKER_PASS`.

Recorded pressure includes:

- H1: 8,000 distinct-slope triples over `F_5` and 74,088 over `F_7`;
- H2: all nonzero `(B,C)` pairs for `q=5,7,13,53`;
- J1: all 167 valid `(s,q)` pairs with odd `s<=15`, prime `q<=101`, `q∤2s`;
- J2: all prime extremal cases through odd `s<=101`;
- explicit q=2, C=0, s=1 and divisor-boundary controls;
- exact C1/C2 integer arithmetic.

The Driver independently rederived the H1 diagonal obstruction and J2 extremal uniqueness and found no additional defect.

Finite pressure is not used as a substitute for the symbolic H1/H2/J1/J2/C1 proofs.

## 8. Independence / identity boundary

The taskbook required a fresh runtime identity and forbade reuse of the originating free-research identity or the #631 audit identity.

The return uses

`EM-POSTHJ-EE1141`

and attests that only the statement-only blind packet and taskbook were used before freeze. The source branch later records this identity explicitly as the independent replicator in the post-replication V2 statement freeze.

No pre-freeze dependence on PR #627 source proofs/checkers is evidenced by the audit branch. The earlier nonblind adversarial check is separately labelled non-independence evidence and is not counted toward this verdict.

## 9. Post-freeze source reconciliation

After the independent return froze, the source branch created:

`research_notes/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_V2_STATEMENT_FREEZE_20260825.md`

with blob

`f45780b5d93bbde446c9b19abdc49ec13f09e4f1`.

That statement layer correctly absorbs the independent repairs:

- Theorem A: distinct tangent bridge is the punctured split hyperbola;
- Theorem B: quadratic character for general odd finite fields, Legendre only for prime fields, and explicit shift relation for the dual-value interpretation;
- Theorem C/D/E: J1, J2 and C1 retained at exact strength;
- Corollary F: exact lane formulas and integer-105 coincidence retained, stronger genealogical claims guarded.

Therefore:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_SOURCE_STATEMENT_REPAIR_PRESENT = true`.

This is a source-branch statement repair, not a Foundation or current-main canonical promotion.

## 10. Final state

Accepted:

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION = PASS_WITH_NARROWING`

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_HARD_TARGET = CLOSED`

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_SOURCE_STATEMENT_REPAIR_PRESENT = true`

Not accepted:

- unqualified full-hyperbola tangent/dual identification under distinct tangents;
- Legendre notation over arbitrary odd prime powers;
- C2 genealogy/provenance beyond the inputs independently exposed;
- external novelty;
- Foundation promotion;
- automatic canonical merge of PR #637 or PR #627;
- unrestricted prime-run or factoring claims.

`SUCCESSOR_AUTOMATICALLY_OPENED = false`

Stop after this Driver review.