# Causal Dimension–Collapse Core — Hidden Motion, Growth Order, and P008 Basin Lowering

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT INTEGER BRIDGE THEOREMS + EXECUTABLE REFERENCES`

Ownership: bridge among A3/A5/P008/P012/P019. The P008 order-adjoint mother theorem and geometry-specific ownership remain separate. This note does **not** define physical dimension as polynomial degree; it proves regimes in which several independently generated integer witnesses coincide.

## 1. Fixed-total LEGO fiber and hidden motion

For `m` integer slots, retain only total

\[
T(x)=\sum_i x_i.
\]

Differences between any two fine states with the same total lie in

\[
\boxed{K_m=\{\eta\in\mathbb Z^m:\sum_i\eta_i=0\}.}
\]

The explicit basis

\[
e_1-e_m,\ldots,e_{m-1}-e_m
\]

shows

\[
\boxed{\operatorname{rank}K_m=m-1.}
\]

For nonnegative allocations, the finite same-total fiber has multiplicity

\[
H_m(c)=\binom{c+m-1}{m-1}.
\]

## 2. DC-01 — Hidden-motion rank equals fiber-growth difference degree

Exact finite difference gives

\[
\boxed{\Delta H_m(c)=H_{m-1}(c+1)}
\]

and therefore

\[
\Delta^rH_m(c)=H_{m-r}(c+r),
\]

\[
\Delta^{m-1}H_m=1,
\qquad
\Delta^mH_m=0.
\]

Hence

\[
\boxed{\operatorname{rank}K_m=\deg_\Delta H_m=m-1.}
\]

Both numbers come directly from the same coarse-total collapse; Ehrhart theory is a traditional comparison tool, not required for this derivation.

## 3. DC-02 — Block redistribution decomposition

Partition `m=sum_i m_i` fine slots into `k` coarse blocks. If every block total remains visible, internal hidden rank is

\[
\sum_i(m_i-1)=m-k.
\]

If only the grand total remains, the `k` block totals themselves acquire a zero-sum redistribution lattice of rank

\[
\boxed{k-1.}
\]

Thus

\[
\boxed{(m-k)+(k-1)=m-1.}
\]

At the set level,

\[
\boxed{
\mathcal F_m(c)
\cong
\bigsqcup_{c_1+\cdots+c_k=c}
\prod_i\mathcal F_{m_i}(c_i).
}
\]

The outer block-total allocation fiber carries the `k-1` cross-block freedoms; the inner factors carry the internal freedoms. Joining two blocks and forgetting their separate totals creates exactly one new cross-block redistribution freedom.

## 4. DC-03 — Three-way agreement in the free A_p regime

The zero-sum integer representation of `A_p` uses `p+1` slots, so hidden motion rank is `p`. The same free-slot fiber multiplicity `H_(p+1)` has difference degree `p`. The existing exact `A_p` graph-ball cardinality is also an integer-valued polynomial of degree `p`.

Therefore in this explicit working regime

\[
\boxed{
\text{hidden relation rank}
=
\text{fiber-growth degree}
=
\text{graph-ball growth degree}
=p.
}
\]

This is a **dimension agreement certificate**, not a definition by fiat.

## 5. Task continuation complexity is separate

A future task has its own minimum continuation-state capacity `C(d)`. Its growth order may differ from substrate relation dimension.

- parity: `C(d)=2`, order 0;
- binary sum: `C(d)=d+1`, order 1;
- binary copy/history at the midpoint: `C(d)=2^d`, no fixed finite polynomial order.

Thus task/state-growth dimension, relation dimension, and physical/geometric dimension are not automatically identical.

For independent tasks whose exact capacities are nonzero-leading integer polynomials, signature-product independence gives capacity multiplication, so their growth degrees add. Degree additivity is therefore a shadow of independent future-state multiplication.

## 6. DC-04 — Causally generated complete growth returns to P008

Let a causal LEGO construction generate a strictly increasing integer complete-growth law

\[
V(k).
\]

P008 gives the right-adjoint root

\[
\boxed{R_V(n)=\max\{k:V(k)\le n\}}
\]

and idempotent downward collapse

\[
\boxed{C_V(n)=V(R_V(n)).}
\]

Hence the causal route does not create a second project foundation:

\[
\boxed{
\text{one-slot causal law}
\to\text{complete integer growth }V
\to\text{P008 root}
\to\text{collapse}.
}
\]

## 7. DC-05 — P008 basin width is the first lowering difference

The k-th root basin is

\[
V(k)\le n<V(k+1)
\]

with exact width

\[
\boxed{|B_k|=V(k+1)-V(k)=\Delta V(k).}
\]

If complete growth has exact polynomial degree `p`, the basin-width growth has degree `p-1`.

For free LEGO allocation this strengthens to exact same-family lowering:

\[
\boxed{H_m(c+1)-H_m(c)=H_{m-1}(c+1).}
\]

The entire basin width is literally a complete lower-rank LEGO fiber cardinality.

For `A_p` graph balls,

\[
|B_r|-|B_{r-1}|=|S_r|
\]

and shell growth has degree `p-1`.

## 8. State boundary versus relation boundary

Different finite observations of the same hole/ball need not define the same surface.

Counting newly added states gives the ordinary shell and only guarantees degree lowering. Counting directed primitive relations cut by an `A_p` ball gives the stronger exact identity

\[
\boxed{E_{p,\alpha}(r)=|B_{p-1}(r)|}
\]

for each directed primitive root `alpha`, hence

\[
\boxed{E_p(r)=p(p+1)|B_{p-1}(r)|.}
\]

Thus the relation boundary literally reproduces the lower-dimensional ball family while the state shell generally does not. “Surface” is observation-language dependent.

## 9. Important negative boundary: degree lowering is not family lowering

The free allocation family is specially closed under finite difference. A generic geometric complete-growth sequence only guarantees one lower **growth degree**; it need not become the lower-dimensional member of the same geometric family. Exact family lowering requires an additional bijection/recurrence theorem.

## 10. DC-06 — Plateau levels must be causally quotiented before root recovery

If a monotone complete observable has a plateau `V(k)=V(k+1)`, it has already erased the distinction between those raw levels. Either future language still distinguishes them, in which case `V` is an insufficient state and must be refined, or future also identifies them, in which case plateau levels should first be quotiented into one causal level. The induced class-capacity sequence is strictly increasing and is the correct P008 order embedding.

A root must never reconstruct distinctions its observation has erased.

Free one-slot configuration count `H_1(c)=1` for all `c` is the minimal example: structure count cannot recover value total. Again,

\[
\boxed{\text{value}\ne\text{structure count}.}
\]

## 11. Variable-basin precision and composition safety

Every strict growth law gives exact basin state

\[
n=V(k)+\delta,
\qquad
0\le\delta<V(k+1)-V(k).
\]

The current basin width is the native detail capacity. Linear `V(k)=dk` recovers fixed P018-like scale; square, LEGO-allocation and `A_p` ball growth produce state-dependent detail capacity.

If intermediate composition immediately erases detail, algebraic path dependence can be manufactured. For square growth, the complete-level operation

\[
a\star b=\lfloor\sqrt{a^2+b^2}\rfloor
\]

is not associative: `(3 star 4) star 4 = 6` while `3 star (4 star 4)=5`. Retaining basin detail restores exact associative amount addition.

Even linear block growth only passes the weaker complete-representative associativity gate; quotient-only floor classes are not addition-congruent on basin members unless future increments are whole-block aligned.

## 12. Unbounded basin obstruction and periodic positive case

For any fixed positive additive increment `t`, if some basin width exceeds `t`, two states in that basin are separated after `+t`. Therefore unbounded basin widths imply that **no fixed positive additive translation is globally future-safe on the level-only quotient**.

Any positive-growth polynomial of degree at least two has unbounded first difference, so detail is globally unavoidable for positive additive dynamics at the level-only quotient.

By contrast, if basin widths are periodic with period `p`, then the total capacity of one period

\[
T=\sum_{j=0}^{p-1}w_j
\]

satisfies `V(k+p)=V(k)+T`, hence `+T` descends exactly to the quotient and preserves basin detail. Constant-width P018 blocks are the period-one special case.

## 13. Relation to early “thickness / rebound layer” intuition

The P008 basin width `Delta V(k)` is the exact integer thickness of amounts collapsing to one complete state before the next complete level. In free LEGO growth, that thickness is itself a lower-rank fiber. This supplies a mathematical mother structure for earlier rebound/thickness intuition, but does not by itself derive physical material force or restitution dynamics.

## 14. Executable assets

- `causal_hidden_motion.py`
- `causal_block_redistribution.py`
- `causal_dimension_agreement.py`
- `causal_completion_collapse.py`
- `causal_basin_dimension.py`
- `causal_basin_state.py`
- `causal_basin_translation.py`
- `causal_basin_periodicity.py`
- `causal_collapse_composition.py`
- `causal_relation_boundary.py`
- `lego_partition_fiber.py`
- corresponding tests

## 15. Prior-art boundary

Ehrhart/lattice-point results connecting polynomial degree to geometric dimension are classical. This project does not claim those theorems. The project-specific work is the causal LEGO derivation tying hidden-motion rank, exact fiber growth, P008 completion collapse, basin lowering, task-dependent continuation complexity, and observation-dependent boundaries into one integer-first framework.
