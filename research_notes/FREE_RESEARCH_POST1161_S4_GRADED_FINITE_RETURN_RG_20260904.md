# Post-#1161 free research — graded finite-state S4-equivariant first-return RG

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / EXACT FINITE PREDICTIVE TOWER + S4-EQUIVARIANT WEIGHTED RG / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessor: `research_notes/FREE_RESEARCH_POST1161_S4_DIAMOND_MEMORY_BUNDLE_20260904.md`

## 0. Result

The post-#1161 scalar first-return/chord reconstruction admits an exact **finite state at every finite future precision** and an exact graded dynamics between those finite states.

For remaining first-return horizon `h`, define

\[
\boxed{Q_h=\{0,1,\ldots,h,\infty_h\}},
\qquad |Q_h|=h+2,
\]

where `d=0..h` are the exact absolute branch-imbalance states and `infinity_h` is the predictive class containing every `d>h`.

The correct finite dynamics is not an endomap of one fixed `Q_h`. One branch step consumes one unit of future horizon, so the exact operation is graded:

\[
\boxed{T_h:Q_h\longrightarrow \mathbb Q_{\ge0}[Q_{h-1}]}
\qquad(h\ge1),
\]

with two branch weights `1/2,1/2`.

Tensoring with the twelve K4/FCC diamond positions gives

\[
\boxed{X_h=D_{12}\times Q_h,\qquad |X_h|=12(h+2),}
\]

and the graded weighted kernel is exactly `S4`-equivariant.

This closes the dynamical question left by the previous S4 diamond-memory bundle: the scalar AGM return RG is not merely an invariant observer; it has a finite, precision-graded, operation-safe `S4` dynamical realization.

## 1. Infinite counter process

The exact unlabeled branch-memory process is the absorbing first-hit chain on

\[
d\in\mathbb N_0.
\]

For `d>0`, one concrete diamond witness decreases the absolute imbalance and the other increases it, so at positive `d`

\[
\boxed{d\mapsto d-1\text{ or }d+1}
\]

with normalized branch mass `1/2` each.

For first-return verification, `0` is absorbing after the hit. This absorbing state is a verification representation of the observer, not a new primitive cell state.

## 2. Exact finite predictive quotient at horizon h

Define

\[
q_h(d)=
\begin{cases}
d,&d\le h,\\
\infty_h,&d>h.
\end{cases}
\]

The previous Myhill-Nerode result proved that this is the coarsest horizon-`h` quotient for the length-resolved first-return observer.

The far class is safe only when the horizon is lowered together with the dynamics. If `d>h`, then after one branch step

\[
d-1>h-1,\qquad d+1>h-1,
\]

so both successors belong to the single far class `infinity_{h-1}`.

This is why the exact finite dynamics is naturally graded rather than a fixed-horizon self-map.

## 3. Graded weighted kernel

For `h>=1`, define `T_h` by

\[
T_h(0)=\delta_0,
\]

\[
T_h(\infty_h)=\delta_{\infty_{h-1}},
\]

and for `1<=d<=h`,

\[
\boxed{
T_h(d)
=\frac12\delta_{q_{h-1}(d-1)}
+\frac12\delta_{q_{h-1}(d+1)}.
}
\]

Here equal target states are combined by addition of rational mass.

Let `T` denote the full absorbing counter kernel on `N_0`. Then the finite quotient is exact:

\[
\boxed{
(q_{h-1})_*\,T
= T_h\,q_h.
}
\]

Thus the finite process is a genuine operation-safe quotient of the full first-return process at the declared future precision.

The checker verifies this identity on `1872` exact counter/horizon cases through `h=32`.

## 4. Precision projections form a tower

For `0<=k<=h`, define

\[
\pi_{h,k}:Q_h\to Q_k
\]

by retaining `0..k` and sending every larger finite state and `infinity_h` to `infinity_k`.

These projections compose exactly:

\[
\boxed{
\pi_{m,k}\circ\pi_{h,m}=\pi_{h,k}
\qquad(k\le m\le h).
}
\]

More importantly, dynamics commutes with precision loss:

\[
\boxed{
(\pi_{h-1,k-1})_*\circ T_h
= T_k\circ\pi_{h,k}
\qquad(1\le k\le h).
}
\]

This is the exact graded analogue of a composition-safe precision system.

The checker verifies:

- `12496` inter-horizon transition naturality cases;
- `170170` projection-composition cases.

So finite first-return depth is an endogenous predictive precision coordinate, not an ad hoc truncation index.

## 5. S4 skew-product state

Let `D_12` be the twelve unordered FCC/K4 diamond positions from the previous result. `S4` acts transitively on `D_12` and trivially on the scalar counter coordinate.

Define

\[
X_h=D_{12}\times Q_h.
\]

The local first-return excursion remains attached to its transported diamond position during one counter evolution, so the graded kernel is

\[
\mathcal T_h(\Delta,d)
=\sum_{d'}T_h(d,d')\,\delta_{(\Delta,d')}.
\]

For every `g in S4`,

\[
\boxed{
\mathcal T_h\bigl(g\cdot(\Delta,d)\bigr)
=g_*\mathcal T_h(\Delta,d).
}
\]

The checker verifies `14976` exact `S4`/transition commutation cases through horizon `8`.

State count is linear in horizon:

\[
\boxed{|X_h|=12(h+2).}
\]

For `h=0..8` the exact counts are

`24,36,48,60,72,84,96,108,120`.

Thus the exponentially large concrete branch-word history is replaced by a linearly growing finite predictive state tower while preserving the required first-return observer exactly to each finite horizon.

## 6. Recovery of the first-return coefficients from finite kernels

After the initial two concrete first-step witnesses are aggregated to total scalar mass one, the counter starts at `d=1`.

Run the graded kernel for `2N-1` remaining branch steps. The mass first absorbed at zero after `2n-1` further steps is exactly

\[
\boxed{
f_n=\frac{C_{n-1}}{2^{2n-1}}.}
\]

Therefore the finite state tower directly reconstructs

\[
F_N(s)=\sum_{n=1}^N f_n s^{2n}
\]

without a square-root selector or an implicit algebraic solve.

The checker reconstructs the first `32` coefficients. The first eight are

\[
\frac12,
\frac18,
\frac1{16},
\frac5{128},
\frac7{256},
\frac{21}{1024},
\frac{33}{2048},
\frac{429}{32768}.
\]

These agree with the first-balance Catalan formula exactly.

## 7. Finite AGM RG readout

At return depth `N`, use the finite mass polynomial

\[
F_N(s)=\sum_{n=1}^N f_ns^{2n}.
\]

The explicit finite AGM mean/channel readouts are

\[
\boxed{
H_N^+=H\left(1-\frac{F_N(s)}2\right),
\qquad
U_N^+=H\frac{F_N(s)}2,
}
\]

\[
\boxed{
s_N^+=\frac{F_N(s)}{2-F_N(s)},}
\]

\[
\boxed{
a_N^+=\frac H2,
\qquad
b_N^+=\frac H2(1-F_N(s)).}
\]

As `N` increases, these are compatible readouts of an increasingly deep predictive tower. In the completion,

\[
F_N\uparrow F,
\]

and the exact AGM update is recovered.

The already proved tail bound

\[
0<F-F_N\le s^{2N+2}
\]

gives on the standard orbit

\[
0<b_N^+-\sqrt{ab}<2^{-4N-4}.
\]

Thus the graded state tower and the finite mean certificate are two views of the same endogenous return-depth precision.

## 8. Relation to Gen18 full-lift-fiber transparency

Gen18 freezes the rule that, with hidden structural kernel present, checking one chosen `a,b` lift is insufficient; an observer/background is globally transparent only when the full lift fibers over the quotient generators preserve it.

The previous S4 diamond-memory result proves that the scalar counter `|z|` is invariant under every bijection of a two-element witness fiber. Therefore, conditional on structural lifts transporting the retained diamond fiber as a two-element object, every element of the full lift fiber acts transparently on the counter and hence on `Q_h`.

The graded transitions depend only on the scalar counter and equal branch weights. Consequently the entire finite tower `X_h` inherits this section-independence.

This consumes Gen18 but does not duplicate active Gen19, which concerns PF-10/connection moduli and nondegenerate enriched Full-Cell backgrounds.

## 9. Exact semantic strength

The finite `Q_h`/`X_h` states are observer-relative predictive quotients of N1 path memory. Their exactness does not promote them to instantaneous P000/N0 cell state.

Strongest current typing:

\[
\boxed{
\text{framed derived Full-Cell S4 geometry}
\to
\text{N1 branch-memory process}
\to
\text{finite predictive quotients }X_h
\to
\text{N2 first-return/chord/AGM readouts}.}
\]

What is now exact is the finite Markov/predictive dynamics **at every declared future precision**, including transport under the derived `S4` geometry.

The bare-G0 collision and bounded-hidden-fiber no-go results remain unchanged.

## 10. Executable evidence and correction record

Task-local checker:

`scripts/check_free_research_agm_s4_graded_return_rg.py`

Initial checker commit:

`f67a4c76886c9619c1ec25a08e746d6a235c3e9a`.

The initial script's four expected census totals were manually miscounted; the mathematical transition/naturality logic was unchanged. After write-back replay, the frozen golden totals were corrected in commit

`7468197cc0c99f9a6b52b8a3a8c9133e7f3bdbf4`.

Correct replay totals:

- full-counter quotient factorization: `1872`;
- inter-horizon transition naturality: `12496`;
- precision-projection composition: `170170`;
- `S4` equivariance: `14976`;
- first-return coefficients recovered: `32`.

The corrected file was fetched from `main` and the full exact logic was replayed successfully.

## 11. Tool/prior-art boundary

Finite-state predictive quotienting, Markov lumping, graded state systems, and group-equivariant kernels are standard mathematics. Existing Enterprise predictive-quotient and finite-symmetry ideas are reused; no new global tool family is claimed.

The project-specific result is the exact synthesis

\[
\boxed{
\text{FCC/K4 diamond orbit}
\times
\text{minimal horizon first-return quotient}
\to
\text{finite S4-equivariant graded RG}
\to
\text{AGM chord/mean map}.}
\]

## 12. Next independent question

The representational and dynamical ambiguities of the post-#1161 scalar return RG are now closed at the derived finite-predictive level.

A remaining independent precision question, not overlapping active Gen19, is:

> How much first-return depth is actually needed at AGM outer step `n` to retain the quadratic outer convergence and a target certified precision? Equivalently, what is the optimal two-parameter tradeoff between outer AGM depth and inner predictive horizon/state count?

This is a finite-precision/resource theorem, not a native-lift ontology question.
