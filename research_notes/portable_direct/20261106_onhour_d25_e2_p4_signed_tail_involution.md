# D25: p^4 signed tail-port theorem for E.2 and original-216

Date: 2026-11-06. Author-side, PROVED (finite factorial reflection), independently FINITE-VERIFIED, UNREVIEWED / NOT_ADMITTED. Logical research lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance lane). Task TP2-B6F4FC938FF94941C1B7; frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Parent and independent scope

Frozen scalar target: W_p = p (mod p^3) for primes p=13,19 (mod 24), where
a_n=(2n)!(3n)!/[216^n(n!)^5], W_p=sum_{0<=n<p}(6n+1)a_n.
The bridge to the established Van Hamme E.2 sum
b_n=(-1)^n[(1/3)_n/n!]^3, V_p=sum_{0<=n<p}(6n+1)b_n
remains an open uniform claim W_p=V_p (mod p^3). Previous 216 three-shell, Franel/E.2 two-jet, and p-integral locality-bound results are consumed without repetition: main commits eec361046d7677ee6b53bf85786af97e616e325d, a953484013a1c1297f006b86a721869fab29f6ef and 96ffdf1472ee4c44fce84c678f433029ff7c0d0c.

## New theorem 1: the FULL E.2 high-index tail vanishes modulo p^4

For EVERY prime p=6m+1>3, define V_low=sum_{n=0}^{2m}(6n+1)b_n. Then

**V_p = V_low (mod p^4).**

Proof. Since 1/3=-2m+p/3, for each 2m<n<p the factor j=2m of (1/3)_n is p/3, and all other factors are p-units. Writing D(n)=n(n-1)...(n-2m), direct extraction of this unique p factor gives

b_n/p^3 = (-1)^n * [(2m)!(n-2m-1)!]^3 / [27(n!)^3]
        = (-1)^n ((2m)!)^3 / [27 D(n)^3] (mod p).

All denominators are p-units. Pair n with n'=8m+1-n. This fixed-point-free involution preserves the interval 2m+1<=n<=6m. Modulo p, n'=2m-n, so D(n')=-D(n), because D contains 2m+1 consecutive factors. Also (-1)^n'=-(-1)^n. Hence b_n'/p^3=b_n/p^3 (mod p). Their weights satisfy (6n+1)+(6n'+1)=8p. Thus each weighted pair cancels modulo p, and the entire tail is zero modulo p^4. QED.

Notice that individual E.2 tail coefficients have exact p-valuation 3; this is a SIGNED PAIR cancellation, not an assertion that each term vanishes modulo p^4.

## New theorem 2: explicit original-216 third-shell coefficient

For EVERY prime p=6m+1>3 and 4m<n<p, put

A3(n)= (-1)^m (2m)!(3m)!(4m)! (n-2m-1)!(n-3m-1)!(n-4m-1)! / [9 * 2^n * (n!)^3].

Then a_n/p^3 = A3(n) (mod p), and the original upper-shell contribution is exactly

U_p = sum_{n=4m+1}^{6m} (6n+1) A3(n) (mod p),
sum_{n=4m+1}^{p-1}(6n+1)a_n = p^3 U_p (mod p^4).

Proof. Substitute 1/2=-3m+p/2, 1/3=-2m+p/3, 2/3=-4m+2p/3 into
a_n=(1/2)_n(1/3)_n(2/3)_n/[2^n(n!)^3].
For n>4m there is precisely one zero-mod-p factor in each Pochhammer symbol (at j=3m,2m,4m). Their normalized product is (1/2)(1/3)(2/3)=1/9. Removing these three factors gives sign (-1)^(3m+2m+4m)=(-1)^m and the six factorials in A3(n). All denominators are p-units. QED.

This theorem identifies a nontrivial original216 p^3 port even though E.2's entire high tail cancels. The n>=4m+1 shell was correctly omitted for the p^3 target; at the next precision it must be retained.

## Independent exact validation (not universal proof of W_p=V_p)

Standard-library checker d25_e2_p4_tail_ports_20261106.py uses two independent routes:
(1) direct original and E.2 modular hypergeometric recurrences in Z/p^4, and
(2) the two normalized closed-factorial tail formulas in F_p.
Every one of the 148 primes 7<=p<=1999, p=1 (mod 6) was checked, including 77 target primes. Both closed-form tail sums matched the actual p^4 recurrence; all E.2 high-tail sums were zero modulo p; W_p=V_p modulo p^3 was independently observed for 148/148 primes. The last observation remains finite evidence only.

Representative columns below are U_p, E.2 normalized high tail, and delta_p=(W_p-V_p)/p^3 mod p, respectively:
- p=13: 5, 0, 10; W_p mod p^4=19786, V_p mod p^4=26377.
- p=19: 4, 0, 13; W_p mod p^4=82327, V_p mod p^4=123481.
- p=67: 31, 0, 10; W_p mod p^4=16542032, V_p mod p^4=13534402.
- p=373: 278, 0, 170; W_p mod p^4=11832087049, V_p mod p^4=3009917159.

Explicit witness at p=19: W_19-V_19=-41154=-6*19^3, so delta_19=13 (mod 19). Therefore a hypothetical uniform W=V (mod p^4) on the frozen target classes is FALSE. The mod-p^3 bridge remains the precise target, while any p^4 lift needs a genuinely nonzero signed boundary. Of 148 primes checked, p=7 alone has delta=0; no inference about all primes is drawn.

## BRC / typed observable resolution

COMPOSE_APPLIED: carrier (family label 216/E2, n, prime, valuation shell, signed p-unit, cutoff), observable (weighted shell sum mod p^4). For E.2, the involution preserves the normalized unweighted coefficient but negates the weight; summation gives zero while individual ports do not. For original216, the third shell is independently identified by A3(n). A total-only quotient would hide this contrast. This arithmetic carrier makes no claim about the native X6 physical observer.

## Durable next action / unchanged experimental debt

Minimal unfinished scalar unit: a NONLOCAL or signed-boundary finite adjoint/WZ certificate proving W_p-V_p=0 (mod p^3) uniformly for p=13,19 (mod24), consuming the earlier full three-shell and E.2 Franel two-jet. The present tail involution is a proved precision-boundary lemma, not that certificate. The strict p^4 witness p=19, and p=373 signed shell U_373=278, are discriminating tests for any proposed transform.

Native fixed p373 original H0/B0 divided-power [X]U mod139129, Frobenius direction/eta, rank, odd signed Hesse/Green, kappa/Delta-R and independent replica remain NOT_EXECUTED / PENDING_OWNER under issue #1559; do not substitute portable arithmetic. The native Research source last reported (prior author's snapshot) research_authority_granted=false; last verified client checkpoint revision 22. Pending original target_request_id: onhour11-20261106-1400-exact-research-lane-continuation (last observed QUEUED after reconciliation); second read request onhour12-20261106-1957-read-continuation (last observed QUEUED). No fresh authoritative status receipt or legitimate session/claim/run was obtained in this author-side unit; do not infer ownership, reissue requests or import three old staging items. Exact current Source receipt/recovery_status must be read before any role-bound continuation.

Evidence status: SOURCE SCIENTIFIC PIN UNCHANGED; AUTHOR-SIDE GITHUB MATERIAL ONLY; REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.
