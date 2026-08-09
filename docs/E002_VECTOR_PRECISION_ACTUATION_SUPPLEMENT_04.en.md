# E002 — Vector Precision and Correlated Actuation, Supplement 04

Status: `ACTIVE ENGINEERING RESEARCH NOTE`  
Scope: rectangular vector precision, finite-horizon vector actions, coordinate projection repair, and correlation expansion  
Parent: `docs/E002_PRECISION_HORIZON_SATURATION_SUPPLEMENT_03.en.md`  
Dependency: E002 centered quotient/action calculus and P023 task-relative future compatibility

## 1. Why multiple dimensions are a genuine pressure test

The scalar Stage-3 theorem says that for one centered width `w`, the exact number of within-cell classes required by all action words up to horizon `h` is

\[
c_h=|S_h|,
\]

where `S_h` is the set of reachable total-action residues modulo `w`.

A tempting multidimensional generalization is to replace `S_h` by the set of reachable residue **vectors** and keep the same cardinality rule.

That guess is false.

A vector coarse observable reports each coordinate quotient separately. One reachable residue vector may therefore introduce an independent boundary on several coordinate detail axes at once. Correlation in the physical action trajectory does not imply that the observed coordinate phases may be collapsed together.

This supplement derives the exact rectangular replacement and records a minimal counterexample to the naive subgroup-size rule.

## 2. Rectangular centered precision

Let the state be

\[
x=(x_1,\ldots,x_n)\in\mathbb Z^n
\]

and let the centered odd cell widths be

\[
w=(w_1,\ldots,w_n),
\qquad w_i\in2\mathbb N+1.
\]

For every coordinate write

\[
\boxed{
x_i=w_iq_i+r_i-c_i,
\qquad
c_i=\frac{w_i-1}{2},
\qquad
0\le r_i<w_i.}
\]

The rectangular quotient/detail state is

\[
Q_w^c(x)=(q_1,\ldots,q_n),
\qquad
R_w^c(x)=(r_1,\ldots,r_n).
\]

This is just the Cartesian product of the one-dimensional centered Euclidean charts; no Euclidean norm or hidden real coordinate is introduced.

## 3. E002-T24 — Vector translation compatibility

Let one physical vector action be

\[
a=(a_1,\ldots,a_n)\in\mathbb Z^n.
\]

For each coordinate write

\[
a_i=k_iw_i+s_i,
\qquad0\le s_i<w_i.
\]

Then the exact vector transport is

\[
\boxed{
q_i'=q_i+k_i+\gamma_i,
\qquad
r_i'=(r_i+s_i)\bmod w_i,
}
\]

where

\[
\boxed{
\gamma_i=\mathbf1_{r_i+s_i\ge w_i}.}
\]

Consequently the translation descends to a deterministic operation on the full rectangular quotient if and only if

\[
\boxed{w_i\mid a_i\quad\text{for every coordinate }i.}
\]

### Proof

The transport formula is the scalar Stage-2 Euclidean carry identity applied coordinate-wise. If every remainder `s_i` is zero, all carry bits vanish and the quotient update is deterministic.

Conversely, if some `s_j` is nonzero, hold every other detail coordinate fixed and choose two values of `r_j` on opposite sides of the threshold `w_j-s_j`. The two fine vector states share one rectangular quotient before the action but have different `j`-th quotient coordinates afterward. ∎

## 4. Reachable vector residues

Let `A` be a finite vector-action alphabet and let `W_h` be all words of length at most `h`.

For a word `v`, write its total vector increment as

\[
\Sigma(v)=(\Sigma_1(v),\ldots,\Sigma_n(v)).
\]

Define the reachable residue-vector set

\[
\boxed{
S_h=
\{(\Sigma_1(v)\bmod w_1,\ldots,\Sigma_n(v)\bmod w_n):v\in W_h\}.
}
\]

For each coordinate let

\[
\boxed{S_{h,i}=\pi_i(S_h)\subseteq\mathbb Z/w_i\mathbb Z}
\]

be its coordinate projection.

## 5. E002-T25 — Exact vector finite-horizon class count

For the **full vector quotient output**, two detail vectors `r,r'` in one original rectangular cell are future-equivalent through horizon `h` if and only if, for every coordinate `i`,

\[
\boxed{
\mathbf1_{r_i+s\ge w_i}
=
\mathbf1_{r_i'+s\ge w_i}
\quad
\text{for every }s\in S_{h,i}.}
\]

Therefore coordinate `i` is partitioned into exactly

\[
|S_{h,i}|
\]

future-distinguishable detail intervals, and the complete rectangular detail cell is partitioned into exactly

\[
\boxed{
C_h=\prod_{i=1}^n|S_{h,i}|.}
\]

### Proof

For a fixed future word, the `i`-th output quotient differs between two states in the same input cell only through the coordinate carry associated with that word's `i`-th residue. Thus equality of all full vector outputs is equivalent to equality of all coordinate carry bits for all residues that actually occur in each coordinate projection.

The scalar Stage-3 threshold argument gives exactly `|S_(h,i)|` classes on coordinate `i`. Conditions on distinct detail coordinates are independent because the output exposes every quotient coordinate. The whole equivalence relation is therefore the Cartesian product of the coordinate relations, giving the product cardinality. ∎

## 6. E002-T25a — Vector repair rank

Define one scalar threshold rank per coordinate:

\[
\boxed{
\rho_{h,i}(r_i)
=
\#\{s\in S_{h,i}\setminus\{0\}:r_i+s\ge w_i\}.
}
\]

Then the repaired state

\[
\boxed{
(Q_w^c(x),\rho_{h,1}(r_1),\ldots,\rho_{h,n}(r_n))
}
\]

is the coarsest state that preserves all full-vector quotient outputs for all words of length at most `h`.

The repair cardinality inside one original rectangular cell is exactly `C_h`.

## 7. Minimal counterexample to the naive residue-vector count

Take

\[
w_1=w_2=3
\]

and the single repeated action

\[
a=(1,1).
\]

By horizon `2`, the reachable residue vectors are only

\[
S_2=\{(0,0),(1,1),(2,2)\},
\]

so

\[
|S_2|=3.
\]

But both coordinate projections are

\[
S_{2,1}=S_{2,2}=\{0,1,2\}.
\]

Hence T25 gives

\[
\boxed{C_2=3\cdot3=9.}
\]

Direct enumeration confirms that all nine fine phases in the original `3x3` cell have distinct horizon-2 full-vector quotient signatures.

Thus

\[
\boxed{|S_h|\text{ is not the multidimensional precision class count}.}
\]

This is a strict negative boundary on the scalar theorem.

## 8. E002-T26 — Arbitrary-horizon coordinate gcd repair

For an action family

\[
A=\{a^{(1)},\ldots,a^{(m)}\},
\]

define for each coordinate

\[
\boxed{
g_i=\gcd(w_i,|a_i^{(1)}|,\ldots,|a_i^{(m)}|).}
\]

At arbitrary finite horizon, the `i`-th coordinate projection of the generated residue subgroup is exactly

\[
\boxed{
H_i=\{0,g_i,2g_i,\ldots,w_i-g_i\},
}
\]

with

\[
|H_i|=w_i/g_i.
\]

Therefore the coarsest arbitrary-horizon future-safe rectangular refinement has coordinate widths

\[
\boxed{(g_1,\ldots,g_n)}
\]

and exactly

\[
\boxed{
C_\infty=\prod_{i=1}^n\frac{w_i}{g_i}
}
\]

classes inside each original rectangular cell.

### Why action correlation does not reduce this count

Suppose two detail vectors differ in the repaired class of coordinate `i`. The scalar gcd theorem guarantees a residue value in `H_i` that separates them. Since `H_i` is the projection of the full generated vector subgroup, some actual finite action word realizes a vector residue having exactly that `i`-th component. The full vector output then differs in coordinate `i`, regardless of what happens on the other coordinates.

Thus the complete future-equivalence relation is the product of coordinate gcd repairs.

## 9. Full action subgroup versus observed precision state

Let

\[
H\subseteq\prod_i\mathbb Z/w_i\mathbb Z
\]

be the full residue subgroup generated by the vector actions.

There is a canonical inclusion

\[
\boxed{H\hookrightarrow\prod_iH_i.}
\]

Its cardinality need not be the precision class count.

Define the integer

\[
\boxed{
\Delta_A
=
\frac{\prod_i|H_i|}{|H|}.}
\]

Because `H` is a subgroup of the finite product of its projections,

\[
\boxed{\Delta_A\in\mathbb N_{\ge1}.}
\]

## 10. E002-T27 — Correlation expansion factor

For the full vector quotient observable,

\[
\boxed{C_\infty=\Delta_A|H|.}
\]

Moreover

\[
\boxed{\Delta_A=1}
\]

if and only if

\[
\boxed{H=\prod_iH_i.}
\]

### Proof

The first identity is the definition combined with T26. Since `H` is a finite subset/subgroup of the product of its coordinate projections, equality of cardinalities holds exactly when the inclusion is surjective, i.e. exactly when `H` equals the full product. ∎

### Interpretation

`Delta_A` does **not** measure a new physical force or entropy. It records how much the full coordinate-wise precision observable expands beyond the cardinality of the correlated physical action residue subgroup.

If actions can vary independently along all coordinate projections, `Delta_A=1`.

If action coordinates are strongly correlated, `Delta_A` can be large because the full output still reads each coordinate phase independently.

## 11. E002-T28 — Single vector action closed forms

For one repeated vector action

\[
a=(a_1,\ldots,a_n),
\]

define coordinate periods

\[
\boxed{
P_i=\frac{w_i}{\gcd(w_i,|a_i|)}.}
\]

The residue vector itself has group order

\[
\boxed{
|H|=\operatorname{lcm}(P_1,\ldots,P_n).
}
\]

But the full-vector arbitrary-horizon precision state has

\[
\boxed{
C_\infty=\prod_iP_i.
}
\]

and therefore

\[
\boxed{
\Delta_A=
\frac{\prod_iP_i}{\operatorname{lcm}(P_1,\ldots,P_n)}.
}
\]

At finite horizon,

\[
\boxed{
C_h=\prod_i\min(h+1,P_i).
}
\]

### Proof

At horizon `h`, the only word totals are `ka`, `0<=k<=h`. Coordinate `i` therefore visits `min(h+1,P_i)` distinct residues before its period closes. Apply T25. The arbitrary-horizon formulas follow after every coordinate projection has stabilized. The order of the single residue vector in the direct product group is the lcm of the coordinate orders. ∎

## 12. Dimension-power growth from one unbranched actuator

If all `n` coordinates have the same period `P`, then a single repeated correlated action gives

\[
\boxed{
C_h=\min(h+1,P)^n.
}
\]

Its physical residue trajectory has only `P` vector states, but the full vector quotient eventually needs

\[
\boxed{P^n}
\]

within-cell classes, with

\[
\boxed{\Delta_A=P^{n-1}.}
\]

Example:

\[
w=(5,5,5),
\qquad a=(1,1,1).
\]

The finite-horizon class counts are

\[
\boxed{1,8,27,64,125,125,\ldots}
\]

for horizons `0,1,2,3,4,5,...`. The action subgroup has order only `5`, while the full vector precision partition has `125` classes and `Delta_A=25`.

This demonstrates that branching of the **action policy** is not required for rapid growth of the precision obligation; multiple observed coordinates can expose independent boundary phases along one deterministic action orbit.

## 13. Task-relative negative boundary

T25 through T28 assume that the future observable is the **complete vector of centered quotient coordinates**.

If a task observes only:

- one coordinate;
- a Boolean condition;
- a norm-like shell;
- an aggregate relation;
- or another many-to-one function of the vector quotient,

then P023 may permit a strictly coarser repair.

Therefore

\[
\prod_i|S_{h,i}|
\]

is not a universal multidimensional precision law independent of the future language. It is the exact law for the declared rectangular full-vector quotient language.

This boundary is essential: otherwise E002 would simply replace one overly strong universal scalar precision with an overly strong universal rectangular precision.

## 14. Relation to possible lattice/SNF generalizations

The scalar gcd theorem might suggest immediately replacing gcd by Smith normal form in multiple dimensions. T27 shows why that move is premature.

Smith/module invariants describe the generated action subgroup and its quotient structure, but the full rectangular observable may require more classes than the subgroup cardinality because it reads coordinate boundary phases separately.

A genuine lattice-shaped precision cell or mixed linear observable may indeed make module normal forms the correct language. That must be derived for the declared observation map rather than imported by analogy.

## 15. Executable audit

Implementation:

- `src/enterprise_math/precision_vector_actuation.py`

Tests:

- `tests/test_precision_vector_actuation.py`

Probe:

- `experiments/e002_vector_actuation_probe.py`

Independent bounded reconstruction checked over more than one thousand small 2D/3D width/action/horizon cases that direct operation-word signatures equal the product-of-coordinate-projection formula. The committed tests also check:

- exact rectangular reconstruction and vector carry transport;
- component-wise divisibility for one-step quotient closure;
- coordinate repair rank against direct future signatures;
- the `3x3` diagonal-action counterexample `|S_2|=3` versus `C_2=9`;
- coordinate-wise gcd stable widths;
- integer `Delta_A` and its collapse to one for independent axes;
- single-action finite-horizon and subgroup-order closed forms;
- the three-dimensional `1,8,27,64,125` phase-growth example.

## 16. Prior-art and novelty boundary

Direct products of finite cyclic groups, coordinate projections, subgroup indices, gcd/lcm order formulas, rectangular quantization, and product partitions are established mathematics and engineering structures. E002 does not claim them as inventions.

The research contribution being tested is the exact way the declared full-vector finite-precision future language forces a product-of-projection repair rather than the naive cardinality of the correlated action residue set.

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 17. Next pressure tests

High-value next targets:

1. replace the full rectangular output by a mixed linear/lattice observation and determine when subgroup/module invariants become sufficient;
2. derive state-dependent vector action alphabets and controller-policy restrictions on the reachable residue graph;
3. apply the vector horizon formula to spatial E001 motion/collision coordinates;
4. compare precision-growth complexity `C_h` with direct fine-state simulation cost;
5. test non-rectangular finite cells before making any geometric claim about physical space.
