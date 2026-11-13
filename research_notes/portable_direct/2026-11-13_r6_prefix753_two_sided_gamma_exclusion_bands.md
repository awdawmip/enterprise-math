# PREFIX-753-R6 — Two-sided continuous Gamma exclusion bands and the remaining offset corridor

Date: 2026-11-13 (Asia/Shanghai). Parent: PREFIX-675; predecessor: PREFIX-752-R6.
Researcher-ID: `EM-DIRECT-AF1024`; Activity-ID: `RA-48AA52AC279B6CA46156238F`.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Evidence status: **AUTHOR COMPUTED FULL GRID WITH CERTIFIED ERROR ASSUMPTIONS AND INDEPENDENT EXACT FRACTION SPOTS / UNREVIEWED / NOT ADMITTED**.
The two-parameter Gamma(max) observer is an **external auxiliary** statistical model, not a native X6 plane or complete three-dimensional slice.

## Question

PREFIX-752 corrected the full historical author certificate union through PREFIX-749 to 140662 of 147456 original fine cells. That source-level geometric count (95.39252387152778...%) still leaves 6794 fine cells uncertified. Instead of continuing to add duplicate physical cells, determine a geometric **continuous parameter region** that cannot contain any maximizer of the frozen Gamma objective for any real `q>=2`.

## Exact scientific definitions

Let `D=[0,1/2]^2`, and let `Y(p,z)=max(T_p,T_z)` be the maximum of two independent conditional Gamma completion clocks based on the frozen 189-layer BRC stopped-survivor law. Let
`mu(x)=E[Y(x)]`, `M2(x)=E[Y(x)^2]`, `W(x)=M2(x)-mu(x)^2`, and
`V_q(x)=q^2 W(x)-q mu(x)`.
Use the original fixed feasible competitor `e0=(0,3/20)`. For indices `0<=u,v<384`, the closed fine cell is
`F_uv=[u/768,(u+1)/768] x [v/768,(v+1)/768]`, with lower and upper corners `a,h`. The original PREFIX-712 sufficient comparator is

```text
G_uv = W(e0) - M2(h) + mu(a)^2 - max(0, (mu(e0)-mu(a))/2).
```

By the frozen clock stochastic ordering, `mu(x)>=mu(a)` and `M2(x)<=M2(h)` for `x in F_uv`; therefore

```text
[V_q(e0)-V_q(x)]/q^2 >= G_uv        (all x in F_uv, all real q>=2).
```

This follows because the exact lower comparison is affine in `t=1/q in [0,1/2]` and `G_uv` is its minimum over both endpoints.

## Theorem 753.1 — a certified near-diagonal band

**For every real `q>=2` and every `(p,z) in D` with `|p-z|<=17/256`,**

```text
V_q(e0) - V_q(p,z) > (3/4) q^2 > 0.
```

The complete lattice band `|u-v|<=51` has `384 + 2 sum_{d=1}^{51}(384-d)=36900` fine cells. The full old-witness G matrix computed from the immutable 189-layer integer survivor recurrence has minimum binary64 value

```text
min_{|u-v|<=51} G_uv = 0.7664868306305976
at (u,v)=(55,106), and transpose.
```

PREFIX-752 published a uniform absolute binary64-to-exact error enclosure below `1/100` for *all* original G entries under its explicit IEEE-754 input/BLAS assumptions. Consequently the exact rational minimum is strictly above `0.7664868306-0.01>0.75`. The stated continuous band is contained in the union of the certified **closed** cells: away from boundaries a point with `|p-z|<=51/768` has indices differing by at most 51, and at a grid-boundary equality point an adjacent certified closed cell supplies coverage. The old endpoint inequality proves the result.

## Theorem 753.2 — a certified large-offset band

**For every real `q>=2` and every `(p,z) in D` with `|p-z|>=57/256`,**

```text
V_q(e0) - V_q(p,z) > (29/10) q^2 > 0.
```

The complete outer lattice band `|u-v|>=171` has

```text
2 sum_{d=171}^{383}(384-d)=45582
```

fine cells. Its full-grid binary64 minimum is `2.990905434524393`, located at `(0,171)` and its transpose. The same independent uniform error enclosure gives exact G strictly above `2.9909054345-0.01>2.9`. The union of the corresponding closed cells covers every point with `|p-z|>=171/768=57/256`, including threshold boundary points.

The two lattice bands are disjoint and certify `36900+45582=82482` original fine cells without relying on the later competitor certificates.

## Corollary 753.3 — a continuous localization for ALL global maximizers

For every fixed real `q>=2`, continuity of `V_q` on the compact square D ensures at least one global maximizer. The two theorems imply **every** global maximizer `x=(p,z)` must satisfy the strict corridor inequality

```text
17/256 < |p-z| < 57/256.
```

Thus no global optimum can occur on the diagonal `p=z`, within the entire near-diagonal strip, or in the outer corner-offset bands. This is an exclusion/localization theorem for the **auxiliary Gamma(max) problem only**, not an assertion about the native X6 dynamics or the true solution inside the corridor.

The complete PREFIX-752 author-level combined union also leaves 6794 fine cells uncertified. Since the exact original old-witness mask already certifies all 384 diagonal fine cells and the Gamma observer is invariant under exchanging p and z, these unexcluded fine cells form 3397 off-diagonal swap-pairs, **conditional on the PREFIX-752 full historical support count**. The corridor is a geometric constraint; it must not be confused with the much smaller 6794-cell source-ledger complement.

## Sharpness of the *old sufficient test*, not of the actual optimizer

In the full old-G scan, 51 is the largest integer `K` for which **every** fine cell with `|u-v|<=K` passes `G>0`: at offset 52, cell `(49,101)` has exact `floor(10^6 G)=-576380`. Similarly, the outer band begins at 171 because `(0,170)` has exact `floor(10^6 G)=-681635`. A negative G means this specific monotone-corner certificate is insufficient; it is **not** a counterexample to the true comparison, and does not show an optimizer lies on either boundary.

The extremal positive cells were independently evaluated in Python's exact `fractions.Fraction` arithmetic using the original frozen 189-layer kernel:

| Original fine cell | Exact floor(10^6 G) | Role |
|---|---:|---|
| (55,106) | 766486 | Near-diagonal band minimum |
| (0,171) | 2990905 | Outer band minimum |
| (49,101) | -576380 | First failing diagonal offset 52 |
| (0,170) | -681635 | Last failing outer offset 170 |

These are exact rational-sign regressions; the **whole-band** bounds rely on the separately stated certified binary64 error enclosure from PREFIX-752, not just on the four sample cells.

## What was actually executed

An independent local Python/NumPy run rebuilt the exact frozen 189-layer survivor count recursion (9529 nonzero entries, empty final row), formed the entire original `384x384` G array, reproduced `|O712|=137168`, tested the whole integer-offset strips, and found the displayed two global band minima. A second independent standard-library Python process evaluated the four exact Fraction G values and confirmed their integer microfloors. Both actually executed in this research turn.

The accompanying published checker `PREFIX753_R6_TWO_EXCLUSION_BANDS_CHECK.py` composes the published PREFIX-752 full scan with the PREFIX-741 exact kernel and reruns the spot/band assertions; it **has not yet** been separately executed in a fully assembled checkout with its complete source dependencies. The exact results and source pins are in `PREFIX753_R6_TWO_EXCLUSION_BANDS_RESULTS.json`.

The prior Gamma analytic model, original coordinatewise stochastic order and PREFIX-752 all-sign binary64 error proof have **not** received an independent Driver mathematical review. Evidence status remains **AUTHOR / UNREVIEWED / NOT ADMITTED**. Source publication does not confer a shared CLAIM, formal Result, review, Foundation or P000 change.

## Next concrete research unit

1. Assemble and execute the complete published PREFIX-752/753 checkers and their pinned JSONs together; independently examine the PREFIX-752 error bound, especially the stated matrix multiply and rational input rounding assumptions.
2. Extract exactly the 6794 fine cells outside the real PREFIX-752 historical certified union, fold by coordinate swap to 3397 unordered off-diagonal orbits, and rank contiguous corridor components for new rational witness/coupled-moment certificates.
3. Evaluate one genuinely uncovered cell with exact Fraction multiwitness or moment coupling, then expand only on a successful certificate and count geometric union *after* normalized deduplication. Keep the global optimizer target and its unresolved necessary stationarity/candidate analysis explicit.
