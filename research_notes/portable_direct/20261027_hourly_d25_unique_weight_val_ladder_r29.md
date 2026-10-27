# D25/LIFT R29 — Unique S weight-zero valuation ladder; the p≡19 low-half second-digit source

2026-10-27 Asia/Hong_Kong. TASK_RESEARCH logical conversation chatgpt-research-hourly-enterprise-math-20260923, separate from CONTROL_PLANE_MAINTENANCE. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. D25/LIFT/JT2 OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is not a canonical CLAIM, OPEN, Source checkpoint, all-prime W=S proof, native CM experiment, Result, independent Driver review or formalized theorem.

## Consumed sources and exact new question

R23 (half-tail) established the original low-half plus W-high p² reduction. R24–R28 established the distinct W/S weighted ports, Hadamard kernel, PF source intertwiner, endpoint-sensitive finite Green adjoint and, for p≡13 (mod 24), a one-dimensional S weighted-source hole with surviving fourth-digit source. We consume those verified author results without recredit. An externally proved Guo–Zudilin 2019 theorem is an input for S truncations, not for W=S. A missing gap is the valuation of the unique original weight-zero S index in *other* prime classes, especially whether it contributes inside the genuine low-half p² defect.

For p=6m+1 prime p≥7 and 0≤k<p, let two genuinely distinct source-labelled terms in Z_(p) be

    w_k = (6k+1)(2k)!(3k)! / [(k!)^5 216^k]
    s_k = (8k+1)(4k)! / [(k!)^4 2304^k].

The arithmetic carrier retains W/S origin, integer k, exact valuations, normalized unit, and low-half (k≤3m) versus high (3m<k≤4m) observer. These ranks do not represent Enterprise native X6 axes.

## Lemma — Wilson factorial-block units

For integers 0≤b<p and 0≤r<p, Legendre gives v_p((bp+r)!)=b (since bp+r<p²). Removing the actual p factors yields

    (bp+r)!/p^b ≡ (-1)^b b! r!   (mod p).            [1]

Proof: the b completed blocks each have the p−1 unit residues, whose product is −1 by Wilson; their removed multiples are p·1,...,p·b. The remaining r unit residues multiply to r!. This proves the unit statement without illicit division by p inside F_p.

## Theorem — unique S weight-zero source and exact all-residue valuation ladder

Let a be the least positive residue of p modulo 8 (a∈{1,3,5,7}); set

    k* = (ap−1)/8,   q=(a−1)/2,
    q2=floor(2k*/p), q3=floor(3k*/p),
    e=1 if p=7 and e=0 otherwise.

Then k* is the UNIQUE index 0≤k<p at which 8k+1≡0 (mod p), with

    8k*+1=ap,  6k*+1=(3ap+1)/4 ≡ 1/4 (mod p),
    floor(4k*/p)=q=q2+q3.

In particular,

    v_p(w_(k*))=q,    v_p(s_(k*))=q+1+e.           [2]

The exceptional p=7 has 8k*+1=49=p² and v_p(s)=5, versus v_p(w)=3; for every p>7 the S source has exactly one more p factor than its same-index W source. Therefore (w_(k*)−s_(k*))/p^q is nonzero mod p; the two cannot be paired by a valuation-preserving unit-diagonal same-index transfer.

More strongly, put u2=2k*−q2p, u3=3k*−q3p, R=(p−1)/2 (all factorial arguments in [0,p−1]). The exact normalized unit residues satisfy

    w_(k*)/p^q ≡
      (6k*+1)(-1)^q q2!q3!u2!u3! / [(k*!)^5 216^(k*)]    (mod p), [3]

    s_(k*)/p^(q+1+e) ≡
      (a/p^e)(-1)^q q! R! / [(k*!)^4 2304^(k*)]           (mod p). [4]

Here a/p^e is the integer 1 when p=7 and a otherwise. Each displayed normalized residue is a p-unit.

Proof: uniqueness follows from 8 invertible modulo p, and the odd number 8k+1 for 0≤k<p has a multiple ap with odd a∈{1,3,5,7}; ap≡1 mod 8 implies a≡p mod 8 since p²≡1 mod 8. The floor identities follow by substituting k*. Legendre's formula gives the numerator-factorial valuations q2, q3, q; k*! is a p-unit, 6k*+1≡1/4 mod p, and ap has p-valuation 1 except p=a=7, when it has valuation 2. Apply [1] to the three numerator factorials, observing 4k*−qp=(p−1)/2. This proves [2]–[4] and unit nonvanishing. QED.

## New low-half corollary for p≡19 (mod24)

Here a=3, q=1, k3=(3p−1)/8 lies strictly above 2m=(p−1)/3 and at or below 3m=(p−1)/2. Therefore the unique p-divisible S weight occurs *inside the original R23 low-half discrepancy*, rather than the p²-reflected S-mid or W-high interval. Its exact source valuation and second digit are

    v_p(w_(k3))=1,  v_p(s_(k3))=2,
    s_(k3)/p² ≡ −3 ((p−1)/2)! / [(k3!)^4 2304^(k3)] !=0 (mod p). [5]

This provides a previously unisolated S-only second-digit coordinate required by any source-faithful low-half WZ/adjoint certificate in the p≡19 hard-target class. Suppressing s_(k3) because it vanishes modulo p² loses precisely a potentially decisive p³ digit. The same index has a W first-digit unit and must be retained separately.

For p≡13 (mod24), a=5, q=2, k5=(5p−1)/8 occurs in 3m<k≤4m, and [2] recovers (without recredit) R25/R26's W-high/S-mid valuation hole and sign-faithful fourth-digit repair. For p≡1(mod24), q=0,v_s=1; p≡7(mod24), q=3,v_s=4 except p=7 has v_s=5. This is a termwise source classification, *not* a no-go for a nonlocal WZ certificate.

## Executed exact author verification

The adjacent Python 3 standard-library checker independently evaluates true original integer binomial coefficients at k* modulo p^(q+3+e), compares their exact valuations and both independently derived Wilson-unit formulas, and evaluates full original W and S factorial-ratio sums modulo p³ by a second recurrence. **ACTUALLY EXECUTED PASS for all 148 primes 7≤p<2000, p≡1(mod6), including 40 primes p≡13 and 37 p≡19 (mod24).** In this *finite scope only*, W_p=S_p=p mod p³ and the p²-divided low-half discrepancy equals minus W-high U_p. Finite enumeration is not a universal proof; [1]–[5] are general algebraic proofs. No native original-class experiment or independent mathematical review was run.

    p    a   k*  v_w v_s   w_unit s_unit   low/p² high/p²
    7    7    6    3   5        5      6         2       5
    13   5    8    2   3        9      8         3      10
    19   3    7    1   2       13     10        10       9
    43   3   16    1   2       35     28         8      35
    181  5  113    2   3       83     12        29     152
    373  5  233    2   3      234    331       107     266
    733  5  458    2   3        9    405       666      67

**BRC COMPOSE_APPLIED:** this is a source-labelled valuation/observer repair, not a cancellation of positive branch mass or a native X6 theorem. The exact original (series,k) and p-adic unit carry information lost by a modulo-p² projection; the output observable and permitted future operations (low-half summing, factorial reflection, PF/WZ transfer, next-digit lift) determine what may be safely compressed.

## Actual native boundary and next smallest unfinished unit

Current native v0.6.11 status has research_authority_granted=false. Own direct continuation request researchhourly-20261027-0829-continuation-r29 returned INVALID_ARGUMENT / CONTROL_QUOTA, original-request receipt CONTROL_REQUEST_NOT_FOUND. Historical own recovery/continuation was read without any live CLAIM or current authorization, although the old Source checkpoint bytes were verified and predecessor-claim pointers conflict. No session_close, new identity, maintenance-conversation mutation, CLAIM/OPEN, native Source checkpoint, freeze or review was attempted. Existing control support owner is Enterprise Math Issue #1558. GitHub portable artifact and Research-Activity metadata, even when durable, cannot be substituted for native task Source checkpoint. Preserve two neutral staging archives.

**Next exact action:** feed the nonzero p≡19 S low-half unit [5] and p≡13 W-high/S-mid unit [4] into the actual R28 boundary-aware Green adjoint, seeking the p²-divided low-half compensator for the distinct W-high U_p. Retain both series identities, all six original z=2 Hasse J/E channels, finite left/right ports, independent positive-infinity/high/high, native original-class H0/B0, [X]U mod p², semilinear Frobenius η/κ, actual p373 CM experiment, and independent Driver. The mother D25/LIFT/JT2 remains OPEN. This result changes none of P000, the protected ACTIVE worldview or the frozen scientific Source pin, and no scheduler/Actions/cron or notification configurations were modified.
