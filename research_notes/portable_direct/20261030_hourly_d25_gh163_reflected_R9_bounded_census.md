# D25/LIFT GH-163: bounded exact census of exceptional reflected zero

2026-10-30. **AUTHOR-EXACT-CHECKED / FINITE-CERTIFICATE / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Same Research lane `chatgpt-research-hourly-enterprise-math-20260923` and mother D25/LIFT/JT2 task as GH-161–162. P000 ACTIVE_LOCKED and frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remain unchanged.

GH-162 proved **stationarity** `R'_p(9)=0` for all primes `p>=11, p≡3 (mod8)` in the GH-153 **reflected** polynomial. It did not prove `R_p(9)=0`. This new unit exhaustively measures the distinction over a finite range.

For `p=8m+3`, in F_p let `h_0=1`,
`h_(j+1)=h_j*(4j+3)^3/((4j+4)(4j+5)(4j+6))`, `0<=j<2m`, and

`R_p(9)=sum_(j=0)^(2m) (8j+5)*h_j*9^(2m+1+j)/(2m+1+j)`,

`R'_p(9)=sum_(j=0)^(2m) (8j+5)*h_j*9^(2m+j)`.

All denominators are in `1..p−1` and invertible. The deterministic C++17 program `d25_reflected_R9_prime_scan.cpp` first sieves every prime <=500000, then enumerates all primes `p≡3 mod8` in that interval and evaluates both quantities by exact modular integer operations. Actual compiled execution with `g++ -O2 -std=c++17 -Wall -Wextra` returned exit code zero and this complete nonroutine output:

```
ANCHOR 11 5 0
ANCHOR 19 8 0
ROOT 3347
ANCHOR 3347 0 0
SUMMARY p<=500000 count=10417 stationary=10417 zero=1
```

**Finite-domain certificate:** among the **10,417** primes `11<=p<=500000, p≡3 mod8`, precisely one has `R_p(9)=0`, namely `p=3347`. All 10,417 have `R'_p(9)=0`. The exact scan took 29.99 seconds on the author's runtime. The earlier independent Python finite-field checker re-evaluated 20 designated primes, including the 11,19,3347 anchors. The universal derivative theorem is the separate algebraic GH-161/162 result; this bounded census does **not** establish unique zero over all primes, a density law or the source-original GH-3 sum.

**BRC `COMPOSE_APPLIED`:** retaining merely the stationarity indicator erases the exceptional zero-value event; retaining merely the value-zero indicator erases the general zero derivative. The future operations `read R(9)`, `read R'(9)`, `read root multiplicity` require a typed pair (plus the prior p3347 second derivative `R''=2331` where needed). This is an auxiliary finite-field observer, not a P000 native spatial theorem.

**Next unfinished mathematics:** arithmetic explanation for why p3347 is exceptional, then the exact original GH-3 vs reflected interface comparison. Preserve D25 H0/B0 divided-power, `[X]U mod p²`, Frobenius/eta and native p373. No CLAIM, OPEN, Source checkpoint, Result or independent review is inferred from this GitHub research-note publication.
