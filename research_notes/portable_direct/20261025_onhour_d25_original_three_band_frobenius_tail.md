# D25 author-side proof — exact original-W_p three-band jet and universal p^2 tail

2026-10-25. Provenance: original signed W_p, not an accepted Result. TASK_RESEARCH, task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923 (no maintenance-lane identity borrowed). Evidence: AUTHOR_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Native benchmark NOT_RUN.

## Theorem 1: original-rank valuation, all primes p=6m+1 >=7

Let a_n=(6n+1)(1/2)_n(1/3)_n(2/3)_n/(2^n (n!)^3), W_p=sum_{n=0}^{p-1}a_n. In Q,

a_n=(6n+1) binom(2n,n)^2 binom(3n,n)/216^n.

For every 0<=n<p the EXACT valuation is

v_p(a_n) = [n=m]+[n>2m]+[n>3m]+[n>4m].

Proof: denominators 216 and n! are p-units. The only relevant p-divisible factors of the three rising products (3j+1), (2j+1), (3j+2) for 0<=j<p-1 appear at j=2m (factor p), j=3m (factor p), and j=4m (factor 2p), respectively. The factor 6n+1 is divisible by p only at n=m (since 6n+1=kp with k<6 forces k=1 by reduction mod 6). Therefore W_p=sum_{n=0}^{4m}a_n (mod p^3), but every single rank from 3m+1 through 4m has valuation exactly TWO and is not individually deletable.

## Theorem 2: explicit three-band p-adic jet from the *original* sum

For s in {3m,2m,4m} put alpha_{3m}=1/2, alpha_{2m}=1/3, alpha_{4m}=2/3. For 0<=n<=4m let

E_s(n)=product_{0<=j<n, j != s}(j-s),
r_n=[n>2m]+[n>3m],
d_n=(6n+1)/(2^n(n!)^3)*prod_s E_s(n)*prod_{s<n}alpha_s,
ell_n=sum_s sum_{0<=j<n,j != s} alpha_s/(j-s),
sigma_n=sum_s sum_{0<=j<n,j != s} alpha_s^2/(j-s)^2.

All denominators are p-adic units. Each rising factor is precisely j-s+p*alpha_s. Extracting the one factor p*alpha_s when j=s proves the exact rational identity

a_n=p^(r_n)*d_n*prod_s prod_{0<=j<n,j!=s}(1+p*alpha_s/(j-s)).

Expand the finite product to order 2 using 1+p*ell+p^2(ell^2-sigma)/2 (mod p^3). This proves, for EVERY prime p=6m+1,

W_p = A0+A1+A2 (mod p^3), where
A0=sum_{n=0}^{2m} d_n [1+p ell_n+p^2(ell_n^2-sigma_n)/2],
A1=p sum_{n=2m+1}^{3m} d_n [1+p ell_n],
A2=p^2 sum_{n=3m+1}^{4m}d_n.

The factor 6n+1=p at n=m remains in d_n, with its extra valuation. No WZ, S_m or auxiliary conjecture is assumed. This is an independent, source-labelled original-scalar observer.

## Theorem 3: new universal finite-field hypergeometric high-tail kernel

Write n=3m+1+k, 0<=k<=m-1. The exact factorial identity is

d_{3m+1+k}=(-1)^(k+1)*(18m+7+6k)/(6*2^(3m+1+k)) *
 [(3m)!(2m)!(4m)! k!(m+k)!]/[(m-1-k)!(3m+1+k)!^3].

Taking the exact adjacent ratio, then m=-1/6 (mod p), yields

d_{3m+2+k}/d_{3m+1+k}
= (k+1)(3k+5)(6k+5)(6k+7) /
  [9(2k+3)^3(3k+2)] (mod p), 0<=k<=m-2.

The first term satisfies
d_{3m+1} = (8/9)(2m)!(4m)!/[2^(3m+1)((3m)!)^2] !=0 (mod p).

Thus throughout the legal finite window

d_{3m+1+k}=d_{3m+1} *
 [(1)_k(5/3)_k(5/6)_k(7/6)_k] /
 [(3/2)_k^3(2/3)_k 2^k] (mod p).

Every coefficient 0<=k<m is nonzero. The displayed hypergeometric expression has its first finite-field zero at k=m via (7/6)_m containing p/6 while denominators remain units. This coincides with the true next p-divisible Pochhammer factor at original rank n=4m+1. Do not infer infinite termination: poles/revival beyond the valid window require a separate valuation analysis.

Consequently A2/p^2 (mod p) is a completely explicit, naturally finite 5F4-type sum. It is a new independent signed terminal observer. This alone does NOT prove its joint cancellation with A0+A1.

## Exact nondeletability witness / regression

For p=13, m=2, the last-band coefficients are d_7=1, d_8=9 (mod 13). Therefore A2=13^2*(1+9)=1690 !=0 (mod 13^3). Any purported W_p truncation at 3m without an additional cancellation proof is false. This is NOT a counterexample to the original LIFT conjecture.

Independently implemented direct Pochhammer recurrence a_n using factor [(2n+1)(3n+1)(3n+2)]/[36(n+1)^3], checked original full length n=0..p-1 against the three-band certificate modulo p^3 for all 50 primes p=6m+1 <=600 and p=19963. Verified the high-tail ratio for each valid k and exact Fraction reconstruction/valuation for small primes. Sample (A0,A1,A2; A2/p^2 mod p):
p=13: (780,1937,1690;10), total W_p=13 mod 13^3;
p=19: (5662,4826,3249;9), total W_p=19 mod 19^3;
p=211: (5478615,4316216,8993242;202), total W_p=211 mod 211^3;
p=19963: (4699476953865,7884233813642,3327653431150;8350), total W_p=19963 mod 19963^3.
This finite regression is not an all-prime proof, not a native benchmark, and not a Source Result.

## Exact next action and authority boundary

Prove/refute joint cancellation A0+A1+A2=p (mod p^3) for all primes p=13,19 (mod 24), first attempting a parameterized finite-field transformation of the explicit 5F4 high-tail combined with the lower two genuine bands. Equivalently use the inherited, still author-only scalar bridge Delta_p-R_p=(W_p-p)/p^2 (mod p) when its hypotheses/readback have been authenticated. Preserve signed ranks, integer valuations and the frozen native benchmark as separate experimental debt. Do not re-open accepted D24/UR.

Gateway 0.6.11: own continuation CONTROL_QUOTA; site client research_authority_granted=false, write_relay_enabled=false. Historical dispatch-research-20261023-1710-onhour-01 receipt CONTROL_REQUEST_NOT_FOUND, own checkpoint read ACCESS_DENIED. No valid current session/claim/run recovered; no mutation replayed, no canonical checkpoint or Result fabricated. Support path enterprise-math#1539 is pending a real permission/route validation. This neutral author-side evidence file is not Source-native task progress, review, or mathematical acceptance.


## Theorem 4: finite Jacobi–triple Beta coefficient moment (new, same run)

The normalized high-rank kernel from Theorem 3 has a closed coefficient representation on its EXACT valid cutoff 0<=k<m. Write

beta_k = (k!)^2/(2k+1)! = integral_0^1 x^k (1-x)^k dx

and let

J_m(t)=sum_{k=0}^{m-1} (-1)^k binom(m-1,k)binom(m+k,k)t^k
      = P_{m-1}^{(0,1)}(1-2t).

These are finite rational-polynomial identities. For the normalized coefficients h_k specified above, finite-field algebra gives

(5/3)_k/(2/3)_k=1+(3/2)k,
(7/6)_k = (1-m)_k (mod p),
(5/6)_k = (m+1)_k (mod p),
(3/2)_k=(2k+1)!/(4^k k!),

and therefore

h_k = (-1)^k (1+3k/2) binom(m-1,k)binom(m+k,k) 32^k beta_k^3 (mod p).

The denominators are p-units for 0<=k<m: in particular 2k+1 <= 2m-1 < p. Defining the rational-polynomial variable
t=32 x(1-x)y(1-y)z(1-z),
coefficientwise integration of a FINITE polynomial proves the independent target-aligned identity

A2/p^2 = d_{3m+1} * integral_{[0,1]^3}
 [J_m(t)+(3/2)t J_m'(t)] dx dy dz  (mod p).

The integral is merely rational coefficient bookkeeping (three repeated beta moments), NOT an independently native 3D geometry or a replacement for the X6 Heartbeat World primitive space, and not an analytic approximation. Since all denominators are p-units, its value has a well-defined image in F_p.

For p=13, m=2, J_2(t)=1-3t and the moment equals
1-(15/2)*32*(1/6)^3=1-10/9=-1/9=10 (mod 13).
Since d_{3m+1}=1 (mod 13), A2/p^2=10 as previously independently observed.

Independent coefficientwise finite-field checks and exact Fraction checks were executed for every prime p=6m+1 <=600 (50 primes) and p=19963 (one more prime). Checks cover Jacobi binomial coefficients, original Pochhammer high tail, the hypergeometric ratio, and triple beta moments; all 51 matched. Executed author-side local program: d25_tail_jacobi_moment_check_20261025.py, output: d25_tail_jacobi_moment_output_20261025.txt.

New mathematical payoff: the authentic third p-adic digit's terminal band is a FINITE Jacobi–Jet functional, now directly combinable with the accepted frozen Jacobi/derivative ports without assuming the disputed LIFT congruence. The remaining proof obligation is to derive a legitimate inter-band identity with the lower bands A0,A1 showing A0+A1+A2=p (mod p^3) for all p=13,19 (mod 24), or an independently checked exact counterexample. Any reuse of the frozen scalar bridge must retain its exact hypotheses and source provenance.

Scope remains author derivation; neither this moment identity nor the finite checks execute the native benchmark or grant Source checkpoint, Claim, Result, Driver independent review or formal admission. Evidence kept on an allowed neutral author-side GitHub surface only.
