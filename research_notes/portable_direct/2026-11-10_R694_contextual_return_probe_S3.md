# R694 — Controlled future S₃ return probes distinguish source laws hidden by homogeneous BRC traces

Date: 2026-11-10. Status: AUTHOR-DERIVED / EXACT-COMPUTATION-CHECKED / UNREVIEWED / NOT ADMITTED.
Mother: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Researcher EM-X6-28DBA1; activity RA-CFE8DF672084C79B3D757D94. The live task was READY/NEEDS_DISPATCH, owner taskbook/unassigned; **no CLAIM was made**.

### Scientific inputs and observer scope

Keep frozen parent-science source \`a72226e2430ffa4786321ac86e7f0c599d5f0389\` unchanged (an older source locator is DRAFT_OR_UNVERIFIED in native continuation). Reuse verified R692C E* candidate at \`3dacca5010104893d96301af4d61608d5a5a0879:research_notes/portable_direct/R692C_ESTAR_MASK_RETURN_EXACT.js\` (Git blob \`0c6d51f99eac5903a30770c8c393c972a68d93ad\`), derived from labelled native X6 returning squares; related independent Cell-dependent port-gate candidate PR #1985 at \`2b393a2f2df78faadf4dff69b9694742692d29d3\`. No V29/V39 permission or triadic-force dynamics are asserted.

Fix root phase a=0,1,2. Each of four direction signs has 15 labelled, four-step X6 returning squares with group-valued S₃ holonomy. Nonempty mask m in {1,...,15} enables its selected signs, with uniform measure on 15 popcount(m) labelled paths and group law μ_(a,m). One macro returns to the chosen Cell and phase while updating the S₃ frame. This study expands R693's **stationary, repeated-mask** return observation to an experiment in which the next macro may use an independently chosen direction mask λ. The observation is complete-frame return to identity after one or two macros.

For arbitrary group probability measures:
\[
r_1(\mu)=\mu(e),\qquad
r_2(\mu,\nu)=(\mu*\nu)(e)=\sum_{g\in S_3}\mu(g)\nu(g^{-1}).
\]
This is a typed BRC convolution pairing. R693's three spectral invariants (s,t,d) determine all **homogeneous** return probabilities μ^{*k}(e), but a controlled future mask changes the scope of the observer.

### Theorem A: exact counterexample to homogeneous-return congruence

For a=0, write e=012, τ=021, c=120, c²=201. Masks m=2 and m'=5 give
\[
\mu_2=(6e+6\tau+3c)/15,\quad
\mu_5=(6e+6\tau+3c^2)/15.
\]
Conjugation by τ fixes e and τ and swaps c,c². Hence \(\mu_2^{*k}(e)=\mu_5^{*k}(e)\) for **every k≥0**, including equality of the complete R693 spectral triple. Choose continuation λ=4, whose law is \(\mu_4=(6e+3\tau+6c^2)/15\). Since \(c^{-1}=c^2\), exact counting yields
\[
r_2(\mu_2,\mu_4)=\frac{6\cdot6+6\cdot3+3\cdot6}{225}=\frac8{25},\quad
r_2(\mu_5,\mu_4)=\frac{6\cdot6+6\cdot3}{225}=\frac6{25}.
\]
**Difference = 2/25.** An all-horizon homogeneous-return quotient is not automatically a congruence for heterogeneous future actions. This concrete information-loss witness applies within the E* candidate model, not as a theorem about live native V29 behavior.

### Theorem B: one fixed continuation mask resolves every full group-kernel class in this finite menu

For a fixed root phase, choose **the same λ=3** as second macro for any first mask m. Set
\[
\Phi_a(m)=\bigl(r_1(\mu_{a,m}),\,r_2(\mu_{a,m},\mu_{a,3})\bigr).
\]
Then, for any m,m' in {1,...,15},
\[
\boxed{\Phi_a(m)=\Phi_a(m')\iff\mu_{a,m}=\mu_{a,m'}.}
\]
The full-law (equivalently fixed-probe) class counts for a=0,1,2 are **13,13,9**. For a=0, r1=2/5 for all 15 masks, so the **single two-macro return scalar** distinguishes all 13 different S₃ laws. For a=2, r1 alone already distinguishes all nine laws. Complete duplicate-mask classes: a=0,1 have {6,9,15}; a=2 additionally has {2,5,7}, {4,10,14}. For comparison, R692c's *homogeneous-return* class counts are 12,12,9.

**Algebraic proof and finite completion.** Write m_j∈{0,1}, k=Σm_j>0. The four immutable R692C integer kernels give at a=0:
\[
r_1=2/5,\qquad
r_2(\mu_{0,m},\mu_{0,3})=
\frac{23m_0+18m_1+15m_2+10m_3}{50k}.
\]
Among the 15 nonempty subsets of {23,18,15,10}, their means coincide only for masks {6,9,15}, which all have mean 33/2. These masks also have identical full laws because \(n_{0,0}+n_{0,3}=n_{0,1}+n_{0,2}\) exactly.

At a=1,
\[
r_1=\frac{2m_0+3m_1+4m_2+5m_3}{5k},\qquad
r_2(\mu_{1,m},\mu_{1,3})=
\frac{16m_0+17m_1+24m_2+25m_3}{50k}.
\]
Exact enumeration of all 15 subset pairs gives the sole collision {6,9,15}, again identical full group laws. At a=2 all kernels lie in C₂={e,τ}; their full laws are determined by r1, with nine distinct values. The attached executed exact checker verifies all \(3\cdot15^2=675\) ordered mask pairs for this iff and another 675 for separation by four single-direction continuation probes, as well as the 8/25 versus 6/25 witness and 12 homogeneous powers. It returned \`R694_ALL_EXACT_ASSERTIONS_PASS\`. The accompanying result JSON contains all rational signatures.

### Observer memory, provenance, and next unit

Under externally chosen nonstationary mask schedules, exactly 13/13/9 classes of initial masks are future-equivalent for **S₃ return-only** observation. Within each phase the worst-case fixed-length binary encoding remains 4 bits: the equivalence becomes finer at a=0,1 but its bit ceiling does not change. A full labelled-source admission observer may distinguish masks with identical group kernels and requires a different quotient (R692's 60-bit source vector in its separate Cell-gating model). The finite 15-mask probe theorem is **not** an injectivity claim on the continuous simplex of all S₃ probability measures.

Reuse: \`REUSE_APPLIED\` R692C original positive labelled BRC kernels; \`COMPOSE_APPLIED\` R693 spectral-return theory and the R692 static-port observer boundary. General finite-group convolution is established mathematics; the novel contribution here is the exact source-menu contextual certificate and its minimal distinguishing probe.

Next: replace externally chosen masks with **actual frozen** Link/Port permissions and V29 PASS/TRANSFER plus V39 event-update rules. Test whether the above pair of context kernels can be produced by legal source-preserving native updates, then construct the minimal controller/port repair coordinate or prove a stronger native-preserving quotient. Keep the parent primitive triad Cell/path closure and rotation-covariance target open. No Result, Driver review or Foundation/Working Truth admission is asserted.
