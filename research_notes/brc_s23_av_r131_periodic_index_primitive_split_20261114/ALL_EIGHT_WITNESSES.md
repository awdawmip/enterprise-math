# R131.3 — All eight three-bit S23 patterns have explicit certificates in the primitive hard-sweep family

Date: 2026-11-14 (Asia/Shanghai). Same S23 auxiliary observer and frozen science pin as R131.1/2. This theorem sharpens the R131.2 observation: exponential chronological event complexity can coexist with *constant-many closed-form witnesses* for the complete word-set.

For every integer K>=3, set x=0, A=K, d=1, E=1, m=3, I=(0,1). For i=0,1,2 define

`S_i(theta)=1[{(K+i)theta}<{theta}]`.

**Theorem.** Every word in `{0,1}^3` is attained on I, and the following rational phase witnesses are valid simultaneously for every K>=3:

| Word | Rational witness theta |
|---|---|
| 000 | 1/(2K) |
| 001 | 1/(K+2) |
| 010 | 1/(K+1) |
| 011 | 1-2/(2K-1) |
| 100 | 1/K |
| 101 | 1-1/K |
| 110 | 1-1/(K+1) |
| 111 | 1-1/(K+2) |

All entries lie strictly inside (0,1) for K>=3. This is an *exact complete set of certificates* for length-three word membership, independent of how large the primitive slope K becomes. It complements R131.2, which proves at least K-1 *genuine chronological bit transitions* on the same input family.

**Proof.** At theta=1/(2K), the fractional phase `{K theta}=1/2` and for i=1,2 the fractions are `1/2+i/(2K) <1`; all three exceed theta and the word is 000.

For theta=1/(K+r), r=1 or 2, the r-th phase is exactly integral and gives bit 1. For i<r, the fractional part is `(K+i)/(K+r)>=1/(K+r)=theta`; for i>r the fractional part is `(i-r)/(K+r)>=theta`. Hence theta=1/(K+1) gives 010 and theta=1/(K+2) gives 001. At theta=1/K, only i=0 is integral; the other two fractional parts are i/K>=theta, giving 100.

For theta=1-1/(K+r), r=0,1,2, every i<=r has phase fractional part `(r-i)/(K+r)<theta`, and thus bit 1. For i>r, the fractional part is `1-(i-r)/(K+r)`, which is strictly below theta exactly when i-r>1. The corresponding three words are respectively 101, 110, 111.

Finally, let D=2K-1 and theta=1-2/D. For i=0 the fractional part of `(K+i)theta` is `1-1/D>theta`, giving bit 0. For i=1 it is `1-3/D<theta`. For i=2 and D>5 it is `1-5/D<theta`; at K=3 (D=5) the phase is integral, so it remains below theta. Hence the last pattern is 011. The eight exhaustive binary signatures now have explicit witnesses, proving the theorem. QED.

**Bit complexity of this particular membership construction.** The eight witness fractions have numerators and denominators of O(log K) bits and can be constructed with a bounded number of integer arithmetic operations. The guarantee concerns this explicitly specified family and length m=3; it is not a polynomial algorithm for every S23 input.

**Verification.** `check_r131_all_words.py` imported the same independently direct `word` evaluator from the published `check_r131.py`. Exhaustive check of all 8 rational certificates for every K=3,4,...,1023: 1,021 values of K, 8,168 exact Fraction comparisons, zero mismatches; output `R131_ALL_EIGHT_WITNESSES_PASS`.

**Next:** seek parameterized closed-form word certificates for growing m or nonzero rational offset x, and compare their arithmetic cost against R126/R127 exact fixed-dimensional feasibility and R130's explicit event-index construction. Every candidate must preserve strict endpoints and actual observation scope.
