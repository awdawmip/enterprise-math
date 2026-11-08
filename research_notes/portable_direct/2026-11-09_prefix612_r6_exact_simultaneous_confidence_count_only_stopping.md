# PREFIX-612-R6 — Exact simultaneous confidence and count-only stopping for BRC signed labels

Date: 2026-11-09 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_ARITHMETIC_CHECKED / UNREVIEWED / NOT_ADMITTED

## Frozen source and scope

Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Original native BRC graph: PREFIX-565, Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41.
Exact dependent likelihood: PREFIX-610 at commit 4bdeec79b72e184703390c74bbb020910340b97e, and PREFIX-611 at commit 9b5a1df1a87eca3478a0b2f665b887135ae14711.
Reuse: REUSE_APPLIED to those proven native-reduced signed-label laws. This paper derives their consequences without re-running the original 96-port graph.

Fix k simultaneously critical pairs (1 <= k <= 6, each 4*t_e*t_f=1), d=2k, and the source-phase family pi_theta=uniform_48+sum_l(theta_l*h_l), with |theta_l|<1/48. Every trial independently redraws an initial source phase, makes one weighted BRC native action and observes its terminal phase with one Boolean action-slot tag. It is not one length-N native trajectory. With q=12 for slot 0, q=24 for slot 1 or 2, the signed-label sufficient experiment of PREFIX-610/611 has:

    P(Y=(l,s)) = (1+48*s*theta_l)/(2*q), l=1,...,d, s=+1 or -1.
    P(Y=neutral) = 1-d/q.

M_l counts informative direction-l observations, and K_l counts positive signs among them. The vector (M_1,...,M_d,N-sum M_l) is multinomial(N;1/q,...,1/q,1-d/q), independent of theta. Conditional on the entire direction/neutral index sequence, the signs are mutually independent Bernoulli variables, each with p_l=(1+48*theta_l)/2. Their exact source identities and labels remain available in the underlying experiment, even when a sufficient statistic is used for this restricted likelihood.

## Theorem A: fully finite-sample simultaneous confidence intervals

Choose 0<beta<1. For m>0 and 0<=a<=m define the exact binomial-tail acceptance interval

    C(m,a) = {p in [0,1]:
       sum(i=a..m) C(m,i)*p^i*(1-p)^(m-i) >= beta/2
       AND sum(i=0..a) C(m,i)*p^i*(1-p)^(m-i) >= beta/2}.

For m=0 define C(0,0)=[0,1]. For each direction report

    I_l = {(2*p-1)/48 : p in C(M_l,K_l)} intersect [-1/48,1/48].

For every N>=0 and every admissible theta, conditional on the whole direction-index sequence,

    P_theta(all theta_l in I_l | direction-index sequence)
       >= (1-beta)^d >= 1-d*beta.

In particular with beta=1/240, d<=12 the joint coverage is greater than 19/20. Missing directions with M_l=0 receive the entire possible parameter interval: no fictitious observations.

Proof. Fix m and p. The right-tail binomial probability evaluated at observed K is nonincreasing in K. The event that it is below beta/2 is either empty or one upper tail of mass at most beta/2. The corresponding left-tail rejection is one lower tail of mass at most beta/2. Their union has mass at most beta, so C(m,K) contains the true p with probability >=1-beta for every p. Conditional on direction indices, sign coins for distinct directions are independent; multiply the individual coverage bounds. If m=0 the interval covers with probability one. The parameter transformation is exactly theta=(2p-1)/48. QED.

The same result holds at ANY almost surely finite stopping time based ONLY on the direction/neutral index sequence and independent auxiliary randomness. Conditioning on that stopped index sequence leaves the sign coins independent with unchanged Bernoulli parameters. In particular stopping when all directions have reached r informative observations preserves the coverage. Sign-adaptive stopping has a different obligation (confidence sequences).

For m>0, the exact interval C(m,a) lies inside
  [a/m - sqrt(log(2/beta)/(2m)), a/m + sqrt(log(2/beta)/(2m))] intersect [0,1]
by binomial Hoeffding tails. Thus the theta-interval diameter is at most
  min(1/24, sqrt(log(2/beta)/(2m))/12).
The logarithmic expression is an optional deterministic analytic width bound; the actual acceptance interval is specified by exact polynomial inequalities.

## Theorem B: all-r exact occupancy and sharp thresholds

For integer r>=1, d<=q and N>=0 define D_0(n)=(q-d)^n, with 0^0=1, and recursively

    D_i(n) = sum(m=r..n) C(n,m)*D_(i-1)(n-m), i=1,...,d.

Then, for every theta,

    P_theta(min_l M_l >= r) = D_d(N)/q^N
      = N!/q^N * [z^N] exp((q-d)z)*(exp(z)-sum(a=0..r-1) z^a/a!)^d.

Proof. Realize each direction index by one of q equiprobable slots; d are informative, q-d are neutral (neutral slots may be merged in the recorded observer). D_0 counts words using only neutral slots. When adding the i-th special letter, choose its m>=r positions in C(n,m) ways and fill the remaining n-m positions with a word counted by D_(i-1). This is a disjoint exhaustive enumeration and yields the exponential generating function. Divide the integer word count by q^N. QED.

Monotonicity on appending a sample makes comparison at N and N-1 an exact sharp minimum test. New r=3,4 thresholds for d=12 (the previously published PREFIX-611 covers r=1,2):

| minimum hits per direction | slot0 q12 at 95%,99% | slot1/2 q24 at 95%,99% |
| --- | --- | --- |
| r=3 | 110, 133 | 224, 270 |
| r=4 | 131, 155 | 265, 314 |

These are exact count-coverage thresholds, not stand-alone estimation-error thresholds. For the joint event that all counts reach r and all the reported parameters are covered, the probability is >= (1-beta)^d * D_d(N)/q^N, uniformly in theta. Theorem A's bound on interval diameter supplies an explicit combined width guarantee when a requested r is large enough.

## Corollary: exact expected first full count coverage

For T_1 = min{N: min_l M_l >= 1}, the waiting time with i unseen special slots is geometric with mean q/i. Therefore

    E[T_1] = q * H_d, H_d = sum(i=1..d) 1/i.

At d=12, H_12=86021/27720, and the expectations are exactly 86021/2310 (slot0) and 86021/1155 (slot1 or slot2) independent one-step trials. By the PREFIX-611 thinning coupling, a slot1/2 informative direction is obtained by independently retaining a slot0 informative observation with probability 1/2. Thus T_r(slot0)<=T_r(slot1/2) pathwise under this coupling and equal per-trial costs.

## Certificate, evidence scope, next unit

Companion executable file PREFIX612_R6_exact_joint_confidence_certificate.py and companion result PREFIX612_R6_RESULTS.json reproduce all r=3,4 sharp thresholds. Local execution completed ALL_CHECKS_PASS, 300 exact checks: small exhaustive q-letter strings; independent published r1/r2 formula cross-checks; binomial confidence coverage on a stated rational grid m=0..12 and p={0,1/10,1/5,1/2,3/4,1}; exact rational sharp threshold comparisons at N and N-1. The all-parameter theorem follows from the arguments above, not a finite empirical grid. The code uses only integer and Fraction arithmetic. The original BRC graph was not rerun during this turn.

Next: derive an anytime-valid simultaneous confidence sequence for sign-adaptive stopping, and compare its precision and expected terminal-phase-plus-tag observation cost with these count-only results. Preserve exact source provenance and the original full observer if applying this reduced statistic to different future operations.

Control status for this turn: Source-native session_start request em-r6-20261109-0147-turn11-session and dispatch request em-r6-20261109-0147-turn11-dispatch returned FAILED/GITHUB_HTTP_403. There is no verified native current Researcher-ID, activity, owner or formal CLAIM for this work; Source persistence here is an independent author research note, not formal Result/Review/Working Truth/Foundation admission.
