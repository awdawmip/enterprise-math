# R749SSH — Sharp scale-dependent noise margin for complete unknown-cutoff ratio recovery

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen source model:** `a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessors:** R749SSF (exact raw-ratio recovery) and R749SSG (uniform cutoff-only noise radius), both in Draft PR #2557.

## Exact statement

For five distinct positive labeled sources with weights `w=(1,1,2,3,6)`, let

\[
C_q=\#\{k\in\mathbb Z_{\ge0}^5:\sum_jw_jk_j\le q-1\},\qquad
T_q=\sum_{\sum_jw_jk_j\le q-1}k_1.
\]

Each legal integer error pair `(e,d)∈{-2,-1,0,1,2}²` gives the raw rational ratio

\[
X(q,e,d)=\frac{T_q+e}{C_q+d}.
\]

**Theorem.** For every integer cutoff `q≥28`, the exact smallest separation among the 25 distinct raw ratios at that cutoff is

\[
\boxed{\min_{(e,d)\ne(e',d')}|X(q,e,d)-X(q,e',d')|=\frac1{C_q+2}.}
\]

This simple formula has a **sharp global integer starting threshold 28**: at `q=27` the true minimum is `2615/25244502`, strictly less than `1/8703`, with pairs `(e,d)=(2,2)` and `(e',d')=(-2,1)`.

Combined with R749SSG's global **inter-cutoff** lower bound `1/201`, this proves the following sharp scale-dependent statement: for any true unknown `q≥28`, arbitrary real additive perturbation of the single observed ratio with

\[
\boxed{|\eta|<\frac1{2(C_q+2)}}
\]

preserves unique recovery of the *entire* triple `(q,e,d)` by the nearest-legal-ratio decoder, even with competitor cutoffs `q'ge6`. Equality of the noise radius is sharp in the worst case at every such q, because two adjacent numerator errors at `d=2` have exactly that separation and a midpoint tie.

The bound depends on the unknown true q; it describes a conditional robustness guarantee rather than a measurement algorithm that knows q in advance.

## Exact proof

**Case 1: equal denominator error `d=d'`.** Distinct integer numerators differ by at least one, hence

\[
|X(q,e,d)-X(q,e',d)|=\frac{|e-e'|}{C_q+d}
\ge\frac1{C_q+2}.
\]

Equality is attained by `d=2` and adjacent permitted numerator errors.

**Case 2: different denominator errors `d
e d'`.** Cross-multiplication yields the *integer* numerator

\[
N=T_q(d'-d)+C_q(e-e')+ed'-e'd.
\]

Since `|d'-d|≥1`, `|e-e'|≤4` and `|ed'-e'd|≤8`,

\[
|N|\ge T_q-4C_q-8.
\]

We now prove

\[
\boxed{T_q\ge5C_q+10\qquad(q\ge28).}
\]

The attached exact integer recurrence independently checks this for `28≤q≤47`, beginning with `C_{28}=10126`, `T_{28}=51356`, so `T_{28}-5C_{28}=726`.

For every shell of *exact* source weight `m≥47`, decompose each labeled source occupancy uniquely as

\[
k_j=(6/w_j)n_j+t_j,\quad 0\le t_j<6/w_j,\quad
B_t=\sum_jw_jt_j\le17.
\]

In each nonempty residue block, the five nonnegative integers `n_j` satisfy the exact relation `sum_jn_j=L=(m-B_t)/6≥5`. By symmetry among five variables, the average `n_1` over the `inom{L+4}{4}` compositions is `L/5`. Thus the average marked-source count equals

\[
6L/5+t_1\ge 6>5.
\]

After adding a shell, the difference `T_{m+1}-5C_{m+1}` is at least its previous value; it is therefore nondecreasing for `m≥47`. The finite base `q=47` is already above 10, which proves the inequality for the infinite tail, and together with the finite check covers every `q≥28`.

It follows that `|N|≥C_q+2`. Since the two different denominator offsets cannot both equal +2, their positive denominator product is **strictly less than** `(C_q+2)^2`. Consequently

\[
|X(q,e,d)-X(q,e',d')|
=\frac{|N|}{(C_q+d)(C_q+d')}
>\frac1{C_q+2}.
\]

Combining both cases establishes the precise minimum. The q27 witness establishes the sharp start.

Finally, R749SSG proves every pair of observations from *different* cutoffs is separated by at least `1/201`. For `q≥28`, `C_q≥10126`, so `1/(C_q+2)<1/201`. The nearest competitor therefore comes from the same cutoff and has the computed exact separation. The midpoint gives the precise noise bound. `□`

## Reproducibility and limitations

`R749SSH_SCALE_DEPENDENT_FULL_TRIPLE_CERT.py` uses standard-library exact Fraction arithmetic with exact finite exhaustive comparison of 25 ratios at each q=6..500; verifies the shell average/monotonic inequality across q=47..499; and records all exact minimum gaps for q=6..27 including the last failing q27. The unbounded part is the symmetric-composition shell argument above, not a finite extrapolation. The machine-readable results are `R749SSH_SCALE_DEPENDENT_FULL_TRIPLE_RESULTS.json`; local run returned `PASS`.

This work applies to the **raw ratio** observer, not the earlier smooth-subtracted Y readout, whose infinite unknown-cutoff injectivity remains open. The auxiliary source model has not been promoted to a native signed BRC/Cell/Link/Port time law.

**Next:** classify sharp same-cutoff error-pair separation analytically for `6≤q≤27` (the finite exact table is supplied); determine noise-aware decoding when q is not even approximately bounded and the noise budget must be assigned before q is observed; investigate the original Y readout's infinite collision question.
