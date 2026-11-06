# D25: exact source-tangent first digit and three-prime fiber theorem

2026-11-06 | Author-side portable evidence | UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.

## Source-labelled definitions and universal algebraic result

Let p=6m+1 be prime, p>=7; a=2m, b=3m, c=4m. All computations are in the p-local rational ring. For j=0,...,p-1 define

```text
U_j(x) = (-1/2)^j * binom(a+x1,j) * binom(b+x2,j) * binom(c+x3,j)
w_j    = 6*j+1
W_p(v) = SUM_j w_j * U_j(p*v)              (mod p^2)
B_p    = SUM_j w_j * U_j(0)
T_i    = SUM_j w_j * (partial_i U_j)(0)    (mod p)
```

**Theorem, all such p and all p-integral source tangents v:**

```text
W_p(v) = B_p + p*(T_1*v1 + T_2*v2 + T_3*v3)  (mod p^2).
```

Proof: The generalized binomial is a polynomial in its upper variable divided by j!, a unit for j<p. Multivariate Taylor at x=0 yields U_j(pv)=U_j(0)+p*grad U_j(0)·v (mod p^2) termwise; sum with signed weights. At j>b at least two original binomial factors vanish, so every first derivative vanishes. The proof does not divide by U_j(0) and includes all labelled carry positions.

Whenever p|B_p, the exact divided first digit is W_p(v)/p = B_p/p + T·v (mod p). For the original 216 sum, v*=(-1/3,-1/2,-2/3) and U_j(p*v*) is exactly the original hypergeometric summand coefficient, including signs.

## Exact kernel and observable loss at three target instances

Two implementations were compared: finite-field polynomial jets without division by a zero coefficient, and direct full weighted binomial sum modulo p^2 with each source perturbed independently.

| p | (T1,T2,T3) mod p | Z mod p | W_p(v*)/p mod p | complete basis of ker(T) | change of labelled j=1 /p on delta=(1,0,1) |
|---:|---|---:|---:|---|---:|
| 13 | (10,12,3) | 0 | 1 | (4,1,0), (1,0,1) | 3 |
| 19 | (4,15,15) | 0 | 1 | (1,1,0), (1,0,1) | 14 |
| 373 | (48,75,325) | 0 | 1 | (115,1,0), (1,0,1) | 93 |

At each listed p, T1 is nonzero, so rank(T)=1, kernel dimension is exactly 2, and every first-digit fiber has exactly p^2 tangents. The labelled j=1 coefficient changes along delta=(1,0,1) by p*(b/2) (mod p^2), since its directional derivative equals -b*(a+c)/2 = b/2 (mod p), nonzero. Thus the first-digit total observer erases information which a subsequent local-coefficient observer retains. This loss is proven only for the stated observer/operation; it is not an assertion of global redundancy or native Frobenius equivalence.

## Exact finite scan, separate universal conjecture

The companion Python certificate `d25_first_digit_source_fiber_20261106.py` verified all 207 primes p=1 mod6 in [7,3000], including three independent direct mod-p^2 finite differences per prime. It found W_p(v*)/p=1 and T1+T3=0 (mod p) in all 207. The latter is an **all-prime conjecture**, not an all-prime proof. p=13/19 kernel lines were also exhaustively tested by direct evaluation; at p=373 selected points were checked and the complete fiber follows from exact linearization.

## Forward connection

The next precise scientific step is an all-prime finite-sum proof or counterexample for T1+T3=0, then a source-preserving map to the compensated regular/one-carry Theta observer. The frozen parent target remains Delta_p-R_p=0 (mod p) for p=13 or 19 (mod 24). Authentic original-class H0/B0, [X]U mod p^2, semilinear Frobenius eta/kappa, odd branch and independent review remain open. This is author-side GitHub evidence, not a native Source checkpoint or formal research acceptance.
