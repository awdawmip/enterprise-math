# D25 — Finite Gauss Picard–Fuchs endpoint and two-moment LIFT observer

2026-11-06 · TASK_RESEARCH author-side; EXACT PROVED / FINITE VERIFIED / UNREVIEWED / NOT_ADMITTED. Frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3; publication TP2-B6F4FC938FF94941C1B7; Research lane chatgpt-research-onhour-enterprise-math-20260923. No maintenance-lane identity. Original native p373 H0/B0 benchmark #1559 remains pending.

## Theorem 1 — an exact finite Picard–Fuchs defect

Let d_n=(1/6)_n(1/3)_n/[2^n(n!)²], F_N(x)=Σ_{n=0}^{N−1} d_n x^n and θ=x∂_x. For **every integer N≥1** the identity of rational polynomials is

    [36θ²−x(6θ+1)(3θ+1)]F_N(x)
        = −(6N−5)(3N−2)d_(N−1) x^N.                 (1)

Proof: 36(n+1)²d_(n+1)=(6n+1)(3n+1)d_n. Coefficients of degrees <N cancel exactly. At degree N the missing coefficient gives precisely the stated right side.

For every prime p=6m+1>3, v_p(d_(p−1))=2, and the reflected product formula (also directly from Wilson's theorem and the two numerator progressions) gives

    d_(p−1)/p² ≡ 1/10  (mod p).

Explicitly (1/6)_(p−1)/p ≡1/5, (1/3)_(p−1)/p ≡1/2, and 2^(p−1)((p−1)!)²≡1 (mod p). Therefore the exact source at the truncated endpoint is

    [36θ²−x(6θ+1)(3θ+1)]F_p(x)
           ≡ −p² x^p (mod p³).                     (2)

The high-index p² endpoint is nonzero; setting the finite Picard–Fuchs defect to zero modulo p³ loses one real observer.

## Theorem 2 — a universal quadratic moment

Set S=Σ_(n<p)d_n, T=Σ_(n<p)n d_n, M2=Σ_(n<p)n²d_n, and K=S+12T. Equation (1) at x=1 gives exactly

    18M2−9T−S=−(6p−5)(3p−2)d_(p−1),

and therefore, for **every prime p≡1 (mod 6)**,

    Σ_(n<p)(1+9n−18n²)d_n ≡ p² (mod p³),            (3)
    K ≡ 24M2−S/3+(4/3)p² (mod p³).                (4)

## Theorem 3 — direct source-preserving LIFT equivalence

Consume the previously proved signed Clausen triangular relation with its ordered low/high pairs (not newly credited):

    W_p ≡ S K − 2p² J_p (mod p³),
    R_p ≡ 2J_p (mod p),

where W_p=Σ_(n<p)(6n+1)(2n)!(3n)!/[216^n(n!)^5], and J_p is the original signed triangular correction. Inserting (4) gives, for all p≡1 (mod6),

    W_p ≡ 24 S M2 − S²/3 + (4/3)p² S − 2p² J_p (mod p³).   (5)

For target primes p≡13,19 (mod24), consume the accepted CM first digit p|S, put G=S/p mod p², retain the frozen original Δ_p=(G K−1)/p mod p and R_p=2J_p. The accepted UR first-digit GK≡1 (mod p) legitimizes division. From (4):

    Δ_p−R_p ≡ [24 G M2−(p/3)G²−1]/p − 2J_p (mod p).       (6)

Consequently the frozen D25 LIFT objective is **strictly equivalent** to a new three-observer finite congruence

    24 G M2 − (p/3)G² ≡ 1 + 2p J_p (mod p²).             (7)

This replaces the separate first-weighted-jet and Legendre companion in the *evaluation interface* by a quadratic Gauss moment constrained by the exact Picard–Fuchs defect. It retains all p-adic bands implicitly in G/M2 and explicitly the nonzero signed ordered-pair cutoff J. The universal cancellation (7) is **OPEN**; only the equivalence (6)–(7) and moment identity (3) are proved here. M2 is a moment, distinct from the earlier upper valuation shell named U_p.

## Executed independent exact checks

A separate stdlib modular checker reconstructs d_n and its 0/1/2 moments, original weighted 216 sum W independently, and the reflection-prefix signed correction J independently. Exact rational identity (1) checked for N=1..11. All 80 primes p≡1 mod6, 7≤p≤997, pass (2)–(5), and 45 target primes pass the precise frozen observer equality (6). Finite 45/45 zero values of (7) are empirical, not its general proof.

| p | S mod p³ | M2 mod p² | G mod p² | J mod p | 24GM2−pG²/3 mod p² | Δ | R |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 988 | 88 | 76 | 0 | 1 | 0 | 0 |
| 19 | 1596 | 295 | 84 | 6 | 229 | 12 | 12 |
| 67 | 62444 | 3236 | 932 | 44 | 1408 | 21 | 21 |
| 373 | 24495656 | 78104 | 65672 | 98 | 73109 | 196 | 196 |

At p=373, (73109−1)/373=196=R, at p=19 (229−1)/19=12=R; the signed cutoff is genuinely nonzero. Original native H0/B0 [X]U mod139129, rank, eta, Frobenius, kappa and independent replication remain NOT_EXECUTED/PENDING_OWNER on Issue #1559. This study is not a Source-native Result or independent review.

Next scientific unit: use (2) as nonhomogeneous Gauss/Picard–Fuchs input to attempt an actual Jacobi/CM or finite creative-telescoping certificate for (7), first preserving p=19 and p=373 nonzero triangular boundary; compare with the inherited four-source two-jet residual without redoing its proven components. Preserve original immutable p-adic source, observer labels, exact arithmetic, and BRC signed pair incidence. External Gauss polynomial variables are number-theoretic auxiliary coordinates, not native X6 geometry or a 2D Enterprise slice.

Checker: research_notes/portable_direct/d25_gauss_picard_endpoint_check_20261106.py (same commit).