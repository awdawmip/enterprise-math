# Viète binary graph-cover model and completion types — alternative ancestry model

Status: `PARTIALLY_SUPERSEDED / ALTERNATIVE_GRAPH_COVER_AND_ANCESTRY_MODEL / DIRECT_CHARACTER_LIMIT_RETAINED / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Current directed-state authority: `research_notes/VIETE_DIRECTED_C3_CYCLIC_INTERPOLATION_CORRECTION_20260903.md`
Correction commit: `9d82f77052a41a3c55a590cb55fb851c4c0292ab`
Original full note provenance: commit `65648369effd67d186ecf209e738cbba6a6eac1a`

## 1. Current correction

The original version treated the current directed positive-ray refinement

\[
C_3\to C_6\to C_{12}\to\cdots
\]

as a tower of ordinary connected two-sheeted graph covers.

That is not the correct primary semantics for the current directed `C3` ray cycle. The active refinement is instead **state-retaining cyclic interpolation**:

\[
\boxed{
\iota_N:C_N\hookrightarrow C_{2N},
\qquad
\iota_N(r)=q^2.
}
\]

Every old state is retained as an even power, while odd powers are inserted between old states. One coarse rotation step becomes two identical fine steps.

Therefore the graph-cover language in the original note is superseded for current directed state refinement.

## 2. What remains valid on the direct state-refinement side

The finite state groups themselves remain

\[
C_{3\cdot2^m}.
\]

The state-retaining character inclusions remain exact:

\[
\mu_{3\cdot2^m}
\subset
\mu_{3\cdot2^{m+1}}.
\]

Their direct union is

\[
\boxed{
\bigcup_m\mu_{3\cdot2^m}
\cong C_3\times C_{2^\infty},
}
\]

with `C_(2^infinity)` the Prüfer 2-group.

Under the ordinary algebraic/complex character realization, the mesh tends to zero and the direct union is dense in `U(1)`. Thus its analytic/topological closure is

\[
\boxed{U(1).}
\]

This direct-limit/character-completion statement is compatible with the corrected cyclic interpolation semantics.

## 3. The old inverse-limit C3 x Z2 statement is retyped

The original note also considered the reduction projections

\[
C_{3\cdot2^{m+1}}	o C_{3\cdot2^m}
\]

and obtained the inverse-limit address space

\[
\boxed{
C_3\times\mathbb Z_2.
}
\]

That inverse-limit calculation remains valid for the **alternative coarse-graining/root-ancestry projection system**.

It is not the primary current directed-state refinement, because the active refinement arrow goes the opposite way: old states embed into finer state spaces.

Therefore distinguish:

- `DIRECT STATE REFINEMENT`: index-two embeddings / cyclic interpolation / direct character union;
- `PROFINITE ANCESTRY ADDRESS`: reduction projections / inverse-limit `C3 x Z_2`.

Freeze correction:

\[
\boxed{
\text{DIRECT STATE REFINEMENT}\neq\text{PROFINITE ANCESTRY COMPLETION}.
}
\]

Both may be mathematically useful, but they are differently typed constructions.

## 4. Half-turn and quarter-turn chronology under the corrected model

At `C3` there is no half-turn.

Under

\[
C_3\hookrightarrow C_6,
\qquad r\mapsto q^2,
\]

the original positive rays are

\[
1,q^2,q^4,
\]

and the new interpolating states are

\[
q,q^3,q^5.
\]

The new state

\[
h=q^3
\]

is the first half-turn.

At the next interpolation

\[
C_6\hookrightarrow C_{12},
\]

`h` embeds as `Q^6`, whose two square roots are

\[
Q^3,Q^9.
\]

These are the two quarter-turn sheets. Later state-retaining interpolations preserve the two inversion-related branches and generate the Viète nested-radical trace sequence through the shortest-root rule.

## 5. Completion-type boundary retained

Even after the correction, the broader completion distinction remains important:

1. finite discrete orientation states and their direct union are not yet the continuous phase space;
2. the character-image analytic closure is a later completion;
3. a profinite ancestry/address completion, when used, is a different totally disconnected object.

Thus:

\[
\boxed{
\text{FINITE/DIRECT REFINEMENT STATE}
\neq
\text{PROFINITE ANCESTRY ADDRESS}
\neq
\text{ANALYTIC PHASE COMPLETION}.
}
\]

## 6. Current precision interpretation

The valid state-refinement picture is now:

```text
current directed C3 positive-ray cycle
    -> retain old states and insert equal intermediate states: C3 ⊂ C6
    -> half-turn first appears in C6
    -> retain states and interpolate again: C6 ⊂ C12
    -> the half-turn has two quarter-turn square roots
    -> repeated identity-near square-root interpolation
    -> algebraic character traces give Viète radicals
    -> target-free Pi_rot
    -> analytic character completion / classical compatibility
```

Each refinement doubles the finite orientation-state count and, on the Viète branch, halves normalized Cayley distance to identity.

## 7. Native boundary

Current P000 does not yet prove that actual fixed-radius Cell rotation admits this homogeneous generator-square-root interpolation. Q29 prevents assuming uniqueness.

The remaining G0 question is therefore the existence/selection of a state-retaining fine generator `q` satisfying

\[
q^2=\iota(r),
\]

plus the actual Cell-dynamical realization of identity-directed square-root refinement.

The original graph-cover analysis remains available in Git history for alternative model studies, but is not current #1158 directed-ray semantics.