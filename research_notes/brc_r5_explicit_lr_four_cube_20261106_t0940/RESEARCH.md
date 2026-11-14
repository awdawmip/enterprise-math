# R5 — An explicit rational four-dimensional box in the seedless LR actual behavior image

Date: 2026-11-06 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Question and scope
This is a new quantitative local-result theorem for the strictly positive rational four-stage P/Q stopping experiment at δ=1/4 in the existing R5 mother research. Its observable is (W=(e_P,e_Q,T_P,T_Q)), where e_P is the P-probability of declaring Q and e_Q the Q-probability of declaring P. Full-history decisions retain ordered branches; seedless LR decisions depend only on the current observed likelihood-ratio key. The statement concerns the auxiliary P/Q positive-mass BRC observer, not native X6 Heartbeat dynamics.

Scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate frozen scientific predecessor: `02e1b1263649e6bef8c2acf16212a54ffb9dd851`, especially `research_notes/brc_r5_interior_time_j_thickness_20261106_t0840/RESEARCH.md`. Source registration of this research turn: Researcher-ID `EM-DIRECT-2775A0`, Activity-ID `RA-B178AB36239FA3EAB59B322D`; source activity registered at `7c7cddd4e25c3d8a912e2ec4cbb6fecd29737c4a`.

## Theorem: closed four-dimensional LR box, radius 1/148
In the fixed R5 δ=1/4 experiment, put `W_*=(1/2,1/2,15/8,15/8)` and `h=1/148`. Every four-vector of **real** numbers with
`
|e_P-1/2| <= h, |e_Q-1/2| <= h,
|T_P-15/8| <= h, |T_Q-15/8| <= h
`
is realized by one legal, seedless LR randomized stopping-and-declaration policy. Consequently the entire closed `l_infty` four-cube is included in both seedless LR and FULL_HIST actual observation images.

An explicit inverse policy is as follows. Set `a=T_P-15/8`, `b=T_Q-15/8`, `c=e_P-1/2`, `d=e_Q-1/2`. In the earlier six-flow notation `x=(g,u0,u1,X0,X1,X2)`, choose
`
g = 1/2 + 3b - 2a,
u0=u1=1/4, X0=27/640, X1=13/320,
X2=27/640+2(a-b).
`
Let `M_1` be the **total** stopped Q mass at likelihood ratio 1, including the root, time-3 ratio-1 stop key and time-4 ratio-1 terminal key. The prior affine seven-ratio mass formula gives
`
A=u0/10, B=9u1/40, alpha=47/180, beta=67/162,
J_LR=X1*(alpha*A+beta*B)/(A+B),
M_1=(1-g)+V1+382*(X0+X2)/900-2*J_LR.
`
Here A+B=V1=13/160>0. At **every** stopped key with ratio 1, use one common P-declaration probability
`
t_ratio1 = 1/2 + (-4c-3d)/M_1.
`
At the time-2 stop key with first branch i=0 declare P with probability
`
t_stop0 = 1/2 + 8(c+d)/(g-1/4).
`
At every other stopped LR key (except ratio 1 and the time-2 ratio 3/4 key) declare P with probability exactly 1/2. Whenever a LR continuation key has Q mass V_j, use continuation probability X_j/V_j (all V_j are strictly positive here). At time-1 key i use continuation u_i/g. These are shared likelihood-ratio-key policies, with no hidden history-dependent downstream choices.

For this *fixed four-control inverse section* the claimed cube radius is optimal: arbitrarily increasing h beyond 1/148 makes the displayed t_stop0 invalid for some cube target while all other flow coordinates remain meaningful locally. No maximality among all LR strategies is asserted.

## Proof
The exact time observations from the frozen model are
`
T_P=1+g+(3u0+5u1)/8+X0/2+X1+3X2/2,
T_Q=1+g+(u0+u1)/2+X0+X1+X2.
`
The central flow C is
`
(1/2,1/4,1/4,27/640,13/320,27/640),
`
with `T_P=T_Q=15/8`, and the Q capacities are `V=(27/320,13/160,27/320)`. Keeping u_i,X0,X1 fixed, the displayed g and X2 shifts yield exactly `ΔT_P=a`, `ΔT_Q=b` by direct substitution.

The time-2 first-branch LR key has P and Q stopping masses `3(g-1/4)/8` and `(g-1/4)/2` respectively (initial P,Q masses of this branch are 3/8,1/2). The total stopped Q mass at ratio 1 is `M_1`, as defined above; by the likelihood-ratio identity its stopped P mass is also `M_1`. Importantly the seedless declaration probability at ratio 1 is **shared across all times**. All other stopped LR-key declarations remain at 1/2. Since each P,Q stop-time law has total mass one, the baseline errors are exactly `(1/2,1/2)`. If `r=t_ratio1-1/2` and `s=t_stop0-1/2`, the only error changes are
`
c=-M_1*r-3(g-1/4)s/8,
d=M_1*r+(g-1/4)s/2.
`
Adding gives `c+d=(g-1/4)s/8`. Substitution then gives the displayed unique inverse r,s. Thus every target W is obtained algebraically.

It remains to check that this is a genuine all-real strategy. For `|a|,|b|,|c|,|d|<=h`,
`
|g-1/2|<=5h, |X2-27/640|<=4h.
`
At h=1/148 the bounds imply `1/4<g<1`, and `0<=X2<=27/320`, because `4/148=1/37 < 27/640`. X0,X1 are exactly half their unchanged Q capacities. Hence all six flow constraints hold.
Moreover
`
|s| <= 16h/(1/4-5h) <= 1/2,
|r| <= 7h/(1/2-5h) <= 1/2,
`
The second bound uses `M_1 >= 1-g` because the root mass `1-g` is a nonnegative component of the ratio-1 aggregate; all seven aggregate masses are nonnegative in this legal LR flow. The first final inequality is equality when h=1/148, and the second follows from h<=1/38. Therefore all declared probabilities belong to [0,1]. The conditional kernels are the previous strictly positive normalized q3 rows, with likelihood-ratio moments
`sum_j q3[i,j] * (1/2,1,3/2)[j] = (3/4,5/4)[i]`.
The q3 kernels and their P counterparts are unchanged. The argument is exact over all real target W in the cube, including its boundary. QED.

For the stated inverse controller, consider the joint deviations `(c,d,a,b)=(h,h,h,-h)`. They force `g=1/2-5h` and `s=16h/(1/4-5h)`. For h strictly above 1/148 and sufficiently close, s>1/2, so t_stop0>1. This establishes local optimality of the certificate under the prescribed inverse formulas.

## Verification
The accompanying executable `VERIFY.py` uses Python `fractions.Fraction`. It checks Q transition kernels and LR-moment identities, all seven stopped ratio masses and P/Q normalization, the exact capacity constraints, all 16 cube corners and all 81 {-1,0,1}^4 grid positions, the full seven-ratio recomputed error and timing observations, and the sharpness witness at h=1/147. Its deterministic output is in `EXACT_OUTPUT.txt`, with marker `PASS_EXACT_R5_QUANTIFIED_FOUR_DIMENSIONAL_LR_BOX_FULL_KEY_SHARING`. The proof of the entire real cube rests on the analytic bounds above; the finite computation checks implementation and concrete boundary cases.

## Consequence for R5
Any putative `FULL_HIST \ LR` witness in this fixed model is necessarily outside this explicit rational four-cube. The exact R5 mother question remains to be decided by solving the seven-variable polytope K(W) / one-quadratic-residual sign problem on other observation targets. This box gives a directly testable exclusion and an explicit rational inverse map (for rational targets), in addition to prior nonquantitative full-rank interior patches.

### Verification correction (same turn)
The original draft changed the root's ratio-1 declaration without changing other stopped occurrences of the same ratio. That violated the seedless LR key-sharing condition. The corrected proof above replaces root mass by the **full** ratio-1 mass `M_1` and the checker reconstructs all seven aggregate stopped-ratio masses. This correction preserves the exact 1/148 cube theorem and its bounds; it supersedes the draft at commit `556e556e71d8c4ebdbaffe3c08274f720f4f4c1c`.
