# R5 — Sharp fixed-chart lower ratio and full positive-residual four-parameter prism

**Date:** 2026-11-08. **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Science pins remain frozen:** Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Mathematical model, seven likelihood-ratio nodes, terminal error maps and TP/TQ equations are reproduced in `RESEARCH.md` and `VERIFY.py`. P000 and ACTIVE worldview unchanged.

## Stronger all-real theorem

Set `tau=4/5`, `kappa=3/4`, `g=b=1`, and source
```
x(t,p,q,theta) =
 (1,t,1, (13t/40+1/80)p, t theta/10+27/160,
            (3t/40+21/80)q, t theta/10).
```
**For every real**
```
t in [369/43076, 1/5], p,q in [0,1], theta in [3/4,1],
```
there is a lawful seedless-LR target on one fixed chart
`C_(4/5)={z'=2a'/25, v'-z'=9b'/50}`
and a nonnegative, declaration-independent 7×7 calibrated Blackwell transport. The transport preserves the P/Q seven-node terminal laws, both expected stopping times `TP,TQ` and hence arbitrary seven-node decisions `(eP,eQ,TP,TQ)`, including source-target interpolation with every `h∈[0,1]`.

**The lower endpoint `t*=369/43076≈0.008566254991` is sharp for a common `C_(4/5)` representation of the *entire* physical p,q,theta prism.** In fact, for the explicit corner `(p,q,theta)=(0,1,3/4)`, a lawful target on this same chart matching both stopping times exists **only if `t≥t*`**. An exact Blackwell kernel at `t=t*` establishes attainment of this bound.

The previous theorem in `RESEARCH.md` (t≥1/100) is a corollary and its 16 independently verified certificates remain available as original provenance; the present statement is the stronger result.

## Sharp impossibility below t* on C_(4/5)

Take an arbitrary lawful seedless target `y=(g,a,b,u,v,w,z)` on `C_(4/5)`, and let the physical nonnegative slacks be
```
m4=(g-b)/2 >= 0,
m5=(3a/40)+(21b/80)-w >= 0.
```
Substitution into the exact observer formulas yields the following identity, with all coefficients strictly positive:
```
L(y) := (1759/800)*(TQ(y)-1) - (777/400)*(TP(y)-1)
     = (1081/3200)*a + (491/400)*u + (41/80)*m4 + (143/200)*m5
     >= 0.
```
This identity holds for **every real lawful y on this fixed chart**, regardless of Blackwell support.

For the explicit source `x(t,0,1,3/4)`, exact evaluation gives
```
TP(x)-1 = 35/16 + (9/16)*t,
TQ(x)-1 = 309/160 + (13/20)*t,
L(x) = -369/128000 + (10769/32000)*t.
```
The requirement `TP(y)=TP(x)`, `TQ(y)=TQ(x)` therefore implies
`t ≥ (369/128000)/(10769/32000) = 369/43076`. At `t=1/120` the separator equals `-301/3840000 < 0`: an **exact chart-specific infeasibility witness**, superseding the earlier floating-point LP failure. This negative statement is deliberately scoped to `C_(4/5)`, the explicit source corner, and preserving these stops.

## Attainment and full-real proof by 16 exact certificates

At the sharp endpoint `t=t*`, all eight corners `(p,q,theta)∈{0,1}²×{3/4,1}` have verified exact rational seedless targets and calibrated Blackwell kernels on the same chart (78 positive transport edges). At `t=1/5`, all eight counterparts also have exact rational targets and calibrated kernels (80 positive edges). The **16 complete exact certificates (158 edges)** are encoded losslessly as base64(zlib(UTF-8 JSON)) in `SHARP_CERTIFICATES.zlib.b64`, keyed by `t|p|q|theta`, with explicit rational `target=[g,a,b,u,w]` and nonnegative `edges={"i,j":fraction}`.

The checker `VERIFY_SHARP.py` imports only standard-library `Fraction` and the local common `VERIFY.py` model, decompresses and reconstructs all 16 full 7x7 kernels, independently tests each lawfulness, seedless chart, both measure normalizations, all seven row, column and r-weighted-column identities, and both stopping-time equations. It also checks the separating identity by verifying zero and the five target-chart basis vectors (sufficient for its five-affine-variable algebra), checks the rational corner separator and confirms the exact negative value at `t=1/120`. The checker was actually executed: **16 exact vertices + 601 exact interior regressions passed**, with stdout in `EXACT_SHARP_OUTPUT.txt`.

For an arbitrary real interior source let `s=(t-t*)/(1/5-t*)` and `v=4(theta-3/4)`. Every coordinate of `x(t,p,q,theta)` is separately affine in `t,p,q,theta`. Using the 16 product weights
```
W_e=(s if t_e=1/5 else 1-s)
    *(p if p_e=1 else 1-p)
    *(q if q_e=1 else 1-q)
    *(v if theta_e=1 else 1-v)
```
gives `x=sum_e W_e*x_e`, `y=sum_e W_e*y_e` and `Q=sum_e W_e*Q_e`. All weights are nonnegative and sum to 1, and the fixed chart, physical inequalities, Blackwell transport equations and stopping observers are affine. Thus the 16 exact corners yield a **proof for all real parameters including irrational values**. The 601 interior checks verify implementation, not the logical coverage.

Together with the previous exact author-side `theta∈[0,3/4]` theorem in Draft PR #1803 (on C_(3/4)), the full range
`t∈[369/43076,1/5]`, `p,q,theta∈[0,1]`, fixed `kappa=3/4`
has a two-chart four-dimensional seedless equivalence construction for both signs of residual `R=9t(theta-3/4)/10`.

## Provenance and next unit

BRC observer: REUSE_APPLIED; existing r-weighted transport law used unchanged, retaining joint node information rather than only scalar error rates. Discovery LP used SciPy HiGHS; final mathematical certificates are **exact rational** and independently checked without SciPy.

GitHub identity: awdawmip. Native Researcher-ID: `EM-DIRECT-D41404`, activity `RA-25D3E492799088B30BBD4A1B`; no active Task CLAIM or independent mathematical acceptance asserted. The activity registration is canonical-main; source evidence is a Draft research PR.

**Next:** close `0<t<369/43076` for `theta>3/4` via a different chart or explicitly parameter-dependent chart switching; at `t=0` the source is seedless on `C_(3/4)`. The new exact C_(4/5) separator guides which chart must change. A global impossibility argument would have to exclude all lawful seedless representations, not just `C_(4/5)`.
