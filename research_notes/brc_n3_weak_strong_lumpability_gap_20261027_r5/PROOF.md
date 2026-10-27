# R5 — Weak predictive invariance does not imply full-history fidelity

Author-side theorem and exact rational verification, 2026-10-27. No native CLAIM, Result, Driver review, or P000 mathematical admission.

## Source and typing

Account GLOBAL_KNOWLEDGE_V1 frozen main at cc9bb8a39531f5b6dc06133d6575cf6f48d21a17. Verified the P000_STARTUP projection against original canonical P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; loaded ACTIVE worldview and original project P000. Project source frozen main at 59cd706d1bd078640f8bbc218622d32e2cbca09c. Reused docs/PORTABLE_RESEARCH_PROTOCOL.md, the existing 14-leaf ancestral-signature theorem (research_notes/brc_n3_signature_kernel_polycoeff_20261027_r5/PROOF.md), and the R5 ternary hinge gate (research_notes/brc_n3_ternary_hinge_variance_support_gate_20261027_r5/PROOF.md). The experiment is an EXTERNAL finite two-measure rational tree: sample count is not Heartbeat native time; exact LR is not an X6 spatial coordinate. Reuse of BRC is ordered positive branch masses, conserved likelihood ratios, labels, and exact occupancy—not a native dynamical calculation.

## Theorem A: history-wise strong lumpability is sufficient for exact four-observer fidelity

Let Q(h)>0 and P(h)=r(h)Q(h)>0 be exact physical arrival masses at each node of a finite horizon-N observation tree. A full-history policy chooses stop/decide P, stop/decide Q, or continue at each ordered history. A seedless time/LR behavioral policy shares one locally randomized action distribution for every pair (t,r), without persistent global random seed. The observer is O=(P(decide Q),Q(decide P),E_P tau,E_Q tau).

For each nonterminal h let K_h(s) be its physical conditional Q distribution of the next time's exact LR s. If K_h(s) is identical for all histories sharing (t,r), then **every** full-history four-vector is attainable by a seedless LR behavioral policy and conversely:

    O_full = O_seedless.

Proof. Under any full-history policy, let m_h be its actual Q occupation mass before the node's action; group by g=(t,r) and sum Q masses for stop/decide P, stop/decide Q, continue as d_g^P,d_g^Q,a_g. Strong lumpability yields m_(t+1,s)=sum_r a_(t,r) K_(t,r)(s). Define the seedless policy at each reached g by local action probabilities (d_g^P,d_g^Q,a_g)/(d_g^P+d_g^Q+a_g), arbitrary at unreachable states. An induction on t reproduces these aggregated Q occupations and action masses. The corresponding P occupation at h is r(h) times Q occupation because the same history-dependent randomized action rule applies under both hypotheses. Hence both policies have the identical four-vector by the linear formulas

    e_P = sum_g r_g*d_g^Q,
    e_Q = sum_g d_g^P,
    E_P tau = sum_g t_g*r_g*(d_g^P+d_g^Q),
    E_Q tau = sum_g t_g*(d_g^P+d_g^Q).

The reverse inclusion is trivial since every seedless LR policy is also a full-history policy. This is a sufficient condition for this observer, not claimed necessary. QED.

This is stronger than *ancestral-signature-averaged* prediction invariance: the latter fixes only the coarse policy's combined kernel, whereas full-history actions can reweight constituent histories within the same signature.

## Theorem B: an exact 14-leaf separation despite weak kernel invariance

Reusing the already published positive 14-leaf model, set root time 0 LR=1, branches at t=1 to a and b with (Q mass, LR) respectively (1/3,2) and (2/3,1/2). Both a and b branch at t=2 with conditional Q weights (1/8,1/8,3/4) into u,v,w. The absolute LRs at au,av,aw are (1,1,7/3); at bu,bv,bw they are (1,1,1/3). Each w has one terminal child of unchanged LR. Each of the four histories h=au,av,bu,bv has three terminal t=3 children with absolute LRs y=(1/2,1,3/2) and Q conditional weights (s_h,1-2s_h,s_h), with

    (s_au,s_av,s_bu,s_bv)=(1/10,2/5,1/5,3/10).

P child masses equal Q child mass times the absolute child LR. Each parent's P and Q mass is conserved and both terminal totals are one; all 14 leaf masses are strictly positive. VERIFY.py checks these statements exactly.

At the only nontrivial coarse collision g=(2,1), the ancestral signatures from a and b each group two equally Q-weighted nodes, with respective averaged s values

    ((1/10)+(2/5))/2 = 1/4 = ((1/5)+(3/10))/2.

Consequently both signature-averaged conditional terminal LR kernels are exactly (1/4,1/2,1/4), and the aggregate next-LR prediction at g is invariant under arbitrary earlier seedless continuation probabilities x_a,x_b>0. All other nonterminal coarse states have one physical history. The *previous verified coefficient theorem* therefore implies the entire seedless four-observer image is a rational convex polytope. Nevertheless strong lumpability fails, since K_au=(1/10,4/5,1/10) and K_av=(2/5,1/5,2/5).

Choose the signed linear four-observer functional

    J = e_P + (3/4)e_Q + (11/200)E_Q tau.

At any LR r, immediate Bayesian-optimal decision has cost min(r,3/4) per unit Q mass. At a t=2 ternary node with parameter s, sampling once more yields Bayes error (3/4)-(s/4) and incurs Q time cost gamma=11/200. Hence continuing beats stopping iff s > 11/50. The full-history t=2 decisions on au,av,bu,bv are therefore stop,continue,stop,continue; the w nodes stop (no future LR change and positive sampling cost). The full t=1 conditional costs to continue are C_a=1279/1600>3/4 and C_b=49/100<1/2; thus a stops, b continues. The root continues because its cost 379/600 is below immediate stopping cost 3/4. An exactly attainable optimal full vector is

    O_F = (43/240,19/40,17/12,7/4),
    V_full = J(O_F) = 379/600 = 1516/2400.

A seedless policy must share one continuation probability theta at coarse node (2,1), even though its two hidden b histories have different s. Under arbitrary theta in [0,1], its t=1 continuation values are

    C_a(theta)=(1288-3theta)/1600 > 3/4,
    C_b(theta)=(788-3theta)/1600 < 1/2.

So a always stops and b always continues, while the root continues. The objective decreases in theta, hence the seedless optimum is theta=1, continuing *both* bu and bv. One optimal seedless vector is

    O_S = (3/16,11/24,3/2,11/6),
    V_seedless = J(O_S) = 1517/2400.

Therefore

    V_seedless - V_full = 1/2400 > 0.

This is a global exact signed support separator, not merely a discrepancy for one particular aggregation algorithm. For both strategy classes J is multi-affine in the independent nonterminal local action probabilities, because a (time,LR) decision variable appears at most once along any trajectory. Thus a global minimum over *all real local randomization* occurs at a deterministic vertex. With positive decision-error coefficients the Bayesian decision at each stopping point is deterministic-optimal as stated. The accompanying Python Fraction checker enumerates all 256 full stopping patterns and all 32 seedless patterns, verifies the four-vectors and performs independent Bellman recursion. Optional root stopping yields J=3/4 and cannot improve either optimum.

**Scope.** Weak prediction invariance suffices for seedless-image convexity, but not full-vs-seedless fidelity. Strong history-wise LR lumpability suffices for the latter. This particular witness has unequal signed support functions; it is not the sought example with equal convex hulls but unequal images. It is a new full-vs-coarse separation *on the already verified safe-signature rational family*, not a new family or native P000/X6 physical result.

## Evidence, controls and next step

VERIFY.py is an exactly arithmetic Python 3 stdlib verifier, run locally as the author-side computation; EXACT_OUTPUT.txt is its original output. The general sufficiency result is proved algebraically; the finite executable independently checks the explicit witness, not the universal theorem. Native control task inventory returned CONTROL_QUOTA and researcher session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. GitHub authentication was awdawmip with repository admin/push. No active native Owner was verified, and no CLAIM, Result, Driver review or mathematical canonical promotion was obtained. The next mother-problem unit is stated in NEXT_TASK.md.