# PREFIX-869 — Exact p=31 odd-port recovery via strict alphabet capacity

Date: 2026-11-17. Previous result: PREFIX-868, full-transition fixed two odd moduli p=27–30.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Scope: binary named-source auxiliary BRC modulo observer. Scientific status: author-proved with exact arithmetic check; independent review and native X6 event admission pending.

## Model

For p named binary sources, N=2^p. A legal ordered update is a no-op or a flip of one named bit, yielding exactly T=N(p+1) distinct ordered (before,after) transitions. Two predetermined odd modulus observations (u mod q1, v mod q2), with each modulus represented by at most B bits (so q1,q2<=2^B-1), must jointly identify the complete ordered transition.

## Theorem 869-A: strict port-alphabet bound

For all p>=1 and any fixed moduli (odd or even), injectivity requires

```
(2^B-1)^2 >= 2^p(p+1).
```

**Proof.** The total number of possible ordered residue pairs is q1*q2, at most (2^B-1)^2; all N(p+1) distinct transitions must map to distinct outputs. QED.

Consequently B is at least the *smallest integer* satisfying that strict finite-alphabet inequality, which is a potentially stronger lower bound than simply requiring 2^(2B)>=T.

**Infinite boundary family.** For any odd positive integer k, put p=2^k-1. Then p+k is even and T=2^(p+k), so B>=(p+k)/2+1. Indeed, choosing B=(p+k)/2 gives (2^B-1)^2<2^(2B)=T. For example k=3 gives p=7, B>=6; k=5 gives p=31, B>=19. This is a uniform lower bound for the entire family, not a claim of its general optimal attainability.

## Theorem 869-B: exact optimal width for p=31

```
B_fix,odd(31)=19.
```

**Lower bound.** Here T=2^31*32=2^36=68,719,476,736, whereas two 18-bit residue alphabets have at most (2^18-1)^2=68,718,952,449 pairs, a shortfall of 524,287. Therefore B>=19.

**Matching constructive upper bound.** Choose the shared GCD g=67 and coprime odd a=5661, b=5663. Then

```
q1=379287,  q2=379421,
gcd(a,b)=1,  h(67)=33>=31,
lcm(q1,q2)=g*a*b=2147902281>=2^31=2147483648.
```

The h(g) condition makes the legal increments delta in {0, +/-2^i : 0<=i<31} pairwise distinct mod 67. The difference of the observed residues mod 67 recovers delta, and generalized CRT recovers terminal v from v=r1+delta (mod q1), v=r2 (mod q2) uniquely on 0<=v<2^31. Recover u=v-delta and the named flipped bit, if any. q1 and q2 each fit 19 bits, proving the matching bound. The construction is an instance of PREFIX-861's shared-GCD theorem.

## Exact check and continuation

The accompanying Python standard-library script validates half-order, coprimality, both odd moduli, lcm coverage, the strict 18-bit capacity deficit, and the infinite-family capacity formula at k=1,3,5,7,9. It returned ALL_EXACT_ASSERTIONS_PASSED. The infinite family follows from the symbolic proof; testing selected k does not supply its general proof.

This new p=31 result needs no massive exclusion loop. It changes neither native X6 Cell/Link/Port event admission nor the locked P000 ontology, and it does not assign a shared Task CLAIM or independent review status.

Next: examine when the strict finite-alphabet bound is attained for general p; improve CRT common-factor constructions and classify the p=32 boundary, while developing structural (non-enumerative) collision certificates for p=27 and p=29.
