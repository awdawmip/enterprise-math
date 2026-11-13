# R637 — 秩二 signed BRC 校准的5进精度税：精确分类与复用原证明

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f, binomial signed K generator blob 7fa7a762f758b30c6090468ac43487daa34abad8.
Directly inherits R636@87cf91ddd0162c4f4e0e7c15037a4e4c7334f7e2 and preserves all its hypotheses. The full mathematical source proof of the inherited 5-adic branch-leading-order signature, optimal t-degree, and complete integer polynomial collision follows in Appendix A below.

## 1. New finite-precision observation protocol

Fix the same c=(0,5,1,2,3,4) and original six-axis model Y_x^+=A_x^+P_j+H_0+c_xH_1, Y_x^-=A_x^-M_j+H_0+c_xH_1. The unknown permutation j=pi^(-1)(x), integer polynomials H0,H1 and gains, known a>=1, exact signed K branches, and gain orders nu5(A+)=nu_t(A+)=a, nu5(A-)>=a-1 remain unchanged from R636. A matched reference at axis x is R_x=H0+c_x H1, without perturbing the experiment. New observer reads each coefficient of all twelve outputs and two chosen references only modulo 5^N, N>=1, and only through t^d. Distinguish p-adic digit depth N from t-jet depth d.

### Theorem (two independent sharp resource bounds)

For any two distinct calibration axes r,s, set Delta=c_s-c_r and e=v5(Delta). All 720 S6 orientations are uniquely recovered for every allowed nuisance choice if and only if

    N >= e+1 AND d >= a+8.

Of all 15 axis pairs, only axes (1,2) have |Delta|=5 and require modulus 25. The other fourteen have 5-adic unit Delta and require only modulus 5. Both the modulus and t-degree bounds are sharp in the stated model.

### Proof: sufficient digit resolution

References satisfy Rs-Rr=Delta*H1=5^e*u*H1, where u=Delta/5^e is a unit modulo5. For N>=e+1, every coefficient of H1 modulo5 is computable as inverse(u)*( (Rs-Rr mod 5^N)/5^e ) modulo5. Division means choose the divisible representative modulo 5^N; the quotient modulo5 is independent of the representative because N-e>=1. Likewise H0=Rr-c_rH1 mod5. Thus every background Hx modulo5 is known. Subtract it from positive Yx to get Ax+*Pj mod5. The initial nonzero t-orders are a,a+2,a+4,a+6,a+8,a+10, since all frozen Uj(0) and gain leading coefficients are 5-units. At d=a+8 identify five labels and infer the sixth from pi being a permutation. No other noise restrictions are used.

### Proof: sharp t-depth

If d<=a+7, set H0=H1=0 and gains A+=t^a, A-=t^(a-1). Swapping labels5 and6 leaves both positive and negative outputs zero up through d for both affected axes; all references remain zero. Hence no digit depth can improve the optimal t cutoff.

### Proof: sharp p-adic depth

Fourteen pairs have e=0 and N>=1 by definition. For the exceptional pair axes1,2, use the following **complete Z[t] witness**, valid for every a>=1: put v_j=a+2j-2, W=12 product_{j=1}^6(U_j*V_j), C_j=t^{v_j} W. Baseline pi=id and H0=H1=0, with gains A_j+=t^a W/Uj, A_j-=t^(a-1) W/Vj, yields both outputs C_j on axis j and references R1=R2=0.

Swap the direction labels on axes5 and6. Set T=(C_5-C_6)/3 (integer polynomial) and new backgrounds H0'=0,H1'=T,Hx'=c_x*T. For the exchanged label k(x), set

    F_x = 3*t^(v_x) - c_x*t^(v_5) + c_x*t^(v_6),
    Q_x = F_x/t^(v_(k(x))),
    A_x+'=t^a*(W/(3U_k))*Q_x,
    A_x-'=t^(a-1)*(W/(3V_k))*Q_x.

Because 3 divides 12 and c=(0,5,1,2,3,4), all Qx are integer polynomials with 5-unit constant coefficients; all new gains satisfy the same order conditions and are integer polynomials. On every axis the exact identities

    A_x+'*P_(k(x)) + c_x*T = C_x = A_x-'*M_(k(x)) + c_x*T

hold in Z[t]. Thus all twelve complete outputs match. Meanwhile R1'=0 matches baseline exactly, and R2'=5T matches baseline modulo5. W(0) is a 5-unit, so T mod5 is nonzero and 5T mod25 is nonzero. At N=1 these two different directions share all observed outputs for every t-degree. This proves N>=2 for axes1,2 and closes the iff theorem.

## 2. General integer-matrix calibration lemma

Let C be a full-rank q-by-q integer calibration matrix, p any prime, UCV=diag(d1,...,dq) its Smith normal form with unimodular integer U,V, and e*=max_i vp(di). For every integer nuisance vector h, observations C*h modulo p^N uniquely determine h modulo p **if and only if** N>e*. Indeed U,V preserve invertibility modulo p^N. Each coordinate di*z_i modulo p^N determines z_i modulo p exactly when N>vp(di). If N<=e*, two Smith coordinate vectors differing by the ith standard basis vector for the maximally divisible di yield equal measurements but different h modp. In the rank-two model C=[[1,c_r],[1,c_s]], invariants are 1 and |Delta|, so e*=v5(Delta).

This lemma establishes nuisance-coordinate calibration precision. A direction-information lower bound additionally needs compatible signed BRC gains and outputs; the concrete exceptional-pair witness above supplies exactly that.

## 3. Validation, BRC reuse and native boundary

R637_VERIFY.py was run locally with exact Python integer polynomial arithmetic and modular coefficients: 15 calibration pairs times three gain orders a in {1,2,4} times all 720 S6 permutations = 32,400 direction recoveries. It also checks all six axes in the complete polynomial collision and the mod5 versus mod25 calibration contrast. R637_EVIDENCE.json supplies counts and per-pair thresholds. Analytic algebra proves all a>=1 and arbitrary nuisance polynomials within the model; finite checks validate the frozen instance and executable reconstruction.

BRC REUSE_APPLIED: frozen R462 signed binomial K law and the R636 exact complete collision; retain signed branch identities and provenance. This is a static auxiliary observer, not a proven native X6 triadic field update. Future work: locate an actual Source-registered X6 coupled field and legitimate background-only references, derive its integer observation matrix and compute Smith precision factors, then verify branch/path/field information is preserved through one real update.

## Appendix A — complete exact predecessor proof (R636, unchanged frozen scientific context)

# R636 — Two-calibration theorem for rank-two signed BRC backgrounds

Date: 2026-11-08. Author-side exact mathematical derivation; no independent Driver acceptance.

Frozen input: R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f, signed binomial K generator blob 7fa7a762f758b30c6090468ac43487daa34abad8, theta=0. Parent R635 commit 86d36d60dcf43bd633592b7ca093c09bba3c137a.

## Precise model

For each of six X6 axis direction labels j=1,...,6, P_j=K_(2j-1)=t^(2j-2)U_j and M_j=K_(2j)=t^(2j-1)V_j, with U(0)=(2,-8,6,106,83,9) and V(0)=(-1,-11,53,119,36,1). All these coefficients are nonzero modulo 5.

Unknown pi in S6 assigns branch label j=pi^(-1)(x) to spatial axis x. Fix KNOWN integer vector c=(0,5,1,2,3,4), indexed by x. For arbitrary H0,H1,A_x^+,A_x^- in Z[t], form Y_x^+=A_x^+ P_j+H0+c_xH1 and Y_x^-=A_x^- M_j+H0+c_xH1. Known integer a>=1; nu_5(A_x^+)=nu_t(A_x^+)=a; nu_5(A_x^-)>=a-1. Here nu_5 counts the lowest t-power with nonzero coefficient modulo 5. A matched reference on axis r independently reads R_r=H0+c_rH1, WITHOUT changing the gains or the background. Jets are read through t^d. Backgrounds and gains may vary between different candidate explanations of the same transcript.

## Theorem

For this fixed rank-two background model, any TWO distinct background references suffice to distinguish all 720 permutations at the optimal uniform jet depth d_min=a+8. Conversely, for EVERY designated single reference location r, two different S6 permutations with valid integer gains and rank-two backgrounds produce IDENTICAL twelve entire integer readout polynomials and the same R_r. Therefore two is the smallest number of matched references guaranteeing identification in this declared model.

## Two-reference reconstruction and optimal depth

Take r!=s. Because c_s!=c_r, H1=(R_s-R_r)/(c_s-c_r) and H0=R_r-c_rH1, computed coefficientwise to degree d in Q[t]. The source model ensures these recovered polynomials have integral coefficients. Removing the background from the six positive readouts leaves A_x^+P_j, whose lowest nonzero mod-5 coefficients occur at distinct orders a,a+2,a+4,a+6,a+8,a+10. At depth d=a+8, five labels are uniquely visible; the sixth is fixed by the permutation condition.

For d<=a+7, labels 5 and 6 have both positive and negative probe order >=a+8 under the gain hypothesis. The choices H0=H1=0, A^+=t^a and A^-=t^(a-1) give identical truncated transcripts upon swapping labels 5 and 6, even when both backgrounds are supplied. Thus d_min is sharp.

## Exact full-polynomial single-reference collision

Let v_j=a+2j-2, W=12 product_(j=1)^6 U_j V_j, and C_j=t^(v_j)W in Z[t]. W(0) is a nonzero mod-5 unit.

Baseline: pi=id, H0=H1=0, A_j^+=t^a(W/U_j), A_j^-=t^(a-1)(W/V_j). Then Y_j^+=Y_j^-=C_j for all six axes.

Fix ANY calibration axis r. Let p<q be the two LARGEST indices among the other five labels. The six tuples (r,p,q,h,c_q-c_r), with h=c_p-c_r, are:
(1,5,6,3,4); (2,5,6,-2,-1); (3,5,6,2,3); (4,5,6,1,2); (5,4,6,-1,1); (6,4,5,-2,-1).
In every case h divides 12, h!=0 mod 5, and c_q-c_r!=0 mod 5.

Define T=(C_p-C_q)/h in Z[t], H1'=T, H0'=-c_r T. The NEW background on axis x is H_x'=(c_x-c_r)T; at the chosen calibration r it is zero, so R_r'=R_r. Exchange direction labels p and q while leaving other labels unchanged, and let k(x) be the new label.

The branch response required on axis x becomes
 B_x=C_x-H_x'=(W/h)[h t^(v_x)-(c_x-c_r)t^(v_p)+(c_x-c_r)t^(v_q)].
For x=p, B_p=C_q has order v_q. For x=q, the leading degree v_p coefficient is -(c_q-c_r)W(0)/h, a 5-unit. Every other uncalibrated x has label x<p and leading order v_x; calibration axis r is unchanged. Thus B_x has exactly order v_(k(x)) mod 5.

Put F_x=h t^(v_x)-(c_x-c_r)t^(v_p)+(c_x-c_r)t^(v_q) and Q_x=F_x/t^(v_(k(x))). Q_x is in Z[t] with Q_x(0) a 5-unit. Since W/h=(12/h) product U_j V_j belongs to Z[t] and includes every U_k,V_k factor, the new gains
 A_x^{+'}=t^a[W/(h U_k)]Q_x and A_x^{-'}=t^(a-1)[W/(h V_k)]Q_x
are in Z[t] and satisfy the same leading-order hypotheses. They obey, simultaneously for all x,
 A_x^{+'}P_(k(x))+H_x' = C_x = A_x^{-'}M_(k(x))+H_x'
as exact integer-polynomial identities. The R_r' calibration is zero, identical to the baseline. Hence the two distinct directions produce exactly the same complete twelve polynomial readouts and the same sole reference. This works for arbitrary a>=1 and every r, completing the necessity proof.

## Scientific scope, computation and continuation

This is an auxiliary STATIC signed BRC observable theorem using frozen K branches and an explicitly hypothetical rank-two axis coupling. It neither asserts realization by a registered native X6 operator nor permits quotienting provenance, full joint state, branch history, grade, or heartbeat evolution. P000 six-axis space and separate time are preserved. Reuse resolution: REUSE_APPLIED — R462 signed binomial K formula and R635 branch factorization.

A deterministic exact-integer local extended suite regenerated all twelve K polynomials, checked 18 full-polynomial collisions, and all 15 calibration pairs x 720 permutations x 3 gain orders a in {1,2,4} = 32,400 recovery configurations, plus ancillary assertions; 33,105 grouped checks passed with marker R636_RANK_TWO_BACKGROUND_TWO_CALIBRATIONS_EXACT_PASS. The accompanying compact executable reproducer checks 32,616 exact items (marker R636_COMPACT_REPRODUCE_PASS). The analytic proof establishes the arbitrary-a result, not the finite test count.

Next open unit: inspect actually registered native X6 triadic-field operators for a legal cross-axis rank-two nuisance H0+c_xH1, a non-perturbative matched reference, and preservation of gain/source/path semantics. For other coefficient vectors seek precise integer divisibility and residue conditions for a single-reference collision before generalization.

