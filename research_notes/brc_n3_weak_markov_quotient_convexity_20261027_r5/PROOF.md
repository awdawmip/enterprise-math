# N=3 root-masking quotient: exact convex occupancy flow and proof-gap repair

Date: 2026-10-27. Status: AUTHOR-LEVEL mathematical proof, independent rational check pending remote evidence; NOT a Source-native CLAIM/Result or independent Driver review.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@7b33f8066e9993e7c941959a9d738ed405248eb8, Enterprise Math main@a9ae818f48f4b18e81a48e25a8732a79ccdbba00. Retain ACTIVE P000: the native ontology is discrete six-dimensional Cell space plus separately typed time. The following is an explicitly EXTERNAL finite P/Q sequential decision model using ordered positive branch mass; it is not native BRC/Heartbeat dynamics or an X6 embedding.

## Question and answer

Earlier author result research_notes/brc_lr_n3_any_kernel_root_masking_20261026_r5/PROOF.md showed equality of all signed Bellman support minima in a two-hidden-history N=3 root-masking family. Subsequent research_notes/brc_n3_seedless_behavioral_nonconvexity_20261027_r5/PROOF.md exhibited a general seedless (time,LR) image that is not convex. Therefore the earlier argument's statement that *every* quotient image is convex cannot be used generally. This note proves convexity for **that precise earlier root-masking family**, thus repairing the support-to-policy implication in its proper scope, and rules out that family as a candidate for matching support functions but different attainable images.

At time 1 histories a,b have Q=P=1/2 and L1=1. Under Q, the time-2 LR R lies in {1/2,1,3/2} with transition rows

q_a=(alpha,1-2alpha,alpha), q_b=(beta,1-2beta,beta), 0<alpha,beta<1/2.

Under P the corresponding row is R*q_h(R) (its sum is 1). Time-3 terminal LR Y has a finite positive Q kernel mu_r(y) depending on current R=r, independent of hidden h, with sum_y mu_r(y)=1, sum_y y*mu_r(y)=r. Its P kernel is y*mu_r(y)/r. Policies can stop and decide P/Q at times 0,1,2 and decide at time 3; tau counts observations.

Although q_a != q_b when alpha != beta (failure of strong lumpability at time 1), every (time,LR)-only seedless policy uses exactly the same action distribution at a,b. Consequently, conditional on continuing there, their posterior Q weights remain 1/2 each. The induced quotient continue-transition is policy-independent:

k_r=(q_a(r)+q_b(r))/2.

The final mu_r(y) is also policy-independent and depends only on current quotient r. This is a weak, POLICY-CLASS-SCOPED controlled Markov quotient, not a claim that all full histories are lumpable.

## Theorem: exact flow characterization and convexity

For Q action-flow variables u0^C,u0^Q,u0^P at root, u1^C,u1^Q,u1^P at L1=1, u2,r^C,u2,r^Q,u2,r^P at each r and u3,y^Q,u3,y^P at each terminal y, impose the following LINEAR nonnegative equations:

(1) u0^C+u0^Q+u0^P=1.
(2) u1^C+u1^Q+u1^P=u0^C.
(3) u2,r^C+u2,r^Q+u2,r^P=k_r*u1^C for each r.
(4) u3,y^Q+u3,y^P=sum_r mu_r(y)*u2,r^C for each y.

Because P-arrival mass at any quotient LR=l is exactly l times its Q-arrival mass, the observer map is LINEAR:

e_P=u0^Q+u1^Q+sum_r r*u2,r^Q+sum_y y*u3,y^Q;
e_Q=u0^P+u1^P+sum_r u2,r^P+sum_y u3,y^P;
E_P(tau)=u0^C+u1^C+sum_r r*u2,r^C;
E_Q(tau)=u0^C+u1^C+sum_r u2,r^C.

PROOF, forward: any seedless quotient behavioral policy generates exactly these flows, because its time-1 shared continuation probability preserves the fixed a/b mixture and later transitions depend only on r. PROOF, converse: any nonnegative solution to equations (1)-(4) can be realized without a persistent seed. At each positive-reach state divide its continue/decide-Q/decide-P flows by that state's Q incoming mass to obtain three legitimate probabilities; at zero-reach states pick any action. Induction on t reproduces all flows, including arrivals from multiple r to the same terminal y. Hence the quotient attainable observer image equals the linear image of a compact polytope: it is COMPACT, CONVEX, and rational-polyhedral when the model data are rational. Moreover, any rational feasible flow is realized by rational local probabilities. QED.

The FULL-HISTORY policy observer image is also a compact convex polytope, by the identical Q-mass equations on all ordered histories, where each transition is fixed and local behavior is recovered from positive incoming mass.

COROLLARY: within this family, equality of the minima of EVERY REAL SIGNED linear functional on all four observers implies equality of the FULL and SEEDLESS QUOTIENT images. Proof: two unequal compact convex sets can be strictly separated; unequal images would yield unequal signed support minima. QED.

The earlier author Bellman proof supplies the antecedent, for

0<alpha<=beta<1/2; beta<=3*alpha; 3*beta-alpha<=1.

This note does NOT independently re-prove its all-signed Bellman inequality. Combining that precisely cited author lemma with the new convexity proof repairs the former universal-policy preservation inference. In particular, the stronger desired equal-support/different-image counterexample CANNOT be found inside this common-terminal-kernel family.

GENERALIZATION: for ANY finite positive P/Q tree where, under every seedless quotient policy, continuing from (time t, LR=l) induces a policy-INDEPENDENT Q transition kernel K_t(l,l') satisfying sum_{l'} l'*K_t(l,l')=l, the same flow argument proves the quotient four-observer image convex. Therefore a nonconvex seedless quotient image requires failure of this policy-independent controlled Markov hypothesis, in its declared scope. No native residual-erasure permission follows without the observer/future-operation certificate.

## Exact rational audit

An independent Python Fraction check (external finite rational model, NOT BRC physics) uses alpha=1/4, beta=1/3, k=(7/24,5/12,7/24), terminal Y=(1/4,1,2) and the Q kernel:

r=1/2: (5/7,1/4,1/28);
r=1: (15/28,1/16,45/112);
r=3/2: (1/28,7/16,59/112).

Every Q and induced P row is strictly positive and normalizes; sum_y y*mu_r(y)=r. The kernel violates the earlier convex-order sufficient condition by precisely 27/224 at (Y-1)+, so this is not a trivial iid example.

Two distinct rational quotient policies A and B are evaluated by BOTH direct full ordered P/Q tree summation and quotient occupation flow. The arithmetic average of their Q action flows is then inverted state-by-state into a third seedless policy C (no persistent mixing seed). Direct tree accumulation, all flow equations, and all four observer values agree EXACTLY:

O(A)=(2125259/11612160,4567081/5806080,2041/1152,1003/576);
O(B)=(11461/15750,78139/252000,1291/900,328/225);
O(C)=(37768661/82944000,22740727/41472000,30779/19200,46067/28800)
     =(O(A)+O(B))/2.

Example of recovered probabilities for C: root (continue,decideQ)=(5/6,1/6); time1 (continue,decideQ)=(31/50,1/25). Exact verifier and full output are in the attached complete research packet. This one sample checks the calculation, whereas the polyhedral argument proves the all-real statement.

Evidence boundaries: AUTHOR-LEVEL PROOF plus executed exact Fraction audit. No all-real CAD/QE, no formal Source claim/freeze, no Driver acceptance, no native BRC mathematical runtime or Heartbeat/X6 physics theorem.

Next: search policy-dependent hidden kernels such that signed supports still root-mask but seedless image is nonconvex; require a full rational witness and an ALL-REAL polynomial infeasibility certificate. See NEXT_TASK in the research packet.
