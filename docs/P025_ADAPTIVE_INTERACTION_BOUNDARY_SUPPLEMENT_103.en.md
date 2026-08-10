# P025 Supplement 103 — Adaptive Ferrers Boundary for Mixed History Interactions

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-history-closure-stage101`  
Depends on: P025 Supplement 102  
Hard block: `NONE`

## 1. Raw second-order storage is still over-precise

Stage 102 proves exact finite-history closure with the mixed corner block

\[
C_{ij}=\mathbf1_{\{v_j\ge U_i\}}.
\]

Written naively, this appears to require `a*b` Boolean coordinates for `a` candidate thresholds and `b` future nodes.

Stage 103 shows that most of those bits are either forced or Ferrers-redundant.

## 2. P025-T234 — resolved threshold rows force all mixed corners

Let the old orbit maximum be

\[
M:=\rho_h.
\]

For candidate threshold `U_i`, its old-block span satisfies

\[
L_i>0
\iff
U_i\le M.
\]

Every future node obeys

\[
v_j\ge M.
\]

Therefore

\[
\boxed{
L_i>0
\Longrightarrow
C_{ij}=1\quad\text{for every }j.
}
\]

So a candidate threshold already resolved by the old horizon contributes **zero new mixed uncertainty**.

Only thresholds with

\[
\boxed{U_i>M}
\]

can carry nontrivial second-order information.

Because the candidate thresholds are ordered, these unresolved thresholds form a suffix.

## 3. P025-D46 — unresolved interaction block

Let

\[
u:=\#\{i:U_i>M\}
\]

be the number of unresolved candidate thresholds.

Discard the forced all-one resolved rows and retain only the `u x b` unresolved block.

For each unresolved threshold define the future crossing depth

\[
\kappa_i:=\min\{j:v_j\ge U_i\},
\]

with `infinity` when the future prefix never reaches the threshold.

Since the unresolved thresholds increase,

\[
\boxed{
\kappa_1\le\kappa_2\le\cdots\le\kappa_u.
}
\]

Thus the entire unresolved interaction block is reconstructed from one monotone crossing vector.

## 4. Dual future-rank coordinates

For each future node define its rank among unresolved candidate thresholds:

\[
q_j:=\#\{i:U_i>M,\ v_j\ge U_i\}.
\]

Because future values are nondecreasing,

\[
\boxed{q_1\le q_2\le\cdots\le q_b.}
\]

The two coordinate systems are exact duals:

\[
q_j=\#\{i:\kappa_i\le j\},
\]

\[
\kappa_i=\min\{j:q_j\ge i\}.
\]

So the mixed second-order response has the same Ferrers geometry that appeared in Stages 92–94, now localized to the **unresolved prospective block**.

## 5. P025-T235 — exact interaction-state count

An unconstrained `u x b` Boolean block has

\[
2^{ub}
\]

possible states.

A Ferrers block is determined by a weakly increasing crossing vector of length `u` taking values in

\[
0,1,\ldots,b-1,\infty.
\]

Hence the number of compatible mixed interaction states is exactly

\[
\boxed{
\binom{u+b}{u}.
}
\]

For `u=b=4`, this is

\[
\boxed{70}
\]

instead of

\[
\boxed{65536}.
\]

## 6. Degenerate return to first order

If

\[
u=0,
\]

then every candidate threshold is already crossed by the old orbit maximum. The entire mixed block is forced to all ones, so

\[
\boxed{
\#\text{compatible mixed states}=1.
}
\]

No genuinely new second-order precision is required.

Thus “history closure is second order” is a worst-case structural statement. The precision actually instantiated at a state can collapse back to first order.

## 7. Stage101 recovered as the smallest case

For one unresolved threshold and one future node (`u=b=1`), the compatible interaction states are exactly

\[
\boxed{C_{U,v}\in\{0,1\}.}
\]

This is precisely the mixed corner bit isolated by Stage101.

So Stage101 is not an isolated counterexample; it is the smallest cell of the Stage103 Ferrers interaction geometry.

## 8. Arithmetic fixture

For the `(q,p)=(3,41)` dyadic pressure orbit, take the old prefix through exponent `4`:

\[
M=\rho_{4,-}=\frac{13}{22}.
\]

With candidate thresholds

\[
\frac1{20},\frac12,1,5,11
\]

only the first two are resolved by the old horizon. The unresolved suffix is

\[
1,5,11.
\]

The next two exact dyadic pressures are both

\[
\frac{221}{22}.
\]

Therefore the unresolved crossing depths are

\[
\boxed{(0,0,\infty)}
\]

and the future unresolved ranks are

\[
\boxed{(2,2).}
\]

The full mixed block is exactly reconstructible from either description.

## 9. Architectural consequence

Stage 103 gives an adaptive precision-genesis rule:

\[
\boxed{
\text{second-order state is born only on unresolved future distinctions.}
}
\]

The response order is determined by the operation algebra, but the **amount** of second-order information is determined by the current state relative to the declared future horizon.

This separates two notions that should not be conflated:

- maximal interaction order required by the language;
- realized precision dimension at the current state.

## 10. Prior-art / novelty boundary

Ferrers matrices, lattice paths and monotone rank/crossing duality are classical combinatorics. P025 claims none individually.

The project-side result is the adaptive localization of Stage102's exact history interaction block to unresolved arithmetic precision, together with executable pressure fixtures. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_history_interaction_boundary.py`;
- `tests/test_abc_history_interaction_boundary.py`.

## 12. Next frontier

The remaining first-order node data `(R_j)` also form a monotone staircase. Stage104 should combine:

1. candidate-threshold old spans;
2. future-node old ranks;
3. unresolved mixed Ferrers boundary;

into one compressed history-response atlas and determine which parts are forced by the others.