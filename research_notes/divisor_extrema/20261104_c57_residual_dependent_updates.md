# C57: residual-dependent updates and score-matched calibration

Progress-Event-ID: prime-c57-residual-updates-20261104-a1
Date: 2026-11-04 Asia/Taipei
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING
Researcher-ID: EM-DIRECT-74BABD / TASK_RESEARCH
Research-Activity-ID: RA-C90E164C9C5831A6B24570D9
Global-read: 2827dbd8bdd216a1135fade833ca64144cd0c526
EM-read: 82205c53d6ae2c00213796b7c138d398b198e51a
Pre-publication-main: b1e9b17746ff1cdd22e80e6c80b420a029783558

## 1. Scope and inherited frontier

Continue C56 at EM commit385c69228b3e63dd449d5a5f505aff3fb53ab2f5, research_notes/divisor_extrema/20261103_c56_approximate_synchronization.md, blob69667f08ad587e40fc4b9d5249cd74e51123a010, and the mounted reproduction archive. The parent question concerns whole-path conditions, local ordering and predictive stability of prime/composite joint paths.

Keep all different complete words in prime types(2,3,5,7). Xpq counts p-before-q occurrence pairs. At total counts(a,b,c,d), A=2(X23-X25+X27+X35-X37)-(ab-ac+ad+bc-bd), B=2X57-cd. Positive selected probabilities are Q(w)=P(w)W(A,B)/Z, with the same strictly positive terminal W at each score. Main calibration requires neither evenness nor a quadratic W. Full provenance, signed scores, positive masses and rho_1 remain distinct. Words and memory are internal records over the retained Heartbeat X6 Cell, not new spatial axes or a physical time law.

## 2. Residual-matched channels in one target

Use the C56 calibrated response rates z=(1/4,1,4) and complete tails557/575/755:
T=[[1/15,4/15,2/3],[1/3,1/3,1/3],[32/45,8/45,1/9]], detT=-1/15.

Memory ell is in{0,1,2}:2 increments it capped at2; the first two3s reset it to0 for preparation; later3s retain the old state with probability e(xi), otherwise reset0;5/7 preserve it. State0 is absorbing under3. The feedback coordinate, evaluated before the new3, is xi=2X23-n2*n3. Reference next-symbol probabilities are rates(1,1,z_ell,1) times remaining counts, normalized.

At target302400=2^6*3^3*5^2*7, the following histories all reach576. Each row lists pure states0,1,2:
xi0:32222223,23222232,22322322;
xi2:23222223,22322232,22232322;
xi4:22322223,22232232,22223322.
Their X23 values are6,7,8. Append3 and a complete tail. For a fixed xi the three final columns have scores(xi+3,2),(xi+3,0),(xi+3,-2), independent of the history row.

Thus Q_xi(i,j)=a_i(U_xi T)_ij W(xi+3,Bj)/Z, with U_xi=[[1,0,0],[1-e,e,0],[1-e,0,e]]. Within each xi, rhat_ij=(Q_ij/Q_0j)T_0j, row normalization and multiplication by T^-1 recover U_xi. Known T and the unchanged reference state0 are the calibration premises.

The four-probability ratio C_xi=Q20 Q02/(Q22 Q00)=(6+58e)/(6-5e), so e=6(C_xi-1)/(5C_xi+58). Prefix probabilities, terminal selection and Z cancel within each residual layer.

## 3. Feedback fit, holdout and deterministic errors

For the declared candidate e(xi)=1/(a0+b0*xi^2), a0>=1,b0>=0, two levels recover a0=1/e0 and b0=(1/e2-1/e0)/4. The third level must satisfy1/e4=4/e2-3/e0.

Example a0=4,b0=1 gives e0=1/4,e2=1/8,e4=1/20 and C=(82/19,106/43,178/115). With each of four probabilities within1% relative error, outward retention intervals are[.2397902,.2603984],[.1175609,.1326348],[.0446667,.0554989]. They are pairwise disjoint. The first two layers predict e4 in[.0444363,.0566667]. The distinct positive candidate1/[4+xi^2+xi^2(xi^2-4)^2/192] agrees at0 and2 but gives1/32 at4; its1% interval[.0264947,.0361586] is disjoint from that prediction. These are deterministic input budgets, not sampling confidence intervals.

A cross-score confounder is exact: true e=1/4, common W=q^[(A+gamma B)^2], q=9/10,gamma1/2. Borrowing the xi0 anchor for the xi2 state2 row gives C_bad=(82/19)(9/10)^8. The incorrect inverse returns e about.0764884733524. Using the separate matched anchor in each layer recovers1/4 in both. Different score layers generally have different terminal column multipliers.

## 4. Necessary state repair

Histories25332 and32325 both reach180, have identical counts, current(A,B)=(-2,0), and old memory ell1. Their local xi values are0 and-2. Complete both to18900 with suffix357 or375. In the example feedback their retention probabilities are1/4 and1/8. The subsequent57/75 odds are11/29 and19/61; the selected four-word cross ratio is671/551 for every common positive terminal W.

Therefore(counts,A,B,ell) is insufficient for this feedback. Adding X23, equivalently xi at known counts, makes emissions, score updates, latent updates and terminal readings factor through the state. Induction on remaining length proves future sufficiency for the declared operations. The new DP retains(counts,partial A,partial B,X23,ell); signed labels do not cancel positive branch mass.

## 5. General positive first-reset formula

For target family N_k=576*3^k*5^2*7 and matched words h_i(d0)3^k c_j, the jth update sees d_j=d0+6(j-1). Let e_j=e(d_j), E_k=product_(j=1)^k e_j, and w_j=(1-e_j)product_(l<j)e_l. Let R_i(n)=product_(h=1)^n(h+2z_i+1)/(h+2z0+1).

Conditioned on observing the common block3^k, the surviving nonreference state probability is exactly
p_i(k)=E_k/[E_k+sum_(j=1)^k w_j R_i(k-j)].

Proof: split the positive path mass by the first reset location, retaining every state-dependent likelihood of selecting3. Equivalently, at step j with n=k-j+1 remaining3s,
p_j=e_j p_(j-1)L_i(n)/[(1-p_(j-1))L0(n)+p_(j-1)L_i(n)], p0=1,
where L_i(n)=n/(n+2z_i+1). Both formulas are checked independently.

For z_i>z0, positive e_j and E_k->0, R_i is increasing, R_i(k-j)/R_i(k)->1 for fixed j, and sum_j w_j=1. Dominated convergence gives p_i(k)~E_k/R_i(k). The standard Gamma ratio then gives
p_i(k)~Gamma(2z_i+2)/Gamma(2z0+2)*E_k*k^[-2(z_i-z0)].
Thus the actual update product and the common-history likelihood correction remain separate. The constant-retention case reproduces C56.

Because L_i<=L0, p_i(k)<=E_k. For reciprocal-quadratic feedback, d0>=0,b0>0 and visible count6,
p_i(k)<=[a0*(36b0)^(k-1)*((k-1)!)^2]^-1.

Main example d0=0:
k1:p1=p2=1/4;
k2:p1=1/232,p2=1/520;
k3:p1=35/1749212,p2=7/1725532;
k5:p1=77/1271718455892,p2=1/304882427060;
k10:p1=1463/796730941381857238197209671832,p2=19/2112427074599864594849931689560.

The three response rows are T0,T0+p1(T1-T0),T0+p2(T2-T0), with determinant p1*p2*detT. Every finite k has rank3 when all e_j>0. Under any common positive terminal selection, the row-to-reference total variation is bounded by tanh(logH_i/4)<=(H_i-1)/4, where H1=(2+8p1)/(2-p1),H2=(6+58p2)/(6-5p2). Small residual mass is never clipped.

## 6. Same-target last-update reconstruction

Compare h_i3^k c_j and h_i3^(k-1)c_j3 inside the same N_k. Both panels have history-independent column scores. The delayed panel uses the known substochastic tail kernel H_i=P(5573,5753,7553|state i, remaining3/5/7=1/2/1). Reference-row correction, multiplication by H^-1, then normalization recover the pre-last3 state probability p^-. The early panel with T recovers p^+.

With l_i=1/(2+2z_i), the actual final update is
e_last=p^+[(1-p^-)l0+p^-l_i]/(p^-l_i), p^->0.

This avoids replacing the pre-update posterior by that of a different smaller target.24 exact same-target comparisons recover e(d0+6(k-1)); no new per-depth parameter is fitted. Extremely small surviving probabilities can amplify noisy inverse errors; early calibration bounds and exact deep predictions retain separate scope.

## 7. Executed evidence and provenance

All assertions passed.144 matched retention inverses,144 channel inverses,432 score-column checks;12 two-parameter fits and third-residual holdouts;28 DP/direct-word histogram comparisons with6988 word evaluations;1080 forward/first-reset comparisons and810 factorial bounds;144 multidepth full-word inverses;24 same-target final-update inverses; initial1..5, a wrong-anchor witness and the missing-state witness. A separate full check enumerated all55440 words of302400, using independent all-pairs scoring, and matched the DP's84 terminal score fibers with exact total mass1. Five symbolic identities and48 positive-convolution checks also passed. Counts may overlap and are not independent samples; no Monte Carlo.

The unchanged BRC kernel is8138 bytes, Git blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1, matched to current EM metadata.64 native positive serial/recoalescence operations were executed on proved terminal-equivalent fibers; the additional feedback coordinate is retained during transitions.

Prior work actually read: Turner et al., Introduction to PlackettLuce, author documentation section1; Del Moral/Doucet/Singh2010, A backward particle interpretation of Feynman-Kac formulae, journal abstract; NIST DLMF5.11.12 for the Gamma ratio. Generic ranking/filtering methods retain their attribution. The finite matched construction, feedback diagnostics and first-reset decomposition are the present author derivations; independent review, formalization and physical calibration remain separate.

The full Chinese proof, residual_updates.py, run_checks.py, symbolic_checks.py, exact results and inherited dependencies are preserved in prime_quantum_residual_updates_c57.zip. This Source note is the standalone result record, not a claim that all code is integrated.

Native registration succeeded this turn: session_start request prime-c57-residual-updates-20261104-a1 created RA-C90E164C9C5831A6B24570D9 and EM-DIRECT-74BABD, with verified canonical readback at8b11e61f460d6824a7bfe4b74397d14c27a65ed9. This is activity registration, not a formal Task claim or mathematical acceptance. Publication/checkpoint receipts are recorded separately.

Next: retain the same feedback under interleaved visible inputs, where xi can return toward zero; determine which return histories preserve long memory and which admit a uniform concentration bound.
