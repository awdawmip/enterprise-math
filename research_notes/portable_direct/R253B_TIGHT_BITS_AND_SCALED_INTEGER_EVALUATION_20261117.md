# R253B — Tight explicit output size and integer-scaled binary evaluation for 63 labelled masks

Scientific date: 2026-11-17 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED.
Frozen input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessors: R252 e23e0150fc15b9a32df3c8b7cf94a5d9a83a07c9; R253 f56ec5905e8eb21ce9f83f29fe71c909e347161c.
The subject is the auxiliary positive scalar observer, not a native X6/BRC signed-port claim.

## Theorem A — matching bit-size upper and lower bounds

Fix any admissible rational s in (39/100,41/100). For the unchanged seven-source R252 model let
D_m={0} union {i+1: bit i of m is set}, 0<=m<=62, with d_m=|D_m|,
P_D[i,j]=a_i delta_ij+(1-a_i) pi_j,
h_{m,k}=W_popcount(m) rho_D^T P_D^k 1 (k integer >=0),
and W=(144,576,1440,4320,17280,86400,518400).
All a_i, pi_i, rho_i are rational and positive, with 0<a_i<1, sum_i pi_i=sum_i rho_i=1.

Let L(s) be the positive least common multiple of denominators of all 49 entries of the full seven-by-seven P, and let J(s) be the least common multiple of denominators of all 249 weighted entries W_popcount(m) rho_i, i in D_m. Both are finite integers for each fixed rational s.

Set A_m=L P_D (integral) and B_m=J W_popcount(m) rho_D (integral). Then for every k>=0
  N_{m,k}=B_m^T A_m^k 1 is a positive integer,
  h_{m,k}=N_{m,k}/(J L^k),
  0 < N_{m,k} <= J W_popcount(m) L^k.

Consequently the total conventional numerator/denominator bit length of the 63 separately labelled, REDUCED exact rational values at one event k is
  Theta_s(k+1).

The upper bound follows from these explicit integral representatives, the fixed number of labels, and numerator <= W_popcount(m) times denominator. The lower bound is the R253 singleton mask m=0, whose reduced denominator has k log_2(12)+O_s(1) bits for EVERY fixed admissible rational s. Thus the two bounds match. The event index of R252 is n=k+1.

## Theorem B — a concrete bit-algorithm upper bound

For each fixed rational s, the 63 exact UNREDUCED fractions with common denominator J L^k can be generated using binary powering of the nonnegative integral matrices A_m (dimensions at most 7), with O_s((k+1)^2) elementary bit operations under ordinary schoolbook integer multiplication.

Proof: row sums of P_D are at most 1, since sum_{j in D} pi_j<=1. Hence row sums of A_m^t are at most L^t; entries of all intermediate binary powers A_m^(2^j) use O_s(2^j+1) bits. Each fixed-dimension square/matrix-vector product at level j uses O_s(4^j) schoolbook bit operations. Summing the geometric levels up to floor(log_2(k)) costs O_s((k+1)^2). The common denominator L^k is computed once with the same bound. This describes integer-scaled representation construction; making 63 REDUCED fractions also requires their gcd/division and formatting costs, which are not included in this particular bound.

This explicitly separates R252's O(1071 log(k+2)) rational-field operations from actual bit complexity and the Theta_s(k) output-size cost. This is an upper bound for the proposed alternative; it is not a claim of optimal bit-running time or superiority over R251.

## Theorem C — there is no parameter-independent finite scaling denominator

For 0.39<s<0.41 the fourth nonzero-index diagonal component obeys
  P[4,4](s) = s + (5/18)(1/2-s) = (13/18)s+5/36.
Take s_q=2/5+1/q for any prime q>100. Then s_q is admissible and
  P[4,4](s_q)=(77q+130)/(180q).
Since q does not divide 130, its reduced denominator is divisible by q. Arbitrarily large primes q occur, so no single finite integer L can clear all rational parameter denominators throughout the open interval. Any uniform bit bound must account for rational parameter height. This is independent of the fixed-parameter Theta_s(k) conclusion.

## Exact validation

A standalone Python Fraction checker reconstructs frozen a,b,pi,rho, all 63 subsets and integer-scaled transition matrices. At s=39/100,2/5,41/100 and k in {0,1,2,8,32}, it compares the independent direct Fraction recursion with integer-scaled binary matrix powering at all 63 labels: 3*5*63=945 exact equalities; positive numerator, divisibility and bit bounds also pass. Four prime witnesses q=101,103,127,1009 check Theorem C's denominator fact. The program outputs R253B_verification.json and printed PASS.

Certified scaling anchors:
- s=39/100: L=30669704049600, J=1264239823;
- s=2/5: L=552847680, J=2055053;
- s=41/100: L=29048283633600, J=400724401.

The proof of the theorems is universal over stated fixed rational parameters. Numerical checking covers only the listed finite test cases. No independent mathematical review, formal CLAIM/Result, or native BRC EffectHistogram execution is claimed.

## Next research frontier

Explore representation-sensitive lower bounds and efficient exact reconstruction for the aggregate 229-order scalar observer versus the 63-labelled carrier. In particular, determine whether a shared integer denominator can be made substantially smaller than J L^k while retaining the 63 individual labels, and measure exact bit-cost in realistic event horizons. The continuous-parameter 270/403 two-mode threshold problem remains open. Preserve native provenance/type boundaries before any BRC port compression.
