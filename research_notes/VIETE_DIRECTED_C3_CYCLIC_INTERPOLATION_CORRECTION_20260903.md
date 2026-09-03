# Viète correction: current directed C3 ray refinement is an index-two cyclic interpolation, not a two-sheet graph cover

Status: `FREE_RESEARCH / CORRECTION + EXACT CYCLIC-INTERPOLATION REFINEMENT THEOREM / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Corrects/retypes:
- `VIETE_BINARY_CYCLE_COVERS_2ADIC_VS_ANALYTIC_COMPLETION_20260903.md`;
- `VIETE_MINIMAL_FINITE_REFINEMENT_EXTENSION_CLASSIFICATION_20260903.md`;
- `VIETE_C3_TO_C6_BINARY_COVER_HOLONOMY_BIT_20260903.md`.
Preserves the algebraic root theorem in:
- `VIETE_FINITE_CYCLIC_SHORTEST_ROOT_REFINEMENT_20260903.md`.

## 1. Correction trigger

The current three-axis Foundation does not begin with three **unoriented** line classes. It begins with three directed positive native rays

\[
E_1,E_2,E_3
\]

in cyclic order, with one coarse ray transition corresponding to the `C3` generator.

Therefore a correct precision refinement must preserve those three old directed states and insert finer orientation states **between** them.

A graph-cover projection

\[
C_6\to C_3
\]

that maps each fine adjacent step to one coarse adjacent step has the wrong monodromy for this meaning: three fine steps complete a coarse `C3` loop but land at the opposite fine state. That would interpret one coarse full turn as a fine half-turn.

For the current directed positive-ray semantics this is not the intended state refinement.

Hence the prior “connected two-sheeted cover of the current C3 ray cycle” interpretation is retracted at native/G1-directed-ray strength.

## 2. Correct binary precision refinement: retain old states and split each old step

Let

\[
G_N=C_N=\langle r\mid r^N=e\rangle
\]

be a finite directed orientation cycle whose generator `r` is one coarse rotation step.

A binary interpolation refinement should supply a fine cyclic group

\[
G_{2N}=C_{2N}=\langle q\mid q^{2N}=e\rangle
\]

and an injective homomorphism

\[
\boxed{
\iota_N:G_N\hookrightarrow G_{2N}
}
\]

such that

\[
\boxed{
\iota_N(r)=q^2.
}
\]

Thus every old state is retained:

\[
\boxed{
\iota_N(r^k)=q^{2k}.
}
\]

The new odd powers

\[
q^{2k+1}
\]

are the interpolating fine states inserted between the old even states.

This is the correct “one coarse step becomes two equal fine steps” semantics.

## 3. Full-turn closure is preserved

The coarse full turn is

\[
r^N=e.
\]

Under the refinement,

\[
\iota_N(r^N)=q^{2N}=e.
\]

Thus one complete old `C_N` cycle remains one complete fine `C_(2N)` cycle when each old edge is resolved into two fine steps.

There is no erroneous sheet flip after one old full turn.

## 4. C3 -> C6 now has the correct directed-ray interpretation

Start from the current positive-ray cycle

\[
C_3=\langle r\rangle.
\]

Refine to

\[
C_6=\langle q\rangle,
\qquad
r\mapsto q^2.
\]

The three current positive ray states are the even powers

\[
\boxed{
1,\quad q^2,\quad q^4.
}
\]

The new interpolating fine states are

\[
\boxed{
q,\quad q^3,\quad q^5.
}
\]

The half-turn is

\[
\boxed{h=q^3.}
\]

It is **new at the first refinement** and is not one of the original positive-ray states.

Thus the six-gate shell still emerges minimally from the `C3` positive-ray structure, but by cyclic interpolation rather than by a graph-cover monodromy of the directed ray cycle.

No primitive native negative axes are introduced.

## 5. Next refinement C6 -> C12 produces the quarter-turn roots correctly

Refine again:

\[
C_6\hookrightarrow C_{12},
\qquad
q\mapsto Q^2.
\]

The coarse half-turn

\[
h=q^3
\]

embeds as

\[
\iota_6(h)=Q^6.
\]

Its two square roots in `C12` are

\[
\boxed{
Q^3,
\qquad
Q^9.
}
\]

Both have order four and are exchanged by inversion.

Therefore the key #1158 sequence survives unchanged:

\[
C_3
\hookrightarrow
C_6
\hookrightarrow
C_{12}
\hookrightarrow
C_{24}
\hookrightarrow\cdots,
\]

but the arrows mean **state-retaining cyclic interpolation embeddings**, not graph-cover projections of the current directed ray cycle.

## 6. Square-root formulation

For a coarse state

\[
x=r^k,
\]

its embedded fine state is

\[
\iota_N(x)=q^{2k}.
\]

The two square roots of that embedded state are

\[
\boxed{
q^k,
\qquad
q^{k+N}.
}
\]

This is exactly the root pair already used in the valid shortest-root theorem.

Therefore the algebraic core of `VIETE_FINITE_CYCLIC_SHORTEST_ROOT_REFINEMENT_20260903.md` remains correct.

## 7. Exact normalized-distance halving survives the correction

Define coarse normalized Cayley distance

\[
\theta_N(r^k)
=
\frac{\min(k,N-k)}{N}.
\]

The embedded old state has fine distance

\[
\delta_{2N}(q^{2k},e)
=2\min(k,N-k),
\]

so its normalized distance is unchanged:

\[
\boxed{
\theta_{2N}(\iota_N(x))=\theta_N(x).
}
\]

The two square roots have fine distances

\[
k
\quad\text{and}\quad
N-k.
\]

The identity-near root(s) therefore have distance

\[
\min(k,N-k).
\]

Hence the retained shortest root satisfies

\[
\boxed{
\theta_{2N}(\operatorname{root}_{\min}x)
=
\frac12\theta_N(x).
}
\]

Thus the strongest target-free interpretation of “half-angle” is unchanged:

> preserve the old state under cyclic interpolation, then take the square root whose normalized finite rotation distance is exactly half of the old state's distance.

## 8. Half-turn tie occurs only once the half-turn exists

If `N` is even, the coarse half-turn is

\[
r^{N/2}.
\]

Its two fine square roots have equal distance to identity and both are retained.

For the initial `C3` layer, `N=3` is odd and no half-turn exists.

The first refinement `C3 -> C6` **creates** the half-turn `q^3`.

The second refinement `C6 -> C12` is therefore the first stage at which the half-turn root relation produces the two quarter-turn sheets.

This gives the correct precision chronology:

```text
C3: current positive-ray cycle, no half-turn
    -> interpolate each coarse step
C6: half-turn first appears
    -> root the half-turn
C12: two quarter-turn roots appear
    -> repeated identity-near square-root interpolation
C24 -> C48 -> ...
```

## 9. Correct minimal finite refinement clauses

Inside the directed cyclic-interpolation architecture, the required clauses are:

1. **STATE RETENTION / INDEX TWO:** old `C_N` states embed as an index-two subgroup of the fine state system;
2. **EQUAL STEP SPLITTING:** a fine generator `q` satisfies `q^2=iota(r)`, so every old rotation step is exactly two identical fine steps;
3. **IDENTITY-DIRECTED ROOT:** for state refinement, retain the square root(s) of minimum fine Cayley distance to identity, equivalently exact normalized-distance halving;
4. **INVERSION-SAFE TIES:** if the two minimum roots tie, retain both rather than break turn-sense symmetry.

These replace the previous graph-cover clause set for the current directed positive-ray semantics.

## 10. Why the old holonomy-bit claim does not apply here

The prior cover model treated a fine adjacent step as projecting to one coarse adjacent step. For a two-sheeted cover of a cycle this indeed carries a `C2` monodromy/holonomy bit distinguishing a connected `C_(2N)` cover from two disconnected `C_N` sheets.

That is valid graph-cover mathematics.

But it answers a different refinement question.

In the current native directed-ray setting, one coarse step must be represented by **two** fine steps, not by one. The old states are an embedded even subgroup rather than the quotient vertices of a covering projection that preserves adjacency one-for-one.

Therefore:

\[
\boxed{
C_2\text{ COVER HOLONOMY IS NOT THE MISSING DATUM FOR THE CURRENT DIRECTED }C_3\to C_6\text{ REFINEMENT.}
}
\]

The missing datum is instead the existence of a homogeneous fine generator square root `q` of the coarse generator `r`.

## 11. Completion typing correction

The direct character inclusions

\[
\mu_N\subset\mu_{2N}
\]

remain correct and correspond exactly to the state-retaining embeddings above.

Their union across dyadic refinement is

\[
C_3\times C_{2^\infty}
\]

and is dense in the analytic `U(1)` character completion.

The previously described inverse-limit `C3 x Z_2` belongs to the alternative coarse-graining/squaring projection system. It may remain mathematically useful as a root-ancestry/profinite address construction, but it is **not** the primary current-directed-ray state-refinement semantics.

Freeze correction:

`DIRECT STATE REFINEMENT = DIRECT LIMIT / CYCLIC INTERPOLATION SIDE`.

`PROFINITE COVER ADDRESS = SEPARATE ALTERNATIVE/ANCESTRY TYPING`.

## 12. G0 residual after correction

The remaining native question is now cleaner:

> does actual fixed-radius Enterprise Cell rotation admit a finite orientation quotient whose current coarse `C3` ray transition has a homogeneous square-root transition `q`, so that one coarse rotation step splits into two equal fine transitions while old states are retained?

Current P000/Q29 does not allow this to be assumed uniquely.

If such a generator-root/interpolation theorem is supplied, the already-proved shortest-root/distance-halving mechanism forces the subsequent Viète refinement at G1 strength.

## 13. Current corrected verdict

The following #1158 results survive unchanged:

- target-free nested radical recursion;
- two-sheeted quarter-turn seed at `C12`;
- shortest-root normalized-distance halving;
- gate readout and intrinsic completion constant;
- target-free brackets/error quartering;
- Viète–Wallis–AGM internal completion equality;
- algebraic-degree/state-complexity theorems.

The specific earlier claim that current directed `C3 -> C6` refinement is selected by a nontrivial binary graph-cover holonomy bit is superseded.

The correct state-refinement primitive is:

\[
\boxed{
\text{retain old states and adjoin a homogeneous generator square root }q\text{ with }q^2=r.
}
\]
