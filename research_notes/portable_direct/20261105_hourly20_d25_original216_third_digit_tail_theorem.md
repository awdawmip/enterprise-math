# D25 — Original-216 Clausen high tail: next p-adic digit and source channels

Date: 2026-11-05. TASK_RESEARCH author-side portable research; UNREVIEWED / NOT_ADMITTED.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication TP2-B6F4FC938FF94941C1B7; frozen science input c47e13e4aba0e006366f989d6334d443f6333ae3.
Previous theorem/erratum: 20261105_hourly20_d25_original216_quadratic_tail_jets_erratum.md (do not recredit).

## Theorem: one further p-adic digit (mod p^4)

Let p=6m+1 >=7 be prime and b_k=(1/6)_k (1/3)_k / ((k!)^2 2^k), 0<=k<p. The fractions are p-integral. For any polynomial P in Z_(p)[X], let the **ordered** upper convolution strip be

    T_P=sum_{0<=a,b<p; a+b>=p} P(a+b)b_a b_b.

The established valuations are v_p(b_k)=0 for 0<=k<=m, 1 for m<k<=2m, 2 for 2m<k<p. In particular p^2 divides T_P. Define:

    L_i=b_i mod p^2                           (1<=i<=m),
    E_i=b_i/p mod p                           (m<i<=2m),
    D_r=b_(p-r)/p^2 mod p^2                 (1<=r<=2m).

The exact new identity is

    T_P/p^2 =
        2 sum_{i=1}^m L_i sum_{r=1}^i D_r [P(i-r)+pP'(i-r)]
      + 2p sum_{i=m+1}^{2m} E_i sum_{r=1}^i (D_r mod p) P(i-r)
      (mod p^2).                                                   (1)

**Proof.** A pair in a+b>=p has valuation below four only if it has indices (i,p-r) or the reversed pair with 1<=r<=i and 1<=i<=2m. For i<=m the product valuation is exactly two (low/high); for m<i<=2m it is three (middle/high). Low/low, low/middle and middle/middle cannot reach a+b>=p. High/high has valuation >=4 and vanishes modulo p^4. Divide the contributing products by p^2 and use the declared unit precisions. In the low/high channel, a+b=p+i-r, so the integral polynomial Taylor identity P(p+x)=P(x)+pP'(x) mod p^2 supplies the required p-shift. In the middle/high channel the extra factor p allows P(p+x) to be evaluated mod p. Pair symmetry supplies the factor two. QED.

For moments P(X)=X^j, j=0,1,2, introduce retained prefix moments M_s(i)=sum_{r<=i}r^s D_r mod p^2. In the low/high channel the inner expressions are

    S0=M0,
    S1=iM0-M1+pM0,
    S2=i^2 M0-2iM1+M2+2p(iM0-M1).

The middle/high channel uses the same expressions without p terms and reduced modulo p. This computes the triple (T0,T1,T2)/p^2 mod p^2 using O(p) modular operations and O(1) auxiliary registers. D1 can be initialized from b_(p-1) mod p^4 via an O(p), constant-storage forward pass; D_(r+1)/D_r = 36(p-r)^2/[(6(p-r)-5)(3(p-r)-2)] mod p^2 for r<2m, with p-unit denominators. A second forward pass produces L_i and E_i while the reversed coefficients and prefix moments are generated simultaneously. Bit-complexity and the original native crystalline experiment are not included in this algebraic-operation count.

Reducing (1) mod p recovers the previously proved second-digit formula, but discards two genuinely necessary next-digit contributions: the middle/high valuation-three channel and the Taylor p-shift in the low/high channel.

## Independent exact certificates

A stand-alone Python checker computes the complete ordered convolution mod p^4 independently from the O(p) prefix formula, over all 35 primes p<=373 with p=1 mod6. For j=0,1,2 the result is PASS 35/35, including p=373. Independent rational Fraction computation of the weighted sum confirms p=7,13,19.

At p=373:

    (T0,T1,T2)/p^2 mod 373^2 = (13187,124717,107605)
    low/high = (55336,107932,3911)
    middle/high = (96980,16785,103694)
    T_(1+6X)/p^2 = 65844 = 196 + 176*373 (mod 373^2).

Thus the earlier observed 196 digit is conserved; the **new** next digit is 176.

At p=13:

    (T0,T1,T2)/p^2 mod 13^2 = (84,116,77);
    T_(1+6X)/p^2 = 104 = 8*13 (mod 169),
    T_(1+6X) = 17576 mod 13^4.

The previous weighted mod-p observation was zero, yet the true weighted tail has valuation exactly three, not four: an exact residual-fidelity witness across precisions. This is NOT a counterexample to the frozen D24 LIFT/JT2 claim (whose R_p has not been independently identified).

## BRC/observer and scope

BRC_REUSE=COMPOSE_APPLIED: retain ordered-pair multiplicity, source valuations, low/high versus middle/high, the index p-shift, signed weighted combinations, and the allowed 0th–2nd index moments at p^4. Do not collapse to a single mod-p weighted tail before future operations. This is ordinary auxiliary original-216 hypergeometric mathematics, not native original-class H0/B0.

The mother target Delta_p-R_p=0 mod p for p=13,19 mod24 remains OPEN. The exact independent geometric R_p source/normalization and native H0/B0 divided powers, [X]U mod p^2, semilinear Frobenius, eta/kappa and independent review remain unfulfilled. This author-side artifact does not create a native CLAIM/open/checkpoint or mathematical admission, nor replace Source completed_units.

Next exact action: retrieve the frozen independent R_p definition/normalization and compare p=13,19,373; if absent, preserve that exact missing datum. Keep native original-class verification separate. Continue from highest Source checkpoint; preserve old protected session and staging.
