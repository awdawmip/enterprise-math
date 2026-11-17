# R253 — A sharp output-size obstruction for 63 labelled rational masks

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_INTEGER_AND_FRACTION_TESTED / NOT_REVIEWED**. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor: R252 at `e23e0150fc15b9a32df3c8b7cf94a5d9a83a07c9`. This concerns only the auxiliary positive scalar 63-mask observer; it is not a native X6 dynamics or typed BRC EffectHistogram claim.

## Theorem: labelled-output denominators necessarily grow linearly in the event index

For every admissible rational parameter s in (39/100,41/100), let h_{m,k}=W_{popcount(m)} rho_{D_m}^T P_{D_m}^k 1 be exactly the R252 labelled observer, k>=0. The singleton mask m=0 has D_0={0}, W_0=144, a_0=1/5, b_0=13/60. Consequently

`P_{D_0}=[a_0+b_0]=[5/12]` and `h_{0,k}(s)=144 rho_0(s) (5/12)^k`.

Here rho_0(s)>0 is rational. For any fixed admissible rational s its reduced denominator has bit length **k log_2 12 + O_s(1)**. Hence an algorithm outputting all 63 exact **reduced rational** labelled values explicitly must write Omega(k) bits in the worst case, even if its field-operation count is O(log k). This is an **output size**, not an arithmetic complexity impossibility for a compressed representation, modular result or the aggregate-only scalar.

At the exact anchor s=2/5 the frozen seven-state definitions give `rho_0=2079/16424` and `144rho_0=37422/2053`. Thus

```
h_{0,k} = (37422 * 5^k)/(2053 * 12^k)
reduced denominator D_k = 2053 * 2^max(2k-1,0) * 3^max(k-5,0).
```

For k>=5 the **reduced numerator is exactly** `77*5^k` and the denominator is `2053*2^(2k-1)*3^(k-5)`; in particular its bit length is `floor(log2(D_k))+1`. At k=1000 it is **3588 bits** (not counting the positive numerator and separator).

### Proof

The 1-by-1 mask transition is `a_0+(1-a_0)pi_0 = a_0+b_0=5/12`. R252 weights the initial all-ones vector by `144rho_0`, establishing the exact geometric formula. For any fixed rational scalar C=144rho_0>0 in lowest terms, multiplication by 5^k cannot cancel any powers of 2 or 3 in 12^k. The fixed numerator and denominator of C can cancel/add at most constant exponents of 2 and 3. Therefore its reduced denominator contains `2^(2k-O_s(1))3^(k-O_s(1))`; all other residual prime factors are bounded independently of k (those dividing 5 in the denominator eventually cancel). Thus the denominator bit length is `k log2(12)+O_s(1)`.

For s=2/5, use `144rho_0=37422/2053`, `gcd(37422,2053)=1`, `gcd(2053,60)=1`, `v_2(37422)=1`, and `v_3(37422)=5`. Exact cancellation yields the formula for all k>=0 and the reduced numerator 77*5^k for k>=5. Since this singleton is one of the 63 separately requested outputs, the lower bound follows. QED.

## Verification

The standard-library Python program reconstructs t,a,b,pi,rho from the original frozen formulas; it independently iterates the singleton transition for 1001 successive exponents and checks exact fractions at 12 indices. It verifies the reduced denominator formula and two independent prime-field readings for each selected index (24 comparisons, p=1000000007 and p=1000000009). Local execution printed `PASS 12 integer denominators 24 modular crosschecks`. The deterministically generated `R253_verification.json` had local SHA-256 `9780640f1a2170dc8c17e9a0b9137c164777995d444d60542185f8969e457006`. The general theorem rests on the proof, not finite checks; only these exact verification ranges are asserted.

## Complexity interpretation and next research

R252's O(1071 log(k+2)) count refers to rational-field **operations**, not bit cost. An explicit 63-rational-output format has Omega(k) output cost already from m=0. A symbolic/power-expression output such as `(37422/2053)*(5/12)^k`, or fixed-prime modular reduction, avoids this output expansion but answers a distinct representation/observer query. Native signed/provenance/histogram observers are not implied. Next: quantify intermediate rational height for each mask's binary modular reduction, compare compressed factored-output encodings, and experimentally measure exact-output bit and time cost against the 229-order aggregate and direct rank-one propagation. Continue the continuous-parameter 270/403 two-mode threshold problem independently.

No formal CLAIM, Result freeze, independent Review or Foundation promotion is claimed.
