# R5: two genuine LR mergers with split/reconvergence — exact Jensen support obstruction

2026-11-04, author-side portable research. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Finite auxiliary two-law BRC stopping model, not a native-X6 or physical theorem.

## Scientific scope and immutable inputs
Mother R5 asks for positive source-and-route-sensitive P/Q experiments with equal FULL/seedless-LR four-observer convex hulls but unequal actual real-policy images. This note constructs a genuinely branched, twice merged model and a continuous **open exclusion region**, not such a mother counterexample.
Frozen inputs: GLOBAL_KNOWLEDGE_V1 a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Prior frontier: 2026-11-04 serial-hazard result at 45e9434afa34f375bcb4ba6fc3edf40dae8876ee; interacting predictive lumpability result at c3488066ceb11f3c0bfc0a17f2b23147a95f6ad7. Current behavioral rules are read separately. P000 and ACTIVE worldview unchanged.

## Complete finite model
- At time 1, Q and P each assign origin A/B mass 1/2. Both histories have LR r=P/Q=1, a first information merger M1. Choose stop-and-declare-P, stop-and-declare-Q, or continue.
- Upon continuing, at time 2 a visible L/R route splits. Conditional Q=(1/2,1/2); conditional P=(1/4,3/4), giving LR r_L=1/2 and r_R=3/2. No time-2 choice.
- At time 3, conditional on L: Q(M2 at r=1)=1/4 and Q(side at r=1/3)=3/4, corresponding P=(1/2,1/2). Conditional on R: Q(M2 at r=1)=1/4 and Q(side at r=5/3)=3/4, corresponding P=(1/6,5/6). Side nodes at time 3 must declare P or Q. M2=(time 3, LR 1) joins FOUR distinct positive histories (A,L),(A,R),(B,L),(B,R) and permits stopP, stopQ or continue. Each of the four paths has Q mass 1/16 on arrival if its origin continued.
- At M2, if provenance j continues, at time 4 the terminal LR is (1/2,1,3/2) with conditional Q probabilities (u_j,1-2u_j,u_j) and conditional P probabilities (u_j/2,1-2u_j,3u_j/2), one strictly interior real parameter 0<u_j<1/2 for each source-route j. Every terminal path stops and declares P or Q. Each P/Q row sums to one and has strictly positive entries. This future kernel is genuinely source-and-route sensitive when u_j differ, although all j share the same current (3,1) LR key.

FULL observes entire source/path history and may choose independently at M1 and M2, whereas seedless LR uses only (time,LR) with fresh local randomization and no persistent correlated seed. Readout is the four-vector
O4=(eP=P[declare Q],eQ=Q[declare P],TP=E_P[t_stop],TQ=E_Q[t_stop]).
Source identity, route and multiplicity are retained in the model until observation; this is a positive probability-flow BRC construction, not signed-mass cancellation.

## Exact all-real theorem
Fix n=(1,1,-1/16,0), and for C=FULL or LR define h_C(n)=max of n·O4(pi) over *all real behavioral policies*. For every u in (0,1/2)^4:

h_FULL(n)-h_LR(n)
= {sum_j (u_j-1/8)_+ - (sum_j u_j-1/2)_+}/32
= min{sum_j (u_j-1/8)_+,sum_j(1/8-u_j)_+}/32.

In particular the gap is STRICTLY POSITIVE if and only if some u_j<1/8 and some u_k>1/8. Thus the four-observer convex hulls differ throughout that open, nonempty four-dimensional parameter region. A zero gap for this particular signed direction on the complementary same-side region does not establish all-signed hull equality.

## Proof with upstream optimization included
At LR r, Q mass q, time t, declaration P yields n-payoff q(1-tr/16), declaration Q yields q(r-tr/16). Therefore the optimal t=3 side values per unit Q mass are L: 1-3(1/3)/16=15/16, and R: 5/3-3(5/3)/16=65/48. When both origins continue their total side contribution is (3/8)(15/16+65/48)=55/64.

At M2, r=1, immediate declaration of either kind yields S=1-3/16=13/16 per Q mass. Continuing history j yields, using the terminal LR moment E_Q[r|j]=1 and optimal terminal declarations,
C(u_j)=-4/16+u_j*max(1,1/2)+(1-2u_j)*max(1,1)+u_j*max(1,3/2)
      =3/4+u_j/2.
Thus C(u_j)-S=(u_j-1/8)/2. The terminal declaration maximizing this directional reward depends only on terminal LR, so it is a single valid seedless-LR choice; it does not require hidden origin information.

At first merger M1, stopping at t=1 gives 1-1/16=15/16 per source Q mass. If origin s continues, its *unconditional* side contribution is 55/128, and its two M2 histories contribute at least 2*(1/16)*(13/16)=13/128. Conditional on its initial mass 1/2, the continue payoff is therefore at least 2*(55/128+13/128)=17/16>15/16. Hence each source in FULL and the common LR policy strictly continues at M1, for ALL parameters u in the domain. No upstream decision was silently fixed.

With Q mass 1/16 at each of four M2 histories, FULL optimizes the M2 choice separately. LR must use a common M2 action and sees average terminal continuation value (1/4)sum C(u_j). Hence, exactly,
h_FULL=55/64+(1/16)sum_j max{13/16,3/4+u_j/2},
h_LR=55/64+(1/4)max{13/16,3/4+(1/8)sum_j u_j}.
Their difference simplifies to the first stated formula. For arbitrary real x_j, sum (x_j)_+ - (sum x_j)_+ = min{sum(x_j)_+,sum(-x_j)_+}, so the second formula and iff strictness follow. Bellman maximization at every finite information node is valid for real randomized policies because each local objective is affine in its probability simplex; the displayed maxima are attained by legitimate deterministic choices. QED.

## Fully rational witness; exact support and distance
Choose (u_AL,u_AR,u_BL,u_BR)=(1/32,3/32,13/32,15/32), so all P/Q edges are strictly positive and terminal laws vary by both source and route. FULL: continue both origins at M1; side L declare P, side R declare Q at t=3; at M2 stop-and-declare-P for A histories and continue for B histories; at t=4 declare P at LR 1/2 and 1, Q at LR 3/2. The exact four-observer vector is
W=(181/256,73/128,25/8,25/8),
n·W=277/256.

The optimal seedless LR policy continues at M1 and M2, stops P on L side and Q on R side, then chooses (P,P,Q) at t=4 for LR (1/2,1,3/2). For it h_LR(n)=69/64=276/256. Thus Delta=1/256. Since ||n||_1=33/16, Holder duality implies
dist_infinity(W,conv O4(LR)) >= (1/256)/(33/16) = 1/528.
This automatically also separates W from the actual LR image. The mixed-side gap is a Jensen/positive-part selection residual, not a global impossibility for other constructions.

## Executed certificate, references, next
VERIFY.py (Python standard-library fractions.Fraction) constructs every rational Q/P path, checks normalization and LR moments, evaluates actual O4, enumerates all 288 seedless-LR deterministic policies (3 first choices *2 L-side *2 R-side *3 M2 *2^3 terminal LR decisions), independently checks the Bellman/Jensen formulas, and asserts the distance bound. EXACT_OUTPUT.txt is the executed stdout. These are exhaustive for the declared finite rational LR policy space, not a claim of universal-computation proof. The universal-real parameter theorem follows from the algebra above. No independent scientific review, native Result/CLAIM or native-X6 transfer is asserted.

Related independent mathematical context (not claimed as proof of this theorem): R. Laroche and R. Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, ICML 2023, PMLR 202:18548–18562, https://proceedings.mlr.press/v202/laroche23a.html. Compare current partial-observation verification context in M. Belly et al., Revelations: A Decidable Class of POMDPs with Omega-Regular Objectives, AAAI 2025, https://doi.org/10.1609/aaai.v39i25.34845. Different assumptions and objectives; no global originality priority is asserted.

Next: test the same-side heterogeneous u family where this one normal has zero gap, first u=(5/32,6/32,7/32,8/32), using ALL-SIGNED exact convex-hull certificates (<=5 LR vertices per FULL vector or exact rational Farkas separator) before attempting any real-image nonmembership proof. The R5 mother objective remains OPEN.