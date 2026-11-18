# R266 — Exact weighted zero-only observer phase diagrams

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / NOT_REVIEWED**. Independent portable scientific continuation, without a formal Task CLAIM or Result/Review acceptance.

## Immutable scientific inputs and scope

Reuses R265 at commit `4ed8378e61389385e4bb8848b605d4c58ee8517f`, file `research_notes/portable_direct/R265_OPTIMAL_SEQUENTIAL_ZERO_ONLY_OBSERVER_20261118.md`; frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

The seven-source **auxiliary positive-rational scalar model** remains unchanged: \(s=67/169,\ J=1184397599,\ T=989553240,\ K=3805974000,\ p=13\). Its 63 labelled normalized integer sequences are \(q_{m,k}=(JT^k/K)h_{m,k}\) for \(k\ge3\). Modulo 13 each has period dividing 2184 by its exact integer monic characteristic recurrence and the 249 shifted-tap equalities.

The decision predicate is whether *all 63* labelled \(q_{m,k}\) vanish modulo 13. There are 39 identically-zero supports and 24 active labels forming six **Boolean-support-equivalent** classes represented by 9, 10, 12, 13, 24 and 26; the all-zero predicate occurs at two of the 2184 phases. Class equivalence preserves only this Boolean query at a fixed event, **not** numerical values, multiplicity, source identity, signed ports, provenance or native BRC dynamics. The event phase \(n=(k-3)\bmod2184\) is not directly visible to the querying algorithm.

Each Boolean probe queries an *original* source label and returns whether that source is nonzero modulo 13. On a nonzero response the algorithm may immediately answer “not all zero”; on a zero response it may continue. It must answer correctly on every phase (including any phase of zero probability). Only the number/cost of original-label Boolean probes is optimized.

## Theorem 1: exact weighted observer principle

Let \(U_i\subseteq\{0,\ldots,2183\}\) be the nonzero-event support of active class \(i\), \(U=\bigcup_i U_i\), and \(A(S)=\bigcup_{i\in S}U_i\). Suppose phase \(n\) has a nonnegative rational workload weight \(w_n\), not all zero, and the query cost for any original label in support class \(i\) is the same strictly positive rational \(c_i\). Define the remaining workload mass
\[
M(S)=\sum_{n\notin A(S)}w_n.
\]
The globally optimal deterministic zero-only strategy has minimum *unnormalized* expected probe cost given by the exact 64-state recursion
\[
F(S)=
\begin{cases}
0,&A(S)=U,\\
\min_{i\notin S}\{c_i M(S)+F(S\cup\{i\})\},& A(S)\neq U.
\end{cases}
\]
The normalized expected cost is \(F(\varnothing)/\sum_n w_n\).

**Proof.** The algorithm has only one continuing path: the path on which every prior answer was zero. Any nonzero probe already certifies that the all-zero predicate is false, so another strictly positive-cost query cannot improve the decision. A repeat of a support profile provides no new Boolean information. As long as \(A(S)\ne U\), there is a phase in \(U\setminus A(S)\) that has exactly the same observed zeros as one of the two genuinely all-zero phases. Hence a globally correct algorithm cannot yet return all-zero. When \(A(S)=U\), all remaining phases satisfy the all-zero predicate, so returning all-zero is correct. The next query is paid exactly on the still-surviving phases, whose weighted mass is \(M(S)\); induction yields the displayed recurrence. All possibly optimal all-zero paths are truncated permutations of six support classes. If some \(w_n=0\), the correctness condition \(A(S)=U\) remains unchanged.

## Theorem 2: sharp sensitivity to a source-class probe cost

Take uniform workload weights \(w_n=1\). Give every one of the **eight source labels in support class 9** (9, 14, 27, 29, 41, 46, 59, 61) query cost \(\theta\ge1\), and every label in the other five active classes query cost 1. This includes the cost of alternative equivalent labels so no cheaper substitute for class 9 is hidden. The minimum total cost over one full 2184-event period is exactly
\[
\boxed{C_9(\theta)=
\begin{cases}
172+2184\theta,&1\le\theta\le169/168,\\
2200+168\theta,&169/168\le\theta\le15/14,\\
2380,&\theta\ge15/14.
\end{cases}}
\]
Optimal paths on the three open intervals are respectively
\[
(9,26,10,13),\quad (26,9,10,13),\quad(26,12,10,13).
\]
At the thresholds multiple paths tie. The mean cost per event is \(C_9(\theta)/2184\). The uniform-cost optimal first query ceases to be optimal after an increase of only \(1/168\) in class 9 probe cost (approximately 0.5952%). Once \(\theta>15/14\), the optimal displayed path avoids that source class.

## Theorem 3: sharp sensitivity to a phase-biased workload

Keep all query costs at 1, but assign each phase with \(n\bmod6=0\) weight \(\alpha\ge1\), all other phases weight 1. There are 364 such phases and 1820 others, hence total workload weight is \(1820+364\alpha\). The exact optimum over one weighted period is
\[
\boxed{C_{\mathrm{phase}}(\alpha)=
\begin{cases}
1936+420\alpha,&1\le\alpha\le3/2,\\
1972+396\alpha,&3/2\le\alpha\le5,\\
1992+392\alpha,&5\le\alpha\le8,\\
2216+364\alpha,&\alpha\ge8.
\end{cases}}
\]
One optimal order on each open interval is, respectively,
\[
(9,26,10,13),\quad (26,9,10,13),\quad
(26,10,9,13),\quad(10,26,9,13).
\]
The expectation is \(C_{\mathrm{phase}}(\alpha)/(1820+364\alpha)\). At \(\alpha=2\), the new optimum uses 2764 weighted probe units while the original uniform-prior order uses 2776 under the same workload.

## Exhaustive finite proof and reproducibility

The self-contained standard-library checker `R266_weighted_cost_phase_certificate.py` rederives all 63 rational initial sequences with `Fraction`, computes the integer-scaled characteristic recurrence, checks **249 shifted period taps**, reproduces the six labelled support-equivalence classes and **2182 nonzero / 2 all-zero** phases, and enumerates all \(6!=720\) class permutations separately for each parameter family. Every truncated permutation defines an integer-affine cost \(a+b\theta\) or \(a+b\alpha\), obtained by counting the exact surviving phase set after each probe.

Deduplicated candidate affine functions number **333** for \(\theta\) and **209** for \(\alpha\). Their pointwise minimum is a piecewise affine function. The checker constructs the exact lower envelope using sorted slopes and rational pairwise line intersections, checking a representative rational point of each resulting interval against all candidate lines and separately checking specified rational boundary values. The minimum-envelope formulas are exactly the two displayed piecewise expressions. The algebraic fact that two affine lines can change order only at their unique rational intersection establishes validity on whole open intervals; equalities hold at the endpoints by direct substitution. A periodic monic recurrence with 249 matching shifted initial taps extends the support certificate to **every** \(k\ge3\), so both theorems hold for any number of repeated 2184-period workloads.

Running `python R266_weighted_cost_phase_certificate.py` produces `R266_verification.json` and prints `R266 PASS`. It checks exact fractions and integer bitsets only. Coverage: both infinite-\(k\) claims conditional on the stated periodic auxiliary model, exact finite support/optimization certificates. Independent expert review and native typed BRC correspondence remain open.

## Observation and future-operation boundary

These optimal observers preserve only the **Boolean all-zero predicate** under the stated fixed-event label queries. They do not reconstruct the 63 rational values or preserve signed Port/source histories under arbitrary state-changing operations. No assertion transfers them to the P000 six-dimensional native world or a three-dimensional native slice. P000 and the frozen science remain unchanged.

**Next:** determine exact optimal cost chambers in the full six-dimensional positive class-price cone (five-dimensional up to common scaling), including simultaneous price and phase-prior perturbations; seek the smallest provenance-preserving typed BRC observer whose Boolean projection recovers these costs without losing source/Port semantics.
