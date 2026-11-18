# EC49FTJ — Exact native BRC16943 seven-phase lower-z fan (two-parameter)

Date: 2026-11-19. Scientific status: **AUTHOR_PROVED / EXACT_PRIMARY_16 / INDEPENDENT_RAW94_2 / NOT_REVIEWED**.

## Provenance and exact target

Predecessor: [EC49FTI PR #2770](https://github.com/awdawmip/enterprise-math/pull/2770). Frozen scientific input: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, retaining **310 original configurations, 141 individually named joint-response profiles, and all 228 physical query indices**. P000 and the ACTIVE worldview are unchanged. This is an exact finite native BRC identification decision problem, not an assertion of an unproved X6 physical transfer.

Let a,b,z be the discounts on q32,q34,q140. For an original-index complete identifying tree of total path usage vector (U,N32,N34,N140), its direct normalized cost is U−aN32−bN34−zN140; under the q32/q34 discount swap it is U−bN32−aN34−zN140. D,S denote global minima over **all** legal original-index trees, not just the displayed witnesses.

## Continuous exact theorem

For **every real** b,z satisfying

- a = 3/4;
- 7/16 ≤ b ≤ 57/128;
- 1/4 ≤ z ≤ 3/8,

the **unrestricted all-228 native Bellman optima** are

```text
D(b,z) = min(
    307-141a-41b-10z,  # D10
    309-141a-41b-16z,  # D16
    311-141a-47b-14z,  # D14 [new distinct full-area phase]
    313-141a-47b-20z   # D20
)
S(b,z) = min(
    305-32b-141a-29z,  # S29 [new full-area wedge]
    304-28b-141a-32z,  # S32
    309-28b-141a-46z   # S46
)
```

All seven witnesses are complete original-index trees, with each one replayed against all 141 **separately named** original profile paths; no observer alias or profile quotient is used.

**Direct price: four phases.** Define z_c(b)=1−3b/2. For b<4/9, increasing z gives D10 → D16 at z=1/3 → D20 at z=z_c(b). For b>4/9, it gives D10 → D14 at z=z_c(b) → D20 at z=1/3. At **(b,z)=(4/9,1/3)** all four displayed direct-price trees are optimal simultaneously (no uniqueness claim). The newly discovered D14 witness has native usage vector **(311,141,47,14)**; at (57/128,213/640) it improves the preexisting D10/D16/D20 menu by **1/320**, an exact counterexample to extending that three-tree menu over the entire rectangle.

**Swapped price: three phases.** Define z_s(b)=(4b−1)/3. The optimum is S29 for 1/4 ≤ z ≤ z_s(b), S32 for z_s(b) ≤ z ≤ 5/14, and S46 for 5/14 ≤ z ≤ 3/8. The S29 wedge collapses at b=7/16 and reaches z_s=25/96 at b=57/128.

**Sharp swap-gap bounds** on the full rectangle:

```text
351/128 <= D(b,z) - S(b,z) <= 87/16.
```

The lower value is attained at (b,z)=(57/128,1/4), the upper at (7/16,3/8). For fixed b, the gap is strictly increasing in z: swapped optimal trees use q140 on 29,32 or 46 named paths, while direct optimal trees use it on 10,14,16 or 20, so its local slope is always at least 9.

## Original-source exact Bellman vertex certificate

The candidate-minimum cells are convex polygons whose vertices are computed by **exact rational half-plane clipping**. For the D orientation they have 9 distinct vertices; for S they have 7. Every vertex was checked independently by a complete integer-scaled **all 228-observation** Bellman solver. Actual original-index unrestricted values:

| orientation | b | z | unrestricted Bellman |
|---|---:|---:|---:|
| D | 7/16 | 1/4 | 2893/16 |
| D | 7/16 | 1/3 | 8639/48 |
| D | 7/16 | 11/32 | 2877/16 |
| D | 7/16 | 3/8 | 2867/16 |
| D | 4/9 | 1/3 | 6469/36 |
| D | 57/128 | 1/4 | 23103/128 |
| D | 57/128 | 85/256 | 11499/64 |
| D | 57/128 | 1/3 | 68987/384 |
| D | 57/128 | 3/8 | 22889/128 |
| S | 7/16 | 1/4 | 178 |
| S | 7/16 | 5/14 | 1222/7 |
| S | 7/16 | 3/8 | 695/4 |
| S | 57/128 | 1/4 | 711/4 |
| S | 57/128 | 25/96 | 17035/96 |
| S | 57/128 | 5/14 | 39055/224 |
| S | 57/128 | 3/8 | 5553/32 |

These 16 entries were recomputed through the standalone checker in two completed batches, 0:8 and 8:16. **Partial independent raw94 decoder checks:** D(4/9,1/3)=6469/36 and S(57/128,25/96)=17035/96.

## Proof covering all real parameters

Each of the seven displayed **feasible** original-index trees defines an affine upper bound on its orientation's unrestricted optimal cost. The unrestricted Bellman value B is the infimum of the affine costs of all feasible complete finite decision trees, and therefore is jointly **concave** in (b,z). On a closed convex candidate-minimal polygon P with witness cost L, exact unrestricted Bellman equality B(v)=L(v) holds at **every** vertex v by the finite certificate. Every point p in P is a convex combination p=Σ λᵢvᵢ. Thus concavity yields B(p)≥Σ λᵢB(vᵢ)=L(p), while feasibility gives B(p)≤L(p). Equality holds throughout each polygon, including irrational points and phase boundaries. The polygons cover the whole rectangle. Simple affine comparisons give the stated switch sheets, the fourfold tie and the S29 wedge. Continuity and the strictly positive q140-use slope gap give the attained sharp bounds via its two z edges.

## Source, independent audit and deliverable

Frozen input SHA256: `frozen_original_master.txt` = `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv` = `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Complete local self-contained evidence archive: `EC49FTJ_NATIVE_BRC_SEVEN_PHASE_TWO_PRICE_FULL_EVIDENCE_20261119.tar.xz`, SHA256 `86955db4176dab0acfcda27a328f544ad3a76189aa70aa49e8d22878f31fd56f`. It contains the frozen raw source, independent raw94 reconstruction, exact all-228 solver, seven full JSON trees, proof, machine certificate, executable `EC49FTJ_VERIFY.py`, full validation logs and per-file hash manifest. Run `python EC49FTJ_VERIFY.py --independent`, then `--full --start 0 --stop 8` and `--full --start 8 --stop 16`; all three commands were executed successfully. Formal theorem-admission review and proof assistant checking were not performed.

## Research control and next question

This is **portable independent scientific evidence**, separate from formal Task CLAIM, Result and Review. Source task `RS-EC49AS` previously lacked a canonical publication directory; the present owner-read `r4-ec49ftj-20261119-0523-owner-read-01` was queued, while subsequent receipt access returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`. No active owner claim or Activity checkpoint is inferred from those responses.

**Next science:** extend the exact rectangle below z=1/4 to find the next native query-use families, or lift a away from 3/4 to obtain a certified three-parameter region. Use all 228 original-index observations and preserve named profile identity.