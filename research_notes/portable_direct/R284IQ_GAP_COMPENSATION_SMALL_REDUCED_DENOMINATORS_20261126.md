# R284IQ — Compensation across convergent gaps with small reduced denominator
2026-11-26. Author proof, NOT_REVIEWED. Own directed R284 frontier; no shared Task claim or state mutation. The original own registration r1-20261124-0256-r284gd-session-v1 returned SUCCEEDED and recovery returned own session, not closed, no runs. EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Owner inventory r1-20261126-1700-owner-inventory last observed RUNNING before proof publication; this does not confer authority. Account entry blobs matched main@3ba5ea237f8ecb60b3e7bd28a61ceedefa9f9da7, P000 V4 projection hash matched, Source foundation V5 startup and ACTIVE worldview consulted. External arithmetic observer only, not native spatial attribution.

Frozen inputs:
- IP @8c838a160e4159db2864ae4dd46c9e59576a9638:research_notes/portable_direct/R284IP_CONVERGENT_WINDOW_POWER_SAVINGS_20261126.md
- IO @b6d9d4c99b9fcba85c5fca2e9eb83fe763d276cf:research_notes/portable_direct/R284IO_CRITICAL_TRANSCENDENCE_E_FUNCTIONS_20261126.md
- IL @0ba4281d63293680694a2bb4843b732fd2cf819f:research_notes/portable_direct/R284IL_QUANTITATIVE_JOINT_DIOPHANTINE_SEPARATION_20261126.md
- IJ/IK/ID through IP and IO; actual minimum interpretation retains author-level ID monotonicity; independent review pending.

## New result
Write s=s0, z=s², C=C0, A=1/z, B=-2C/z, Q_n=A n²+B n+C²/z. For integer M large let a/r be a reduced rational with
|A-a/r| <= 1/(r M).
In particular one can take the convergent with r<=M<R (R next denominator). Unlike IP's favorable endpoint windows, the following controls arbitrarily deep intermediate windows if the preceding denominator is small.
Define absolute interval discrepancy E_M as the supremum, over integer subintervals I of [1,M] and circular intervals J, of |#(n in I: {Q_n} in J)-|I||J||.

Theorem 1. For any fixed 0<=theta<1, c>0 and 0<kappa<(1-theta)/(2(2-theta)), if r<=c(log M)^theta, then E_M=O(M^(1-kappa)), uniformly over the specified rational approximations and subintervals. Constants may depend on theta,c,kappa and the actual endpoint pair. No finite irrationality measure is assumed. For example theta=1/2 permits any kappa<1/6, theta=1/3 permits kappa<1/5, theta=2/3 permits kappa<1/8. Theta=0 is a formally valid bound, but bounded r cannot persist as M tends to infinity for this irrational A.
Theorem 2. Put L=log M/log log M. If r<=L/100 and |A-a/r|<=1/(r M), then E_M=O(M exp(-L/10)). Thus even certain denominators at the IL/IM logarithmic scale give much faster discrepancy decay when one uses the actual endpoint pair instead of general simultaneous separation.
These are conditional-on-window bounds, not claims that the specified window regimes recur infinitely often for the actual A.

## 1. A rational approximant to the endpoint ratio, preserving reduced denominator
IL supplies the exact relation exp(z/2)=R(z,C) where
R(z,C)=(8C p_f(z)-n_f(z))/(n_e(z)-8C p_e(z)),
n_e=40z³-470z²+1179z+328, n_f=364z³-1068z²+1069z-328,
p_e=60z²+8z+13, p_f=78z²-73z-13.
The denominator is bounded away from zero in a fixed compact neighborhood of (z,C), as proved in IL; R is Lipschitz there. Write delta=A-a/r. For h>=1 put l nearest to hrB, t'=r/(2a), z'=r/a, C'=-l/(2ha). The approximant v/d=R(z',C') has positive denominator d<=C_1 h r³ after reduction: multiplying numerator and denominator by h a³ clears all rational coefficients. Also |z-z'|+|C-C'|<=C_2(|delta|+||hrB||/(hr)), by reciprocal and product Lipschitz bounds near A. For M large, the points are in the fixed neighborhood uniformly in h and r for which hr tends to infinity; if hr is bounded, the C' neighborhood may fail. In that case ||hrB||/(hr) is bounded below by a fixed positive neighborhood radius, so the detuning conclusion below holds directly. More generally whenever the neighborhood fails the same direct bound holds, since |delta| tends to zero. In the neighborhood,
|exp(t')-v/d|<=C_3(|delta|+||hrB||/(hr)).
The reduced denominator b of t' is at most 2a<=3r for all sufficiently large M, since A is about 1.067. The parameter t' is in [2/5,3/5]. This use of h only in the rational height, not in the denominator of the exponent, is the new joint-coordinate resource.

## 2. Uniform rational exponential separation across a growing frequency range
Use IL's positive-integral construction for t'=a'/b in [2/5,3/5], f_n(x)=x^n(a'-bx)^n/n!, and J_n=U_n exp(t')-V_n with integers U_n,V_n:
(b/100)^n/(5 n!) <= J_n <= e(e b/(4n))^n,
|U_n| <= (n+1)2^n b^n (2n)^n.
Whenever J_n<1/(2d), U_n !=0; the two integer cases give |exp(t')-v/d| >= min(1/(2d),J_n)/|U_n|.

For theorem 1 choose beta with 2kappa/(1-theta)<beta<1-2kappa, and H=floor(M^kappa). Choose a fixed small nu>0 so 2(kappa+nu)/(1-theta)<beta. Set n=ceil((kappa+nu)L/(1-theta)). Uniformly for h<=H, log d<=kappa log M+O(log log M), b<=3c(log M)^theta, and n log(n/b)>=(kappa+nu+o(1))log M. Hence J_n<1/(2d) eventually. The two inverse error bounds obey
log(2d|U_n|) <= [kappa+(kappa+nu)(1+theta)/(1-theta)+o(1)] log M,
log(|U_n|/J_n) <= 2n log n+O(n+log(n+1)) <= [2(kappa+nu)/(1-theta)+o(1)] log M.
Both are <beta log M eventually. Consequently uniformly over these frequencies and all the rational v/d arising above,
|exp(t')-v/d| >= M^(-beta).
For theorem 2 take H=floor(exp(L/10)), n=floor(L/4), beta=2/3. Then b<=3L/100, n>=L/5, e b/(4n)<1/4 (even e<3 suffices). Therefore J_n<=e 4^(-n)<1/(2d), since log d<=L/10+O(log log M) and log 4/5>1/10. Also log(2d|U_n|)<=(1/2+o(1))log M and log(|U_n|/J_n)<=(1/2+o(1))log M. The same separation >=M^(-beta) follows. All asymptotic constants and starting bounds in this section are not numerically optimized.

## 3. Split by actual curvature, not by independent frequency worst cases
For either theorem, put c_* >0 small enough in terms of C_3, fixed independently of M,h. In the small-curvature case |delta|<=c_* M^(-1-beta), the preceding comparison yields
||hrB|| >= c_4 hr M^(-beta) for all 1<=h<=H,
with c_4>0 fixed; this also holds in the outside-neighborhood case of section 1. Choose c_*<=c_4/4. One may first take c_4=1/(2C_3) after enlarging C_3 to cover that case, then choose c_*<=min(1/(4C_3),c_4/4). On each residue class n=u+rj, the rational quadratic h a n²/r is constant modulo 1. The derivative of the remaining phase h delta(u+rj)²+h B(u+rj), with respect to j, is hrB+2hr delta n, at circular distance at least (c_4/2)hr M^(-beta) from the integers throughout 1<=n<=M, and monotone. By the first derivative estimate used in frozen IL (Kusmin–Landau), the sum along each residue over any integer subinterval I is O(M^beta/(hr)). Summing r residue classes gives |S_h(I)|=O(M^beta/h). Constants uniform in I.

In the complementary case |delta|>c_* M^(-1-beta), the second derivative in j has absolute value 2h r²|delta|. Apply IL's standard second derivative estimate on each progression of length at most M/r+1, obtaining
|S_h(I)|/M <= C (r sqrt(h|delta|)+1/(M sqrt(h|delta|)))
<= C (sqrt(hr/M)+M^(-(1-beta)/2)/sqrt(h)).
Here r<=M and |delta|<=1/(rM). The bounds include short progressions, since the standard second derivative estimate includes the reciprocal square-root term; no assumption of a full residue block is needed. This second branch does not need detuning. A zero delta is in the first branch.

Erdos–Turan in its ordinary interval-count form, already used by IP, bounds E_M/M by O(1/H + sum_{h<=H}|S_h(I)|/(hM)), uniformly in I and J. In the first branch the sum is O(M^(beta-1)) because sum h^-2 is bounded. In the second branch it is O(sqrt(rH/M)+M^(-(1-beta)/2)), since sum h^-1/2=O(sqrt H), sum h^-3/2=O(1). For theorem 1 beta<1-2kappa and kappa<=1/4 imply both terms are O(M^-kappa) (the first has strict margin since 3kappa<1 and r is polylogarithmic). For theorem 2 the terms decay by a fixed positive power of M, faster than exp(-L/10); H has subpower size. This proves both theorems.

Classical estimates: same first/second derivative bounds and Erdos–Turan as frozen IL/IP, references https://doi.org/10.1016/j.indag.2015.11.009 and https://doi.org/10.1112/S0025579310001580. No new claim of novelty for those inequalities.

## 4. Actual critical exception transfer
For X large put M=floor(s sqrt X+C) (changing the cutoff by O(1) is harmless). IP/IJ/IK give the ideal width W=2Z0/s, N2(X) equal to the sum of the ideal interval counts up to M plus O(1) and a moving-boundary error, and N3(X) bounded by the moving-boundary count plus O(1). Each moving boundary requires ||Q_n-W||<=K/n with fixed K. In each dyadic block of indices, a fixed arc of length <=min(1,2K/2^j) covers the target, so the expected count is O_K(1), and the difference is at most E_M. Summing O(log M) blocks bounds the entire count by O(log M (1+E_M)). Since W M=2Z0 sqrt X+O(1), the same controls the N2 error. Under theorem 1, apply its discrepancy result with kappa' strictly between kappa and the limiting exponent, absorb log M, to obtain N2(X)=2Z0 sqrt X+O(M^(1-kappa)), N3(X)=O(M^(1-kappa)). Equivalently error O(X^(1/2-kappa/2)), along all X satisfying the stated denominator window hypotheses. Under theorem 2 absorb log M into the weaker exponential: both errors O(M exp(-L/20)). Theorems retain IJ and ID author-level dependencies, not formal admission. No explicit finite sign-bracket constants from IJ are newly extracted here.

## 5. Consequence for the remaining all-scale problem
IP already covers scales r>=M^alpha for any fixed alpha>0 (partition into blocks of length <=r), yielding normalized error O_epsilon(M^(-alpha/2+epsilon)) up to log factors. If the next denominator R satisfies R<=M^(2-alpha), IP applied with R>=M gives normalized error O_epsilon(M^(-alpha/2+epsilon)). IQ now also covers r<=c(log M)^theta (any fixed theta<1) by the polynomial error, and r<=L/100 by a faster-than-log error. Thus the unresolved intermediate branch for general all-X power savings must allow preceding r growing beyond each fixed sublinear log power yet subpower in M, and next R approaching/exceeding the M² scale (in exponent), along a putative subsequence with no fixed power saving. This is a necessary localization of difficult scales, not evidence they actually occur. In particular, the large finite partial quotient 254 in IP is not by itself an example of asymptotic small-denominator regime. No claim of recurrence of IQ windows or improved global irrationality measure.

## Validation and next
The new work is a written analytic proof, using IL's verified exact endpoint relation and integral bounds. No new finite true-K enumeration or numerical claim is made. The proof uses exact parameter inequalities; independent review and explicit finite threshold extraction are outstanding.
Next: strengthen the rational-exponential separation for r beyond log M/log log M, or exploit the full F,E,G system in IO to bound the primitive denominator gaps. Alternatively derive an explicit IJ sign-band constant to make the existing sparse correction algorithm effective. Do not repeat previously validated K computations.
