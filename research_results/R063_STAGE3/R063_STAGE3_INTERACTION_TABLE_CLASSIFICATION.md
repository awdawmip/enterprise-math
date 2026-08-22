# R063 Stage 3 — Interaction Table Classification

Status: `PROVED / FROZEN_STAGE2_SCOPE`
Researcher-ID: `EM-R063S3-F1CF9D`
Task-ID: `RS-R063-STAGE3-PAIRWISE-INTERACTION-SIGNED-CANCELLATION-MULTIPLICATIVE-PROCESS-LIFT`
Taskbook source: `f1cf9d88428c14ae56e228ed97eba9b657b1fb90`
Frozen Stage 2: `96fbcd431f4cbb8263347bffb5c8bf33b7639e98`; Driver acceptance `b31419774f6d7190a4ed51332a9f69f4c7359b31`.

## Theorem

Let `e_i=(1,0)` and `e_j=(0,1)`. The frozen Stage 2 raw oriented component law is

`F((a,b),(c,d))=(ac-bd,ad+bc)`.

If a pair-interaction law is bilinear in component counts and its aggregate equals `F`, then its four basis interactions are uniquely forced:

| left | right | output |
|---|---|---|
| `X_i` | `X_i` | `+X_i` |
| `X_i` | `X_j` | `+X_j` |
| `X_j` | `X_i` | `+X_j` |
| `X_j` | `X_j` | `-X_i` |

Proof: bilinearity makes a map on arbitrary counts equal to the sum of its values on the four basis pairs. Substitution of `(1,0)` and `(0,1)` into `F` fixes those four values exactly. Conversely these four values extend bilinearly to `(ac-bd,ad+bc)`. Factor-order symmetry fixes the two mixed entries equal, and `X_i` is the multiplicative identity basis state. There is therefore no remaining table choice and no target-path selector.

## Minimal signed alphabet

For one binary product of positive `{X_i,X_j}` paths, three output symbols `+X_i,+X_j,-X_i` suffice. They do **not** close under repeated multiplication or unit transport. Closure requires the fourth symbol `-X_j` because, for example, `(-X_i) tensor X_j -> -X_j`.

Thus the closed finite label carrier is the cyclic four-state set

`C4={0,1,2,3} = {+X_i,+X_j,-X_i,-X_j}`,

with pair interaction given by addition modulo four.

## Semantic status

The table is **derived** from the frozen Stage 2 bilinear law. It is not introduced as a new N0 primitive. The closed interaction process built from it is classified `N1_DERIVED_OPERATIONAL` until a separate native-promotion certificate exists.

`PAIRWISE_INTERACTION_TABLE_DERIVED_UNIQUELY = true`.
