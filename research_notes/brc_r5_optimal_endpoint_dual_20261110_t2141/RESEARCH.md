# R5: exact two-parameter seven-dual exclusion envelope and optimal terminal parameter

Date: 2026-11-10 Asia/Shanghai. Evidence: author-side exact rational derivation, independent mathematical review pending.

## Object and immutable scientific provenance

The finite-support seven-likelihood-ratio auxiliary P/Q–BRC Blackwell model has 30 permitted nonnegative transport arcs, 21 marginal/martingale equations (15 rescaled independent rows), five affine physical equalities and 26 capacities. This statistical observer changes neither P000 nor native Heartbeat World X6 geometry. Scientific pins remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e.

Inherited exact author-side evidence: PR #1976, commit b9d0da58b74a18fe45f4b29bb238b70df79b96bc (five-vertex lawful P7, six forced arcs, a seventh separation functional and uniform positive margins); PR #1986, commit 590b50e71a58632b02c5fb930f9a5c8b1c1219f5 (15×8 frozen physical perturbation T, seven exact dual sensitivities); PR #1990, commit 08ae691eaa7406c0f17a963294565e4f0f32f6f2 (lawful P7 to P3(v) bridge); PR #1994, commit 141d99fedb0a818832a54fd92cf0886307bf6708 (uniform in v exclusion envelope). Their original 30-column checks and five-vertex enumeration are not re-executed here.

For p7 in the entire closed P7, v in [1/10,13/40] and t in [0,1], let p(t,v)=(1-t)p7+t p3(v), with p3(v)=(x3(v),x3(v)), x3(v)=(1,1,1,27/80,v,27/80,1/10). Write the 15-row Blackwell transport equation Ce=q(p(t,v)). Perturb only along the same frozen eight directions q'=q(p(t,v))+T delta.

## Theorem 1: complete two-variable reduction for the seven fixed certificates

Let the seven indices be 00,33,43,45,65,66,ell. Each beta_h is the verified exact minimum h·q(p7) across the closed P7; eta_h=||T^T h||_1 is the exact sensitivity. The exact rational beta and eta pairs are literal constants in VERIFY_OPTIMAL_ENDPOINT.py.

Define S(v)=7933/36000+(67/162)(v-1/10). At p3(v) the exact seven terminal evaluations are (S(v),1-2S(v),0,0,0,S(v),0). Therefore define the uniform seven-certificate radius

R7(t,v) = min_h { ((1-t) beta_h + t gamma_h(v)) / eta_h }.

For ALL real t in [0,1], v in [1/10,13/40],

R7(t,v) = min{ ((1-t) beta_66+t S(v))/eta_66, C(1-t) },

where eta_66=1017037/324000 and C=beta_43/eta_43=550609460307500/116839042577461087.

For each 0<=t<1, all p7 in P7, and each real delta satisfying ||delta||_infinity<R7(t,v), every nonnegative transport on the original 30 arcs solving Ce=q(p(t,v))+T delta, if it exists, has at least SEVEN strictly positive edges.

## Theorem 2: globally optimal v and t for this fixed seven-functional test

Set

A=beta_66/eta_66=254087337130964128905/142439520168704998753514;
Bmin=S(1/10)/eta_66=71397/1017037;
Bmax=S(13/40)/eta_66=101547/1017037;
C=550609460307500/116839042577461087.

For each fixed t, the maximum over all permitted v of R7(t,v) is

R_best(t)=min{A+(Bmax-A)t,C(1-t)}.

Its unique global maximum over t in [0,1] is achieved at

v_opt=13/40,
t_opt=(C-A)/(Bmax-A+C)
=27506071400619459894935030258545/965242855541993161664216604137419
approximately 0.028496529389149983,

R_opt=C(1-t_opt)
=4419128514205873438322431365000/965242855541993161664216604137419
approximately 0.004578255605657387.

This is approximately 1.203370395% larger than the previous uniform-in-v certified peak 0.004523817327207455 from PR #1994 and approximately 2.56654 times the old t=0 certificate radius.

Complete fixed-t optimizer classification: at t=0 all v tie; for 0<t<t_opt, only v=13/40 is optimal. Define t_uniform=(C-A)/(Bmin-A+C), exactly 27506071400619459894935030258545/686822379881831688569552660816119. For t_opt<=t<t_uniform, every and only v in [v_req(t),13/40] optimizes, where

v_req(t)=1/10+(162/67)*(((eta_66*C-beta_66)*(1-t)/t)-7933/36000).

For t_uniform<=t<=1, every v is optimal. v_req is only used for positive t in the indicated interval.

## Proof

Each of the six inherited forcing duals y_f has y_f^T C_e<=1_{e=f} for EVERY permitted arc. A seventh functional ell annihilates the six forced columns and detects a further required positive arc. Positivity of all seven evaluations yields the seven-edge lower bound. Their full exact inequalities across 30 columns and lawful bridge/source-lift are inherited from the pinned predecessor evidence. For a physical perturbation delta, each h evaluation is at least

(1-t) beta_h+t gamma_h(v)-eta_h ||delta||_infinity.

For every h in {00,33,45,65,ell}, the excess of the h-radius above the 43-radius equals

D_h(t,v)=((1-t)beta_h+t gamma_h(v))/eta_h-C(1-t).

This is multi-affine in (t,v) on the full rectangle [0,1]×[1/10,13/40]. Its value everywhere is a convex combination of its four corner values. All 20 corner values are >=0 by exact Fraction checks in the verifier. Thus the minimum over seven functionals is exactly the minimum of 66 and 43 everywhere, establishing Theorem 1, including continuum coverage.

The 66 radius is increasing in v for each t>0; the 43 radius is v-independent. Hence at each t the largest possible seven-functional minimum is their envelope at v=13/40. The 66 line A+(Bmax-A)t strictly rises and the 43 line C(1-t) strictly falls, giving the unique exact peak at their intersection. Equality with the 43 ceiling for general v requires S(v)>=(eta_66*C(1-t)-(1-t)beta_66)/t. Solving this equality gives the optimizer threshold v_req(t) and the stated classification.

## Actual verification, boundary and next question

An exact standard-library Python Fraction calculation checked the seven beta/eta input constants, all 20 multi-affine corners, envelope at its breakpoints, exact t_opt/R_opt, and optimizer threshold identities, with output saved in EXACT_OUTPUT.txt. No floating-point tolerance enters a proof assertion. The predecessor mathematical certificates and scientific model remain pinned author-side results; Source formal Result and independent review are pending. This optimized object is the sufficient radius of these SEVEN FIXED functionals, not the true shortest distance to a six-edge physical transport.

Next discriminating research unit: construct a new valid all-30-column rational dual separating functional, optimized against (t,v), and test whether it strictly improves R_opt. Independently reconstruct a lawful 4/5/6-edge transverse departure near p3(13/40), preserving 21 equations, 5 equalities and 26 physical capacities. This tests the gap between the current sufficient radius and a true low-support contact.
