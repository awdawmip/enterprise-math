# N=2 nonunit-LR fiber: strong lumpability is necessary even with root stopping

Date: 2026-10-26. Evidence: AUTHOR-LEVEL exact proof, finite strictly positive two-measure ordered tree. This is an **external auxiliary model**, not P000/X6/Heartbeat physics, formal acceptance or native Driver review.

## Source and authority

GLOBAL_KNOWLEDGE_V1 canonical input main@b1c6f9e87fc51617f9b75e37235682850b279b20: bootstrap, operating manual, P000 startup projection matching original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, math/code/BRC policy. EM project source main@2c8e32bebf20b3134d51a709f78fce96fbf992a0; portable protocol docs/PORTABLE_RESEARCH_PROTOCOL.md blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c. Exact predecessor: research_notes/brc_lr_root_masking_20261026_r5/PROOF_LR_ROOT_MASKING_N2.md and NEXT_TASK_PACKET.md. This work answers the predecessor's **nonunit first-LR fiber** problem, not the previously solved all-unit-root masking case.

GitHub actor awdawmip has push permission. Native task read returned CONTROL_QUOTA and native session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Live owner, CLAIM, formal Result and independent Driver review remain unverified; no native role or claim is adopted.

## Statement

Let P and Q give strictly positive probabilities to every raw history in a finite N=2 ordered observation tree. At each n<2 the decision rule may decide P, decide Q or continue, including at the root. At n=2 it must decide P or Q. Policy randomization is hypothesis-independent. Write L_n(u)=P(u)/Q(u), time-indexed T_n=L_n (the statistic carries no extra history label), and O(pi)=(eP,eQ,tP,tQ)=(P_pi[decide Q],Q_pi[decide P],E_P tau,E_Q tau).

**Theorem.** If two first histories h,k satisfy L_1(h)=L_1(k)=l ≠ 1 but have unequal conditional laws of terminal LR L_2 under Q, there exists a full-history policy pi whose four-observer vector cannot be reproduced by ANY randomized time/LR-only policy beta, even when beta may stop at the root. Thus universal four-scalar LR sufficiency necessarily implies strong P- and Q-lumpability on all nonunit first-LR classes. The theorem does NOT claim the same for unit LR classes.

## Complete proof

For any theta>0 consider the real linear functional
J=eP+theta*eQ+C*tP+D*tQ,
where C,D can be signed. In Q-mass units, the optimal terminal decision cost at LR=r is H_theta(r)=min(r,theta). For depth-one history h with LR=l, put
F_h(theta)=E_Q[min(L_2,theta)|h] and d_h(theta)=min(l,theta)-F_h(theta).
Since E_Q[L_2|h]=l, Jensen's inequality for the concave function min(r,theta) gives d_h>=0.

The entire family F_h(theta), theta>0, uniquely determines the finite conditional distribution of L_2: between support atoms its right derivative is Q(L_2>theta|h) and the jumps recover atom masses. Hence distinct conditional LR distributions at h,k imply d_h(theta)≠d_k(theta) for some theta>0. Choose gamma_l strictly between these two nonnegative deficits; in particular gamma_l>0.

Because l ≠ 1, select any gamma_0<0 and set C=(gamma_l-gamma_0)/(l-1), D=gamma_0-C. Then C*l+D=gamma_l while C+D=gamma_0<0. At depth one, the optimal stop loss per Q mass is min(l,theta); optimal continuation cost is gamma_l+F_h(theta). Their difference is d_h(theta)-gamma_l. Thus h and k strictly prefer opposite actions. The full-history optimizer acts independently at h and k. Any T_1-only strategy must choose a single mixture of stop/continue across the entire LR=l class; its cost is strictly greater than the Q-weighted sum of the separate full-history minima. The difference is positive because both histories have positive Q mass. Other LR classes only increase or leave unchanged the T-only versus history-optimum gap. Terminal minimizing actions depend only on L_2, so no terminal hidden-history distinction can erase the bound.

Root stopping does not mask this: immediate root loss is min(1,theta). Root continuation followed by optimal STOP at every first history has cost at most
gamma_0 + sum_h Q(h) min(L_1(h),theta)
<= gamma_0 + min(1,theta) < min(1,theta),
using sum_h Q(h)L_1(h)=1 and Jensen again. Thus both optimization problems STRICTLY continue at the root. Their depth-one strict difference survives root optimization, so min J_full < min J_LR. Universal equality of four-observer attainable sets would imply equality of minima for every real linear J, contradiction. QED.

Why signed sampling weights matter: the proof constructs gamma_0<0 while holding gamma_l at the desired separating value; this is legal for separation of four-dimensional observation sets, though it is not a usual nonnegative sampling-cost Bayes risk. When l=1 the two gamma values cannot vary independently, explaining why the predecessor's root-masking exception is real. The theorem is strictly horizon-two and observer-scoped, with no hidden-port or X6-transfer claim.

## Six-leaf positive rational witness

First-level Q(h,k,z)=(1/6,1/6,2/3), L_1(h,k,z)=(2,2,1/2), P(h,k,z)=(1/3,1/3,1/3). All conditional Q(x,y)=(1/2,1/2). Conditional P(x,y) at h is (3/4,1/4), at k is (1/2,1/2), at z is (1/2,1/2). Terminal LR by raw history is (3,1) at h, (2,2) at k, (1/2,1/2) at z, with no extra terminal statistic beyond these exact LR levels.

Strong P/Q lumpability FAILS on first LR=2. The raw x probability under P is 3/4 at h versus 1/2 at k, difference 1/4; the exact LR=3 class has mass 3/4 at h versus 0 at k. All six raw branch masses are strictly positive; support at an LR level may differ across histories.

For the exact separating objective
J=eP+2eQ+2tP-(15/4)tQ,
the stop/continue losses in Q conditional units are h:(2,7/4), k:(2,9/4), z:(1/2,-9/4); root time increment C+D=-7/4. Full-history Bellman optimum is -21/8, attained by continuing at root, h and z, stopping and deciding P at k; terminal at h x decides P, h y decides Q, and at z decides Q. The resulting observer vector is exactly
O=(5/12,1/4,5/3,11/6), J=-21/8.

Every randomized LR-only policy has J>=-31/12: the LR=2 fiber must share its stop/continue mixture, giving its best Q-weighted contribution 2/3; the z fiber continues with contribution -3/2; plus root increment -7/4. Root stop costs +1. Thus min J_LR=-31/12 and the exact separation gap is
(-31/12)-(-21/8)=1/24>0.
A linear functional attains its minimum at a deterministic LR action table, so randomization cannot evade this lower bound.

## Validation, BRC method and boundary

An actually executed Python standard-library fractions.Fraction checker confirmed positivity, all normalized P/Q rows and exact LR labels; the full witness tuple, both Bellman optima and the exact gap. An independent finite-table check exhausted all 432 deterministic time/LR tables (3 root choices × 3^2 first LR decisions ×2^4 terminal LR decisions), obtaining the same minimum -31/12. The general theorem is algebraic; 432 tables verify only the stated rational witness. Execution output and reproducible checker accompany this proof.

BRC usage: ordered labeled positive rational branch flows transported under P and Q; likelihood ratios are preserved until the explicitly observer-scoped quotient. Method resolution REUSE_APPLIED (existing BRC weighted substrate and horizon-two Bellman/occupancy machinery); no new native BRC mechanism or signed-amplitude identity claimed.

Next unit: mixed first-LR classification when a potentially nonlumpable LR=1 fiber coexists with lumpable nonunit fibers. Find the root-aware support/envelope criterion and exact finite rational examples. Independent native review and any P000/X6 bridge remain open.
