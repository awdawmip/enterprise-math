# R5 — Occupation-weighted and stage-sensitive two-law LR compression

Date: 2026-10-28, Asia/Shanghai. Author-side: LOCAL_EMR5_20261028_1440_OCC_TV_27C5 / TASK_RESEARCH (local identifier only). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This note is portable research material; it is not a Source CLAIM, service-issued identity, Result or review.

Inputs frozen for this author run: GLOBAL_KNOWLEDGE_V1 main@24e87efc3f9be57dab101b68577900c07d602ea1, Enterprise Math main@f89d309e632bdf08cb6e5c665d3466d2b2efd406. Predecessor: research_notes/brc_r5_multilevel_lumpability_tv_20261028_t1340/RESEARCH.md (its previously proved uniform levelwise bound is not repeated). P000/ACTIVE worldview and portable-research boundaries were read. This result concerns an external finite positive two-law statistical observation tree, not an embedded native X6 system.

## Definitions and theorem

Let N>=2 and each observed finite history h have positive masses p_h=P(h), q_h=Q(h), likelihood ratio r_h=p_h/q_h. Full policies choose stop-declare-P, stop-declare-Q or continue from the raw history, with real local randomness and compulsory stopping at N. Seedless LR policies use only the current (time t, ratio r_h) and fresh local randomness. Define O=(e_P,e_Q,T_P,T_Q), where e_P=P(declare Q), e_Q=Q(declare P), and T_mu=E_mu[stopping stage]. Group histories into fibers F=(t,r). At each nonterminal F, K_h^mu is the conditional next-ratio distribution under law mu given continuation. Put delta_F^mu=max_{h,g in F} TV(K_h^mu,K_g^mu), zero on singletons.

For a full policy pi, denote by R_h(pi) its conditional pre-action reach probability at raw h, and by a_h^c its continue probability. Define its *actual continuing flow* C_F^mu(pi)=sum_{h in F}mu(h)R_h(pi)a_h^c and the stage budget epsilon_t^mu(pi)=sum_{F at stage t} C_F^mu(pi) delta_F^mu. These are typed law/time/source quantities; C_F^P=r*C_F^Q.

**Theorem A (complete real-policy approximation):** For every full policy pi there is a real seedless LR policy bar(pi) satisfying, for each mu=P,Q,

TV(Law_mu(t_stop,terminal declaration | pi),Law_mu(t_stop,terminal declaration | bar(pi))) <= B_mu^e(pi):=min(1,sum_{t=1}^{N-1} epsilon_t^mu(pi)),

|T_mu(pi)-T_mu(bar(pi))| <= B_mu^T(pi):=sum_{t=1}^{N-2}(N-t-1) epsilon_t^mu(pi).

Therefore |e_P(pi)-e_P(bar(pi))|<=B_P^e and |e_Q(pi)-e_Q(bar(pi))|<=B_Q^e. For any signed lambda in R^4, with V_C(lambda)=min_{pi in C}lambda·O(pi),

0<=V_LR(lambda)-V_full(lambda) <= sup_{pi in Full} [ |lambda_1|B_P^e(pi)+|lambda_2|B_Q^e(pi)+|lambda_3|B_P^T(pi)+|lambda_4|B_Q^T(pi) ].

This improves the predecessor's max-fiber-per-stage TV bound for a given policy. A completely policy-independent improvement replaces C_F^mu by its unconditional total history mass sum_{h in F}mu(h). In particular the final nonterminal kernel difference (t=N-1) may affect declaration errors but **contributes zero to expected stopping-time error**.

### Proof A

Write full-policy Q reach weights w_h=q_h R_h(pi) and W_F=sum_{h in F}w_h. For W_F>0 choose every LR action probability as bar a_F^j=sum_h w_h a_h^j/W_F (for zero-mass fibers choose any valid row). Since p_h/q_h is the constant r within F, the conditional action averages of the full process at F are identical under P and Q. Thus both aggregated processes have exactly the same action row at a given (t,r), in each law; their conditional next-fiber distributions after continuation are *possibly different convex combinations* of the K_h^mu in F. Any two such convex combinations have TV at most delta_F^mu, so the one-step row TV is at most bar a_F^c delta_F^mu. Terminal absorbing-label rows coincide exactly.

For each law augment the active LR-fiber distribution at time t by absorbing all prior (stage,label) outcomes. Let rho_t^full,rho_t^LR be the resulting marginals. The full history process admits a time-indexed aggregated kernel conditional on its own actual hidden-source occupation; the LR policy has its own hidden-source mixture. The triangle inequality and stochastic TV contraction give

TV(rho_{t+1}^full,rho_{t+1}^LR) <= TV(rho_t^full,rho_t^LR)+sum_F rho_t^full(F)bar a_F^c delta_F^mu = TV(rho_t^full,rho_t^LR)+epsilon_t^mu(pi).

Initial aggregated states agree. Induction, forced stopping, and TV<=1 prove the terminal joint-TV claim and hence the two error-coordinate claims.

For time, use E_mu[t_stop]=1+sum_{s=1}^{N-1}Pr_mu(t_stop>s). Continuation out of stage s is the same [0,1]-valued function bar a_F^c of the active signature F for both aggregated processes. Accordingly the survival-probability discrepancy at s is <=TV(rho_s^full,rho_s^LR), zero at s=1 and <=sum_{t<s}epsilon_t at later s. Summing s=2,...,N-1 yields sum_{t=1}^{N-2}(N-t-1)epsilon_t. For the signed-support statement, pick a full optimum, construct bar(pi), and use its coordinate bounds; the finite policy cube is compact. All real local random probabilities are included. QED.

**Theorem B (three-signature identity and minimal heterogeneity):** At a given ratio r>0, if two Q next-ratio kernels are supported on a common three-point set 0<s1<s2<s3, their difference d=(d1,d2,d3) obeys sum_i d_i=sum_i s_i d_i=0. Hence d=tau(s3-s2,-(s3-s1),s2-s1), for real tau. Using K_h^P(s)=(s/r)K_h^Q(s) yields

TV(K_h^P,K_g^P)=(s2/r)TV(K_h^Q,K_g^Q).

For an entire such fiber delta_F^P=(s2/r)delta_F^Q, and its P budget is s2*C_F^Q*delta_F^Q, versus Q budget C_F^Q*delta_F^Q. With only two *common* next-ratio signatures both moment equations force the two kernels equal. Heterogeneity requires a union of at least three next-ratio signatures. These are finite rational-mass identities, not claims about native P000 triadic force stability.

## Exact rational two-level example and computational scope

VERIFY.py constructs 22 raw histories, 14 strictly positive terminal leaves, 11 LR fibers at stages 1,2,3. At t=1 tags A,B each have q=p=1/2 and r=1. Their t=2 ratios are (1/2,1,3/2). A has Q conditional row (1/4,1/2,1/4); B has (1/8,3/4,1/8). At t=2 the ratio-1 fiber has exactly these distinct A/B three-child Q rows again; the ratio-1/2 and ratio-3/2 fibers have source-independent binary next multipliers (3/4,5/4) with Q row (1/2,1/2). All local rows satisfy sum Q=1 and sum_s s K^Q(s)=r, and both leaf laws exactly sum to one.

The only nonzero predictive diameters are delta_(1,1)^P=delta_(1,1)^Q=1/4 and delta_(2,1)^P=delta_(2,1)^Q=1/4. The explicitly recorded full policy has C_(1,1)^mu=5/8, C_(2,1)^mu=17/96 under both laws, giving epsilon_1^mu=5/32 and epsilon_2^mu=17/384. Hence the exact per-policy certified terminal-label error envelope is 77/384 and expected-time envelope is 5/32 under both P and Q. The previous levelwise bound is respectively 1/2 and 1. A policy-independent unconditional-fiber envelope also improves these to 13/32 for declaration errors and 1/4 for time.

An actual run of Python fractions.Fraction checked leaf positivity, both law normalizations, every raw conditional mass, diameter identities, complete selected full/averaged four-observer vectors, both coordinate envelopes, both terminal (time,label) TV bounds, plus 100 reproducible rational-policy regression inputs. Output ends ALL EXACT OCCUPATION-WEIGHTED TV CHECKS PASSED. The finite execution does not prove the theorem for all real policies; the mathematical proof does. The example has **not** established all-signed support equality, real LR nonmembership, or a mother-problem witness.

BRC reuse: typed positive rational P/Q branch masses, retained source tags, exact LR and Q/P flux, signed/unsigned residual distinction and observer/future-operation fidelity. No native Heartbeat World X6 Cell embedding/readout/future-relation-preservation has been proved. Source of general background (not a novelty claim): Laroche & Tachet des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, ICML/PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html . Specific results here are the explicitly stated, proved task-level refinements.

## Authority and next

At this run the native task inventory query returned CONTROL_QUOTA; Site status reported research_authority_granted=false and write_relay_enabled=false. Thus active Source owner, native CLAIM, Result and independent Driver review are not verified. Publishing this author-side note does not grant them. Follow-up: keep two interacting predictive-heterogeneous nonterminal LR fibers; first prove equality of all signed four-dimensional support functions (including terminal-label freedom and sourcewise Bellman conditions), then establish an actual rational full-policy four-vector that no real seedless LR policy realizes by global semialgebraic proof. Small TV upper bounds do not imply zero support gap. See NEXT_TASK.md.
