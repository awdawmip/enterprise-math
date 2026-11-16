# R749SSC — Exact phase-recovery thresholds over the five denominator-bias partitions

**Date:** 2026-11-16 (Asia/Shanghai). **Review:** AUTHOR_EXACT_NOT_REVIEWED. **Scientific pin:** a72226e2430ffa4786321ac86e7f0c599d5f0389. Follows the R749SSB common-bias model (this branch), and R749SSA independent-error results in [PR #2546](https://github.com/awdawmip/enterprise-math/pull/2546).

## A correlation poset rather than two unrelated noise models

Keep the positive labeled weights \(w=(1,1,2,3,6)\), marked first source, ideal six-phase signatures \(S_a=(P_a,P_{a+1},P_{a+5})\) for \(J=(0,1,5)\), with \(P=(455,-295,-25,185,-25,-295)/36\). The exact observed coordinate at \(q=r+h_i\) is

\[
Y_i=\frac{q^3(T_q+e_i)}{C_q+d_i}-q^4 H_4(q),\qquad
|e_i|\le M,\quad |d_i|\le K,\quad C_q+d_i>0,
\]

where \(C_q,T_q,H_4(q)\) retain their frozen definitions in R749SSB. Errors are integers. The new structure is a partition \(\pi\) of the three coordinate indices \(\{0,1,2\}\). Denominator errors are constant **within each partition block**, with independent values across distinct blocks. Numerator errors remain independently selectable.

There are exactly five partitions: \(012\) (all-common), \(01|2\), \(02|1\), \(12|0\), and \(0|1|2\) (fully independent). For each partition define its sharp global nearest-\(\ell_\infty\) phase recovery threshold \(N_\pi(M,K)\).

## Theorem 1: bias partitions form an exact recovery-order poset

If \(\pi_2\) refines \(\pi_1\) (splits one or more shared-bias blocks), then for all integer \(M,K\ge0\) under positive denominator constraints,

\[
\boxed{N_{\pi_1}(M,K)\le N_{\pi_2}(M,K).}
\]

**Proof.** Every vector whose denominator errors are constant on a block of \(\pi_1\) is also constant on every subset block created by refinement. Thus the admissible joint error set of \(\pi_1\) is a subset of that of \(\pi_2\), at each cutoff \(r\). Any cutoff at which every refined-model error vector is decoded correctly is also correct for the coarser model. Therefore the threshold is monotone in the refinement order. \(\square\)

This is an observer-specific joint-relation theorem: it does not identify independent error populations with a shared-error population.

## Theorem 2: the full five-partition sharp-threshold table, M,K≤2

Each cell below gives \((N_\pi(0,K),N_\pi(1,K),N_\pi(2,K))\), for numerator budgets \(M=0,1,2\). The three K=0 values are always \((35,53,65)\).

| Denominator partition | K=1; M=0,1,2 | K=2; M=0,1,2 |
|---|---|---|
| **012 all-common** | **(41,55,67)** | **(41,59,71)** |
| **01|2** | (261,267,273) | (497,503,503) |
| **02|1** | (261,267,273) | (507,513,513) |
| **12|0** | **(249,255,261)** | **(409,415,415)** |
| **0|1|2 independent** | (261,267,273) | (507,513,513) |

The three two-block partitions are **incomparable** in the refinement poset and have different sharp thresholds: when \(M=K=2\), preserving the bias relation for offsets 1 and 5 (partition \(12|0\)) lowers the threshold from 513 to 415; preserving the relation for offsets 0 and 1 (\(01|2\)) lowers it to 503; preserving the relation for offsets 0 and 5 (\(02|1\)) leaves it at 513. Thus the location of the retained correlation matters, not only the number of retained error degrees of freedom.

Exact last-failure examples at \(M=K=2\):

| Partition | Failure cutoff \(r\) | Phase → rival | Denominator triple \(d\) | Numerator triple \(e\) |
|---|---:|---|---|---|
| 012 | 70 | 4 → 3 | (-2,-2,-2) | (-2,2,-2) |
| 01|2 | 502 | 4 → 3 | (-2,-2,+2) | (-2,2,-2) |
| 02|1 | 512 | 2 → 3 | (-2,+2,-2) | (-2,-2,+2) |
| 12|0 | 414 | 0 → 3 | (+2,-2,-2) | (-2,+2,-2) |
| 0|1|2 | 512 | 2 → 3 | (-2,+2,-2) | (-2,-2,+2) |

**Proof and exact completeness.** For any fixed block-error assignment, scalar observations remain increasing in their own numerator errors. Exactly as in the R749SSB extreme-coordinate theorem, an adversarial rival exists iff a failing vector exists with one numerator error at \(\pm M\); the other numerator errors are decided by exact rational integer intervals. Enumerate only assignments of one denominator error per block. All positive-denominator constraints are enforced, including the small-cutoff cases. The standard-library certificate performs the complete finite check \(1\le r<N_{\mathrm{independent}}(M,K)\) for each of the five partitions and nine budget pairs: **12,390** exact cutoff/partition/budget decisions. For each result it records the last failing cutoff, a concrete error vector, exact rival and true distances and the chosen partition. It independently brute-force compares the extreme-coordinate checker to the complete error-vector cubes for \(r=1,\ldots,16\) and all 45 combinations: **720** cases, all PASS.

For the infinite part, R749SSA already proves that the independent-error decoder succeeds at every \(r\ge N_{\mathrm{independent}}(M,K)\) for these nine budgets, with a fully specified exact finite-plus-infinite certificate. Every partition-restricted joint error set is contained in that independent-error set. Therefore no untested failure exists above the finite scan; every displayed threshold is global and sharp by its recorded last-failure witness. \(\square\)

## Reproduction and limits

Run the R749SSB certificate in the same directory, then the accompanying independent Python file R749SSC_PARTITION_BIAS_CERT.py; it imports R749SSB's exact source-count arithmetic and writes R749SSC_PARTITION_BIAS_RESULTS.json with every one of 45 certificates. The committed compact JSON records the full 45 thresholds and five selected maximal-budget witnesses; the executable reproduces the expanded result. All arithmetic is standard-library integer/Fraction arithmetic.

This is an author-side exact result for a frozen positive-source observer. The cited R749SSA infinite-tail result is an explicit mathematical dependency; no independent external review, signed BRC port morphism, physical-time assertion, or canonical Foundation admission is claimed.

**Next unresolved scientific unit:** Classify the full phase-dependent asymptotic of \(N_\pi(M,K)\) as budgets grow, and identify which bias-partition refinements are observationally invisible in restricted future-operation horizons. Test a source-provenance-preserving BRC interface separately rather than treating a period-six scalar observer as native X6 spatial state.