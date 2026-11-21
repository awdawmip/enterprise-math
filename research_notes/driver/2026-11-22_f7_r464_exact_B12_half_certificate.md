# CBRC F7 — Driver r464: exact B=12 finite-box minimax value

Date: 2026-11-22 (Asia/Taipei). Original F7 author: `EM-CBRCF7-83A1D4`. Follow-on constructor and scoped checker: `EM-DVR-DEBB5E`.
Research type: exact finite exhaustive certificate. Native Driver Review, Result acceptance and Source/Activity linking remain separately pending.

## Precise unchanged mathematical statement

Set `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)` and `A=I+u v^T`. For integer `z=(a,b,c,d)`, write `k=a-2b-c+2d` and

`D_q(z) = q(a+k,b+k) + q(c-k,d-k) - q(a,b) - q(c,d)`.

The admissible q is a function on Z^2 with `q(0,0)=0`, `q(-x,y)=q(x,y)`, `q(s,0)=1` for nonzero s, `q(x,y)>=1/2` on all nonzero off-axis points, and exact marks `q(2,1)=q(-1,-1)=1/2`. Define

`E_B^* = inf_q max_{(a,b,c,d) in [-B,B]^4 intersect Z^4} |D_q(a,b,c,d)|`.

**r464 theorem: E_12^* = 1/2.** Hence `E_B^*=1/2` for every integer `1<=B<=12`, extending the previous r461 statement for `B<=11`. The original infinite-domain question retains the prior bracket `1/2<=E_infinity<=4/7`.

## Lower bound for all admissible functions

Take `z=(1,-1,0,0)`. Then `k=3` and

`D_q(z) = q(4,2) + q(-3,-3) - q(1,-1) >= 1/2 + 1/2 - 1/2 = 1/2`.

The last term is one of the exact marks, using evenness in the first coordinate. This proves `E_12^*>=1/2`.

## Fixed global upper-bound witness

Use integer denominator `M=30000000000000`. Put `q(0,0)=0`; `q(s,0)=1` for nonzero s; and both marks with evenness. All other off-axis points are given by

`q(x,y) = 1/2 + n(abs(x),y)/M`,

where n is zero unless the coordinate appears in a **frozen, sorted table of 2813 triples** `[abs(x),y,positive_integer_n]`. Thus q is globally defined, even in x, and has the required nonnegativity and marks.

The independent Python standard-library checker enumerates all `(2*12+1)^4=390625` ordered integer inputs and evaluates integer numerator `M*D_q` exactly. Verified outcome:

- Maximum `|M*D_q| = 15000000000000 = M/2`.
- Exactly `514` inputs attain this maximum.
- Table file: `F7_R464_B12_Exact_Half_Witness_20261122.json`, `62463` bytes, SHA256 `340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5`.
- Checker source: `research_checks/CBRC_F7_R464_BOX12_EXACT_HALF_CERT_20261122.py`.

The lower-bound input and exhaustive integer-checked witness establish the theorem on the finite box.

## Discovery route and provenance

From r463's denominator-10^13 near-optimal fixed table, retain all inequalities with distance at most 100 numerator units from the half-bound. These become 6754 sparse linear inequalities involving 2867 correction coordinates. A bounded LP with each correction in `[-2,2]` returned a feasible vector with components in integer thirds. Rescaling by 3 produced the frozen denominator-3*10^13 table; final truth is checked by exact integer exhaustion, not by floating-point LP status.

r463's predecessor artifact: `research_notes/driver/2026-11-22_f7_r463_B12_fixed_integer_1e13_precision.md`, predecessor table SHA256 `5026e4e8d9ccecd26806d95a096af4f41ff3c4507ea5ec7a43552e1a1edf68b6`.

## Durable storage and control boundary

The frozen 62463-byte table and checker are retained together in the current run's portable certificate ZIP. This GitHub note and the checker code have canonical-main publication and readback; **the static table is not yet published to GitHub** and needs exact-byte upload to `research_artifacts/` followed by digest readback. Keep this explicit until it is done. Formal Review, Result acceptance and Activity linkage require separate current authenticated Driver authority. Preserve the original author, other active owner scopes and already final requests.

Proof scope: the specified two-coordinate F7 finite scalar model. No automatic result for infinite boxes or a native-X6 information-preserving lift is asserted.