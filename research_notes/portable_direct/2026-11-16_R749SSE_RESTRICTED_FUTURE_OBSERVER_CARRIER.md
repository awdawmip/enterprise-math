# R749SSE — Exact restricted-future observer carrier for joint count-error partitions

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen auxiliary scientific input:** a72226e2430ffa4786321ac86e7f0c599d5f0389. **Scientific predecessor:** R749SSD, immutable commit 6cf5eb12932a9fab620a92a2027b1a8d1b2c2875, [paper](https://github.com/awdawmip/enterprise-math/blob/6cf5eb12932a9fab620a92a2027b1a8d1b2c2875/research_notes/portable_direct/2026-11-16_R749SSD_JOINT_ERROR_PARTITION_LATTICE.md).

## Question and model

The predecessor classified 225 sharp six-phase recovery thresholds with independently partitioned numerator/denominator errors. Here we classify the **observational equivalence of those 25 joint error-correlation types** under a declared restricted future-observation language. This is a different proposition from equality of decoder thresholds.

Use the same five **labeled** positive source weights \(w=(1,1,2,3,6)\), marking the first weight-one source. For integer \(q\ge1\),
\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^{5}:\sum_jw_j k_j\le q-1\},\quad C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
For integer errors \(|e|\le2, |d|\le2\), requiring \(C_q+d>0\), the numerical readout is
\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-q^4H_4(q),
\quad H_4(q)=\frac16+\frac1{2q}-\frac{115}{36q^2}+\frac{115}{6q^3}-\frac{16315}{108q^4}.
\]
At base cutoff \(r\ge6\), use indexed offsets \(h=(0,1,5)\), \(q_i=r+h_i\). Each of the numerator and denominator error vectors is constant on the blocks of its own partition \(\pi_e,\pi_d\) of \(\{0,1,2\}\). For selected future-observation indices \(S\subseteq\{0,1,2\}\), define \(\mathcal O_S(r;\pi_e,\pi_d)\) to be the **set of all jointly possible numerical tuples** \((Y_{q_i}(e_i,d_i))_{i\in S}\), existentially quantifying errors at unobserved indices. The observer knows \(r\), the model, budgets and offsets; the errors themselves remain latent.

## Theorem 1: bounded integer ratio identifiability

For positive integer \(C>K\), nonnegative integer \(T\) and budgets \(M,K\ge0\), the map \((e,d)\mapsto (T+e)/(C+d)\), with integer \(|e|\le M, |d|\le K\), is injective whenever
\[
\boxed{T>2M(C+K).}
\]
Indeed equality for two error pairs implies
\[
T(d'-d)+C(e-e')+ed'-e'd=0.
\]
If \(d'\ne d\), the magnitude of the first term is at least \(T\), but the combined magnitude of the other terms is at most \(2MC+2MK\), a contradiction. Therefore \(d'=d\), and positivity of \(C+d\) forces \(e'=e\). Multiplying by \(q^3>0\) and subtracting the known smooth term preserves injectivity. \(\square\)

## Theorem 2: exact sharp injectivity cutoff for the frozen source weights

For budgets \(M=K=2\), the numerical map \((e,d)\mapsto Y_q(e,d)\) is injective for **every integer \(q\ge6\)**. This cutoff is sharp. At \(q=5\), \(C_5=T_5=25\), so \((e,d)=(-2,-2)\) and \((-1,-1)\) both give ratio 1.

To prove the infinite tail, all source weights divide 6. Uniquely write each source count as \(k_j=(6/w_j)n_j+t_j\), where \(0\le t_j<6/w_j\). There are \(6\cdot6\cdot3\cdot2\cdot1=216\) residue vectors. Their residual weight \(B_t=\sum_j w_jt_j\) satisfies \(0\le B_t\le17\). Conditional on the residue vector, \(\sum_j n_j\le L_t=\lfloor(q-1-B_t)/6\rfloor\). For \(q\ge48\), every \(L_t\ge5\). Stars and bars gives \(\binom{L_t+5}{5}\) possible vectors, and their average first coordinate is \(L_t/6\). Consequently the average marked original count \(k_1=6n_1+t_1\) is \(L_t+t_1\ge5\). Averaging the blocks yields \(T_q\ge5C_q\). Also \(C_q\ge C_{48}=104712>8\), hence
\[
T_q\ge5C_q>4(C_q+2)=2M(C_q+K),
\]
and Theorem 1 applies throughout the infinite tail \(q\ge48\).

For \(6\le q\le47\) the attached Python certificate uses **exact rational arithmetic** to enumerate every legal \((e,d)\) in the \(5\times5\) error square and checks all pairwise collisions, finding none. It also independently verifies the residue-decomposition exact population and marked-count formulas for \(1\le q\le100\). Exact witnesses establish noninjectivity at each \(q=1,2,3,4,5\). Combining the complete finite check with the preceding infinite proof establishes the sharp threshold 6. \(\square\)

## Theorem 3: exact finite-future-language quotient and minimal carrier

For \(r\ge6\), budgets \(M=K=2\), and every \(S\subseteq\{0,1,2\}\),
\[
\boxed{\mathcal O_S(r;\pi_e,\pi_d)=\mathcal O_S(r;\pi'_e,\pi'_d)
\iff \pi_e|_S=\pi'_e|_S\ \text{and}\ \pi_d|_S=\pi'_d|_S.}
\]
Here \(\pi|_S\) means the equality relation on the selected index set. Hence the 25 partition pairs have exactly **1** observational equivalence class at a 0- or 1-index horizon, **4** at any 2-index horizon, and **25** for the complete three-observation language. Under the same coordinatewise-injectivity hypothesis and arbitrary nonnegative budgets \(M,K\), the class count generalizes to
\[
\mathrm{Bell}(|S|)^{\mathbf 1_{M>0}+\mathbf 1_{K>0}},\qquad \mathrm{Bell}(0,1,2,3)=(1,1,2,5).
\]

**Proof.** Every assignment on the blocks of the restricted partitions extends to a full three-coordinate assignment by giving unobserved members the value of their block. For all \(q_i\ge6\), \(C_{q_i}\ge41>2\) makes every denominator assignment positive. Thus the projected error-pair set is determined exactly by the restricted partition pair. Theorem 2 says each selected coordinate map \((e_i,d_i)\mapsto Y_{q_i}\) is injective, so its product map is injective. Equality of numerical image sets is equivalent to equality of the underlying projected error-assignment sets. For an error budget at least 1, two distinct partitions of \(S\) have distinct admissible integer-assignment sets: one can assign 0 and 1 to indices separated by one partition but identified by the other. When a budget is zero its assignment is identically zero, making that partition irrelevant. This gives both the equivalence criterion and the Bell-number class counts. \(\square\)

**Explicit future-operation counterexample.** At \(r=6\), numerator partitions \(\pi_e=012\) (all common) and \(\pi'_e=01|2\) have identical restrictions to the first two observations \(S=\{0,1\}\), regardless of the common denominator partition. Under \(\pi'_e\) take errors \(e=(0,0,1)\) and \(d=(0,0,0)\). The first two readouts coincide with their zero-error counterparts. At the third position \(q_2=11\), \(C_{11}=281, T_{11}=600\), and the readout differs by exactly \(11^3/281=1331/281\). Under \(\pi_e=012\), the two initial exact readouts force the common error to zero (Theorem 2), so no joint third-index reproduction is possible. Therefore the two-observation quotient is safe for the specified horizon but not the full future-observation language.

## Reproducibility, scope, BRC/X6 boundary and next problem

The standard-library program R749SSE_RESTRICTED_OBSERVER_CERT.py uses exact Python integers and Fraction; it checks the 42 finite cutoff values \(q=6,\ldots,47\), all legal error pairs, the independent residue formulas at 100 cutoffs, sharp small-cutoff witnesses and the partition-equivalence class counts. R749SSE_RESTRICTED_OBSERVER_RESULTS.json is the emitted machine-readable evidence. The infinite assertion relies on the exact combinatorial proof above, not extrapolation from finite tests. Mathematical review status remains AUTHOR_EXACT_NOT_REVIEWED.

This model yields a **typed observer-dependent sufficient carrier**: two integer error coordinates, their independently specified joint equality relations, and labeled source readouts. Restricting the allowed future language admits a proved quotient; expanding it may require restoring a discarded joint relation. This implements the project's joint-residual-fidelity discipline inside the declared auxiliary source model. It does not establish a native signed BRC port/branch morphism or equate cutoff phase with Heartbeat World spatial coordinates or physical time.

**Next:** analyze the minimal observable carrier when the base cutoff \(r\) is **not supplied to the observer**, and the effect of bounded measurement noise or additional future shift operators. Test a genuinely typed source-label/branch-preserving mapping from this joint-error carrier to existing BRC port operations.
