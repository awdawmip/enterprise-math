# PREFIX-731-R6 — Exact monotone-moment domination over 144 whole Gamma-grid cells

Date: 2026-11-12 (Asia/Shanghai). Mother problem: PREFIX-675; scientific input remains frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Scientific status: AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem

Use the frozen 189-level BRC stopping/survivor count observer with two independent, conditional, unit-rate Gamma completion clocks, as in PREFIX-726 to PREFIX-730. Let
`Y(p,z)=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²`,
`f_t=W-t*mu` and `V_q=q² f_(1/q)`, for `(p,z) in [0,1/2]^2` and every real `q>=2`.

Let the fixed feasible comparator `e=(0,73/500)` and the closed square
`S=[38/384,50/384] × [38/384,50/384]`.
Then the following inequality holds simultaneously for every `(p,z) in S` and every real `q>=2`:

```
V_q(e)-V_q(p,z) > 40*q² > 0.
```

Thus the 12×12 block of **144 entire cells** with indices `(i,j)`, `38<=i,j<50`, is excluded from the frozen auxiliary global maximizer set. It extends the separately published PREFIX-729/730 whole-cell comparator block `40<=i,j<48` (64 cells); 80 certified cells lie geometrically outside that particular block. Their *new contribution to the complete historical all-q union* still requires exact deduplication against the PREFIX-712/713/714/716/718 union. No additive union percentage is claimed here.

## Proof: monotone second-moment rectangle envelope

For each frozen survival row `n<189`, let `w_(n,k)` be its actual nonnegative survivor-path count, and write
`b_(n,k)=w_(n,k)/binom(n,k)` and `s_n(p)=sum_k w_(n,k) p^k(1-p)^(n-k)`.
The exact checker reconstructs 9,529 nonzero cells from the original 18-bit integer-width predicate and verifies in every row
`b_(n,k)=b_(n,n-k)`, `b_(n,k+1)>=b_(n,k)` for `k<n/2`.
The Bernstein derivative pairing (PREFIX-727) then yields `s_n'(p)>=0` for `0<=p<=1/2`. Hence the integer clock shape `N_p` is ordered stochastically in `p`, because `Pr(N_p>n)=s_n(p)`. The unit-rate Gamma clock can be realized as a sum of positive exponential increments; consequently the two-clock maximum and its square are stochastically increasing in each coordinate. In particular, both `mu(p,z)` and `M2(p,z)` are coordinatewise nondecreasing on the domain.

Write `c=11/96=44/384`, `h=1/384`, and the 19 exact rational subdivision points
`a_i=c-6h+i/(576)` for `i=0,...,18`; they span `[38/384,50/384]`.
For each of the 324 rational rectangles
`R_ij=[a_i,a_(i+1)]×[a_j,a_(j+1)]`, let
`m_ij=mu(a_i,a_j)` and `B_ij=M2(a_(i+1),a_(j+1))`.

For every `x in R_ij`, `mu(x)>=m_ij>0`, `M2(x)<=B_ij`. Since `t>=0`,
```
f_t(x)=M2(x)-mu(x)^2-t*mu(x)
     <= B_ij-m_ij^2-t*m_ij =: U_ij(t).
```

Every comparison `f_t(e)-U_ij(t)` is affine in `t`. The checker evaluates the frozen conditional-Gamma moment kernel at the comparator and all needed exact rational corners, then verifies for each `0<=i,j<18`:
```
f_0(e)-U_ij(0) > 40;
f_(1/2)(e)-U_ij(1/2) > 40.
```
By affinity this holds on the complete interval `t in [0,1/2]`, including `t=1/q` for all real `q>=2`. Clock-exchange symmetry reduces the 324 rectangle checks to 171 exact rational computations. The smallest observed integer floor of the endpoint gaps is 46 (index `(0,17)`, `t=1/2`), strictly above the chosen floor 40. This proves the theorem.

## Exact evidence and reproduction

The accompanying `PREFIX731_R6_MONOTONE_MOMENT_TILE.py` uses standard-library arbitrary-precision integers and `fractions.Fraction`, the frozen 189-row integer predicate, and the exact negative-binomial Gamma kernel. It cross-checks the center and comparator moments against the independently published PREFIX-726 hashes. The local standalone exact computation completed with `ALL_CHECKS_PASS PREFIX729-R6` under the earlier local draft filename: 324 tiled rectangles, 171 symmetry-reduced comparisons, 144 whole grid cells, and integer gap floors >=46. The final PREFIX-731 checker preserves these tests under its own name; the scientific data and formulas are unchanged. The frozen scientific pin and earlier certificates remain unchanged.

Do not substitute a numerical plot or sample grid for the certified continuous statement; the result relies on exact rational endpoint inequalities and verified monotone moment ordering.

## Distinction from previous frontier and next unit

PREFIX-728's center-based Lipschitz diamond covered no full 384-grid cell. PREFIX-729/730 already certified and deduplicated an 8×8 cell block. This certificate enlarges direct all-q whole-cell coverage to a 12×12 block by replacing the Lipschitz envelope with monotone moment corners and affine-in-t endpoint comparison.

The next finite task is to reconstruct the exact prior certified-cell union, subtract the overlap of the 144 index pairs, and update the cumulative certified fraction only after that set subtraction. The second route is an adaptive monotone-moment partition to extend the boundary beyond `38<=i,j<50`. Preserve the user-pinned Gamma science and current shared task ownership.
