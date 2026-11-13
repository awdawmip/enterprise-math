# PREFIX-606-R2 — Exact identifiability threshold for sampled native X6-BRC gate-prefix operators

**Date:** 2026-11-09 (Asia/Shanghai). **Status:** AUTHOR-SIDE PROOF + EXECUTED EXACT CHECKS; independent mathematical review pending.  
**Frozen science pin:** \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).  
**Dependency:** PREFIX-602, PREFIX-604, PREFIX-605, especially \`3de4cbc240273265424ce0ce26393ec05c52bc02\` (PR #1830).  
**Role:** direct portable TASK_RESEARCH author-side unit; no claim, Result, review or Foundation promotion.

## 1. Original model and observational boundary

The frozen native X6-BRC source has 48 STAR phases, 96 bit ports, 576 tagged actions, six native axes and three original gate-source branches. Restrict the **derived 48-phase linear observer** to axis weights \((1,1,1,1,0,0)\), with any **nonnegative real** gate word \(q=(q_1,\ldots,q_n)\), \(n\ge1\). After an arbitrary shared two-step transient \(Q(a)Q(b)\), \(a,b\ge0\), PREFIX-602 establishes the common rank-16 image \(V\), and PREFIX-604 establishes its fixed \(12+4\) split. On the four-dimensional gate-sensitive factor,
\[
B(q)=\begin{pmatrix}
0&0&0&4(q+3)\\1&0&0&0\\0&1&0&0\\0&0&1&0
\end{pmatrix}.
\]
At every sample time \(t\), the observed data are the **entire linear input-to-full-48-phase-output prefix operator** after the common transient, not one chosen input vector. Since the transient has image \(V\), the 48-phase reconstruction is injective on \(V\), and the four-dimensional summand is complemented, these samples determine the 4D prefix operators and vice versa for comparing two words at fixed sample times; the 12D factor is word-independent. No claim is made about the raw tagged path history or all intermediate readouts.

For \(0\le t\le n\), define
\[
p_r(t)=\prod_{\substack{1\le j\le t\\j\equiv r\pmod4}}(q_j+3),\qquad r\in\{1,2,3,4\},
\]
with residue 4 for multiples of four and empty product 1. Since \(q_j\ge0\), all \(p_r(t)>0\). PREFIX-605 proves that each prefix operator exposes all four \(p_r(t)\) exactly through its nonzero monomial entries, with the known length-dependent powers of four.

## 2. Theorem 606.1 — sharp sparse checkpoint reconstruction

Let a known length-\(n\) word be sampled at prefix times
\[
0=t_0<t_1<\cdots<t_m=n.
\]
The mapping from the **entire** nonnegative gate word to these complete prefix operators is injective on \([0,\infty)^n\) **if and only if**
\[
\boxed{t_\ell-t_{\ell-1}\le4\quad\text{for every }\ell.}
\]

**Sufficiency.** The samples expose the positive cumulative products \(p_r(t_\ell)\). Their exact ratios give
\[
R_{\ell,r}=\frac{p_r(t_\ell)}{p_r(t_{\ell-1})}
=\prod_{\substack{t_{\ell-1}<j\le t_\ell\\j\equiv r\pmod4}}(q_j+3).
\]
When the gap length is at most four, each residue occurs at most once. For the unique index \(j\) in the gap of residue \(r\), recover
\[
\boxed{q_j=R_{\ell,r}-3.}
\]
Empty residue classes give \(R_{\ell,r}=1\); no division by zero occurs. This recovers every gate exactly, including zero gates.

**Necessity.** A gap of length at least five contains positions \(j,j+4\) of the same residue. Fix all gates to 1; replace the gates at these two positions by \(0\) and \(7/3\), respectively. Their old shifted product was \((1+3)^2=16\), whereas the new product is \((0+3)(7/3+3)=16\). All prefix products at the previous sample and at the next sample are unchanged; all later sampled prefix products remain unchanged. The two distinct words therefore yield the same complete native-derived 48-phase sampled endpoint operators. This is a counterexample **inside the nonnegative admissible domain**. QED.

**Optimal number of complete prefix snapshots.** Every length-\(n\) word requires at least \(\lceil n/4\rceil\) such samples, and times \(4,8,\ldots,n\) (omitting duplicates) attain the bound. Here the final time \(n\) is an observed checkpoint; no extra observations outside the declared interval are supplied.

## 3. Theorem 606.2 — exact generic information dimension of an arbitrary sampling schedule

On the interior \((0,\infty)^n\), the real-smooth map from gate words to the sampled full prefix-transfer operators has Jacobian rank exactly
\[
\boxed{\operatorname{rank}D\Phi=\sum_{\ell=1}^{m}\min(4,t_\ell-t_{\ell-1}).}
\]
Its local smooth fiber dimension is
\[
\boxed{\dim\Phi^{-1}(\Phi(q))=n-\operatorname{rank}D\Phi
=\sum_{\ell=1}^m\max(0,t_\ell-t_{\ell-1}-4).}
\]

**Proof.** For each sample, pass from its cumulative products \(p_r(t_\ell)\) to segment ratios \(R_{\ell,r}\); positivity makes this an invertible smooth triangular coordinate change on the observed data. Next take logarithms, \(u_j=\log(q_j+3)\). Each observed segment statistic becomes a sum of \(u_j\) in exactly one segment-residue group. These groups are disjoint, and each nonempty group gives one independent row in the incidence Jacobian. An interval of length \(d\) contributes \(\min(4,d)\) nonempty residue groups, giving the displayed rank. All coordinate changes are smooth with nonzero derivatives on the positive gate domain. The constant-rank theorem gives the fiber dimension. The local families can also be exhibited by varying the log variables within a fixed group while preserving their sum. QED.

On boundary faces \(q_j=0\), the input is not an open manifold; the injectivity theorem remains exact throughout the closed nonnegative orthant. The fiber dimension statement is explicitly for the positive interior, not a blanket smooth-manifold claim about boundary strata.

## 4. Exact counterexample, original-source verification and algorithmic interface

Take \(n=8\), \(q=(0,2,1,5,3,4,7,6)\). The two samples \(t=4,8\) recover **all eight gates** exactly via \(q_j=p_{j\bmod4}(t_\ell)/p_{j\bmod4}(t_{\ell-1})-3\), with the proper residue-class convention. In contrast, checkpoints \(t=5,8\) cannot separate
\[
(1,1,1,1,1,1,1,1)\quad\text{and}\quad(0,1,1,1,7/3,1,1,1).
\]
Their complete 4D sampled prefix operators coincide at both times, whereas the time-1 operators differ. With the shared native two-step transient \(Q(0)Q(1)\), the **full 48×48 native-derived endpoint operators** at times 5 and 8 coincide for the pair; the time-1 native-derived operators do not. The proof remains native-derived rather than a replacement of the native 96-port/576-edge substrate.

Executed self-contained checker: \`PREFIX606_R2_gate_prefix_sampling_checker.py\`, results \`PREFIX606_R2_gate_prefix_sampling_results.json\`. It reconstructs Q from the frozen STAR triads; exhaustively checks the analytic rank formula for **511 nonempty-prefix sampling schedules at n=1..9** (each schedule includes final n), exact recovery for every gap-at-most-four schedule, eight-step 4D transfer identities, and **96 complete native-derived 48-phase basis-column equalities** at the ambiguous checkpoint times. SymPy exact integers/rationals throughout. Finite tests check the checker and explicit witnesses; the general theorem follows from the product formula and algebraic proof.

**Computational opportunity:** four cumulative gate products allow dense prefix checkpoints to encode and *exactly reconstruct* a long gate program using only \(\lceil n/4\rceil\) full-operator observations, versus one checkpoint per step. Evaluating one whole linear operator, its bit cost, two-step initialization and 48/96-port recovery still costs work; this theorem is an information/identifiability result, **not** a measured wall-clock speedup. Sparse single-output sensors are a distinct unresolved inverse problem.

## 5. Next discriminating unit and preservation scope

Compare the 16D positive-realization question from PREFIX-605 with the sharp 4-step sampling threshold: whether a fixed small set of original nonnegative source probes, with specified 48-phase output coordinates, suffices to reconstruct all four gate products at every sample. Seek a minimal probe/readout measurement design or a counterexample, using the exact 16D \(U_4\oplus Z_{12}\) decomposition and preserving full native tagged provenance when requested. Do not promote this phase-linear endpoint result to identity of original branch histories or physical heartbeat trajectories.

**Publication status:** author-side exact proof and computation, independent review pending, no formal Native Result/CLAIM/Working Truth/Foundation promotion asserted.
