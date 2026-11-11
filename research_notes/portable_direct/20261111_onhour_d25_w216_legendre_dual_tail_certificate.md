# D25/LIFT — W216 镜像尾项的 Legendre–对偶超几何精确公式

Date: 2026-11-11 Asia/Hong_Kong.
Status: AUTHOR_SIDE / SYMBOLIC_PROOF / 22_EXACT_PRIME_CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0B0_NOT_RUN.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Frozen scientific source: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged.
Provenance: current TASK_RESEARCH author-side construction; logical Research lane declared `chatgpt-research-onhour-enterprise-math-20260923`; not a platform-authenticated session claim.
Predecessor theorem: `research_notes/portable_direct/20261111_onhour_d25_w216_reflected_half_length_exact_certificate.md`. Its half-length fold is consumed, not reproved as a new claim.

## Theorem A: character value of the distinguished middle coefficient (all p>3)

Set `a_k=(2k)!(3k)!/(216^k(k!)^5)` in `Z_(p)`, `n=(p-1)/2`, and `chi_p=(6/p)`, the Legendre symbol. Then `v_p(a_n)=1` and

```text
b_n := a_n/p mod p = -2 chi_p   in F_p.
```

Proof: `2n=p-1`, `3n=p+(n-1)`. For `r<p`, the p-free unit of `(p+r)!` is `-r!` mod p. Wilson gives `(p-1)!=-1`, so

```text
b_n = (n-1)! / (216^n (n!)^5)
    = n^(-1) * (n!)^(-4) * 216^(-n)  (mod p).
```

Wilson's middle-factorial identity `(n!)^2=(-1)^(n+1)` makes its inverse fourth power 1, and `n^(-1)=-2`. Euler's criterion gives `216^(-n)=(216/p)=(6/p)` because `216=6^3`. QED.

## Theorem B: exact dual hypergeometric form of the original reflected tail

Let `p=6m+1>3`, `n=3m`, and define the polynomial over `F_p`

```text
H_m(x) = sum_{j=0}^{m-1} (1)_j (5/6)_j (7/6)_j
                       / ((3/2)_j)^3 * x^j.
D_m = (4+6x d/dx) H_m(x) |_(x=1/2).
```

All displayed denominators are p-units for `0<=j<m`. This equals the corresponding truncation of `_4F_3(1,1,5/6,7/6;3/2,3/2,3/2;x)`, because its standard `j!` cancels one of the two upper `(1)_j` factors. In characteristic p, `(7/6)_m=0`; the truncation is natural.

The previous exact mirror theorem supplied

```text
W_p := sum_{k=0}^{p-1} (6k+1)a_k
  = L_p + p^2 T_p  (mod p^3),
L_p := sum_{k=0}^{n}(6k+1)a_k,
T_p := sum_{2m<k<=3m} (1-6k)/(36k^3 b_k)   in F_p,
b_k:=a_k/p mod p.
```

Here **the new exact reduction** is

```text
T_p = chi_p D_m / 9                      (mod p),
W_p = L_p + p^2 chi_p D_m/9              (mod p^3).
```

Proof: put `k=n-j`, `0<=j<m`, and `B_j=b_(n-j)^(-1)`. The original coefficient recurrence `a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3)` gives

```text
B_(j+1)/B_j
 = (j+1)(j+5/6)(j+7/6) / (2(j+1/2)^3) mod p,
B_j = B_0*(1)_j*(5/6)_j*(7/6)_j/
                  (2^j * (1/2)_j^3).
```

Also `1-6(n-j)=6j+4 (mod p)` and `n-j=-(j+1/2) (mod p)`. Hence using `(1/2)_(j+1)=(1/2)(3/2)_j`,

```text
T_p = -(2 B_0/9) *
      sum_(j=0)^(m-1) (6j+4) (1)_j*(5/6)_j*(7/6)_j /
                                (2^j*(3/2)_j^3).
```

Theorem A gives `B_0=(-2chi_p)^(-1)=-chi_p/2`. Substitution proves `T_p=chi_p D_m/9`. QED.

For the frozen target classes, `p≡13 (mod24)` has `chi_p=-1`, whereas `p≡19 (mod24)` has `chi_p=+1`.
Since the accepted first-digit interface ensures `L_p≡p (mod p^2)` in these classes, the **precise remaining scalar LIFT criterion** becomes:

```text
(L_p-p)/p^2 + chi_p D_m/9 = 0  in F_p.
```

This is a strictly typed transfer of the original reflected p² tail to an explicitly signed finite-field terminating hypergeometric jet. It eliminates the `m` unknown unit inversions `b_k^(-1)` from the observer *formula* and exposes the Legendre character. Arithmetic complexity includes evaluation of `H_m,D_m` and the p³ half-sum; no asymptotic improvement is claimed.

## Exact execution and p=373 certificate

Checker `d25_w216_legendre_dual_tail_20261111.py` used independent factorial-block normalization, the original modular recurrence, direct I2 signed contribution and independent dual polynomial recurrence. 22 selected primes (including both p≡1 and p≡5 mod6 for Theorem A, and target p=373) passed all applicable assertions. No floating point was used.

For `p=373`, `m=62`, `n=186`, `chi_373=-1`, `b_186=2`.
The dual polynomial has `H_m(1/2)=121` and `H'_m(1/2)=284`, so

```text
D_m = 4*121 + 3*284 = 217 (mod373);
T_373 = (-1)*217/9 = 266 (mod373);
L_373 = 14887176 (mod51895117);
W_373 = 14887176 + 139129*266
      = 51895490 = 373 (mod51895117).
```

Thus the new character–dual formula exactly reproduces the *original* signed reflected contribution `266` and the surviving second-digit cancellation `107+266=0 mod373`, retaining the original p-adic valuation and coefficient provenance. No native H0/B0 [X]U computation is implied.

## Continuation / concrete missing evidence

The frozen parent LIFT/JT2 target remains open. To close it mathematically, prove `(L_p-p)/p²=-chi_p D_m/9` for all target primes via the original half-range p³ coefficients, or find an exact original-class counterexample. This new hypergeometric polynomial supplies a finite-field derivative/jet attack surface without reducing p-adic precision of `L_p`. The highest-priority native benchmark continues to be `[X]U mod139129` at p373, with actual H0/B0 rank, Frobenius semilinear direction, eta, signed kappa, original Delta-R and independent reproduction via existing Issue #1559 (pending owner).

Source claims/Result/Driver admission are not asserted. On 2026-11-11 the historical exact continuation `onhour11-20261111-1457-cont` was SUCCEEDED; the new read `onhour11-20261111-1608-exact-cont` was QUEUED when this note was authored. Own site recovery returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; historical session `MCP-7af27f545c01441eaf19206f89c6832b` is provenance, not current execution capability.
