# R5 K3 — common clock-threshold slice: exact all-real time-hull classification

Date: 2026-11-04, Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Scientific input pins (immutable): GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e.
Current control/normative sources read separately: GLOBAL_KNOWLEDGE_V1 main@9ca4f1ad00ebb3d774a8e946a92609217e672d07; Enterprise Math main@10cb2e6abc7a5d29f053f970397d712dd758d10a.
Predecessor: research_notes/brc_r5_k3_general_threshold_mask_20261104_t0543/RESEARCH.md, immutable commit f29e236ed7f32328f3550be31c6c09b5459b4f08. Do not mutate P000, ACTIVE worldview, source pins or task records.

## Object, observers, and exact quantifiers

The exact K3 auxiliary two-law common-terminal-label model has sources S=(C,I,BJ,IJ) with positive capacities c=(1/8,1/6,1/16,3/32). FULL upstream variables satisfy 0<=x,y<=1, 0<=i<=1-x; seedless LR requires i=(1-x)y. Source weights are w=(1/8,(1-x)/6,y/16,3i/32), and d=y/16+3i/32. FULL chooses source-specific local continuation (z_s,t_s,u_s) in [0,1]^3, whereas seedless LR uses common (z,t,u). Let M_s=w_s z_s, S_s=(2/3)M_s t_s and U_s=S_s u_s. For independently chosen r_s,v_s,p_s,q_s in (0,1),

 eP=107/128-21x/128+d/4-(sum S_s)/2+(sum p_s S_s)/8;
 eQ=13/64+3x/64-d/2+(sum S_s)/8+(sum q_s S_s)/32;
 TP=3+sum M_s+(3/2)sum S_s+sum r_s U_s;
 TQ=3+(sum M_s)/2+(3/8)sum S_s+(sum v_s U_s)/4.

The clock projection O_clock is (TP,TQ). The results quantify over ALL real admissible upstream and local behavioral policies. They are internal to this auxiliary experiment; no native Heartbeat X6 embedding or physical calibration is asserted. All BRC provenance sources remain distinct; the projection is explicitly observer-scoped.

## Main theorem: exact equality classification on a common-mu slice

Assume the four clock thresholds are equal:

  mu_s=(9+2v_s)/(8(3+r_s)) = mu  for s in S,

with 0<r_s,v_s<1. Equivalently, v_s=(8mu(3+r_s)-9)/2, with all four resulting v_s strictly between zero and one.

Then

  conv O_clock(FULL) = conv O_clock(seedless LR)

IF AND ONLY IF r_C=r_I=r_BJ=r_IJ (and therefore v_C=v_I=v_BJ=v_IJ).

In particular, ANY unequal r_s on this common-mu slice yields a strictly separating signed clock normal n=(0,0,-tau,1), for some 0<tau<1/2, independently of all eight terminal error parameters p_s,q_s. Consequently the full four-observer convex hulls are also strictly different in that case.

### Support reduction

For n=(0,0,-tau,1), drop the common baseline 3(1-tau). Per unit source weight the four deterministic stage gains (stop immediately, stop after stage 1, stop after stage 2, continue through stage 3) are

  g0=0,
  g1=A(tau)=1/2-tau,
  g2=B(tau)=3/4-2tau,
  g3=C_s(tau)=3/4+v_s/6-(2+2r_s/3)tau.

FULL can attain simultaneously all capacities c_s by x=0,y=1,i=1; each source independently takes its best positive stage. Thus

  h_FULL(n)=3(1-tau)+sum_s c_s max(0,A,B,C_s).

LR local actions share one stage. Since its stage probabilities and upstream weights are multi-affine in the real behavioral parameters, maxima occur at deterministic local stages and the four upstream (x,y) corners. The possible stage-3 source masks are M={empty,{C},{C,I},{C,BJ},S}; stages 1 and 2 can attain all capacities c_s. Therefore

  h_LR(n)=3(1-tau)+max(0, c_total*A, c_total*B, max_{D in M} sum_{s in D}c_s C_s),

where c_total=43/96. This formula is exact over real policies, not merely tested rational strategies.

### Mixed-stage separation lemma

If, for some tau, J=max(0,A(tau),B(tau))>0, and the source set contains both a source with C_s(tau)>J and another with C_t(tau)<J, then h_FULL(n)>h_LR(n).

Indeed, at full positive capacities FULL selects stage 3 for each C_s>J, and the baseline stage achieving J for each C_t<J. Every LR deterministic policy uses one common stage. Stage 0, 1 or 2 misses a strictly positive high-source improvement. A stage-3 policy also falls strictly short on a low source: its contribution is either w_t C_t (<= c_t C_t when C_t>=0) or zero, and either choice is strictly smaller than c_t J; the other source contributions cannot exceed their FULL source maxima. All c_s are positive, and the finite deterministic LR maximum is therefore strictly smaller. Multi-affinity extends the conclusion to all real behavioral policies.

### Construct a mixed stage for every unequal common-mu clock

Since r_s>0 and v_s<1, mu<11/24<1/2. Put

  alpha_s = v_s/(4r_s),
  nu_s=(3+2v_s)/(4(3+2r_s)).

Direct exact identities give

  C_s-B = (2r_s/3)(alpha_s-tau),
  C_s-A = (1+2r_s/3)(nu_s-tau),

  nu_s = [2mu(3+r_s)-3/2]/(3+2r_s),
  d nu_s / d r_s = (3-6mu)/(3+2r_s)^2 > 0.

Consequently, if the r_s are unequal, the nu_s are strictly ordered along the distinct r_s.

CASE 1: all v_s>=r_s. Then every nu_s>=1/4 and nu_s<1/2. Choose tau strictly between min nu_s and max nu_s, avoiding the endpoints. Since 1/4<tau<1/2, J=A(tau)>0 and A>B. The identity C_s-A changes sign across the sources; apply the lemma.

CASE 2: all v_s<=r_s. Then mu<3/8, every alpha_s<=1/4, and the common-mu equation gives

  alpha_s = mu + (3mu-9/8)/r_s,
  d alpha_s / d r_s = (9/8-3mu)/r_s^2 > 0.

Hence alpha_s are not all equal. Choose tau strictly between min alpha_s and max alpha_s. Because 0<tau<1/4, J=B(tau)>A(tau),0. The identity C_s-B changes sign; apply the lemma.

CASE 3: at least one v_s>r_s and at least one v_t<r_t. Choose tau=1/4. Then A=B=1/4>0 and C_s-B=(v_s-r_s)/6 has both strict signs; apply the lemma.

The three cases exhaust all possibilities, including v_s=r_s at some sources. Therefore every nonconstant r_s on the common-mu slice has a strict time-hull separation.

Conversely, if all r_s coincide, the common-mu relation forces all v_s to coincide. In any signed clock direction (a,b), the four stage gains are then identical across sources. FULL's maximum is c_total times the best nonnegative gain, achieved at full capacities. LR achieves the same support with the identical common stage and upstream x=0,y=1. Thus the clock convex hulls agree in every signed direction. QED.

## Exact finite regression, with four independent rational witnesses

The Python standard-library Fraction companion enumerates 1536 deterministic FULL and 16 deterministic LR vectors for each rational model, independently computes both support maxima, and checks the analytic support formulas and actual FULL witness.

1. SUBCRITICAL: mu=1/3, r=(1/2,3/5,3/4,9/10), v=(1/6,3/10,1/2,7/10); tau=1/7; FULL stages=(2,2,3,3). Exact clock support gap 7/1920. An actual FULL four-vector is W=(10261/13824,9263/55296,239/60,1609/480); L-infinity distance from LR four-hull >=49/15360.
2. CROSSING: mu=7/20, r=(3/10,1/2,4/5,9/10), v=(3/25,2/5,41/50,24/25); tau=1/4; stages=(1,1,3,3). Gap 11/9600; distance >=11/12000.
3. CRITICAL: mu=3/8, r=(1/5,1/3,1/2,3/5), v=(3/10,1/2,3/4,9/10); tau=11/40; stages=(1,1,3,3). Gap 83/43200; distance >=83/55080.
4. SUPERCRITICAL: mu=2/5, r=(1/10,1/5,1/4,2/5), v=(23/50,31/50,7/10,47/50); tau=5/16; stages=(1,1,3,3). Gap 7/7200; distance >=1/1350.

Each bound follows from a genuine n-support gap and ||n||_1=1+tau, with n carrying zero error-coordinate coefficients. The unequal error probabilities used for two cases show that the time result is independent of p_s,q_s; the theorem itself already establishes all-real parameter independence. The 4 exhaustive rational instances verify the instances, not the continuous theorem. Execution stdout is preserved literally in EXACT_OUTPUT.txt.

## Scientific consequence, next and authority

The predecessor's necessary condition for full four-hull equality was: either all mu_s coincide OR min_s mu_s>=3/8. This note resolves the unequal-clock part of its first alternative: all mu_s equal and r_s unequal implies strict separation. The remaining candidate clock domain for full four-hull equality therefore has either uniform (r_s,v_s) or min mu_s>=3/8 with nonuniform thresholds. Continue by pruning the second region with stage-1/stage-3 and stage-2/stage-3 signed normals, and, for survivors, exact all-signed four-hull primal/Farkas certificates before testing the real observer image.

GitHub connector identity awdawmip had push/admin permission at this run. Enterprise Math Site reported static_machine_readonly / research_authority_granted=false; owner list returned CONTROL_QUOTA. This is source-preserved author research, not native CLAIM, Result, independent Driver review or mathematical admission.
