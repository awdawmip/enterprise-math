# Viète C3 -> C6 bridge: the connected six-gate refinement is exactly one nontrivial C2 holonomy bit

Status: `FREE_RESEARCH / EXACT BINARY-COVER HOLONOMY CLASSIFICATION + LOCALITY NO-GO / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parents:
- `research_notes/VIETE_BINARY_CYCLE_COVERS_2ADIC_VS_ANALYTIC_COMPLETION_20260903.md`
- `research_notes/VIETE_MINIMAL_FINITE_REFINEMENT_EXTENSION_CLASSIFICATION_20260903.md`

## 1. Question

The finite refinement classification identified `CONNECTED_BINARY_ORIENTATION_REFINEMENT` as one of the exact extra clauses needed to force the Viète gate tower.

This note asks what information connectedness actually adds over a local two-sheeted refinement of the current `C3` ray cycle.

Answer: exactly one global `C2` monodromy/holonomy bit around the coarse cycle.

## 2. Binary sheet transport on an N-cycle

Let the coarse orientation graph be the cycle

\[
\Gamma_N
\]

with vertices

\[
v_0,v_1,\ldots,v_{N-1}
\]

and cyclic edges

\[
e_i:v_i\to v_{i+1}.
\]

Give each coarse vertex a two-element sheet fiber

\[
\{0,1\}\cong\mathbf F_2.
\]

A local lift of the coarse edge `e_i` transports the sheet by

\[
b\mapsto b+\alpha_i,
\qquad
\alpha_i\in\mathbf F_2.
\]

Thus the entire binary cover is encoded by an edge cochain

\[
\alpha=(\alpha_0,\ldots,\alpha_{N-1})\in\mathbf F_2^N.
\]

Every local edge neighborhood is still a two-sheeted lift regardless of the values of the `alpha_i`.

## 3. Vertex gauge and the invariant loop bit

Relabel the two sheets independently at each coarse vertex by

\[
b\mapsto b+\lambda_i,
\qquad
\lambda_i\in\mathbf F_2.
\]

Then the edge labels transform as

\[
\alpha_i
\mapsto
\alpha_i+\lambda_i+\lambda_{i+1}.
\]

This is the ordinary `C2` vertex-gauge/coboundary transformation.

The total loop parity

\[
\boxed{
h(\alpha):=\sum_{i=0}^{N-1}\alpha_i\pmod2}
\]

is gauge-invariant, because every `lambda_i` appears twice in the sum.

For a single cycle this is the only gauge-invariant binary datum. Equivalently, the two isomorphism classes are indexed by

\[
H^1(\Gamma_N;\mathbf F_2)\cong\mathbf F_2.
\]

No historical novelty is claimed for this standard graph-cover/cohomology fact.

## 4. Holonomy zero gives two disconnected sheets

If

\[
h(\alpha)=0,
\]

then `alpha` is gauge-equivalent to the all-zero edge assignment.

In that gauge every coarse edge preserves the sheet:

\[
(v_i,b)\to(v_{i+1},b).
\]

Therefore the refined graph is

\[
\boxed{
\Gamma_N\sqcup\Gamma_N.
}
\]

A complete coarse turn returns to the same sheet.

For `N=3`, this is two disconnected three-state cycles.

## 5. Holonomy one gives the connected double cycle

If

\[
h(\alpha)=1,
\]

then `alpha` is gauge-equivalent to a form with exactly one twisted edge.

A complete coarse turn flips the sheet:

\[
b\mapsto b+1.
\]

Hence one must make two coarse turns before returning to the original fine state. The lifted graph is one connected cycle of length `2N`:

\[
\boxed{
\Gamma_{2N}.
}
\]

For `N=3`:

\[
\boxed{
h=1\Longleftrightarrow C_6.}
\]

Thus the connected six-gate shell is exactly the nontrivial binary holonomy class over the current three-ray cycle.

## 6. The minimal global information added by C3 -> C6

The local data

- three coarse ray states;
- two fine representatives over each ray;
- locally bijective edge transport;

is identical in the trivial and nontrivial covers.

The only difference is what happens after a complete loop:

\[
\boxed{
\text{same sheet after one C3 loop}\quad\text{versus}\quad\text{opposite sheet after one C3 loop}.
}
\]

Therefore the connected `C6` refinement adds exactly one global bit:

\[
\boxed{
\text{C3 -> C6 CONNECTEDNESS DATA}=\text{NONTRIVIAL }C_2\text{ HOLONOMY }h=1.
}
\]

This is more precise than saying merely that “connectedness is an extra assumption.”

## 7. Locality no-go

Any rule that inspects only one coarse vertex, one binary fiber, or one lifted edge has the same local view in the `h=0` and `h=1` covers.

Therefore:

\[
\boxed{
\text{no strictly local Cell/ray-fiber rule can distinguish the connected C6 cover from two disconnected C3 sheets.}
}
\]

To select the six-gate connected refinement, one needs loop-transport information or an equivalent global connectedness/holonomy principle.

This is an exact information boundary: more detailed local geometry is not sufficient unless it is assembled into a complete-loop transport invariant.

## 8. Relation to the rotation orientation variable epsilon

Current Cell-rotation semantics already requires a two-state local sweep/orientation datum `epsilon`.

That local `C2` torsor is not by itself the global holonomy bit `h`.

They have different types:

- `epsilon` — local orientation/sweep state carried by a rotating segment;
- `h` — global monodromy of the binary refinement bundle around the coarse orientation cycle.

A theory may possess local `epsilon` states while still choosing either trivial or nontrivial global sheet transport.

Therefore

\[
\boxed{\epsilon\text{ does not automatically imply }h=1.}
\]

This separates local chirality from global six-gate connectivity.

## 9. Iterated binary refinement

At every later level

\[
C_N\leftarrow C_{2N}
\]

the same classification applies: a two-sheeted local refinement over the coarse cycle has a `C2` loop-holonomy bit.

Demanding one connected cycle at every resolution level is equivalent to requiring the nontrivial holonomy class

\[
h_m=1
\]

at every binary refinement stage.

Thus the connected dyadic Viète tower may be typed as a sequence of nontrivial binary cycle-cover classes.

The principle

`CONNECTED_BINARY_ORIENTATION_REFINEMENT`

is exactly the policy

\[
\boxed{h_m=1\text{ at every refinement level}.}
\]

## 10. Precision significance

The nontrivial first holonomy bit produces

\[
C_3\to C_6,
\]

where the six-state shell first contains a half-cycle/deck phase.

The next nontrivial binary cover

\[
C_6\to C_{12}
\]

lifts that half-turn into the two quarter-turn roots, after which normalized-distance halving generates the Viète tower.

Therefore the first genuinely global precision datum is not a real angle. It is a binary loop-monodromy class.

## 11. Native boundary sharpened

Current three-axis Foundation supplies the coarse cyclic ray structure and current rotation semantics supplies local sweep orientation, but neither alone fixes the global binary holonomy of a refinement cover.

Hence the remaining G0 lift problem has two separable missing ingredients:

1. **global topological/refinement datum:** nontrivial `C2` holonomy `h=1` selecting the connected binary cover;
2. **refinement dynamics:** normalized cycle-distance halving selecting the identity-near fine lift, with inversion-safe tie retention.

This is a sharper necessity decomposition than a generic “derive C6 from Cell geometry” requirement.

## 12. Current #1158 residual

At free-research theorem strength, the first missing native/global datum for the six-gate refinement is exactly one `C2` monodromy bit around the coarse `C3` orientation cycle.

Whether actual Enterprise Cell rotation canonically supplies `h=1` remains open. If it does not, both the connected and disconnected binary refinements remain locally compatible and the six-gate tower cannot be promoted to G0 merely from local Cell state data.
