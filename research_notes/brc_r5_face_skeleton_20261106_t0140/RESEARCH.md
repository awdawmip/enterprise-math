# R5: Exact 619-face lattice and behavioral one-skeleton, delta=1/4

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_COMPUTER_ASSISTED_EXACT_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother objective and immutable sources

R5 asks for a finite strictly-positive P/Q stopping tree whose full-history (FULL_HIST) and seedless time/likelihood-ratio (LR) strategies share their complete four-observer convex hull but have distinct actual real-behavior observation images. Frozen scientific pins are GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. P000 and ACTIVE Heartbeat worldview remain unchanged. This is an auxiliary typed BRC observer model, not an X6 physical or dynamics claim.

The model is exactly the previously authored delta=1/4 strictly-positive four-stage history-dependent P/Q tree in research_notes/brc_r5_quadratic_zonotope_20261106_t0112/RESEARCH.md at EM f00bca43d2c668e4bf05ff7974db140c9e0d2adf. The earlier author-side exact certificate at EM fed51a882c12831a889cd5437da5d1dc564fd673 (research_notes/brc_r5_kernel_perturbation_phase_diagram_20261106_t0047/RESEARCH_HULL.md, H_FACETS.txt, VERIFY_HULL.py) establishes H=conv O4(LR)=conv O4(FULL_HIST). H is the intersection of 80 rational halfspaces n·(720000 W) <= c, and has 82 vertices each given by a deterministic LR observation. This run reuses that earlier theorem and does not rerun its 80 full-history Bellman support checks.

At six nonterminal observation keys (root, two time-2, three time-3), the LR policy chooses stop-and-declare-Q, stop-and-declare-P or continue; at three terminal keys choose one declaration. Thus exactly 3^6*2^3=5832 deterministic profiles exist, with 806 distinct exact W=(P(error),Q(error),E_P tau,E_Q tau).

## Theorem A: exact complete face vector

Conditional on the established H identity, the full four-dimensional polytope has exactly 619 nonempty faces, by dimension 0,1,2,3,4 respectively: (82,237,227,72,1). Eight out of the 80 supporting inequalities have equality faces below dimension three, namely 1-based row numbers and dimensions (33,2), (34,2), (38,1), (40,1), (41,2), (43,2), (47,2), (48,2). Therefore exactly 72 of the 80 inequalities define actual three-dimensional facets. The Euler identity 82-237+227-72=0 holds.

## Theorem B: complete one-key connectivity of every face-optimal policy fiber

For any nonempty face F of H, define Gamma(F) with one vertex for each of the 5832 deterministic seedless LR profiles whose W lies in F. Two profiles are connected when their actions differ at exactly ONE of the nine observation keys. The exact enumeration in VERIFY.py proves that Gamma(F) is connected for all 619 nonempty faces (including H). Total profile incidences summed over faces: 551264. Zero disconnected cases.

## Theorem C: every H edge is saturated by actual real behavior

All 237 H edges lie entirely within O4(LR), the actual real-behavior observation set. Proof: each edge endpoint is a deterministic LR observation by the earlier 82-vertex certificate. By Theorem B the two endpoint policies connect by a finite path of face-optimal deterministic profiles, consecutive pairs differing at only one action key. Interpolating that key's probability with arbitrary real theta in [0,1], with all other action rules fixed, produces the entire straight observation segment between the profiles: the acyclic stopping process never revisits that key along a single sample path, so W is affine in its action distribution. All intermediate W remain on the exposed edge. The union of these segments is a connected subset of that edge containing both extreme endpoints; therefore it equals the whole edge. QED.

## Theorem D: positive-area real behavioral patch on each two-face

For each of 227 two-dimensional faces, the finite verifier finds (i) three noncollinear W values attained by differing only in one trinary action key (30 two-faces), or (ii) all four profiles of a two-key binary-action Cartesian box with linearly independent observation differences at its base corner (197 two-faces). In case (i), randomization over one trinary key attains an entire nondegenerate triangle inside F. In case (ii), independently randomizing the two action keys yields a bilinear map from the unit square to the affine plane of F. Its derivative has rank two at the base corner by the independent corner differences. Continuity implies full rank at some interior probability pair, so the inverse function theorem yields a relatively open two-dimensional observation patch in F. Because the map is a convex combination of the four corner observations, the entire patch stays in F. QED.

Thus exact real-behavior separation witnesses, if present for this fixed model, occur in relative interiors of dimension >=2 faces; none can occur on an exposed H edge. Connectivity alone does not decide every face-interior member.

## Exact exhaustive verification and proof kernel

VERIFY.py uses standard-library fractions.Fraction, integer masks and rational Gaussian elimination only. Its five deterministic steps are:

1. Reconstruct the strictly positive normalized P/Q branch kernel with ratios r2=(3/4,5/4), r3=(1/2,1,3/2), r4=(1/10,1,19/10), Q transition rows q2=(1/2,1/2); q3=((13/20,1/5,3/20),(1/40,9/20,21/40)); terminal Q row at j=0 is (509,382,9)/900, at j=2 is (9,382,509)/900, at (i,j)=(0,1) is (47/180,43/90,47/180), at (1,1) is (67/162,14/81,67/162). P transitions follow P(child|history)=Q(child|history)*r_child/r_parent. Assert all moment conditions.
2. Enumerate all 5832 deterministic LR profiles and calculate W with exact Fraction; every 720000*W has integer coordinates, and exactly 806 distinct points appear. Check all profiles against all 80 prior exact inequalities.
3. Form for each inequality the nonempty bit mask of profiles lying in equality. Begin with the full profile mask and close under all intersections with these 80 masks, retaining nonempty sets. The procedure finds exactly 619. Any face of bounded H is an intersection of supporting hyperplanes; since all H vertices are deterministic LR observations, equality profile sets enumerate every H face exactly.
4. Exact rational affine ranks yield the claimed face vector and the eight rank-deficient supporting inequalities.
5. For each face profile mask, traverse every Hamming-distance-one action neighbor to assert graph connectedness. For each rank-two face, test all one-key trinary triangles and all two-key four-corner boxes until an exact rank-two witness is found; all 227 succeed.

To reproduce, run: python VERIFY.py ../brc_r5_kernel_perturbation_phase_diagram_20261106_t0047/H_FACETS.txt . Use the immutable source H_FACETS.txt with Git blob 3f4ccf5d86435cba687b19d0a8f874635865600f. Exact local stdout is in EXACT_OUTPUT.txt. General all-real behavior conclusions are analytic consequences of the finite certificates and the separately affine/multiaffine property, not finite-sampling extrapolations.

## Next and source/admission boundary

The mother R5 question remains open. Select an exact rational W in relative interiors of dimension >=2 H faces not covered by identified behavior patches; test real feasibility of the six-variable quadratic-zonotope iff in the immediate predecessor. A certified algebraic UNSAT would establish an actual-image difference, while a constructive universal solution would establish image equality for this model. Preserve all real-variable boundaries and keep the previous hull theorem as a declared author-side dependency. No native active R5 owner, research CLAIM, formal Result, independent Driver review or Foundation promotion is asserted. Reuse: REUSE_APPLIED typed positive weighted BRC branch mass, likelihood-ratio observer, pinned exact H polytope certificate.