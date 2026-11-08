# PREFIX-611-R6 — Exact BRC multicritical sampling coverage and a strict Blackwell order

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_COMBINATORIAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Researcher-ID: EM-DIRECT-152A65 / TASK_RESEARCH; Research-Activity-ID: RA-F747DE488855BE8B36642003 (native Source registration, no CLAIM).

## Frozen scientific input and exact inherited model

Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Original native BRC graph: PREFIX-565, Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41. The upstream source for this result is PREFIX-610, 2026-11-08_prefix610_r6_exact_signed_coin_likelihood.md at enterprise-math commit 4bdeec79b72e184703390c74bbb020910340b97e, itself using PREFIX-609 and PREFIX-605. Reuse classification: REUSE_APPLIED to the original native BRC likelihood; this study proves new exact consequences, not a fresh independent re-execution of PREFIX-565.

Fix k simultaneously critical original weighted-BRC incidence pairs satisfying 4*t_e*t_f=1, with 1<=k<=6. These give d=2k disjoint invisible phase-contrast directions h_l. Choose an initial distribution pi_theta=uniform_48+sum_l theta_l*h_l with all |theta_l|<1/48. Each independent trial draws a fresh source phase and performs ONE native weighted action; an N-sample experiment means N independent one-step paths, NOT one length-N native trajectory. Observe the terminal phase jointly with a Boolean tag indicating whether the native action belongs to slot j, j=0,1,2.

PREFIX-610 establishes that each positive-probability tagged-terminal outcome y has baseline mass a_j(y)>0 and likelihood factor 1+48*s(y)*theta_l for at most one l and s(y) in {+1,-1}; otherwise the atom has theta-independent mass. The total informative mass per direction is m_0=1/12 for slot 0 and m_1=m_2=1/24 for slot 1 or 2, split equally between the two signs at the uniform baseline. Different directions have disjoint terminal phase supports. Let q=1/m_j, i.e. q=12 or q=24.

## Theorem A: sufficient signed-label experiment and strict Blackwell order

The full tagged-terminal observation is statistically equivalent, for this exact d-parameter family, to a statistic S_j in {neutral} union {(l,+),(l,-): l=1,...,d} with:

~~~text
Pr(S_j=(l,s)) = (1+48*s*theta_l)/(2q),  s in {-1,+1}.
Pr(S_j=neutral) = 1-d/q.
~~~

Proof: its likelihood factors as a_j(y)*f_theta(S_j(y)). Conditioned on each attainable signed label (or neutral), the distribution of the raw outcomes equals the baseline conditional distribution and does not involve theta. The signed statistic is thus both a deterministic function of the full observation and an exact generative sufficient representation for this family.

For every theta there exists one theta-independent Markov kernel from the complete slot-0 tagged-terminal experiment B_0 to B_1, and another to B_2. Extract S_0, independently delete each nonneutral signed label with probability 1/2 (send it to neutral), keep neutral unchanged, and regenerate a full target tagged-terminal outcome from that label's theta-independent baseline conditional law. The resulting signed-label mass is (1+48*s*theta_l)/48, i.e. the slot-1/2 law, and neutral mass is 1-d/24. The kernel operates on one trial and independently tensorizes over N trials.

The order is STRICT for any nontrivial parameter segment. If theta and theta' differ only in coordinate l, then the full-observation total-variation distances satisfy:

~~~text
TV(B_0(theta),B_0(theta')) = 2*abs(theta_l-theta'_l);
TV(B_1(theta),B_1(theta')) = TV(B_2(theta),B_2(theta'))
                           = abs(theta_l-theta'_l).
~~~

Indeed the changes occur only at the two signed atoms for l. Total variation cannot increase under a parameter-independent Markov kernel; therefore neither B_1 nor B_2 can simulate B_0 on this family. Consequently slot-0 *strictly Blackwell-dominates* each other Boolean slot tag, stronger than the earlier 2:1:1 Fisher information comparison: under the SAME per-trial acquisition cost it cannot be worse for any statistical decision rule estimating this theta family. This is a scoped statistical experiment comparison, not a comparison of full unrestricted phase laws, hardware costs or all possible native observations.

## Theorem B: complete multi-direction sampling coverage

Let M_l be the number of trials with an informative signed label for l (ignoring the sign). For every theta in the open parameter cube and N>=0,

~~~text
(M_1,...,M_d,N-sum_l M_l) ~ Multinomial(N;1/q,...,1/q,1-d/q).
Pr(min_l M_l >= 1) = q^(-N)*
    sum_{a=0}^d (-1)^a * C(d,a)*(q-a)^N.
~~~

These formulas are exact and theta-independent. Proof: each mutually exclusive informative direction has constant mass 1/q, and inclusion-exclusion over any a directions missing in all trials gives (1-a/q)^N. At N=0 the finite formula uses 0^0=1, and the success probability equals 0 for d>=1. Appending a sample shows monotonicity in N, so checking N and N-1 by exact integers gives the strict minimum sample count meeting any fixed probability target.

Likewise, for N>=0 the exact probability that **each direction appears at least twice** is

~~~text
Pr(min_l M_l >= 2) = q^(-N)*sum_{j=0}^d (-1)^j*C(d,j)*
  sum_{a=0}^{min(j,N)} C(j,a)*(N)_a*(q-j)^(N-a),
where (N)_a=N!/(N-a)!.
~~~

Proof: inclusion-exclusion over directions observed at most once. For a selected j-subset, exactly a of those directions can occur once. Choose which a, allocate a distinct positions in (N)_a ways, then assign all other positions among q-j available equally weighted alternatives.

## Exact sharp finite-sample thresholds

For d=12 (all six original incidence pairs critical), the **smallest** independent one-step sample sizes are:

| Requirement | slot 0, q=12 | slot 1/2, q=24 |
|---|---:|---:|
| Pr(all 12 directions observed >=1 time) >=95% | 63 | 129 |
| Pr(all 12 directions observed >=1 time) >=99% | 82 | 167 |
| Pr(all 12 directions observed >=2 times) >=95% | 89 | 180 |
| Pr(all 12 directions observed >=2 times) >=99% | 109 | 223 |

The companion Python certificate computes these and d=2,4 thresholds with exact integer comparisons at N and N-1, tests both finite inclusion-exclusion identities against independent occupancy dynamic programming on small fully covered domains, and verifies theta-dependent thinning and strict total variation at rational sample parameters. Its locally executed verification returned ALL_CHECKS_PASS with 230 exact checks. No floating-point probability approximation is used. These numbers refer to obtaining informative observations, NOT to estimation error guarantees or full 48-phase reconstruction.

## Validation boundary and next unit

Evidence: companion PREFIX611_R6_coverage_blackwell_certificate.py and PREFIX611_R6_RESULTS.json. The standalone arithmetic certificate does not independently re-run original BRC graph actions; the native semantics rely explicitly on the pinned PREFIX-610 verified likelihood reduction. This is an exact **conditional-on-source-likelihood derivation**, not an assertion of Source review, Working Truth or canonical admission.

Next: derive exact simultaneous finite-sample confidence regions for theta with random informative counts, including the missing-count event. Compare the observational/encoding cost of the terminal phase and the Boolean tag; separately test whether any dominance remains under unrestricted unknown initial phase distributions and unequal tag costs.