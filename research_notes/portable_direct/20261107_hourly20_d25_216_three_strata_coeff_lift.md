# D25: 216 coefficientwise three-port lift through p³ (2026-11-07)

**AUTHOR-SIDE PROVED ALGEBRA / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED.** Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Complements the 2304 three-port lift at `c9b9650c4a34c882c34eec39ccfbc78956e42522` and the parallel on-hour exact Fricke two-jet at `22538312c7d022d773dd09562273e724d23af290`, without claiming to replace either.

## Universal coefficientwise theorem

Let `p=6m+1>3` be prime and `0<=n<p`. Define
`a_n=(1/2)_n(1/3)_n(2/3)_n/(2^n(n!)³)` in `Z_(p)`,
`H_r^(s)=sum_(j=1)^r j^(-s)`, `H_0^(s)=0`,
and `D_r^(s)(n)=H_r^(s)-H_(r-n)^(s)`.
All expressions below have p-unit denominators in the displayed ranges.

**L: `0<=n<=2m`, valuation 0.** Put
`h_n=(-1)^n binom(2m,n)binom(3m,n)binom(4m,n)/2^n`,
`u_n=-D_(2m)^(1)(n)/3-D_(3m)^(1)(n)/2-2D_(4m)^(1)(n)/3`,
`v_n=D_(2m)^(2)(n)/9+D_(3m)^(2)(n)/4+4D_(4m)^(2)(n)/9`.
Then

`a_n = h_n[1+p u_n+(p²/2)(u_n²-v_n)] (mod p³)`. (A)

**M: `2m<n<=3m`, valuation 1.** Put
`M_n=(2m)!(3m)!(4m)!(n-2m-1)!/[3(3m-n)!(4m-n)!(n!)³2^n]` and
`u'_n=(H_(n-2m-1)-H_(2m))/3 -(H_(3m)-H_(3m-n))/2-2(H_(4m)-H_(4m-n))/3`.
Then `a_n=p M_n(1+p u'_n) (mod p³)`. (B)

**U: `3m<n<=4m`, valuation 2.** Put
`U_n=(-1)^(3m+n)(2m)!(3m)!(4m)!(n-2m-1)!(n-3m-1)!/[6(4m-n)!(n!)³2^n]`.
Then `a_n=p²U_n (mod p³)`. (C)

**Discard: `4m<n<p`, valuation 3:** `a_n=0 (mod p³)`. (D)

**Proof.** The exact p-local substitutions are `1/3=-2m+p/3`, `1/2=-3m+p/2`, `2/3=-4m+2p/3`. Their rising-factorial zeros occur at `j=2m,3m,4m` respectively; `n! ` is a p-unit. Before any zero, expand the product over p-units by the identity `product(1+p x_j)=1+p sum(x_j)+(p²/2)[(sum x_j)²-sum x_j²]` modulo p³, obtaining (A). After the first zero, remove `p/3` and retain linear unit-factor corrections, yielding (B). After the second zero, remove `p/2` and keep the constant unit term, including its parity, yielding (C). After the third zero, the coefficient is p³-divisible. Every equality is uniform over all specified primes and indices.

## Required weighted-source bridge

The weighted 216 series `W_p=sum_(n=0)^(p-1)(6n+1)a_n` is represented modulo p³ by `L_A+p M_A+p²U_A` from the above disjoint index ports. The existing 2304 construction supplies `L_B+p M_B+p²U_B`, retaining its different cutoff boundaries. The remaining, **not proved here**, exact bridge certificate is
`(L_A-L_B)+p(M_A-M_B)+p²(U_A-U_B)=0 (mod p³)`.
The previously proved Guo-Zudilin 2304 full/half theorem gives `U_B=0 (mod p)` after normalization, whereas `U_A` need not vanish. The target requires cancellation across the lower lifts; a scalar port quotient erases this information. The next unit combines these exact coefficient lifts with the independent finite Fricke two-jet, aiming to prove the normalized lower-port correction rather than rechecking whole sums.

**Reproduction.** Python standard-library integer finite-ring checker `d25_216_padic_ports_compact_20261107.py` checked all 36,668 coefficients for all 80 primes `7<=p<1000, p=1(mod6)` against the independent hypergeometric recurrence. A second integer-binomial evaluator checked every n for `p=13,19,43,67,373`. Weighted snapshots `(p,L,(pM)/p,(p²U)/p²)`: `(19,5662,254,9)`, `(43,53062,960,35)`, `(67,134938,3079,58)`, `(373,28094360,103721,266)`; recombined original finite W sums equal p modulo p³ for these **finite** cases. This is not the native p373 H0/B0 experiment.

**BRC:** `COMPOSE_APPLIED`; preserve index, valuation port, signed weight, first/second coefficient-lift corrections, and future Fricke branch. External p-adic arithmetic does not override P000/ACTIVE project worldview.

**Control status:** current gateway `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`, Site `CONFIGURED_NOT_LIVE_VERIFIED`; historical session/claim/run/staging UNKNOWN/PRESERVE, `REGISTER_PENDING`. Do not replay `em-h20-20261106-1324-d25-task-r13` or `em-h20-20261106-1324-d25-cont-r13`. Support issue #1558. No native checkpoint, formal Result/review/admission asserted.
