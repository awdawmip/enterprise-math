# R284BR — Finite-exception theorem for one frozen leaf of the star-Port determinant

Date: 2026-11-20 (Asia/Shanghai).
Status: AUTHOR_PROVED / ALGEBRAIC_ARGUMENT / NOT_REVIEWED.
Scientific input: exact BP gauge lemma at `R284BP@5a54002ac3d36d2c5aca143198ac72d2b5219047` (blob `0e95becfc0bdb5b82f4780357a9a5b4a58a494b3`). Distinct finite 4×4 binary census R284BQ is saved at `d588bc013048ba982255668a6ce1cb71120d5980`.

## Statement

Fix `n>=4`, `H>=2`, and a leaf index `j∈{1,...,n-1}`. Let `C∈{1,...,H}^{n×n}`, and define the full star-Port polynomial

```
  F_C(d,z) = det(diag(d_0,...,d_{n-1})-C-
                 sum_{i=1}^{n-1} z_i E_{0i}).
```

The designated `d_j=t∈Z` is frozen; `d_0`, every other leaf diagonal, and every `z_i` remain independent free controls.

**BR1 (no persistent single-diagonal ambiguity).**
For any two distinct strictly positive rational matrices `C,C'`, the full polynomial difference `F_C-F_C'` cannot depend on `d_j` alone. In particular, there are not two distinct frozen values `t_1≠t_2` for which `F_C|_{d_j=t_i}-F_C'|_{d_j=t_i}` is constant in the remaining controls. There is at most one such exceptional `t` per distinct matrix pair.

**BR2 (explicit bound for an integer alphabet).**
The set of integer values `t` for which some distinct `C,C'∈{1,...,H}^{n×n}` have a constant difference on their frozen-leaf response is finite and contained in

```
      -2*n!*H^n <= t <= 2*n!*H^n.
```

Consequently, every integer `|t|>2*n!*H^n` makes all `H^{n²}` frozen-leaf response polynomials pairwise different by a **nonconstant** polynomial in the remaining controls.

**BR3 (finite-error one-reading corollary).**
For any such integer `t` and every prescribed finite adversarial circular real error radius `rho>=0`, some prime `p` and a single nonadaptive assignment of all remaining controls in `F_p` permit unique lookup-table reconstruction of every `C∈{1,...,H}^{n×n}`. This is an existence result with no general small-modulus or polynomial-time decoder claim.

The bound is a safe explicit universal bound, not claimed sharp. For `n=4,H=2`, R284BQ strengthens it to the exact leaf `j=1` condition `t<=-4` or `t>=5`.

## Proof

Write `m=n-1>=3`, `C=[a,b^T;v,A]`, `x=(d_1,...,d_m)`, `B(x)=diag(x)-A`, and `g(x)=adj(B(x))v`. The star-Port identity is

```
F_C=(d_0-a) det B - (b+z)^T g.                    (1)
```

**Step 1: coefficient independence.**
The coefficient of the degree `m-1` monomial `prod_{k≠i}x_k` in `g_i` equals `v_i>0`, and all other components of `g` have zero coefficients at that monomial. Hence the polynomials `g_1,...,g_m` are linearly independent over `Q`.

**Step 2: a single-diagonal-only difference forces equality.**
Suppose `F_C-F_C'` depends on `x_j` alone, hence is independent of all `z_i` and of `d_0`.

From the independent `z` coefficients in (1), `g=g'`. The adjugate-vector fibre lemma proved in R284BP applies with *all* leaf variables available: it yields `v'=v` and `A'=A+v alpha^T` for some `alpha∈Q^m`. The rank-one determinant lemma gives `det B' = det B-alpha^T g`. Independence of `d_0` says `det B' = det B`, so Step 1 forces `alpha=0`. Therefore `A'=A`, `v'=v`.

With these equalities the remaining difference is `(a'-a)det B+(b'-b)^Tg`. The unique degree-`m` term of `det B` is `prod_k x_k`; thus `a'=a` if the difference has degree at most one. Next the degree-`m-1` terms of the independent `g_i` force `b'=b`, since `m-1>=2`. Therefore `C=C'`, contrary to distinctness. This proves BR1's first assertion.

**Step 3: two frozen values imply the impossible dependence.**
Fix `C≠C'`. Since every diagonal variable enters the determinant linearly,

```
     F_C-F_C' = x_j U(~x,z) + V(~x,z),
```

where `~x` denotes all the other free diagonals. If the difference were constant in the free controls at two different `x_j` values, subtracting those two polynomial identities would force `U` constant, and then `V` constant as well. Thus the full difference would depend only on `x_j`, contradicting Step 2. The exceptional value is unique if it exists.

**Step 4: explicit integer bound.**
Expand every determinant in (1) by the Leibniz formula with its distinct free-control variables. At `x_j=0`, each coefficient of `V=F_C|_{x_j=0}-F_C'|_{x_j=0}` has integer absolute value at most `2*n!*H^n`: there are at most `n!` permutation contributions for each determinant coefficient, each product of non-control entries has absolute value at most `H^n`.

For a pair whose nonconstant frozen-response coefficient vanishes at integer `t`, some nonconstant coefficient has nonzero integer slope in `U` by Step 3 (otherwise the same difference would be independent of the other controls for every `t`). In that coefficient, `t*u+v=0` with `u∈Z\{0}` and `|v|<=2*n!*H^n`. Therefore `|t|<=2*n!*H^n`. All pairs are covered by the finite alphabet, proving BR2.

**Step 5: finite-field error separation.**
For `|t|` outside that bound all candidate-pair differences in the free variables are nonconstant integer polynomials of degree at most `n`. Let `N=H^{n²}` and `M=floor(2rho)`. Each polynomial `F_C-F_C'-k`, `|k|<=M`, remains nonzero modulo all sufficiently large primes. Schwartz–Zippel and a union bound give failure probability at most `n(2M+1)binom(N,2)/p` under uniform independent free controls. Choose the prime large enough to make that strictly less than one and also `p>2M+1`. A fixed successful setting gives pairwise circular distance exceeding `2rho`. Its closed radius-`rho` balls are disjoint and finite lookup decodes each candidate. This proves BR3.

## Scope, information and continuation

This general theorem is a positive-alphabet existence/exception result for an *auxiliary signed determinant Port observer*. It does not establish a native P000/X6 implementation, positive weighted BRC cancellation, bounded instrument cost, or efficient decoding. Freezing is an observer operation, and changing the frozen control later invalidates a quotient that discards these fibres.

The n=3 boundary is mathematically distinct: when `m-1=1`, a nonzero linear combination of `g_i` may depend on one leaf diagonal alone. That is why the R284BN three-dimensional-alphabet leaf threshold can depend on the error radius.

Next: sharpen the explicit `2n!H^n` bound via source coefficients or rank-one fibre classification; classify exceptional leaf values for `n>=5,H>=3`; seek constructive finite-field controls and an efficient decoder. Preserve the R284BQ exhaustive certificate without rereading or recomputing its 65,536-matrix census.

Historical lineage: R1 portable research, `EM-DIRECT-E6B1DD` (not a current authenticated CLAIM/RUN). Independent mathematical review remains `NOT_REVIEWED`.
