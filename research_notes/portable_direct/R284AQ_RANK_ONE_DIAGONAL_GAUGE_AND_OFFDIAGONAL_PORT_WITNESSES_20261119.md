# R284AQ — Rank-one diagonal-observer gauge, off-diagonal Port witnesses, and a minimal repair graph

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AP (primewise modular principal-rank closure), R284AN (intrinsic-rank compression), R284AG–AH (SCC and signed principal-minor observer).
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The project P000 and ACTIVE six-axis/three-dimensional-slice worldview are unchanged.
Scope: a finite rational **auxiliary named-Port matrix observer**, not a proposed native X6 time evolution or an unqualified BRC state quotient. The matrices below are observer-channel indices, not native spatial axes.

## AQ1. Complete rank-one classification for diagonal Port edits

Let `m≥2`, `a,b∈(Q\\{0})^m` (in particular all entries may be strictly positive), `C=ab^T`, `c_i=a_i b_i`, and `D=diag(d_1,...,d_m)` with independently named commuting indeterminates `d_i`. Define the diagonal observer

`F_C(d)=det(D-C)`.

**Theorem AQ1.** In `Q[d_1,...,d_m]`,

`F_C(d)=∏_i d_i − ∑_i c_i ∏_{j≠i}d_j.`                                    (AQ1)

Thus two everywhere-nonzero rank-one matrices `C=ab^T` and `C'=a'b'^T` have **identical full diagonal-edit determinant polynomials** iff their diagonal entries coincide, `a_i b_i=a'_i b'_i` for all `i`. In that case, there exists an invertible diagonal gauge `S=diag(λ_i)` such that

`C'=S C S^{-1}`, where `λ_i=a'_i/a_i`.                                 (AQ2)

*Proof.* For invertible formal `D`, the rank-one determinant lemma gives `det(D-ab^T)=det(D)(1-b^T D^{-1}a)`. Clearing denominators produces (AQ1) as a polynomial identity, valid at zero `d_i` as well. The coefficient of the monomial missing exactly `d_i` is `−c_i`, giving necessity and sufficiency. With `λ_i=a'_i/a_i`, the common diagonal imposes `b'_i=b_i/λ_i`, proving (AQ2). Conversely a diagonal similarity preserves every principal minor and the entire diagonal polynomial.

This is the complete rank-one fibre of the **declared diagonal observer**; it does not classify larger-rank principal-minor fibres.

## AQ2. Exact response to one extra directed Port edit

For `u≠v` and a new named edit `s`, define

`G_{uv,C}(d,s)=det(D-C-s E_{uv})`.

**Theorem AQ2.** The exact joint response is

`G_{uv,C}(d,s)=F_C(d) − s C_{vu} ∏_{i∉{u,v}}d_i.`                    (AQ3)

In particular at `d_i=1`,

`G_{uv,C}(1,s)-F_C(1)=-s C_{vu}`,                                   (AQ4)

so one additional directed edit `E_{uv}` reads one previously invisible off-diagonal matrix entry `C_{vu}` exactly. This one-edit response is affine in `s`, and `s=1` can be used algebraically; small positive `s` can be chosen when maintaining an auxiliary nonnegative substochastic Port realization.

*Proof.* Apply the rank-two determinant lemma to
`D-[a,se_u][b,e_v]^T`. The reduced determinant is

`det [[1-Σ_i c_i/d_i, -s b_u/d_u],[-a_v/d_v,1-sδ_{uv}/d_u]]`.

Because `u≠v`, its `δ` term vanishes and its cross term is `−s a_v b_u/(d_u d_v)`. Multiplying by `det D` proves (AQ3) and then (AQ4) as polynomial identities.

**Explicit strictly positive stable counterexample.** Let `ε=1/100` and

`C=ε[[1,2],[3,6]]`,  `C'=ε[[1,1],[6,6]]`.

Both are rank one, strictly positive, and every row sum is below 1. Their full diagonal responses coincide:

`F_C(d_1,d_2)=F_{C'}(d_1,d_2)=d_1d_2−ε d_2−6ε d_1.`

Nevertheless, at `D=I` and `s=ε` for edit `E_{21}`,

`det(I-C-εE_{21})=4649/5000`,
`det(I-C'-εE_{21})=9299/10000`;

their difference is `−1/10000` (checked exactly). Thus full agreement on *all* named diagonal determinant observations, even with positivity, stability and intrinsic rank one, does not license discarding the off-diagonal relation when the future observer adds that named edit. This is an exact observer-relative residual witness.

## AQ3. Which non-diagonal edit sets fully repair the loss?

Let `H⊆{(u,v):u,v∈[m],u≠v}` be the collection of allowed directed single-entry interventions `E_{uv}`. Observe the full diagonal polynomial and the `G_{uv,C}` for all `(u,v)∈H`; equivalently, measure the differences in (AQ4) at `d=1,s=1`. Let `Γ(H)` be the **undirected** graph obtained by forgetting the orientations of the probed edges.

**Theorem AQ3 (complete rank-one observable fibre).** For all-nonzero rational rank-one factors, `C,C'` produce the same declared observations iff

`C'=S C S^{-1}`, with `λ_v=λ_u` along every probed edge `(u,v)∈H`.    (AQ5)

Equivalently, the gauge `λ` is constant on each connected component of `Γ(H)`. Therefore:

1. The observations determine the full matrix `C` uniquely **iff `Γ(H)` is connected**.
2. For `h` components, there remain `h−1` independent relative component gauges after quotienting the irrelevant common scale; within the positive family these vary over positive rational values.
3. A spanning tree's `m−1` directed single-entry probes suffice, and fewer than `m−1` such probes cannot universally determine a strictly positive rational rank-one `C` from diagonal responses. This lower bound applies to this declared single-entry measurement model, even when edge choices are adaptive.

*Proof.* AQ1 gives the diagonal gauge. AQ3 says equality of the probed response coefficients is exactly `C_{vu}=C'_{vu}`. Since `C_{vu}=a_v b_u≠0`, using (AQ2) this condition is `λ_v/λ_u=1`. Thus connected components are exactly the residual gauge components, proving (AQ5) and 1–2. For constructive recovery along an oriented edge `u→v`, measure `C_{vu}` from (AQ4) and compute `a_v/a_u=C_{vu}/c_u`. Starting at a root with chosen `a_root=1`, traverse an undirected spanning tree (reverse the ratio when traversing the edge in reverse); put `b_i=c_i/a_i`. This recovers `C` exactly. A graph with fewer than `m−1` edges is disconnected; unequal positive rational component scales preserve all its measurements yet change cross-component matrix entries. This also proves the adaptive-probe lower bound since the realized graph still has fewer than `m−1` edges.

**Observer-safe quotient boundary.** Under diagonal determinant edits alone, the gauge fibre is unobservable. A declared off-diagonal edit edge refines the quotient by equating the corresponding gauge components. A connected measurement graph removes this rank-one gauge ambiguity. This says nothing about preserving BRC path multiplicity or branch provenance not present in the matrix `C`; those demand their own typed observation maps.

## Reproducible exact checks

Companions in this folder:
- `R284AQ_rankone_observer_gauge_checker.py` — Python 3 standard library, integer/rational exact determinant, fixed seed 28401711.
- `R284AQ_exact_verification.json` — actual output of the script.

100 positive rational rank-one cases (`m=2,...,6`, 20 per size), each with an independently chosen positive diagonal gauge, were checked. PASS: 100 diagonal identities; 200 off-diagonal response identities; 100 spanning-path reconstruction checks; 100 disconnected-gauge ambiguity checks; 60 independent Leibniz determinant comparisons for `m≤4`; and the explicit stable `2×2` distinguishing pair above. These are finite regression tests; AQ1–AQ3 are proved for every permitted rank-one rational input by the displayed identities and graph argument.

## Next science

(A) Investigate the higher-rank observer fibre: diagonal principal-minor data are invariant under diagonal similarity, but for rank≥2 additional nongauge ambiguities may exist. Find the smallest exact strictly positive counterexample or a classified subclass.
(B) Generalize minimal intervention graph recovery to rank `k>1` and to typed BRC path-sensitive observations; distinguish recovery of matrix entries from recovery of branch provenance.
(C) Compare the cost of maintaining a gauge-aware rank-one certificate against R284AP primewise exterior-span closure, including construction, probe, and verification costs on matched inputs.

Control/publication: independent portable mathematical note. No formal CLAIM, native Result, independent Review or P000 promotion is asserted; the existing frozen scientific pin is unchanged.
