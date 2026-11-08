# PREFIX-613-R6 — Anytime-valid BRC signed-label confidence under adaptive stopping

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_MARTINGALE_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Original model and observation contract

Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Original native graph: PREFIX-565, Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
Signed-label BRC likelihood from PREFIX-610 (commit 4bdeec79b72e184703390c74bbb020910340b97e) and PREFIX-611 (commit 9b5a1df1a87eca3478a0b2f665b887135ae14711).
The count-only stopping construction PREFIX-612 is preserved in this project under its own complete proof and code. This paper extends its inference to stopping rules that may depend on observed signs.

Fix 1<=k<=6 simultaneously critical incidence pairs, 4*t_e*t_f=1, d=2k. Restrict source distributions to pi_theta=uniform_48+sum_l theta_l*h_l, |theta_l|<1/48. Each independent trial draws a new original source phase, makes one native weighted BRC action and observes the terminal phase jointly with a Boolean slot tag. These observations reduce, for this exact likelihood, to Y in {neutral} union {(l,+),(l,-):1<=l<=d} with

    P_theta(Y=(l,s))=(1+48*s*theta_l)/(2q),
    P_theta(Y=neutral)=1-d/q,

where q=12 for slot0 and q=24 for slot1/2. Direction labels have constant mass 1/q. The conditional sign probability for direction l is p_l=(1+48*theta_l)/2, strictly between zero and one. The full original source/branch/phase observer remains the physical carrier; this is a proven statistical sufficient reduction only for the declared family and outputs.

## Theorem A — exact all-time JOINT confidence region without a d-fold Bonferroni penalty

At global trial count N let M_l(N) be the number of informative labels of direction l and K_l(N) the count of positive signs among them. For integers m>=0 and 0<=a<=m, and 0<p<1 define

    E(m,a;p) = 1 / ((m+1)*binom(m,a)*p^a*(1-p)^(m-a)).
    E(0,0;p) = 1.

For any candidate parameter vector theta set p_l=(1+48*theta_l)/2 and define

    E_N(theta) = product_l E(M_l(N),K_l(N);p_l).

Under the actual parameter theta, (E_N(theta))_(N>=0) is a nonnegative martingale with initial value 1, even with arbitrary global-time sign-dependent decisions about whether to stop observing. Consequently, for every 0<alpha<1,

    P_theta( exists N>=0 : E_N(theta) >= 1/alpha ) <= alpha.

An explicit simultaneous ANYTIME-valid confidence region for the entire parameter vector is therefore

    C_joint(N) = { theta in (-1/48,1/48)^d :
      product_l [ (M_l+1)*binom(M_l,K_l)*p_l^K_l*(1-p_l)^(M_l-K_l) ] > alpha }.

For every admissible theta,

    P_theta( for ALL N>=0, theta belongs to C_joint(N) ) >= 1-alpha.

The set is a joint likelihood-style region and need not be a rectangle. Its defining inequalities are exact algebraic inequalities for fixed integer counts, with no numerical tail inversion and no required random sample count minimum. At M_l=0 the corresponding factor is 1.

**Proof.** Fix a hypothetical p in (0,1). For all m,k the following exact rational identity holds:

    p*E(m+1,k+1;p)+(1-p)*E(m+1,k;p)=E(m,k;p).

It follows by substituting binomial coefficients, or by expanding the reciprocal-factorial identity. At each global trial the direction index is l with probability 1/q independent of theta and of the past; if it is l, only factor l changes, via a Bernoulli(p_l) sign. The displayed identity gives conditional expectation 1 for the ratio of its new to old factor; all other factors are unchanged. A neutral observation changes none. Therefore the product process is a nonnegative martingale with expectation one. Ville's maximal inequality gives the all-N crossing probability at most alpha. This already covers arbitrary stopping times adapted to the observed signs and indices. QED.

## Theorem B — rectangular anytime intervals and a useful width envelope

Define for every direction l and N

    C_l(N) = {theta_l in (-1/48,1/48):
       (M_l+1)*binom(M_l,K_l)*p_l^K_l*(1-p_l)^(M_l-K_l) > alpha/d }.

The same martingale argument applied to each direction, plus union bound across l, yields

    P_theta( for all N>=0 and all l, theta_l in C_l(N) ) >= 1-alpha.

Thus C_rect(N)=product_l C_l(N) is an anytime-valid box, including sign-adaptive stopping. For m>0, writing p_hat=a/m, the elementary binomial bound
    binom(m,a)*p^a*(1-p)^(m-a) <= exp(-m*D(p_hat||p))
with Bernoulli relative entropy D, shows that every accepted p must obey

    m*D(p_hat||p) < log((m+1)*d/alpha).

Pinsker's bound D(x||y)>=2(x-y)^2 then gives

    |theta_l - (2*p_hat-1)/48|
        < sqrt(log((m+1)*d/alpha)/(2m))/24,

so its theta diameter is at most sqrt(log((m+1)*d/alpha)/(2m))/12, additionally clipped by the full admissible width 1/24. The extra log(m) factor reflects all-time coverage; this is not the fixed-m interval in PREFIX-612.

For an example at alpha=1/20 and d=12, m=12, K=6, the rational candidate p=1/2 satisfies E(12,6;1/2)<240 and is accepted in the corresponding direction; p=1/100 satisfies E(12,6;1/100)>240 and is excluded. No floating point evaluation is needed.

## Execution, verification and successor

Companion executable standard-library certificate PREFIX613_R6_anytime_BRC_signed_coin_certificate.py, with result PREFIX613_R6_RESULTS.json, checks the single-coin martingale identity for 693 exact integer/fraction configurations, product-martingale identity for 100 two-direction states, four exact absorbing finite-horizon stopping experiments through N=8 and two rational interval membership tests: 799 exact checks. The executed result is ALL_CHECKS_PASS. Finite enumeration supports the underlying recurrence; the all-time assertion follows algebraically from the martingale identity and Ville's inequality, not extrapolation of horizon eight. The certificate does not re-run the native PREFIX-565 graph.

Next: characterize the exact positive/negative BRC action-coupling cost of implementing the anytime confidence region and compare sharp confidence diameter at fixed stopping budget against the count-only stopping intervals from PREFIX-612. Test whether an observer cheaper than the terminal-phase-plus-slot tag still preserves the same signed-label experiment for all allowed native roots.

Source control for this research turn: native session_start and dispatch both returned FAILED/GITHUB_HTTP_403. No verified current researcher identity, activity, formal owner, CLAIM, Result, Review or Foundation admission is asserted. GitHub note publication is independent author provenance only.
