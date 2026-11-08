# PREFIX-621-R6 — Sharp stochastic dominance of BRC confidence stopping and exact uniform quantiles

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Native graph reference: PREFIX-565 blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41 (not rerun here). Provenance-preserving BRC signed-label experiment and corresponding first-passage scope are inherited exactly from PREFIX-610, -613, -615, -617 through -620. These compressed signed labels are sufficient for the specified confidence-width stopping operation; the original branch/port state is retained for any other future native operation.

## Model and first-passage observer

Two identifiable information directions each produce, in an original one-step trial, a positive label with probability p_i/q, a negative label with probability (1-p_i)/q; the remaining probability 1-2/q is neutral. q=12 for Boolean slot-0 observer, q=24 for slot-1/2 observer; p_i in [0,1]. Independent informative signs within each direction are Bernoulli(p_i). Here "trial" is an original BRC action, not a physical time interval.

Set beta=1/40 and the desired diameter delta=1/4 in the p coordinate. For m informative signs and k positive signs let

    C(m,k) = {u in (0,1): 40(m+1)*binom(m,k)*u^k*(1-u)^(m-k)>1};
    D(m,k) = diameter C(m,k).

A direction completes on the first m with D(m,k)<=1/4. For both directions let T_q(p1,p2) be the number of original BRC actions required for both first-passage events.

Define A_0(0)=1 and

    A_m(k) = 1{D(m,k)>1/4}*(A_(m-1)(k)+A_(m-1)(k-1)),

with missing coefficients zero; A_m(k) counts sign histories surviving **all earlier** stopping checks. Put a_m=sum_k A_m(k), and s_m(p)=sum_k A_m(k)*p^k*(1-p)^(m-k). The frozen PREFIX-620 finite Bernstein certificate proves, for all m>=0 and p in [0,1], s_m(p)<=s_m(1/2), with strict inequality for m=25 and p!=1/2. Its exact enumeration covers all m<=189, with A_m=0 for m>=189 and first possible completion at m=25. The pathwise recursion is needed because D(25,25)<=1/4 but D(26,25)>1/4: an already completed history cannot be resurrected.

## Theorem A — Global and sharp first-order stochastic dominance

For every q in {12,24}, p1,p2 in [0,1], and integer N>=0:

    Pr_{p1,p2}(T_q>N) <= Pr_{1/2,1/2}(T_q>N).

For N<50 equality holds (neither pair can finish). For N>=50 the inequality is strict unless p1=p2=1/2.

Proof. Let M1 and M2 count the directions emitted by the N original trials. Their joint law is multinomial with probabilities (1/q,1/q,1-2/q), independent of both sign parameters. Conditional on M1=a and M2=b, sign streams are independent, and the exact chance that both directions have already stopped is

    (1-s_a(p1))*(1-s_b(p2)).

By PREFIX-620's finite checked Bernstein unimodality, each factor is at least its balanced-p counterpart. Averaging over all counts yields the asserted tail ordering. For N<50 each direction requires >=25 informative hits, so the event is impossible. For any N>=50 the count event M1=M2=25, remaining N-50 events neutral, has positive probability. The completion probability of a direction with exactly 25 hits is p^25+(1-p)^25, strictly larger than at p=1/2 if p!=1/2 and strictly positive for all p in [0,1]. Thus the corresponding conditional two-direction product is strictly greater for any nonbalanced parameter pair. QED.

Constructive coupling. In each informative direction, couple its completion count J_i(p_i) and J_i(1/2) by common independent uniform inverse-CDF sampling. The proven survival inequality gives J_i(p_i)<=J_i(1/2) pathwise in that coupling. Use the same independent direction/neutral label sequence for both experiments. Each model stops when both direction counts reach its own required J_i. Thus T_q(p1,p2)<=T_q(1/2,1/2) almost surely in this **observer-level coupling**, proving the full stochastic ordering, not just a comparison of means. The coupling addresses these stopping-observer marginals and is not an equivalence for arbitrary BRC port/branch operations.

## Theorem B — Exact integer tail and globally sharp fixed-N quantiles

For the balanced pair, a_m is finite and zero for m>=189. Define

    M_N(q) = sum_{a=0}^{min(188,N)} binom(N,a)*a_a*[2(q-1)]^(N-a)
    J_N(q) = sum_{0<=a,b<=188; a+b<=N}
           binom(N,a)*binom(N-a,b)*a_a*a_b*[2(q-2)]^(N-a-b).

Then for every N>=0,

    Pr_{1/2,1/2}(T_q>N) = [2 M_N(q)-J_N(q)]/(2q)^N.

Proof. In the fair-sign experiment, survival of one direction after m hits has exact probability a_m/2^m. Binomially select which N positions hit that direction, and count the other q-1 signed/native outcomes, yielding M_N(q)/(2q)^N. Similarly, multinomially select both direction hit sets, yielding J_N(q)/(2q)^N. Inclusion-exclusion gives the displayed integer fraction. QED.

Since Theorem A makes the balanced pair the unique worst tail for N>=50, these finite exact integers determine *parameter-uniform sharp fixed-trial resource thresholds* for both directions reaching the width target:

| Requirement: Pr(both directions have stopped by N) | q=12 (slot 0) | q=24 (slot 1 or slot 2) |
| --- | ---: | ---: |
| at least 95% | **2578 trials** | **5171 trials** |
| at least 99% | **2687 trials** | **5393 trials** |

Exact integer certificates compare the predecessor and candidate counts using 100*tail_(N-1)>(100-target)*den_(N-1) and 100*tail_N<=(100-target)*den_N.

For q=12: CDF at N=2577 / 2578 is approximately 0.949433623759 / 0.950103370021; at N=2686 / 2687 is 0.989891999969 / 0.990054326333. For q=24: CDF at N=5170 / 5171 is approximately 0.949971227076 / 0.950296034773; at N=5392 / 5393 is 0.989931011396 / 0.990010376370. The test itself uses exact integers, not these decimals.

**Distinguish two probabilities.** The 95% and 99% thresholds above concern the probability that the *width condition has been reached* by the stated trial horizon; the inherited anytime **parameter coverage** guarantee is separately at least 95% (PREFIX-613). These are different properties of the same confidence-observer process.

## Earliest-event exact witness

At N=50 the only possible successful count allocation is M1=M2=25, and a 25-sign direction stops only if all signs agree. Hence

    Pr(T_q<=50)
      = binom(50,25)/q^50
        * [p1^25+(1-p1)^25] * [p2^25+(1-p2)^25],

and the balanced value is binom(50,25)/(2^48*q^50). This explicit exact witness verifies strict stochastic separation already at the first possible native-trial horizon.

## Certificate, dependency correction and verification range

Executable stdlib Python source: PREFIX621_R6_stochastic_tail_certificate.py; exact results: PREFIX621_R6_RESULTS.json. An actual run on 2026-11-09 yielded ALL_CHECKS_PASS 364185, with 18,144 symmetry and 9,025 Bernstein shape assertions; exact dyadic width-root comparisons; first informative stop at 25, worst informative stop at 189; independent N=50 CDF identities; and the four quantile boundary integer comparisons. The all-parameter/all-N theorem follows from the analytic multinomial comparison and PREFIX-620's finite exhaustively checked coefficient lemma.

A reproducibility defect was detected in the published PREFIX618_R6_exact_balanced_stop_certificate.py: right-side threshold bisection inverted its bracket update. On the right root, lo is inside and hi outside, so the correct update is 'inside => lo=x, outside => hi=x'. This is repaired in the repository (without rewriting historical commits). With that fix, the code reproduces the published PREFIX-618 exact cost and integer comparison count 364131. It also supports PREFIX-619 and PREFIX-620 imports which otherwise inherited this bug.

No raw PREFIX-565 96-port computation or independent mathematical review was undertaken in this research iteration. This is a BRC-native-derived signed-label model theorem under its exact stated interface, not a Foundation/Working Truth promotion.

## Next discriminating problem

Determine whether Var(T_q) is globally maximal at balanced signs. First-order stochastic dominance proves bounds for increasing losses and all tail/quantile objectives, but variance is not monotone in that order. Reuse the same finite survivor integers to derive a rational second-moment polynomial and either prove its variance ordering or construct an exact rational counterexample. Then consider d up to 12 directions and the least sufficient native branch/port marker under an explicitly specified future-operation horizon.

BRC reuse: COMPOSE_APPLIED PREFIX-610, PREFIX-613, PREFIX-615, PREFIX-617 through PREFIX-620; EXTEND_EXISTING_TOOL the exact BRC signed-label pathwise Bernstein integer-tail certificate.
