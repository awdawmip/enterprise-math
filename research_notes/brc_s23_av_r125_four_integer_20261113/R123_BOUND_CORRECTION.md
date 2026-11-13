# R123 predecessor correction — constant integral affine phase

Date: 2026-11-13. Correction to R123's stated finite floor bound, not a new Task CLAIM or independent mathematical review.

## Exact counterexample

R123 `PROOF.md` at `c5e7cb5aaa31be2d12f261c9efd6db9e5563fc9c` claimed that for affine `f(theta)` on open `(l,h)`, `floor(min(f(l),f(h))) <= floor(f(theta)) <= ceil(max(f(l),f(h)))-1`.

Set `x=0,N=j=a=0,c=1,d=1,m=2,I=(0,1)`. Then `Y_0=x+(N-j)theta=0` identically. The claimed n range is `0<=n<=-1`, which is empty, but the true `n=floor(Y_0)=0`. Moreover the positively directed half-open S23 arc is `[0,theta)` for every `theta in (0,1)`, and `{Y_0}=0` is inside while `{Y_1}={theta}=theta` is excluded. Thus the exact joint signature is `(1,0)` for the **whole** open interval.

The published original `check_r123.py` reconstructed from the earlier R123 research bundle returned all four bit signatures with `count=0`, including the actually attained `10`. A direct witness is `theta=1/2`. This is a false-negative in the original bounded-n feasibility enumeration for the declared rational-x model. It does not undermine the separate bounded rational polygon floor-sum lemma.

## Localized mathematical repair

For any affine `f(theta)=u theta+v` with rational coefficients and `theta in (l,h)`, continuity and monotonicity give

`min(f(l),f(h)) <= f(theta) <= max(f(l),f(h))`.

Therefore the **uniform safe integer-floor enclosure** is

`floor(min(f(l),f(h))) <= floor(f(theta)) <= floor(max(f(l),f(h)))`.

The upper endpoint may be unattained, but is eliminated by the original strict parameter and phase inequalities. The enclosure is always finite and has bit length polynomial in input size, so it preserves R123's asymptotic reduction after replacement. A sharper `ceil(max)-1` bound remains valid when the affine function does not attain its maximum on the open interval, notably for nonzero slope, but it is not safe for a constant integral function.

For the R123 Python checker, replace exactly two expressions at original lines 189–190, according to the included `fix_r123_floor_bounds.patch`. The conservative `floor(max)` form is used for both `n` and `k`; this is valid regardless of whether `d` is zero. Here `d!=0` already assures k's earlier bound was safe on nonempty open gaps, but updating it maintains one uniformly correct convention.

## Regression evidence

With original R123 source, the example output is `{'10': {'count':'0', 'theta':None, 'chunks':2}}`. With the two-line patch, `{'10': {'count':'1','theta':'1/2','chunks':2}}`, and all other bit pairs remain empty. The corrected original R123 full test routine was **actually executed** and returned `R123_FLOOR_SUM_LATTICE_PASS`, including 1,500 floor-sum comparisons, 800 random integral polygons, 450 rational-polygon comparisons, and 680 small signed S23 signature queries. A minimal machine-readable record is `verification_r123_correction.json`.

The R125 exact four-integer verifier uses the safe bound and also cross-checks 30 signed small cases and 10 huge signed forward identities. The predecessor correction and successor mathematics remain separate from any formal Result/Review acceptance.

## Recovery

When an execution consumes the R123 source, apply this two-line correction before using the generic affine-floor enumeration, and add the constant-integral test as a focused regression. Do not rewrite the original immutable R123 commit.
