# CBRC F7 r491 — exact B30 quarter-grid minimax certificate

Date: 2026-11-22 Asia/Taipei. Contributor: established RESEARCH_DRIVER logical lane EM-DVR-DEBB5E (original own SID MCP-9b4714dc46b948afa4875a86c89c713c). Preserve the distinct original CBRC F7 author EM-CBRCF7-83A1D4 and frozen RR-AA38973D56330E59D315, its source and incomplete formal review record.

## Exact original model and theorem

Let `q:Z²→R` obey `q(-x,y)=q(x,y)`, `q(0,0)=0`, `q(x,0)=1` for `x!=0`, `q(x,y)>=1/2` if `y!=0`, and `q(2,1)=q(-1,-1)=1/2`. For integer quadruple `(a,b,c,d)`, put `k=a-2b-c+2d` and `D_q=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`. Define `e_B = inf_q max_{(a,b,c,d)∈([-B,B]∩Z)^4}|D_q|`, with q globally constrained as above.

**Theorem r491:** `e_B=1/2` for every integer `1<=B<=30`.

The universal lower bound holds already at `(a,b,c,d)=(1,-1,0,0)` with `k=3`, as

```text
D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0) >=1/2.
```

## Fully specified global quarter-grid upper-bound construction

Put `Q=4q`, set `Q(0,0)=0`, `Q(x,0)=4` for `x≠0`, `Q(±2,1)=Q(±1,-1)=2`. The remaining off-axis values depend only on `K=(|x|,y)` with `y≠0`. Use this deterministic ordered index for `B=30`:

- `R={-60,...,60}`. For each `r∈R`, let `T_r=[2r-min(B,r+B), 2r-max(-B,r-B)]∩Z`.
- Loop `r` increasing; for each `r`, `u>r` increasing; loop `v` through `T_r` then `T_u` in increasing order; for each `v`, visit `rr=r` then `rr=u`. On first occurrence, append `(|2rr-v|,rr-v)` when second coordinate is nonzero and key is not either original fixed mark.
- Exactly **18,688** free keys are inserted. Assign their Q values in index order from the following immutable encoded raw-byte array; for any off-axis key not indexed and not fixed, set `Q=2`.

Immutable [B30 fixed certificate](https://github.com/awdawmip/enterprise-math/blob/004f12cbe85d0ac39a1ef92afac298bbda2b0611/research_artifacts/F7_R491_B30_Exact_Quarter_Witness_20261122.b85) is Base85(zlib(raw unsigned Q bytes)) with 18,688 bytes and raw SHA256

```text
7a49938391a054b9f022d29063d8a10344ef92ca1d3f9667d29aba3b33092e3f
```

The exact certificate Git blob SHA1 including trailing newline is `b990de3b189a3a0dd7896ec3cc205761d14ee7fb`; source GitHub readback matched. Q value frequencies: **Q2=11,844, Q3=5,519, Q4=1,325**. These values, with defaults and axis/marks, define a global admissible q on `Z²`.

The independent [full original-input verifier](https://github.com/awdawmip/enterprise-math/blob/46372bf6e4b609c0cdf5382a05de528a4e44392d/research_checks/CBRC_F7_R491_B30_EXACT_QUARTER_CERT_20261122.py) rebuilds the index, checks the static raw SHA256, and tests **every one of `61^4=13,845,841` original `(a,b,c,d)` integer inputs** by the original four-term shear expression using integer arithmetic. An independently run, pure Python standard-library original-input enumeration succeeded with the exact histogram:

| `4D_q` | Input count |
|---:|---:|
| -2 | 288,904 |
| -1 | 2,898,222 |
| 0 | 6,685,565 |
| +1 | 3,512,054 |
| +2 | 461,096 |

Their sum is 13,845,841 and the maximum `|4D_q|` is 2, hence `E_30(q)=1/2`. The matching universal lower bound makes the optimum exact. The **same global q** proves `e_B=1/2` for every smaller positive integer B.

## Search, repair and proof scope

The fixed candidate was obtained by extending the already-verified [r490 exact B29 witness](https://github.com/awdawmip/enterprise-math/blob/0d83466839888b89d03c24c55068153e674908f0/research_notes/driver/2026-11-22_f7_r490_B29_exact_quarter_minimax.md) with default Q2 on the newly indexed B30 keys. The initial B30 default extension had **11,214** violations (max `|4D|=4`) in all `61^4` inputs. A bounded sparse cutting-plane LP then produced an integer-quarter witness, verified separately using exact integer enumeration. The final construction changes **664** of r490's old B29 indexed keys (632 by +1 Q unit, 30 by -1, 2 by +2) and keeps all newly added **1,218** B30 keys at Q2. No minimum-repair claim is made.

The LP and candidate search are not components of the exact proof. Exact static bytes and an exhaustive integer check of the original formula certify this *finite* input box; the global unrestricted F7 minimax remains bounded by `1/2<=e_infinity<=4/7`.

**Status:** mathematical proof subunit r491 stored; the finite-box exact frontier is B30. The next open finite box is **B31**. The separate native frozen-Result integrity and first-review issue [#2874](https://github.com/awdawmip/enterprise-math/issues/2874), Source/Activity association and formal Result/Task/mother Objective states remain subject to actual current authoritative evidence. Original author, other owners, claims and automation schedule unchanged.
