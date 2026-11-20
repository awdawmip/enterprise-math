# X6 R47 — Blind-source BRC tomography: simultaneous Port-count and unordered source-weight identification

Date: 2026-11-20 (Asia/Shanghai). Research continuation: R44 → R45 → R46 → R47. Topic: RS-X6-NATIVE-TIME-DYNAMICS.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_COMBINATORIAL_DERIVATION / TWO_IMPLEMENTATION_FINITE_CHECK / NOT_INDEPENDENTLY_REVIEWED.
Classification: independent portable research on the R44 candidate law, not a P000-native event admission, CLAIM, formal PROGRESS or Result.

## Exact carrier and observation

Fix an integer p≥1, two *named, once-only, whole-triad* sources A,B, and p named Ports indexed 0,...,p−1. Source A_i or B_i uses its Port once. Port 0 competes for one shared X6 Cell. The public event R clears occupied Cell; a once-only conditional event T reoccupies according to the previously chosen Port, precisely as in the frozen conditional R44 transition grammar. Source names and Port indices remain in the underlying BRC path population. The coarse observer projects A_i,B_i to F and leaves R,T distinct. Assign fixed positive real weights α to each A_i and β to each B_i; R,T weigh 1. For a coarse word w, Z(w) is the exact sum of products of weights over all successful named serial histories projecting to w, starting at the both-unused state U. Empty word has mass 1. No probability normalization or signed cancellation occurs.

The unknown physical parameters to reconstruct are p and α,β. Their *source labels* are hidden by the instrument. P000 remains frozen at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, including the six signed native axes, chart-relative Cell anchors, indivisible triadic closure, and ordered time; R and T remain conditional research operations, not established native TRIADIC_CLOSURE_E updates.

## R47.1 — Three exact short-word coefficients identify p and the unordered weights

Set X=Z(F), Y=Z(FT), D=Z(FF), H=Z(FRF). In the R44 grammar, for every integer p≥1 and every α,β>0,

\[
\boxed{
X=p(\alpha+\beta),\quad
Y=(p-1)(\alpha+\beta),\quad
D=2(p^2-1)\alpha\beta,\quad
H=2p\alpha\beta.
}
\]

It follows that the Port count and the *unordered multiset* of source weights are uniquely determined:

\[
\boxed{
S=X-Y=\alpha+\beta>0,\qquad
p=\frac{X}{X-Y},\qquad
P=\alpha\beta=
\begin{cases}
H/2,&p=1,\\
D/[2(p^2-1)],&p\ge2.
\end{cases}
}
\]

The unordered pair {α,β} is the set of roots of t²−St+P=0. The required observation horizon is at most three events. For p≥2 the three coefficients (X,Y,D), all with event lengths ≤2, suffice; for p=1 use (X,Y,H) with length ≤3.

**Proof.** A one-letter F transfer may come from either source at any of its p Ports, giving X=p(α+β). For FT, the following T is immediately enabled exactly when the first Port was nonzero: the first transfer then leaves the shared target free, exactly one source used and T unspent. That gives p−1 choices from each source, hence Y=(p−1)(α+β). For FF, the two successive transfers must use different sources. Every ordered pair of chosen Ports is allowed except (0,0), since the first Port 0 transfer occupies the target. There are p²−1 choices for each source order, giving D=2(p²−1)αβ. For FRF, R must follow a first Port 0 transfer, and then the unused source can fire at any of p Ports: 2p choices of product αβ, giving H=2pαβ. The inversion follows by subtraction and the quadratic formula; positivity ensures S,H>0. QED.

As a redundant internal exact check, D/H=(p²−1)/p=p−1/p, so the positive solution of p²−(D/H)p−1=0 independently returns the same p using the (FF,FRF) pair alone.

## R47.2 — Sharp depth and exact ambiguity

For p≥2, the observable depth-1 coefficient X alone cannot determine both source weights, but (F,FT,FF) determines p and {α,β} by depth 2. For p=1, **length 3 is necessary**: choose positive weights (1,3) and (2,2). Every word in {F,R,T}* of length at most 2 has the same root coefficient in the two models: such words use at most one F in the p=1 graph (FF is forbidden), so coefficients depend only on S=4. But Z(FRF) equals 2·3=6 and 2·4=8 respectively. Thus depth 2 is insufficient in this regime, and depth 3 is sufficient.

Swapping source names A↔B *and* weights α↔β is a weight-preserving bijection on named R44 histories. Projection to F,R,T makes paired root observations identical. Hence only the unordered pair can be reconstructed from the root source-blind observer, regardless of the horizon. This is an exact observational symmetry, not an absence of names in the hidden carrier.

## R47.3 — Unknown common transfer gain: what remains identifiable

Suppose the instrument multiplies every F transfer by an unknown common gain g>0 (R,T retain unit weight). The measured word series is exactly Z(w;gα,gβ). The same inversion identifies p and the unordered **effective** weights {gα,gβ}; therefore it identifies the unordered ratio {α/β,β/α}, but no absolute source-weight scale. Indeed (α,β,g) and (cα,cβ,g/c) have identical observations for every c>0 and every future coarse word. This gauge family is an explicit nonidentifiability certificate. It does not alter the Port-count conclusion. If the gain instead depends on source, state or time, this theorem does not assert identifiability.

The four short-word coefficients supply immediate model diagnostics: X−Y must be positive, X/(X−Y) must be a positive integer, the derived discriminant S²−4P must be nonnegative, and the redundant D/H identity must hold. A failed exact identity falsifies this particular weighted R44 observer model or its assumed calibration, not P000.

## Exact checking, provenance, limitations

Two separate local implementations were executed: a Python Fraction-valued full transition enumerator (p=1..40, five positive integer/rational weight pairs; 200 exact parameter cases), and an independent Node.js enumerator of the R44 transition grammar (p=1..30, five integer pairs; 150 exact cases). Both evaluated F,FT,FF,FRF directly by state-level weighted path propagation, checked all four identities, reconstruction, and the p=1 short-horizon witness. PASS. Universal quantification over all p and positive real weights rests on the four bijective counting arguments above, not on finite testing.

Source mapping: R44 candidate grammar in research_notes/portable_direct/x6_r44_rotation_reoccupation_brc_verify.js (blob 9e6e7f25d0f1430ab054adb298887ae42b79f1f0); R46 weighted observer in research_notes/portable_direct/2026-11-20_x6_r46_source_weight_asymmetry_provenance.md (blob a0099c378d57822c85f6908cf00b7c1cd281864c). Joint relation-preservation rule applies: the named paths and Port origins are retained in the underlying carrier; collapsing is certified only for the root exact positive-mass series with the declared events.

**Next:** test the same algebra against an actually authorized native Cell/Link/Port whole-triad transition map, or derive a finite-resolution interval certificate for (X,Y,D,H) under bounded readout error; distinguish source-specific gain from common gain. No native R/T admission, physical calibration, independent mathematical review, or formal Result is asserted.