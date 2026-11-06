# D25: Reflection of the original 216 valuation-two shell into low-index units

Date: 2026-11-06. Author-side exact algebra; status **PROVED (within stated elementary assumptions) / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED**. No current Source CLAIM/run. Task publication: TP2-B6F4FC938FF94941C1B7; frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Logical research lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded.

## Mother objective and consumed frontiers

For p = 6m+1 > 3 prime, let
a_k = (2k)!(3k)! / [216^k (k!)^5],
W_p = sum_{k=0}^{p-1} (6k+1) a_k.
Frozen target, restricted to p mod 24 in {13,19}: W_p = p (mod p^3), equivalently the previously defined Delta_p-R_p=0 (mod p). The original three-shell decomposition (commit eec361046d7677ee6b53bf85786af97e616e325d) already isolated the valuation-two contribution k=3m+1,...,4m in terms of its q/G recursion. The E.2 comparison remains open; its high-tail p^4 involution (commit f95df526a8f1ae61e37fc5c70974ec0922ff0c0c) is consumed but not replayed. This unit constructs a **termwise opposite-index transport** for the original valuation-two shell, preserving its signed weighted observer.

## Theorem: reverse-shell p-unit transport

For every prime p=6m+1>3, 1 <= j <= m, define k_j=4m+1-j and C_j = a_{k_j}/p^2 in F_p (well-defined since v_p(a_{k_j})=2). Then

(1) C_j = (2k_j-p)! (3k_j-p)! / [216^{k_j} (k_j!)^5] (mod p).

(2) C_1 = (2m-1)! / [216^{4m} ((4m)!)^5] (mod p).

(3) For 1<=j<m,

C_{j+1}/C_j = 4(3j-1)^3 / [3j(6j+1)(3j+1)] (mod p).

Every displayed denominator is a p-unit and each C_j is nonzero in F_p. In particular, the original full weighted valuation-two shell has the **exact second-digit low-index readout**

(4) SUM_{k=3m+1}^{4m} (6k+1) a_k
    = p^2 SUM_{j=1}^{m} (3-6j) C_j   (mod p^3).

This includes the signed weights and all m indices. All equalities (mod p) in the coefficient formulas are interpreted in F_p, and (4) in Z/p^3Z.

### Proof

For 3m+1 <= k <= 4m, p<2k<2p and p<3k<2p, whereas k<p. Thus exactly one p occurs in each of (2k)! and (3k)!, and no p occurs in the denominator; v_p(a_k)=2. For p <= N < 2p,

N!/p = (p-1)! (p+1)...N = -(N-p)! (mod p)

by Wilson's theorem. Apply this twice with N=2k,3k. The two minus signs cancel, giving (1). For k_1=4m, 2k_1-p=2m-1 and 3k_1-p=6m-1=p-2; (p-2)!=1 (mod p), yielding (2).

The exact original-coefficient recurrence is

a_k/a_{k-1} = (2k-1)(3k-2)(3k-1)/(36k^3).

Hence C_{j+1}/C_j=a_{k_j-1}/a_{k_j}=36 k_j^3 / [(2k_j-1)(3k_j-2)(3k_j-1)]. Since 4m+1=(2p+1)/3, modulo p one has k_j=1/3-j. Substitution and cancellation give (3). Its denominators do not vanish since 1<=j<m and 6j+1,3j+1,j<p; numerators also do not vanish because 3j-1 is nonzero mod p. Finally 6k_j+1=4p+3-6j, and index reversal proves (4). QED.

### Exact reconciliation with the earlier three-shell result

In the earlier original-216 q/G notation (same frozen task and coefficients), the previously established three-shell formula expresses this contribution as
 -p^2 a_{2m} q_{m-1} G_0 / 576 (mod p^3).
Consequently, the two independently parametrized **low-index** observers satisfy

SUM_{j=1}^{m} (3-6j) C_j
 = - a_{2m} q_{m-1} G_0 / 576 (mod p).

This is an explicit equality of the *same original valuation-two shell*, not a new proof of the mother target. The coefficient C_j can now be compared termwise with Franel/E.2 low-index jets without moving or dropping the original shell.

## Independent exact integer checks

Reproducer: d25_reflected_shell_check_20261106.py. The modular recurrence for a_k is computed in Z/p^3Z, separately from the factorial-extraction formula for every C_j in F_p. The recurrence in (3), initial value (2), reversed term-by-term coefficient list, and weighted total (4) are checked independently. Actual run: ALL_PASS on all 148 primes 7<=p<=1999 with p=1 mod6 and separately p=5113, total 149 distinct primes and 23,804 exact coefficient comparisons. The numbers are finite checks; the proof above establishes the theorem for all primes in its domain.

- p=7, m=1: C_1=3; signed valuation-two shell/p^2=5 (mod 7).
- p=13, m=2: C_1=10; shell/p^2=10 (mod 13).
- p=19, m=3: C_1=2; shell/p^2=9 (mod 19).
- p=67, m=11: C_1=43; shell/p^2=58 (mod 67).
- p=373, m=62: C_1=181; shell/p^2=266 (mod 373).
- p=5113, m=852: C_1=72; shell/p^2=4671 (mod 5113).

The p=19 shell is 9*19^2 modulo 19^3; p=373 shell is 266*373^2 modulo 373^3. These agree with the original 216 three-shell observations. A new readout has been proved, not a duplicate claim of their previous computation.

## Typed BRC observable and next exact unit

Carrier fields: (p,m,j,k_j, valuation=2, p-unit C_j, signed weight 3-6j, original-216 provenance). The observer is the weighted sum in F_p, then multiplication by p^2 before reading in Z/p^3Z. Index reversal preserves the individual coefficients and their shell membership; a scalar total alone would erase the cross-shell source needed by future adjoint/cancellation operators. This is an external arithmetic auxiliary readout, not native X6 or H0/B0 execution.

Next exact scientific action: incorporate this low-index p^2-shell transport into the **joint original-216 versus E.2 Franel two-jet** difference modulo p^3, looking for a finite nonlocal signed-boundary telescoper that cancels the *whole* W_p-V_p. Retain nonzero p=19,373 signed J and valuation-two ports, and use p=5113 as an additional discriminant. Alternative: seek an explicit counterexample to a proposed universal adjoint kernel before accepting it.

Fixed original-class p=373 H0/B0 divided-power [X]U, native rank, semilinear Frobenius direction/eta, odd signed Green/Hesse, kappa/Delta-R and independent replication remain NOT_EXECUTED / PENDING_OWNER under issue #1559. This local modular program does not supply those observations. Source formal registration/CLAIM/run/Result remain pending; preserve original target_request_id onhour11-20261106-1400-exact-research-lane-continuation and its receipt. Old staging artifacts retain their separate provenance.