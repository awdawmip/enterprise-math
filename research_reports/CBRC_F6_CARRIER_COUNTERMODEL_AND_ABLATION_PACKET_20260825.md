# CBRC F6 — Carrier Countermodel and Ablation Packet

Researcher-ID: `EM-CBRCF6-D694C8`

Task-ID: `RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`

Status: `FINAL_FROZEN`

Mathematical source used before raw freeze: only `research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21`.

## Purpose

This packet records exact carrier witnesses and one-at-a-time ablations. It uses only additive groups and additive unary automorphisms. No multiplication, ring/field structure, norm, inner product, square law, two-slot mixing, external quantum structure, or named rank-two number system is introduced.

## Carrier witnesses

### M0 — least carrier

`C_min = Z e ⊕ Z f ⊕ <tau | 3 tau=0>`

with `pi(e)=e`, `pi(f)=pi(tau)=0`.

This realizes the full frozen upstream additive layer with no torsion beyond the inherited `tau`.

### M1 — extra cyclic torsion; full retract fails

`C_9 = Z e ⊕ Z f ⊕ <g | 9g=0>`, with `tau=3g`.

Then `tau` has exact order `3`, the old projection exists, and the upstream additive layer embeds. But every homomorphism `phi:Z/9->Z/3` kills `3g`, hence no `r:C_9->C1` can satisfy `r(tau)=tau`.

### M2 — extra noncyclic torsion

`C_33 = Z e ⊕ Z f ⊕ <tau | 3tau=0> ⊕ <u | 3u=0>`.

It satisfies the additive carrier conditions but is strictly worse than `C_min` in the issued torsion-minimality order.

### M3 — arbitrary extra finite spectators

For every finite abelian group `A`,

`C_A = C_min ⊕ A`

with `pi(A)=0` remains a rank-two additive carrier. Taking the inherited unary maps to act trivially on `A` gives valid extensions. Therefore extra torsion is never needed for unary realizability.

## Exact minimal-carrier unary normal form

On `C_min`, every projection-covariant lift is determined by

`R(f)=f+r tau`,
`J(f)=delta f+j tau`,
`S(f)=sigma f+s tau`,

where `r,j,s in Z/3` and `delta,sigma in {+1,-1}`.

The exact relation constraints are

`(delta-1)j=0`,
`(sigma-1)s=0`,
`(1+delta)r=0`,
`(sigma-1)(s-r)=0`

in `Z/3`.

This gives `22` raw parameter solutions. Quotienting by the allowed typed complement gauge

`f -> eps f + a tau`, `eps in {±1}`, `a in Z/3`,

leaves exactly `6` inequivalent lift classes.

The unique class minimizing additional unary structure is the class containing

`R(f)=f`, `J(f)=f`, `S(f)=f`.

It is the only orbit admitting a complement on which all three inherited unary maps act trivially.

## Mandatory ablation ledger

### A1 — primitive old generator

Verdict: `REDUNDANT_GIVEN_PI`.

With `pi:C->Z e` and `pi(e)=e`, the old free generator is automatically primitive. If `e=d x` in the free quotient with `|d|>1`, applying the integer coefficient of `pi` gives `1=d k`, impossible.

Checker regression: all nonzero vectors in `[-4,4]^2` were tested; `48` primitive vectors admit Bezout retractions and `32` nonprimitive vectors do not.

### A2 — preservation of order-three `tau`

Verdict: `ESSENTIAL`.

If `tau` is collapsed, the relative witness collapses:

`e+JRe=-tau=0`.

Thus preserving nonzero order-three `tau` is essential to the accepted upstream layer.

### A3 — old retraction `pi`

Verdict: `CLASSIFICATION_ENLARGES_WITHOUT_TYPED_PI`.

If no old projection is typed, integral `e`-shears on the new free direction become admissible. Exact witness:

`R(e)=e+tau`, `R(f)=f`, `R(tau)=tau`;
`J(e)=-e`, `J(f)=f`, `J(tau)=-tau`;
`S(e)=e`, `S(f)=3e-f`, `S(tau)=-tau`.

These maps satisfy `R^3=id`, `J^2=S^2=id`, `JR=RJ`, and `SRS^-1=R^-1`, while the shear is excluded by the typed projection covariance used in F6.

### A4 — full upstream retract

Verdict: `NOT_NEEDED_FOR_LEAST_CLASS`.

F6 does not use a full retract as a hypothesis for minimality. `C_min` admits one automatically, while `C_9` does not. Thus the stronger notion matters away from the minimum but does not change the least carrier.

### A5 — `R^3=id`

Verdict: `ESSENTIAL_FOR_LIFT_CLASS`.

Remove only `R^3=id`. Let the accepted upstream action remain unchanged and set

`R(f)=-f`, `J(f)=f`, `S(f)=f`.

All other unary relations and projection covariance hold, but `R^3(f)=-f!=f`. Hence the order-three relation is exactly what forbids this additional free sign for `R`.

### A6 — `JR=RJ`

Verdict: `ESSENTIAL_FOR_LIFT_CLASS`.

Remove only commutation. Set

`R(f)=f+tau`, `J(f)=f`, `S(f)=f`.

Then `R^3=id`, both involution relations, `SRS^-1=R^-1`, and projection covariance hold, but `JR(f)=f-tau` while `RJ(f)=f+tau`.

### A7 — `SRS^-1=R^-1`

Verdict: `ESSENTIAL_FOR_LIFT_CLASS`.

Remove only the conjugation law. Set

`R(f)=f+tau`, `J(f)=-f`, `S(f)=-f`.

Then `R^3=id`, `J^2=S^2=id`, `JR=RJ`, and projection covariance hold, but the `SRS^-1` relation fails on `f`.

### A8 — old-projection covariance

Verdict: `ESSENTIAL_FOR_LIFT_CLASS`.

Retain the additive map `pi` but drop covariance. The shear witness from A3 satisfies all unary group relations yet has

`pi(S(f))=3e != 0=pi(f)`.

Thus covariance removes genuine integral-shear classes rather than merely choosing notation.

### A9 — no-extra-torsion minimality preference

Verdict: `ESSENTIAL_FOR_UNIQUE_LEAST_CARRIER`.

Without this preference, the infinite family `C_min ⊕ Z/m`, `m>=2`, preserves the upstream layer and admits unary extensions. Their torsion orders `3m` already distinguish infinitely many pairwise nonisomorphic examples.

## Exact checker coverage

Checker:

`scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`

SHA-256:

`682c3ba50ede00bf5cad9ea948e03b8542f1d8a0ded927c2aef34664bd2e9b2a`

Result: `PASS`, exit code `0`.

The checker covers:

- finite-presentation/SNF witnesses `C_min`, `C_9`, and `C_33`;
- bounded primitive embeddings;
- all `22` raw unary parameter solutions;
- all `6` gauge-equivalence classes;
- exact global unary relations and projection covariance;
- depth-4 typed compositions;
- the nonzero upstream relative witness;
- every ablation listed above;
- `0` theorem/model mismatches.

## Final ablation conclusion

The least-carrier conclusion does not depend on the explicit primitive clause or on imposing a full upstream retract. It does depend on preserving the nonzero order-three upstream layer and on the no-extra-torsion preference. The exact six-class unary classification depends materially on the issued unary relations and old-projection covariance.
