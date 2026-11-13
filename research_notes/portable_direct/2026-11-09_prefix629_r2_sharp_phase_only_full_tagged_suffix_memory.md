# PREFIX-629 R2: exact one-register cost of phase-only native BRC suffix history

**2026-11-09 (Asia/Shanghai).** Author-side research. Researcher **EM-X6-A33F09**, activity **RA-4C18FD5D23A7EE394FE8D3DD**, mother task **RS-X6-NATIVE-ROTATION-DYNAMICS**. Scientific inputs frozen at **awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d**. Source-native P000 V5, ACTIVE Heartbeat/X6 and joint-relation preservation retained. This result remains UNREVIEWED.

## Precise question and theorem

Use the original four-point probe \(d=e_4+e_{11}+e_{14}+e_{32}\), positive input strength \(\lambda>0\), and nonnegative gates \(g_1,\ldots,g_n\ge0\). Every step uses the **original native 96-port/576 source/action-labelled BRC operator** \(A(g)\), on its 48 original STAR phases, without substituting an untyped propagator.

Let \(r_j=A(g_j)\cdots A(g_1)E(\lambda d)\). The terminal observer knows **only the exact 48 native phase sums** \(v_n=\operatorname{phase}(r_n)\), not the terminal 96 ports. It must reproduce **all original ordered, source-port/action-labelled length-\(L\) suffix path masses** starting from the actual predecessor \(r_t\), \(t=n-L\). Each path output includes exact original source port, sequence of labelled steps and final port; path mass is its true predecessor source mass times its \(L\) typed edge weights. It may additionally maintain \(m\) continuously updated real scalar registers.

**THEOREM.** For integers \(L\ge1\), \(n\ge L+4\) and the full nonnegative parameter domain, the sharp supplementary register requirement is
\[
\boxed{m_{\rm phase}(n,L)=
\begin{cases}
L,&t=n-L=4,\\
L+1,&t=n-L\ge5.
\end{cases}}
\]
The original **full-96-port** terminal-observer result in PREFIX-628 R2 has \(m_{\rm port}=L-1\) at \(t=4\) and \(m_{\rm port}=L\) for \(t\ge5\); hence terminal phase aggregation costs **exactly one additional continuous real register** for this complete labelled suffix observer.

This is a claim about the declared continuous-register class and actual original source-labelled path tensor; it does not count the 48 given terminal observer coordinates as supplementary registers or claim fixed-bit storage.

## Native formulas used

The already-derived original four-point native BRC phase factorization (PREFIX-617/622/626/628) recovers five quantities **exactly from \(v_n\)** whenever \(n\ge5\):
\[
\lambda,\quad \Pi_r(n)=
\prod_{\substack{1\le k\le n\\k\bmod4=r}}(g_k+3),
\quad r=0,1,2,3.
\]
In particular, gate-free phase positions \((2,28,38,16)\) determine \(\lambda\) at the known time, while the four B-phase positions \((14,40,26,4)\), their fixed scale factors and modulo-four positions determine the four products. The code gives their complete explicit rational readout, including the powers of \(2\) and \(4\). Every divisor is positive, even for zero gates.

For the original reachable four-point family and \(t\ge5\), the **full original 96-port predecessor** \(r_t\) is determined by exactly the six-tuple \((\lambda,\Pi_0(t),\ldots,\Pi_3(t),g_t)\). At \(t=4\) every residue product has one gate, so the four products alone determine \(g_1,\ldots,g_4\) and thus \(r_4\). In the original full-port terminal observer, an additional port split can recover \(g_n\); the terminal phase sums no longer carry that split.

Relevant path interfaces: each of the 64 live original source ports has a gate-independent weight-one labelled continuation of every positive finite length; source ports 28 and 29 are live. The original typed gated edge \(9\to29\) has scalar coefficient \(g_k\) at step \(k\), and a positive source-prefix and gate-free suffix exist at the needed stages. These are exact statements about the frozen 576-action graph, reused from PREFIX-625 and PREFIX-628.

## Constructive upper bound

Maintain the true native dynamics and a rolling gate buffer. At query time, put \(t=n-L\).
* If \(t=4\), retain \(g_5,\ldots,g_n\) in precisely **\(L\)** registers.
* If \(t\ge5\), retain \(g_t,\ldots,g_n\) in precisely **\(L+1\)** registers.

Read \(\lambda\) and \(\Pi_r(n)\) from the 48 given phase sums. Remove the known suffix factors:
\[
\Pi_r(t)=\frac{\Pi_r(n)}
{\prod_{t<k\le n,\ k\bmod4=r}(g_k+3)}.
\]

At \(t=4\), solve each \(g_i=\Pi_{i\bmod4}(4)-3\), and run the original native operator four times to obtain the exact \(r_4\).

At \(t\ge5\), construct a nonnegative **synthetic prefix** \(h_1,\ldots,h_t\): initialize all \(h_j=0\), set \(h_t=g_t\), and in each modulo-four residue class choose its distinct early index \(i(r)\in\{1,2,3,4\}\). Set
\[
h_{i(r)}
=\frac{\Pi_r(t)}
{\prod_{1\le j\le t,\ j\bmod4=r,\ j\ne i(r)}(h_j+3)}-3.
\]
Every \(h_{i(r)}\ge0\): all original unsaved gate-plus-three factors are at least 3 and any nonzero denominator factor is the *correct saved terminal prefix gate* \(g_t+3\). The synthetic prefix has exactly the four true products \(\Pi_r(t)\) and the same last prefix gate \(h_t=g_t\). The original native exact fiber identity gives
\[
A(h_t)\cdots A(h_1)E(\lambda d)=r_t.
\]
Finally, enumerate every requested original source/action/port-labelled path of length \(L\) starting at this exact predecessor, multiplying the original typed weights using the known true suffix gates. This recovers all path masses, including zero-gate boundaries, at the claimed register count. The direct synthetic-prefix realization requires \(O(n)\) scalar-action update stages plus the output-size work; the rank-16 inverse of PREFIX-628 provides a separate \(O(L)\) predecessor-pullback route after reconstructing a compatible full terminal port realization. Exact bit growth and the explicit output cardinality are separate engineering resources.

## Sharp lower bound

Restrict the parameter domain to a neighborhood of any **strictly positive** gate history, and keep \(\lambda\) fixed. For \(t\ge5\), vary \(g_t,\ldots,g_n\) freely and independently (an \(L+1\)-dimensional open parameter family). For every early index \(i\in\{1,2,3,4\}\), define
\[
g_i'+3=(g_i+3)
\prod_{\substack{t\le k\le n\\k\bmod4=i\bmod4}}
\frac{g_k+3}{g_k'+3}.
\]
The four adjusted early gates stay positive for sufficiently small variations. These adjustments hold all four \(\Pi_r(n)\) fixed, so the **entire 48-phase terminal observation \(v_n\)** is constant on the resulting open \((L+1)\)-parameter family.

For \(t=4\), instead vary \(g_5,\ldots,g_n\) and compensate \(g_1,\ldots,g_4\); this yields a constant-phase open \(L\)-parameter family.

The *complete original labelled suffix path tensor* distinguishes all points of either family. Gate-independent weight-one paths reveal the actual values of **all live precursor source ports** from \(r_t\). For \(t\ge5\), in particular they reveal both ports at phases 2, 3, 14 and 15; setting
\[
\delta_t=r_t[29]-r_t[28],\qquad
\ell_t=v_t[3]+v_t[14]+v_t[15]-2v_t[2]>0
\]
gives the existing native port decoder
\[
g_t=\frac{\ell_t+9\delta_t}{\ell_t-3\delta_t},
\qquad \ell_t-3\delta_t>0.
\]
Once the source port state and preceding suffix gates are known, the gated native edge \(9\to29\), reached through a positive labelled prefix and followed by a positive gate-free continuation, reveals each successive \(g_{t+1},\ldots,g_n\) by an exact labelled path ratio. This determines every free gate; the labelled tensor is injective on the constant-phase fiber. At \(t=4\), the same successive-edge extraction recovers all \(L\) free tail gates. Thus any continuous \(m\)-register map universally recovering the tensor must be injective on an open subset of \(\mathbb R^{L+1}\) or \(\mathbb R^L\), respectively. **Invariance of domain** forces \(m\ge L+1\) or \(m\ge L\). Both bounds match the constructive algorithm.

This topological lower bound targets continuous real registers; no claim is made here about discontinuous encodings or finite-bit machine models.

## Exact original-action counterexample

Set \(\lambda=3/2\), \(n=6\), \(L=1\), with gate sequences
\[
A=(1,1,1,1,1,1),\qquad
B=(1,9/13,1,1,1,4/3).
\]
These have **identical full 48-phase terminal vectors**, since the changed second gate compensates the changed sixth gate in the same residue class. Their original labelled one-step suffix tensors differ: the labelled path from original source port 8 to port 6 has weight **24** for \(A\) and **\(288/13\)** for \(B\). The executable checker also constructs exact different-suffix same-phase collisions at \((n,L)=(5,1)\) and \((10,3)\). The witnesses preserve the original nonnegative gates and source/action labels.

## Executed checks, provenance and open unit

The independent standalone **PREFIX629_phase_only_suffix_checker.py** reconstructs all 48 STAR phases, all 96 original ports and **576 actual original labelled actions** from the frozen source semantics and uses exact Python Fraction arithmetic. Executed result: **ALL_ASSERTIONS_PASS**, **40** rational histories, **9,921** nonzero labelled suffix path coordinate comparisons, **4** phase-identical/source-history-distinct witnesses, including **4** cases at \(t=4\). Original input horizons: \(n\in\{5,6,7,8,9,10,11,12\}\), \(L\le4\). The complete actual inputs, synthetic prefixes, counts and witnesses are in the accompanying JSON. Cross-comparison against the original published PREFIX-626 checker independently matched all **576** typed action arcs, **4** arbitrary-port exact transitions and **10** terminal phase decoder experiments. The universal theorem depends on the exact previously identified native factorization and full-labelled-source-separation lemmas; finite checks confirm the new implementation.

Previous exact results reused at original scope: PREFIX-625 (rank-16 original native path transition), PREFIX-626 (mod-four products), PREFIX-627 (selected-path finite lag), PREFIX-628 R2 (full-labelled suffix sharp memory and rank-16 inverse; Draft PR #1883). All remain author-side and independently unreviewed. The wider physical X6 rotation dynamics mother target remains open.

**Next discriminating unit:** compare native phase-only (i) synthetic-prefix replay and (ii) reconstruction of terminal ports from \(v_n,g_n\) followed by exact rank-16 backwards suffix pullback. Run actual Fraction benchmarks at fixed \(L\) and growing \(n\), including input/preprocessing, numerator/denominator bit lengths, actual original action counts, full labelled-output size and verification. Separately explore minimum information in finite-bit and approximate observers.

**Status:** AUTHOR_SIDE_EXACT_DERIVATION_AND_ORIGINAL_BRC_CHECKS / UNREVIEWED / no formal CLAIM, Native Result or Driver mathematical acceptance.