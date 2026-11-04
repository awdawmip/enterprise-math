# R5 — two interacting gates: covariance propagation and affine-kernel annihilation

Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Model: finite strictly positive P/Q nature kernels; at every nonterminal key STOP/declaration P, STOP/declaration Q, or CONTINUE; at the terminal key free P/Q declaration; FULL sees provenance, seedless LR sees only (time, likelihood ratio).
Frozen research inputs (unchanged): GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`; EM \`86149263e38c22292c9def1e0f69092efa1be77e\`. Current behavioral policies were read separately on 2026-11-05.
Predecessor: \`research_notes/brc_r5_gate_kernel_covariance_20261105_t0244/RESEARCH.md\`, commit \`0883215995e4813b0b6ef34601cda59eeea950f2\`.
Mother R5 target: one *lawful* model with equal complete O4 convex hulls but unequal actual real-strategy O4 sets. The present theorem supplies exact two-gate flow identities and an affine residual-annihilation mechanism; mother target remains open.

## 1. Lawful two-gate model and the canonical LR strategy

At t=1 two provenance histories h∈{A,B} have Q masses w_h>0, sum w_h=1 and common likelihood ratio 1. A FULL action consists of STOP/P, STOP/Q, CONTINUE with probabilities s_h^P,s_h^Q,c_h summing to 1. Upon CONTINUE, a positive Q kernel K_h(j)>0 leads to common t=2 LR keys r_j>0:
\[
\sum_j K_h(j)=1,\qquad \sum_j r_j K_h(j)=1.
\]
The corresponding P transition is r_j K_h(j). At (h,j), FULL chooses STOP/P, STOP/Q or CONTINUE with probabilities u_{hj},v_{hj},d_{hj} summing to 1. Conditional upon second CONTINUE, a strictly positive Q kernel M_{hj}(\ell) leads to terminal t=3 LR keys s_\ell>0:
\[
\sum_\ell M_{hj}(\ell)=1,\qquad
\sum_\ell s_\ell M_{hj}(\ell)=r_j.
\]
The corresponding P conditional kernel is s_\ell M_{hj}(\ell)/r_j. FULL declares P at (h,j,\ell) with probability f_{hj\ell}∈[0,1] and Q otherwise. Expected stop times under P,Q use t∈{1,2,3}; risks eP=P(declare Q), eQ=Q(declare P). All behavioral probabilities are real in [0,1].

Define \(\bar K_j=\sum_h w_hK_h(j)\), \(C=\sum_hw_hc_h\), \(A_j=\sum_hw_hc_hK_h(j)\), \(B_j=C\bar K_j\) and \(D_j=A_j-B_j\). When C>0, strict positivity implies A_j>0. Define the canonical seedless LR action at t=1 by Q-weighting the three source actions; at t=2 put
\[
\alpha_j=\frac{\sum_hw_hc_hK_h(j)u_{hj}}{A_j},\quad
\beta_j=\frac{\sum_hw_hc_hK_h(j)v_{hj}}{A_j},\quad
d_j=\frac{\sum_hw_hc_hK_h(j)d_{hj}}{A_j}.
\]
For C=0, LR also stops at t=1 and all later actions are irrelevant; take (α,β,d)=(1,0,0). The conditional Q kernel at t=3 given j under LR is the physical hidden-source mixture
\[
\rho_j(h)=w_hK_h(j)/\bar K_j,\quad
\bar M_j(\ell)=\sum_h\rho_j(h)M_{hj}(\ell).
\]
This is the same nature experiment under a seedless first action, not an adversarial choice of a new kernel.

The FULL and LR terminal Q masses are
\[
\mu^F_\ell=\sum_{h,j}w_hc_hK_h(j)d_{hj}M_{hj}(\ell),\quad
\mu^L_\ell=\sum_jB_jd_j\bar M_j(\ell).
\]
At each terminal LR key, assign seedless LR P-declaration probability \(p_\ell=N_\ell/\mu^F_\ell\) when \(\mu^F_\ell>0\), otherwise 0; here \(N_\ell=\sum_{h,j} w_hc_hK_h(j)d_{hj}M_{hj}(\ell) f_{hj\ell}\).

## 2. Two-gate covariance propagation theorem (all real behavior strategies)

For every such model and FULL strategy, let \(E_\ell=\mu^F_\ell-\mu^L_\ell\). Then
\[
D_j=\operatorname{Cov}_{w}(c_h,K_h(j)),\quad
\sum_jD_j=\sum_jr_jD_j=0,
\]
\[
\boxed{E_\ell=\sum_j\left[D_jd_j\bar M_j(\ell)+
\bar K_j\operatorname{Cov}_{\rho_j}(c_hd_{hj},M_{hj}(\ell))\right].}\tag{1}
\]
The second term is the genuine second-gate provenance interaction; it need not vanish when D vanishes. For two sources, D_j=w_Aw_B(c_A-c_B)(K_A(j)-K_B(j)).

The terminal residual's two moments and full **four-dimensional** canonical reconstruction discrepancy are exactly
\[
\sum_\ell E_\ell=\sum_jD_jd_j,\quad
\sum_\ell s_\ell E_\ell=\sum_jr_jD_jd_j,\tag{2}
\]
\[
\boxed{\begin{aligned}
e_Q(F)-e_Q(L^\circ)&=\sum_jD_j\alpha_j+\sum_\ell E_\ell p_\ell,\\
e_P(F)-e_P(L^\circ)&=\sum_jr_jD_j\beta_j+\sum_\ell s_\ell E_\ell(1-p_\ell),\\
T_Q(F)-T_Q(L^\circ)&=\sum_jD_jd_j,\\
T_P(F)-T_P(L^\circ)&=\sum_jr_jD_jd_j.
\end{aligned}}\tag{3}
\]
The formulas account for all STOP/P, STOP/Q and CONTINUE options at both gates and arbitrary history-dependent terminal declarations.

**Proof.** Q conservation gives A,B and their covariance difference; both K rows have Q mass 1 and P moment 1, giving the two null moments of D. At gate 2, the FULL continuing Q occupancy is \(U_j=\sum_hw_hc_hK_h(j)d_{hj}=A_jd_j\). The LR continuing occupancy is \(B_jd_j\). Write
\[
E_\ell=\sum_j(U_j-B_jd_j)\bar M_j(\ell)
+\sum_{h,j}w_hc_hK_h(j)d_{hj}(M_{hj}(\ell)-\bar M_j(\ell)).
\]
The first difference is D_jd_j; the second is the conditional covariance term in (1). Summing with weights 1 or s_\ell annihilates each conditional covariance because every M_hj row has total 1 and s-moment r_j; this proves (2). At t=1 the averaged LR stop masses equal FULL stop masses under both measures because the initial LR is 1. At t=2 the discrepancies in Q STOP/P and P STOP/Q are respectively D_jα_j and r_jD_jβ_j. At t=3 the LR P declaration is p_\ell by construction; the Q STOP/P discrepancy is E_\ell p_\ell and the P STOP/Q discrepancy is s_\ell E_\ell(1-p_\ell). Summing t-weighted continuation occupancies gives 1+C+ΣU_j versus 1+C+ΣB_jd_j under Q, and 1+C+Σr_j U_j versus 1+C+Σr_jB_jd_j under P. This proves (3). QED.

## 3. Affine-kernel annihilation theorem and converse

Suppose M_hj=M_j is independent of hidden source h, and every column obeys
\[
M_j(\ell)=a_\ell+b_\ell r_j\quad\text{for all j}.
\]
For any first-gate source-dependent action and any (possibly source-dependent) second-gate strategy whose **Q-occupancy-averaged** probabilities α_j, β_j, d_j are independent of j, write their common values α,β,d. In this full strategy class, *arbitrary final provenance-sensitive declarations* are allowed, and the canonical seedless LR strategy has **identical O4**.

Indeed, the covariance interaction in (1) vanishes since M_hj=M_j, and \(E_\ell=d\sum_jD_j(a_\ell+b_\ell r_j)=0\). The two t=2 action terms and time terms in (3) vanish by the two null moments. Therefore all four coordinates match.

The algebraic condition is exact: for any finite set of distinct or repeated r_j, a linear kernel M with columns M_(·,ℓ) annihilates **every** real signed D with \(\sum D_j=\sum r_jD_j=0\) iff each column lies in \(\operatorname{span}\{\mathbf1,r\}\). This is \((\ker A)^\perp=\operatorname{rowspace}(A)\) for \(A=(\mathbf1^\top;r^\top)\). Under an interior strictly positive K_0 with ΣK_0=ΣrK_0=1 and two positive source weights, every direction D in this nullspace is locally attainable in a lawful model: take w_A=w_B=1/2, c_A=1,c_B=0, K_A=K_0+εD and K_B=K_0−εD for sufficiently small ε>0; the actual gate residual is (ε/2)D. This yields a **physical local necessity**, not just a formal vector-space observation. The criterion concerns universal residual annihilation by this particular common continuation kernel; it does not assert universal FULL/LR image equality.

## 4. Strictly positive rational witness

At gate 2 choose r=(1/2,1,3/2), w=(1/2,1/2) and
\[
K_A=(1/4,1/2,1/4),\quad K_B=(5/16,6/16,5/16).
\]
At terminal gate 3 choose s=(1/8,1,15/8), and rows
\[
M=\frac1{56}\begin{pmatrix}37&14&5\\21&14&21\\5&14&37\end{pmatrix}.
\]
Every K and M entry is positive. Q row sums are 1; the P moment of K is 1, and the P moment of M's jth row is r_j. Each column of M is affine in r_j. Let source A continue at gate 1 while B STOP/P. At gate 2 use a source-independent 1/2 STOP/P + 1/2 CONTINUE action at every j; at terminal declare P exactly at s=1 and Q otherwise. Then
\[
D=(-1,2,-1)/64\ne0,\quad
\mu^F=\mu^L=(3/32,1/16,3/32),\quad
O_4(F)=O_4(L^\circ)=(3/16,13/16,7/4,7/4).
\]
The non-lumpable first kernel has a genuine nonzero provenance residual, but the affine second kernel annihilates its contribution to all four final observations for this strategy class. Conversely a j-dependent second continue fraction d=(1,0,1) produces \(\Delta T_P=\Delta T_Q=-1/32\): intermediate timing can expose residuals that a later terminal projection hides.

A lawful nonaffine counter-check is obtained by replacing only the middle row M_1 with M_1+(1,-2,1)/56. Positivity, Q mass and P moment continue to hold; for the signed null vector q=(1,-2,1), the first terminal column yields \(\sum_jq_jM'_j(0)=-1/28\ne0\).

## 5. Verification, scope, and next question

The attached standard-library Fraction script VERIFY.py independently enumerates all 3²·3⁶=6,561 deterministic first-/second-gate source action patterns, using a history-sensitive terminal declaration pattern, and checks (1)–(3) for the source-independent M case. It also checks the rational cancellation witness, nonuniform timing residual, strict P/Q positivity, and a lawful nonaffine perturbation. The finite result supports only those 6,561 enumerated patterns; the all-real statements are established by the algebra above. See EXACT_OUTPUT.txt.

Typed BRC carrier: positive rational P/Q source-labeled path masses, action occupation, likelihood-ratio keys, and the signed difference of positive flows (D,E). Compression is assessed only for the declared O4 observer and future actions. REUSE_APPLIED: predecessor exact gate–kernel covariance residual and Q-key occupancy Markovization. Signed D is a diagnostic difference, not a negative probability. This is an auxiliary mathematical statement in a probability experiment; no native X6 physical dynamics is inferred.

The R5 mother objective remains open. The next discriminating task is to combine (1)–(3) with a full four-dimensional *deterministic* FULL/LR hull comparison in a lawful multi-gate family, requiring an exact convex-combination certificate on every FULL vertex for a hull-equal candidate. If one passes, examine real-behavior LR semialgebraic nonmembership of a FULL point. Keep the two conditions separate and preserve exact immutable input pins and author-side review status.
