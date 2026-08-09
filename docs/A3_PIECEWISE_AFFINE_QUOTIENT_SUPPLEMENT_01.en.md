# A3 Piecewise Affine Quotient Supplement 01 — Two-Stage Construction of the Unique Coarsest Exact Partition

Status: `RESEARCH WIP / COARSEST EXACT PARTITION THEOREM + EXECUTABLE SOLVER`

## 1. Background

The main note proves that exactness for a binary threshold-affine map is **not monotone** under arbitrary partition refinement.

That does not imply that a minimum exact partition fails to exist or is computationally inaccessible.

On the full integer lattice `Z^k`, with one linear threshold guard and two integer affine branches, every declared initial partition still has a **unique coarsest exact refinement**, obtained by a two-stage synthesis.

## 2. Program

\[
T(c)=
\begin{cases}
B_+c+u_+,&w^Tc+b\ge0,\\
B_-c+u_-,&w^Tc+b<0.
\end{cases}
\]

Let the initial partition be `P_0`.

## 3. A3-PW04 — Branch-stable core partition

First ignore branch identity and require only that both branch linear parts descend.

Use the existing A3 linear-family solver to compute

\[
P_L=
\text{the coarsest refinement of }P_0
\text{ on which }B_+,B_-\text{ both descend}.
\]

Every exact partition for a nonconstant guard must refine `P_L`: whenever a branch is active on a coarse fiber, hidden kernel moves inside that fiber cannot change its coarse output.

## 4. Case one: `P_L` is already exact

Apply PW01/PW02 on `P_L`:

- the guard is already coarse-readable; or
- the guard is hidden but the two descended affine branch effects are identical.

Then

\[
\boxed{P_*=P_L.}
\]

It is exact, and every other exact refinement must refine `P_L`; hence it is the unique coarsest exact refinement.

This includes the important hidden-branch-erasure regime: branch identity is invisible, but it has no coarse consequence, so precision should not be raised merely to recover it.

## 5. Case two: hidden guard with different coarse branch effects

Let

\[
\Delta B=B_+-B_-,
\qquad
\Delta u=u_+-u_-.
\]

On `P_L` both branches descend individually, but their coarse effects differ. Therefore some `P_L` target block has a nonzero aggregated branch difference in a column of `Delta B`, or a nonzero aggregated offset difference from `Delta u`.

Suppose a finer partition `R` keeps the guard hidden yet tries to make the coarse branch effects equal again.

`R` splits that parent target block into child blocks. Equality on `R` would require the corresponding `Delta` aggregate to be zero on every child. Summing the child aggregates would force the parent aggregate to be zero as well, contradicting the nonzero difference already present on `P_L`.

Therefore

\[
\boxed{
\text{once a hidden guard sees different coarse branch effects on }P_L,
\text{ no refinement that keeps the guard hidden can be exact.}
}
\]

Every exact refinement must expose the guard.

## 6. Two-stage synthesis

First refine `P_L` by the guard coefficient signature:

\[
P_G=\operatorname{ObsRefine}(P_L,w).
\]

The guard is now coarse-readable.

But refinement can destroy branch stability, as shown by the non-monotonicity counterexample, so we cannot stop at `P_G`.

Restabilize both branch matrices:

\[
P_*=\operatorname{LinearStable}(P_G;B_+,B_-).
\]

Any exact partition must:

1. refine `P_L`;
2. in the current case expose the guard, hence refine `P_G`;
3. make both branch dynamics descend.

The coarseness theorem of the A3 linear solver therefore gives

\[
\boxed{
P_*=\text{the unique coarsest exact refinement of }P_0.
}
\]

## 7. Globally constant guard

If the fine guard has `w=0`, branch choice is globally constant and depends only on `b`.

The inactive branch creates no future obligation. The minimum solver stabilizes only the active branch:

\[
P_*=\operatorname{LinearStable}(P_0;B_{active}).
\]

This avoids artificial over-refinement.

## 8. Non-monotone exactness but a computable minimum

The binary-threshold class therefore has both properties:

1. exactness itself is not monotone under arbitrary partition refinement;
2. for every initial partition, the minimum exact refinement is still unique and has the two-stage construction above.

The correct solver invariant is a structural regime switch, not the false claim that every intermediate refinement remains exact.

## 9. Implementation and pressure tests

`src/enterprise_math/piecewise_relation_quotient.py` adds

`minimum_exact_partition_for_binary_threshold_piecewise(...)`.

Tests cover:

- retaining a coarse partition when a hidden guard is safely erased;
- exposing the guard only when hidden coarse branch effects differ;
- stabilizing only the active branch for a globally constant guard;
- a 4-coordinate exhaustive set-partition oracle verifying that every exact candidate refines the solver output.

## 10. Next

The next layer is a finite guard family, not arbitrary nonlinear code.

For guard matrix `W`, the structural object is

\[
W(K_A)\subseteq\mathbb Z^r,
\]

the integer image lattice generated in guard-score space by hidden partition motion.

The single-guard theorem is the first two cases:

- `rank W(K_A)=0`: guard visible;
- `rank W(K_A)=1`: both threshold sides occur in every coarse fiber.

For multiple guards we must distinguish full-rank hidden guard lattices from partially hidden directions and determine which branch sign patterns are actually realizable inside one coarse fiber.
