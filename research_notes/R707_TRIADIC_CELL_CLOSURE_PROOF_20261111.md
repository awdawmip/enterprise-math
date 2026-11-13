# R707 — Canonical equal-quantum X6 triad event and decomposition polynomial

Date 2026-11-11 Asia/Shanghai. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142; frozen scientific base @a72226e2430ffa4786321ac86e7f0c599d5f0389. Author-side construction, not an accepted native dynamical completion.

## Cell-attached primitive model

Let c be an arbitrary Cell in the affine signed native Z^6 torsor, q>0 a rational force quantum, and define a primitive single-axis force token (id,c,i,σ,q,provenance), where i∈{0,...,5}, σ∈{±1}, and id is distinct even among otherwise equal tokens. Tokens are force incidences **at c**, not spatial steps away from c. A *candidate canonical equal-quantum triad* T consists of three different tokens at the same c,q whose native axes are pairwise distinct, hence pairwise PERP_E with P000 native right angle 120°. Define C_eq(c,T)=true for such a triple. AddTriad/RemoveTriad adds/removes the whole triple atomically, retaining token IDs and the triadic branch provenance. These are explicitly candidate events pending V29 PASS/TRANSFER and V39 loop-flow compatibility. No classical Euclidean force-vector-sum-zero is used. There are C(6,3)*2^3=160 unordered signed-axis triad choices and 3!=6 labeled source-order refinements per choice, total 960 ordered source refinements. Their similarity in count to R704 spatial three-step endpoints does not identify the objects.

## Labeled decomposition theorem

Let F be a finite multiset of individually **labeled** tokens at c, all with common q. Let n_i count the tokens on native axis i (token signs remain on tokens), and Σ_i n_i=3m. A canonical decomposition is an **unordered partition** of all 3m tokens into m triples, each triple choosing three distinct axes; all triples are admitted by the above C_eq candidate. Set H(x_0,...,x_5)=Σ_{0≤i<j<k<6} x_i*x_j*x_k.

**Theorem R707.** The exact number of canonical triadic decompositions of the labeled population is

D(n_0,...,n_5) = (∏_i n_i! / m!) [x_0^{n_0}...x_5^{n_5}] H(x)^m.

D is an integer. If some n_i>m then D=0. The expression is covariant under S6 relabeling of axes and independent of a global Cell origin.

**Proof.** Temporarily order and label m triad slots. The coefficient of x^n in H^m counts ordered axis triples assigned to those slots with total axis multiplicity vector n; each triple has distinct axes by construction. For a fixed ordered axis-slot pattern, the n_i distinct tokens on axis i may be bijectively assigned to its n_i occurrences in n_i! ways, independently across i. The number of labeled-slot realizations is therefore coefficient*∏ n_i!. Every unlabeled set partition into triads has exactly m! possible orderings of its m distinct triads, so divide by m!. This is a bijection and also proves integrality. Permuting variables x_i together with token axis labels preserves H, proving S6 covariance. QED.

**Corollary 1 (unbounded exact family).** For n=(m,m,m,0,0,0), only monomial (x_0*x_1*x_2)^m contributes, yielding D=(m!)^3/m!=(m!)^2 for every integer m≥0. With two labeled tokens on each of three axes, there are four decompositions. With one labeled token on each of all six axes, [x_0...x_5]H²=C(6,3)=20 and D=20/2=10 decompositions. Equal total force count N=6 does not preserve BRC decomposition branch multiplicity (4 vs 10). Positivity of branch count is not signed-force cancellation.

**Corollary 2 (explicit apparent two-force lift).** Fix two distinct signed native-axis tokens at c of equal quantum q. The hidden third signed axis has exactly 4 other axis choices and 2 signs, so there are exactly 8 labeled hidden third-axis choices making a candidate canonical equal-quantum primitive triad, or 8*6=48 source-order refinements. The observer that hides the third token reads an apparent pair; each lift remains a **three-force** primitive event. If the two visible tokens occupy the same native axis, no candidate canonical distinct-axis triad contains both; this is a precise subfamily obstruction, not a statement about later general TRIADIC_CLOSURE_E laws. The eight third-axis branches must retain provenance until a typed observer-safe quotient is proved.

## Exact validation and scientific boundaries

The included Python checker independently computes D(n) from a coefficient recursion and from recursive labeled-token set-partition enumeration (fix one first-axis token, choose partners on two distinct other axes). They agree on all 242 vectors n_i∈{0,1,2}, Σn_i≤9 divisible by 3. It checks family n=(m,m,m,0,0,0) for m=1,...,6, the two six-token examples, 720 permutations for each of three representative profiles, and 8 third signed choices for each distinct visible-axis pair. Marker R707_X6_CELL_TRIAD_COEFFICIENT_EXACT_PASS. Analytical formula and family extend beyond the finite check by the bijective proof.

Source BRC use: labeled decomposition multiplicity and hidden-source lift, positive integer/rational branch measures; no signed/amplitude identification. Exact primitive and rotation semantics used: P000 equal-quantum triads have PERP_E distinct axes and native 120°; translation and S6 axis-permutation skeleton covariance. Actual native V29/V39 event permission, full rotation-generator mapping and whether the candidate C_eq is a complete TRIADIC_CLOSURE_E remain specific unresolved bridge problems.

Next: at immutable science pin locate actual X6 Cell/Link/Port, V29 PASS/TRANSFER, V39 j-flow and active rotation-generator source; construct one legal Cell-attached AddTriad and conservation ledger, test two-force projected readout and source-preserving multiple decompositions. This construction does not require forcing a spatial three-step return, since its three forces act on the same Cell atomically.