# BRC-X6: source-action collision + Gram–Fischer bound gives explicit 154-bit 13-minimal controller

2026-11-09 · AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_VERIFIED / UNREVIEWED / NOT_ADMITTED.

## Scope and provenance

Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original native 96-port, six actions, four signed source ports (6,7,28,29) with signs (+,-,-,+), nine frozen roots, and full signed next-port / seven-reward joint observer. The 38 lawful preserving deterministic action quadruples and their 24 *labelled* source/action incidence coordinates are retained unchanged. This is **author-side portable mathematics**, not the D25 original-class Frobenius/CM computation, native CLAIM, Source Result or independent review.

This note improves the exact *explicit* certificate in the existing 169-bit base-`2^14` proof. A separate 35-bit result was only an existential bound, not an explicit 35-bit witness; that distinction remains.

Let `c(v)\in\{0,1\}^{24}` be the four-block six-action incidence vector of a lawful pure policy `v`; each column has exactly four ones, one per labelled port. Let `s(x)` be the minimum number of positive-lawful-policy terms in an exact convex representation of `x`.

## New universal native determinant bound

**Theorem (Fischer pairing bound).** Every `k×k` minor of the original `24×38` labelled incidence matrix for `k≤13` obeys

\[
\boxed{|\det M|\le 7200}.
\]

For `k≤12`, Hadamard gives `|\det M|≤2^k≤4096`, since each full incidence column has Euclidean norm 2 and restricting rows cannot increase it.

For `k=13`, fix any one *labelled* source port and distribute 13 arbitrary legal columns among its six actions. If the bin sizes are `n_0,\ldots,n_5`, then there are `q=\sum_a\lfloor n_a/2\rfloor=(13-o)/2≥4` disjoint same-action column pairs; `o≤5` is the number of odd bin sizes. Select four pairs and leave five singleton columns. For any pair, its two full 24-vectors have norms squared 4 and inner product at least 1, so its Gram determinant is at most `16-1=15`. Every singleton Gram determinant equals 4.

For the full `24×13` column matrix `U`, the positive-semidefinite Gram matrix `G=U^T U` satisfies the Hadamard–Fischer inequality for this block partition:

\[
0\le\det G\le15^4\cdot 4^5=51,840,000=7200^2.
\]

Cauchy–Binet gives `\det G=\sum_{R:|R|=13}\det(U_R)^2`. Consequently each original-row-restricted 13×13 determinant has absolute value at most 7200. This is a *source-label collision* bound, not a generic 0/1 determinant bound. QED.

## Five improved fully positive exact-support witnesses

Reuse **the same original 13-lawful-policy list** as the already published base-`2^14` certificate:

```
(0,0,2,2) (1,0,3,2) (2,2,4,4) (3,3,5,5) (4,4,0,0)
(4,4,5,5) (4,5,0,1) (5,1,1,3) (5,5,5,5)
(0,0,0,0) (0,0,1,1) (0,0,4,4) (0,1,2,3)
```

Their prefixes of length `k=9,\ldots,13` all have rank `k` in the **original 24-coordinate rational column space**, and each prefix covers all 24 labelled source/action cells. These properties were rechecked using the frozen original signed kernel and exact rank calculations; no new policy discovery is claimed.

Set `B=7201`, `D_k=\sum_{j=0}^{k-1}B^j`, and

\[
X_k=\frac{1}{D_k}\sum_{j=0}^{k-1}B^j c(v_j),\quad 9\le k\le13.
\]

All 24 original action probabilities are strictly positive, all four port-row sums are 1, and signed native observations are preserved at each of the nine roots by linearity. The construction gives `s(X_k)≤k`.

To prove the lower bound, suppose `D_k X_k` belonged to the rational linear span of `≤k-1` lawful columns. Extend those columns to `k-1` *independent* lawful columns `S` (the full matrix has rank 13). Since the chosen `k` policies are independent, some `c(v_j)` lies outside `span_Q(S)`. Hence there exists a selection of `k` original labelled coordinate rows giving a determinant functional

\[
L(z)=\det([S_1,\ldots,S_{k-1},z]_R),\qquad
a_j=L(c(v_j))\in\mathbb Z,
\]

not identically zero across the chosen `k` columns. By the theorem, `|a_j|≤7200=B-1`. Let `d` be the largest index with `a_d\ne0`. Then

\[
|a_d B^d|\ge B^d,\qquad
\Big|\sum_{j<d}a_j B^j\Big|
\le(B-1)\sum_{j<d}B^j=B^d-1.
\]

Therefore `L(D_kX_k)=\sum_j a_j B^j\ne0`, contrary to membership in the proposed `≤k-1` span. This excludes *all* shorter positive convex decompositions without enumerating 2,707,475,148 twelve-element subsets. Thus

\[
\boxed{s(X_k)=k\quad (k=9,10,11,12,13)}.
\]

### Exact common *unreduced* denominators

| k | D_k | Bits | Older explicit bits |
|---:|---:|---:|---:|
| 9 | 7231073931723390812499202819209 | 103 | 113 |
| 10 | 52070963382340137240806759501124010 | 116 | 127 |
| 11 | 374963007316231328271049475167593996011 | 129 | 141 |
| 12 | 2700108615684181794879827270681844365275212 | 141 | 155 |
| 13 | 19443482141541793104929636176179961274346801613 | **154** | 169 |

The final 13-term **explicit** certificate is shorter by 15 binary bits than the previous exact 169-bit witness. The separately established ≤35-bit *existence* theorem remains stronger as an existential size statement, with no named 35-bit witness.

## Reproducibility and active boundaries

The author-side portable bundle `BRC_X6_SOURCE_COLLISION_FISCHER_7201_AUTHOR_PORTABLE_20261109.zip` contains the unchanged frozen original native kernel; two different exact verifiers; an exact 9–13 numerator/denominator certificate; source-readable full proof; and a SHA-256 manifest. Its two verifiers pass clean extraction checks: rebuilding 1,296 native candidates to obtain exactly 38 lawful policies, all nine roots, original signed reward/next-port edge balances, 24 positive rational cells, exact rank, and the 13-in-six-bins ≥4 disjoint-pairs certificate. This is author-side crosschecking, not independent Driver review.

BRC reuse here is concrete: native source-labelled incidence is retained, overlap is an exact combinatorial residual, and integer determinant functionals certify impossibility of lower-support readouts. Totals, second moments and unsigned port collapses are not substituted for the frozen joint observer. Native P000 and ACTIVE X6 worldview remain unchanged.

**Unfinished original frontier:** UR four-file V2 bundle original bytes (94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remain unrecovered; D25/LIFT/JT2 native `H0/B0`, `[X]U mod p²`, semilinear `eta`, `kappa`/Delta comparison and CM remain NOT_RUN/UNFINISHED. Source CLAIM, formal checkpoint, independent review and acceptance remain separate. The last known durable D25 continuation request is read-only, and this note does not republish old Source research as new owner progress.

**Next discriminating action:** strengthen the ≥4 collision-matching guarantee if true for frozen 38-vertex subsets, with an exact counterexample otherwise; or construct a named ≤35-bit full-positive 13-minimal rational witness with a complete exclusion certificate rather than relying on the existing existential statement.
