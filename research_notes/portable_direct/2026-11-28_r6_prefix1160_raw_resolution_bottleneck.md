# PREFIX-1160: raw-resolution bottleneck and scale-tail separation

Date: 2026-11-28. EM-DIRECT-780BBE / TASK_RESEARCH, own managed session metadata verified, no formal claim. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / AFFINE_OUTER_MODEL_WITNESSES / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.

## Inputs and authority

Continue PREFIX-1159 at e309c6d77591bf9d2b015a106f1b75a869cd5edb:research_notes/portable_direct/2026-11-28_r6_prefix1159_grid_scale_clearance.md. Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d with its joint-observer, Heartbeat and residual-fidelity companions. Current global rule snapshot cddb04ede09d2865a524ee1062517c61ec3e0a24 and control source cb546532976a7a1c94559a2586c2fb81d66ea324. Original own registration r6-20261123-2358-session-start-own-v1 recovered with no closed/revoked flag; recovery grants no execution. Owner inventory r6-20261128-2255-owner-read SUCCEEDED, fixed INV-5b7a6cb12c95ce3d0a3be9bdc6a6e91c as of 2026-11-28T14:55:58.564498Z, total 547, LEASED filtered list empty, source/event issue unchanged at completion 14:57:15Z. No new claim or shared task-state mutation. This is auxiliary parameter arithmetic, not a native Heartbeat computation. Original Stage46 asymptotic, anchor, affine transfer and primitive-relation reduction assumptions remain load-bearing.

## 1. Scale-adaptive search with the old certified section

Reuse the PREFIX-1159 16-vertex section P (coordinates relative to the affine reference r,u). At scale L the necessary ratio domain is P+[-K/L^2,0]x[0,H/L]; it contains all larger-scale domains. Rebase at each L via the maximum-area observation triangle and exact rational LLL. Verify V W=I with integer V,W. Since each transformed coordinate is q times an affine function of (p/q,h/q), its extrema on q0<=q<=Q and the ratio polygon occur among the two denominator endpoints and polygon vertices. Use outward integer bounds for a complete box, then exact interval elimination in the last coordinate, cross-checked by full box enumeration with original-coordinate inequalities. Test gcd(q,p)=1 as inherited. All eight runs were independently enumerated by both methods:

| L | Q | box | feasible | primitive | minimum q (approximate) |
|---|---|---:|---:|---:|---:|
| 3e134 | 1e89 | 0 | 0 | 0 | >1e89 |
| 3e134 | 3e89 | 672 | 110 | 90 | 1.2278681328e89 |
| 1e135 | 3e89 | 168 | 41 | 28 | 1.2278681328e89 |
| 1e136 | 1e90 | 1045 | 146 | 87 | 2.5869832318e89 |
| 1e137 | 3e90 | 3105 | 416 | 257 | 3.7780802541e89 |
| 1e138 | 1e91 | 13680 | 2306 | 1404 | 8.5792394540e89 |
| 1e140 | 1e91 | 5418 | 863 | 524 | 1.4531087887e90 |
| 1e152 | 1e91 | 5418 | 849 | 517 | 1.4531087887e90 |

The last minimum is q_old=1453108788683279458746971083142301765111381877116130690887157247121933310897371353649740211. The old zero-scale full affine fiber has an exact witness with slack >0.0639.

## 2. Actual final-grid refinement without new raw moments

Keep Hraw=10^150, J=10^155, anchor order 9600, 15 observation rows and 12 shared columns. Reconstruct all 13 moment rows at final G=10^155 (previous G0=10^150); rescale the two point rows exactly. For each row retain the original rational center M, columns B_j and analytic budget delta=tail+1/(2Hraw)+10^-180+1205/J. With m=floor(G*M), C_j=floor(G*B_j), e=ceil(G*delta)+13, the sum of the center and twelve column rounding errors is <=13 grid units for shared coefficients in [-1,1]. This proves the new outer model, without narrowing any inherited raw or analytic error. The old grid is reconstructed exactly before each refinement. For each of rows 10--14, the normalized radius is reduced by 27.3336066694 times (exact ratio between 27.33 and 27.34). The new radius budget is 97.6200% raw quantization and 2.3526% internal arithmetic, with the remaining fraction principally final rounding; row 9 improves by 1.00847 and lower rows are essentially unchanged. The old raw input is now the limiting budget in these five rows, not a claim of optimality of all observations. Holding the inherited raw uncertainty fixed leaves the floor 1/(2Hraw) even as final G tends to infinity. No new raw moment, point or anchor run was done.

Let U=[C,diag(e)] and v=A(p/q-r)+B(h/q-u)-m. The old q_old is now excluded at L>=1e140 by the oriented support test

n.v > sum_j |n.U_j| + max(0,-n.A) K/L^2 + max(0,n.B) H/L.

The compact verifier gives ratio 13.98936705145638 at L=1e140 and monotonicity extends it to larger L. Separately the centered full-scale test gives ratio 17.9675358076 and zero-scale test gives 26.3411234102. Those ratios have different centers; the first failed compact assertion incorrectly used the centered threshold for the oriented ratio and is retained in the ZIP. The corrected exact inequality passes.

## 3. New outer section and complete search

Intersect the old section with the valid support strips for 15 inverse-pivot normals and eight sparse cofactor normals from seven-element subsets of {0,1,9,10,11,12,13,14}. All 27 shared and independent generators are paid in every strip. Iterative clipping and all boundary-pair intersections give the same 16 vertices. Width rho=2.0136858216845926e-133, c=9.657774759492286e-133, improvements about 1.12779 and 1.12780 respectively. These are outer-section widths, not full exact projection widths.

| L | Q | box | feasible | primitive | minimum q (approximate) |
|---|---|---:|---:|---:|---:|
| 1e138 | 1e91 | 9408 | 1323 | 815 | 8.5792394540e89 |
| 1e140 | 1e91 | 144 | 48 | 28 | 1.6113599338e90 |
| 1e142 | 3e91 | 3312 | 797 | 477 | 1.8097548815e90 |
| 1e144 | 3e91 | 3312 | 795 | 476 | 1.8097548815e90 |
| 1e152 | 3e91 | 3312 | 795 | 476 | 1.8097548815e90 |

Every box was independently exhausted in addition to interval elimination. The last two compact verifier searches independently reconstruct the old and new polygons, use original-coordinate support inequalities and verify exact minima. The new exact minimum is

qstar=1809754881531112186904694767481139172491414761359983491189786084567209150450511632496318670.

Under the inherited hypotheses, for all L>=10^142, b-a>=q>=qstar. This is about 18.09755 times the earlier strict threshold 10^89 (which applies already at L>=3e134). The old scale baseline L>=1e134 remains valid. By nestedness of signed scale outer domains the new statement holds for all larger L, not just the sampled scales. The first 28 full-scale fibers at L=1e140 and first 20 at L=1e142 all have exact 29-variable witnesses, minimum slacks >0.0078. In particular qstar has zero-scale slack >0.556, with a compact exact rational witness verified without floating LP. Therefore no added linear support direction for the unchanged affine model can exclude qstar even at zero scale. That is a model obstruction, not evidence of an actual anomalous integer pair.

## 4. Stitched anomaly windows

Use inherited triple necessary q^2<4E L/dlo, E=400000, and near-pair condition gap<=sqrt(L). The PREFIX-1159 certified dyadic coverage extends beyond 10^142. Stitch at that scale; first not excluded dyadic starts (L=10^8*2^j) are

triple 23587265155134633451509716131176680568230757627602752677351289376535151014950930325538292032360367297134177343942274030623566153937029953953508964071454350272808720793600000000
near pair 6183260036827613351512563025491179750878283727530295997851576402322430627663296679257910026531076124739941785650403483483784125857668780249188653877547329197915169303717478400000000

These extend the previous boundaries by 256 and 512 respectively, not demonstrated actual anomaly windows. Continuous integer endpoint remains 4.72478e43. Unconditional unbounded separation, B_fix,odd(32), inherited anchor exit confirmation and independent review remain open.

## 5. Reproduction and next action

Frozen PREFIX-1159-execution-evidence.zip SHA256 b1785c7ef00b42daf6280d062c8b6d9abedc7a085db722cbf1bdda3b2f679998; its 406 manifest entries verified. In the extracted directory run compact1160.py (remote source at 28b42ca30bae99b80d4d9b461d7fe5726ae71ac6:research_notes/portable_direct/2026-11-28_r6_prefix1160_compact_verify.py, SHA256 23e5fe5c96b4687771b3b1c47cdde5d3f24a2c393d6efbad890414ccfb5edba3, Git blob 4e8f03d242944b73ebbdeec36797ffaa4117afe5, exact remote match). It imports the existing compact1159.py and independently checks the key new section, integer minima, exclusion, qstar witness and stitched windows. Executed log SHA256 9405fc4fb3c2d353a8d2e5581f4ce87f3f4c650b2a4ca7d653ef65354fa2bf99. Full discovery scripts scale1160.py, refine1160.py, fibers1160.py and exact JSON records are in the new execution evidence. Inherited anchor/Stage46 analytic certificates are not regenerated. Next: target the raw moment quantization at the five highest-order rows, using finer raw Hraw together with larger internal J (which already contributes 2.35% of their radius). First diagnose the qstar fiber under a changed raw error budget, then actually recompute the selected raw moments and retain their certified quantization; do not merely relabel a hypothetical error reduction. Keep all shared directions and point rows.
