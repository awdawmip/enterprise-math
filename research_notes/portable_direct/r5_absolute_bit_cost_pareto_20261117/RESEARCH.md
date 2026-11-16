# R5 — Sharp cost × raw count-bit Pareto frontier at the optimal absolute-noise margins (2026-11-17)

**Scope:** frozen 954-event indexed-center radius-two *derived integer-count observer*, 8 effective closure bits, integer budgets 214–314. Scientific input pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`. **Status:** `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. This is not native X6 dynamical admission and does not change P000.

## Question and theorem

Earlier R5 work at commit [`9a87e52e`](https://github.com/awdawmip/enterprise-math/commit/9a87e52ef88e51bec0c6b8934b055a72667e6b60) classified **all** fixed scalar schedules achieving their sharp worst-case absolute-error separation margins D3 and D4:

- Triple schedules `Q=(217,m,l)`, 224≤m≤290, 298≤l≤311 (938 schedules; margin D3).
- Quadruple schedules `Q=(217,e,m,l)`, e in {218,219}, same m,l (1,876 schedules; margin D4).

Here we solve a **new two-resource objective** on exactly these certified families. Define `C(Q)=Σ_{k in Q} k` (numerical budget sum); `w(k)=max_{b=0,...,255} bit_length(N_b(k))`, for the positive exact integer count readout `N_b(k)`; and `W(Q)=max_{k in Q} w(k)` (peak raw unsigned binary width of a single count). `bit_length(n)=floor(log2(n))+1` for `n≥1`. This is **not** an information-theoretic lower bound for arbitrary codes nor an estimate of wall time or compressed payloads.

**Theorem.** The complete Pareto-optimal fixed schedules in `(C,W)` for each sharp absolute-noise margin have exactly three points:

| Margin | Fixed budgets Q | C(Q) | W(Q), bits | Σ w(k), bits |
|---|---|---:|---:|---:|
| D3 | (217,224,298) | 739 | 133 | 352 |
| D3 | (217,289,298) | 804 | 128 | 347 |
| D3 | (217,290,298) | 805 | 116 | 335 |
| D4 | (217,218,224,298) | 957 | 133 | 460 |
| D4 | (217,218,289,298) | 1022 | 128 | 455 |
| D4 | (217,218,290,298) | 1023 | 116 | 443 |

In particular, the **minimum achievable peak raw-count width is 116 bits for either query-count class**. The minimum total raw-count widths, 335 and 443 bits respectively, occur at the final row for each class. The peak-width optimum increases numerical budget cost by 66 compared with each minimum-C schedule. No other margin-optimal fixed schedule improves on any of these two resources without worsening the other.

Equivalently, among D3 schedules, the minimum C subject to `W≤B` equals 805 for `116≤B<128`, 804 for `128≤B<133`, and 739 for `B≥133`; no such schedule exists if `B<116`. Among D4 schedules replace 805,804,739 with 1023,1022,957. B is an integer width cap.

## Proof, complete finite domain

For each k, reconstruct all 256 counts from the pinned nonnegative integer cohort coefficients by `N_b(k)=Σ_{T⊆b} A_T(k)`; compare all 25,856 reconstructed counts byte-independent as integers with the separately preserved complete table. Then compute `w(k)` by Python arbitrary-precision `int.bit_length()`, without floating-point logs. In the middle window k=224..290, relevant low-width candidates are `(224,133)`, `(289,128)`, `(290,116)`; all other middle k values have `w(k)≥133` except the two final candidates. The exact late window k=298..311 has `w(298)=111`; all later l are more expensive and **none has smaller w** than 298. Early values are `w(217)=w(218)=w(219)=108`. Therefore `l=298` dominates every larger late choice in both C and W. For quadruples, `e=218` similarly dominates `e=219`. Reducing to the middle window, the only nondominated (k,w(k)) alternatives are precisely the three listed above; adding the common terms yields the six rows. This finite exhaustion is sufficient because the preceding R5 schedule classification has already proved the family complete; it does not re-prove that older classification.

**Verification boundary:** 101×256 exact integer cohort-to-full-table comparisons, 938 triple and 1,876 quadruple schedule resource evaluations, exact pairwise Pareto comparisons; every asserted result is checked with the accompanying standalone Python verifier. The coefficients are from `compact_stdout.json` SHA256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`; complete independent saved count table SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Both are historical pinned research evidence, not new 954-event DP executions.

## Exact reproducibility

`python VERIFY_R5_BITS_PARETO.py compact_stdout.json EXACT_R5_ALL_101_BUDGETS.json > RESULTS_EXACT.json`

Expected `status=PASS_R5_SHARP_ABSOLUTE_MARGIN_BIT_COST_PARETO`, `full_count_checks=25856`, 3 Pareto rows in each family, minimum peak width 116 bits. The accompanying result JSON includes the full `w(k)` tables for the two relevant windows, which provide short independent audit witnesses.

## Limitations and next questions

The Pareto claim optimizes **only** the already-proved D3/D4-margin-optimal **fixed** nonadaptive scalar schedules. Adaptation may lower worst-case total budget, and richer encodings or differential readouts may reduce transmitted bits. Neither is addressed by this theorem. Next: construct an exact minimax game certificate for adaptive worst-case C at each absolute-error class, and inspect whether a provenance-bearing joint observer bypasses scalar noise saturation while preserving the chosen future-operation scope. Also preserve the separate original indexed-center `max-new/min-old` replacement-distance question.

**Control provenance:** prior R5 registered Researcher-ID `EM-DIRECT-C52C70`, Activity `RA-E56F584D739D86CC48916236` and SID `MCP-51b3895079074d4e9f863bd325121dfe`; this science remains a portable independent return. Registration does not grant a formal CLAIM or review. Do not overwrite a live owner or claim a protected Activity checkpoint without actual authorized source-CAS linkage.
