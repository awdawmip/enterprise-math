# R231 — Multi-pair source spectral collision hypercubes and a sharp 244-mode six-source witness

Date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Scope: abstract paired-source scalar ideal-cardinality observer; native typed BRC integration NOT_EXECUTED.

## Provenance and scientific scope

Continue R229 and R230 at immutable commits:
- R229: \`awdawmip/enterprise-math@acfb0cd5c685aaae2802ed51054bcff2019d8d4e:research_notes/portable_direct/R229_STICKY_RESET_OBSERVABLE_SPECTRUM_AND_COLLISIONS_20261117.md\`
- R230: \`awdawmip/enterprise-math@3cdf59d8bfddb69c8e6eac219c6773d27b5c80ea:research_notes/portable_direct/R230_NESTED_SOURCE_SPECTRAL_COLLISION_20261117.md\`
- Immutable frozen scientific input \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
- P000, ACTIVE Heartbeat X6 worldview, joint-relation retention and existing native BRC signed/port/provenance/cross-moment carrier remain unchanged.

This is an exact calculation for a **derived scalar stochastic source-support observer** \(\mathbb E F_n\) of \(J_{m,k,L}\) for \(n\ge L\). It neither replaces the native six-axis, twelve-signed-direction state nor asserts a physical stochastic law.

Sources are \(0,1,\dots,k\), with 0 neutral. The strictly positive sticky-reset Markov chain is
\[
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\qquad
0<\alpha_i<1,\quad\pi_i>0,\quad\sum_i\pi_i=1.
\]
Take stationary initialization \(\rho_i=c\pi_i/(1-\alpha_i)\), \(c^{-1}=\sum_i\pi_i/(1-\alpha_i)\).
For a proper nonneutral source subset \(U\subsetneq[k]\), write \(D_U=\{0\}\cup U\), \(b_i=(1-\alpha_i)\pi_i\). When the holding parameters are pairwise distinct, write
\[
C_D(x)=\prod_{i\in D}(x-\alpha_i)-
\sum_{i\in D}b_i\prod_{j\in D\setminus\{i\}}(x-\alpha_j).
\]
For repeated holding values, \(C_D\) denotes R229's grouped reduced observable polynomial (not the unreduced determinant). With distinct \(\alpha_i\), every killed-block \(C_D\) has simple positive roots below 1. The full source block contributes only the observed stationary eigenvalue 1. The exact scalar recurrence polynomial is the squarefree lcm of \(x-1\) and all proper-block \(C_D\) (R229). All its proper-block roots occur with positive spectral weight (proof below).

## Theorem 1 — quantitative limit on nested block spectral coincidences

Let \(D\subsetneq E\) be proper source blocks, and let \(t\) be the number of **distinct** holding values \(\alpha_i\) for newly added indices \(i\in E\setminus D\). Then
\[
\deg\gcd(C_D,C_E)\le \min(\deg C_D,t-1).
\]
When the added holding values are distinct, any shared eigenvalue must be one of the \(t-1\) simple real zeros, one in each interval between consecutive added holding values, of
\[
S_{E\setminus D}(x)=
\sum_{i\in E\setminus D}\frac{(1-\alpha_i)\pi_i}{x-\alpha_i}.
\]

**Proof.** A common reduced secular root avoids the holding poles, and the R230 exact criterion says \(S_D(\lambda)=1\) and \(S_{E\setminus D}(\lambda)=0\). Collect any repeated added holding values into a single positive residue \(B_a=\sum_{\alpha_i=a}b_i>0\). Off its poles, \(S_{E\setminus D}'(x)=-\sum_a B_a/(x-a)^2<0\). There is exactly one simple zero between each consecutive pair of distinct added poles: the function falls from \(+\infty\) to \(-\infty\). Before the smallest pole every summand is negative, and after the largest every summand is positive, so there are no other real zeros. All secular roots are real; hence there are at most \(t-1\) common roots, as well as the trivial bound \(\deg C_D\). QED.

## Theorem 2 — a hypercube of simultaneous proper-block collisions

For any integer \(t\ge1\) and \(k\ge2t\), choose \(0<\alpha_0<\lambda<1\), set
\[
\pi_0=\frac{\lambda-\alpha_0}{1-\alpha_0}\in(0,1),
\]
and choose \(t\) disjoint nonneutral source pairs \((a_j,b_j)\) with
\(\alpha_{a_j}<\lambda<\alpha_{b_j}\). Divide a positive part of the remaining probability among each pair, choosing within-pair probabilities so that
\[
\frac{\pi_{b_j}}{\pi_{a_j}}=
\frac{(1-\alpha_{a_j})(\alpha_{b_j}-\lambda)}
{(1-\alpha_{b_j})(\lambda-\alpha_{a_j})}.
\]
Allocate any leftover positive probability to additional unpaired sources (if any). Then \(S_{\{0\}}(\lambda)=1\), and each pair contributes zero to its secular sum. Therefore every \(D_U\) with \(U\) a union of complete chosen pairs has \(\lambda\) as a secular root, whenever \(U\subsetneq[k]\).

There are \(N=2^t-1\) such proper blocks when \(k=2t\) and \(N=2^t\) when \(k>2t\) and unpaired sources are omitted. Consequently, relative to the no-collision degree bound
\[
d_{\rm gen}=(k+2)2^{k-1}-k,
\]
the scalar minimal order is at most \(d_{\rm gen}-(N-1)\). This is a constructive multi-block collision family, with the exact rank depending on any additional coincidences.

**Proof.** The chosen \(\pi_0\) gives \(b_0/(\lambda-\alpha_0)=1\). The ratio makes the two signed rational contributions of each pair sum to zero. Every union of complete pairs therefore preserves the secular equation. Proper-block modes have positive observable weight by the lemma below, so counting a common mode across \(N\) blocks removes at least \(N-1\) repetitions from the direct-sum degree count. QED.

## Theorem 3 — exact six-source 244-mode witness

Set \(k=6\), \(m=12\) signed-direction labels, \(L=2\), and choose the strictly positive rational parameters
\[
\alpha=(1/5,\ 1/4,\ 3/4,\ 3/10,\ 7/10,\ 7/20,\ 13/20),
\]
\[
\pi=(36,\ 5,\ 15,\ 6,\ 14,\ 7,\ 13)/96.
\]
All 7 holding values are distinct. The neutral-source contribution at \(\lambda=1/2\) equals 1, and the three pairs \((1,2),(3,4),(5,6)\) each cancel exactly. Seven **proper** masks carry the same mode:
\[
\boxed{U_{\text{mask}}\in\{0,3,12,15,48,51,60\}}.
\]
The full nonneutral mask 63 is omitted from the proper-block list; its observed scalar mode is only 1.

The 63 proper killed-block polynomials have a total degree of 249. The verified finite instance uses seven pairwise distinct holding values. An exact rational polynomial Euclidean algorithm finds precisely 21 nontrivial pairwise gcds among their \(\binom{63}{2}=1953\) pairs. In every such pair the gcd is \(x-1/2\); the 21 pairs are exactly the \(\binom{7}{2}\) pairs of the seven masks above. All 63 polynomials are squarefree and none has root 1. Therefore
\[
\boxed{d_{\min}=1+249-(7-1)=244}.
\]
This is a **strictly positive, reversible, positive-spectrum** stationary sticky-reset chain: the standard diagonal-plus-positive-rank-one symmetrization is positive definite, and the scalar \(\mathbb E F_n\) is completely monotone. Thus the same structurally regular family admits both 250-mode generic and 244-mode exact-collision instances.

**Reproducible finite proof.** Run the standard-library-only \`R231_multipair_collision_exact_check.py\` alongside this note. It computes all polynomials as exact \`fractions.Fraction\` coefficient arrays; executes 63 derivative gcd checks and all 1953 pairwise gcds; validates the three pair cancellations and the seven root masks; and asserts 244. Exact output is in \`R231_verification.json\`. This exhaustive finite rational verification is an exact certificate for the explicitly displayed 7-state parameters, while Theorems 1–2 are symbolic arguments.

## Lemma — every proper killed-block eigenvalue has positive scalar observation mass

Under stationary initialization, \(P\) is reversible with \(\rho_i\propto\pi_i/(1-\alpha_i)\). The symmetric killed block is
\[
K_D=\operatorname{diag}(\alpha_i)_{i\in D}+vv^\top,\quad v_i=\sqrt{(1-\alpha_i)\pi_i}.
\]
For distinct holdings and a secular eigenvalue \(\lambda\), a corresponding eigenvector has components \(v_i/(\lambda-\alpha_i)\). Its scalar observation overlap with \((\sqrt{\rho_i})_{i\in D}\) is proportional to \(\sum_{i\in D}\pi_i/(\lambda-\alpha_i)\). Writing \(q_D=\sum_{i\in D}\pi_i<1\) and using \(S_D(\lambda)=1\),
\[
\sum_{i\in D}\frac{\pi_i}{\lambda-\alpha_i}=\frac{1-q_D}{1-\lambda}>0.
\]
Because \(K_D\) is positive definite and \(P_D\) is strictly substochastic for proper \(D\), \(0<\lambda<1\). Thus every root has strictly positive spectral mass in \(\rho_D P_D^{n-1}\mathbf1_D\); positive R215 source-fiber weights \(W_{|U|}\) preserve this in the total \(\mathbb E F_n\). Repeated roots across blocks add positive weights and cannot cancel. QED.

## Validation scope, current work and next questions

Validation: author proof and exact finite rational verification; 7 source states, 63 proper masks, 1953 gcd pairs, all squarefree checks, all PASS. External independent review NOT_REVIEWED. No statement here uses an unexecuted native BRC numerical operation or reduces the native joint signed/port/provenance/cross-moment carrier.

Unfinished: classify maximal achievable rank loss under strict positivity when k=6; distinguish generic collision codimensions from multi-way positive-weight constraints; compare exact bit/time cost of 244-mode recurrence, 250-mode generic scalar representation and direct reachable 256-state propagation; implement a read-only observer adapter on native \`EffectHistogram\` retaining all typed data. Preserve the existing R230 source and activity history; no formal task CLAIM, Result, Review or Foundation admission is asserted.
