# Causal Graded Operation Geometry — One Primitive Law Generates Transport and Future Precision

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCE`

Ownership note: P012 should consume the transport bridge; P023/A2 the future-equivalence quotient; P011 the revelation spectrum; P018 only after an explicit bridge to its block-precision calculus. A3 keeps the finite weighted compiler.

## 1. Primitive data

Take:

- a finite raw state set `X`;
- causal operation generators `G`;
- a positive integer grade/cost for every primitive generator,
  \[
  c:G\to\mathbb N_{>0};
  \]
- a current discrete observation,
  \[
  O:X\to Y.
  \]

For a finite operation word

\[
w=g_1g_2\cdots g_m,
\]

define

\[
\boxed{|w|_c=\sum_{i=1}^{m}c(g_i).}
\]

The empty word has cost zero.

Positive primitive costs are part of the present finite-budget discipline. A repeatable zero-cost generator could require unbounded closure already at budget zero and therefore needs a different definition.

## 2. GG-01 — Transport cost

Define

\[
\boxed{
d_{move}(x,y)=\min\{|w|_c:w(x)=y\}.}
\]

Use infinity when `y` is unreachable from `x`.

This is a graded/directed extension of the P012 primitive-operation path distance. If the generator language is irreversible, `d_move` is generally a directed reachability cost rather than a metric. A symmetric shortest-path metric appears only after reverse primitive operations and symmetric reverse costs are justified.

## 3. GG-02 — Future distinguishing cost

Define

\[
\boxed{
d_{sep}(x,y)=\min\{|w|_c:O(w(x))\ne O(w(y))\}.}
\]

If no finite future distinguishes the two states, set

\[
d_{sep}(x,y)=\infty.
\]

This is not an ordinary metric: `d_sep(x,x)=infinity`, not zero. Larger values mean that a deeper or more expensive causal future is required before the states can be separated. It is therefore an agreement depth / distinguishing cost.

## 4. GG-03 — Finite-budget future quotient

For integer budget `R>=0`, define

\[
\boxed{x\equiv_R y\iff d_{sep}(x,y)>R.}
\]

Equivalently, every future word of total cost at most `R` gives the same observation.

The partitions are nested:

\[
\boxed{E_0\succeq E_1\succeq E_2\succeq\cdots.}
\]

An exact finite recurrence is

\[
P_0=\ker O,
\]

\[
\boxed{
P_R(x)=
\left(
O(x),
P_{R-1}(x),
\bigl(P_{R-c(g)}(g(x))\bigr)_{c(g)\le R}
\right).
}
\]

Executable assets:

- `causal_weighted_future.py`
- `tests/test_causal_weighted_future.py`

## 5. GG-04 — Strong agreement law

For all states,

\[
\boxed{
d_{sep}(x,z)\ge\min\{d_{sep}(x,y),d_{sep}(y,z)\}.}
\]

If a word of cost `r` separates `x,z` while `r` is smaller than both other separation depths, the same word would have to satisfy

\[
O(w(x))=O(w(y))=O(w(z)),
\]

which is impossible. Thus the nested future partitions generate an ultrametric-like agreement structure. A traditional real ultrametric requires an additional monotone numerical recoding and is not primitive here.

## 6. GG-05 — Ultimate quotient versus cost regrading

As long as all primitive generators keep positive integer costs and the operation set `G` is unchanged,

\[
\boxed{E_\infty=E_G}
\]

depends only on which finite operation words exist, not on their positive integer grades. Costs determine when a distinction becomes visible, not whether it is ultimately visible.

If

\[
c'(g)\ge c(g)\quad\forall g,
\]

then at the same budget

\[
\boxed{E_R^c\preceq E_R^{c'},}
\]

and

\[
\boxed{d_{move}^{c'}\ge d_{move}^{c},\qquad d_{sep}^{c'}\ge d_{sep}^{c}.}
\]

For uniform integer rescaling

\[
c'=mc,\qquad m\in\mathbb N_{>0},
\]

one has exactly

\[
\boxed{d'_{move}=m d_{move},\qquad d'_{sep}=m d_{sep},}
\]

and

\[
\boxed{E_R^{c'}=E_{\lfloor R/m\rfloor}^{c}.}
\]

Thus the integer cost unit can be regraded; its numeric value alone must not be identified with physical spatial distance.

Executable assets:

- `causal_cost_regrading.py`
- `tests/test_causal_cost_regrading.py`

## 7. GG-06 — Operation cost is a precision-layer transport degree

If generator `g` has cost `c`, then

\[
\boxed{xE_{R+c}y\Longrightarrow g(x)E_Rg(y).}
\]

Indeed, if `g(x),g(y)` were separated by a future word of cost at most `R`, appending that probe after `g` would separate `x,y` within cost `R+c`.

Therefore `g` induces a canonical map

\[
\boxed{\bar g_R:X/E_{R+c}\to X/E_R.}
\]

For a word `w` of total cost `C`,

\[
\boxed{\bar w_R:X/E_{R+C}\to X/E_R.}
\]

If `u` is followed by `v`, with costs `C_u,C_v`, then

\[
\boxed{
\overline{v\circ u}_R
=
\bar v_R\circ\bar u_{R+C_v}.
}
\]

Exact addition of operation cost matches exact composition of quotient maps.

Executable assets:

- `causal_graded_precision_transport.py`
- `tests/test_causal_graded_precision_transport.py`

## 8. GG-07 — Agreement-depth loss bound

The previous theorem yields

\[
\boxed{d_{sep}(g(x),g(y))\ge d_{sep}(x,y)-c(g).}
\]

If the original depth is infinite, the image pair remains permanently future-equivalent. For a word `w`,

\[
\boxed{d_{sep}(w(x),w(y))\ge d_{sep}(x,y)-|w|_c.}
\]

This is generated by future-budget composition rather than imported from a traditional error-propagation formula.

## 9. GG-08 — P011 precision revelation spectrum

For budget partition `E_R`, define

\[
\boxed{J_k(R)=\sum_{C\in X/E_R}\binom{|C|}{k}.}
\]

For `k>=2`, `J_k(R)` cannot increase as the budget grows. Define

\[
\boxed{\Lambda_k(R)=J_k(R-1)-J_k(R),\qquad R\ge1.}
\]

This counts `k`-subsets that remain entirely future-indistinguishable through budget `R-1` but are first split at budget `R`.

In particular,

\[
\boxed{\Lambda_2(R)=\#\{\{x,y\}:d_{sep}(x,y)=R\}.}
\]

And

\[
\boxed{\sum_{R=1}^{B}\Lambda_k(R)=J_k(0)-J_k(B).}
\]

So the P011 collision spectrum can also record the exact integer budget at which hidden distinctions are revealed.

Executable assets:

- `causal_revelation_spectrum.py`
- `tests/test_causal_revelation_spectrum.py`

## 10. Bridge to P012

P012 already treats primitive adjacency/operation as geometric data and shortest primitive walks as intrinsic integer distance. The graded form is

\[
(G,c)\to d_{move}.
\]

The same `(G,c)` combined with observation `O` produces

\[
(G,c,O)\to(E_R,d_{sep},\Lambda_k).
\]

Thus the current relationship between transport geometry and distinguishability geometry should be upgraded from `COMPOSABLE_INDEPENDENT` to

\[
\boxed{\text{COMMON_CAUSAL_SOURCE / NOT_IDENTIFIED}.}
\]

They share a primitive operation/cost layer, but are generally different shadows.

## 11. Prior-art boundary

Weighted transition systems, weighted automata, bisimulation metrics, behavioral distances, shortest weighted paths, partition refinement, and ultrametric-like nested-equivalence representations are established research areas. The project does not claim those general mathematical objects as novel.

The project-level claim requiring review is their placement in the Enterprise Math ontology:

\[
\boxed{
\text{primitive causal operations}
+\text{integer grade}
+\text{future observation}
\to
\text{transport}
+\text{precision tower}
+\text{revelation spectrum}
+\text{cross-layer operation transport}.
}
\]

## 12. Current boundary

Still open:

- infinite-state graded compilers;
- physical derivation of primitive cost rather than declared cost;
- typed separation among locality, energy, latency, and other grade semantics;
- stochastic/quantum channels;
- a strict two-scale bridge between P018 block precision and future-budget precision;
- Lean formalization;
- clean-integration CI.
