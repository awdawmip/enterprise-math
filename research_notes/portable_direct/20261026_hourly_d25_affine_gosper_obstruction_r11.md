# D25/LIFT — sharp obstruction to a uniform affine Gosper certificate

**Date:** 2026-10-26. **Parent:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged.

**Evidence state:** `AUTHOR-DERIVED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`. Exact algebraic proof below; no native Source checkpoint, experiment, independent review or completion of the original all-target-prime congruence.

## Exact unanswered step from the preceding new Green/adjoint unit

The new note `20261026_hourly_d25_green_hypergeometric_adjoint_r11.md` proves a causal Green/adjoint port and the quadratic outer-rank antidifference, while preserving a nonzero signed Abel residual. The first possible oversimplification would be to seek a *single first-order rational antidifference* for the outer corrected middle-rank source with the original affine rank weight. We now determine rigorously whether such a prime-independent rational certificate exists.

For `p=6m+1`, the corrected middle-rank source `v_j=a_j 2^{-j}` satisfies

[
\frac{v_{j+1}}{v_j}=\frac{(j-m)(j-2m)}{2(j+1)^2}\quad (m+1\le j<2m).
]

Because `m=(p-1)/6=-1/6` in `F_p`, its uniform characteristic-zero rational lift of the one-step ratio is

[
\boxed{r(x)=\frac{(x+1/6)(x+1/3)}{2(x+1)^2}\in\mathbb Q(x).}\tag{1}
]

This is a *model for a uniform certificate ansatz*, not an equality between full rational source values and their canonical mod-p lifts.

## Theorem I — affine scalar Gosper obstruction (new)

For any rational constants `A,B` not both zero, the rational difference equation

[
\boxed{r(x)R(x+1)-R(x)=Ax+B}\tag{2}
]

has **no solution** `R(x)\in\mathbb Q(x)`.

Equivalently, the characteristic-zero uniform ratio (1) has no rational one-step Gosper certificate for *any nonzero affine weight*. In particular, taking `Ax+B=6x+1-6\ell` for a fixed symbolic rank `\ell` cannot give such a certificate over `\mathbb Q(\ell)(x)` either: its linear coefficient is 6 and the identical argument applies after extending the constant field to `\mathbb Q(\ell)`.

**Proof.** Work over an algebraic closure of the constant field, so every putative rational pole can be analyzed on its integer-translation orbit `\alpha+\mathbb Z`. The only finite pole of `r` is `x=-1` (order two); its only zeros are `-1/6` and `-1/3`. These three points lie in *distinct integer-translation orbits*.

Suppose that `R` has a pole in an orbit not containing `-1`. Select the rightmost pole `\alpha` of `R` within that orbit (the set is finite). At `x=\alpha`, the shifted `R(x+1)` is holomorphic and `r(x)` has no pole, so `r(x)R(x+1)` is holomorphic, while `-R(x)` has a pole. This contradicts the polynomial right side of (2).

It remains to exclude the orbit of `-1`. Select its leftmost pole `\beta`. At `x=\beta-1`, the unshifted `R(x)` is holomorphic while `R(x+1)` has a pole. Here `r(x)` is never zero: the only zeros are in other shift orbits. It may be finite/nonzero or have its own pole, but in either case the product retains a pole. Again (2) is impossible.

Thus `R` has **no finite poles** and is a polynomial. The double pole of `r(x)` at `x=-1` then forces `R(x+1)` to have a zero of order at least two at `x=-1`; equivalently `x^2\mid R(x)`. Therefore any nonzero such polynomial has degree `d\ge2`. Yet at infinity `r(x)=1/2+O(x^{-1})`; if `R(x)=cx^d+\cdots` with `c\ne0`, the left side has leading term `-cx^d/2`. Its degree is `d\ge2`, contradicting the affine right side. The only remaining `R=0` yields `A=B=0`, excluded. QED.

## Sharpness and safe scope

The degree obstruction is **sharp**: the quadratic certificate `R(x)=x^2` gives

[
\boxed{
r(x)(x+1)^2-x^2
=-\tfrac12\left(x^2-\tfrac12x-\tfrac1{18}\right).
}\tag{3}
]

The quadratic weight in (3) is the mod-p specialization of `W_j=j^2+3mj-2m^2` in the preceding Green/adjoint note. That note also proves its contraction with the true signed observer `K_j` produces a boundary **plus a bulk residual**, not a boundary-only result; the residual is `12 mod 13` for `p=13`.

**Precise limitation.** Theorem I is a statement over characteristic-zero `\mathbb Q(x)` (or `\mathbb Q(\ell)(x)`) with a *fixed uniform rational certificate*. It does **not** rule out a different `p`-dependent rational/interpolation certificate in `\mathbb F_p(x)`, a higher-order/2D WZ certificate, or a combination involving the full corrected Clausen differential operator, source normalization or original CM data. It is not a proof that the D25 hard congruence fails.

**BRC:** `COMPOSE_APPLIED`; precisely the `v_j` source and future signed affine-rank observer are declared, the nonexistence applies only to a narrow scalar rational quotient, and the proved nonzero Abel residual prevents unjustified disappearance of signed branch data. P000 and the frozen scientific source pin are unchanged.

**Next executable mathematics:** search for a *coupled second-order or bidirectional* WZ/adjoint syzygy using the predecessor's equations (4)–(9) and the corrected Clausen operator, rather than repeating a first-order rational affine Gosper ansatz. Preserve endpoint/source ranks, proof strength and actual original CM experimental欠项. Any native role-bound execution still requires fresh canonical continuation, own winning CLAIM/open and Source durable checkpoint; this portable note grants none.
