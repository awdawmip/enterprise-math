# EC49FQN — Seven-price-grid exact BRC sections and a certified global two-parameter enclosure

**Date:** 2026-11-16. **Scientific status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Frozen scientific input:** awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. **Predecessors:** EC49FQM PR #2552, EC49FQL PR #2548, EC49FQI PR #2539. This is independent portable research, with no new canonical Task, CLAIM, Result, Review, P000 modification, or physical calibration.

## 1. Exact native BRC model and cost functions

This is the original class represented by configuration 16943: 310 configurations, 141 *complete named-root* observational profiles, 144 terminal scalar observations, 84 named-root scalar observations (228 physical query indices; 209 distinct response partitions). A finite adaptive decision tree must distinguish all 141 full profiles. Every executed observation must split its live candidate subset. Root observations cost \(r>0\), terminal observations \(t>0\); write \(x=r/t\).

For multiplicities \(m_i\), with \(\sum_i m_i=310\), use the prior interpolation
\[
p_\lambda(i)=\frac{1-\lambda}{141}+\frac{\lambda m_i}{310},\quad 0\le\lambda\le1.
\]
The dimensionless unrestricted optimum is \(v(\lambda,x)=V(\lambda;r,t)/t\). Five complete, explicitly replayed native decision-tree costs are
\[
\begin{aligned}
A&=(1-\lambda)(6x+290)/141+\lambda(6x+751)/310,\\
B&=(1-\lambda)(5x+293)/141+\lambda(5x+704)/310,\\
C&=(1-\lambda)(5x+295)/141+\lambda(5x+685)/310,\\
B_h&=(1-\lambda)(4x+296)/141+\lambda(4x+707)/310,\\
C_h&=(1-\lambda)(4x+298)/141+\lambda(4x+688)/310 .
\end{aligned}
\]
The count vectors (uniform-root, uniform-terminal; multiplicity-root, multiplicity-terminal) for A, B and C are respectively \((6,290;6,751)\), \((5,293;5,704)\), and \((5,295;5,685)\). These are feasible native strategies, not informal cost fits. Their root/terminal index witnesses have first observations A: 32 or 34, B: 140 or 142, C: 16 or 23.

Define
\[
\beta=620/3299,\quad \gamma(x)=310(3-x)/(7557-169x),\quad F(\lambda,x)=\min(A,B,C).
\]
For \(0\le\lambda\le\beta\), \(F=\min(A,B)\), because
\[
A-B=(1-\lambda)(x-3)/141+\lambda(x+47)/310,\quad
C-B=2(1-\lambda)/141-19\lambda/310 .
\]

## 2. Theorem A — two previously unproved complete real-prior slices

For **each** of the exact price ratios \(x=4/3\) and \(x=8/3\), and **every real** \(0\le\lambda\le1\), the unrestricted native optimum is
\[
\boxed{v(\lambda,x)=F(\lambda,x)=\min(A,B,C).}
\]
The first transition is \(\gamma(4/3)=310/4399\), or \(\gamma(8/3)=310/21319\), respectively. The second transition is \(\beta=620/3299\) in both cases. The **complete physical optimal first-observation index sets**, including all ties, are:

| Range of prior interpolation | All globally optimal physical first queries |
|---|---|
| \(0\le\lambda<\gamma(x)\) | 32, 34 |
| \(\lambda=\gamma(x)\) | 32, 34, 140, 142 |
| \(\gamma(x)<\lambda<\beta\) | 140, 142 |
| \(\lambda=\beta\) | 16, 23, 140, 142 |
| \(\beta<\lambda\le1\) | 16, 23 |

**Proof.** For each of the two prices, compute *all unrestricted* Bellman values and physical optimal first queries at \(\lambda=0,\gamma(x),\beta,1\). The 8 primary exact-integer certificates and an independent 141-state Bellman implementation establish the table above. All 228 physical first queries are evaluated. At each rational endpoint, all optimal first-query witness trees are replayed over the full native profile population and attain exactly the corresponding A/B/C cost vector.

At fixed \(x\), the cost of any admissible finite adaptive decision tree is affine in \(\lambda\). Choose the fixed feasible A, B, or C tree that is optimal at two successive verified endpoints. For any competing tree, its cost gap over the witness is affine and nonnegative at both endpoints, hence nonnegative for every intermediate real prior. All strict interior optimal first actions are exactly the intersection of the optimal first-action sets at the two endpoints; the replayed witnesses give the reverse inclusion. The explicit A−B and C−B formulas give the two rational intersections and strict inequalities on either side. QED.

## 3. Theorem B — continuous global cost enclosure over all priors and all \(x\ge1\)

Combine the already-proved complete sections \(x=1,3/2,2,5/2,3\) (EC49FQI/FQL/FQM) with Theorem A. They form a **seven-price grid**
\[
G=\{1,\ 4/3,\ 3/2,\ 2,\ 5/2,\ 8/3,\ 3\}.
\]
For every one of these 7 prices and every real prior \(\lambda\in[0,1]\), \(v(\lambda,x)=F(\lambda,x)\).

Let \(1\le x\le3\), and let \([a,b]\) be any consecutive grid interval containing \(x\). Define the *explicit rational/real-parameter lower certificate*
\[
L_{a,b}(\lambda,x)=\frac{b-x}{b-a}F(\lambda,a)+\frac{x-a}{b-a}F(\lambda,b).
\]
Then for all real \(0\le\lambda\le1\) and \(1\le x\le3\),
\[
\boxed{ L_{a,b}(\lambda,x)\le v(\lambda,x)\le F(\lambda,x),\quad
0\le F(\lambda,x)-v(\lambda,x)\le\frac{25}{28538}<0.000877.}
\]
Since \(v=V/t\), the absolute expected-cost difference is at most \(25t/28538\), with arbitrary positive prices and no bounded-depth restriction. At each grid price, the bound collapses to equality. The inherited exact results give \(v=C\) throughout \(\beta\le\lambda\le1,\ 1\le x\le3\), and
\[
v=\min(B_h,C_h)\quad\text{for all }\lambda\in[0,1],\ x\ge3.
\]
Thus the uniform bound applies on the **entire half-infinite parameter domain** \(0\le\lambda\le1,\ x\ge1\) (error zero in those exact subdomains).

**Proof of enclosure.** For fixed \(\lambda\), the cost of any correct finite adaptive decision tree is affine in \(x\), because it has fixed expected counts of root and terminal queries. The infimum of these affine costs is concave. Concavity and the two independently established exact grid values imply \(v(\lambda,x)\ge L_{a,b}(\lambda,x)\). The full native A/B/C trees are feasible for every parameter, so \(v(\lambda,x)\le F(\lambda,x)\).

For \(\lambda\ge\beta\), the inherited theorem establishes \(v=C\). For \(0\le\lambda\le\beta\), \(F=\min(A,B)\) has at most one kink, at
\[
s=x_c(\lambda)=\frac{930-7557\lambda}{310-169\lambda},
\]
with positive slope decrease
\[
d(\lambda)=\frac{\partial A}{\partial x}-\frac{\partial B}{\partial x}
=\frac{1-\lambda}{141}+\frac{\lambda}{310}.
\]
If \(s\notin(a,b)\), \(F\) is affine on \([a,b]\), and therefore \(F=L=v\) **everywhere** in that entire price segment. If \(a<s<b\), the exact gap of the upper and lower certificates is
\[
F-L=\begin{cases}
d(\lambda)(x-a)(b-s)/(b-a),&a\le x\le s,\\
d(\lambda)(s-a)(b-x)/(b-a),&s\le x\le b .
\end{cases}
\]
Its maximum is \(d(\lambda)(s-a)(b-s)/(b-a)\le d(\lambda)(b-a)/4\). Since \(\gamma\) is strictly decreasing and \(a<s<b\), \(\lambda\ge\gamma(b)\). Since \(d\) decreases with \(\lambda\), the error is bounded above by the rational number \(d(\gamma(b))(b-a)/4\). In order over the six consecutive grid intervals, these **six exact rational bounds** are:

| Consecutive prices \([a,b]\) | Bound for \(F-L\) |
|---|---|
| \([1,4/3]\) | \(5/8798\) |
| \([4/3,3/2]\) | \(25/87642\) |
| \([3/2,2]\) | \(25/28876\) |
| \([2,5/2]\) | \(25/28538\) |
| \([5/2,8/3]\) | \(25/85276\) |
| \([8/3,3]\) | \(1/1692\) |

The maximum equals \(25/28538\), and \(0\le F-v\le F-L\). QED.

**Interpretation.** The explicit policy F is now proven within 0.000877 terminal-price units of the exact unrestricted optimum for *every prior and every price ratio at least 1*. Its claimed phase boundary \(\lambda=\gamma(x)\) is exact on seven full price sections. A third native strategy could still improve F at some unsolved interior point, but any such improvement is bounded by this certificate.

## 4. Reproducible exact evidence, calculation, and provenance

The raw native inputs have SHA256:
- frozen_original_master.txt: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e
- EC49FPG_PROFILE.csv: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f

At each rational prior \(\lambda=a/b\), the independent Bellman solver uses positive integer profile weights \(310(b-a)+141 a m_i\) and the exact 209-partition recurrence. There are 8 **new** full integer Bellman anchors, all with 228 physical-first-action verification; each stored first-query witness is re-executed against the original 141 profiles/310 multiplicities. There are 17 inherited anchors in the combined self-contained evidence package (13 EC49FQM, 4 EC49FQL x=2), giving **25 exact independently recomputed anchors**. New independent validation and the three partitioned full-regression runs all passed. The analytical concavity and affine-interpolation proofs, rather than finite sampling alone, establish the real-continuum statements.

The self-contained artifact accompanying EC49FQN contains 25 full JSON Bellman certificates, native frozen source data, original and independent solver scripts, full theorem, actual validation logs, a machine manifest, and SHA256SUMS. Reproduce with: unpack; run sha256sum -c SHA256SUMS; run PYTHONPATH=code python3 code/EC49FQN_VERIFY_25.py (or run it with group arguments 0,1,2 separately). A source SHA merely selects the data version, while the independent exact recurrence and proof supply the mathematical evidence.

The deduplication of 228 physical queries to 209 response partitions is scoped to scalar observation of this fixed live profile set, with equal action price and identical response fibers. Original physical index labels are retained for first-action classification. Joint relations, provenance, hidden named-root distinctions and future-observer semantics outside this experiment are unchanged.

## 5. Remaining mathematical problem

Determine whether \(v(\lambda,x)=F(\lambda,x)\) **throughout** the remaining low-prior corridor \(0<\lambda<155/1847,\ 1<x<3\), including all non-grid prices, or construct a correct native decision tree and exact rational parameter witness with cost strictly below F. A useful next solver will construct a parametric Bellman lower envelope in lifted coordinates \((x,\lambda,\lambda x)\) and verify region coverage with rational inequalities. Retain current scientific source pins and formal control boundaries; the current author-verified mathematical material is not yet independent peer-reviewed or adopted as a canonical Result.
