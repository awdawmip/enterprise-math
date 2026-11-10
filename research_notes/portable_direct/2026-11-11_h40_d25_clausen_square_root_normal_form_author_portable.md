# D25/LIFT — Finite Clausen square-root normal form and exact endpoint multiplicity

Date: 2026-11-11. Status: **AUTHOR_PROVED / EXACT_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED**. TASK_RESEARCH, author-side portable evidence, not a native H0/B0 run, Source Result or independent review.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` (OPEN). Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. The existing finite Clausen identity is explicitly reused from `research_notes/portable_direct/2026-11-11_h40_d25_finite_clausen_frobenius_ghost_author_portable.md` at `27fad7cb5f8cae563f4b8e497868280d64569859`; the old theorem is not recredited.

## Universal small-degree normal form

For every prime `p >= 5`, write `p=6m+1+4ε`, where `m=floor(p/6)` and `ε=0` for `p=1 (mod 6)`, `ε=1` for `p=5 (mod 6)`. Put

```text
K_p(X) = sum_{k=0}^m binom(m,k) binom(2m+ε,k) X^k    in F_p[X].
c_k = (1/6)_k (1/3)_k / (k!)^2
f_k = (1/2)_k (1/3)_k (2/3)_k / (k!)^3
G_p(X) = sum_{k=0}^{d_p} c_k X^k; d_p=m if ε=0, d_p=4m+3 if ε=1.
F_p(X) = sum_{k=0}^{floor(p/3)} f_k X^k.
```

Every rational coefficient is reduced from its p-integral representative. **Exact polynomial identities**, not just evaluation congruences, hold:

```text
G_p(X) = (1-X)^{ε(p+1)/2} K_p(X)
F_p(X) = (1-X)^ε K_p(X)^2                           (NF)
```

The polynomial `K_p` has degree exactly `m` and `m` distinct roots in an algebraic closure of `F_p`. Moreover,

```text
K_p(1) = binom(3m+ε,m) != 0 (mod p).
```

Consequently for `p=5 (mod 6)`, `ord_{X=1}(G_p)=(p+1)/2` exactly and `ord_{X=1}(F_p)=1` exactly; for `p=1 (mod 6)`, neither has a root at 1. Thus the complete root divisor of `F_p` consists of `m` distinct double roots and (if and only if ε=1) one additional simple root at 1. Case `p=5,m=0` is included.

### Proof of G normal form

If `p=6m+1`, in `F_p`, `1/6=-m` and `1/3=-2m`. The Gauss coefficient recurrence gives `G_p=K_p`.

If `p=6m+5`, `1/6=-(5m+4)`, `1/3=-(4m+3)`, hence `1-1/6=-m`, `1-1/3=-(2m+1)` in `F_p`, and `1-1/6-1/3=1/2=(p+1)/2` in `F_p`. Euler's Gauss differential-equation transformation shows that

```text
H(X)=(1-X)^{(p+1)/2} 2F1(-m,-(2m+1);1;X)
    =(1-X)^{(p+1)/2} K_p(X)
```

solves the Gauss equation with parameters `(1/6,1/3;1)`. Both `H` and `G_p` have constant term 1 and degree `(p+1)/2+m=4m+3<p`. A polynomial solution of degree `<p` with constant term 1 is unique: its coefficients satisfy `j^2 u_j=(j-1+1/6)(j-1+1/3)u_{j-1}` for all `1<=j<p`, and the denominator is invertible. Therefore `H=G_p`.

### Proof of F normal form and roots

The **previous** finite Clausen identity is `G_p(X)^2=(1-ε X^p)F_p(X)`. For ε=0 substitute `G_p=K_p`. For ε=1 use `1-X^p=(1-X)^p` in characteristic p and the newly proved `G_p=(1-X)^{(p+1)/2}K_p`; polynomial cancellation gives `F_p=(1-X)K_p^2`.

Vandermonde's exact integer identity yields `K_p(1)=sum_k binom(m,k)binom(2m+ε,k)=binom(3m+ε,m)`. Its upper index is `<p`, so it is nonzero mod p, proving the endpoint multiplicities.

The polynomial `K_p=2F1(-m,-(2m+ε);1;X)` solves the Gauss equation with leading second-derivative coefficient `X(1-X)`. At any hypothetical repeated root `α != 0,1` in the algebraic closure, zero initial data `K(α)=K'(α)=0` force all local Taylor coefficients through degree `m<p` to vanish: the coefficient recursion has invertible factors `α(1-α)j(j-1)` for `2<=j<=m`. This contradicts `K(0)=1`. Neither 0 nor 1 is a root. Therefore the m roots are simple.

## Weighted observer in BRC coordinates

The original frozen weighted hypergeometric coefficient satisfies `a_k=2^{-k}f_k`. The operator `D=1+6X d/dX` applied to `F_p` and evaluated at `X=1/2` yields the original `W_p = sum_{k=0}^{p-1}(6k+1)a_k (mod p)`, because `f_k=0 (mod p)` for `k>floor(p/3)`.

Using (NF), the **exact small-polynomial observer formula** is

```text
W_p = 2^{-ε} K_p(1/2)
        ((1-6ε)K_p(1/2)+6K'_p(1/2))       (mod p).  (W-K)
```

These two port factors never vanish simultaneously: if `K_p(1/2)=0`, squarefreeness gives `K'_p(1/2)!=0`, and the second factor is `6K'_p(1/2)!=0`. The ε coordinate carries the endpoint/Frobenius twist required for this particular differential-evaluation observer; the polynomial K alone is insufficient without that coordinate. This is a *typed* BRC descent, not a native crystalline Frobenius assertion.

## Executed exact validation

The accompanying portable Python checker constructs the original `G_p,F_p` from independent hypergeometric recurrences, K from integer binomials, and the twist from integer binomial coefficients; it checks all polynomial coefficients, the gcd(K,K'), Vandermonde, and (W-K). The local full certificate covers **all 301 primes 5<=p<2000**, plus **2003, 2017, 5003, 10007, 10009**: **306 primes**, **102180 original F coefficients** and **129342 original G coefficients**, all PASS. In the tested sample `W_p=0 (mod p)` for every prime, with the two distinct zero-factor types occurring **153** times each. This last finite observation is a separate open all-prime proof target.

Examples: `p=5: ε=1,m=0,ord_1G=3`; `p=11: ε=1,m=1,ord_1G=6`; `p=157: ε=0,m=26,K(1/2)=0,K'(1/2)=118`; `p=373: ε=0,m=62,K(1/2)=0,K'(1/2)=215`; `p=10007: ε=1,m=1667,ord_1G=5004`.

## Continuation

Smallest independent scientific unit: prove the zero of one of the two explicit (W-K) factors for each prime, or produce a scoped counterexample/characterization; then seek a p-adic lift toward `W_p=χ_{-3}(p)*p (mod p^3)` while preserving the ε/Frobenius observer. The original H0/B0 divided-power source module, normalization, semilinear direction, native CM test, and Source admission remain pending actual own session/CLAIM. UR V2 proof is already completed; only original four-file bundle provenance/writer recovery is pending (94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). Do not repeat UR proof or claim that uploaded/staged bytes are Source-published.
