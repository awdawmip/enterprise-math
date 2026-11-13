# R131.4 — Uniform 2m+2 closed-form words in a primitive S23 family

2026-11-14 (Asia/Shanghai); extension of R131.3, same frozen S23 auxiliary scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Statement

Fix any integers `m>=3` and `K>=m`, rational parameter `theta in (0,1)`, and the correlated observer

`S_i(theta)=1[ {(K+i)theta} < {theta} ]`, for `i=0,...,m-1`.

This is the x=0, A=K, d=1, E=1 subfamily; gcd(K,1,1)=1.

**Theorem R131.4.** For every m>=3 and every K>=m, at least `2m+2` pairwise distinct length-m words are attained in `(0,1)`. They are the all-zero word, the all-one word, all m single-one words, and all m single-zero words. Each has a rational phase certificate expressible using a bounded number of integer operations on `m,K`:

1. `0^m` at `theta=1/(2K)`.
2. For each `r in {0,...,m-1}`, one-hot word `e_r` at `theta=1/(K+r)`.
3. For each `z in {1,...,m-1}`, all-ones except coordinate z at `theta=1-1/(K+z-1)`.
4. All-ones except coordinate 0 at `theta=1-2/(2K-1)`.
5. `1^m` at `theta=1-1/(K+m-1)`.

The displayed words are distinct for m>=3, so `|{S(theta):0<theta<1}| >= 2m+2`. Their certificates have `O(log(K+m))`-bit numerators and denominators.

## Proof

All phases are strictly between zero and one under K>=m>=3.

At `1/(2K)`, each unwrapped fractional part `(K+i)/(2K)=1/2+i/(2K)` lies in `[1/2,1)`; it is greater than theta, so every bit is zero.

Fix `r<m` and `theta=1/(K+r)`. For i=r the numerator K+i equals the denominator, giving fractional part zero and bit one. For i<r the unwrapped fraction `(K+i)/(K+r)` is at least theta and strictly below one. For i>r the fractional part after one wrap is `(i-r)/(K+r)`, at least theta and below one because i-r<=m-1<K+r. This gives precisely `e_r`.

Next let `theta=1-1/(K+r)` for `r in {0,...,m-1}`. If i<=r, the fractional part of `(K+i)theta` equals `(r-i)/(K+r)`, which is strictly below theta (including zero when i=r). If i>r, its fractional part is `1-(i-r)/(K+r)` since 1<=i-r<=m-1<K+r. It is smaller than theta exactly when i-r>1. Thus for r<=m-2 the word is all ones except the *single* zero at i=r+1, while r=m-1 gives the all-one word.

For the one remaining zero at index 0, set `D=2K-1` and `theta=1-2/D`. Then
`(K+i)theta=K+i-1-(2i+1)/D`.
At i=0 its fractional part is `1-1/D>theta`, giving zero. For every i>=1 up to m-1, `3<=2i+1<=2m-1<=D`. When `2i+1<D`, the fractional part is `1-(2i+1)/D<theta`; when equality holds, the phase is integral and the fractional part is zero, still less than theta. Hence all later bits equal one.

This constructs exactly the claimed pairwise distinct patterns. QED.

## Verification

`check_r131_linear_family.py` applies the direct exact `word` evaluator from `check_r131.py`, for every m from 3 through 34 and five tested K per m: `m,m+1,2m,10m,10^80+m`. It checks that every generated witness lies in (0,1), the asserted set has exactly `2m+2` unique words and each evaluates to its designated pattern. All `6,240` exact Fraction comparisons pass, returning `R131_LINEAR_CERTIFICATE_FAMILY_PASS`.

This proves a growing-m positive construction with tiny certificates in a primitive family whose chronological event count can still be huge. It does not determine the *total* number of realizable length-m words; direct finite enumeration for m=4, K>=4 has 14 words, exceeding the lower bound 10. A sharper complete classification and coefficient-independent existence solver are useful next questions.
