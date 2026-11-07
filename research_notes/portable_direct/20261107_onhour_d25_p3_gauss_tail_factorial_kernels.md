# D25 — Explicit factorial kernels for p³ Clausen/Euler tail ports

2026-11-07 · TASK_RESEARCH author-side; **exact theorem, finite recurrence verification; UNREVIEWED / NOT_ADMITTED**. Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Stable research lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded.

This is a genuine follow-up to the p³ **projected** Clausen/Euler fold at commit 36b2cab4deb92e75008f244d377359a3de33d547. It converts the normalized high-index source coefficients that drive its Frobenius overflow into direct, universally valid finite-field factorials. It does not replace the native p373 H0/B0 experiment.

## Theorem — explicit sources over F_p

Let p=6m+1>3 be prime and f_n=(1/6)_n(1/3)_n/(n!)². For every integer n with 2m+1≤n≤p-1, f_n/p² belongs to Z_(p) and

    f_n/p² ≡ (-1)^m m!(2m)!(n-m-1)!(n-2m-1)!
             / [18(n!)²]                                   (mod p).    (A)

Let p=8k+3 or 8k+5 be prime and choose Gauss parameters (a,b)=(1/8,3/8) or (5/8,7/8), respectively. Put g_n=(a)_n(b)_n/(n!)². For every integer 3k+2≤n≤p-1,

    g_n/p² ≡ -3 k!(3k+1)!(n-k-1)!(n-3k-2)!
             / [64(n!)²]                                   (mod p).    (B)

Thus the **same B-side normalized factorial kernel** covers both frozen target classes (the 8k+5 case retains its distinct Euler C(z)=1-z multiplier in the projected full sum).

**Proof.** When p=6m+1, the unique numerator factors divisible by p up to index n-1 occur at j=m in (1/6)_n, with value p/6, and j=2m in (1/3)_n, with value p/3. Since 1/6≡-m and 1/3≡-2m mod p, removing those two factors yields respectively (-1)^m m!(n-m-1)!/6 and (2m)!(n-2m-1)!/3. Their product, divided by (n!)², is (A). No denominator factor n! is divisible by p because n<p.

For p=8k+3, (3/8)_{n} has its p-factor at j=k, value p/8, and (1/8)_n at j=3k+1, value 3p/8. For p=8k+5, (5/8)_n has its factor at j=k, value p/8, and (7/8)_n at j=3k+1, value 3p/8. In either case the residue upper parameters are -k and -(3k+1); after removing the two factors their remaining products contribute (-1)^{k+3k+1}=-1, k!, (3k+1)!, (n-k-1)! and (n-3k-2)!. Multiplication by 3/64 and division by (n!)² gives (B). QED.

These formulas also yield non-singular recurrence ratios for the normalized tail (until n=p-1):

    A: r_(n+1)/r_n = (n-m)(n-2m)/(n+1)²      (mod p),
    B: r_(n+1)/r_n = (n-k)(n-3k-1)/(n+1)²    (mod p),

with explicit first coefficient from (A)/(B). This lets the Frobenius overflow port P=Π_p(CQR) be reconstructed directly over F_p using a lower-range Gauss factor Q mod p, without generating the high-index Gauss coefficients modulo p³. The original A/B coefficient sources, index shift, Euler flag, cutoff and operation remain typed and retained.

## Exact executed checks

The companion standard-library script calculates actual g_n and f_n modulo p³ by their original rising-factorial ratio recurrences and independently evaluates the explicit factorial formula modulo p. **Every normalized tail coefficient** was verified for all 178 primes p≤2500 in the A class and all 189 primes p≤2500 in the B classes. No floating point, rational approximation, or assumed CM root enters the proof or check.

|p|number of A tail terms|A first normalized term|number of B tail terms|B first normalized term|
|--:|--:|--:|--:|--:|
|13|8|3|8|9|
|19|12|7|11|18|
|43|28|41|26|6|
|67|44|16|41|13|
|373|248|69|233|342|

The factorial theorem is universal in its stated prime classes. The still-unproved mother target is W_p≡p (mod p³) for p≡13,19 (mod24). The next exact action is to combine (A)/(B) with the previous short Gauss-jet and projected overflow formulas and seek a Fricke/Dwork identity for the residual (G_A-G_B)/p²+E_A-E_B mod p; test a candidate at 13,19,43,67,373 before asserting a uniform proof.

## Native-source / independent benchmark state

Native request onhour11-20261106-1400-exact-research-lane-continuation remains unresolved: last prior evidence QUEUED/EVENT_COLLECTION_IO/Error; 2026-11-07 12:08 UTC em_status and em_control_result reported BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Site was CONFIGURED_NOT_LIVE_VERIFIED with research_authority_granted=false. No duplicate mutation, session/CLAIM/run or native checkpoint asserted. H0/B0 [X]U divided-power, Frobenius, Hesse κ and independent replication for the original p373 class remain open at issue #1559. This author-side proof is not an accepted Source Result.
