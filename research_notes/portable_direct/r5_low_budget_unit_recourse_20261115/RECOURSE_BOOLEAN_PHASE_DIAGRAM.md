# R5 — exact Boolean phase diagram for full-background offline recourse

Date: 2026-11-15. Scientific input freeze `435e77af0d180eac32bd1f9c4c464bc4010b7551`. State: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Object: derived 954-event integer, radius-two, indexed-center observer, retaining its event labels and 28 gap-closure bits.

## Definition and new theorem

For cut i and center budget K, define the **background-resolved** distance
\[
r_i(K,B)=\max_{S\in\operatorname{Opt}_{B\cup\{i\}}(K)}
          \min_{T\in\operatorname{Opt}_{B}(K)}|S\setminus T|,
\qquad i\notin B.
\]
This is more informative than its global maximum \(R_i(K)=\max_B r_i(K,B)\).

Let \(a=\mathbf 1_{8\in B}\), \(b=\mathbf 1_{9\in B}\), and \(c=\mathbf 1_{10\in B}\). Then the complete 27-bit background dependence, for every integer \(214\le K\le221\), is exactly:

| Budget | r_8(K,B) | r_9(K,B) |
|---|---|---|
| 214 | \(7-4b(1-c)\) | \(7-2a\) |
| 215 | \(6-3b(1-c)\) | \(6-a\) |
| 216 | \(6-3b-c+3bc\) | \(5+(1-a)(1-c)\) |
| 217–220 | \(5-2b(1-c)\) | \(5\) |
| 221 | \(5-2b\) | \(5\) |

All formulas are integer-valued on \(a,b,c\in\{0,1\}\).

**Minimal sufficient background supports**, treating each K and each changed cut separately:

| K | For changed cut 8 | For changed cut 9 |
|---|---|---|
| 214–215 | \(\{9,10\}\) | \(\{8\}\) |
| 216 | \(\{9,10\}\) | \(\{8,10\}\) |
| 217–220 | \(\{9,10\}\) | \(\varnothing\) |
| 221 | \(\{9\}\) | \(\varnothing\) |

Consequently the original closure variables 3 and 27 influence the optimizer families in this budget band but are **exactly inert for these two background-resolved recourse observers**. For K=217..221, cut 9's recourse is the universal constant five across all \(2^{27}\) backgrounds; at K=221 cut 8's recourse depends on one bit only.

## Proof and validation

The preceding theorem `OFFLINE_MAXMIN_EXACT_RECOURSE_THEOREM.md` establishes the exact minimax value for each of the 256 transitions (8 budgets × 2 changed cuts × 16 effective backgrounds). The independently verified optimizer-family support theorem reduces all other original closure variables to the five effective bits \(\{3,8,9,10,27\}\) while preserving complete indexed-center optimum sets and the max-new/min-old quantifier order.

For each fixed (K,i), substituting the 16 exact integer values into the displayed multilinear Boolean expressions gives equality on the entire four-bit background cube. A Boolean function is uniquely specified by its values on its full Boolean cube. Hence the polynomial readout formulas hold for every original background. A bit is essential exactly when its finite difference \(f(B\cup\{j\})-f(B)\) is nonzero at some background; the 16-case calculations establish every listed support as minimal and all omitted supports as absent.

The committed standard-library Python `VERIFY_R5_RECOURSE_BOOLEAN_PHASE.py` consumes `EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json` and recomputes all 256 formula matches, plus minimal support by comparing every flip at each available mask. Actual run returned `PASS_EXACT_R5_RECOURSE_BOOLEAN_PHASE`. This is an exhaustive finite result for the stated frozen observer and all original 27-bit backgrounds via the proven optimizer-family factorization.

## Structural interpretation and next unit

Different observers induce distinct exact quotients: the full K214..221 optimizer family depends on five cut variables, while the per-cut recourse observer above needs at most two of the other cut variables and sometimes none. This is an observer-specific exact fiber-constancy certificate, not a license to erase the source cut identities from future objectives, native X6 or other observables.

Next analyze the maximum Pareto-frontier antichain size and algorithmic complexity for wider K/n families; independently review the common-anchor factorization and full offline minimax dynamic program before any project promotion. The proof and exact checks are author-side scientific evidence on Draft PR #2427, not a formal CLAIM, Result or independent Review.
