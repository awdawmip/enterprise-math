# PREFIX-738-R6 — 612 exact Gamma exclusions in the next left band; repaired frozen-kernel digest assertion

Date: 2026-11-13 (Asia/Shanghai). Researcher: `EM-DIRECT-371506`; native activity: `RA-3A89DCF7FDB0716C38B20462`.
Parent: PREFIX-675, frozen 189-row BRC stopped-count **independent-Gamma auxiliary observer**. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. This note does not change P000, native X6 or the scientific pin.

## Exact theorem (continuous cell interiors and boundaries)

Set `Y=max(T_p,T_z)`, `mu=E Y`, `M2=E Y²`, `W=M2-mu²`, `V_q=q²W-q mu`, and the fixed witness `e=(0,73/500)`. Let `R_{ij}=[i/384,(i+1)/384]×[j/384,(j+1)/384]`.

For **every real `q>=2`**, for all `(p,z)` in the 306 closed cells with `40<=i<58`, `79<=j<96`, and in the 306 transposed cells, the following strict inequality holds:

```
V_q(e)-V_q(p,z) > 20*q*q > 0.
```

Thus each of these 612 complete parameter cells excludes global maximizers of this exact auxiliary Gamma objective.

## Calculation proof

The frozen `PREFIX731_R6_MONOTONE_MOMENT_TILE.py` kernel constructs 189 survivor tails from the width predicate and proves coordinatewise monotonicity of `mu` and `M2`. Its exact Gamma-pair cross-kernel is `c[n,m]=binom(n+m,n)/2^(n+m+1)`. For a rectangle `R=[a,c]×[b,d]`, let `L=mu(a,b)`, `U=M2(c,d)-L²`, and witness mean and variance `mu_e,W_e`. The normalized gap obeys

```
[V_q(e)-V_q(p,z)]/q²
 >= W_e-U - t*(mu_e-L),  t=1/q ∈ (0,1/2].
```

It is therefore bounded below by the endpoint minimum

```
G(R)=min(W_e-U, W_e-U-(mu_e-L)/2).
```

For each of the 306 cells split both axes at the exact midpoint and calculate all four `G` values using Python `Fraction`. Each of the 306 four-piece minima is **strictly greater than 20**. The least integer floor of `10^6 G` is **23,100,177**, attained at `(i,j)=(40,79)`. Hence every point of every closed cell satisfies the theorem.

Row minima for `j=79,...,95`, in order, of `floor(10^6 G)` are:

```
23100177 25666322 28522867 31648103 35019735 38615165
42411756 46387080 50519140 54786572 59168811
63646250 68200362 72813804 77470499 82155704 86856046
```

The 306 upper cells are strictly off-diagonal. Pair symmetry yields 306 further distinct transposed cells.

## Geometric union and historical overlap

For each upper cell, the original `PREFIX712` all-q witness `(0,3/20)` gives a nonpositive 384-cell *unrefined* envelope, which also prevents the containing 192-parent envelope from certifying it under the same all-q criterion. Exact original immutable GitHub JSON sets for `PREFIX713` coupled and multicompetitor, `PREFIX716` and `PREFIX718` were fetched and intersected with all 612 coordinates: **zero intersections**. The index rectangles for `PREFIX733-A/B`, `PREFIX735`, `PREFIX736` and `PREFIX737` are disjoint.

Consequently, relative to the PREFIX-737 author-level union, this exact criterion adds 612 distinct cells:

```
140592+612 = 141204,
141204/147456 = 11767/12288 = 95.7600911458333...%,
147456-141204 = 6252 unexcluded cells.
```

The 6252 unexcluded cells are a certificate-coverage remainder, not a claim that maximizers exist there.

## Material reproduction repair

The checked-in `PREFIX731_R6_MONOTONE_MOMENT_TILE.py` had a malformed **54-character** expected SHA256 string for `center_W.numerator`; the mathematically recomputed digest is the full **64-character**
`e4bd76b871f468d154f971a4cc69371fa21fad5bee103be950554fe83d7ea03c`.
The other three frozen moment digests matched. Only that assertion literal was corrected at `main@32f7fde1a3e85ab1c71571fe9c54ab5c25141d55` and independently read back, without changing recurrence or gamma formulas. Prior composite scripts importing the uncorrected module would have failed at this assertion even with correct arithmetic.

## Executed checks, exact limits and next question

Nine bounded local batches reconstructed the same 9529 nonzero survivor count positions, passed the corrected four SHA256 moment assertions, and tested **all 306 exact rational quarter-cell certificates**. Independent connector reads of four original GitHub JSON source files verified the stated empty historical intersections. The checked-in combined `PREFIX738_R6_GAMMA_LEFT_BAND_612.py` is a replayable checker of all 306 cells, reflection, historical-source overlap and total union; **its complete original-dependency end-to-end execution remains pending**. This is author-level exact mathematics, not an independently reviewed/admitted Result.

Next: run that composite checker against all exact source files, then move to `j>=96` and/or adapt the witness to reach the remaining 6252 fine-grid cells. Do not repeat the finished 306-cell rational scan unless the source input or proof obligations change.
