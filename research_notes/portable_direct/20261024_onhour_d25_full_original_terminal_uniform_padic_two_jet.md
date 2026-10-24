# D25 / SECOND-DIGIT-LIFT: uniform original-terminal p-adic two-jet and exact normalization obstruction

2026-10-24. Ordinary research author lane: chatgpt-research-onhour-enterprise-math-20260923. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Author-side exact derivation and Fraction regressions, not native benchmark, Source checkpoint/run/Result, CM identification, independent review, or a complete infinite-prime LIFT theorem.

## Frozen question and provenance

Mother objective: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Known publication: TP2-B6F4FC938FF94941C1B7. Frozen mathematical Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). The D24 UR Result was already frozen; do not re-credit it. Consume, without re-crediting, earlier exact WZ five tails (c7fb90fd), five-port third-digit transport (7724e73f), Jacobi half-rank seeds (5404753a/6f14c39f), 575-prime full target test (c6ba00a0), and distinct other-author WZ quotient/Bernoulli work (4f716929). This note is a direct *full-original-terminal* normalization, not another WZ rank shift.

For a prime p=6m+1, m>=1, define

A_m=(6m)!/[3^(6m)((2m)!)^3], R_(m,0)=1,
R_(m,n+1)/R_(m,n)=(4m+2n+1)(3n+1)(3n+2)/
  [36(n+1)(2m+n+1)(4m+n+1)],
S_m=A_m * sum_(n=0)^(4m) (6n+2p-1)R_(m,n).

The original hard target for primes p mod 24 in {13,19}, with *this unchanged terminal and normalization*, is S_m == p*(4/3)^(p-1) mod p^3.

## Theorem 1: exact uniform seam regularization and two jets

For all 0<=n<=4m let eps_n=1_(n>m) and delta_n=1_(n>2m), and define

C_(m,n) = (-1)^n * 2^(-n) * binom(m,n),                        n<=m,
C_(m,n) = (-1)^m*m!*(n-m-1)!/[2^(n+1)*3^(delta_n)*n!],        n>m.

All these C values are nonzero rational p-units. Define, for r=1,2,

X_r(n)=sum_(0<=j<n, j!=m) (j-m)^(-r),
Y_r(n)=sum_(0<=j<n, j!=2m) (j-2m)^(-r),
Z_r(n)=sum_(j=0)^(n-1) (3j+2)^(-r),
D_n=X_1(n)/2-2Y_1(n)/3-Z_1(n),
E_n=X_2(n)/4-8Y_2(n)/9-Z_2(n).

**Exact Q identity**, retaining both singular seam indices and their true p-adic factors:

R_(m,n)=p^(eps_n)*C_(m,n)
  * PROD_(0<=j<n,j!=m) [1+p/(2(j-m))]
  * PROD_(0<=j<n,j!=2m) [(1+p/(3(j-2m)))/(1+p/(j-2m))]
  * PROD_(0<=j<n) [1+p/(3j+2)]^(-1).                    (1)

**Universal termwise third-digit identity over Z_(p)**:

R_(m,n) == p^(eps_n)*C_(m,n)*
   [1+p*D_n+(p^2/2)*(D_n^2-E_n)]                 (mod p^3). (2)

Proof: the original unchanged terminating Pochhammer parameters are

R_(m,n)=(-m+p/2)_n*(-2m+p/3)_n*(2/3)_n/
 [2^n*n!*(-2m+p)_n*(2/3+p/3)_n].

At j=m the first numerator produces precisely p/2 when n>m; at j=2m, the second numerator divided by its denominator produces exactly (p/3)/p=1/3 when n>2m. Removing these genuine factors and evaluating the remaining unshifted product gives the stated C_(m,n), then (1). Every residual denominator is a p-unit: |j-m|<p, |j-2m|<p, and 3j+2 cannot equal p by residue modulo 3 and reaches 2p only at j=4m outside the range. The first and negative second logarithmic coefficients of the remaining p-unit product are D_n and E_n. Expanding the finite product proves (2), including the actual original exceptional n=m and n=2m, without inverting p.

## Theorem 2: complete original endpoint normalized to mod p^2

Define exact rational, p-local finite observers

J0=2^(-m)
 +sum_(n=0)^m (6n-1)C_(m,n)*D_n
 +sum_(n=m+1)^(4m) (6n-1)C_(m,n),

J1=sum_(n=0)^m C_(m,n)*[2D_n+(6n-1)*(D_n^2-E_n)/2]
 +sum_(n=m+1)^(4m) C_(m,n)*[2+(6n-1)D_n].

Then for every prime p=6m+1>=7,

                 S_m == p*A_m*(J0+p*J1)           (mod p^3).  (3)

In particular S_m == 0 (mod p) for **every** prime p=6m+1. For the two original target classes, the as-yet OPEN hard-target condition is **equivalent** to the new same-prime two-digit obstruction

      A_m*(J0+p*J1) ?== (4/3)^(p-1)               (mod p^2).  (4)

Proof: the exact low coefficients are C=(-1)^n*binom(m,n)/2^n. The binomial identities sum C=2^(-m), sum nC=-m*2^(-m) imply sum_(n<=m)(6n-1)C=-p*2^(-m). Substitute (2) into each original summand A_m*(6n+2p-1)*R_(m,n). Low eps=0 terms use the quadratic jet; high eps=1 terms only require the linear jet. Collect the constant, p, and p^2 coefficients after the exact binomial cancellation. The result is p*A_m*[J0+pJ1] modulo p^3. Here A_m is a p-unit because its factorial arguments are all <p. This proves p-divisibility without using either preexisting half-rank seed or the five-tail WZ route. Dividing the exact congruence by p proves (4). The leading obligation A_m*J0==1 mod p and its second-digit successor with J1 remain genuinely unproved.

## Actual arithmetic checks and BRC information boundary

A separate standard-library Fraction checker reconstructs R from its original recurrence, *separately* computes C,D,E, tests (2) termwise including n=m,m+1,2m,2m+1,4m, verifies the exact binomial moments and (3), and compares the unchanged source target as a finite regression. Actual execution covered **37 primes p<=400, p=6m+1**, all PASS. Examples: (p,m,S_m/p mod p^2)=(13,2,144),(19,3,134),(211,35,42201). The checker was also executed directly as a script. These finite regressions are not the universal proof; the universal assertions above rest on the exact rational product and finite p-unit jet calculation. The same-class native benchmark has not been run.

BRC COMPOSE_APPLIED. This is a signed, provenance-labeled finite arithmetic carrier (p,m,n,eps_n,delta_n,C,D,E and the original scalar); the admitted observer is only the full terminal modulo p^3 and its normalized quotient modulo p^2. Exact valuation and both seams remain visible until proved safe for that output. This is an external scalar number-theoretic calculation, not a claim of native Heartbeat World X6 dynamics or a source-authenticated CM/divided-power class. The P000 six-axis premise plus separate time, the observer preservation contract, and original source pin are untouched.

## Durable continuation, native obligations and control truth

Highest author-side result: (1) exact all-n seam product; (2) full two-jet p^3 reduction; (3) full terminal p-divisibility and uniform two-digit obstruction (4). **Do not redo** accepted D24 UR, full WZ five tails, half-rank Jacobi seed reductions, or previous prime scans. Next smallest genuine math unit: establish or falsify A_m*J0 == 1 (mod p) for prescribed p mod 24, then close the second normalized digit with J1 via an authenticated same-class CM/divided-power comparison; the original native experiment/host verification remains separate and NOT_RUN. The exact benchmark input/owner is not confirmed here. Existing support case enterprise-math#1539 is the control permission restoration path.

Sites Gateway 0.6.11 reports static read-only research status (research_authority_granted=false), and its direct recovery_status action is not available as a callable in this execution. No unknown request was replayed, no maintained conversation identity was touched, and no native Researcher session, CLAIM, open/run, checkpoint, Result or independent review is asserted. Three old UR staging materials are independent and not silently imported. This is author GitHub evidence only, not native Source registration/admission. Schedule, notifications, and frozen scientific Source pin are unchanged.
