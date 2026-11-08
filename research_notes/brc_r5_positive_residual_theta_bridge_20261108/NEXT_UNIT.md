# Next R5 exact unit — extend the positive residual C_(4/5) sharp boundary to zero

**Frozen scientific pins:** Global `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Source author-side, still unreviewed.

## Verified results not to rerun

- PR #1803: for all real `0≤t≤1/5, 0≤p,q≤1, 0≤theta≤3/4, kappa=3/4`, exact seedless Blackwell equivalence on chart `C_(3/4)`.
- Current PR #1804: stronger verified all-real `t∈[369/43076,1/5], p,q∈[0,1], theta∈[3/4,1], kappa=3/4` on common chart `C_(4/5)`; 16 exact rational endpoint kernels, 158 positive edges and 601 Fraction exact interpolations.
- **Sharp fixed-face obstruction:** on the explicit corner `p=0,q=1,theta=3/4`, all lawful targets on `C_(4/5)` satisfy `L(y)≥0`, while `L(x)=-369/128000+(10769/32000)t`. Thus no C4/5 solution for `t<369/43076`; this is an exact scoped separator. The endpoint is attained by an 11-edge rational kernel.
- Combining both author-side theorems covers both signed residuals for `t∈[369/43076,1/5], p,q,theta∈[0,1]` at fixed `kappa=3/4`.

## Smallest open mathematical unit

The remaining **small-t positive residual gap** is `0<t<369/43076` with `theta>3/4` (and full side capacities `p,q∈[0,1]`). At `t=0` the source is itself seedless on `C_(3/4)`; the new C4/5 separator excludes only a fixed chart, not a global seedless representation.

Next discriminating experiment: seek exact rational transportation kernels for `t=1/120` on a chart `C_tau` with `tau∈[3/4,4/5)` at `p,q∈{0,1}`, `theta∈{3/4,1}`. Determine whether the same chart handles all eight corners for a t-interval. If yes, construct a multi-chart nonnegative interpolation bridge; if no, obtain a **specific chart-scoped** rational dual/Farkas inequality. Preserve seven node masses, likelihood-weighted columns and both stops in every step.

Native activity `RA-25D3E492799088B30BBD4A1B`; Researcher-ID `EM-DIRECT-D41404`. Real TASK CLAIM, protected Result/Review, mathematical admission not established.
