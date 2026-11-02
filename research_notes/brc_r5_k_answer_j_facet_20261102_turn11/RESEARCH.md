# R5 — K-answer neutralization transfers the remaining facet to J

Date: 2026-11-02 Asia/Shanghai. Author research status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Source and model

Frozen scientific input remains GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568 and enterprise-math main@86149263e38c22292c9def1e0f69092efa1be77e. Latest verified predecessor is enterprise-math commit a97757c31fb962dd0f36e8e3286b807e74f11f41, research_notes/brc_r5_temporal_face_transfer_20261102_t0740. Current normative context was fetched separately. This is an auxiliary positive two-law BRC stopping model with explicit source provenance, not native-X6 dynamics. P000/ACTIVE worldview unchanged.

Use the predecessor's true time/likelihood-ratio shared decision keys I=(1,1), J=(2,1), K=(3,1), with identical P/Q initial masses 1/2 at I, 1/4 at J via B, 1/4 at K via C. After I continues, equiprobable natural edges reach J via I or K via I; after J continues, equiprobable edges reach a time-3 final answer or K via BJ/IJ. Stop at I,J,K returns answer P. A final answer has law-P probability p of P and law-Q probability q of P, hence e_P=p and e_Q=1-q; terminal time is t3 or t4/t5. A K continuation has time expectation (4+dP,4+dQ).

At fixed predecessor delay lambda=1, all four source-labelled K kernels (p0,q0,dP,dQ) are C:(3/4,1/4,1/4,1/8), I:(1/4,3/4,3/4,1/4), BJ:(2/3,1/3,1/3,1/6), IJ:(1/3,2/3,2/3,1/3). J final answer kernels are B:(2/5,3/5) and I:(3/5,2/5). Every P/Q conditional probability and complement is strictly between 0 and 1. Sources remain separate until the fourfold observation O=(e_P,e_Q,T_P,T_Q). FULL has seven stop variables (x,jB,jI,kC,kI,kBJ,kIJ) in [0,1]^7; LR enforces jB=jI=y and all four K stop variables=z, retaining (x,y,z) in [0,1]^3.

## Theorem 1: complete K-only answer-interpolation envelopes

For each K source independently replace (p0,q0) with (p(s),q(s))=((1-s)p0+s/2,(1-s)q0+s/2), 0<=s<=1, retaining all other probabilities. Let E=e_P+e_Q, and m_X=min_X E, M_X=max_X E, with all *real behavioral policies* included.

For 0<=s<=2/5:
m_FULL=5/6+s/6; m_LR=39/40; M_FULL=7/6-s/6; M_LR=137/120-s/6.

For 2/5<=s<=1:
m_FULL=17/20+s/8; m_LR=39/40; M_FULL=23/20-s/8; M_LR=9/8-s/8.

Thus h_FULL(E)-h_LR(E)=M_FULL-M_LR=1/40 on the *entire* closed interval. In the opposite direction h_FULL(-E)-h_LR(-E)=m_LR-m_FULL equals 17/120-s/6 on [0,2/5] and (1-s)/8 on [2/5,1], reaching zero exactly at s=1.

PROOF: For any fixed deterministic policy, O(s) is affine in s, and at fixed s the observation is multiaffine in its stop parameters, so support extrema over the full real strategy cubes occur at all 128 and 8 deterministic vertices. The complete verifier checks every vertex against each proposed affine envelope at both endpoints of [0,2/5] and [2/5,1] and identifies a *single common attaining deterministic vertex* at both endpoints of every interval, for each of the four envelopes. Affine interpolation proves the claims for all real s on each segment; multiaffine interpolation extends from deterministic vertices to every real policy. The executable Fraction certificate, endpoint-attaining witnesses and actual stdout are supplied as VERIFY.py and EXACT_OUTPUT.txt.

## Theorem 2: closure of -E with rank-four survival, and exact opposite separator

At s=1 every K continuation has p=q=1/2 and E=1. The final J source rewards are E_B=4/5 and E_I=6/5. Source-resolved backward substitution gives, *for every real FULL policy*,

E_FULL(1)=39/40+[jB+(1-x)(1-jI)]/40.

For LR this becomes E_LR(1)=1-x(1-y)/40. Consequently min_FULL E=min_LR E=39/40, max_FULL E=41/40, max_LR E=1. The previous -E support obstruction vanishes exactly, but the +E gap remains 1/40.

The exact FULL policy (0,1,0,0,0,0,0) witnesses W=(51/80,31/80,89/24,337/96), E(W)=41/40. With n=(1,1,0,0) and ||n||_1=2, dist_infty(W,conv(LR))>=1/80. The terminal time mechanisms are unchanged by s; at lambda=1 the two models have min D=0 and max D=7/32 for D=T_P-T_Q, so both signed time supports agree.

At s=1, LR deterministic corners (000,001,010,100,101) have fourfold affine determinant 13/98304!=0. The FULL interior Jacobian at all seven stop probabilities 1/2, columns (x,jB,jI,kC), has determinant 47/1310720!=0. The LR hull is four-dimensional and the FULL real map has a four-dimensional local image. These exact determinants were recomputed with Fraction row elimination and endpoint differences for multiaffine Jacobian columns.

## Theorem 3: uniform J neutralization has an exact dimension-collapse boundary

At s=1, additionally interpolate *both J answer pairs* to (1/2,1/2) with parameter t in [0,1]. Direct source accounting yields for all real policies

E_FULL(1,t)=1+(1-t)[jB+(1-x)(1-jI)-1]/40,
E_LR(1,t)=1-(1-t)x(1-y)/40.

Therefore the positive E support gap is exactly (1-t)/40 and the negative E support gap is zero throughout. Its only zero positive-gap point in this uniform interpolation is t=1; there E(O)=1 for all policies, so both full and LR images lie in the affine hyperplane e_P+e_Q=1 and their ranks are <=3. Strict kernel positivity persists, but this uniform equalization route sacrifices four-dimensionality. This identity is algebraic; the code also checks all vertices at t=0,1/3,2/3,1.

## Theorem 4: J sign alignment removes both E gaps without rank collapse, exposing an oblique separator

Keep lambda=1 and K p=q=1/2. Change only the J B-source final answer pair to (3/5,2/5), equal to the I-source final pair. Preserve both J arrival histories and distinct K time kernels. Exact exhaustive vertex extremization and multiaffinity give min_FULL E=min_LR E=1 and max_FULL E=max_LR E=21/20: both signed E support gaps equal zero.

The LR affine determinant (corners 000,001,010,100,101) is now -49/61440!=0, and the FULL interior (x,jB,jI,kC) Jacobian minor is 23/1966080!=0. Four-dimensional structure survives.

A new, exact signed normal n=(2,-1,1,0) has h_FULL(n)=71/15 and h_LR(n)=93/20, hence support gap 1/12. The FULL policy (0,0,0,1,0,1,0) gives W'=(57/80,27/80,175/48,167/48) with n.W'=71/15. As ||n||_1=4, dist_infty(W',conv(LR))>=1/48. The 128 FULL and 8 LR exact values cover all real behavioral parameters by multiaffinity. This isolates a mixed answer/time obstruction surviving the elimination of both pure answer support gaps.

## Evidence and next question

The actual Python 3 standard-library Fraction checker VERIFY.py produced EXACT_OUTPUT.txt with 1525 assertions and 1888 source-labelled complete observation evaluations, ending in PASS_EXACT_R5_K_ANSWER_NEUTRALIZATION_FACET_MIGRATION. The finite endpoint theorem is extended analytically by affine/multiaffine interpolation; the other fixed-model support claims are exact exhaustive rational vertex results. No external-source or native-HB theorem is inferred.

The mother target is a positive two-measure stopped-branch model in which FULL and LR four-dimensional convex hulls coincide but actual real observation sets differ. This particular construction shows a route from an answer facet to a mixed answer/time facet while preserving rank. NEXT_TASK.md specifies an independent source-specific time-kernel perturbation and the required complete 128-to-8 rational convex-combination/Farkas test.

Service status observed: GitHub authenticated awdawmip with push access. Sites gateway reports static_machine_readonly, research_authority_granted=false, write_relay_enabled=false. Bounded native owner/task enumeration returned CONTROL_QUOTA, so this is portable author-side provenance only: no native activity, CLAIM, Result, Driver review or mathematical admission claimed.