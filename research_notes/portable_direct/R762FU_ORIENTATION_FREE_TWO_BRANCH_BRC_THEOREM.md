# R762FU — Orientation-free two-branch BRC kernel: minimal S6-equivariant rotation choice and exact C3 depth counts

2026-11-19; scientific status: AUTHOR_PROVED / EXACT_FINITE_VALIDATION_PASS / NOT_REVIEWED.

Mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen taskbook \`awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md\`, frozen P000 scientific source \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` plus corresponding pinned X6 spatial torsor and three-force/triadic-balance definitions. Scientific continuation R762FM–FT, especially R762FT's no deterministic S6-equivariant orientation choice on unordered T (Draft PR #2794, first commit beebd7baba4571b3e14c8d54b82a8e1ba4c1a7fa).

## Question and exact typed input

R762FT proves a deterministic obstruction: a directed nonidentity three-cycle on an unordered set T of three distinct native axes requires an orientation bit under the already admitted S6 *axis-permutation rotation skeleton*. Can a **positive-rational BRC branching operator** instead avoid selecting an orientation, without suppressing the two distinct source histories?

Fix T={a,b,c} among six native X6 axes. The two candidate label permutations are g_+=(a b c) and g_-=(a c b)=g_+^{-1}, fixing all other axes. This is a candidate S6 skeleton, not a certified physical triadic closure event. A typed input w is a finite ordered word of named signed native primitive axis steps, with independent source IDs, signed flags and positive rational branch weights. All six Cell coordinates remain in a chart of the Z^6 torsor. No classic vector-sum-zero, trigonometric rotation, signed-mass cancellation, or physical time calibration is assumed.

## Theorem A — unique minimally supported S6-equivariant positive branch kernel

Define an explicit two-branch BRC operator
\[
K_T(w)=\tfrac12[g_+\cdot w;\mathrm{branch}=g_+]
       +\tfrac12[g_-\cdot w;\mathrm{branch}=g_-].
\]
The '+' denotes positive rational *branch mass*, not addition of signed forces or cancellation of distinct path identities. Both output words retain their branch ID, ordered source IDs, signs and weights. If a represented BRC input branch has weight q>0, its two output contributions each have weight q/2.

For every sigma in S6,
\[
\sigma_\ast K_T(w)=K_{\sigma T}(\sigma_\ast w),
\]
where sigma conjugates the cycle labels and acts letterwise on the typed words. Moreover, among probability kernels whose support is a **nonempty subset of the two nonidentity directed T-cycles**, exact S6-equivariance forces equal positive weights on both. Consequently the unique such normalized kernel has two branches, each of mass 1/2: two is the minimum permitted support size. This avoids a *deterministic* orientation selector but does not erase orientation information from the output branch identity.

Proof. A transposition in the setwise stabilizer of T swaps g_+ with g_- by conjugation. An invariant nonempty probability distribution on the two-element orbit must put equal mass on the two; normalization forces 1/2 each. All S6 conjugates carry this uniform distribution into the uniform distribution on the conjugate two-element orbit, and R762FT's exact Cell/Link/signed BRC letterwise covariance proves the stated kernel law. The stabilizer exchanges branches rather than demanding either branch individually invariant. QED.

## Theorem B — exact all-depth BRC multiplicities for fixed T

Fix the same T throughout h successive independent applications of K_T (this is **BRC path depth**, not automatically physical time or heartbeat intervals). Each step chooses g_+ or g_- with positive rational weight 1/2. Keep the entire ordered sequence of branch IDs, of which there are 2^h and each has mass 2^{-h}. Their composed label permutations are in the cyclic subgroup C3={1,g_+,g_+^2}; identify residues 0,1,2 respectively.

Let n_h(r) count the distinct length-h source sequences whose composed group permutation has residue r mod 3. For every integer h>=0,
\[
\boxed{n_h(0)=\frac{2^h+2(-1)^h}{3},\qquad
n_h(1)=n_h(2)=\frac{2^h-(-1)^h}{3}.}
\]
These are nonnegative integers and sum to 2^h. Proof: n_0=(1,0,0); each positive/negative branch changes the residue by +1/-1, so n_{h+1}(r)=n_h(r-1)+n_h(r+1). By symmetry write n_h=(a_h,b_h,b_h), then a_{h+1}=2b_h, b_{h+1}=a_h+b_h. Thus a_h+2b_h=2^h and a_h-b_h=(-1)^h. Solving these two integer equations gives the result. QED.

For h=1, n=(0,1,1); h=2, n=(2,1,1); h=6, n=(22,21,21). The image of the final label-permutation observer consists of two classes at h=1 and all three classes at h>=2, so its optimal fixed-length encoding uses one bit at h=1 and two bits for h>=2. This is an **observer-specific** quotient of branch histories; a future query reading ordered path labels/source ID/step order still requires their original provenance (up to 2^h distinct histories). Even if two group products coincide, their branch source words need not be interchangeable under future operations.

## Exact verification and honest scope

The standalone Node.js 18+ source \`R762FU_VERIFY.mjs\` uses only integer combinatorics, BigInt recurrences and signed source-ordered BRC word transformations. Executed with PASS:
- all 20 unordered native X6 triples and all 720 S6 label permutations: 14,400 two-sheet kernel equivariance tests;
- two oriented branches for every triple/permutation: 28,800 BRC named-word and signed endpoint transport comparisons;
- 20 stabilizer transposition tests for the minimum two-branch requirement;
- recurrence against the exact integer closed formula for h=0,..,64 (65 full BigInt depths);
- fully enumerated 2^h bit histories for h=0,..,12 (8,191 total histories).

The companion \`R762FU_EVIDENCE.json\` preserves counts, concrete instances and scope. The proof is valid for all h on this explicit fixed-T branching carrier; finite checks are supplementary. This extension reuses R762FT's S6 covariance and addresses its deterministic one-bit orientation obstruction through branching; it does **not** establish that Source's primitive \`TRIADIC_CLOSURE_E\` permits either orientation, allows a stochastic/multibranch native event, or admits iterated physical evolution. Authors' mathematical proof and exact checker only; independent review NOT_REVIEWED.

## Next decisive question

Read the actual frozen native Cell/Link/Port and triadic rotation *permission* definitions. Determine whether source incidence already carries a cyclic order, whether nondeterministic BRC branch rotations are legal candidate events, and whether any native orientation reversal is forbidden. Then either give a typed Source-native to (T,{g_+,g_-}) observer/transition morphism proving legal correspondence, or a minimal exact contradiction. Keep the R762FG q9 period gap separately open. No old R762FM–FT proof or identical enumeration needs repetition.