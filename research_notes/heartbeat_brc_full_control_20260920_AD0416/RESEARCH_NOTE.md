# Heartbeat World BRC: full typed control-state ladder

Status: `RESEARCH_CONSTRUCTION / EXECUTED_FINITE_CERTIFICATE / NOT_FOUNDATION`
Date: `2026-09-20`

This unit combines the three repair coordinates already isolated in Heartbeat World research:

1. spatial residue `r mod 4`;
2. six-channel local environment mask `m in {0,1}^6`;
3. local phase offset `delta in Z/6Z` relative to the shared Heartbeat World clock.

The raw finite diagnostic control population has `4*64*6 = 1536` states. The initial observer keeps only the two-class macro residue sign and the 13-class D6 shape of the globally aligned environment, giving 26 classes.

## Exact effect-valued ladder

Use the existing T0 `ControlPacket` refinement and exact EffectHistogram rows. The declared packet families are:

- `SAFE, ROT, REF`: symmetry-safe macro behavior; the spatial effect depends only on macro residue class and an environment orbit invariant.
- `MICRO`: within-cycle residue operation whose spatial displacement distinguishes raw residue members.
- `ABS`: globally framed phase-addressed environment operation. It distinguishes the globally aligned 64-mask orientation but not the local phase offset.
- `LOCAL`: local-frame operation whose spatial axis is selected by the local phase offset.

Exact refinement gives:

| declared future family | retained classes |
|---|---:|
| SAFE + ROT + REF | 26 = 2 × 13 |
| + MICRO | 52 = 4 × 13 |
| + ABS | 128 = 2 × 64 |
| + MICRO + ABS | 256 = 4 × 64 |
| + LOCAL | 768 = 2 × 64 × 6 |
| + MICRO + LOCAL | 1536 = 4 × 64 × 6 |

Thus a globally shared time phase does not mechanically multiply every BRC state by six. When the globally aligned environment is sufficient for all future effects, local phase offset is a gauge residual and is omitted. When a local-frame effect can use the offset, the factor of six becomes necessary.

A second exact certificate starts directly from the 128-class state `(macro residue class, globally aligned mask)`. A globally framed translation is safe on that quotient. Adding a local-axis translation indexed by `delta` rejects the quotient and refines to 768 classes.

## Interpretation

The result supports a typed state rule:

`external shared clock != local phase residual != spatial residue != environment state`.

They should not be flattened into seven or more spatial coordinates. The BRC state should carry only the repair coordinates that the declared future language can actually use, and should restore a finer product state when a new future operation invalidates an earlier quotient.

The counts above are not universal Heartbeat World complexity. They are exact for this finite diagnostic product model. Full twelve-direction occupancy, asynchronous time dynamics, changing local oscillator offsets, semantic memory operations and Nollm production behavior remain outside the claim.

## Validation

The earlier 18 tests, three shared-clock/local-phase tests, and two full typed-control tests all pass when run in their validated groups. The final two 1536-state tests pass standalone in about 26 seconds. A combined all-file pytest invocation hit the current 90-second tool timeout after completing the earlier 21 tests, so no single-run 23-test timing claim is made. No full repository suite, independent referee, Lean proof or production deployment is claimed.
