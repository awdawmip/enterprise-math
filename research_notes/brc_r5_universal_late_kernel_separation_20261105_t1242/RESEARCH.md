# R5: universal late-kernel separation with source-dependent first-stage kernels

2026-11-05. Status: AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral rules were independently read at GLOBAL main 039e337d990d4e7d4eef9eb0008af1144054189b and EM main 1293f2d54b300d91928488bdc52c889b7b4e4d66.

## 1. Exact statistical BRC model

A hidden source h=A,B has strictly positive weight w_h under both P and Q, with w_A+w_B=1 and starting likelihood ratio 1. FULL observes h at t=1; seedless LR observes only time and current likelihood ratio. At t=1 either stop and declare P or Q, or continue. Continuing produces at t=2 one of finitely many common positive ratios r_j with source-conditional Q probabilities K_h(j)>0, sum K_h=1 and sum r_j*K_h(j)=1. Assume the common R alphabet includes more than one ratio; the mean-one condition then implies positive probability for ratios on both sides of 1. At t=2 either stop or continue; continuing produces a terminal ratio s_l>0 with Q kernel M_hj(l)>0 on one common finite terminal alphabet S, sum M_hj=1 and sum s_l*M_hj(l)=r_j. At t=3 freely declare P or Q. The P path weights are Q path weights multiplied by their likelihood ratios. Behaviors may randomize by real probabilities at their own information keys.

The complete four-observer output is O4=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P), and T_P,T_Q the corresponding mean stopping times. The retained BRC carrier is source/branch provenance and exact Q/P path masses; the proposed projection erases h, while future operations include stopping decisions. This is a finite typed statistical observer, not a modification of P000 or its native six-axis ontology.

For a direction n=(a,b,g,d), let L(r)=max(a*r,b), c(r)=-(g*r+d), A_h=sum_j K_h(j)*L(r_j)-L(1), B_hj=sum_l M_hj(l)*L(s_l)-L(r_j), D_hj=B_hj-c(r_j), X_h=A_h-c(1)+sum_j K_h(j)*[D_hj]_+, mu=sum_h w_h*X_h and

eta=sum_j (sum_h w_h*K_h(j)*[D_hj]_+ - [sum_h w_h*K_h(j)*D_hj]_+).

The preceding all-normal Bellman-Jensen formula, obtained by backward induction, is

h_FULL(n)=L(1)-c(1)+sum_h w_h*[X_h]_+,
h_LR(n)=L(1)-c(1)+[mu-eta]_+.

All quantities refer to supports of complete four-dimensional convex hulls. The formulas cover unrestricted real behavioral policies, not merely a fixed list of normals.

## 2. New theorem and complete proof

**Theorem (late-kernel separation independent of first-kernel identity).** Under the preceding finite strictly-positive common-support and nondegenerate first-stage assumptions, if M_A,j0 != M_B,j0 at ANY shared time-2 ratio r0, then h_FULL(n)>h_LR(n) for some four-dimensional normal n. No equality K_A=K_B is assumed; all other M_hj may differ arbitrarily. If all model inputs are rational, the separating normal may be rational.

**Constructive exact gap.** Let a positive rational k (or a real positive k for real data) distinguish the two conditional late distributions via the call payoff L_k(s)=max(s,k). Define B_h,j0(k)=E_M[h,j0] L_k(S)-L_k(r0), q=|B_A,j0(k)-B_B,j0(k)|>0, t=(B_A,j0+B_B,j0)/2 and c_alpha(r)=t+alpha*(r-r0). The corresponding normal is n_alpha=(1,k,-alpha,alpha*r0-t). For sufficiently large finite alpha with the sign described below,

h_FULL(n_alpha)-h_LR(n_alpha) = q/2 * min(w_A*K_A(j0),w_B*K_B(j0)) > 0.

**Proof, step 1 (terminal separation).** A finite probability law on positive S is determined by E max(S,k) for all k>0: away from atoms the derivative in k is the CDF P(S<k). Hence distinct M_A,j0 and M_B,j0 admit k>0 with different call expectations. Both laws have the same mean r0, so the B difference is nonzero. For rational S and rational kernels a rational k at or between finitely many breakpoints works.

**Proof, step 2 (isolate the time-2 gate).** At r0, cost c_alpha(r0)=t, so the two D_h,j0 have opposite signs, magnitudes q/2. For every other r_j!=r0, the finite B_hj terms are dominated by -alpha*(r_j-r0) as |alpha| tends to infinity. Thus both sources eventually have one identical strict D sign at each OTHER node, and every other time-2 Jensen term vanishes. The remaining Jensen residual is exactly eta=(q/2)*min(w_A*K_A(j0),w_B*K_B(j0))>0. This computation is valid with K_A!=K_B.

**Proof, step 3 (force first-gate continuation without changing the target residual).** For r0>1 choose alpha->+infinity; for r0<1 choose alpha->-infinity. Then c_alpha(1)=t+alpha*(1-r0)->-infinity, and X_h>=A_h-c_alpha(1)->+infinity for both sources. If r0=1, c_alpha(1)=t is constant, but each nondegenerate mean-one K_h gives positive mass to at least one r_j<1. Choosing alpha->+infinity sends D_hj to +infinity at that lower node, hence X_h->+infinity. Therefore in every case a finite alpha makes X_A,X_B>0 and mu>eta, while eta stays equal to its single-target positive value. The first-gate Jensen term is zero and the remaining gap is [mu]_+-[mu-eta]_+=eta. A rational sufficiently large integer alpha exists for rational input. QED.

**Corollary (kernel-identity prerequisite for equal hulls).** Complete FULL/LR O4 convex-hull equality in this two-source nondegenerate positive model requires M_A,j=M_B,j at EVERY shared time-2 node. Source dependence of the first K kernels remains a distinct open subproblem. This corollary does not generalize the exclusion to degenerate R, source-specific supports or deeper/reconvergent models.

## 3. Fully rational witnesses

Common w=(1/2,1/2), R=(1/2,1,3/2), K_A=(1/4,1/2,1/4), K_B=(3/8,1/4,3/8), S=(1/4,1,7/4). Let

LOW=(3/4,1/6,1/12); HIGH=(1/12,1/6,3/4); MID_A=(1/4,1/2,1/4); MID_B=(1/3,1/3,1/3);
ALT_LOW=(35/48,5/24,1/16); ALT_HIGH=(1/16,5/24,35/48).

All Q/P probabilities are strictly positive and normalized. In each case non-target M kernels are identical across sources.

| Target ratio r0 | M_A/M_B at target | exact normal n | FULL support | LR support | gap | FULL attaining O4 | infinity-distance lower bound |
|---|---|---|---|---|---|---|---|
| 1 | MID_A/MID_B | (1,1,-2,57/32) | 505/512 | 503/512 | 1/256 | (451/768,119/192,73/32,39/16) | 1/1480 |
| 3/2 | HIGH/ALT_HIGH | (1,1,-4,761/128) | 14541/2048 | 14539/2048 | 1/1024 | (503/768,115/192,87/32,45/16) | 1/12232 |
| 1/2 | LOW/ALT_LOW | (1,1,4,-263/128) | 14541/2048 | 14539/2048 | 1/1024 | (455/768,127/192,93/32,45/16) | 1/8248 |

The distance lower bound is gap / ||n||_1 from the explicit supporting hyperplane. For the central node, B_A=3/16, B_B=1/4; X_A=15/128, X_B=75/256, and eta=1/256. All values are exact fractions.

## 4. Actual verification and boundaries

The companion Python standard-library Fraction script VERIFY.py checks every transition's Q and P normalizations, computes Bellman advantages and the FULL support, integrates an explicitly selected attaining FULL policy under the original path measures, and independently enumerates 3*3^3*2^3=648 deterministic seedless-LR policies per case. All 1,944 rational policy valuations match the LR support bounds. The actual stdout is in EXACT_OUTPUT.txt; its final marker is PASS_EXACT_R5_UNIVERSAL_LATE_KERNEL_SEPARATION. The general finite-model theorem is the analytic proof in section 2, not a consequence of finite enumeration.

Scientific predecessor: Enterprise Math research_notes/brc_r5_two_gate_sign_compatibility_20261105_t1145/RESEARCH.md at immutable commit a0811cc29ebdb06428383cc6d32a74b872f9e5f3. Reuse of its all-normal Bellman-Jensen formula is REUSE_APPLIED; no native X6 software run was claimed. External contextual literature: David Blackwell, Equivalent Comparisons of Experiments (1953), DOI 10.1214/aoms/1177729032; Romain Laroche and Rémi Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html . These sources are not cited as proving this new model-specific time-tilt theorem.

## 5. Next mathematical question

Constrain all late kernels M_A,j=M_B,j, while keeping distinct positive mean-one K_A != K_B. Since eta then vanishes for every n, analyze the all-normal first-gate Jensen gap sum_h w_h[X_h]_+ - [sum_h w_h X_h]_+. Search for an exact complete hull-equality certificate or a general K-difference separation lemma. Test policy-image nonmembership only after a genuine hull-equality certificate. Separately preserve degenerate/reconvergent architectures as possible research routes. Current R5 mother objective is open. No task CLAIM, independent Driver review, Working Truth or formal Result admission is asserted.
