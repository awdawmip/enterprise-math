# PREFIX-626B — Exactly n−6 additional continuous coordinates recover full gate-tagged paths

Date: 2026-11-09 (Asia/Shanghai). Companion to PREFIX-626, same original native 48-phase/96-port/576-action positive X6-BRC and frozen science `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original scientific source: PREFIX-625 native action enumerator, PR #1869. Researcher EM-X6-E90CA6; research activity RA-DBF18FC5261DB71FA7124AE9. Status: author-side exact theorem/certificate, independent review pending.

## Exact question and carrier

At fixed known finite length n≥2, suppose the observer already retains the entire terminal-operator sufficient statistic from PREFIX-626:

[
S_n(g)=(g_1,g_n, (P_r)_{I_r\ne\varnothing}),\quad
I_r=\{j:2\le j\le n-1,\ j\equiv r\pmod4\},
\quad P_r=\prod_{j\in I_r}(1+g_j/3).
]

For every g_j≥0, let \(J^{\mathrm{tag}}_n(g)\) denote the *full ordered source/action-labelled native BRC path operator*: for each original precursor port, keep the mass of every legal ordered length-n action path including original labels. This gate-history observation is distinct from the linear rank of \(J_n\) as an operator in the *initial precursor vector* in PREFIX-625. Ask the minimum number of supplementary **continuous real scalar functions of the gate sequence**, in addition to \(S_n\), sufficient to reproduce \(J^{\mathrm{tag}}_n(g)\) for all nonnegative gates. Arbitrary discontinuous encodings of reals are outside this numerical/continuous-state representation class.

## Theorem 626B.1 — every historical gate is directly readable in the fully tagged operator

The original zero-gate positive BRC actions include the following two directed weight-one cycles:

[
9\to28\to80\to52\to9,
\qquad
29\to80\to52\to8\to29.
]

The original gate-dependent action is the *labelled* edge \(9\to29\), label \((14,4,1,1)\), of weight exactly g at that time. All cycle actions have weight exactly 1 for every gate g≥0 (their original labels are verified in the checker).

Fix any n≥1 and any gate position 1≤j≤n. Use the first cycle backwards to construct a weight-one prefix of length j−1 ending at port 9; cross 9→29 at step j; then use the second cycle forwards for a weight-one suffix of length n−j. This is a legal original ordered BRC action path whose weight for unit input at its uniquely identified original source port is

[
\boxed{J^{\mathrm{tag}}_n(g)[\gamma_{n,j}]=g_j.}
]

Consequently, the complete tagged history operator determines **every individual gate g_j** exactly, for all n≥1 and all nonnegative gates. In particular, the gate-to-tagged-history observation is injective and has n independent scalar coordinate readouts.

## Theorem 626B.2 — sharp residual continuous memory law

Let c(n) be the number of nonempty interior mod-4 classes. For n≥2,
\(c(n)=\min(4,n-2)\). The exact minimum number of *additional continuous real scalar observations* beyond \(S_n\) required to recover the entire gate-tagged native path operator is

[
\boxed{m_{\min}(n)=n-2-c(n)=\max(0,n-6).}
]

**Constructive upper bound.** For each nonempty class \(I_r\), choose one position \(j_r\). Store the original gate values at all interior positions except these c(n) positions, a total of \(n-2-c(n)\) extra scalars. Recover the omitted gate exactly from its already-retained product:

[
\boxed{
g_{j_r}=3\left[
\frac{P_r}{\prod_{j\in I_r\setminus\{j_r\}}(1+g_j/3)}
-1\right].
}
]

All denominators are positive on the nonnegative gate domain. Recovered complete gate history determines all original labelled path weights.

**Lower bound.** Restrict to the strictly positive open set \((0,\infty)^n\). Fix both boundary gates and all c(n) products. After the smooth change of variables \(x_j=\log(1+g_j/3)\), these constraints become one independent sum equation for each nonempty residue group. Hence every interior generic fiber of \(S_n\) is a smooth cell of dimension \(d=n-2-c(n)\). By Theorem 626B.1 the full tagged path operator separates every distinct point of this fiber. If a continuous m-scalar added observer suffices, its restriction to this d-dimensional open fiber must be injective; by invariance of domain/dimension this requires m≥d. This matches the construction. The logarithm here is **only a proof-coordinate transformation of the gate parameter space**, not a native BRC evolution/observer or physical scientific arithmetic.

For n=6, the four interior gate positions occupy four separate classes and no supplementary state is required. For n=10, four additional gate coordinates are necessary and sufficient. The required supplementary continuous memory grows by one scalar per extra interior gate after all four classes are occupied, although the full terminal 96×96 operator remains controlled by the fixed six-quantity summary \(S_n\).

## Source-linked finite certificate

The standalone `PREFIX626B_native_gate_full_tagged_memory_checker.py` constructs all 576 original typed BRC actions, verifies both unit cycles and the gate-labelled edge, builds an explicit one-gate path for **every gate position** across 13 test lengths \(n=2,3,4,5,6,7,8,9,10,13,17,32,64\) (180 positions total), tests exact rational path weights, and verifies reconstruction of every gate from \(S_n\) plus the prescribed minimum extra coordinates. All executed assertions passed; the proof for all n is supplied by the two cycles, regular-fiber dimension and explicit inverse formula.

This is a theorem about **full source/action-labelled ordered paths**, all original precursor ports, known horizon, nonnegative gates, and supplementary *continuous real scalar gate-history observations*. It is not a claim about a single fixed input path query, nor about unbounded-precision discontinuous encodings.

## Next step

For a *specified small set* of tagged path queries rather than the full path operator, determine the number of independent gate values actually queried, and construct the minimal streaming residue repair. Specialize to the four-point BRC reachable input family, measuring total arithmetic and output decoding cost. No formal CLAIM/Native Result/independent Driver acceptance is asserted.
