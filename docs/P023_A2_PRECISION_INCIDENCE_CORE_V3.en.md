# P023 / A2 — Precision Incidence Core v3

Status: `PROVED OWNER DISTILLATION / RESEARCH`  
Owner: A2 future-compatible quotient  
Source pressure: P011/P018/P023/P024 and P017  
Frozen source: `research/p023-precision-incidence-scheduling@646530c3acd69332efe0fb937258cec888713688`

This document replaces a proliferating chain of application-first supplements with one owner-level finite theorem surface. The underlying mathematics—finite partitions, equivalence relations, bipartite incidence graphs, binomial inversion, and directed metric ideas—is established prior mathematics. Enterprise Math's value here is the exact repair interface and the cross-route synthesis.

## 1. Precision states are finite partitions

Let `X` be a finite nonempty state set. A precision/task state is an equivalence relation `E` on `X`, or equivalently a partition `X/E`.

Adding another task `F` retains the common refinement

\[
E\cap F.
\]

The realized joint states are not the formal Cartesian product. They are exactly the nonempty block intersections

\[
\Gamma(E,F)=\{(B,C)\in X/E\times X/F:B\cap C\ne\varnothing\}.
\]

Hence

\[
\boxed{|X/(E\cap F)|=|\Gamma(E,F)|.}
\]

The defect `|X/E| |X/F|-|Gamma(E,F)|` counts formal product labels that are never realized by an actual state.

## 2. Minimum repair is maximum local split degree

Assume `E` is already retained and task `F` is added. For each `E` block `B`, let

\[
s_B=\#\{C\in X/F:B\cap C\ne\varnothing\}.
\]

Then the exact minimum alphabet of any repair coordinate that upgrades `E` to `E cap F` is

\[
\boxed{\rho(E,F)=\max_{B\in X/E}s_B.}
\]

Necessity is pigeonhole inside the worst coarse block. Sufficiency follows by numbering the realized `F` subblocks locally and reusing the same repair alphabet across different `E` blocks.

Thus a one-bit repair is not a special phenomenon:

\[
\boxed{\text{binary repair is sufficient iff }\rho(E,F)\le2.}
\]

The crossing bit, carry bit, shell-label repair, and material/event repair examples are specializations of this local split law.

## 3. Full relative repair spectrum

The worst local alphabet is only the top statistic. Define

\[
\boxed{\mathcal R_k(E,F)=\sum_{B\in X/E}\binom{s_B}{k}.}
\]

This is exactly the P011 collision spectrum of the canonical quotient projection `X/(E cap F) -> X/E`.

Consequences:

- `R_1(E,F)=|X/(E cap F)|`;
- `R_2` counts pairs of newly distinguished joint classes that had shared one old `E` block;
- the full finite spectrum recovers the distribution of local repair sizes by binomial inversion;
- if every local split is binary, then

\[
\boxed{\#\{B:s_B=2\}=\mathcal R_2(E,F)=|X/(E\cap F)|-|X/E|.}
\]

This separates local repair width `rho` from global active repair support and from higher-order repair mass.

## 4. Incidence geometry

The pairwise incidence graph gives a directed repair factor `rho(E,F)`. For any third precision relation `G`,

\[
\boxed{\rho(E,G)\le\rho(E,F)\rho(F,G).}
\]

Proof: one `E` block meets at most `rho(E,F)` intermediate `F` blocks, and each such block meets at most `rho(F,G)` `G` blocks.

For an integer alphabet base `b>=2`, define

\[
L_b(n)=\min\{\ell:n\le b^\ell\},\qquad d_b(E,F)=L_b(\rho(E,F)).
\]

Then

\[
\boxed{d_b(E,G)\le d_b(E,F)+d_b(F,G).}
\]

Moreover `d_b(E,F)=0 iff E subseteq F`. The symmetrization

\[
\boxed{D_b(E,F)=d_b(E,F)+d_b(F,E)}
\]

is an integer metric on finite precision relations over the fixed state set.

This is an intrinsic geometry of task translation cost, not physical-space geometry.

## 5. Higher-order incidence cannot be reconstructed pairwise

For three or more task partitions, define the realized incidence hypergraph

\[
\Gamma(E_1,\dots,E_m)=\{(B_1,\dots,B_m):B_1\cap\cdots\cap B_m\ne\varnothing\}.
\]

Then

\[
\boxed{|X/(\cap_iE_i)|=|\Gamma(E_1,\dots,E_m)|.}
\]

Pairwise weighted incidence is insufficient.

Explicit eight-state counterexample: System A realizes the four even-parity binary triples `000,011,101,110`, each twice. System B realizes all eight binary triples once. Every single partition has the same block sizes and every weighted pairwise incidence table is identical, yet the joint class counts are `4` and `8` respectively. In A, after two tasks the third is free, while in B its conditional repair factor is `2`.

Therefore

\[
\boxed{\text{pairwise precision geometry does not determine joint precision}.}
\]

## 6. Context monotonicity

Let `C'` refine retained context `C`. For the same new task `F`,

\[
\boxed{\rho(C',F)\le\rho(C,F).}
\]

More retained context cannot increase the minimum alphabet needed to add one unchanged task. This is a deterministic finite-partition theorem, not an entropy or probability statement.

## 7. Realizability and observation monotonicity

More generally, let a finite incidence relation `R subseteq I x X` encode which fine states are actually admissible under label `i`, and let `g:X->Y` be the retained observation. The local label burden at `y` is

\[
m_{R,g}(y)=|\{i:\exists x,\ (i,x)\in R,\ g(x)=y\}|.
\]

The minimum repair alphabet for recovering the label is

\[
\boxed{M(R,g)=\max_y m_{R,g}(y).}
\]

Two monotonicities follow immediately: relation enlargement cannot lower `M`, and observation coarsening cannot lower `M`. Image separation is exactly the endpoint `M=1`.

This is the owner-level statement behind the project rule that candidate supersets can manufacture false collisions.

## 8. Boundaries

This core does not claim that every precision question is finite; that pairwise metrics replace higher-order task structure; that task-relative predictive sufficiency changes physical ontology; that an informative feature is automatically a necessary repair; or that formal Cartesian task products are realized.

The correct object is always the realized partition/incidence structure for the declared task language.

## 9. Executable specification

Owner-local modules:

- `src/enterprise_math/a2_precision_incidence.py`
- `tests/test_a2_precision_incidence.py`

The executable regression checks exact realized tuple counts, repair-spectrum inversion, the binary active-support identity, the pairwise-shadow no-go example, all 3375 triples of the 15 partitions of a four-state set for the multiplicative/additive triangle laws, and the symmetrized metric triangle.

Finite enumeration is regression and counterexample reconstruction, not the proof of the ordinary finite statements above.
