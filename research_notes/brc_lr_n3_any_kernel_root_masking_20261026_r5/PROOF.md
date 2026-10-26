# N=3 four-observer exact root masking without terminal convex order

2026-10-26 | AUTHOR-LEVEL MATHEMATICAL PROOF, NOT DRIVER-REVIEWED.
Global source snapshot: awdawmip/chatgpt-global-knowledge@d1dd5aa7e590ab3dec37f1f4eb2851770df489c8 (GLOBAL_KNOWLEDGE_V1); original project read: awdawmip/enterprise-math@0929779757189d61ebfa1e815d8c5a31fd95f6df.
Predecessor: research_notes/brc_lr_n3_convex_order_kernel_20261026_r5/PROOF_CONVEX_ORDER.md and NEXT_TASK_PACKET.md at the pinned project read. This note resolves their open *necessity* question. P000, native X6 and Heartbeat constraints are starting rules, not established by this external finite decision model.

## Model and exact theorem

At time 0 the likelihood ratio is one. At time 1 two distinct histories a,b have Q(a)=P(a)=Q(b)=P(b)=1/2. At time 2 the likelihood ratio R takes values (1/2,1,3/2) with the Q transition rows

q_a=(alpha,1-2 alpha,alpha), q_b=(beta,1-2 beta,beta).

Under P the row is (R_i q_h(i)) because L1=1, and is normalized. Assume
0<alpha<=beta<1/2, beta<=3 alpha, 3 beta-alpha<=1.

From time 2 to time 3 allow ANY finite terminal Q likelihood-ratio kernel mu_r on positive Y, with E_mu_r[Y]=r, with no convex-order or common iid-increment assumption. The P transition probability is Y mu_r(Y)/r. Strategies may randomly stop and decide P or Q at times 0,1,2, and must stop at time 3.

THEOREM. For every complete ordered-history randomized strategy, a strategy depending only on (time, current exact LR) has precisely the same four observer scalars O=(P(decide Q),Q(decide P),E_P tau,E_Q tau). In fact the complete and LR-only four-observer attainable sets are equal, for every permitted terminal kernel. If alpha != beta, the time-1 LR class is not strongly Q-lumpable.

## Proof: every signed Bellman support agrees

Fix arbitrary REAL A,B,C,D and minimize
J=A P(decide Q)+B Q(decide P)+C E_P tau+D E_Q tau.
Use Q arrival masses: at LR x, terminal Bayes cost H(x)=min(A x,B), a concave function (minimum of affine functions). Define

m=H(1); gamma=C+D;
phi(r)=min{H(r), C r+D+E_mu_r[H(Y)]}.

phi is the exact Bellman value at time 2. We DO NOT assume phi concave. The stopping option ensures phi(r)<=H(r), hence d0=m-phi(1)>=0. Set
G=2 phi(1)-phi(1/2)-phi(3/2).
Concavity of H and phi<=H imply

G >= 2 phi(1)-H(1/2)-H(3/2)
  = [2 H(1)-H(1/2)-H(3/2)]-2 d0 >= -2 d0.       (1)

Writing f_h=E_{q_h} phi(R) and d_h=m-f_h, the symmetric R rows give

d_a=d0+alpha G,
d_b=d0+beta G,
dbar=(d_a+d_b)/2=d0+(alpha+beta)G/2.               (2)

Claim: dmin=min(d_a,d_b)>=0 and dbar<=2 dmin, WITHOUT any terminal convex order.

If G>=0, then dmin=d_a>=0 and
2 dmin-dbar=d0+(3 alpha-beta)G/2>=0.
If G<0, then dmin=d_b>=d0(1-2 beta)>=0 by (1), and
2 dmin-dbar=d0+(3 beta-alpha)G/2
  >=(1-3 beta+alpha)d0>=0, using the assumptions.
This proves the claim for all real coefficients.

At time 1 the full-history policy may stop separately after a,b, whereas an LR-only policy must share one action. Accounting also for root stopping gives the exact Q-normalized Bellman minima

V_full=m+min{0, gamma-[(d_a-gamma)_++(d_b-gamma)_+]/2},
V_LR  =m+min{0, gamma-(dbar-gamma)_+},              (3)

where x_+=max(0,x). If gamma<=dmin, the positive parts in (3) are affine, so the values coincide. If gamma>dmin, gamma>0 and

[(d_a-gamma)_++(d_b-gamma)_+]/2
 <=(d_a+d_b)/2-dmin=dbar-dmin<=dmin<gamma.

By convexity of the positive part, (dbar-gamma)_+ is at most the same average, so both outer minima in (3) vanish. Hence V_full=V_LR for EVERY real A,B,C,D.

Each finite-horizon policy class has a compact convex four-observer image given by nonnegative occupancy-flow conservation equations. Under a (time,LR)-dependent policy, P flow at any compressed node equals LR times its Q flow; its successor Q transition law is precisely the specified mu_r, which depends only on the compressed r. Every LR-only image lies in the full image. Strict convex separation would produce a real signed support with unequal minimum if the two images differed. Equation (3) rules this out. This proves policy-by-policy existence with equality of ALL FOUR observer values. (This does not claim identical ordered history flow or future interventions outside the declared observer family.)

## A strictly positive rational counterexample to convex-order necessity

Choose alpha=1/4, beta=1/3, terminal Y=(1/4,1,2), and Q rows indexed by r=(1/2,1,3/2):

mu_(1/2)=(5/7,1/4,1/28);
mu_1    =(15/28,1/16,45/112);
mu_(3/2)=(1/28,7/16,59/112).

All entries and induced P rows Y mu_r(Y)/r are STRICTLY positive; every Q/P row normalizes exactly and E_mu_r[Y]=r. The terminal experiment depends on r.

Yet mu_1 is NOT convex-order-dominated by the average of endpoint kernels. For the call-price test (Y-1)_+, the three expectations are (1/28,45/112,59/112). Thus

E_mu_1[(Y-1)_+] - {E_mu_(1/2)[(Y-1)_+]+E_mu_(3/2)[(Y-1)_+]}/2
=27/224>0.

The previous theorem's convex-order condition is therefore NOT NECESSARY for four-observer universal root masking: the present universal theorem proves losslessness for this very kernel, despite the explicit convex-order violation.

Explicit policy pair: raw policy samples at time 0, continues at time 1 only if h=a, continues at time 2 only if (a,R=3/2), and at time 3 declares Q only for Y=1/4 (otherwise P). LR-only policy samples at time 0, at time 1 continues with probability 1/2, at time 2 continues only at R=3/2 with probability 6/7, and at time 3 makes the same Y-dependent decision. The terminal arrival masses under Q and P are 1/8 and 3/16 in both. Exact observer calculations yield

O_raw=O_LR=(1/896,223/224,27/16,13/8).

## Verification and precise scope

Actually executed the standard-library Fraction checker VERIFY.py locally on 2026-10-26. It verifies positive Q/P row probabilities, row sums, mean-preserving LR transport, exact convex-order violation 27/224, explicit O equality, the intermediate proof inequalities and Bellman equality on a signed rational grid of 9^4=6561 coefficients. The 6561 cases are DIAGNOSTIC, not the source of the universal all-real claim; the algebra above supplies that proof. Exact stdout is in EXACT_CHECK_OUTPUT.txt. Source program SHA-256 as locally executed: d038d5e90439a6940d37ff4893d14c5a6d09072e5113aa4a209596403f2391cf. Remote execution is NOT claimed.

All claims concern this external finite Bayesian decision model with precisely declared stopping rules and four observers. This neither proves native P000/X6/Heartbeat dynamics nor authorizes deleting branch/provenance residuals under other future operations. No original-literature priority, formal RESULT freeze, native CLAIM, or independent Driver acceptance is claimed. GitHub authentication is not research task ownership.

## Next unresolved mathematical problem

Find the SHARP alpha,beta region for losslessness against ALL mean-preserving terminal kernels. The proved inequalities are sufficient but not known necessary. Outside this region, seek a strictly positive rational kernel and a signed support separating V_full from V_LR, or establish a larger universal region. Also test N>=4 kernels depending on hidden history beyond current LR; maintain scope and source provenance.
