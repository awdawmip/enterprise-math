# Post-#1161 free research — branch-memory lattice and its positive-mass orbit quotient

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / BRANCH-RESOLVED MINIMAL MEMORY + UNLABELED ORBIT QUOTIENT / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessors:
- `research_notes/FREE_RESEARCH_POST1161_FIRST_BALANCE_RETURN_G0_BOUNDARY_20260904.md`
- `research_notes/FREE_RESEARCH_POST1161_FIRST_RETURN_ONE_COUNTER_NO_GO_20260904.md`

## 0. Why one counter is not the whole typed story

The absolute imbalance

\[
d=|\#A-\#B|\in\mathbb N_0
\]

is the coarsest state preserving the **unlabeled first-return mass** needed by the scalar AGM return RG.

But if the future language keeps the identity of the actual diamond witness appended at each step, the absolute value loses which branch is currently in excess. A branch-resolved deterministic update therefore needs a stronger memory object.

The correct object can be defined without choosing permanent names `A/B`.

## 1. Canonical branch-memory quotient

Let `D` be the actual two-element commuting-diamond witness fiber. Define the free integer multiplicity module

\[
\mathbb Z^D
\]

and quotient the common-baseline direction:

\[
\boxed{
\mathcal M_D
:=
\mathbb Z^D/\mathbb Z\mathbf1,
}
\]

where `1:D->Z` is the constant function.

A finite branch history `w` has multiplicity function

\[
\mu_w:D\to\mathbb N_0\subset\mathbb Z,
\]

and therefore a memory class

\[
\boxed{m(w)=[\mu_w]\in\mathcal M_D.}
\]

Adding the same count to both branch witnesses does not change the memory class. This is exactly the information irrelevant to future balance.

The zero class is precisely equal branch multiplicity:

\[
\boxed{m(w)=0\iff w\text{ is balanced}.}
\]

## 2. Branch append is well-defined before choosing a coordinate

For an actual witness `x in D`, append acts by

\[
\boxed{T_x([\mu])=[\mu+\delta_x].}
\]

This is well-defined on the quotient because a common diagonal shift remains a common diagonal shift after adding `delta_x`.

Thus `\mathcal M_D` supports the concrete branch-resolved process without choosing which witness is globally positive.

Because `|D|=2`, `\mathcal M_D` is a rank-one free abelian group. A choice of ordered names `(A,B)` identifies it with

\[
\mathbb Z,
\qquad
[\mu]\mapsto \mu(A)-\mu(B),
\]

but this coordinate is not canonical.

## 3. Witness swap acts by inversion

The nontrivial element of `Sym(D)=S_2` exchanges the two witnesses and induces

\[
\boxed{m\mapsto -m}
\]

on the rank-one memory lattice.

Therefore the choice of a positive generator of `\mathcal M_D` is an orientation choice; the object itself is canonical and carries a reflection action.

This is the exact branch-memory analogue of a typed signed/orientation carrier. Positive recoalescence does not retain this sign.

## 4. Unlabeled predictive quotient

For the first-return mass observer, witness swap is semantically invisible. Quotient again by `S_2`:

\[
\boxed{
\mathcal Q_D:=\mathcal M_D/S_2.
}
\]

For a two-element fiber, after choosing any temporary coordinate `z in Z`, the orbit is determined by `|z|`, so

\[
\boxed{
\mathcal Q_D\cong\mathbb N_0.
}
\]

This recovers exactly the absolute imbalance counter from the previous result.

Hence the typed information tower is

\[
\boxed{
\mathbb Z^D/\mathbb Z\mathbf1
\longrightarrow
(\mathbb Z^D/\mathbb Z\mathbf1)/S_2
\cong
\mathbb N_0.
}
\]

Interpretation:

- left: branch-resolved deterministic memory;
- right: branch-unlabeled first-return-mass predictive memory.

## 5. Minimality for the branch-resolved future language

Choose names only for the proof and write `z in Z` for the coordinate of a memory class.

With terminal zero made absorbing for verification, the two named branch actions are

\[
z\mapsto z+1,
\qquad
z\mapsto z-1.
\]

If `z>0`, the word consisting of `z` copies of the second branch hits zero, while for any `z'>z` it does not. Similarly negative states are separated by copies of the first branch, and `z` and `-z` are distinguished by which named action word returns.

Therefore distinct lattice classes have distinct all-future branch-resolved balance signatures:

\[
\boxed{m\ne m'\Longrightarrow \Sigma_{\rm resolved}(m)\ne\Sigma_{\rm resolved}(m').}
\]

So `\mathcal M_D` is the coarsest exact predictive quotient for the branch-resolved deterministic language.

## 6. Finite-horizon class counts

For a future horizon `h`, branch-resolved states with coordinates

\[
-h,-h+1,\ldots,0,\ldots,h-1,h
\]

are pairwise distinguishable. Every state with `|z|>h` cannot reach zero under any word of length at most `h`, so those states merge into one far class.

Thus the exact branch-resolved horizon quotient has

\[
\boxed{2h+2\text{ classes}.}
\]

After quotienting by witness swap, `z` and `-z` merge. The unlabeled mass observer therefore has

\[
\boxed{h+2\text{ classes},}
\]

matching the previous one-counter theorem.

Hence reflection/orientation data costs exactly `h` additional near classes at horizon `h`.

## 7. Relation to the AGM return RG

The AGM scalar return construction uses only first-return masses and is invariant under swapping the two local diamond witnesses. Therefore it factors completely through

\[
\mathcal Q_D\cong\mathbb N_0.
\]

The stronger `\mathcal M_D` state is unnecessary for the scalar AGM readout itself, but it is necessary if one asks for a branch-resolved deterministic refinement process before the final positive/mass quotient.

This clarifies the current positive-BRC boundary:

\[
\boxed{
\text{branch-resolved reflection-odd memory}
\to
\text{positive/unlabeled orbit memory}
\to
\text{first-return mass}
\to
\text{AGM scalar RG}.}
\]

The lost sign cannot be reconstructed from the positive orbit/mass layer alone.

## 8. Reuse of the existing quotient pattern

The algebraic pattern

\[
\mathbb Z^D/\mathbb Z\mathbf1
\]

resembles the already frozen derived displacement construction

\[
G_D=\mathbb Z^3/\mathbb Z(1,1,1),
\]

but the semantic types are different:

- existing `G_D`: derived endpoint/spatial displacement;
- present `\mathcal M_D`: N1 branch-history memory.

Representation-level similarity does not identify the objects. The current derived-displacement type-separation rule is therefore reused rather than bypassed.

No new generic quotient tool family is claimed.

## 9. Executable verification

Task-local checker:

`scripts/check_free_research_agm_branch_memory_lattice.py`

The checker verifies exactly:

- `1089` nonnegative multiplicity pairs `(a,b)` under common shifts;
- witness swap sends `z` to `-z`;
- concrete branch appends send `z` to `z+1` or `z-1`;
- horizons `h=0..10` have branch-resolved class counts
  `2,4,6,...,22` = `2h+2`;
- the corresponding unlabeled class counts are
  `2,3,4,...,12` = `h+2`;
- unlabeled signatures are invariant under `z -> -z`.

The checker was fetched back from `main` and independently replayed successfully.

## 10. Native-semantics classification

The memory lattice is constructed from cumulative path history, so under current semantics it is N1, not instantaneous N0/G0.

Its orbit quotient `N_0` and first-return masses are observer-relative quotients/readouts downstream of that process.

Strongest current typing:

\[
\boxed{
\text{native two-witness path skeleton}
\to
\text{N1 branch-memory lattice }\mathcal M_D
\to
\text{N1/N2 swap-orbit counter }\mathbb N_0
\to
\text{N2 AGM return-mass RG}.}
\]

This does not promote signed branch memory into the positive Weighted-BRC layer and does not claim a new primitive native negative axis.

## 11. Consequence for the six-dimensional lift question

Any full native lift that intends to reproduce the **branch-resolved** process must carry at least the semantic information of `\mathcal M_D`, or an equivalent state from which its future signatures factor.

A lift intended only to reproduce the scalar AGM return masses need carry only the orbit information `|m|`.

Thus the unresolved native-to-FCC hidden fiber has a newly precise target type:

- reflection-odd rank-one integer memory for branch-resolved lifting;
- rotation-scalar nonnegative integer orbit for scalar AGM lifting.

This gives the existing `NATIVE_TO_FCC_EQUIVARIANT_LIFT_NOT_PROVED` frontier a concrete information requirement rather than an unspecified hidden coordinate.
