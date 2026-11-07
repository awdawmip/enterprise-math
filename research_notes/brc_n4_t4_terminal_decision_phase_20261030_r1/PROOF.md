# BRC N=4: lawful terminal decision reveals hidden BU history even at equal T4 continuation

Date: 2026-10-30, author-side analytic finite-model result. Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is **not** a P000 native X6 or heartbeat dynamics theorem.

## Frozen source and question

Continue PR #1738 at dc89f03f4937a34bf514c3edc9bef0b66a75069a, including the preceding exact G(u,v) T4 read-only theorem and its NEXT_TASK.md. The **original** S2/S23 instantaneous behavioral classes and full sixteen-leaf source are specified in Appendix I of 6d9bc93c9d110418d22daf344ed83d883a4a1a23. We study only stage-four *terminal decisions* already expressible in those classes, not a newly invented physical operation that rewrites the source daughter k.

For s in {AU,AV,BU,BV}, j,k in {0,1}, let q_s=(1/6,1/3,1/4,1/4), with the respective P/Q time-three likelihood ratio pairs (9/10,11/10), (1/4,1/4), (1/5,9/5), (2,2). The source masses are Q(s,j,k)=q_s/4 and P(s,j,k)=q_s r_(s,j)/4. All sixteen masses are positive, and both laws total one. The time-four daughter k is fair conditional on (s,j) in both laws.

## Lawful causal family and observer

For all real u,v,d0,d1 in [0,1], define G(u,v,d0,d1). At time one continue A and B; at time two continue AU and BU with the SAME conditional kernel (probability 1) and stop AV/BV with Q; at time three stop AU with P; on BU,j=0 continue to time four with probability u and on BU,j=1 with probability v, otherwise stop with Q; at time four always stop, deciding P with probability d_j and Q otherwise. Behavioral coins are common to P/Q and independent of the future k. The current likelihood ratios 1/5 and 9/5 distinguish BU j=0 and j=1; each stage-four k daughter at fixed j has the same likelihood ratio. Thus all stated decisions are functions of currently available information and satisfy the original stagewise S23 equal-likelihood requirements, hence S2 as well. The decision changes an **observable label**, not the already sampled physical k.

Let Y=(T,Decision,Z_BU,Z_AU,K_obs), where K_obs=k only on actual T=4 and is otherwise bottom. Its event atoms are E=(2,Q,nonBU), A=(3,P,AU), B3=(3,Q,BU), and B4P0,B4P1,B4Q0,B4Q1 (time four BU with decision and k). Define the old compression C: keep E,A; map all B3/B4 atoms to a single B. Thus P_C=Q_C=(7/12,1/6,1/4) for every profile. Set S=(C,j_BU), where j_BU is the *actual* BU time-three branch on the B fiber.

## Theorem: exact four-parameter decision-observer phase and decoder radius

For all real u,v,d0,d1 in [0,1], both laws have E=7/12 and A=1/6. The remaining observable masses are:

| Y atom | P | Q |
| --- | --- | --- |
| B3 | 1/4-(u+9v)/40 | 1/4-(u+v)/8 |
| B4P0 or B4P1 (each) | (u d0+9v d1)/80 | (u d0+v d1)/16 |
| B4Q0 or B4Q1 (each) | (u(1-d0)+9v(1-d1))/80 | (u(1-d0)+v(1-d1))/16 |

Every probability is nonnegative throughout the closed real parameter cube. Summing the rows with both daughter copies gives one under each law.

Consequently the signed P-minus-Q masses are (u-v)/10 at B3; (v d1-u d0)/20 at each B4P daughter; and (v(1-d1)-u(1-d0))/20 at each B4Q daughter. Therefore, **exactly for all real parameters**,

\[
\boxed{\,T(u,v,d_0,d_1)=TV(P_Y,Q_Y)
 =\frac{|v-u|+|v d_1-u d_0|+|v(1-d_1)-u(1-d_0)|}{20}.\,}
\]

The original read-only predecessor is the subfamily d0=d1=0, where T=|v-u|/10. Importantly, for equal continuation u=v=t, the current theorem gives T=t|d1-d0|/10. In particular, if t=1 and (d0,d1)=(0,1), **both probability laws have equal T4 arrival mass 1/4 and equal k marginal**, yet TV(P_Y,Q_Y)=1/10 because the lawful final decision exposes j. At d0=d1=0 instead, TV=0.

As P_C=Q_C, every law-independent randomized decoder D using only C produces a single common law R under both P and Q. The TV triangle inequality gives max(TV(P_Y,R),TV(Q_Y,R))>=T/2. Equality is attainable by a C-preserving stochastic decoder: from E,A keep the event, and on C=B draw the conditional midpoint of the two B-output distributions, namely D(B→y)=2(P_Y(y)+Q_Y(y)) for B outcomes y. These values sum to one since each law has total B mass 1/4. It follows that

\[
\boxed{\,\inf_{D\ \mathrm{P/Q\ common}}\max(e_P,e_Q)=T(u,v,d_0,d_1)/2.\,}
\]

Thus C permits exact common distributional recovery for the stated Y iff T=0, equivalently **u=v and u(d0-d1)=0**. For equal positive continuation, equality of stage-four decision rates is necessary and sufficient. The strong failure witness above has sharp decoder radius **1/20**, even though the predecessor equal-rate *read-only* experiment had radius zero.

The output is a common Markov kernel of the actual j branch. Since under BU,j the T4 continuation and terminal decision coins have rates u_j,d_j and k is conditionally fair under both P/Q, one P/Q-common kernel from S=(C,j_BU) reconstructs the entire Y distribution for *every* parameter profile. Hence one recorded BU branch bit is sufficient uniformly over this family and is necessary uniformly (the t=1,d0=0,d1=1 witness separates C-only). This is distributional sufficiency, not identification of the physical realized k. Pathwise fidelity to all queries about the actual BU daughter still requires recording actual k on T4 arrival.

Finally, the sharp universal upper bound T<=1/10 follows by data processing on BU,j: the P-minus-Q source masses on BU j=0,1 are respectively -1/10,+1/10; all other source-category marginal mass differences vanish for this observer. G's conditional output kernel given BU,j is common to P/Q, so its output total variation cannot exceed 1/10. Equality is attained by the t=1,d0=0,d1=1 lawful strategy. No numerical optimization or external physical premise is needed.

## Exact T4 action-language boundary

Under the original source and S2/S23 action contract, the time-four source daughter k has already been drawn by the fixed P/Q source transition. The policy controls continuation/stopping and terminal decision labels, not a physical assignment or transition k↦k_new. At time four the strategy always terminates; there is no declared within-source action kernel replacing k. Thus an operation that changes the physical k cannot be called an S2/S23 action **within this declared model**. This is a typed-contract statement about the original action alphabet, not a universal impossibility theorem for enriched physical models. Terminal decision rates d_j are already lawful and suffice to demonstrate non-sufficiency of C, with no extra leaf and no post-stopping read.

## Executed check, provenance, and limits

VERIFY.py was executed in Python Fraction. It rebuilds and normalizes all sixteen positive leaves in each of P and Q, compares full seven-atom observation laws and the exact formula for 625 rational profiles (5^4), checks P_C=Q_C, checks the sharp common midpoint radius, and reconstructs both law-specific Y distributions from the SAME conditional S→Y kernel. It checks the rational separating and equal-decision witnesses. The continuous parameter theorem comes from the displayed leaf algebra and TV triangle/data-processing proof, not the finite grid.

Frozen control read: GLOBAL_KNOWLEDGE_V1 main@cbaa938a795f8844f4ab9e22b4e90c06aa2a0b01; EM main@1a63ddbe5fdc213e916cd328edbd61094933974c; predecessor PR #1738 head dc89f03f4937a34bf514c3edc9bef0b66a75069a. Current GitHub actor: awdawmip. Native Site research_authority_granted=false; task owner query returned CONTROL_QUOTA at the read, no owner CLAIM or reviewed Result is inferred. Exact time/origin scope: external 16-leaf source; independent Driver review and P000 six-axis/three-dimensional 晶包/time bridge remain open. This author contribution must not be used as an independent review of itself.
