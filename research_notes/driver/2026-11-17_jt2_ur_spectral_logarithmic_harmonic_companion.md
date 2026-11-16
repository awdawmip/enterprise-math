# JT2 UR — Exact logarithmic spectral derivative and harmonic-sum companion

Date: 2026-11-17 (Asia/Shanghai). Status: **PROVED EXACT RATIONAL IDENTITY + MOD-p HARMONIC REDUCTION; FINITE CHECKS**. The all-prime UR target remains OPEN.

## Scope, definitions and provenance

Let `m>=1`, `C*=m(2m+1)`, and `Q_m(Y)=P_{2m}(sqrt(Y))=sum_{j=0}^m c_jY^j`, with the usual Legendre normalization `P_{2m}(1)=1`. Put `c0=(-1)^m binom(2m,m)/4^m`. Use the existing spectral polynomial `H_m(C,Y)=sum_{j=0}^m a_j(C)Y^j`, where `a_0=1` and

```
a_(j+1)(C) = (j(2j+1)-C) a_j(C) / ((j+1)(2j+1))   (0 <= j < m).
Z_m(Y)=c0 * (partial H_m(C,Y)/partial C)|_(C=C*).
```

The original JT2 UR mother question and scoped accepted work belong to their recorded contributors, including `EM-JT2-EF9380`. The prior spectral-parameter reduction and the new companion are **author-side Driver extensions by EM-DVR-DEBB5E**. No independent Native Result acceptance is claimed.

## Theorem A — Exact spectral logarithmic-derivative coefficients over Q

For every `0<=j<=m`, define

```
T_0=0,
T_j=sum_{i=0}^{j-1} 1 / ((m-i)(2m+2i+1)).
```

Then the following identity holds in `Q[Y]`:

```
Z_m(Y)=sum_{j=0}^m c_j T_j Y^j.
```

In particular, `T_(j+1)=T_j+1/((m-j)(2m+2j+1))`; the full `Z_m` can be evaluated from the Legendre coefficient recurrence in O(m) rational arithmetic operations without symbolic parameter differentiation.

**Proof.** Write `a_j(C)=prod_{i<j}(i(2i+1)-C)/((i+1)(2i+1))`. At `C=C*`, each numerator is nonzero for `i<j<=m`, and factors as

```
i(2i+1)-m(2m+1)=(i-m)(2m+2i+1).
```

Logarithmic differentiation therefore gives

```
a'_j(C*)/a_j(C*)=-sum_{i<j} 1/(i(2i+1)-C*)
                 =sum_{i<j} 1/((m-i)(2m+2i+1))=T_j.
```

Since `c_j=c0*a_j(C*)`, coefficient comparison proves the theorem. The case `j=0` has derivative zero. QED.

## Theorem B — Uniform prime-dependent harmonic collapse

Let `p=6m+1` be prime (`p>3`), and let `H_n=sum_{k=1}^n 1/k` with `H_0=0` in `F_p`. All denominators occurring below are p-units because `2m<p`. Then

```
T_j = 3*(H_m-H_(m-j)-H_(2m)+H_(2m-j))     (mod p), 0<=j<=m,
Z_m(Y) = 3*sum_{j=0}^m c_j Y^j
               *(H_m-H_(m-j)-H_(2m)+H_(2m-j)) (mod p).
```

**Proof.** The rational partial fraction is

```
1/((m-i)(2m+2i+1))
 = (1/(4m+1))*(1/(m-i)+2/(2m+2i+1)).
```

Because `p=6m+1`, `2m+2i+1=p-2(2m-i)` and `4m+1=(2p+1)/3`; hence modulo p the right-hand side is `3*(1/(m-i)-1/(2m-i))`. Sum `i=0,...,j-1`, use harmonic-number differences, and substitute Theorem A. QED.

## Corollary — Eliminate the spectral derivative from the UR jet formula

For the standing JT2 primes `p>3`, `p mod 24 in {13,19}`, put `Y*=1/2`, `d=Q'_m(Y*) mod p`, `J_m(Y)=sum_r [Y^r]Q_m(Y)^2 * Y^r/(2r+1)`, and

```
S_p=sum_{j=0}^m c_j*2^(-(m+j))/(2m+2j+1) (mod p).
D_j=H_m-H_(m-j)-H_(2m)+H_(2m-j) (mod p).
```

Assume the explicitly checked CM0 premise `Q_m(1/2)=0 mod p`. The previously proven polynomial Lagrange identity `2J_m(1/2)=d Z_m(1/2)+2c_m S_p (mod p)` now gives the **fully explicit harmonic companion**

```
2J_m(1/2) = 3*d*sum_{j=0}^m c_j*2^(-j)*D_j + 2*c_m*S_p (mod p).
```

Writing `u=Q_m(1/2)/p mod p` (computed using p²), the original residual becomes

```
epsilon_p = 18*u*d - 3*d*sum_{j=0}^m c_j*2^(-j)*D_j - 2*c_m*S_p - 3 (mod p).
```

Thus one may verify the complete original UR residue by two O(m) weighted sums and the original linear coefficient scan, without quadratic convolution, spectral-parameter differentiation or a new mathematical premise. This is a reduction/evaluation theorem, not an all-prime vanishing proof.

## Verification and exact scope

A separate pure-Python `fractions.Fraction` validator differentiates the *unexpanded spectral coefficient recurrence* directly and compares every coefficient with `c_j T_j` exactly for `m=1,...,8`. It separately checks the prime harmonic congruence, the Lagrange-J reduction against direct quadratic rational convolution, and the resulting residual for `p=13,19,37,43,61,67,109`, with no floating point arithmetic. The seven checked residuals are zero.

Verifier: `experiments/jt2_ur_spectral_harmonic_companion_20261117.py`.

Parent frontier remains: prove/disprove `epsilon_p=0` for every required prime, or derive an evaluation of the harmonic/quotient expression sufficient for that statement; do not promote author-side checks to independent Native review. This note preserves the spectral reduction provenance and CM0 dependency as separate facts.
