# R284IR — Frequency-resolved gap compensation and enlarged logarithmic denominator window
2026-11-26. Author analytic proof; NOT_REVIEWED. Directed continuation of own R284, no shared task claim or mutation. Original registration r1-20261124-0256-r284gd-session-v1 recovered SUCCEEDED, own Activity RA-B82240E8488EF5A1DA5186C4, Researcher EM-DIRECT-0C386E; session not closed, no runs. Owner inventory r1-20261126-1802-owner-inventory last observed RUNNING before publication. Global entry blobs verified at main@b896b1ccb6b288591ea48958a4876b2173030c23; P000 V4 projection hash matched, Source V5 and joint relation/Heartbeat contracts and ACTIVE worldview consulted. External arithmetic observer, no native spatial attribution.

Frozen input: IQ @cb0d7e4f78985efcd904dac8f7896f69c2e6501e:research_notes/portable_direct/R284IQ_GAP_COMPENSATION_SMALL_REDUCED_DENOMINATORS_20261126.md (endpoint ratio, derivative split and exception transfer); IO @b6d9d4c99b9fcba85c5fca2e9eb83fe763d276cf:research_notes/portable_direct/R284IO_CRITICAL_TRANSCENDENCE_E_FUNCTIONS_20261126.md (A irrational, enclosure); IP @8c838a160e4159db2864ae4dd46c9e59576a9638 and IL/IJ/IK/ID through IQ. Actual minimum interpretation retains ID author-level monotonicity. No formal Result or promotion.

## Results
Write A=1/s0², B=-2C0/s0², Q_n=A n²+B n+C0²/s0², L=log M/log log M. Let a/r be reduced with |delta|=|A-a/r|<=1/(rM), 1<=r<=M; E_M denotes the maximum absolute circular-interval count discrepancy over all integer subintervals of [1,M]. As in IQ, this includes adjacent convergent gaps.

Theorem 1. For fixed 0<=theta<1, c>0 and 0<kappa<(1-theta)/(3-theta), if r<=c(log M)^theta, then E_M=O(M^(1-kappa)), uniformly in the allowed approximants and subintervals. This improves IQ's (1-theta)/(2(2-theta)). At theta=1/2 the limiting exponent improves 1/6 to 1/5; theta=1/3 improves 1/5 to 1/4; theta=2/3 improves 1/8 to 1/7. theta=0 is asymptotically vacuous for irrational A at bounded r.

Theorem 2. For fixed 0<c<4A/e and 0<gamma<(1/2)log(4A/(ec)), if r<=c L, then E_M=O(M exp(-gamma L)). Constants may depend on c,gamma and the actual endpoint pair. For this actual A~1.0670288, 4A/e~1.57015; in particular r<=L permits any gamma< (1/2)log(4A/e) (~0.2256). This extends IQ's r<=L/100 domain. These are asymptotic conditional-on-window results, not recurrence claims or finite starting bounds.

## 1. Frequency-resolved endpoint separation
Use the exact IQ section 1 construction, with h>=1, l nearest hrB, z'=r/a, C'=-l/(2ha), t'=r/(2a) and rational v/d=R(z',C'). In the fixed neighborhood d<=C h r³, reduced denominator b of t' <=2a=O(r), t' in [2/5,3/5], and
|exp(t')-v/d| <= C (|delta|+||hrB||/(hr)).
If outside the neighborhood, the detuning ||hrB||/(hr) already exceeds a fixed positive constant for large M, as in IQ, so only the inside case needs separation. Preserve both the reduced denominator and h rather than paying the maximal frequency in each branch.

Use IQ/IL's positive integral J_n=U_n exp(t')-V_n with integer U_n,V_n:
(b/100)^n/(5 n!) <= J_n <= e(e b/(4n))^n,
|U_n| <= (n+1)2^n b^n (2n)^n.
When J_n<1/(2d), U_n is nonzero (otherwise the nonzero J_n would be an integer). The integer alternatives give separation at least min(1/(2d),J_n)/|U_n|. In particular log(|U_n|/J_n)<=2n log n+O(n+log(n+1)).

For Theorem 1 write p=2/(1-theta), H=floor(M^kappa). Given any fixed small eps>0, choose fixed nu>0 so p nu<eps/2, and for EACH frequency h<=H take
n_h=ceil((log h+nu log M)/((1-theta)log log M)).
Uniformly over h, n_h is between fixed positive multiples of L, so log n_h=log log M-log log log M+O(1); log b<=theta log log M+O(1), log d<=log h+O(log log M). Thus
n_h log(n_h/b)>=log h+nu log M-o(log M),
and J_n<1/(2d) eventually uniformly. Moreover
log(2d|U_n|)<=log h+(1+theta)(log h+nu log M)/(1-theta)+o(log M)
<=p log h+p nu log M+o(log M),
log(|U_n|/J_n)<=p log h+p nu log M+o(log M).
Hence |exp(t')-v/d|>= h^(-p) M^(-eps) uniformly. This is a frequency-resolved lower bound, not the common worst-frequency bound M^(-p kappa-eps) used in IQ.

## 2. Frequency-resolved split and summation
Set T_h=h^(-p) M^(-eps). For each h independently compare |delta| with c_* T_h/M, with a sufficiently small fixed c_*>0. If |delta|<=c_* T_h/M, section 1 implies ||hrB||>=c_1 hr T_h, including the outside-neighborhood case. The phase derivative on a residue class n=u+rj, after dropping the constant rational quadratic phase, is hrB+2hr delta n. Throughout 1<=n<=M it stays at distance >=(c_1/2)hr T_h from integers if c_* is small enough. It is monotone. IQ's first derivative bound gives |S_h(I)|<=C/(h T_h)=C M^eps h^(p-1), after summing the r classes. If |delta|>c_* T_h/M, IQ's second derivative estimate, including short progressions, gives
|S_h(I)|/M <= C (r sqrt(h|delta|)+1/(M sqrt(h|delta|)))
<= C (sqrt(hr/M)+ M^(-(1-eps)/2) h^((p-1)/2)).
In the first branch the normalized bound is the square of V_h=M^(-(1-eps)/2) h^((p-1)/2). Choose eps sufficiently small that (1-eps)>kappa(p+1), possible exactly when kappa<1/(p+1)=(1-theta)/(3-theta). Then V_h<=1 uniformly for h<=H, so both branches admit the same bound C(sqrt(hr/M)+V_h). Summing h^-1 weights via Erdos–Turan yields
E_M/M <= C(1/H+sqrt(rH/M)+M^(-(1-eps)/2) H^((p-1)/2)).
Here p>=2 so the two power sums have the indicated bounds without a log loss. The third term is O(M^-kappa) by the choice of eps, and the second is O(M^-kappa) because 3 kappa<1 and r is polylogarithmic. This proves Theorem 1 uniformly in I and J. Crucially the split may differ by h but uses the same actual delta and B throughout; it does not replace the joint state by independently chosen phases.

## 3. Enlarging the logarithmic denominator region
Retain the actual integration interval instead of using IL's coarse bound x(t'-x)<=1/4. Since a'=b t', the integrand polynomial in J_n is [b x(t'-x)]^n/n!, with maximum at t'/2. Thus
J_n <= e (b t'^2/4)^n/n! <= e (e r/(8 A_- n))^n,
where A_- is any fixed positive number strictly below A and M is sufficiently large so a/r>=A_-; indeed b<=2a gives b t'^2/4<=r²/(8a). The bound uses t'<1, factorial n! >= (n/e)^n. This is the second improvement: a certified upper bound preserving the actual endpoint scale and primitive denominator rather than independently enlarging them.

Given c,gamma as in Theorem 2, choose A_-<A close enough, and tau<1/2 sufficiently close to 1/2, so
gamma<tau log(8 A_- tau/(ec)).
Choose n=floor(tau L), H=floor(exp(gamma L)). Then r<=c L, log d<=gamma L+O(log log M), and log J_n<=-tau log(8 A_- tau/(ec)) L+o(L). Hence J_n<1/(2d) uniformly over h<=H. Both log(2d|U_n|) and log(|U_n|/J_n) <= (2 tau+o(1))log M (use b=O(L), log n<=log log M+O(1)). Choose beta with 2 tau<beta<1; separation >=M^-beta follows. Use IQ's split with common T=M^-beta and first/second derivative estimates. The normalized discrepancy is
O(1/H+M^(beta-1)+sqrt(rH/M)+M^(-(1-beta)/2)).
The last three terms are power-decaying up to subpower factors, hence o(exp(-gamma L)); this proves Theorem 2. No new transcendence theorem or claim of unrestricted polynomial separation is used.

## 4. Transfer to actual critical exception counts
Use frozen IQ section 4 with M=floor(s0 sqrt X+C0), W=2Z0/s0. The ideal interval count error is O(E_M+1); moving-boundary count is O(log(2M)(1+E_M)) by dyadic cover of ||Q_n-W||<=K/n. Apply Theorem 1 with a slightly larger admissible kappa and absorb logs. Thus N2(X)=2Z0 sqrt X+O(X^(1/2-kappa/2)) and N3(X)=O(X^(1/2-kappa/2)) on the corresponding denominator windows. Under Theorem 2 apply with a slightly larger admissible gamma and absorb logs to obtain N2(X)=2Z0 sqrt X+O(M exp(-gamma L)), N3(X)=O(M exp(-gamma L)). ID author-level monotonicity and IJ remainder remain dependencies. Examples: theta=1/2 permits error O_epsilon(X^(2/5+epsilon)); theta=1/3 permits O_epsilon(X^(3/8+epsilon)); theta=2/3 permits O_epsilon(X^(3/7+epsilon)). No repeat true-K enumeration.

## Validation and next
Analytic argument above, reusing exact frozen IQ/IL endpoint relation and integral estimates and the same classical first/second derivative and Erdos–Turan bounds. No new computational evidence is asserted; exponent values follow exact rational algebra. Independent review and explicit finite onset remain pending. The unrestricted all-scale power bound remains open in large primitive denominator gaps. Next: use full IO E-function relation to seek a stronger primitive denominator lower bound, or extract an explicit uniform IJ remainder for certified sparse fallback. The sharpened logarithmic region gives a useful crossover for those investigations.
