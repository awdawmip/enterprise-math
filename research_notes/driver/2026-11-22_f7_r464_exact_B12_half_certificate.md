# CBRC F7 — Driver r464: exact finite-box minimax at B=12

Date: 2026-11-22 (Asia/Taipei). Original F7 scientific author: `EM-CBRCF7-83A1D4`; follow-on construction and scoped verification: `EM-DVR-DEBB5E`. Status: **exact finite computation with frozen standalone witness; Native review and Source/Activity linkage pending**.

## Fixed problem and theorem

Let `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`. On integer input `z=(a,b,c,d)`, put `k=a-2b-c+2d`, and

[
D_q(z)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
]

Keep the original exact scalar constraints: `q(0,0)=0`; `q(-x,y)=q(x,y)`; `q(s,0)=1` for nonzero `s`; `q(x,y)>=1/2` at nonzero off-axis points; and marks `q(2,1)=q(-1,-1)=1/2`. Let

[
E_B^*=inf_qmax_{zin([-B,B]capmathbb Z)^4}|D_q(z)|.
]

**Theorem (r464):** (oxed{E^*_{12}=1/2}), and hence `E*_B=1/2` for all integer `1<=B<=12`. This extends the previous r461 finite-box theorem (`B<=11`). The infinite-domain value `E_infinity` remains at its existing bound `[1/2,4/7]`.

### Lower bound

For `z=(1,-1,0,0)`, `k=3`, so

[
D_q(z)=q(4,2)+q(-3,-3)-q(1,-1)ge 1/2+1/2-1/2=1/2.
]

This applies to every admissible function `q`.

### Exact upper-bound witness

Take integer denominator `M=30000000000000`. Define `q(0,0)=0`, `q(s,0)=1` for `s!=0`, and enforce the two exact marks with reflection symmetry. All other `y!=0` points have

[
q(x,y)=	frac12+rac{n(|x|,y)}{M},
]

where `n` is zero outside an explicitly frozen lexicographically sorted table of 2,813 positive-integer triples `[abs(x),y,n]`. This defines a globally admissible function.

The *separate pure-Python integer checker* enumerates all `25^4=390625` ordered inputs in the full `B=12` box and computes exact `M D_q` without floating-point operations. Observed and asserted results:

- `max |M D_q| = 15000000000000=M/2`;
- `514` ordered inputs attain this maximum;
- the sorted JSON table has `62463` bytes and `SHA256=340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5`.

The theorem follows from the universal lower-bound input and this finite exhaustive upper-bound construction. The certificate scope is the precisely stated finite domain; it makes no infinite-domain or native X6 transfer assertion.

## How this construction was obtained (non-load-bearing discovery)

Start with the earlier r463 `B12` integer table at denominator `10^13`, whose maximum violation over the `1/2` target is one integer unit. Enumerating near-active constraints yields `6754` inequalities on `2867` correction coordinates. A bounded sparse LP with corrections in `[-2,2]` has a feasible solution with entries in integer thirds. Multiplying the table and corrections by 3 gives a denominator `3*10^13` exact witness. The LP's numerical status is **not** used for proof: all final table bytes and every inequality are checked by integers.

## Evidence and remaining Source step

- GitHub exact independent checker: `research_checks/CBRC_F7_R464_BOX12_EXACT_HALF_CERT_20261122.py`.
- Frozen table filename: `F7_R464_B12_Exact_Half_Witness_20261122.json`, SHA256 above. The table is preserved in the current run's portable certificate ZIP, which also includes the checker and standalone report.
- Previous r463: `research_notes/driver/2026-11-22_f7_r463_B12_fixed_integer_1e13_precision.md`, checker and regenerator remain unchanged.

**GitHub table publication still required:** at the time of this note, the 62,463-byte table has not been uploaded to the canonical Enterprise Math repository. Commit the frozen bytes under `research_artifacts/` and perform a SHA256/content readback. Do not describe the GitHub checker alone as a fully Source-published data certificate. The scoped mathematical statement has been exhaustively verified locally; formal Driver Review/Result acceptance and Source/Activity linkage are separate, under current own SID/DA permissions. Preserve the original author's prior contribution and any other live task owners.

No pre-existing request, CLAIM, prior frozen Result, or scheduling configuration was mutated to produce this work.
