# R5 — Binary LR branching gives exact seedless Markovization; three successors are the first non-lumpable escape

Date: 2026-10-30 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Portable author research only: no Source Task, CLAIM, Result, Driver review or novelty-priority claim.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@f20e408007833bc0518fdb16c4919a705d7b8a77; Enterprise Math main@a406972cef38811f58b5afe38c277037415ef81e. Predecessor: R5 three-stop crossing-merger report commit b5cacce4521c98e56bf3c07ed2cf97b056f46950. This finite stopping model is auxiliary mathematics; P000 and ACTIVE worldview are unchanged.

## Theorem 1: exact two-measure seedless occupancy Markovization

Let H_t be the finite natural histories at the predecision STOP/CONTINUE stage t, with q(h),p(h)>0 and r(h)=p(h)/q(h). STOP is genuine absorption; identical real local action probabilities under P and Q are not controlled by a common persistent random seed. Seedless LR knows only s=(t,r(h)). Assume (i) under natural CONTINUE the conditional Q distribution K_t(s,s') of the next LR state does not depend on which full history h in state s is present, and (ii) absorption time/error rewards are functions of this LR state and stopping action, not of hidden history, with a common P/Q Bernoulli-error kernel (or separately state-measurable P/Q reward functions).

Then EVERY FULL real behavioral strategy has a genuine LR real behavioral strategy with the SAME full stopped-(time,LR) distribution under P and Q. Thus the actual four-observer sets, not merely convex hulls, coincide: O_FULL=O_LR for O=(e_P,e_Q,T_P,T_Q).

Proof: For any FULL policy let m_t(s) be its predecision surviving Q mass in s and a_t(s) the Q mass stopping there. Set the LR STOP probability d_t(s)=a_t(s)/m_t(s) if m_t(s)>0, otherwise any probability. This matches its Q stop and continue occupancy. For FULL, by (i), m_(t+1)(s')=sum_s (m_t(s)-a_t(s)) K_t(s,s'); the constructed LR has the same recurrence, so induction matches all Q occupancies. Along every surviving full history identical policy action factors cancel in the P/Q quotient, so its surviving P mass is exactly r(h) times the Q mass. Since r(h) is constant in state s, matched Q stopping mass a_t(s) entails matched P mass r(s)*a_t(s). State-measurable terminal error and stopping time expectations under each law consequently match. The constructed controller randomizes independently at each LR state and uses no persistent seed. QED.

Boundary: this theorem requires BOTH lumpable next-LR transitions and LR-state-measurable rewards. Identical current LR without transition lumpability is not sufficient. Source/provenance-sensitive observers and nonterminal routing actions are outside its scope.

## Theorem 2: two child LR classes force transition lumpability

Under Q, r_t is a finite-horizon likelihood-ratio martingale on the natural tree:
r(h)=sum_(children h') Q(h'|h)*r(h').
Suppose every history of current ratio r has children in the SAME globally fixed two-point ratio set {R_-,R_+}, with 0<R_-<R_+, both occurring. Normalization and the martingale identity force
K(r,R_-)=(R_+-r)/(R_+-R_-),
K(r,R_+)=(r-R_-)/(R_+-R_-).
These quantities depend only on r, not hidden history. If every stage has this property and errors are LR-local, Theorem 1 proves full actual image equality in ANY finite genuine stopping tree, no matter how many stages. The earlier time-3 crossing ratios r=(3/4,5/4) and terminal ratios (1/2,3/2) force final Q transitions (3/4,1/4) and (1/4,3/4), independently of source X.

For k distinct fixed next ratios, positive conditional weights lie in the affine fiber sum w_j=1 and sum R_j*w_j=r, of relative dimension k-2 where nonempty. Therefore k>=3 is NECESSARY to conceal source-dependent natural transition probabilities within a fixed current LR state. This is a minimality statement for this mechanism, not sufficiency for the mother problem.

Prior art context: R. Laroche and R. Tachet des Combes, "On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs", ICML/PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html . The finite two-measure LR-typed argument here is self-contained; broad Markov occupancy equivalence itself is not claimed as new.

## Exact positive twelve-branch, three-successor crossed construction

Keep Q(X,U) = ((3/8,1/8),(1/8,3/8)), intermediate ratios r_u=(3/4,5/4), terminal ratios R_v=(1/2,1,3/2) for v=0,1,2, and source parameters t_0=1/16,t_1=1/8. Under Q set
  Q(V|x,u=0)=(1/2+t_x,1/2-2*t_x,t_x),
  Q(V|x,u=1)=(t_x,1/2-2*t_x,1/2+t_x).
Define q_xuv=Q(XU=xu)*Q(V=v|x,u), p_xuv=R_v*q_xuv. All 12 p and q are strictly positive and sum to 1. Time-2 ratios are (7/8,9/8), time-3 ratios (3/4,5/4), time-4 ratios (1/2,1,3/2). The last transition is genuinely non-lumpable because t_0!=t_1; all three decisions at times 2,3,4 are true STOP/CONTINUE, and continue from 4 absorbs at time 5.

For a concrete legal common Bernoulli-error kernel, STOP at 2 or 3 has error 1/2, STOP at 4 has error C_v=(1/4,1/2,3/4), mandatory time-5 CONTINUE absorption has error 1/2. FULL uses 2+4+12=18 decision bits; LR uses 2+2+3=7. Let H=e_P-T_P+T_Q.

**Theorem 3: exact strict full-rank hull gap.**
  sup_FULL H=821/1024;
  sup_LR H=205/256=820/1024;
  gap=1/1024>0.
FULL witness: continue at time 2 on both X; at time 3 continue for U=0 and for (X=1,U=1), but STOP for (X=0,U=1); at time 4 STOP exactly when V=2. Its observer is
  O*=(617/1024,291/512,1095/256,573/128),
and H(O*)=821/1024. Every real LR observer satisfies H<=205/256, so distance_infinity(O*,O_LR)>=1/3072, since ||(1,0,-1,1)||_1=3.

Proof of supports without finite sampling: final STOP gain in H per unit Q mass is R_v*(C_v-1/2)+(R_v-1) = (-5/8,0,7/8), so one may choose final STOP iff V=2. The stage-3 CONTINUE-over-STOP gain per unit Q(XU) is
  G_xu=2*(1-r_u)+(7/8)*Q(V=2|x,u);
  (G_00,G_10,G_01,G_11)=(71/128,39/64,-1/128,3/64).
Relative to STOP at 2, FULL can gain
  E_x^FULL=sum_u Q(XU=xu)*[(1-r_u)+max(0,G_xu)].
The values are E_0=277/1024 and E_1=32/1024, both positive. Since all-stop-at-2 has H=1/2, FULL max=512/1024+277/1024+32/1024=821/1024. For LR choosing a shared middle decision pair (h_0,h_1) in {0,1}^2, define
  E_x(h)=sum_u Q(XU=xu)*[(1-r_u)+h_u*G_xu].
Optimize early s_x separately by max(0,E_x(h)). The four exact total H values for (h_0,h_1)=(0,0),(0,1),(1,0),(1,1) are 576/1024,575/1024,803/1024,820/1024. Hence max LR=820/1024. All-real behavioral supports equal deterministic extrema by nodewise multi-affinity: each node is visited at most once.

The LR deterministic policies with lexicographic seven-bit indices 0,32,40,41,44 give five observations with 4x4 difference determinant 135/4194304 != 0. Therefore LR convex hull is four-dimensional, as is FULL convex hull despite their STRICT INEQUALITY. This explicit three-child kernel is a NO-GO for the original hull-equal/image-unequal mother target.

## Typed BRC usage and reproducible evidence

The exact carrier is the 12 positive rational P/Q labeled branch masses. Under any policy, the same local survival factor multiplies P and Q, preserving the pathwise likelihood ratio; the future Q transition distribution is an observer capable of detecting the hidden X residual. Aggregating by LR before this future operation is lossless in the binary model and loses source distinctions in the three-class construction. No negative BRC masses, native X6 transfer, physical claim, or global theorem promotion are asserted.

VERIFY.py uses only Python standard-library Fraction/integer arithmetic: checks exact ratios, positivity and normalization; exhausts all 128 LR and 262144 FULL deterministic H values with an exact 1/1024 integer scale; verifies the explicit FULL observer and rank determinant; and validates 256 seeded rational FULL-to-LR policy projections for the old binary successor tree. EXACT_OUTPUT.txt records actual local stdout. Finite regression does not replace Theorems 1-2, which are analytical.

Smallest next unit: retain these twelve masses, non-lumpable three-class merger and three genuine STOP epochs; vary LR-local or compensated middle/final error kernels to seek complete exact four-dimensional hull equality. Give a nonnegative at-most-five-point rational LR convex combination for every FULL deterministic observer, or an exact Farkas separator. Only a certified hull-equal candidate should proceed to actual seedless-LR real-image analysis; a family-wide no-go theorem is equally valid progress. No duplicate binary-class search.