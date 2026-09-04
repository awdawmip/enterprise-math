# Post-#1161 free research — two-index whole-trajectory first-return interval certificate

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / PURE-INTEGER OUTWARD TRAJECTORY CERTIFICATE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessors:
- `research_notes/FREE_RESEARCH_POST1161_S4_GRADED_FINITE_RETURN_RG_20260904.md`
- `research_notes/FREE_RESEARCH_POST1161_ADAPTIVE_RETURN_DEPTH_RESOURCE_LAW_20260904.md`

## 0. Result

The outer AGM iteration and the inner first-return predictive refinement can be combined into one rigorous two-index interval computation that encloses the **exact** endogenous completion `Pi_*` throughout the whole trajectory.

The construction uses only

- integers;
- one fixed dyadic denominator `2^B`;
- integer floor square root for the initial `1/sqrt(2)` precision cell;
- exact rational first-return coefficients;
- outward integer rounding;
- the finite first-return tail theorem.

No floating point, runtime real square root, elliptic integral, classical circumference, or target value of pi enters the propagation.

With

\[
B=640,
\]

six outer AGM steps, and return depths

\[
\boxed{175,43,17,7,3,1,}
\]

the final exact `Pi_*` bracket has

\[
\boxed{\text{width}<2^{-546},}
\]

both endpoints lie in one common

\[
\boxed{544\text{-bit dyadic cell},}
\]

and in one common

\[
\boxed{162\text{-decimal-place cell}.}
\]

This converts the earlier one-step resource law into a whole-trajectory certificate.

## 1. Fixed-point dyadic interval carrier

Fix

\[
S=2^B.
\]

Every nonnegative real quantity `x` is represented by integers

\[
[x_-,x_+]
\]

meaning

\[
\frac{x_-}{S}\le x\le\frac{x_+}{S}.
\]

All arithmetic rounds outward:

- multiplication rounds the lower product down and upper product up after division by `S`;
- positive division uses cross-endpoint floor/ceiling;
- halving rounds lower down and upper up.

Thus every finite machine state is integer-valued.

## 2. Initial state

Set

\[
a_0=1,\qquad A_0=1,\qquad P_0=1.
\]

For

\[
b_0=1/\sqrt2,
\]

compute

\[
k=\left\lfloor 2^B/\sqrt2\right\rfloor
=\operatorname{isqrt}(2^{2B-1}).
\]

Then

\[
\boxed{
\frac{k}{2^B}
\le b_0
<\frac{k+1}{2^B}
}
\]

because

\[
k^2\le2^{2B-1}<(k+1)^2.
\]

This is exactly the previously established integer precision-root semantics.

## 3. Shape interval

Assume current intervals enclose exact `a>=b>0` and `A>0`.

Define outward intervals

\[
H=a+b,
\qquad
U=a-b,
\qquad
s=U/H.
\]

For positive intervals,

\[
\boxed{
\frac{U_-}{H_+}
\le s
\le
\frac{U_+}{H_-}.}
\]

All endpoints are rounded outward on the fixed dyadic grid.

## 4. First-return mass interval

For chosen finite return depth `N`, evaluate the positive polynomial

\[
F_N(s)=\sum_{k=1}^N f_ks^{2k}
\]

outward on the shape interval. Positivity of every coefficient gives

\[
F_N(s_-)\le F_N(s)\le F_N(s_+).
\]

The exact tail theorem gives

\[
0\le F(s)-F_N(s)\le s^{2N+2}.
\]

Hence the exact completed first-return mass is enclosed by

\[
\boxed{
F_N(s_-)
\le F(s)
\le
F_N(s_+)+s_+^{2N+2}.}
\]

The checker evaluates every power and Catalan coefficient by outward fixed-point integer arithmetic.

## 5. Exact state update from the return interval

The exact return reconstruction is

\[
a^+=\frac H2,
\]

\[
b^+=\frac H2(1-F),
\]

\[
A^+=A-PU^2,
\qquad
P^+=2P.
\]

Because all displayed maps are monotone in the relevant nonnegative variables once endpoint directions are respected, the return-mass interval gives a direct outward next-state interval:

\[
\boxed{
a^+\in H/2,}
\]

\[
\boxed{
b^+\in \frac H2\,[1-F_+,1-F_-],}
\]

\[
\boxed{A^+\in[A_- -P U_+^2,\ A_+ -P U_-^2].}
\]

Therefore induction on the outer step proves that every propagated interval contains the corresponding exact AGM state.

No finite point approximation is ever substituted for the exact state.

## 6. Completion bracket without a runtime root

The #1161 finite completion theorem gives at an exact state

\[
\frac{V^2}{A}\le\Pi_*\le\frac{H^2}{A-2\delta},
\]

with

\[
V^2=4ab,
\qquad
\delta=PU^2.
\]

Thus a conservative interval state yields the purely rational bracket

\[
\boxed{
\frac{4a_-b_-}{A_+}
\le\Pi_*
\le
\frac{H_+^2}{A_- -2P U_+^2}.}
\]

No square root is needed even at the final readout.

## 7. Concrete guarded schedule

Take target `256` inner bits and a deliberately conservative `96`-bit local guard. Applying the adaptive return-depth law to target `352` gives

\[
\boxed{N_0,\ldots,N_5=(175,43,17,7,3,1).}
\]

The corresponding `S4` scalar predictive state counts

\[
24N+12
\]

are

\[
\boxed{4212,1044,420,180,84,36.}
\]

This schedule is not claimed globally optimal. It is a robust schedule derived before trajectory propagation.

## 8. Whole-trajectory narrowing

Using `B=640` and the schedule above, the certified completion-bracket width exponents after outer steps `0..6` are

\[
\boxed{0,8,25,61,132,276,546.}
\]

That is, after step `n` the bracket width is strictly less than `2^{-e_n}` for the displayed exponent `e_n`.

The last outer AGM step therefore more than doubles the already certified precision, reflecting the quadratic shape contraction at the level of the completion interval itself.

At step six:

\[
\boxed{\operatorname{width}<2^{-546}.}
\]

Moreover both rational endpoints lie in the same half-open binary cell at depth `544` and the same decimal cell at depth `162`.

The first 80 characters of the common decimal cell are

`3.141592653589793238462643383279502884197169399375105820974944592307816406286208`

This is a computed certificate for the already internally identified `Pi_*`; that decimal string is output, not input.

## 9. Two independent finite precision coordinates

The construction has two finite precision controls:

1. **dyadic arithmetic precision `B`** — how finely scalar intervals are stored;
2. **return depth `N_n`** — how much branch-return future is retained at outer step `n`.

They control different losses:

- fixed-point rounding width;
- unresolved first-return tail mass.

Neither may be silently identified with the other.

The state can therefore be typed by a two-index precision coordinate

\[
\boxed{(B,N_n).}
\]

At every finite pair the computation is finite and certified. Increasing either coordinate refines the corresponding information loss.

## 10. Relation to the graded S4 predictive tower

Return depth `N` corresponds to graded horizon

\[
h=2N-1.
\]

The exact scalar predictive state cost over all twelve diamond positions is

\[
|X_h|=12(h+2)=24N+12.
\]

Thus the interval compiler does not use return coefficients as unexplained external constants: each coefficient is the first-hit mass generated by the finite `S4`-equivariant predictive tower already constructed.

The present compiler is the scalar arithmetic/readout layer sitting on top of that finite state tower.

## 11. Executable evidence

Task-local checker:

`scripts/check_free_research_agm_two_index_interval_certificate.py`

Commit:

`89058ae166c2a5d2b19311b7536949d58b64d05f`.

Frozen parameters/output:

- fixed dyadic bits: `640`;
- outer steps: `6`;
- return depths: `[175,43,17,7,3,1]`;
- state costs: `[4212,1044,420,180,84,36]`;
- bracket width exponents: `[0,8,25,61,132,276,546]`;
- final common binary cell: `544` bits;
- final common decimal cell: `162` places.

The file was fetched back from `main`; its fixed-point integer logic was independently replayed and reproduced the frozen width/cell outputs.

## 12. Scope and next resource problem

This closes the warning left by the one-step adaptive theorem: the finite-return errors can be propagated as outward intervals and do yield a rigorous final completion certificate.

The schedule above is intentionally conservative and strongly overachieves the 256-bit target. The next independent question is an optimization problem:

> Minimize total finite predictive state cost
> \[
> \sum_n(24N_n+12)
> \]
> subject to a declared final `Pi_*` bracket precision, using the rigorous interval compiler as the feasibility oracle; then determine whether the discrete Pareto optimum admits a closed analytic error-allocation law.

This is a resource/precision problem and remains independent of the active P000 Gen19 PF10/connection moduli task.
