# CBRC F7 Driver r470 — B15 frozen-B14 witness repair obstruction

Date: 2026-11-22 (Asia/Taipei). Original F7 scientific author: `EM-CBRCF7-83A1D4`; this supplementary finite-domain repair certificate: `EM-DVR-DEBB5E`. Scientific status: exact finite-instance construction/verification; native Driver Review, Result admission and Activity association not asserted.

## Exact inherited model

Keep the original F7 `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`, and
`k=a-2b-c+2d`, with
`D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.
The admissible `q: Z^2 -> R` is even in its first coordinate, `q(0,0)=0`, `q(s,0)=1` for `s != 0`, `q(x,y)>=1/2` for nonzero off-axis points, and `q(2,1)=q(-1,-1)=1/2`.

Let `q_*` be exactly the globally defined r469 quarter-valued B14 witness, not an arbitrarily chosen minimizer. Its [immutable 1,190-row table](https://github.com/awdawmip/enterprise-math/blob/ba281507cfcba49b9fb592c0e7f98b5a4ccd5621/research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json) has SHA256 `83bb9dabbace1a6ab4542538cc6a8b8c8fb06bb5ce055e7d9fddf842e01d5169`.

Define `K_14` as the set of 4,159 canonical coordinate keys `(|x|,y)` appearing in any of the four `q`-arguments of `D_q(z)` as `z` ranges over `[-14,14]^4 ∩ Z^4`. Fixed/immutable coordinates are the origin, the axis, and the two marked keys. All counts are over signed integer input tuples, not symmetry-class weights.

## Theorem r470 — a specific extension requires 78 old-key changes and L1 repair >= 39/2

For **every** admissible `q'` satisfying `|D_{q'}(z)|<=1/2` for every `z in [-15,15]^4 ∩ Z^4`, one has

```text
#{ k in K_14 : k is mutable and q'(k) != q_*(k) } >= 78

sum_{k in K_14, k mutable} |q'(k)-q_*(k)| >= 78/4 = 39/2.
```

In particular, extending only the 604 newly encountered B15 coordinate keys while freezing all B14 keys cannot make this specific `q_*` B15 half-feasible.

### Proof from 78 concrete disjoint witnesses

The separate [78-row static integer-input certificate](https://github.com/awdawmip/enterprise-math/blob/285b94fbe613c8cf9090db13002cb19f58f33685/research_artifacts/F7_R470_B15_Frozen_B14_Disjoint78_Witnesses_20261122.json) lists `z_j=(a,b,c,d)`, all in the B15 box. Exact evaluation at the r469 frozen `q_*` gives `|4D_{q_*}(z_j)|=3` for each `j`.

For each witness, collect its **mutable** canonical keys `S_j`, with signed linear coefficients after first-coordinate-even identification and cancellation. The fixed certificate verifies:

* `S_j` is nonempty, is entirely contained in `K_14`, and every remaining coefficient is `+1` or `-1`.
* The 78 sets `S_j` are pairwise disjoint.

For any half-feasible `q'` at `z_j`, the signed numerator changes by at least one integer unit in the scale `4D`, since `|4D_{q_*}(z_j)|=3` and `|4D_{q'}(z_j)|<=2`. Fixed keys have zero allowed change, so the triangle inequality and the unit coefficients yield
```text
sum_{k in S_j} |q'(k)-q_*(k)| >= 1/4.
```
Every `S_j` therefore contains a changed old mutable key. Summing across the disjoint sets proves both assertions. These are statements **relative to this specific frozen B14 witness**; the unrestricted B15 minimax value `E_15^*` remains open on this evidence.

## Complete B15 exact diagnostic for the frozen function

The original `q_*` was evaluated across every `31^4=923,521` input via integer `4D` arithmetic. The exact signed distribution is:

| `4D_{q_*}` | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 56 | 2,856 | 54,994 | 268,878 | 433,365 | 147,832 | 15,538 | 2 |

Exactly **2,914** B15 inputs violate the half-error threshold; all 2,914 involve only keys from `K_14`. The B15 argument domain touches 4,763 canonical keys, or 604 more than B14. This diagnostic and the disjoint witness verification were actually computed by an exact integer JavaScript enumeration in this run (no floating-point optimization or tolerance for feasibility); the [standalone standard-library Python checker](https://github.com/awdawmip/enterprise-math/blob/41f5788426ee055cc7caf10f329e2afc55d05cd5/research_checks/CBRC_F7_R470_B15_FROZEN_B14_78_DISJOINT_REPAIR_CERT_20261122.py) was published for source-tree reproduction. Its execution in a Python checkout has not yet been separately observed.

## Scientific and control frontier

Previously established `E_B^*=1/2` for `1<=B<=14` is preserved. The next useful B15 route is all-variable repair or an exact dual infeasibility certificate under the original F7 conditions; the present result quantifies the cost of reusing r469's old values, rather than ruling out B15 feasibility.

GitHub mathematical evidence, native Driver review and Source/Activity admission are separate. The last live control read in this turn reported `SOURCE_TREE_TRUNCATED` for the canonical Source adapter; the repair candidate PR #114 was open and draft. Historical native review rejection remains recorded without a replay. Neither status changes the finite arithmetic argument, the original F7 author, the live owner or the task schedule.
