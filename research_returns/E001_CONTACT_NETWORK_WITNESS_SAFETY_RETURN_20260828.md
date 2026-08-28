# E001 Contact-Network Witness-Safety Continuation — Research Return

Status: `SUCCESS / EXACT_FUTURE_FACTOR_QUOTIENT_CRITERION_AND_MINIMAL_COUNTEREXAMPLE`

Task: `RS-E001-CONTACT-NETWORK`  
Researcher-ID: `EM-E001-CDA85F`  
Claim: `chatgpt-e001cn-20260828-2325`  
Execution branch: `research/e001-contact-network-witness-safety-em-e001-cda85f`  
Execution base: `c884ff0d83ac6e6455665bfd6e9366dd8107f2c1`  
Predecessor evidence: PR #234 head `a31dc25c90d36b64110d93e5ccf7349c9ca40673`

## Question

PR #234 established the exact delivered-impulse algebra

\[
p' = p + Bj,\qquad r' = r + K j,\qquad K=B^TDB,
\]

and, for positive diagonal \(D\),

\[
\ker K=\ker B,\qquad \dim\ker B=E-V+c.
\]

Thus a cyclic contact graph has contact-impulse directions invisible at body level. The open task is sharper: **when may two allocations with the same \(Bj\) actually be identified for all future E001 behavior?**

## Result 1 — exact future-factor quotient criterion

Let \(J\subseteq\mathbb Z^E\) be the admissible delivered-impulse witnesses and define

\[
j\sim_B j' \iff Bj=Bj'.
\]

Equivalently, \(j'-j\in\ker_{\mathbb Z}B\). Let \(\Sigma(j)\) denote the complete declared future signature after delivery: every future legality answer, persistent-state update and observable that the E001 future language is allowed to inspect.

Then the body-update quotient is future-safe **if and only if**

\[
Bj=Bj' \Longrightarrow \Sigma(j)=\Sigma(j')
\quad\text{for every admissible }j,j'.
\]

Equivalently, \(\Sigma\) factors through the incidence image:

\[
\Sigma=\bar\Sigma\circ B.
\]

This is the weakest possible criterion: weakening it means that some pair identified by \(Bj\) remains distinguishable by an allowed future query, so the quotient is not future-safe.

For the full integer witness lattice the quotient has an exact concrete form:

\[
\mathbb Z^E/\ker_{\mathbb Z}B \cong \operatorname{im}_{\mathbb Z}B.
\]

For an oriented graph with connected components \(C_1,\ldots,C_c\),

\[
\operatorname{im}_{\mathbb Z}B
=
\left\{
q\in\mathbb Z^V:
\sum_{v\in C_\alpha}q_v=0\ \text{for every }\alpha
\right\}.
\]

Proof: every incidence column has zero component-sum, giving one inclusion. Conversely, fix a spanning tree in each component. Integer path columns generate every \(e_v-e_{r_\alpha}\), and those vectors generate the entire componentwise zero-sum lattice. The first isomorphism theorem then gives the displayed quotient.

So the exact quotient coordinate is not a chosen minimum-norm contact allocation. It is the componentwise-zero-sum body increment \(q=Bj\). Choosing a particular contact representative is extra witness policy.

## Result 2 — history-free E001 is safe

Suppose that after a delivered impulse the persistent state retained by the future language is only body state plus fixed data (masses/topology), and every later contact score, guard and observable is recomputed from that retained body state. Then two witnesses with the same \(Bj\) lead to the same \(p'=p+Bj\), hence the same recomputed

\[
r'=B^TDp',
\]

and recursively the same allowed future behavior. Therefore all cycle circulations may be quotiented exactly.

This identifies the positive boundary promised by PR #234: **cycle ambiguity is harmless when the future language is body-factorized.**

## Result 3 — additive persistent contact memory has an exact algebraic test

Let a persistent contact-memory channel take values in an abelian group \(A\) and update additively by a homomorphism

\[
h' = h + Cj,\qquad C:\mathbb Z^E\to A.
\]

If the future language may faithfully inspect this memory, then the body quotient is future-safe exactly when

\[
\ker_{\mathbb Z}B \subseteq \ker C.
\]

Equivalently, \(C\) factors uniquely through \(\operatorname{im}_{\mathbb Z}B\).

Thus a faithful cumulative per-contact impulse register \(C=I_E\) is quotient-safe exactly when \(\ker B=0\), i.e. exactly when the simple contact graph is a forest. On every cyclic graph, at least one nonzero circulation remains visible to the persistent contact state.

This criterion also covers damage/reservoir variables whenever their future-relevant update distinguishes a cycle shift. No generic A2/P023 theorem is re-owned here; this is the E001 incidence specialization.

## Result 4 — minimal persistent-contact counterexample

For simple contact graphs, the smallest cyclic topology is the triangle \(C_3\). Orient its edges cyclically \(0\to1\), \(1\to2\), \(2\to0\):

\[
B=
\begin{pmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{pmatrix}.
\]

Take two nonnegative delivered-impulse witnesses

\[
j=(0,0,0),\qquad j'=(1,1,1).
\]

Then

\[
Bj=Bj'=(0,0,0),
\]

so the body momentum state is identical. But with a faithful per-contact reservoir \(h\leftarrow h+j\), starting from \(h=0\),

\[
h_j=(0,0,0),\qquad h_{j'}=(1,1,1).
\]

A future guard such as “edge 0 can accept one additional unit iff \(h_0<1\)” is true after \(j\) and false after \(j'\). Therefore body equality does not imply future equivalence.

This is minimal among simple graphs: on fewer than three vertices no cycle exists, so \(\ker B=0\).

## Exact regression

`scripts/check_e001_contact_network_witness_safety.py` uses no CAS. It exhausts all labelled simple graphs on \(1\le V\le5\) (1099 graphs) and checks exact rational incidence rank

\[
\operatorname{rank}B=V-c,\qquad
\operatorname{nullity}B=E-V+c.
\]

Results:

- 1099 total graphs;
- 339 forests;
- 760 cyclic graphs;
- first cyclic simple graph: \(V=3,E=3,\beta=1\);
- the cyclically oriented triangle has the nonnegative circulation `(1,1,1)`;
- body-only signatures agree for `j=0` and `j'=(1,1,1)`;
- faithful per-contact reservoir state and an explicit next-step guard distinguish them.

Checker status: `PASS`.

## Boundary / interpretation

The result does **not** say that cyclic contact allocations are physically unique or that a particular representative should be selected. It says exactly when representative choice is semantically irrelevant.

The sharp E001 boundary is:

- **safe**: every future-relevant object factors through \(Bj\);
- **unsafe**: some admissible cycle shift is visible to a future guard, update or observable.

Minimum-norm, minimum-total, lexicographic or other representative selection is therefore not derived physics; it is a witness-selection convention unless an independent E001 law makes the future language invariant under all cycle shifts.

## Return verdict

Hard target achieved at task scope:

`E001_CONTACT_NETWORK_CYCLE_WITNESS_FUTURE_SAFE_QUOTIENT_EXACTLY_CLASSIFIED`

No hard block remains inside this bounded continuation.

Recommended next action: Driver-review this return together with PR #234. If accepted, preserve the factor-through-\(Bj\) condition as the exact E001 quotient boundary and the triangle reservoir construction as the regression guard. Any particular contact-representative selection rule should remain a separate owner/task unless derived from additional material semantics.
