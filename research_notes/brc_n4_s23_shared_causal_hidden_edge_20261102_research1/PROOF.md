# BRC N=4, S23: shared-causal interior obstruction and sharp one-dimensional edge profile

Date: 2026-11-02. AUTHOR ANALYTIC PROOF / EXACT INTEGER EXECUTED / UNREVIEWED / NOT_ADMITTED. Scientific input remains frozen at enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continues the exact two-parameter fixed-seven/free-three theorem (previous PR #1765 commit 7a6494f5cefe177458bcdd7d2caf33d21c6f93f4). This is an S23 behavioral observer model result; it asserts no native P000 dynamics or physical residual.

## Precise population and new strategy family

Use the same six separately identified positive sources AU0, AU1, AV, BU0, BU1, BV, the original common four-stop observer and the same row-stochastic 20-denominator source-mixing matrix. The 11-parameter policy z=(z0,...,z10) is evaluated by F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)). Source selectors are A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10), with source mixing rows (10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0), (0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20) divided by 20. This preserves source labels and the shared causal parameter z2=b_U.

Fix exactly the ten decoders D1,D2,D3,D4,D6,D7,D8,K1,K2,K3 from the preceding source. Their complete rational four-stop kernels and mixing expansion are given in VERIFY.js. For each decoder D, L_D(z)=max over the six original separately labeled sources i of TV(P_i(z),Q_i(D)); bank risk m(z)=min over these ten D of L_D(z).

Define the legal three-coordinate face
z(s,t,u)=(s,t,u,0,0;1,0,0,0,0,0), all real s,t,u in [0,1].
The u=0 face is exactly the two-parameter H(s,t) population proved sharp at 3/5 in the preceding work. Here u is the **single common z2=b_U** shared by four original sources, not four independently adjusted source variables.

## Theorem 1: sharp entire real u-edge

For fixed s=3/5 and t=3/10,
max over **all real u in [0,1]** of m(z(3/5,3/10,u)) = 13/20,
with the unique maximizer u=1/2.

**Exact center lower certificate.** At u=1/2, the six observed four-stop distributions are exactly
(3/5,1/5,1/10,1/10), (3/5,1/5,9/100,11/100), (3/5,0,0,2/5), (3/10,7/20,0,7/20), (3/10,7/20,0,7/20), (3/10,0,0,7/10).
The ten bank risks in the declared decoder order are exactly
(4/5,1,1,7/10,13/20,71/100,7/10,7/10,13/20,1).
Consequently m=13/20. These equalities use the six genuine mixed source distributions; the witness is a legal 11-coordinate real policy.

**All-real upper certificate.** With s,t fixed, each of the six original source laws, and hence each mixed observed row, is affine in u. Total variation against a fixed decoder is convex in each prepared row; the maximum over the six sources remains convex. Exact endpoint evaluations are
L_K2(0)=1/2, L_K2(1/2)=13/20,
L_D6(1/2)=13/20, L_D6(1)=1/2.
For 0<=u<=1/2, convexity gives m(u)<=L_K2(u)<=1/2+(3/10)u.
For 1/2<=u<=1, it gives m(u)<=L_D6(u)<=4/5-(3/10)u.
Both right-hand sides are strictly less than 13/20 away from u=1/2. The exact center certificate and these inequalities prove the maximum and its uniqueness.

Thus the previous fixed bank's old 3/5 bound on u=0 extends neither to this real causal edge nor to the entire three-coordinate face. The excess at the unique edge maximizer is exactly 13/20-3/5=1/20.

## Theorem 2: an open three-parameter failure region

The same fixed bank exceeds radius 3/5 on the full relative-open subset
U = {(s,t,u) in [0,1]^3: max(|s-3/5|,|t-3/10|)+|u-1/2| < 1/20}.
In particular this is a positive-volume family of lawful real policies, not an isolated point.

Proof: For every original unmixed source, only the Bernoulli parameters a=s or t and b=u or 0 vary; c is fixed 0 or 1. Coupling the first two conditional decisions bounds source total variation between two parameter triples by |delta a|+|delta b|. Nonnegative stochastic source mixing is TV nonexpansive, so every labeled observed row satisfies TV(P_i(s,t,u),P_i(s',t',u')) <= max(|s-s'|,|t-t'|)+|u-u'|. Applying the reverse triangle inequality to each L_D and then stability of finite max and min yields
|m(s,t,u)-m(s',t',u')| <= max(|s-s'|,|t-t'|)+|u-u'|.
Set (s',t',u')=(3/5,3/10,1/2), where m=13/20. On U this implies m>3/5. All source identities and the joint parameter u are retained.

## Theorem 3: an adaptive-vertex pitfall

At all eight vertices (s,t,u) in {0,1}^3, the **same fixed bank** has risk at most 3/5: in lexicographic order (000,001,010,011,100,101,110,111) the exact minima are (1/2,1/2,1/2,1/2,1/2,1/2,3/5,3/5). Yet its interior point (3/5,3/10,1/2) has risk 13/20. A fixed decoder's TV risk enjoys convex interpolation, but the minimization over decoders permits a *different decoder at each vertex*, which does not certify the interior. Continuum verification by cells requires **one common decoder** for all corners of each cell (or another valid continuum argument), exactly as the preceding 25-cell theorem did on u=0.

## Evidence, scope and unresolved optimization

Run node VERIFY.js. It executes integer arithmetic on probabilities scaled by N=1000, with risk2=2000*TV, checks normalization, six distinct mixed rows, all ten exact center risks, the four endpoint values, midpoint affineness and all eight cube vertices. RUN_EVIDENCE.json records the actual result. The two all-real conclusions follow from the displayed convexity and coupling proofs applied to the exact finite certificates. The proof concerns the specific historical ten-decoder bank. The separately optimized S18 ∪ J([0,1]) ∪ H([0,1]^2) minimax remains 3/5, and the unrestricted eleven-real-parameter ten-label objective retains its earlier interval [1/2,2/3] (k=4,6).

**Immediate optimized-singleton corollary.** Let T=S18 ∪ J([0,1]) ∪ H([0,1]^2) ∪ {E}, E=z(3/5,3/10,1/2). The previously proved restricted minimax on the subset without E is 3/5, while the displayed *same specific old bank* has risk at most 3/5 on that subset and exactly 13/20 at E. Hence, for seven fixed and three jointly reoptimized decoders, **3/5 ≤ inf_bank sup_{z∈T} m_bank(z) ≤ 13/20**. These bounds are exact inequalities; the optimal value between them remains open. They do not use the unrestricted mother problem's 2/3 upper bound.

Next: include the center witness E=z(3/5,3/10,1/2) in the 3/5 lower-certificate population, jointly re-optimize the three free kernels and seek a common-kernel cubical cover of the shared-causal three-coordinate face. The 11-witness triple-event threshold test is only a first obstruction method; stronger pairwise/LP dual or multistrategy evidence may be needed to determine the newly optimized radius.
