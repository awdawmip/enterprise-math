# R5 — Four likelihood-ratio classes hide a source residual without changing the exact STOP-time image

2026-10-31 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**.

## Frozen provenance and authorization

GLOBAL_KNOWLEDGE_V1 main@e5b88cd1418df81a633a50542f6b02320475bb3e (bootstrap, manual, Enterprise Math router, P000, ACTIVE worldview, triggered mathematical/BRC/activity policies); Enterprise Math main@684a68342bf1321ba4ad33ea02b3e25f20d789e7 (including current portable research protocol). The prior R5 exact full-real fixed 12-path time-error NO-GO is in immutable commit 74f0b4ff17d56fc6f17e20a1fdb9322e36a3fde2, research_notes/brc_r5_time_error_global_no_go_20261031_t0344/RESEARCH.md. The model below **changes its path masses, number of terminal LR classes and STOP topology**; it does not overturn that NO-GO.

The native directed context reported authority_granted=false and complete_task_packet=false, and bounded native active-owner lookup returned CONTROL_QUOTA. This is portable author-side research only: no current owner/CLAIM/Result or independent Driver acceptance has been verified. P000 (six native spatial axes + time, enterprise 120-degree orthogonality) and protected ACTIVE worldview are unchanged. This is finite two-measure probability, not native X6 dynamics or a physical assertion.

## Model and exact definitions

Let hidden source I∈{0,1} have P(I=i)=Q(I=i)=1/2, so both sources share likelihood ratio 1. The terminal chance class J∈{1,2,3,4} has likelihood ratios R=(1/4,1/2,3/4,2). The conditional Q kernels are

K_0=(5,2,5,6)/18; K_1=(3,6,3,6)/18; Kbar=(2,2,2,3)/9.

Take q_ij=K_i(j)/2 and p_ij=R_j q_ij. All twelve? This carrier has exactly EIGHT complete source/class chance paths (2×4), with strictly positive P/Q masses and both laws normalized: ∑K_i=∑R_j K_i=1. (This count is eight; the predecessor had twelve.)

There is a genuine absorbing STOP/CONTINUE decision at τ=1, before J, and a second genuine STOP/CONTINUE decision at τ=2 after J. CONTINUE at τ=2 forces termination at τ=3. FULL sees source and then its history (I,J). Seedless LR sees only (τ,likelihood ratio): one shared early bit for the two sources and four independent late bits. No action key repeats and no persistent random seed exists. T_M=E_M τ for M∈{P,Q}. All policies may use real behavioral probabilities independently at available decision keys.

## Proposition 1: all-signed two-time-hull classification

For any finite positive two-source kernels K_i on distinct ratios R_j, with shared initial LR=1, ∑K_i=∑R_jK_i=1, and positive source weights q_i adding to one, the FULL and seedless LR convex hulls of the *two-time observer* (T_P,T_Q) agree exactly when each of the following two scalar roots agrees across sources:

F_i^+(λ) = 1−λ + ∑_j K_i(j)(R_j−λ)_+ = 0, with λ_i^+∈(1,max_j R_j);
F_i^−(λ) = λ−1 + ∑_j K_i(j)(λ−R_j)_+ = 0, with λ_i^−∈(min_j R_j,1).

Proof. For signed objective aT_P+bT_Q, optimize the last decision first. Its CONTINUE increment per unit Q mass at class j is aR_j+b, so its optimal sign is common to FULL and LR. The early conditional CONTINUE gain for source i is

D_i(a,b)=a+b+∑_j K_i(j)[aR_j+b]_+.

The two support maxima have the same constant baseline a+b; their remaining terms are ∑_i q_i[D_i]_+ (FULL) and [∑_i q_i D_i]_+ (LR). They agree in a signed direction iff no two source gains have opposite strict signs (positivity of q_i). For a>0 and λ=−b/a, D_i=aF_i^+(λ), which is continuous strictly decreasing, positive at λ=1 and negative at max R. For a<0 write s=−a>0, b=sλ; D_i=sF_i^−(λ), which is continuous strictly increasing, negative at min R and positive at λ=1. For a=0 the source signs are identical. Therefore equality for *all signed (a,b)* is equivalent to both source root pairs being equal; compact convex hulls are equal iff their support functions agree. QED.

**Three-class rigidity in this exact topology.** With at most three *distinct* terminal ratios, equality of time convex hulls forces K_0=K_1. Indeed a shared λ^+∈(min R,max R) and the linear data ∑K=1, ∑RK=1 and ∑K(R−λ^+)_+ fixed uniquely determine a three-point kernel: the three column vectors of 1, R and the positive-part hinge are linearly independent because the hinge is not affine across three distinct support points straddling λ^+. For two classes, sum and first moment suffice. This claim is scoped to one early collision and one later decision, not all STOP trees.

## Constructed minimal four-class example

For both K_0 and K_1 the mass above 1 is exactly 1/3 at R=2. The mass below 1 is 2/3 and its weighted first moment is 1/3. Thus

F_i^+(5/4)=1−5/4+(1/3)(2−5/4)=0;
F_i^−(4/5)=4/5−1+(2/3)(4/5)−1/3=0.

Strict monotonicity makes both these roots unique. Proposition 1 proves **all-signed two-dimensional STOP-time convex hull equality for all real behavioral policies**. Nonetheless the labelled BRC transition residual is nonzero:

K_0−K_1=(1,−2,1,0)/9;   TV(K_0,K_1)=2/9;
∑_j(K_0(j)−K_1(j))(R_j−5/8)_+ = 1/72.

Thus LR state merging loses genuinely future-predictive source information; the particular optimized time-observer support tests do not expose it. This disproves the proposed *unqualified necessity* of kernel lumpability for time-hull equality, and sharpens the previous three-class threshold.

## Proposition 2: a one-shared-gate topology cannot solve the four-observer mother problem

In any finite experiment with exactly one upstream shared LR CONTINUE gate x, followed by at most one layer of independent downstream LR behavioral decisions z_j and then forced termination, every finite vector of expected pathwise STOP rewards has the affine multilinear form

O_LR(x,z)=v_0+x u+∑_j xz_j v_j.

Set w_j=xz_j. Its exact feasible region is the polytope 0≤w_j≤x≤1; every feasible (x,w) is realizable by z_j=w_j/x if x>0 and arbitrary z_j if x=0. Therefore the *actual seedless LR observer image* is a compact convex polytope, for any number of observer coordinates and any fixed source/class-dependent chance and STOP rewards. FULL similarly uses independent x_i and w_ij=x_i z_ij with 0≤w_ij≤x_i≤1, hence its actual observer image is also a polytope. In this topology, equality of convex hulls *necessarily entails equality of actual real observer sets*. No four-observer example of equal hulls and unequal real images can arise merely by changing endpoint errors on this one-gate carrier, even if rank four is obtained.

The proof does not extend to two serial interacting shared gates, repeat-key trajectories or adaptive decisions after the downstream layer; their observer maps need not admit this single product linearization.

For the special common time-only error tuple (ε_1,ε_2,ε_3), this carrier has the further exact rank obstruction e_P−e_Q=(ε_3−ε_2)(T_P−T_Q), because P and Q have the same early STOP mass. Thus its common-time-error four-observer rank is at most three; this is distinct from the more general single-gate convexity theorem.

In particular the actual two-time images agree in the explicit four-class model, because both are convex and Proposition 1 gives equal hulls. Their common rational hexagon in coordinates (T_P−1,T_Q−1) has vertices

(0,0); (5/3,4/3); (11/6,14/9); (35/18,16/9); (2,2); (4/3,5/3).

For LR, explicitly ΔT_Q=x+∑_j Kbar_j w_j and ΔT_P=x+∑_j R_j Kbar_j w_j; for FULL replace x,w_j by source-specific x_i,w_ij. Both are affine maps of bounded polytopes.

## Exact executed evidence; boundaries; next question

The sibling standalone VERIFY.py uses the Python standard-library Fraction rational type, positive/normalization and mean-one checks, exact threshold equations, exact total-variation and residual checks, and COMPLETE enumeration of 1024 FULL and 32 LR deterministic behavioral policies. A rational monotone-chain convex-hull algorithm verifies six identical hull vertices and containment of all FULL points; output in EXACT_OUTPUT.txt ends PASS_EXACT_R5_FOURCLASS_NONLUMPABLE_TIME_HULL_EQUALITY. The enumeration checks the displayed rational carrier; Propositions 1 and 2 are all-real analytic proofs, not finite extrapolation.

Related literature *context only*: Laroche & Tachet des Combes, “On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs,” ICML/PMLR 2023, https://proceedings.mlr.press/v202/laroche23a.html; Dufour & Prieto-Rumeau, “Absorbing Markov Decision Processes: Geometric Properties and Sufficiency of Finite Mixtures of Deterministic Policies,” arXiv:2512.17511 (2025-12-19), https://arxiv.org/abs/2512.17511. These concern other occupancy/mixture scopes and do not themselves establish the exact dual-measure compressed-LR formulas above. Literature novelty/priority remains unadjudicated.

**Next discriminating unit**: a model with at least TWO serial, interacting shared LR decision gates. Preserve nonzero labelled kernel residual and exact positive P/Q flows. First demand all-signed 2D STOP-time hull equality; then all-signed full four-observer hull equality via exact rational 5-vertex combinations/Farkas witnesses and rank four; only then seek a real image nonmembership proof. See NEXT_TASK.md. Author proof is unreviewed; formal Source owner/CLAIM/Result/independent Driver review remain separate.
