# Enterprise Math R5 — four-parameter collision-preserving support-gap theorem

2026-10-29 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Exact provenance and assumptions

Frozen GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@a6d1b1abccab19686174d6f230b4e6daff4e8d47. Project main: awdawmip/enterprise-math@ffa8e67c108927c3742c9e5e744023185b32b7d7. Relevant controls read: global normative entries, native P000 V5, ACTIVE Heartbeat World, joint-relation observer preservation, portable research. Scientific predecessor (not an accepted Source Result): research_notes/brc_r5_two_sided_tail_bifurcation_20261029_t0940/RESEARCH.md at immutable commit a4d70df58e562ee8154561177f9f82592239c587, Draft PR #1663.

Model: finite horizon t=1..4 with two laws P,Q and LR s=dP/dQ; origins A and B each have Q mass 1/4 and LR 3/2 at t=1, while the remaining Q mass 1/2 terminates with LR 1/2. At t=2 there are paths L at LR 1 and R at LR 3/2, continuing via kernel nu; at t=3 these paths merge at LR 3/2, with an optional t=4 continuation. Full-history behavioral policies remember origin/path; seedless likelihood-ratio (LR) behavioral policies use (time,LR) only, with independent local randomization and no persistent seed. All policy probabilities are arbitrary real numbers in [0,1]. Four readouts O=(e_P,e_Q,T_P,T_Q), e_P=P(declare Q), e_Q=Q(declare P).

Terminal signature set S=(1/2,1,3/2,5/2). Under Q, rows (in S order):

~~~text
mu_A      7/50       11/75       1/2        16/75
mu_B      17/200     23/150      3/5        97/600
nu_A,L    1/2        1/6         1/4        1/12
nu_B,L    5/12       1/3         1/6        1/12
nu_A,R    17/100     23/75       1/5        97/300
nu_B,R    31/120     5/18        1/15       143/360
eta_A     1/8        1/4         3/8        1/4
eta_B     5/32       3/16        13/32      1/4
~~~

P conditional law after parent LR r is Q(s)*s/r. Every row is strictly positive, sums to one, and has first s-moment equal to parent r (mu:3/2, nu L:1, nu R:3/2, eta:3/2). The full policy can select different decisions at the merge for different paths and origins; seedless LR policy shares one coin.

The t=3 source Q masses are the BRC-labelled positive quantities

x_A=41/1200, x_B=59/3600,

where x_i=(1/4)[mu_i(1)*nu_i,L(3/2)+mu_i(3/2)*nu_i,R(3/2)]. Their labels/provenance remain present until the four-observer readout.

## New four-dimensional real parameter family

Define moment-null tangent directions d1=(1,-2,1,0) and d2=(1,0,-2,1). Take any four independent REAL parameters a_A,b_A,a_B,b_B in [-1/1000,1/1000] and replace both terminal kernels by

eta'_i = eta_i + a_i*d1 + b_i*d2.

Both directions have zero row sum and zero signed-LR first moment; all entries of eta'_i stay strictly positive throughout the entire real parameter box. Hence the normalization under both measures and every designated LR collision remain unchanged. This is a four-dimensional relative-open neighborhood of the baseline inside the collision-preserving affine manifold, not an unrestricted open ball of arbitrary kernels.

Put

I_A=1/8+a_A+b_A,   I_B=5/32+a_B+b_B,

V0(theta)=2429/1800+(37/20)*theta,

L_theta(O)=2e_P+2e_Q+theta*T_Q.

THEOREM. For every real point in the four-dimensional box and every theta in [I_A,I_B] INTERSECT [1/8,5/32], minimization over ALL REAL behavioral policies gives

~~~text
V_full = V0(theta)+x_B*(theta-I_B)
V_LR   = V0(theta)+min(0,x_A*(theta-I_A)+x_B*(theta-I_B))
Delta(theta)=V_LR-V_full
            =min(x_A*(theta-I_A), x_B*(I_B-theta)).
~~~

The unique optimizing signed direction in this interval is

theta_star=(x_A*I_A+x_B*I_B)/(x_A+x_B),

and its exact support gap equals

Delta_star=(2419/218400)*(I_B-I_A)
          =(2419/218400)*(1/32+a_B+b_B-a_A-b_A).

Consequently, across the entire REAL parameter cube,

263671/873600000 <= Delta_star <= 341079/873600000,

with the lower bound STRICTLY positive. Thus full-history and seedless-LR four-observer convex hulls are unequal at every point of this four-dimensional family. Every member is a certified NO-GO candidate for the mother problem requiring equal convex hulls.

## Proof for all real parameters and all real behavioral randomizations

1. At terminal LR s and time t, relative to the all-Q declaration baseline, the minimised signed cost is f_t(s)=theta*t+g(s), g(s)=min(0,2-2s). Optimal terminal action declares P when s>1 and Q when s<1. Extra local declaration randomization does not improve a linear minimum.

2. For source i, continuing rather than stopping at the merged t=3 LR state changes the conditional Q-scaled objective by

D_i(theta) = SUM_s eta'_i(s)*f_4(s)-f_3(3/2) = theta-I_i.

To check the identity, SUM d1=SUM d2=0, SUM_s s*d1(s)=SUM_s s*d2(s)=0, and SUM_s d1(s)*g(s)=SUM_s d2(s)*g(s)=-1. The perturbation therefore shifts the threshold exactly by a_i+b_i. This equality is algebraic, not a derivative approximation.

3. Check upstream decisions without falsely forcing full-history downstream coins to agree. Let gamma_L,gamma_R be independent arbitrary real probabilities for continuing at t=3 after paths L,R. At each source i define M_i,L, M_i,R and M_i,root as the conditional STOP cost minus CONTINUE cost. These values depend separately affinely on a_i,b_i,theta,gamma_L,gamma_R. Their minima on the product of five real intervals occur at its 2^5=32 vertices per source. Full exact Fraction calculation in VERIFY.py gives the six GLOBAL minima:

~~~text
origin              M_L                 M_R              M_root
A                5367/16000          71/10000          14599/400000
B                3121/12000          2039/20000        53639/1800000
~~~

Every margin is strictly positive, simultaneously for arbitrary independent full-history path coins. Consequently root and both t=2 branches strictly continue for BOTH policy classes, for every parameter in the cube and all theta in [1/8,5/32]. A sourcewise dominance bound also applies to any LR information aggregation because the Q weights are positive.

4. Fixing upstream continuation leaves the common t=3 LR decision. The counterfactual 'stop at the merge' baseline is V0. The full-history optimum is V0+min(0,x_A D_A)+min(0,x_B D_B), whereas the LR optimum is V0+min(0,x_A D_A+x_B D_B). Since theta lies between I_A and I_B, D_A>=0 and D_B<=0. Subtracting gives the two affine opposing terms of Delta(theta).

5. The two positive affine pieces meet at theta_star=(x_A I_A+x_B I_B)/(x_A+x_B). Since x_A*x_B/(x_A+x_B)=2419/218400, the claimed formula follows. Across the parameter cube, I_B-I_A lies in [109/4000,141/4000]. Moreover theta_star differs from the baseline 787/5824 by at most 1/500, so it stays in [1/8,5/32] and between I_A and I_B. The uniform strict lower/upper gap bounds are immediate. This completes the universal-real proof. QED.

## Explicit four-observer witness and exact separation

Take the full-history policy: all upstream nodes continue; at merged t=3 states only origin B continues; at terminal signatures s>1 declare P, otherwise Q. Its observer is

~~~text
O_B = (
  98731/230400 + (59/7200)*(-3*a_B+b_B),
  627/2560     + (59/3600)*(a_B-b_B),
  5429/2400,
  6719/3600
).
~~~

The time coordinates are unchanged by the moment-null perturbations. At theta_star this policy attains V_full. Every seedless LR policy has L_theta_star(O)>=V_LR, hence by the dual-norm inequality

||O-O_B||_infinity >= Delta_star/(4+theta_star)
                   >= 263671/3630900000 > 0.

This is a genuine observer-distance, full-real-strategy certificate; neither finite probability grids nor latent source-flow nonconvexity are being substituted.

## Executed exact verification, science comparison, control boundary

VERIFY.py is the exact executed Python Fraction verifier; EXACT_OUTPUT.txt contains its actual stdout. It checks Q/P moment normalization, positivity, both moment-null directions, all 32 affine corners per source, 625 rational four-parameter sets including all 16 box vertices, and all 16 deterministic LR upstream policies at each sample, together with the full-history four-vector witness and formulas. All real parameters are proved by the independent affine-corner and algebraic reasoning above, while the 625 checks test arithmetic/implementation.

Scientific context, not a novelty or isomorphism claim: Anderson, Ryan A. and Guido Montúfar, 'The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes,' Proceedings of ICML 2026, PMLR 306:2677–2715 (2026), https://proceedings.mlr.press/v306/anderson26a.html. Their study concerns semialgebraic value sets of memoryless stochastic policies in infinite-horizon POMDPs; this note concerns exact dual-law finite-horizon four-observer support separation.

BRC is applied as positive source/path retention with exact future observer scope. No native X6 / physical interpretation has been derived. Current gateway 2026-10-29 reports research_authority_granted=false and UPSTREAM_CODE_REVIEW_REQUIRED; current active-owner query returned CONTROL_QUOTA. This author-side PR preservation grants no Source Owner, CLAIM, Result, mathematical acceptance or independent Driver review; original research identities are not borrowed. No credentials or sharing changes are made.

Next problem: use this whole relative-open no-go parameter cube for exact pruning of multi-merge candidates. Seek genuinely different architectures where ALL signed full deterministic observer vectors admit rational convex representations by LR deterministic vertices (at most five per point); then—and only then—test actual real four-observer image nonmembership by a certified semialgebraic method. A finite signed-direction sweep or source-flow nonconvexity is not sufficient.
