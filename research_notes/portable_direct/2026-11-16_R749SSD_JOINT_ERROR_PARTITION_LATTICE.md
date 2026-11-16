# R749SSD — Sharp six-phase recovery on the product of two error-partition lattices

**Date:** 2026-11-16 (Asia/Shanghai). **Research status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen scientific input:** a72226e2430ffa4786321ac86e7f0c599d5f0389. Follows [R749SSC PR #2549](https://github.com/awdawmip/enterprise-math/pull/2549) at 9ee299403fa7125bbdd5797d82113311228e9f6a and the infinite-tail theorem of [R749SSA PR #2546](https://github.com/awdawmip/enterprise-math/pull/2546).

## Research question

The previous result classified correlations between denominator-count errors at three sampling positions. This result classifies **simultaneous and independently specified partitions of numerator-error sources and denominator-error sources**, preserving both joint relations rather than treating six errors as independent. It establishes 225 globally sharp recovery thresholds.

Use the frozen five distinct labeled positive sources with weights \(w=(1,1,2,3,6)\), marking the *first* weight-one source. For integer \(q\ge1\) set

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^{5}:\sum_jw_jk_j\le q-1\},\qquad C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

The three offsets are \(J=(0,1,5)\). Retain the frozen smooth part

\[
H_4(q)=\frac16+\frac1{2q}-\frac{115}{36q^2}+\frac{115}{6q^3}-\frac{16315}{108q^4}
\]

and the ideal period-six residual \(P=(455,-295,-25,185,-25,-295)/36\). The ideal signature for phase \(a\) is \(S_a=(P_a,P_{a+1},P_{a+5})\), indexed modulo 6.

The observation at \(q_i=r+J_i\) is

\[
Y_i=\frac{q_i^3(T_{q_i}+e_i)}{C_{q_i}+d_i}-q_i^4H_4(q_i),
\qquad C_{q_i}+d_i>0,
\]

where the integer budgets are \(|e_i|\le M,\ |d_i|\le K\).

Let \(\pi_e\) and \(\pi_d\) independently be any set partition of indices \(\{0,1,2\}\). An error vector respects a partition if coordinates in the same block have equal integer errors. The five partitions, in the order used throughout, are **012 (all-common), 01|2, 02|1, 12|0, 0|1|2 (independent)**. Denominator and numerator partitions may differ.

Define \(N_{\pi_d,\pi_e}(M,K)\) as the least integer \(N\ge1\) such that **for every** \(r\ge N\) and every admissible pair of partition-respecting error vectors, the unique nearest \(S_a\) under \(\ell_\infty\) is \(S_{r\bmod6}\). An exact tie counts as failure.

## Theorem 1 — two-parameter partition refinement is monotone

If \(\pi'_d\) refines \(\pi_d\) and \(\pi'_e\) refines \(\pi_e\), then for every \(M,K\ge0\),

\[
\boxed{N_{\pi_d,\pi_e}(M,K)\le N_{\pi'_d,\pi'_e}(M,K).}
\]

**Proof.** A joint numerator/denominator error vector constant on each coarser block remains constant on every refined block. Positivity constraints on denominators are unchanged. Therefore the set of admissible observation vectors for the coarser pair is contained in that of the refined pair for every fixed cutoff. Correctness for all refined vectors implies correctness for all coarser vectors. The earliest all-future-success cutoff is consequently monotone in each partition coordinate. The same inclusion shows nondecreasing thresholds under increases of \(M\) or \(K\). \(\square\)

## Theorem 2 — 225 exact global thresholds (M,K in 0..2)

The attached executable certificate returns **nine full 5-by-5 matrices** of sharp thresholds, totaling \(9\times25=225\) values. Rows indicate denominator partition \(\pi_d\), columns indicate numerator partition \(\pi_e\), both in the fixed order 012, 01|2, 02|1, 12|0, 0|1|2.

For the maximal tested budgets \(M=K=2\), the sharp matrix is

| denominator \ numerator | 012 | 01\|2 | 02\|1 | 12\|0 | 0\|1\|2 |
|---|---:|---:|---:|---:|---:|
| **012** | **47** | 71 | 71 | 67 | 71 |
| **01\|2** | 497 | 503 | 503 | 497 | 503 |
| **02\|1** | 507 | 513 | 513 | 507 | 513 |
| **12\|0** | 409 | 409 | 415 | 415 | 415 |
| **0\|1\|2** | 507 | 513 | 513 | 507 | **513** |

Thus keeping both *actual all-common* count biases reduces the global threshold from 513 (both fully independent) to **47**, with the same three offsets and the same decoder. Keeping only the denominator correlation gives 71; keeping only numerator correlation gives 507. At \(M=2,K=0\), an all-common numerator error alone gives threshold **41**, against 65 when the numerator errors are independent.

**Sharp witness for fully common numerator and denominator errors:** at \(r=46\), true phase 4 and rival phase 3, take \(e=(1,1,1)\), \(d=(-2,-2,-2)\). The exact maximum-norm distances are

\[
D_{\rm true}=\frac{230239889}{5146956},\qquad
D_{\rm rival}=\frac{663545677}{14841900}<D_{\rm true}.
\]

All 25 maximal-budget entries have exact last-failure vectors in the committed result file; the executable certificate generates the corresponding witnesses for all 225 entries.

**Proof of completeness.** Fix \(\pi_d,\pi_e,M,K\). At each \(r\) enumerate one integer in the allowed interval per block of each partition, expand the block assignments to three coordinates, enforce \(C_{r+J_i}+d_i>0\), and calculate the three \(Y_i\) exactly as rational numbers. For each legal observation compare its true maximum-norm distance with all five rival distances; a tie or closer rival is a failure. This covers every admissible joint vector by construction, without assuming that numerator coordinates can vary independently.

The **prior certified threshold** \(U=N_{\pi_d,\mathrm{independent}}(M,K)\), from R749SSC, is a rigorous upper bound for every numerator partition by Theorem 1. R749SSC obtains its globally valid bound from its exact finite certificates and the R749SSA infinite-tail theorem. Therefore this new certificate only needs to check integers \(r=U-1,U-2,\ldots\), stopping at the first failing cutoff \(L\). Every \(r\) satisfying \(L<r<U\) was checked and passed, and every \(r\ge U\) passes by the prior theorem. The recorded witness at \(L\) proves that \(N=L+1\) is the **least** all-integer threshold. No monotonicity in the individual cutoff \(r\) is assumed.

The certificate performs **773 complete finite cutoff/partition/budget tests**, recovers all 45 preceding denominator-partition thresholds in its independent-numerator column, verifies refinement monotonicity in both coordinates and budget monotonicity across all 225 values, and completes **300 separate direct independent-cube crosschecks** on specified small cutoffs. A second small-population nested enumeration checks the dynamic-programming \(C_q,T_q\) for \(q=1,\ldots,12\). All comparisons use exact Python integers and fractions. The script reports PASS and writes the full 225-value table plus 25 maximal-budget exact witnesses.

## Scope, evidence, and next mathematical dependency

These are **author-side exact results conditional on the predecessor R749SSA/R749SSC published infinite-tail theorem at its stated model and pin**. They do not change P000, create a signed BRC port mapping, equate the auxiliary cutoff \(r\) to native physical time, or claim a Foundation Result/independent review.

The new feature is *joint observability*: replacing a physically common error by three independent error degrees of freedom destroys relevant correlations and can increase the recovery threshold. It is a precise example of the ACTIVE residual-fidelity principle in an auxiliary source observer.

**Next:** classify observational equivalence of partition pairs under restricted future shifts, and determine the two-budget large-noise asymptotic surface when numerator and denominator partitions refine at different rates. Any X6/BRC transfer must preserve actual source labels, signs, branches and future-operation relations with an explicit typed map rather than identifying a six-phase integer index with a native spatial coordinate.

Reproduce using the adjacent standard-library file R749SSD_JOINT_PARTITION_EXACT_CERT.py; it creates R749SSD_JOINT_PARTITION_EXACT_RESULTS.json.