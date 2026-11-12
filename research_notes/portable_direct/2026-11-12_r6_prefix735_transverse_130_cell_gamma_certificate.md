# PREFIX-735-R6-TSTRIP — 130 new complete Gamma cells by a transverse strip

**Date:** 2026-11-12 (Asia/Shanghai)  
**Mother question:** PREFIX-675, global maximum of the frozen 189-row stopped-count independent-Gamma auxiliary observer  
**Scientific input pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`  
**Status:** AUTHOR_EXACT_FRACTION_CHECKED / SOURCE_FIELD_CROSSCHECK / UNREVIEWED / NOT_ADMITTED

## Theorem

Let `p,z` be the independent Gamma observer parameters in the exact frozen model. Write `mu(p,z)=E[max(T_p,T_z)]`, `M2(p,z)=E[max(T_p,T_z)^2]`, `W=M2-mu^2`, and `V_q=q^2 W-q mu`, for **all real** `q>=2`.

Let `e=(0,73/500)`. For each 384-grid cell `[i/384,(i+1)/384] x [j/384,(j+1)/384]` with

`58<=i<70` and `70<=j<76`,

and for each reflected cell obtained by exchanging the two coordinates,

```
V_q(e)-V_q(p,z) > q^2 / 20.
```

The 72 upper-strip cells (and their 72 transposes) are therefore certified to exclude global maxima, for every real `q>=2`.

## Exact proof

For any closed rectangle `R=[a,c]x[b,d]`, reuse the original kernel's coordinatewise nondecreasing mean and second moment. Define

```
mu_low=mu(a,b)
U=M2(c,d)-mu_low^2
Delta_0=W(e)-U
Delta_half=Delta_0-(mu(e)-mu_low)/2.
```

For `t=1/q` in `(0,1/2]`, monotonicity gives `W(p,z)<=U`, `mu(p,z)>=mu_low`, and therefore

```
[V_q(e)-V_q(p,z)]/q^2
  = W(e)-W(p,z) - t*(mu(e)-mu(p,z))
 >= Delta_0 - t*(mu(e)-mu_low)
 >= min(Delta_0,Delta_half).
```

The last inequality is exact because the expression is affine in `t`. All calculations use `fractions.Fraction` and the original exact integer survivor kernel; no floating point decides any test.

For 7 of the 72 cells, the full-cell envelope already exceeds `1/20`. In each of the remaining 65 cells, subdivision into four 768-grid subcells produces four strict envelopes, each exceeding `1/20`. The least observed lower margin has integer floor **50,520 after multiplication by 1,000,000** (actual worst cell: `(68,74)`), so the uniform rational `1/20` bound holds. A separate 189-row reconstruction checked 9,529 nonzero survivor entries and matched the center and comparator numerator SHA-256 digests used in PREFIX-731.

Symmetry `mu(p,z)=mu(z,p)`, `M2(p,z)=M2(z,p)` transfers the strict result to reflected cells.

## Historical certificate union and exact count

Within the 72 upper-strip cells, the earlier `PREFIX-712` witness `e_0=(0,3/20)` has a positive full-cell all-q endpoint test on exactly these 7 cells:

```
(68,74), (68,75),
(69,71), (69,72), (69,73), (69,74), (69,75).
```

They and their transposes are already in the old certified union. The other **65 upper-strip cells** have neither the prior `PREFIX-712` exact full-cell certificate nor an intersection with the actual `PREFIX-713` coupled/multicompetitor, `PREFIX-716`, and `PREFIX-718` explicit certificate sets. The source JSON records for these four later families were fetched and their exact coordinate sets checked; all intersections are empty.

The strip also lies entirely outside PREFIX-733-A `[30,58)^2` and PREFIX-733-B `[50,70)^2` in grid index coordinates, hence it does not duplicate the new PREFIX-734 union. Since all upper-strip indices satisfy `i<j`, the 65 reflected cells are distinct from the 65 upper cells.

Thus, conditional only on the inherited author-grade historical union tally `C_734=139980` and its exact original cell-set descriptions:

```
new = 2*(72-7) = 130;
C_735 = 139980+130 = 140110;
C_735 / 384^2 = 70055/73728 = 95.01817491319444...%;
uncertified grid cells = 147456-140110 = 7346.
```

These are complete continuous 384-grid cell exclusions and count only genuinely new coordinates. The result is a two-parameter auxiliary Gamma optimization statement; no native six-axis dynamical lifting is asserted.

## Evidence and validation scope

1. Frozen kernel: `PREFIX731_R6_MONOTONE_MOMENT_TILE.py` at the scientific pin, 189 survivor rows, 9,529 nonzero integer positions, matching old numerator checks.
2. New author exact calculations: 72 upper cells, 65 exact 2x2 subdivisions, full rational `>1/20` lower margins. A local reimplementation of the same recurrence and pair formula executed these checks; the computation returned `GAMMA_CORE_PASS 72 7 130 65`.
3. Historical set checks: current GitHub connector fetched `PREFIX713_R6_RESULTS.json`, `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json`, `PREFIX716_R6_RESULTS.json`, and `PREFIX718_R6_RESULTS.json`, and separately checked all 130 proposed coordinates against their source-defined sets. Overlaps were zero. The PREFIX-712 old witness endpoint comparisons gave the 7 listed cells.
4. [Published full composite checker](PREFIX735_R6_TRANSVERSE_STRIP_130.py) and [130-coordinate result JSON](PREFIX735_R6_TRANSVERSE_STRIP_130_RESULTS.json). At publication, the published full composite program has **not yet** been rerun end-to-end against a complete local checkout of its four historical JSON inputs. Separate mathematical kernel and exact source-field validations were executed. The subsequent complete run remains a reproducibility task, not an assumed fact.
5. Author evidence only. No independent mathematical review, formal Result or Foundation admission.

## Next scientific unit

Expand from the transverse strip along `j>=76` and toward `i<58`, using adaptive rational moment envelopes rather than a fixed square, and test actual new coordinate differences against the full historical union. Run the published composite checker using the original remote JSONs, then verify a formal task link/claim before any shared Result mutation. Preserve the frozen scientific pin.
