# PREFIX-622-R6 — Exact BRC first-passage variance and a rational counterexample to variance maximization at balance

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Original PREFIX-565 native graph blob: 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41; no original 96-port graph re-execution in this iteration. Immediate dependencies: PREFIX-610, 613, 615, 617 through 621 (especially the corrected finite first-passage survivor integers and the signed-label observer). All operations and probability calculations use the specified BRC-native-derived signed branch-label statistical carrier; this is not a claim about arbitrary future port operations.

## Selected problem

PREFIX-620 and PREFIX-621 prove that the balanced Bernoulli parameters p1=p2=1/2 uniquely maximize **expected stopping time** and stochastically dominate other parameter values in the following exactly specified original-action experiment. Does the same balanced pair also maximize the stopping-time **variance**?

There are two identifiable directions; an original one-step action emits direction i and + with probability p_i/q, direction i and - with probability (1-p_i)/q, otherwise neutral. q=12 for Boolean slot 0 and q=24 for slot 1/2, with independent trials. Fix beta=1/40 and target p-confidence diameter delta=1/4. A direction is completed upon its first informative count m whose width is <=delta, and T_q is the number of original actions until *both* directions have completed. Original port and slot provenance are retained behind this declared stopping observer.

## Theorem A — Finite exact first and second moment formulas

Let A_m(k) be the integer first-passage survivor counts from PREFIX-621 and let

    s_m(p) = sum_(k=0)^m A_m(k)*p^k*(1-p)^(m-k)

be the probability that an individual direction has not stopped after m informative observations. The exact finite certificate establishes s_m=0 for every m>=189, for all p in [0,1].

For p1,p2, let a_m=s_m(p1) and b_m=s_m(p2). Define the following finite rational sums (all indices 0..188):

    S = sum_m a_m + sum_n b_n
    H = sum_m (m+1)*a_m + sum_n (n+1)*b_n
    C = sum_(m,n) a_m*b_n * binom(m+n,m)/2^(m+n+1)
    K = sum_(m,n) a_m*b_n * (m+n+1)*binom(m+n,m)/2^(m+n+2)
    mu = S-C.

Then the exact moments of the number of original BRC actions are

    E[T_q] = q*mu,
    Var(T_q) = q^2 * ( 2*(H-K) - mu^2 ) - q*mu.

Consequently E[T_q], Var(T_q) are exact rational numbers for any rational (p1,p2), computable by a finite sum with no stochastic simulation.

**Proof.** Embed the original one-step trials as marks of an independent rate-1 Poisson process. Direction-i informative events form independent Poisson processes of rate 1/q. After rescaling time by q, write X for the maximum of their two first-passage times. The single-direction survival probability is

    F_p(u) = exp(-u) * sum_(m=0)^188 s_m(p)*u^m/m!.

The two direction processes are independent, giving

    P(X>u) = F_p1(u) + F_p2(u) - F_p1(u)*F_p2(u).

Gamma integrals yield E[X]=S-C and E[X^2]=2*(H-K), with the stated binomial-coefficient factors. Let tau=qX be the rate-1 Poisson horizon at the T_q-th action. Since the exponential gaps are independent of action marks, E[tau|T_q]=T_q and Var(tau|T_q)=T_q. Therefore E[tau]=E[T_q] and Var(tau)=E[T_q]+Var(T_q). Substituting tau=qX proves both formulas. QED.

A useful exact conversion law follows, for every parameter pair:

    E[T_24] = 2 E[T_12],
    Var(T_24) = 4 Var(T_12) + E[T_24].

This refines PREFIX-615's geometric neutral-thinning law to a direct second-moment identity.

## Theorem B — A verified rational counterexample

The global mean maximizer at balance is **not** a variance maximizer. In the exact experiment above, q=12:

| p1, p2 | E[T_12] (display decimal) | Var(T_12) (display decimal) |
| --- | ---: | ---: |
| 1/2, 1/2 | 2350.887101399933 | 17445.437043378321 |
| 1/4, 1/4 | 1797.011059169207 | 31093.689908873980 |
| 1/8, 1/8 | 1083.217901101868 | 50204.442069243654 |

The companion Python Fraction certificate computes **exact rational numerators and denominators** for all cases and asserts

    Var[T_12(1/2,1/2)] < Var[T_12(1/4,1/4)] < Var[T_12(1/8,1/8)]
    E[T_12(1/2,1/2)] > E[T_12(1/4,1/4)] > E[T_12(1/8,1/8)].

These exact inequalities are a counterexample to the all-parameter assertion that the balanced point maximizes variance. The q=24 analogue follows immediately from the positive formula Var(T_24)=4 Var(T_12)+E[T_24]; here the certificate independently computes and checks its rational values for each parameter pair.

**Information gained:** lower-mean BRC observers can have larger stochastic cost variability; the fair experiment provides a sharp full tail *upper bound* (PREFIX-621), but neither the largest variance nor the largest coefficient of variation follows from stochastic dominance. This distinction guides design of resource-sensitive native observation protocols.

## Execution and cross-checks

Python standard library only: PREFIX622_R6_variance_counterexample_certificate.py; its execution generates PREFIX622_R6_RESULTS.json with complete numerator/denominator Fraction values (including q=24). Executed locally on 2026-11-09; output:

    ALL_CHECKS_PASS PREFIX622 q12 Var balanced,quarter,eighth =
    17445.437043378321026214650779488317
    31093.689908873979659174695955407532
    50204.442069243653567328496239642857

The certificate calls the verified PREFIX-621 pathwise survivor implementation, computes all rational finite moments, tests the exact variance/mean inequalities, and independently checks the one-direction all-positive endpoint case: informative stopping count J=25 is deterministic, and original-action waiting time has negative-binomial variance 25*q*(q-1). It verifies the q=12/q=24 moment conversion algebra on five rational parameter pairs. The exact rational arithmetic and the analytic Poisson-time proof jointly support the declared scoped theorem.

Mathematical inference: Theorem A holds for the stated inherited finite BRC signed-label model and any parameter pair for which the finite sums are defined; the printed rational witness proves the exact negative universal statement targeted in Theorem B. Neither physical-time dynamics nor broader BRC port future equivalence is inferred. No independent review or formal Result/Review/Working Truth/Foundation promotion occurred. Sources for standard anytime confidence-sequence background include Howard et al., Annals of Statistics 49 (2021), DOI 10.1214/20-AOS1991, and Kaufmann & Koolen, JMLR 22 (2021), "Mixture Martingales Revisited"; novelty is scoped to this frozen BRC model's rational first-passage calculation.

## Next research unit

Characterize the variance maxima/minima and tail-dependent risk **within** the compact parameter square [0,1]^2 using the finite rational polynomial defined by Theorem A. A finite Bernstein coefficient / exact derivative-sign certificate may identify extrema, or a verified rational stationary-point bracket may be used as a useful local result. Extend the exact tail and second-moment observer for up to 12 information directions, keeping source/branch identity and the specified future-action scope. Continue native session registration and owner reconciliation only when the actual fixed backend connection is available.

BRC reuse resolution: COMPOSE_APPLIED PREFIX-610/613/615/617/618/619/620/621, EXTEND_EXISTING_TOOL finite rational cost and sign-first-passage survivor transfer.
