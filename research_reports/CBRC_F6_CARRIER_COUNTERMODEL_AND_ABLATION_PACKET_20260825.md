# CBRC F6 — Carrier Countermodel and Ablation Packet

Researcher-ID: `EM-CBRCF6-D694C8`

Task-ID: `RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`

Status: `CHECKPOINT_A_DRAFT`

Mathematical source used before raw freeze: only `research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21`.

## Purpose

This packet records the smallest structural witnesses needed to distinguish hypotheses from conveniences. It deliberately does not introduce multiplication, rings, norms, inner products, square laws, two-slot mixing, external quantum structures, or a named rank-two number system.

## Carrier witnesses

### M0 — least carrier

`C_min = Z e ⊕ Z f ⊕ <tau | 3 tau=0>`

with `pi(e)=e`, `pi(f)=pi(tau)=0`.

This proves that no torsion beyond the inherited `tau` is forced.

### M1 — extra cyclic torsion, full retract fails

`C_9 = Z e ⊕ Z f ⊕ <g | 9g=0>`, with `tau=3g`.

Then `tau` has exact order `3`, so the upstream additive layer embeds, and the old projection exists. But every `phi:Z/9->Z/3` kills `3g`, hence no `r:C_9->C1` can satisfy `r(tau)=tau`. This separates old-signed-retraction from full-upstream-retract conservativity.

### M2 — extra noncyclic torsion

`C_33 = Z e ⊕ Z f ⊕ <tau | 3tau=0> ⊕ <u | 3u=0>`.

It satisfies all additive carrier requirements but is strictly worse than `C_min` in the F6 torsion-minimality order.

### M3 — arbitrary extra finite torsion

For any finite abelian group `A`,

`C_A = C_min ⊕ A`

with `pi(A)=0` remains an allowed additive carrier. Thus uniqueness requires the explicit no-extra-torsion preference; rank two alone never eliminates arbitrary finite spectators.

## Mandatory ablation ledger — additive/conservativity frontier

### A1 — primitive old generator

Result: `REDUNDANT_GIVEN_OLD_RETRACTION`.

If `pi:C->Z e` is a retraction with `pi(e)=e`, then `e` is primitive in the free quotient. Removing the explicit primitive clause while retaining `pi` does not enlarge the model class.

### A2 — preservation of order-three `tau`

Result: `ESSENTIAL_FOR_UPSTREAM_RELATIVE_LAYER`.

If the marked order-three element is collapsed to zero, the additive rank-two torsion-free quotient `Z e ⊕ Z f` is smaller, but the frozen witness collapses:

`e + J R e = -tau = 0`.

Thus preserving nonzero order-three `tau` is essential, not a presentation choice.

### A3 — old retraction `pi`

Result: `STRUCTURALLY_RELEVANT_TO_TYPED_UNARY_CLASSIFICATION`.

At the additive level, primitive `e` still permits some retraction. But if no particular old projection is typed, later unary maps can carry integral `e`-shears on the new free direction that are invisible to the upstream embedding. A concrete exact unary witness will be frozen after Q3; this is why the F6 classification must distinguish embedding-only from projection-covariant structure.

### A4 — full upstream retract

Result: `NOT_USED_AS_A_MINIMALITY_HYPOTHESIS`.

The least carrier `C_min` automatically admits a projection-compatible full retract, but F6 does not require one to derive the least carrier. Extra carrier `C_9` shows the stronger notion is genuinely stronger away from the minimum. Imposing or removing existence of a full retract therefore does not alter the least carrier, while typing a particular retract would add unnecessary data.

### A5–A8 — unary relations/covariance

`R^3=id`, `JR=RJ`, `SRS^-1=R^-1`, and old-projection covariance are deferred to the unary-lift checkpoint. Each will receive an explicit exact countermodel showing the class enlargement when the condition is removed.

### A9 — no-extra-torsion minimality preference

Result: `ESSENTIAL_FOR_UNIQUENESS`.

Without the torsion preference, the family `C_min ⊕ A` over arbitrary finite abelian `A` yields infinitely many pairwise nonisomorphic rank-two carriers preserving the upstream layer. Hence the rank bound plus conservativity alone does not select a unique carrier.

## Checkpoint A status

The additive countermodel picture is stable:

- extra torsion is possible but never forced;
- the least pointed torsion is exactly `<tau>≅Z/3`;
- full retraction is stronger away from the minimum but not needed to reach the minimum;
- explicit primitivity is implied by the old retraction;
- removing the no-extra-torsion preference destroys uniqueness.

Unary ablations remain open until the exact lift equations are frozen.
