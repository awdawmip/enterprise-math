# D25 / AF4 — exact low/high signed interface and base-p carry certificate

Date: 2026-11-09. Parent Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`; ordinary Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`, NOT the maintenance lane. **AUTHOR-SIDE finite exact calculation and conditional algebraic reduction; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**

## Reused original carriers (not a different experiment)
`A_n = binom(2n,n)^2 binom(3n,n) / 216^n`, `C_n = binom(4n,2n) binom(2n,n)^2 / 2304^n`, `W_p = sum_{n=0}^{p-1}(6n+1)A_n`, `V_p = sum_{n=0}^{p-1}(8n+1)C_n`.
For p>3, partition by *coefficient* valuation `v_p(A_n)=floor(2n/p)+floor(3n/p)`, `v_p(C_n)=floor(4n/p)` for 0<=n<p. Preserve weight factors before reduction. `W_g,V_g` denote the corresponding signed sums, computed modulo p^4. `chi=(-3/p)`.

Set `L=(W_0+W_1)-2(V_0+V_1)+p chi`, `M=W_2-2V_2`, and `H=W_3-2V_3`, modulo p^4. For the chosen p, `p²|L,M` and `p³|H` were verified with original coefficients. Define canonical residues `ell=L/p² mod p²`, `b=M/p² mod p²`, `t=H/p³ mod p`. Then exactly
$$
\frac{W_p-2V_p+p\chi}{p^2}\equiv\ell+b+pt\pmod{p^2}.
$$
This is the *specific* remaining additive AF4 interface, not a claim that the conjecture holds for all p.

## Exact decimal data: first direct zero/first-grade vs B/Z/D boundary comparison

| p | ell (mod p²) | b=(B_A-2B_C)+p[(Z_A-2Z_C)+(D_A-2D_C)] (mod p²) | t | ell+b+p*t (integer) | mod p² |
|---:|---:|---:|---:|---:|---:|
| 13 | 94 | 166 | 6 | 338 = 2*169 | 0 |
| 19 | 238 | 294 | 10 | 722 = 2*361 | 0 |
| 37 | 498 | 1278 | 26 | 2738 = 2*1369 | 0 |
| 43 | 524 | 1841 | 31 | 3698 = 2*1849 | 0 |
| 73 | 4495 | 2586 | 49 | 10658 = 2*5329 | 0 |
| 373 | 90746 | 33463 | 40 | 139129 = 373² | 0 |

This newly computes `ell` on the **original coefficient-grade zero and one carriers**, rather than inferring it merely as the negative of higher bands. The `b` column coincides at p=13,19,373 with the separately persisted signed first-jet Abel results in `20261109_onhour_d25_WV_signed_firstjet_Abel_boundary.md`. Both the exact original recurrence and a separately coded integer-binomial evaluation agree for 13,19,373; the recurrence checks the other three primes. Detailed original grade sums are in the companion JSON.

## New explicit carry-level boundary condition

Choose base-p digits `ell=ell0+p*ell1`, `b=b0+p*b1` with each digit in `{0,...,p-1}`. Whenever `ell0+b0` is divisible by p, its **unreduced carry** `c=(ell0+b0)/p` is 0 or 1. By exact base-p arithmetic, AF4 for this input is equivalent to *both*:
$$
\ell_0+b_0\equiv0\pmod p,\qquad
\ell_1+b_1+c+t\equiv0\pmod p.
$$
The carry is not optional: it transfers one full unit to the fourth p-adic digit. In all six checked cases `c=1`. For the frozen representatives:

| p | ell0 | b0 | c | ell1 | b1 | t | ell1+b1+t | ell1+b1+c+t |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 3 | 10 | 1 | 7 | 12 | 6 | 25 | 26 |
| 19 | 10 | 9 | 1 | 12 | 15 | 10 | 37 | 38 |
| 373 | 107 | 266 | 1 | 243 | 89 | 40 | 372 | 373 |

Thus the proposed *carry-free fourth-digit cancellation* `ell1+b1+t=0 mod p` is **refuted at both p=13 and p=19 (and p=373)**, while the exact carry-aware AF4 congruence passes at these three values. This isolates a specific omitted boundary term for future WZ/Fricke candidates. It is a BRC-style source/operation-preserving arithmetic carry observer: no native six-axis or H0/B0 operator identification is asserted.

## Verification, owner and next
Run `d25_AF4_low_high_interface_20261109.py` (exact recurrence) and `d25_AF4_low_high_independent_20261109.py` (independent integer binomial checks). Operations use only integer arithmetic and modular inverses of the original p-units (36,288 and n+1; or 216 and 2304); no float. This is a narrower proof interface and an exact counterexample to a concrete carry-free branch; AF4 universal all-prime cancellation is open.

**Next load-bearing action:** derive, on the original zero/first-grade sums, an independent symbolic finite WZ/Fricke boundary expression for the **two-digit pair** `(ell0,ell1)` and test against the already-known `(b0,b1,t,c)`, including 13 and 19. The authentic native p=373 H0/B0 `[X]U mod 139129` and rank/direction/eta/signed kappa/Delta-R remain pending on existing #1559 with no verified executor. Source Role: historical `EM-ENTERPRISE-4DEB43`; current capability/CLAIM/run not verified, so this is author-side Git evidence, not a native checkpoint or accepted Result.
