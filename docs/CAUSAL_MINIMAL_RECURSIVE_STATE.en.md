# Causal Minimal Recursive State — Coarsest Safe Contextual Quotient for a Finite Weighted LEGO Join

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREM + EXECUTABLE REFERENCE`

Ownership: A3 finite weighted specialization. The general future-safe quotient mother theory remains A2/P023.

## 1. Problem

The earlier `kappa(r,tau)` result says raw witness identity normally need not be retained forever: what matters is the continuation type that can still affect the declared future. But if joining another LEGO block is itself an allowed future operation, `tau` must also make the coupled binary join well-defined after quotienting.

This note gives the exact finite answer.

## 2. Raw weighted join

Let `X` be a finite raw witness set with current observation

\[
o:X\to O.
\]

Let the raw binary join kernel be

\[
\boxed{J(x,y;z,\delta)\in\mathbb N_0,}
\]

where `delta` is an integer grade shift. `J=0` means that raw output does not occur; positive values count raw joint witnesses.

## 3. Recursive-safe partition

A partition `P` is **recursive-safe** when both conditions hold.

First, current observation is constant on each block:

\[
x\sim_Px'\Longrightarrow o(x)=o(x').
\]

Second, binary composition descends. If

\[
x\sim_Px',\qquad y\sim_Py',
\]

then for every output block `C in P` and integer shift `delta`,

\[
\boxed{
\sum_{z\in C}J(x,y;z,\delta)
=
\sum_{z\in C}J(x',y';z,\delta).
}
\]

Thus any representatives of the same continuation types have the same typed output multiplicity/grade profile.

## 4. Contextual refinement algorithm

Start from the observation partition `P_0`. At refinement stage `t`, give each raw state `x` the signature consisting of:

1. `o(x)`;
2. for every raw partner `p`, the profile of `J(x,p)` aggregated by current `P_t` output class and grade shift;
3. for every raw partner `p`, the analogous profile of `J(p,x)`.

Split states with different signatures. On a finite set, the process has only finitely many strict refinements and therefore stabilizes.

## 5. MR-01 — Coarsest recursive-safe theorem

Let the stable partition be `P_*`. Then

\[
\boxed{
P_*\text{ is the coarsest recursive-safe refinement of }P_0.
}
\]

Proof sketch: let `S` be any recursive-safe partition refining `P_0`. Inductively suppose `S` refines `P_t`. If `x~_S x'`, then for any raw partner `p`, recursive safety makes the weighted join profiles agree on every `S` output block. Since every `P_t` block is a union of `S` blocks by the induction hypothesis, those profiles also agree after aggregation to `P_t`. The same holds in left and right partner contexts. Hence `x,x'` remain together in `P_(t+1)`, so `S` refines every stage and therefore `P_*`. Stability itself gives recursive safety of `P_*`.

Thus `P_*` is not a heuristic summary: it is the minimum exact identity-free recursive state for the declared observation and binary-composition language.

## 6. MR-02 — Induced typed kernel

For classes `A,B,C in P_*`, define

\[
\boxed{
K(A,B;C,\delta)
=
\sum_{z\in C}J(x,y;z,\delta),
\qquad x\in A,\ y\in B.
}
\]

MR-01 makes the right-hand side representative-independent, so `K` is well-defined. Runtime state therefore stores contextual type inventory rather than raw identity.

## 7. MR-03 — Associativity descends

If the raw weighted join is exactly associative at the witness level, then the induced typed kernel is associative as well. Therefore

\[
\boxed{
\text{associative raw coupled world}
\to P_*
\to\text{associative typed kernel }K
\to\text{arbitrary-dimensional recursive inventory}.
}
\]

No raw witness recovery is needed after the quotient.

## 8. Observation language changes the minimum state

There is no single a priori mathematically correct state granularity independent of the future language.

Example: addition modulo four. If only parity is observed and binary joins carry no grade information, residues `0~2` and `1~3` may remain two contextual types. If the future also reads the exact base-four carry

\[
\gamma(a,b)=\lfloor(a+b)/4\rfloor,
\]

then `0+3` and `2+3` have different grade shifts, so `0,2` must separate; similarly the four residues become distinct.

Hence

\[
\boxed{
\text{state granularity is produced by the declared causal future language, not by an a priori precision annotation.}
}
\]

## 9. Consequence for higher-order coupling

If a marginal/current state is too coarse, a minimal nonface may look like high-order coupling. The correct order of analysis is

\[
\boxed{
\text{exposed failure}
\to\text{minimal contextual refinement}
\to\text{typed coherence test}
\to\text{higher primitive claim only if still necessary}.
}
\]

A high coupling order in the exposed language is therefore not automatically an absolute physical interaction arity.

## 10. Executable assets

- `src/enterprise_math/causal_weighted_context_refinement.py`
- `src/enterprise_math/causal_recursive_join.py`
- `tests/test_causal_weighted_context_refinement.py`
- `tests/test_causal_recursive_join.py`

The test suite includes a small exhaustive set-partition oracle verifying that every recursive-safe partition in a three-state example refines the automatically compiled `P_*`.

## 11. Boundary

This is an exact theorem for finite raw witness spaces with finite nonnegative integer multiplicities and integer grade shifts. Infinite raw witness spaces, general minimal fixed-integer-schema complexity, stochastic/quantum amplitudes, physical FCC/HCP grade selection, Lean formalization, and clean-integration CI remain open.
