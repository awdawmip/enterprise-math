# PFSS admissible-null mechanism screen: shared-q support and covariance certificate
Date 2026-11-18. Task RS-PFSS-JUSTIFIED-NONDEGENERATE-NULL-MECHANISM (TP2-CED1A3712793223C0ABE). Research increment; not an accepted prime-process null or a terminal Result. No PFSS holdout X=3e8 or X=1e9 was opened or evaluated.

Frozen provenance: RR-9F084B92BE8261F3A8D7 (second-order Null A degenerate); RR-4760E87D1D3AD2F6AFFA (finite-window constraints do not identify a probability law), with 2026-09-17 independent Driver reviews.

## Typed finite carrier
Let Q be a finite set of distinct addresses q. Let C be a set of shell/cell observation indices and A=(a_cq) an integer incidence/readout matrix. A shared q address is represented by exactly one latent variable X_q, reused in every cell where q occurs. A primitive linear shell observable is T_c=sum_{q in Q} a_cq X_q. A valid prospective stochastic mechanism specifies a joint law on the *global vector* X, including its support and why this law is applicable to the deterministic prime/semiprime carrier. Algebraic sharing alone does not imply any specific law.

## Exact support and covariance claims
For any random vector X of finite support S and any statistic F on S, Var(F(X))>0 iff two states of positive probability have distinct F-values. Proof: Var=E[(F-EF)^2] is positive iff F is not almost surely constant.

For a *stipulated synthetic* model with independent X_q~Bernoulli(p_q), 0<=p_q<=1,
Cov(T_c,T_d)=sum_q a_cq a_dq p_q(1-p_q)
and Var(T_c)=sum_q a_cq^2 p_q(1-p_q).
Thus T_c is nondegenerate exactly when some a_cq is nonzero and 0<p_q<1. This gives a mechanical necessary-and-sufficient coverage test for linear discovery observables; nonlinear required observables must be audited on their actual support. This independence law is an explicit *additional* premise and has not been derived from arithmetic structure.

## Counterexample to per-cell independence (violates shared q)
One q occurs in two cells c,d. Let each cell assign independent fair flags Y_cq,Y_dq in {0,1}. Then P(Y_cq != Y_dq)=1/2. A single shared q primitive would require equality of these two readings with probability one. Replacing both by the one global X_q fixes address consistency and induces Cov(T_c,T_d)=a_cq a_dq/4 where the common q contributes. The two constructions are observably different. Independent cell noise is not an admissible substitute for global-address randomness without a separate measurement-noise layer.

## Candidate screen
1. iid per cell: explicitly fails shared-q identity if reused q has nontrivial independent randomness.
2. iid Bernoulli per q: respects address consistency and can give nonzero linear variance by theorem; remains a stipulated synthetic law without a source-based justification for prime indicators.
3. Single global random shift of address windows: can preserve common-address bookkeeping if one shift applies to all cells, but primality/semiprime support and shell incidence are not translation-invariant in general. A justified invariant subgroup and conditioning distribution must be supplied.
4. Global permutations of Q: can preserve one-to-one address consistency as a bookkeeping operation; arbitrary permutations break q arithmetic, factoring, shell geometry. Only a demonstrated structural automorphism group could supply an invariance premise.
5. Condition-on-observed residual or variance-floor redesign: inadmissible as post-exposure calibration; cannot establish a source-defensible null.

## Open scientific obligation
Find a defensible number-theoretic ensemble, randomized sampling experiment or independently specified invariance/action on the actual carrier, with frozen parameters and exact law. Verify the complete support of each required discovery observable and the shared-q covariance structure *before* any new statistic or holdout inspection. P000 specifies structure, not a probability law. Present status: exact rejection of per-cell iid, exact criterion for an explicit synthetic alternative, and source gap for a real prime-process null. No terminal claim that all possible mechanisms are impossible.
