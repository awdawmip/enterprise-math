# R5 — Isolated downstream shared behavior cannot heal the four-observer gap

Date: 2026-11-01 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Immutable input and scope

GLOBAL_KNOWLEDGE_V1 canonical main@88e33cb6174f64cab9d36a80314b9b09cc055874. Its bootstrap, manual, current TASK_RESEARCH router, P000 startup and original (matching blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview, math/BRC/activity rules were read. Enterprise Math control main@f42f2906d77f24085c123f3ccfe9667d41caa96d with current autonomous and portable research protocols. Prior author frontier: enterprise-math research commit 84e59d8af7ec61479ed2f418c3aa21e2cf3ecd05 / brc_r5_source_asymmetric_terminal_gap_20261101_t1840, independently unreviewed.

This is an auxiliary classical finite P/Q stopping process, not native Heartbeat/X6 execution. BRC reuse is the exact nonnegative, source-labelled two-measure branch-flow carrier and the four-coordinate observer (eP,eQ,TP,TQ). H=(5,0,5,-8) is a signed functional only on the OBSERVATION, never signed probability mass.

## Theorem: arbitrary K-only descendant behavioral networks are insufficient

Use the exact earlier I/J/B/C/K positive source-prefix: A1=A2 masses (1/8,1/8); B=(1/4,1/8); C=(1/2,5/8). Shared decision keys are I=(1,1), J=(2,2), K=(3,8/5), where the second component is the P/Q likelihood ratio. At K, each of the two A origins may stop with answer P at time 3 or enter an arbitrary finite downstream behavioral/stochastic network with finite stopping-time expectations.

Scope assumptions: (i) the downstream network is entered ONLY by the two K origins, not by B, C, or another bypass; (ii) it never reuses an earlier behavioral key or an upstream behavioral parameter, nor changes the earlier source prefix; (iii) FULL observes the source and has independent source-contingent tail policies y1 in Y1, y2 in Y2, while LR joint tail policies form a (possibly highly coupled) subset S of Y1 x Y2, with identical behavioral probabilities under P and Q; (iv) the conditional two-law nature kernels are normalized and the four observables are well defined. Further shared time/LR keys among the two K descendants ARE ALLOWED.

For each source i, let gamma_i(y_i) be the H increment relative to P at time 3, normalized by K arrival:
gamma_i = - Pr_P(answer Q | K continued,i,y_i)
          + E_P(T-3 | K continued,i,y_i)
          - E_Q(T-3 | K continued,i,y_i).
Let alpha_i = epsilon gamma_i with the original 0<epsilon<1 K-entry thinning; m_i = inf_{y_i in Yi} alpha_i(y_i) and m12 = inf_{(y1,y2) in S} [alpha_1(y1)+alpha_2(y2)].

Then the exact ALL-REAL behavioral minima for H=5eP+5TP-8TQ are

min_FULL H = -35/8 + [min(0,m1)+min(0,m2)]/8;
min_LR   H = -33/8 + min(0,m12)/8;

G = min_LR H - min_FULL H
  = 1/4 + [min(0,m12)-min(0,m1)-min(0,m2)]/8 >= 1/4.

In particular conv(FULL) != conv(LR). For any minimizing FULL witness W,
dist_infinity(W, conv LR) >= G/18 >= 1/72.

### Proof

The positive K-entry P mass of origin i is epsilon (1-p_i)(1-q_i)/40 and the Q mass equals 5/8 of it. Continuing instead of answering P at K therefore changes H by alpha_i(y_i)(1-p_i)(1-q_i)(1-k_i)/8.

Exact enumeration of the unchanged prefix produces
H_FULL = -33/8
  + SUM_i [13p_i/16 - p_i*q_i/8 + q_i/8
           + alpha_i(y_i)(1-p_i)(1-q_i)(1-k_i)/8]
  - q_B/4 + 5r/2.

For fixed alpha, the source term is multi-affine in p_i,q_i,k_i. Its cube corner minima are min(0,alpha)/8: with p=q=0, k=0 or 1 yield alpha/8 or 0, respectively; q=1 produces 1/8 or larger, and p=1 produces at least 11/16. Independently choose q_B=1, r=0. FULL has independent tail policies, giving the first infimum.

Under LR, p1=p2=p, q1=q2=qB=q, k1=k2=k and tail pair in S. Exact substitution yields
H_LR = -33/8 + (13p-2pq)/8
  + [alpha1(y1)+alpha2(y2)](1-p)(1-q)(1-k)/8 + 5r/2.
The p=q=0, k=0/1 corners yield the negative part of the summed alpha divided by 8; other p,q corners cannot decrease it. Optimize the feasible joint tail pair, giving the second identity.

Since S is a subset of Y1 x Y2, m12>=m1+m2. Because min(0,a+b)>=min(0,a)+min(0,b) and min(0,x) is increasing, G>=1/4. Linear support extrema are unchanged by convexification; Holder's inequality with ||H||1=18 gives the distance bound. All-real quantifiers follow from exact algebra and optimization over complete behavioral sets, not finite testing. QED.

## Strictly positive example: a genuine FOURTH shared decision key

Take epsilon=1/2. After K continuation, a natural split under P/Q sends low (1/4,1/2) to answer Q at time 4, and high (3/4,1/2) to the real shared behavioral key L=(4,12/5). At L, source i stops P at time 4 with probability ell_i, otherwise answers Q at time 5. LR must set ell1=ell2=ell; FULL may choose ell_i independently. Both natural branches have strictly positive probabilities under both measures. Low terminal key is (4,4/5) with answer Q; the high key is (4,12/5) with optional P stop, or (5,12/5) with Q answer; no answer-key conflict. This cannot be relabeled as a fixed tail: a genuine LR-shared action takes place at L.

Exact conditional gamma_i(ell_i) = -3/4+ell_i/2; alpha_i(ell_i)=-3/8+ell_i/4. Consequently m1=m2=-3/8, m12=-3/4 and

min_FULL H = -143/32; min_LR H = -135/32; gap G = 1/4.

A FULL minimizing witness has p1=p2=q1=q2=r=k1=k2=ell1=ell2=0 and qB=1, with
W=(31/40,15/64,427/160,347/128); H(W)=-143/32;
dist_infinity(W,conv LR)>=1/72.

The k=1 LR slice retains four independent coefficient directions with exact determinant 59/20480 != 0; hence LR affine rank is 4.

## Verification, source typing and boundary

VERIFY.py is a standalone Fraction checker. It constructs nonnegative source-labelled P/Q branch masses, checks both complete probability normalizations, all 1024 FULL and 32 LR deterministic observation vertices and H formulae, the full/partial extrema, W, determinant, and the gap. EXACT_OUTPUT.txt is captured real stdout. Finite exact checking verifies THIS finite model; it does not formally check the universal arbitrary-descendant theorem, which relies on the proof above.

A downstream key fed by a BYPASS origin outside K, or an alteration of I/J/source geometry, violates the isolated-descendant hypothesis. The mother question conv(FULL)=conv(LR) but unequal actual real policy images remains OPEN. No native X6 correspondence, theorem admission, formal Source CLAIM/Result, or independent review is claimed.

Current native em_status: research_authority_granted=false; executor_binding_configured=false; control CODE_REVIEW_REQUIRED; active quota 5/5. Attempted native owner inventory returned CONTROL_QUOTA. Portable GitHub publication does not imply role-bound task ownership.
