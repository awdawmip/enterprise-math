# R5 K3 — Uniform clocks, heterogeneous terminal kernels: exact subdiagonal four-hull separation

Date: 2026-11-04 (Asia/Shanghai). AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific sources (unchanged): Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Previous real-image equality result: `research_notes/brc_r5_k3_homogeneous_real_image_20261104_t0940/RESEARCH.md` @ `e74cc42ba0d63f674c6ea22db9e1d228654d90c0`. For v>r predecessor: `research_notes/brc_r5_k3_uniform_superdiagonal_error_fiber_20261104_t0844/RESEARCH.md` @ `5e0ff53bd6b9f573258ce2ad7553721176cf6f0c`.

Current behavioral rules: account canonical main 00_BOOTSTRAP.md, OPERATING_MANUAL.md, math/code/expression policies; project docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context and docs/PORTABLE_RESEARCH_PROTOCOL.md; P000 and ACTIVE worldview. Source identity and future-operation semantics are retained. This is an exact four-output *source-labelled finite BRC branch-flow observer model*; it is not native X6 physical time evolution or BRC–Shor, and no physical residual attribution is made.

## Domain and observer

Four BRC sources s=(C,I,BJ,IJ) have capacities c=(1/8,1/6,1/16,3/32), total W0=43/96. FULL upstream choices are x,y∈[0,1], 0≤i≤1−x and source masses w=(c_C,c_I(1−x),c_BJ*y,c_IJ*i); d=w_BJ+w_IJ. Per-source stage flow M_s=w_s z_s, Z_s=(2/3)M_s t_s, U_s=Z_s u_s, with z_s,t_s,u_s∈[0,1]. LR has i=(1−x)y and common z,t,u at all sources.

Time kernels are source-identical 0<v≤r<1; terminal kernels p_s,q_s independently lie in (0,1). With M=ΣM_s,Z=ΣZ_s,U=ΣU_s the four observer values are

    eP=107/128−21x/128+d/4−Z/2+(Σ p_s Z_s)/8
    eQ=13/64+3x/64−d/2+Z/8+(Σ q_s Z_s)/32
    TP=3+M+(3/2)Z+rU
    TQ=3+M/2+(3/8)Z+(v/4)U.

Define capacity means pbar=(Σc_sp_s)/W0 and qbar=(Σc_sq_s)/W0, and q_+=max(q,0).

## Theorem: exact separation for all real v≤r

For each 0<ε≤1/100 define

    κP=ε(4−pbar)/12,
    nP=(−ε,0,−1/4−κP,1),
    κQ=ε(4+qbar)/48,
    nQ=(0,ε,−1/4−κQ,1).

For *all real* input kernels in the declared domain, the FULL and seedless LR convex-support gaps are exactly

    hFULL(nP)−hLR(nP)=ε/12 Σ c_s(pbar−p_s)_+,
    hFULL(nQ)−hLR(nQ)=ε/48 Σ c_s(q_s−qbar)_+.

In particular, any p- or q-source heterogeneity strictly separates the complete four-observer convex hulls. A FULL maximizing deterministic observation V obeys

    dist_∞(V,conv O(LR)) ≥ gap(n)/||n||_1.

### Complete proof

1. **Reduction to actual deterministic vertices.** Every stage policy's expected observer is multi-affine in its own behavioral probabilities. For FULL, each fixed stage assignment is affine over the upstream polytope (x,i) triangle with corners (0,0),(0,1),(1,0), times y∈[0,1], giving 6×4^4=1536 stage/upstream vertices. For LR, substitution i=(1−x)y gives a separately-affine upstream objective on [0,1]^2 and four deterministic shared stages: 2×2×4=16 vertices. These finite supports are equal to the maxima over all corresponding real behavioral policies.

2. **Sourcewise stage rewards.** Fix either normal n=(A,B,a,1) above. Discard the common constant 3(a+1), retain the error baseline B_P=−ε(107/128−21x/128+d/4) or B_Q=ε(13/64+3x/64−d/2). Let κ be the matching positive κP or κQ, and S=1/4−κ. The signed stage reward per unit source mass equals 0 at stage 0 and S at stage 1. At stage 2 it is S+D_s, with D_s=ε(pbar−p_s)/12 for nP and D_s=ε(q_s−qbar)/48 for nQ. Stage 3 has reward S+D_s+(v−r)/6−(2r/3)κ. For 0<v≤r and κ>0, stage 3 is strictly below stage 2, including exactly v=r. Stage 1 is strictly positive for ε≤1/100. FULL therefore chooses stages 1 or 2 for each source with reward R_s=S+max(0,D_s).

3. **All six FULL upstream corners checked analytically.** At (x,y,i)=(0,1,1), w=c. At any other upstream corner w≤c componentwise and the missing total capacity W0−W≥1/16. The per-mass maximizing reward R_s≥1/4−ε/3. Changing the error baseline from its full-capacity value can increase it by no more than 13ε/64 for nP or ε/8 for nQ. Consequently, each other FULL corner scores less by at least (1/16)(1/4−ε/3)−13ε/64>0. So FULL maximizes upstream at (0,1,1) and chooses precisely those stages 2 for which D_s>0.

4. **All four LR upstream corners checked analytically.** At canonical (x,y)=(0,1), w=c. The shared stage-2 reward difference is Σc_sD_s=0 by the definitions of pbar,qbar; LR stages 1 and 2 tie with positive per-mass reward S, and stages 0 and 3 are lower. At every other LR upstream corner, W0−W≥5/32, its signed stage reward per unit source mass is at most 1/4+ε/12, and its error baseline increase is at most 13ε/64. Consequently canonical LR score minus any other LR-corner score is bounded below by

    5/128 − ε(5W0/12+13/64) > 0  (ε≤1/100).

The bound uses canonical stage-1 reward S≥1/4−ε/3; all finite LR choices are therefore covered and the LR support is the full-capacity baseline plus W0 S.

5. **Subtract exact supports.** FULL adds Σc_s(D_s)_+ to that same baseline/W0 S. LR adds zero. This is exactly the two displayed formulas. If p is nonconstant, some p_s<pbar; if q is nonconstant, some q_s>qbar, so the relevant sum is positive. The maximizer is the actual FULL policy of step 3; Hölder duality between L∞ and L1 gives the stated metric lower bound. QED.

The new theorem fills the v≤r terminal-heterogeneity boundary. Along with the cited v>r predecessor and the explicit homogeneous real-image reconstruction, the **uniform-clock K3 subfamily 0<r,v<1** has author-side classification: four-hulls coincide iff p_s and q_s are each constant; in this case actual real observation sets also coincide. The claimed combined classification depends on the exact cited predecessor, not on re-running it.

## Exact executed calculation

Sibling VERIFY.py uses only standard-library Fraction; eight rational model/direction cases enumerate 1536 FULL and 16 LR vertices each, totaling 12,288 FULL and 128 LR deterministic observations. Checks include exact maximal support, maximizing FULL witness, LR optimum, formula and L∞ lower bound. Actual output saved in EXACT_OUTPUT.txt with final marker `PASS_EXACT_R5_K3_UNIFORM_CLOCK_SUBDIAGONAL_ERROR_FIBERS`.

At r=2/3,v=1/3,p=(1/4,1/3,2/3,3/4),q_s=1/2,ε=1/100, nP=(−1/100,0,−31327/123840,1). FULL stages (2,2,1,1) at (x,y,i)=(0,1,1) give gap 11/309600 and L∞ distance lower bound 22/782027. For p_s=1/2,q=(3/4,1/5,2/5,4/5), nQ=(0,1/100,−86323/344000,1), gap 199/16512000, L∞ lower bound 199/20820624. Both examples remain exact at v=r=1/3. This calculation is a model-internal probability-polytope certificate, with source labels retained, not a native X6 arithmetic/physics claim.

## Next dependency

Audit sourcewise assumptions and all parameter boundaries of preceding clock-heterogeneity no-go lemmas before claiming the entire 16-parameter K3 family classified. Advance a distinct reconvergent source-sensitive model toward the R5 mother target: equal complete four-hulls but different actual real images. Exact all-signed hull certificates must precede real-image membership testing. See NEXT_TASK.md.
