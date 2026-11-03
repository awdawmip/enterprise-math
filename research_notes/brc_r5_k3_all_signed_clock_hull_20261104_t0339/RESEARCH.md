# R5 K3 — All-signed clock-hull classification and a unique-C four-observer fiber obstruction

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source, scope, and original model

Scientific predecessor: immutable Enterprise Math commit `c31d5c4caaaa764c6dbb0f4dc63f19ba68cc2eec`, `research_notes/brc_r5_k3_superlevel_mask_classification_20261104_t0243/RESEARCH.md`. Frozen science pins retained: `awdawmip/chatgpt-global-knowledge@a01383f825ef9d43b4b754254303298c64041568` and `awdawmip/enterprise-math@86149263e38c22292c9def1e0f69092efa1be77e`. Current normative rules were separately read from current canonical main. P000 and ACTIVE worldview were not altered. This is the four-source, source-sensitive BRC auxiliary stopping experiment, not an X6 physical embedding. Clock projections are used to test a declared R² observer; four-observer error fibers and source provenance are retained for the next theorem.

Sources S=(C,I,BJ,IJ) have strictly positive capacities c=(1/8,1/6,1/16,3/32). FULL upstream variables satisfy 0<=x,y<=1, 0<=i<=1-x; LR uses i=(1-x)y. Capacity vector w=(1/8,(1-x)/6,y/16,3i/32). At each source, the four deterministic nested K3 stage clock increments per unit capacity are j0=(0,0), j1=(1,1/2), j2=(2,3/4), j3=(2+2r_s/3,3/4+v_s/6). FULL selects stages independently per source; seedless LR must select a shared K3 stage.

Assumptions throughout: 0<k<1, 0<r_s<1, v_s=k r_s, and independent 0<p_s,q_s<1. For real behavioral policies put d=y/16+3i/32, M_s=w_s z_s, S_s=(2/3)M_s t_s, U_s=S_s u_s. The unchanged FOUR observables are

eP=107/128-21x/128+d/4-sum(S_s)/2+sum(p_s S_s/8);
eQ=13/64+3x/64-d/2+sum(S_s)/8+sum(q_s S_s/32);
TP=3+sum(M_s)+(3/2)sum(S_s)+sum(r_s U_s);
TQ=3+sum(M_s)/2+(3/8)sum(S_s)+sum(v_s U_s/4).

## Theorem 1 — exact complete signed time support

For EVERY real normal (a,b) in R² define A=a+b/2, B=2a+3b/4, T=2a/3+kb/6, g_s=B+r_s T, Ctot=sum(c_s)=43/96, and the five LR masks

F={empty,{C},{C,I},{C,BJ},{C,I,BJ,IJ}}.

If T<=0, then
h_FULL(a,b)=h_LR(a,b)=3(a+b)+Ctot*max(0,A,B).

If T>0, then
h_FULL(a,b)=3(a+b)+sum_s c_s*(g_s)_+,
h_LR(a,b)=3(a+b)+max_{D in F} sum_{s in D}c_s*g_s.

Thus Delta(a,b)=sum_s c_s(g_s)_+ - max_{D in F}sum_{s in D}c_s*g_s >=0 whenever T>0. The identities cover all REAL behavioral strategies.

**Proof.** Stage scores are 0,A,B,B+r_s T. Nested real continuation probabilities z,t,u form exact convex mixtures of j=0,1,2,3 with weights (1-z,z(1-t),zt(1-u),ztu). Upstream FULL triangle times the y interval has 6 deterministic corners; LR upstream square has 4. Iterating these multi-affine mixtures shows every real behavioral observation is in the convex hull of the finite deterministic observations, and all deterministic extrema are feasible.

For T<=0, stage 3 is pointwise dominated by stage 2. The same m=max(0,A,B) is the best local score at every source. Every source is bounded by c_s*m; a common maximizing stage at upstream x=0,y=i=1 realizes all source capacities and both classes achieve Ctot*m.

For T>0, stage 3 pointwise dominates stage 2. If A<=0, stage 1 is dominated by stage 0. If A>0, use the exact identity
B-A=((1-k)/(2-k))*A+(3/(2*(2-k)))*T >0.
Therefore g_s>B>A. Thus only stages 0 and 3 can maximize each source. FULL attains all capacities c_s simultaneously and chooses stage 3 where g_s>0. Seedless LR cannot distinguish sources at K3, and its shared stages 1 and 2 are either dominated by stage 0 or by stage 3 at upstream full capacity. For shared stage 3, the objective is multi-affine in LR upstream (x,y) because i=(1-x)y. Its four square corners give source masks {C,I},ALL,{C},{C,BJ}; stage 0 gives empty. Their maximum proves the formula for all real signed normals. QED.

## Theorem 2 — all-signed two-clock hull equivalence and complete classification

Under the standing assumptions, the following are equivalent:

(a) conv O_clock(FULL)=conv O_clock(LR), equivalently h_FULL(a,b)=h_LR(a,b) for every signed real (a,b).

(b) Every proper nonempty strict upper-level set of the source clock vector r is an LR mask in {C},{C,I},{C,BJ}.

(c) The four source clocks have one of EXACTLY these structures:
A: all r_s equal;
B: two levels with high group {C}, {C,I}, or {C,BJ};
C: three levels r_C>r_I>r_BJ=r_IJ, or r_C>r_BJ>r_I=r_IJ.

**Proof.** For T<=0, Theorem 1 gives equality. For T>0, g_s=B+r_s T increases strictly with r_s. Its positive-score set P={s:g_s>0} is a strict upper-level set (or empty/full), with zero-score sources contributing nothing. If (b) holds, P is an allowed mask and the LR and FULL formulas coincide for EVERY signed normal.

Conversely, suppose a proper nonempty upper-level set P is not allowed. The strictly decreasing threshold mu(r)=(9+2kr)/(8(3+r)) lies in (0,3/8) because 0<k,r<1. Choose t in the open gap between its two adjacent threshold values, avoiding all boundaries, and set (a,b)=(t,-1). Then g_s=(2+2r_s/3)*t-3/4-kr_s/6 is strictly positive exactly on P and strictly negative elsewhere. The sign T>0 follows from mu(r)-k/4=(9-6k)/(8(3+r))>0. Since every c_s>0, the sum of positive scores strictly exceeds every allowed LR mask score: the two hulls differ. Thus (a) implies (b). Finally, the only inclusion chains of allowed proper masks are {C} then {C,I}, or {C} then {C,BJ}; their level structures are precisely classes A–C. QED.

The clock result is a scoped exact R² convex-hull statement. No error-coordinate projection or native BRC-source deletion follows from it.

## Theorem 3 — unique highest C produces a strict four-observer fiber residual

Suppose additionally r_C>max(r_I,r_BJ,r_IJ). Then for EVERY independent eight-tuple p_s,q_s in (0,1),

conv O_4(FULL) != conv O_4(LR).

A deterministic FULL point W and the uniquely clock-exposed LR point H have exactly the same (TP,TQ) yet obey

W-H=(13/64,-1/8,0,0).

**Proof.** Since mu(r) decreases strictly, choose mu(r_C)<t<min_{s!=C}mu(r_s). At normal n0=(0,0,t,-1), stage 3 score g_C>0 and g_s<0 for the other sources. Shared stage 1 has t-1/2<0; stage 2 has 2t-3/4<0. FULL uses upstream (x,y,i)=(0,1,1), stage3 only at C, and stage0 elsewhere; call this W. The LR masks have strictly unique best mask {C}; only the LR upstream square corner (x,y)=(1,0) yields that mask. Since the stage-3 upstream objective is multi-affine and the best corner is strict, this corner is the unique real LR time maximizer. Its shared stage3 observer H has w_C=1/8 and all other capacities zero. Both strategies have the same clock readout, S_C and U_C.

Direct substitution in the full four-observer equations gives x_W=0,d_W=5/32, x_H=1,d_H=0. All p/q terms cancel, hence eP(W)-eP(H)=21/128+5/128=13/64 and eQ(W)-eQ(H)=-3/64-5/64=-1/8. The LR convex hull's n0-exposed four-observer face is the singleton {H}. W is in the same supporting hyperplane but differs from H, so W is outside the LR four-observer convex hull. QED.

For rational kernels an explicit four-normal (epsilon,0,t,-1) can be constructed: the LR deterministic vertices outside H have a strictly positive n0-slack, and taking epsilon smaller than every relevant error-coordinate crossing ratio retains H as unique maximizer. This gives quantitative L-infinity distance witnesses.

## Exact certificates for both three-level clock-hull survivors

Take k=1/2, p=(1/4,1/2,3/4,1/3), q=(3/4,1/2,1/4,2/3), t=299/912. In both cases the full and LR CLOCK hulls are the same exact six-vertex rational polygon by Theorem 2.

1. r=(4/5,3/5,1/5,1/5), epsilon=1/1152, n=(epsilon,0,t,-1). Full W=(107/128,211/1536,199/60,1489/480), LR time-face H=(81/128,403/1536,199/60,1489/480). Exact h_FULL-h_LR=13/73728>0; dist_infinity(W,conv O_4(LR))>=247/1861312.
2. r=(4/5,1/5,3/5,1/5), epsilon=1/2432, n=(epsilon,0,t,-1). The same W,H apply. Exact h_FULL-h_LR=13/155648>0; dist_infinity(W,conv O_4(LR))>=39/620224.

The distance inequalities follow from the actual W support surplus divided by the L1 norm of n, by Holder duality.

## Actual exact verification and next frontier

The companion standalone Python standard-library Fraction verifier was executed. It constructs ALL 1536 deterministic FULL and 16 deterministic LR four-observers in each of 51 rational kernels: 24 strict clock permutations, 14 two-level groupings, 12 three-level assignments, one uniform. An exact monotone-chain convex-hull algorithm tests complete planar hull equality, rather than sampling directions. All edge normals of both hull polygons are independently checked against Theorem 1's exact formula. Exactly six kernels pass (3 two-level, 2 three-level, 1 uniform). For both three-level survivors the verifier constructs n0 and a rational mixed normal, checks all four-observer deterministic supports, their explicit W/H vectors, and L-infinity distance lower bounds. The actual stdout in EXACT_OUTPUT.txt ends with 1247 passed exact assertions and PASS_EXACT_R5_K3_ALL_SIGNED_CLOCK_HULL_AND_C_FACE_FIBER. The analytic proof handles the full real parameter domain; computation checks the declared finite rational suite, not independent theorem acceptance.

The remaining wedge/time survivors to study in four dimensions are the two-level groups with high masks {C,I} and {C,BJ}, and uniform clocks. Next derive their exposed clock-face error fibers, mixed signed normals, exact rational LR convex representations or Farkas separators; if full four-hull equality emerges, test actual real behavioral-image nonmembership. The original mother objective remains open.

Native control observation during this run: GitHub connector login awdawmip (repo admin); Enterprise Math Site static_machine_readonly, research_authority_granted=false; active Owner lookup CONTROL_QUOTA. This authored portable checkpoint is not a CLAIM, Result, independent Driver review or canonical mathematical admission. No secrets or permissions were changed.
