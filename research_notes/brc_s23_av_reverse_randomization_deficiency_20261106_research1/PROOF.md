# S23 AV: exact reverse randomization deficiency for the lawful common-(a,b) c-family

Date: 2026-11-06. Scientific source frozen at Enterprise Math commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Author analytic proof / exact rational validation / unreviewed / not admitted.

## Model and quantifiers

Retain the six source identities AU0, AU1, AV, BU0, BU1, BV, the shared A/B control b and lawful domain Q = [1/2,7/8] x [1/8,1/2] x [1/2,7/8]. Here we restrict to two complete lawful parameter choices with the same a and b, varying only c=x and c=y, where 1/2 <= x < y <= 7/8.

Write q=1-a, r=qx, s=qy. The tagged AV complete stop distributions, omitting only the universally zero stop-2 atom, are A_-=(a,r,q-r) and A_+=(a,s,q-s), on (stop1,stop3,stop4). The deterministic projection W=1 if stop3 gives B_-=(r,1-r), B_+=(s,1-s) on (yes,no).

For a single row-stochastic kernel K from two B outcomes to three A outcomes, independent of the true hypothesis, define

delta(A|B)=inf_K max{ TV(A_-,B_-K), TV(A_+,B_+K) },

with TV(P,Q) = (1/2) sum_j |P_j-Q_j|. The decision horizon is one conditional AV sample.

## Theorem 1: complete all-real classification

For every real legal a,b,x,y with x<y,

delta(A|B) = epsilon = a(s-r)/(2-r-s) = a(1-a)(y-x)/[2-(1-a)(x+y)] > 0.

The infimum is attained by one explicit hypothesis-independent stochastic kernel. Set u=2a/(2-r-s); then 0<u<=1 and

K(yes)=point mass at stop3;
K(no)=u times point mass at stop1 + (1-u) times point mass at stop4.

Both hypothesis-conditional TV errors under this same K are exactly epsilon.

**Upper bound.** Because r+s<=2(1-a)=2q, u is in (0,1]. For z=r or s, reconstruction gives B_z K=((1-z)u,z,(1-z)(1-u)). Its stop3 probability agrees exactly with A_z=(a,z,q-z), and its stop1 error is

(1-z)u-a = a(r+s-2z)/(2-r-s).

This is +epsilon for z=r and -epsilon for z=s. Stop4 carries the opposite signed error, so TV is epsilon in both cases.

**Lower bound.** Let K be arbitrary and e=max_z TV(A_z,B_z K). For a prior t on H_+ and any finite-action decision rule with hypothesis-dependent losses in [0,1], composing the rule with K changes its risk by at most (1-t)TV(A_-,B_-K)+t TV(A_+,B_+K)<=e, by the variational characterization of total variation. Applying this to an A-optimal binary zero-one hypothesis test shows R_B(t)-R_A(t)<=e. The all-real exact Bayes-loss theorem previously proved at Enterprise Math commit 1d2c2123c2ca65468f9f46f81a3e8d166748e622 (PR #1775) gives

max_{0<=t<=1}(R_B(t)-R_A(t))=a(s-r)/(2-r-s),

attained uniquely at t*=(1-r)/(2-r-s). Therefore e>=epsilon for every K. The constructive kernel gives e=epsilon. QED.

## Corollary 2: globally sharp deficiency bound

Across all real lawful a,b,x,y with x<y, 0<delta(A|B)<=1/14. Equality occurs exactly at a=1/2, x=1/2, y=7/8, and any lawful b. At equality the reverse kernel uses u=16/21 and the binary 0-1 loss witness uses t*=4/7.

The all-real parameter maximum and uniqueness follow from the exact rational monotonicity proof for the same function in predecessor PR #1775; that proof is reused at its declared hypotheses.

## Corollary 3: full bounded-decision simulation

For any finite action set and losses bounded between 0 and 1, with either of the two stated AV hypotheses, the excess optimal B Bayes risk over A Bayes risk lies in [0,epsilon] for every prior. The positive-direction inequality follows from deterministic A->B data processing; the upper bound is implemented by K followed by an A-optimal decision rule. epsilon is globally sharp for this family already under binary 0-1 loss.

For n conditionally independent samples under either hypothesis, applying K independently gives TV(A_z^tensor n,(B_z K)^tensor n)<=1-(1-epsilon)^n from the elementary product coupling. This is a constructive n-sample upper bound; sharpness at n>1 is an open subquestion.

## BRC and original S23 mother objective

This uses a source-tagged, positive BRC statistical carrier with six preparations and one shared legal b. The information reduction occurs only in the explicitly conditional AV stop-time observer. K is a decision-side randomization kernel, not an alternative legal physical/source preparation. The exact residual epsilon quantifies the erased stop1-versus-stop4 information, while retaining provenance of the upstream carrier.

For the original ten-label S23 behavioral minimax mother objective, an actual legal encoder/decoder/source-policy bridge is required. A single policy must realize the same conditional AV experiment for both hypotheses before transferring the bound through the relevant sup/inf order. Current mother bounds previously recorded for k=4,6 are [1/2,2/3]. This author-side result does not itself alter those bounds.

## Verification and status

A standard-library Python Fraction exact-check program was executed. It checks 24 legal rational parameter choices, 168 exact priors, 411 exact assertions, normalization, the constructive two-sided TV equality, the Bayes-risk lower dual at t*, and global sharp witness. Its finite tests are secondary to the all-real proof above. See VERIFY.py and RUN_EVIDENCE.txt.

Research status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Formal task claim and independent mathematical review remain separate.
