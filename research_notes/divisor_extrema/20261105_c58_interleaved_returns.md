# C58: interleaved residual returns, forgetting and persistent fluctuations

Progress-Event-ID: prime-c58-interleaved-returns-20261105-a1
Date: 2026-11-05 Asia/Taipei
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING
Researcher-ID: EM-DIRECT-023188 / TASK_RESEARCH
Research-Activity-ID: RA-70CFA848B4459CEEFD3D19EE
Global-read: 833f33eb259ea0ce2da38b04b9fca35a680fbc06
EM-read: 740f3a5c005c993c660803a39913769034390412
Pre-publication-main: 45177f012f6ad98acb7dcb1f4059e5c462308e9d

## 1. Inherited model and scope

Continue C57 at EM commit 5fd53df906cd2fb4033cc00849214567eb54db02, research_notes/divisor_extrema/20261104_c57_residual_dependent_updates.md, blob 7decda7883a50004b3322ef4b4c8442f759ecca7, and its actually mounted reproduction archive. The parent question is how complete prime/composite path relations constrain local history and stability. This turn studies interleaved visible inputs under exactly the same feedback.

Keep every complete factor word, positive mass, signed scores, rho_1 and provenance. Words and memory remain internal joint records over the retained Heartbeat X6 Cell; no new spatial axis or physical clock is inferred. States are 0,1,2; a 2 increments the state capped at2; the first two3s reset for preparation; later3s retain the old state with e(xi)=1/(4+xi^2), otherwise reset0. Hidden5/7 preserve state. xi=2X23-n2*n3 is evaluated before the new input. Reference rates are (1,1,z_state,1), z=(1/4,1,4), times remaining counts and normalized.

The common observed block uses only2/3 and leaves exactly two5s and one7. Starting histories have matched counts and score, at least two3s have already occurred, and all feedback values are strictly between0 and1. The calibrated complete-tail matrix for557/575/755 is
T=[[1/15,4/15,2/3],[1/3,1/3,1/3],[32/45,8/45,1/9]], detT=-1/15.
Common positive terminal W(A,B) is allowed. At total counts(a,b,c,d), A=2(X23-X25+X27+X35-X37)-(ab-ac+ad+bc-bd), B=2X57-cd. Equal terminal scores get the same weight.

## 2. Exact conditional transfer and a uniform all-word bound

With m visible occurrences left, the likelihood of observing the specified visible symbol in state s is b_p/(m+c_s), c=(3/2,3,9). Its numerator is state-independent. Put D_m=diag(1/(m+c_s)),
K2=[[0,1,0],[0,0,1],[0,0,1]],
K3(e)=[[1,0,0],[1-e,e,0],[1-e,0,e]].
For a block u of length L, its stripped unnormalized transfer is M_u=D_L K_u1 ... D_1 K_uL. A row pi updates to pi M_u/(pi M_u 1). Observing2 changes xi to xi-n3; observing3 changes it to xi+n2. The omitted factors b_p are common positive scalars, not discarded state likelihoods.

For TV=half-l1, positive reweighting by g is Lipschitz with constant maxg/ming. Proof: differentiate a reweighted event probability along the line between the two input measures; the test-function oscillation is at most maxg and the denominator at least ming. K2 has Dobrushin coefficient1, K3(e) coefficient e. Therefore
TV(pi_u,rho_u)<=min{1,P_L product_(3 steps)e(xi_j) TV(pi,rho)},
P_L=product_(m=1)^L (m+9)/(m+3/2).
The input TV is inside the cap; short observed words can amplify small input differences.

If u contains22, after the second2 the conditional state is exactly2 for all inputs, so subsequent differences are zero. If no22, then N3>=floor(L/2). Since e<=1/4, uniformly over all such common words and all input states,
TV(pi_u,rho_u)<=B_L=min{1,P_L 4^(-floor(L/2))}.
P_L=Gamma(L+10)Gamma(5/2)/[Gamma(10)Gamma(L+5/2)] is asymptotic to a positive constant times L^(15/2). Thus B_L=O(L^(15/2)2^(-L)). Exact product bounds at L20/40/60/100 are approximately .1296355730,9.375990334e-6,1.363187132e-10,4.388394553e-21. This is initial-history sensitivity conditional on a common word, not the variance of the current state. The hidden tail is fixed in this theorem.

## 3. Exact finite rank classification

The transfer has rank3 when u contains no2, rank2 when it contains2 but no22, and rank1 when it contains22. Multiplication by invertible T or positive row/column scales preserves these ranks.

Proof: D_m and K3 are invertible. The first2 reduces to support{1,2}. A22 gives a single state. For each subsequent segment3^r2, r>=1, let B_i be its mass ending in1 through a first reset and S_i its never-reset mass ending in2, for input i=1,2. Then
B_i/S_i=sum_(j=1)^r [(1-e_j)/product_(l=j)^r e_l] product_(l=j+1)^(r+1) d0(m_l)/di(m_l).
The final factor corresponds to the final2, so each positive term contains at least one ratio strictly increasing with c_i. Hence B_2/S_2>B_1/S_1 and the induced2x2 determinant is nonzero. Compose such segments and any terminal3-block. This proves the infinite-family classification; finite enumeration checks the implementation.

## 4. A return-to-zero path with nonvanishing current randomness

Two actual histories h0=322233 and h1=223332 both reach216, have X23=6 and xi=3, and prepare pure states0 and1 under the inherited first-two3 preparation. Use the common block u_k=(23)^k and target N_k=2^(k+3)3^(k+3)5^2*7.

Before each pair, n2=n3=n and xi=n. The2 brings xi to0, so every feedback3 uses exactly e=1/4; that3 produces xi=n+1. Each post3 state law has the form pi(p)=(3/4,(1-p)/4,p/4). Thus its nonreference probability is always1/4, and the indicator of being nonreference has variance3/16 at every k.

After the first pair, inputs0 and1/2 give p=0 and1. If m visible inputs remain before a subsequent pair,
F_m(p)=(2m+3)(m+2)(m+9-6p)/[(2m+3)(m+2)(m+9-6p)+6(m+3)(m+8)(m+9)].
The endpoint parameters are p0(k)=F2 o F4 o ... o F_(2k-2)(0) and p1(k) with endpoint1. Every F_m is strictly decreasing, so finite endpoint differences are nonzero and their sign alternates with k; the response rank is2.

Writing F=(B+Cp)/(A+B+Cp), A=(3/4)d0 d1', B=(1/4)d1 d2', C=(1/4)(d2-d1)d2'<0, gives F'=AC/(A+B+Cp)^2. Consequently |F'|<=|C|/A<=2/(m+3), and
TV(pi(p0(k)),pi(p1(k)))<=Gamma(5/2)/[4Gamma(k+3/2)].
This factorial-type contraction holds while every feedback probability stays1/4.

The intervals I_k=F2 o ... o F_(2k-2)([0,1]) are nested and their widths vanish. Their unique intersection p_* is certified by the k25 rational endpoints:
.080674208836343445960424569389 <= p_* <= .080674208836343445960424569390.
The limiting state law is approximately(.75,.22983144779091414,.02016855220908586), independent of the initial state. Current excitation is not survival of the original history: a2 can excite a state again after a reset.

Exact finite history TV for k1,2,3,5,10,15 is respectively .25,.011167044809982983,.000536039961391509,1.1917870463934567e-6,1.1120996708139078e-13,2.681968728151544e-21. All are decimal displays of exact fractions; recurrence/matrix agreement was checked for k1..50.

## 5. Actual terminal readings and same-residual order tests

For general state distributions, subsequent calibrated tail plus any common positive W has TV at most(32/3) times the state TV, capped at1. Factor the operation into state reweighting by c_i=sum_jTijWj and a stochastic readout; max c_i/min c_i<=max_(i,l,j)Tij/Tlj=32/3.

For the alternating family, the tail law is R(p)=((24+17p),(51-7p),(105-10p))/180. The largest minus smallest log derivative is at most115/136. Hence the common-W Hilbert log ratio is at most(115/136)|p-q| and the selected tail TV is at most(115/544)|p-q|, using the sharp Hilbert/TV inequality already proved in C56. This gives an explicit observable consequence without bounding the strength of W.

Starting from h0/h1, compare common blocks2332 and3223 in the same target1360800. Both end with visible counts(5,5), xi=3, and identical terminal scores by tail column. For2332, the output laws are(0,5864/5899,35/5899) and(0,5812/5819,7/5819); their TV is162372/34326281 and the first-two-tail cross ratio is48568643/48203306. For3223, the22 makes every input identical and the final3 has e(-2)=1/8, giving(7/8,0,1/8) and cross ratio1. Equal endpoint and residual do not determine the ordered update response.

A distinct externally imposed-input control illustrates why likelihood matters: deleting D_m gives (K2K3(1/4))^2 rank1, whereas conditioning the actual complete-path preparation on2323 gives rank2. These are different preparations, not contradictory computations.

## 6. Actual execution, attribution and scope

All new assertions passed:765 rank cases,2295 uniform TV bounds,567 independent latent-path enumerations;126 complete-word conditional checks,189 matched-score checks,756 unknown-weight cross ratios;50 alternating sizes with exact return, nonreference mass, rank and nested intervals;252 nonpure input bounds and an explicit short-observation amplification witness;150 alternating terminal-weight bounds. All5040 complete words with counts(3,3,2,1) were independently scored and summed, matching the inherited DP with total mass1. Six symbolic identities and positive-polynomial checks passed. Counts overlap, and are not statistical sample sizes. No Monte Carlo was used.

The original8138-byte BRC kernel, blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1, was matched to current EM metadata and reused unchanged.96 positive serial/recoalescence operations were performed on proved terminal-equivalent fibers. Complete words remain reproducible and signed labels do not cancel positive mass. The1..5 initial cases remain unique words of probability1.

A draft cap initially put input TV outside min(1,...); author review corrected its placement and added the252 nonpure regressions plus an amplification witness before publication. Universal proofs are independent of the finite table. The full Chinese RESEARCH_NOTE.md, interleaved_returns.py, run_checks.py, symbolic_checks.py, exact JSON, logs and minimal inherited code are in prime_quantum_interleaved_returns_c58.zip. This repository note is a self-contained research checkpoint, not a claim that all code was integrated.

Actual literature reads: Giraud/Del Moral arXiv1209.5654 author HTML introduction (Feynman-Kac stability via transition contraction and potential oscillation); Cohen/Fausti arXiv2309.02413v2 abstract, with the previously scoped C56 inequality; NIST DLMF5.11 for the Gamma ratio. General filtering, Dobrushin and Hilbert methods retain existing attribution. Specific arithmetic word classification, return family and rational interval are author derivations. Independent review, formalization and physical correspondence remain separate.

Native session_start succeeded at18dac72046a1acec239fc1f0dda2464b0384b97c, issuing EM-DIRECT-023188 and RA-70CFA848B4459CEEFD3D19EE. This registers activity, not a Task claim or mathematical acceptance. The current checkpoint binding is recorded separately.

Next: let the hidden observation multiplicity grow with visible length, preserving the same update and matched terminal readout, to determine when likelihood amplification competes with the proved forgetting. The fixed-tail interleaved-return unit is complete at the author-proof and exact-check level.
