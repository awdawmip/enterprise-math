# R5 K3: Exact superlevel-mask classification of ratio-locked clock normals

Date: 2026-11-04 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Mother objective: common-terminal-label P/Q experiment with equal FULL/seedless-LR four-observer convex hulls and unequal actual real-behavior observer sets.

## Provenance, domain, frozen scientific input

Continuation: enterprise-math immutable commit e264df4b5697883e14bda32405edee9c4cb3b402, research_notes/brc_r5_k3_subdiagonal_ratio_mask_20261104_t0140/RESEARCH.md and VERIFY.py.
Frozen scientific pins inherited intact: chatgpt-global-knowledge@a01383f825ef9d43b4b754254303298c64041568 and enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e. Current project/account behavioral rules read separately from current canonical main. P000 and protected ACTIVE worldview remain unchanged. This finite two-law experiment is an auxiliary four-source observer model, not a proved physical X6 embedding.

Retain positive BRC source labels s=(C,I,BJ,IJ), capacities c=(1/8,1/6,1/16,3/32). FULL upstream: 0<=x,y<=1, 0<=i<=1-x. Seedless LR: i=(1-x)y, with one shared K3 stage. Capacities w=(1/8,(1-x)/6,y/16,3i/32). For each source, four deterministic nested-action stages j=0,1,2,3 with incremental (TP,TQ) per unit w:

stage0 = (0,0);
stage1 = (1,1/2);
stage2 = (2,3/4);
stage3 = (2+2r_s/3,3/4+v_s/6).

The actual inherited four observers are, with d=y/16+3i/32, M_s=w_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s:

eP=107/128-21x/128+d/4-sum S/2+sum(p_s*S_s/8);
eQ=13/64+3x/64-d/2+sum S/8+sum(q_s*S_s/32);
TP=3+sum M+3sum S/2+sum(r_s U_s);
TQ=3+sum M/2+3sum S/8+sum(v_s U_s/4).

For the present theorem 0<k<1, 0<r_s<1, v_s=k*r_s, and all p_s,q_s independently lie in (0,1). FULL can select source-specific stages, LR must select one shared stage. The source capacities are kept separate until policy selection, consistent with provenance-preserving BRC reuse.

## Theorem 1: exact signed wedge support function for ALL real behavior policies

For every real 0<t<3/8, n_t=(0,0,t,-1), define

A_s(t)=(2+2r_s/3)t-3/4-k*r_s/6,
F={empty,{C},{C,I},{C,BJ},{C,I,BJ,IJ}}.

Then

h_FULL(n_t)=3(t-1)+sum_s c_s max(0,A_s),
h_LR(n_t)=3(t-1)+max_{B in F} sum_{s in B}c_s A_s,

and the exact nonnegative gap is

Delta(t)=sum_s c_s(A_s)_+ - max_{B in F}sum_{s in B}c_s A_s.

Let P(t)={s:A_s>0}, Z(t)={s:A_s=0}. The exact equality criterion at any t is

Delta(t)=0 iff there exists B in F with P(t) subset B subset P(t) union Z(t).

In particular, when all four scores are nonzero, Delta(t)=0 iff P(t) is one of the five masks in F.

Proof: The directional incremental scores of stages 0,1,2,3 are 0, t-1/2, 2t-3/4, A_s. In 0<t<3/8, stages 1 and 2 are strictly negative. At FULL upstream corner (x,y,i)=(0,1,1), ALL four source capacities are simultaneously achieved. Choosing stage3 for positive A_s and stage0 otherwise attains sum c_s(A_s)_+; sourcewise upper bounds show optimality. Under LR, shared stage0 contributes zero; shared stages1,2 have negative total score (source C is always present). Shared stage3 has multilinear/affine upstream score on x,y in [0,1] because i=(1-x)y, so it attains its maximum at an upstream square corner. The corners give exactly the nonempty masks C,I; ALL; C; C,BJ (and stage0 gives empty). The shared baseline is 3(t-1). For a mask B, the difference from the sourcewise maximum is the sum of all strictly positive source terms omitted by B plus the absolute values of all negative source terms included in B. Strict capacities c_s>0 give the stated exact equality criterion. Deterministic extrema cover every real behavioral choice, proving the formulas for the full continuum. QED.

## Theorem 2: complete classification of wedge-invisible proportional clocks

Define the source threshold mu(r)=(9+2kr)/(8(3+r)). For all 0<k<1 and 0<r<1 it lies in (0,3/8), and its derivative is

mu'(r)=(6k-9)/(8(3+r)^2)<0.

Also A_s(t)>0 exactly when t>mu(r_s). Therefore, as t moves through (0,3/8), P(t) takes exactly the proper, nonempty UPPER LEVEL SETS of the source clock vector r, apart from empty/full and the zero-score threshold boundaries.

The gap vanishes on EVERY real t in (0,3/8) if and only if every proper nonempty upper-level set of the vector r belongs to F. This has the following exhaustive explicit classification:

(A) all four r_s are equal;
(B) exactly TWO different r-levels, with the HIGHER group equal to {C}, {C,I}, or {C,BJ};
(C) exactly THREE different r-levels, with either r_C>r_I>r_BJ=r_IJ or r_C>r_BJ>r_I=r_IJ.

Every clock vector outside (A)-(C) has a strictly separating normal of the above form. In particular every one of the 24 strict orderings has a gap, as does every vector with a unique minimum r_s, regardless of ties among the other three values.

Proof: Strict monotonicity of mu creates a nonempty open t-interval for every proper upper-level set. Theorem 1 makes a gap zero on that interval precisely when this set is in F. At threshold boundaries, continuity of finite maxima yields zero when adjacent intervals give zero. The only proper nonempty masks in F are {C}, {C,I}, and {C,BJ}; the only chains of two distinct such masks are {C} subset {C,I} and {C} subset {C,BJ}. These exactly yield (A)-(C). A unique lowest source produces a three-element positive set for t strictly between its threshold and the next one, and no three-element set is an LR mask. All strict permutations therefore separate. This theorem classifies the DECLARED signed normal wedge, not all four-dimensional support directions. QED.

## Corollary: uniform exact separation of all 24 permutations

Fix k=1/2, t=7/20, n=(0,0,7/20,-1) and let (r_C,r_I,r_BJ,r_IJ) be ANY of the 24 permutations of (1/5,2/5,3/5,4/5). For these exact parameters A_s=(3r_s-1)/20; its values are precisely {-1/50,1/100,1/25,7/100}. Every permutation has three strictly positive source scores, one negative. No LR mask contains exactly those three positive sources. Therefore for each mask either one positive source is omitted or the negative is included, and its shortfall is at least

min_s c_s * min_s |A_s| = (1/16)(1/100)=1/1600.

Consequently Delta(7/20)>=1/1600 for every one of the 24 permutations. The actual FULL policy x=0,y=i=1 with source stage 3 exactly where A_s>0 and stage 0 elsewhere achieves h_FULL. By Holder duality it produces a four-observer vector W with

dist_infinity(W,conv O(LR)) >= Delta / ||n||_1 >= (1/1600)/(27/20)=1/2160.

This also applies to the two-clock projection, since n has no error components. The gap lower bound is sharp among these 24 permutations: r=(3/5,4/5,2/5,1/5) and r=(4/5,3/5,2/5,1/5) give Delta=1/1600 exactly.

## Exact computational regression / coverage

The associated VERIFY.py was executed with Python standard-library fractions.Fraction. It generates the complete inherited four-observer values for all 6*4^4=1536 deterministic FULL configurations and all 4*4=16 LR configurations for each of 24 strict permutations and each of all 14 nontrivial two-level high groups of sizes 1,2,3. It independently checks exact support values, wedge formula, model positivity, actual FULL witness, masks, the two-level classification and the strict permutation gaps. 343 exact assertions passed; the complete real execution record is EXACT_OUTPUT.txt, ending PASS_EXACT_R5_K3_RATIO_LOCKED_SUPERLEVEL_MASK_CLASSIFICATION. The continuously quantified theorems are analytic; finite tests verify specified rational examples and code, not all real inputs.

The smallest exact gap by location of the lowest clock was C:1/400; I:3/3200; BJ:3/3200; IJ:1/1600. The two-level check finds zero wedge gap exactly for the higher-level groups {C}, {C,I}, {C,BJ}, and positive gap for the other eleven nonempty proper high groups.

## Next research and native state

For wedge-invisible families (A)-(C), calculate ALL-signed two-clock hulls and then their actual two-error observer fibers. For any complete four-dimensional convex-hull equality candidate, give exact rational <=5 LR-vertex convex certificates for every FULL deterministic observer, or an exact rational Farkas separator. Only then test actual real policy image nonmembership. The mother objective remains open.

BRC status: REUSE_APPLIED; four positive source masses, provenance and signed clock residual preserved. No new shared BRC tool or native X6 physical theorem claimed. Native Site on 2026-11-04 reported research_authority_granted=false, static_machine_readonly, and active owner query CONTROL_QUOTA. GitHub scientific persistence is author-side and grants no native CLAIM, Result, Driver review or Researcher-ID.
