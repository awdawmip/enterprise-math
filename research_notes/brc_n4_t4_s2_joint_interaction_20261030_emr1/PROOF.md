# BRC N4: S2 stage-four k-dependent decision exposes a pure joint residual

2026-10-30. **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**. Scope: external 16-leaf P/Q finite BRC model, not native P000 X6 dynamics. Extends the prior four-rate result in PR #1738 at a792ea2d6b88e51d71155a65fe4d054a30c5b6fd.

## Frozen source and legal strategy class

For s=AU,AV,BU,BV and j,k in {0,1}, let Q(s,j,k)=q_s/4 and P(s,j,k)=q_s*r_(s,j)/4. In that order q=(1/6,1/3,1/4,1/4), r pairs are (9/10,11/10), (1/4,1/4), (1/5,9/5), (2,2). These are 16 positive leaves per law and both laws sum to one. In particular, BU source masses after summing k are

P(BU,j=0,1)=(1/40,9/40), Q(BU,j=0,1)=(1/8,1/8).

Thus P-Q BU signed j masses are (-1/10,+1/10), while conditioned on BU,j the sampled k is fair in both laws.

Consider original **S2** stagewise policies: continue at stage 1, continue both AU and BU at stage 2 with the identical conditional rate 1, stop AV/BV with Q, stop AU with P at stage 3. At BU,j=0,1 continue to T4 with rates u,v respectively, otherwise stop with Q at T3. Upon reaching T4, the already sampled k is observed and the **terminal decision label** is P with respective rates d_(j,k) and Q otherwise; all six parameters are real in [0,1]. There is no physical operation modifying k. Behavioral random coins have common law under P/Q and do not predict future k.

**Important S2/S23 boundary.** The original S23 language also equates action kernels of equal contemporaneous likelihood ratios. Two k daughters at fixed BU,j have the same ratio, so reachable S23 policies in this family require d_(j,0)=d_(j,1) (unreached cases can be made equal without consequence). The k-dependent witness below is S2, **not S23**. This distinction is supported by the original S2/S23 contract described in OBSERVER_AU_REFINEMENT_NO_GO.md, commit 6d9bc93c9d110418d22daf344ed83d883a4a1a23. The S2 information set is here explicitly assumed to reveal k at T4, as in the frozen source T4 full-history experiment.

Let Y have atoms E=(T2,Q,nonBU), A=(T3,P,AU), B3=(T3,Q,BU), and B4Pk,B4Qk (k=0,1). The old C quotient keeps E,A and collapses B3/B4 to B. Both P_C and Q_C equal (7/12,1/6,1/4).

## Theorem 1: exact six-real-parameter law

Direct leaf aggregation gives

Delta(B3)=(u-v)/10,
Delta(B4Pk)=(v*d_(1,k)-u*d_(0,k))/20,
Delta(B4Qk)=(v*(1-d_(1,k))-u*(1-d_(0,k)))/20,

and Delta(E)=Delta(A)=0. Here Delta means P_Y-Q_Y and every event is observable. Consequently **for every** u,v,d00,d01,d10,d11 in [0,1],

\[
\boxed{TV(P_Y,Q_Y)=
\frac{2|u-v|+\sum_{k=0}^{1}
\bigl(|v d_{1k}-u d_{0k}|+|v(1-d_{1k})-u(1-d_{0k})|\bigr)}{40}.}
\tag{1}
\]

If d_(j,0)=d_(j,1)=d_j, this reduces identically to the earlier four-parameter S23 expression. Equation (1) is exact, not a numerical fit.

## Theorem 2: sharp fixed-(u,v) variation envelope

For each k, put h=v-u, x=v*d_(1,k)-u*d_(0,k). Then x lies in [-u,v] and

|h| <= |x|+|h-x| <= u+v.

The first inequality is the triangle inequality. The second follows because the displayed function is convex and has endpoint values u+v at x=-u and x=v. Inserting into (1) gives, with both endpoints **attained for every fixed u,v**,

\[
\boxed{\frac{|u-v|}{10}\le TV(P_Y,Q_Y)\le\frac{\max(u,v)}{10}.}
\tag{2}
\]

For the lower equality set all d_jk=0; for the upper set d_0k=0,d_1k=1 for both k. Both endpoint policies are within S23 and hence S2. S2's additional expressiveness appears in the *joint structure*, not in this scalar envelope.

## Theorem 3: common reconstruction radius, and a one-bit law decoder

Since P_C=Q_C, every P/Q-common stochastic reconstruction of Y using only C has one recovered output law R under both P and Q. By the TV triangle inequality max(TV(P_Y,R),TV(Q_Y,R)) >= TV(P_Y,Q_Y)/2. Equality is obtained by preserving E,A and on C=B drawing y with conditional probability 2*(P_Y(y)+Q_Y(y)) for each of the five B atoms. These probabilities sum to one. Thus

\[
\boxed{\inf_{D:C\to Y\ \mathrm{P/Q\ common}}\max(e_P,e_Q)=TV(P_Y,Q_Y)/2.}
\tag{3}
\]

The more informative S=(C,j_BU) supports a P/Q-common **distributional** decoder for the entire six-parameter S2 family: on BU,j sample one fair k and apply the continuation and terminal-decision kernel of the chosen policy. Both laws have the same conditional k-distribution given BU,j. Generated-law fidelity is distinguished from recovery of the *authentic* actual k.

## Theorem 4: pure joint-interaction witness restricted to S2

Use u=v=1 and (d00,d01,d10,d11)=(1,0,0,1). This is a deterministic causal S2 policy, but not S23 because k daughters with the same BU,j likelihood ratio receive distinct terminal decisions. In atom order (B4P0,B4Q0,B4P1,B4Q1), the P-minus-Q signed vector is exactly

\[
\boxed{(-1/20,+1/20,+1/20,-1/20).}
\tag{4}
\]

Every other signed Y mass vanishes. Therefore joint TV(P_Y,Q_Y)=1/10 and the sharp common C-only decoder error is 1/20. Yet dropping either k **or** Decision makes the two full observation laws identical. All individual marginals T,Decision,k,C likewise agree. The difference is a pure nonzero Decision–k relational residual whose row and column sums vanish.

For general equal continuation u=v=t and deltas \(\delta_k=d_{1k}-d_{0k}\),

\[
\boxed{TV_{\rm with\ k}=\frac{t(|\delta_0|+|\delta_1|)}{20},
\quad TV_{\rm without\ k}=\frac{t|\delta_0+\delta_1|}{20}.}
\tag{5}
\]

In the restricted S23 class \(\delta_0=\delta_1\), so retaining k does not increase TV at fixed equal continuation. Opposite-sign deltas are available in S2, yielding a zero individual-observer difference and nonzero joint-observer difference. Thus passing two marginal observation checks is insufficient for preserving a joint BRC relation.

## Evidence and transfer boundary

VERIFY.py reconstructs the 16 exact leaves in each law, checks atom differences and equations (1)–(5) on two complete rational six-parameter grids of 729 profiles each, 25 rate pairs and both endpoint families, midpoint reconstruction and the S=(C,j) law decoder. ADVERSARIAL.py independently uses only the BU j masses to reproduce the checkerboard witness and the marginal cancellations. Both were executed with Python Fraction; RUN_EVIDENCE.txt records their actual stdout. Continuous-parameter proof is the explicit leaf algebra and convexity/TV arguments above, not extrapolation from finite tests. The checks are author-side, not independent human review or formal Lean proof.

This result addresses a terminal **decision**, not k-writing physics. The S2 k-reading premise is part of the declared T4 information set; extending to any other original operation language requires checking its frozen information sets. The P000 six-native-axis Cell, three-dimensional slice and separately typed heartbeat time transfer remains a distinct exact correspondence obligation.

Source pins read this turn: GLOBAL_KNOWLEDGE_V1 main 452537354a4962089fa5a5d00066cf3ca14f371a; Enterprise Math main ea390dcadd5d3233200fad2aa0888d427f157db8; PR #1738 prior head a792ea2d6b88e51d71155a65fe4d054a30c5b6fd. Authenticated GitHub user awdawmip. Native Sites status research_authority_granted=false and owner read returned CONTROL_QUOTA. No native CLAIM, Result, independent Driver acceptance or P000 promotion is asserted.
