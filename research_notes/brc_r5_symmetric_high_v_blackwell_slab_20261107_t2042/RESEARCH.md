# R5: Exact all-real pointwise Blackwell lifting on a three-parameter high-v slab

Date: 2026-11-07, Asia/Shanghai. Author-side portable proof, not independently reviewed or Source-admitted.

Scientific inputs remain frozen: GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. Current normative context is read separately. Uses the original four-stage seven-LR-key P/Q-BRC stopping observer; predecessor research_notes/brc_r5_residual_halfspace_pointwise_lift_20261107_t2012 at immutable commit 906fd3cc1b8f8f6c5113437617e6938653834ac3, especially REVERSE_CORNER_ALL_SEVEN.md and VERIFY_REVERSE_ALL.py.

## All-real theorem

For every real 0 <= s <= g <= 1, 0 <= z <= s/10, and declaration vector d in [0,1]^7, the legal FULL_HIST flow

    x(g,s,z)=(g,s,s,0,9s/40,0,z)

has a single legal seedless LR flow y(g,s,z), a row-stochastic calibrated 7-by-7 Blackwell channel K from the y stopped-key experiment to the x stopped-key experiment, and d'=Kd in [0,1]^7 satisfying exact four-observer equality

    (e_P,e_Q,T_P,T_Q)(x,d)=(e_P,e_Q,T_P,T_Q)(y,d').

Both stopping times are 1+g+49s/40. The source historical residual is

    R=9bz-4a(v-z)=13sz-9s²/10.

Thus this one theorem includes the strict negative-R region z<9s/130 (for s>0), the seedless boundary, and the strict positive-R region z>9s/130. It extends the predecessor isolated negative-residual corner to a full continuous 3-parameter real region while retaining arbitrary seven declarations.

## Exact observer and transport obligations

The seven LR keys are r=(1/10,1/2,3/4,1,5/4,3/2,19/10). Let M_i be the frozen affine Q stopping masses of the predecessor's VERIFY.py, with sum_i M_i=sum_i r_i M_i=1. For declarations d_i,

    e_Q=sum_i M_i d_i; 1-e_P=sum_i r_i M_i d_i.

A nonnegative transport Q_ij from y to x satisfies for all i,j:

    sum_j Q_ij=M_i(y),
    sum_i Q_ij=M_j(x),
    sum_i r_i Q_ij=r_j M_j(x).

Then K_ij=Q_ij/M_i(y) for a positive-mass input row (identity row when input mass zero) is stochastic. d'_i=sum_j K_ij d_j preserves both P and Q errors for all real declarations, so it suffices to construct Q and match both times.

## Exact construction when R <= 0

For 0<=z<=9s/130, set t=130z/(9s) if s>0 and t=0 if s=0; then 0<=t<=1. Choose

    y=(g,s(19+t)/20,s(19+t)/20,0,s(11-2t)/40,0,s(11-2t)/130).

The seedless condition follows from a'=b' and z'=4v'/13; y is legal, and T_P(y)=T_Q(y)=1+g+49s/40.

Let E0=(0,0,0,1,0,0,0), E1=(0,0,1/2,0,1/2,0,0), the Q experiments of the two identity baseline flows 0 and (1,0,0,0,0,0,0). Let Q1 be the EXACT 7×7 rational calibrated transport in the predecessor REVERSE_CORNER_ALL_SEVEN.md from y1=(1,19/20,19/20,0,11/40,0,11/130) to x1=(1,1,1,0,9/40,0,0). Its precise K entries, multiply by M_i(y1), are reproduced in VERIFY.py here. Set

    x_low=x(g,s,0), x_mid=x(g,s,9s/130),
    y_low=(g,19s/20,19s/20,0,11s/40,0,11s/130),
    Q_low=(1-g)diag(E0)+(g-s)diag(E1)+s Q1,
    Q=(1-t)Q_low+t diag(M(x_mid)).

The source and target flows obey y=(1-t)y_low+t x_mid and x=(1-t)x_low+t x_mid. The Q masses are affine in full flows. Identity baseline transports and Q1 individually satisfy the Q and likelihood-weighted P column conditions. Their nonnegative convex combinations do as well, for all real g,s,t in the declared domain. This proves the full seven-key transport, including the g=s=0 boundary.

## Exact construction when R >= 0

For 9s/130 <= z <= s/10, take y=x(g,s,9s/130). Set delta=(247/1620)(z-9s/130)>=0. The predecessor's exact affine mass formulas give

    M_0(y)=M_0(x)+delta, M_6(y)=M_6(x)+delta,
    M_3(y)=M_3(x)-2delta,
    M_j(y)=M_j(x) for j in {1,2,4,5}.

Start with Q=diag(M(y)), then for i=0,6 move delta from Q[i,i] to Q[i,3]. All entries remain nonnegative. The P weighted column identities follow from r_0+r_6=2r_3; Q and times also match. This is a single seedless Blackwell lift for all declarations.

## Witness and exact execution

At (g,s,z)=(4/5,1/2,3/260), R=-3/20 and T_P=T_Q=193/80. A legal seedless y is (4/5,29/60,29/60,0,31/240,0,31/780), and its calibrated stochastic kernel works for every real seven-declaration vector. For the strict-positive input (g,s,z)=(4/5,1/2,1/20), R=1/10 and delta=19/8100.

VERIFY.py is executed using only Python standard-library Fraction and verifies the predecessor corner rational certificate, the required exact seven row equations, seven Q columns, seven weighted-P columns, 96 rational parameter settings including boundaries in both residual sectors, and all 128 binary declaration combinations at the strict-negative interior example. EXACT_OUTPUT.txt is its captured stdout. The universal theorem follows from the displayed affine identities, not the finite sample.

## Mathematical and control scope

Pointwise equality is established on this specified symmetric high-v slab (g,a,b,u,v,w,z)=(g,s,s,0,9s/40,0,z). Unequal a,b, nonzero u,w, other v and full four-observer image equality remain open. Blackwell equivalence here concerns the fixed seven-key P/Q observer and its declared stopping/decision observations; no native X6 physical-dynamics identity is claimed. GitHub publication is author-side research evidence, with independent mathematical review pending. Native control currently returns BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; active R5 owner and formal CLAIM are unconfirmed.

Next task: exact side-branch nonzero u,w corner tests; see NEXT_UNIT.md.
