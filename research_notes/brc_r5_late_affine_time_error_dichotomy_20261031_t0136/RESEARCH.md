# R5: late-affine terminal-error dichotomy in the off-diagonal genuine STOP tree

2026-10-31 Asia/Shanghai. AUTHOR_PROVED / EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Exact source and authority

Frozen GLOBAL_KNOWLEDGE_V1 main@f7810c5c449b550e1f963383219b6199276a6f73 (00_BOOTSTRAP, OPERATING_MANUAL, P000 and ACTIVE worldview); Enterprise Math canonical main@61c7e9a043a4b1daa49f8d07989f9f1fa4decf88. Relevant current project protocol: docs/PORTABLE_RESEARCH_PROTOCOL.md. Scientific predecessor is the complete 10-facet two-dimensional time-hull equality certificate and exact early-stop-error lift at immutable Enterprise Math commit 31d7a6b703054bb335242312d6bf17f30fbf49e5, directory research_notes/brc_r5_upstream_reweight_clip_20261031_t0043/. Those author-side results are consumed at their proved scope, not promoted to admission.

Authenticated GitHub login awdawmip is not a Source research role. Native em_status reported research_authority_granted=false, executor_binding_configured=false, 5/5 active jobs; native active-task inventory returned CONTROL_QUOTA. No authenticated current native owner, CLAIM, Result, independent Driver review or Foundation acceptance is asserted.

## Fixed finite model

Nature chooses X,U in {0,1}, with Q(00)=Q(11)=49/100, Q(01)=Q(10)=1/100, time-3 likelihood ratios r0=3/4,r1=5/4. At time 4, V in {0,1,2} has likelihood ratio R=(1/2,1,3/2). For t0=1/16 and t1=1/8, the conditional Q child laws are

  K_(x,0)=(1/2+t_x,1/2-2t_x,t_x);
  K_(x,1)=(t_x,1/2-2t_x,1/2+t_x).

Define q_xuv=Q(x,u)K_(x,u)(v), p_xuv=R_v q_xuv. All 12 q,p masses are positive, and both measures normalize. STOP at time 2,3,4 absorbs immediately; time-4 CONTINUE forces STOP at 5. FULL sees full history; LR chooses arbitrary real behavioural probabilities only from (time, likelihood ratio), with no persistent random seed. Each decision key occurs at most once on any path. Let T_M=E_M[tau] and S_M=M(tau=2), M=P,Q.

## Whole late-affine time-only error family

Let epsilon_j in (0,1), j=2,3,4,5, be any real terminal error probabilities shared under P and Q, depending only on actual STOP time, satisfying

  epsilon_3 - 2 epsilon_4 + epsilon_5 = 0.

Put B=epsilon_4-epsilon_3, A=4epsilon_3-3epsilon_4 and c=epsilon_2-2epsilon_3+epsilon_4. The exact pointwise identity

  epsilon_j = A+B*j+c*1_{j=2}

holds at every possible stopping time, so for EVERY real FULL and LR behavioural strategy

  e_P = A+B*T_P+c*S_P,
  e_Q = A+B*T_Q+c*S_Q.

The four-observer is O=(e_P,e_Q,T_P,T_Q).

## Classification theorem (all real parameters)

(I) If c=0, errors are affine in time on the entire four-time support. Every O is in the affine plane e_P=A+B*T_P and e_Q=A+B*T_Q, hence affine rank <=2. The FULL and LR FOUR-OBSERVER CONVEX HULLS are equal because the predecessor proved their (T_P,T_Q) convex hulls equal, and both are mapped by the same affine map. This case does not assert equality of ACTUAL behavioural images.

(II) If c != 0, BOTH full and LR four-observer hulls have affine rank 4 yet are STRICTLY UNEQUAL. Let lambda=1949/2298. Define the signed four-observer readout

  H_epsilon = T_P - (lambda-B/c)*T_Q - e_Q/c
            = T_P - lambda*T_Q - S_Q - A/c.

The exact supports over ALL real behavioural policies are

  sup_FULL H_epsilon = 202049/229800 - A/c;
  sup_LR   H_epsilon = 202000/229800 - A/c.

Thus the EXACT GAP equals 49/229800 > 0 for every legal nonzero c, without parameter sampling. The relevant full-rank LR deterministic policy indices are 0,49,10,66,6 (full bit layout in VERIFY.py). The determinant of the four difference rows in (S_P,S_Q,T_P,T_Q) coordinates is 147/500000, and the linear observer transformation multiplies it by c². Hence

  det[e_P,e_Q,T_P,T_Q] = (147/500000)*c² != 0.

One explicit FULL strategy achieving the support has no early STOP and (T_P,T_Q)=(13539/3200,6323/1600), giving the four-observer witness

  O* = (A+B*(13539/3200), A+B*(6323/1600),
        13539/3200, 6323/1600).

Every real LR observer has L-infinity distance at least

  (49/229800)/(1+|lambda-B/c|+1/|c|)

from O*. This is positive at each fixed legal c != 0. The covector scales like 1/c, so a constant signed support gap does NOT imply a uniform norm gap as c approaches zero.

Consequently NO parameter in this entire strictly-interior late-affine family satisfies the mother target: equal rank-4 four-observer hulls with unequal real behavioural images. The c=0 family fails rank, while c!=0 fails hull equality. The unrestricted strict STOP/CONTINUE mother problem remains open.

## Proof and exact validation

The epsilon identity follows immediately by matching four terminal-time values. In case c=0, applying the same affine map to the two equal 2D time hulls proves the equal four-hull statement and rank bound.

For c!=0, the displayed H_epsilon is H0-A/c, where H0=T_P-lambda*T_Q-S_Q. The predecessor exactly established for epsilon=(3/4,1/4,1/4,1/4) that H_ref=T_P-lambda*T_Q-2e_Q has FULL/LR suprema 87149/229800 and 871/2298. Since e_Q=1/4+S_Q/2, H0=H_ref+1/2, yielding 202049/229800 versus 202000/229800. Every local control appears multiaffinely in expectations because no observation key repeats along a path; therefore a real behavioural support maximum occurs among deterministic policies. This is a complete all-real signed-support proof, not just a rational grid.

The deterministic rank certificate in (S_P,S_Q,T_P,T_Q) has det=147/500000; replacing S_P,S_Q by e_P,e_Q=A+B*T+c*S multiplies the oriented determinant by c². The fixed FULL witness saturates the support, and the signed coefficient L1 norm is 1+|lambda-B/c|+1/|c|, giving the L-infinity distance by Holder's inequality.

The attached Python 3 stdlib-only Fraction/integer verifier independently enumerates all 2^18=262144 FULL and 2^7=128 LR Boolean policies, checks the ten exact previously certified time-hull halfspaces on each policy, computes both H0 extrema and the rational determinant. Five legal exact parameter sets check positive/negative c, late slopes and c=0. Actual stdout is EXACT_OUTPUT.txt, ending PASS_EXACT_R5_LATE_AFFINE_TIME_ERROR_COMPLETE_DICHOTOMY. The continuum statement is established by the algebraic proof, not by five tests.

BRC reuse resolution: REUSE_APPLIED. Keep the 12 positive source-labelled Q/P masses and source-sensitive next-LR kernel residual TV=1/8; analyse the precisely declared stopping-time/error observer and its kernel. The observer equality is not invertibility of provenance-bearing state. No native X6 embedding or physical prediction is claimed.

Next problem: arbitrary common time-only epsilon has two contrast parameters modulo an affine function of time, c=epsilon2-2epsilon3+epsilon4 and d=epsilon5-2epsilon4+epsilon3. This work completely classifies d=0. For d!=0 seek an all-signed Farkas/rational convex-hull criterion across the full (c,d) plane, then real seedless LR image nonmembership only after full rank and all-signed equality are certified. Source owner and independent review remain for the proper native authority.
