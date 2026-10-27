# D25/SECOND-DIGIT-LIFT — original weighted-216 third-digit middle-tail reflection

Date: 2026-10-28 Asia/Hong_Kong. Actual logical Research lane: chatgpt-research-onhour-enterprise-math-20260923. Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

**Classification:** AUTHOR-SIDE / PROVED ORIGINAL-WEIGHTED-SUM TAIL REFLECTION / EXACT FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. No Source-native CLAIM/open/checkpoint/Result, no native H0/B0 run. This is a new exact lemma about the ORIGINAL W third digit, not a recurrence of the previously completed auxiliary Cauchy second-digit proof.

## 1. Original carrier and precise third-digit obligation

Let p=6m+1>3 be prime. Work in the p-local rationals; 216 is a unit. Define the original immutable summand and weighted finite sum

    w_n=(6n+1) binom(2n,n)^2 binom(3n,n) / 216^n,
    W_p=sum_{n=0}^{p-1} w_n.

The target-class frozen scientific LIFT is W_p ≡ p (mod p^3), equivalently the original Delta_p-R_p=0 (mod p) under the accepted first-digit conditions and the already established source-port alignment. This unit does NOT assume the target third digit vanishes.

For 0<=n<p, elementary factorial valuations give the EXACT formula

    v_p(w_n/(6n+1)) = floor(2n/p)+floor(3n/p).

Thus the original sum has four ordered valuation bands: 0<=n<=2m (0); 2m+1<=n<=3m (1); 3m+1<=n<=4m (2); 4m+1<=n<=6m (3). The weight 6n+1 may add valuation, but cannot decrease it. In particular the final band vanishes modulo p^3.

## 2. New per-term reflection (uniform all p≡1 mod 6)

Define the genuinely original weighted middle-tail digit, keeping n and its signed weight,

    tau_{p,r} = w_{4m-r}/p^2 mod p,  0<=r<m,
    Theta_p = sum_{r=0}^{m-1} tau_{p,r} mod p.

Then all denominators below are p-units, and the exact FIELD identity holds for EVERY p=6m+1>3:

    tau_{p,r} =
      3(2r+1) * 216^(2m+r) * ((2m+r)!)^5 /
      [ (4m+1+2r)! * (3r+1)! ]  (mod p).                      (T1)

Consequently, with W_bulk=sum_{n=0}^{3m} w_n,

    W_p ≡ W_bulk + p^2 Theta_p  (mod p^3).                    (T2)

**Proof.** Set a=p-n=2m+1+r, n=4m-r. In this band the central binomial has valuation one, and Lucas reduces the other factor modulo p:

    (1/p) binom(2p-2a,p-a) ≡ -(a-1)!^2/(2a-1)!    (mod p),
    binom(3p-3a,p-a) ≡ binom(2p-3a,p-a)
                    ≡ -(a-1)!(2a-1)!/(3a-p-1)!  (mod p).

For the first formula, divide the numerator factorial by its one p-factor and apply Wilson's reflection (p-k)! ≡ (-1)^k/(k-1)! modulo p. For the second formula, the base-p top digit is 1 and the bottom digit is 0; Lucas selects its bottom-digit binomial. Every remaining factorial index is in [0,p-1]. Squaring the first factor and multiplying the second gives

    binom(2n,n)^2 binom(3n,n)/p^2
      ≡ -(a-1)!^5 / ((2a-1)!(3a-p-1)!)  (mod p).

Fermat gives 216^(-n) ≡ 216^(a-1) (mod p), and 6n+1 ≡ 1-6a ≡ -3(2r+1) (mod p). Substituting a=2m+1+r yields (T1). The four valuation bands then give (T2). QED.

For an independent O(m) exact certificate, adjacent digits satisfy

    tau_{p,r+1}/tau_{p,r} =
     216(2r+3)(2m+r+1)^5 /
     [(2r+1)(4m+2+2r)(4m+3+2r)
      (3r+2)(3r+3)(3r+4)]  (mod p),  r<m-1.       (T3)

All these denominators are p-units in the stated range, so the recurrence is valid, although the displayed quotient is meant as a multiplication by the unit tau ratio; the script checks it by cross-multiplication in modular arithmetic. This is a closed factorial/recurrence bridge for the original W high-valuation p^2 band, separate from the previously published Gauss-C/tail and frozen signed Clausen Q/R observations.

## 3. Discriminating p=373 certificate and information-loss witness

Here m=62, p^2=139129, p^3=51895117. The executable checks all original weighted terms, retaining their exact n and valuation band:

    W_bulk (n=0..186)            ≡ 14887176 (mod 51895117)
    W_tail (n=187..248)          ≡ 37008314 = 266*139129
    W_discarded (n=249..372)    ≡ 0
    Theta_373                    = 266 (mod 373)
    W_373                        ≡ 373 (mod 51895117)

For the bulk, (W_bulk-373)/139129 ≡ 107 (mod 373); 107+266=373 ≡0 (mod 373). In other words, the original full sum and the bulk-only sum have IDENTICAL readings modulo p^2, but DIFFER at the required p^3 precision by the nonzero original tail 266*p^2. The original frozen Clausen reflected R_373 from the previously proved independent port alignment equals 196, NOT 266: the source operators R and this W-tail are not interchangeable. The strong third-digit cancellation must couple these labeled contributions through a valid identity; dropping the original tail silently changes the observer.

## 4. Verification, provenance and next work

The companion exact executable d25_original216_p3_middle_tail_reflection_guard_20261028.js was executed in this turn with standard BigInt modular arithmetic. It independently uses exact integer binomials on ALL original n<p and the factorial-reflection formula on every r<m, checks the ratio recurrence, valuation bands and full-sum reconstruction, at 23 primes p≡1 mod6 up to 373. It checks the already-known finite target fixtures only as code regression, not as an all-prime proof. Its end status is PASS_D25_ORIGINAL216_P3_MIDDLE_TAIL_REFLECTION. The all-prime (T1)-(T2) proof stands separately from these finite checks.

**BRC observer typing:** carrier (p,n,r,original w_n, p-adic valuations, order/cutoff, sign 6n+1, original Source Delta/R, earlier Gauss C/Q); permitted operations reflection of unit factorials, Lucas reduction, linear truncation and third-digit readout; exact observer W mod p^3. Tail-to-Theta is an exact quotient for this specified observer, NOT a universally sufficient compression for Frobenius operators, future powers or full native Heartbeat X6 dynamics. All original branch, sign, normalization and Source pins are preserved.

**Highest non-substitutable experimental debt:** issue awdawmip/enterprise-math#1559, whose current body asks the lawful native H0/B0 executor to compute the SAME original class at p=373: actual [X]U mod139129, native rank, semilinear Frobenius direction and eta, signed odd Green/Hesse, kappa, Delta_p-R_p, reproducible Source-pinned raw data. This finite W certificate is NOT the native divided-power benchmark or a substitute implementation; the support intake remained OPEN/PENDING_OWNER on this run's read.

**Precise next mathematics:** use the newly explicit Theta_p to find a uniform bulk relation
    (W_bulk-p)/p^2 ≡ -Theta_p (mod p)
in BOTH p≡13,19 (mod24) classes, or exhibit a counterexample. This is exactly the frozen original third digit, not another auxiliary Cauchy conjecture. Preserve the four-port Gauss representation and the original signed cutoff Q/R when transporting between observers. A lawful native execution from #1559 remains the first scientific acceptance priority.

**Control continuation as read this run:** Research lane only (not chatgpt-hourly-enterprise-math-20260921). Historical recovery #6575 reflects ACTIVE session pointer with no Source-authenticated current CLAIM; historical dispatch #6576 failed TimeoutExpired. Direct Site status 2026-10-28 06:03+08:00: research_authority_granted=false, write_relay_enabled=false, active control jobs 5/5. Native control_result does not recognize old GitHub bridge request IDs (CONTROL_REQUEST_NOT_FOUND); no reissue or alternate-identity write was attempted. Source-native session/claim/run: NONE CURRENTLY VERIFIED. Three legacy staging records remain neutral and separate. The GitHub-author checkpoint is not a formal Source publish_checkpoint, and role activity registration remains pending. Frozen scientific pin unchanged.