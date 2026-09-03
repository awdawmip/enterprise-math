# Viète C3 -> C6 graph-cover holonomy model — alternative model only

Status: `SUPERSEDED_FOR_CURRENT_DIRECTED_C3_REFINEMENT / ALTERNATIVE_GRAPH_COVER_MODEL_ONLY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Current correction authority: `research_notes/VIETE_DIRECTED_C3_CYCLIC_INTERPOLATION_CORRECTION_20260903.md`
Correction commit: `9d82f77052a41a3c55a590cb55fb851c4c0292ab`

## Current ruling

The mathematics formerly recorded here classifies ordinary two-sheeted **graph covers** of a cycle by a `C2` loop-holonomy bit. That graph-cover theorem is standard and remains mathematically valid in its own model class.

It is **not** the correct primary refinement semantics for the current Enterprise three-positive-ray `C3` orientation quotient.

Current native/G1 directed-ray refinement must retain the three old directed ray states and split one old coarse transition into two equal finer transitions. Therefore the active refinement is the index-two cyclic interpolation

\[
\boxed{
\iota_N:C_N\hookrightarrow C_{2N},
\qquad
\iota_N(r)=q^2.
}
\]

For `C3 -> C6`, the old states are the even powers

\[
1,q^2,q^4,
\]

and the new interpolating states are

\[
q,q^3,q^5.
\]

The half-turn `q^3` first appears at `C6`. The next interpolation `C6 -> C12` embeds that half-turn as `Q^6`, whose two square roots are `Q^3` and `Q^9`.

Thus the earlier statement

`CURRENT C3 -> C6 REQUIRES NONTRIVIAL C2 COVER HOLONOMY`

is retracted for current directed positive-ray semantics.

Freeze correction:

`C2_GRAPH_COVER_HOLONOMY != CURRENT_DIRECTED_CYCLIC_INTERPOLATION_DATUM`.

## Alternative graph-cover theorem retained for provenance

If one instead studies a different architecture in which:

- every coarse cycle vertex has a two-point fiber;
- every **single fine edge** projects locally to one coarse edge;
- the refinement is an ordinary two-sheeted graph cover,

then edge flips `alpha_e in F_2` have gauge-invariant loop parity

\[
h=\sum_e\alpha_e\pmod2.
\]

For a single cycle:

\[
h=0
\Longleftrightarrow
\Gamma_N\sqcup\Gamma_N,
\]

while

\[
h=1
\Longleftrightarrow
\Gamma_{2N}.
\]

Equivalently the two cover classes are indexed by

\[
H^1(\Gamma_N;\mathbf F_2)\cong\mathbf F_2.
\]

This is useful as a separate graph-cover/monodromy model, but it answers a different question from the current directed state-retaining precision refinement.

## Why the model mismatches current C3 rays

In the graph-cover model, one fine adjacent step projects to one coarse adjacent step. Consequently, after traversing the three coarse edges of `C3`, the connected six-cycle cover lands on the opposite fine sheet rather than the initial fine state.

For current directed positive rays, one complete coarse `C3` turn must remain one complete turn after refinement. The correct relation is instead:

\[
\text{one coarse step}=\text{two fine steps}.
\]

That is exactly what

\[
r\mapsto q^2
\]

implements.

## Current #1158 residual

The missing G0 datum is **not** a `C2` holonomy bit. The corrected native question is:

> Does actual fixed-radius Enterprise Cell rotation admit a homogeneous fine generator `q` whose square is the coarse `C3` rotation generator `r`, with old states retained, so that every coarse transition splits into two equal finer transitions?

If such a state-retaining generator-root interpolation exists, the already-proved identity-directed shortest-root rule yields exact normalized-distance halving and the Viète nested-radical refinement.

The original full graph-cover analysis remains recoverable in Git history at commit `d22d80cc8a954188fd784bd8a7fe892dac61295e`.