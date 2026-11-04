# R5 K3 — uniform superdiagonal clock, heterogeneous error-fiber theorem

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific pins (preserved, not refreshed): GLOBAL_KNOWLEDGE_V1 `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current governing rules independently read from the canonical main entries. Direct predecessor: `research_notes/brc_r5_k3_supercritical_alpha_nu_rigidity_20261104_t0735/RESEARCH.md` at `5895ab8bbbb528c047d7b1822bb7755311fe2295`. This is an auxiliary finite-source BRC observation model. P000 / ACTIVE worldview unchanged; no native X6 physical embedding claimed.

## Model

Let sources S=(C,I,BJ,IJ), with strictly positive capacities
`c=(1/8,1/6,1/16,3/32)`, `Ctot=sum c=43/96`.
FULL has upstream `0<=x,y<=1`, `0<=i<=1-x`; seedless LR has `i=(1-x)y`. Actual source weights are
`w=(1/8,(1-x)/6,y/16,3i/32)`, with `d=w_BJ+w_IJ`.
FULL independently chooses each source stage from {0,1,2,3}; LR shares one common stage, in the deterministic reduction. Behavioral stage transitions use `M_s=w_s z_s`, `Z_s=(2/3)M_s t_s`, `U_s=Z_s u_s`. The four observers are
```
eP = 107/128 - 21*x/128 + d/4 - sum(Z)/2 + sum(p_s*Z_s)/8
eQ =  13/64 +  3*x/64  - d/2 + sum(Z)/8 + sum(q_s*Z_s)/32
TP = 3 + sum(M) + (3/2)sum(Z) + r*sum(U)
TQ = 3 + sum(M)/2 + (3/8)sum(Z) + (v/4)sum(U).
```
Here `0<r<v<1` are common to all four sources and each `p_s,q_s in (0,1)` is independent. For every legitimate real behavioral strategy the observer map is multi-affine after the upstream substitutions, so each compact convex hull equals that of its 1,536 FULL or 16 LR deterministic vectors. The upstream FULL vertices are (x,y,i) with (x,i) among (0,0),(0,1),(1,0) and y in {0,1}; the LR upstream corners are (x,y) in {0,1}².

## Theorem: all-real exposed-error-fiber rigidity

For every `0<r<v<1` and all independent real `p_s,q_s in (0,1)`:

**If the full four-dimensional convex observation hull of FULL equals that of seedless LR, then `p_C=p_I=p_BJ=p_IJ` and `q_C=q_I=q_BJ=q_IJ`.**

More precisely, whenever at least one terminal probability family is heterogeneous, there exists an explicit FULL deterministic observation lying outside the entire LR convex hull, hence a strict real four-dimensional support separator. This is a necessary classification; homogeneous terminal probabilities are the next sufficiency question.

## Complete proof

Define
```
nu=(3+2*v)/(4*(3+2*r)),   A=1+2*r/3,   Ctot=sum_s c_s,
pbar=sum_s(c_s*p_s)/Ctot, qbar=sum_s(c_s*q_s)/Ctot.
```
Since `v>r` and `v<1`, `1/4<nu<1/2`. On the clock normal
`n0=(0,0,-nu,1)`, the per-unit-capacity stage gains relative to the baseline `3(1-nu)` are
```
g0=0, g1=1/2-nu>0,
g2=3/4-2*nu <g1,
g3=(3/4+v/6)-(2+2*r/3)*nu=g1.
```
The last equality follows by definition of nu, and `g2<g1` follows from nu>1/4. Thus the unique clock-maximizing upstream variables are `x=0,y=1,i=1`, because at either maximizing stage 1 or 3 every source contributes its strictly positive capacity. FULL may select stage 1 or 3 independently at each source. LR has exactly two clock-maximizing deterministic observations, `H1` (all stage 1) and `H3` (all stage 3). Its *entire four-dimensional exposed face* is the line segment `[H1,H3]`.

For any source j, choose the FULL stage vector with stage 3 at j and stage 1 at every other source, keeping upstream `(0,1,1)`. Denote its genuine observation by `W_j`. In both clock coordinates,
```
(TP,TQ)(W_j) = (TP,TQ)(H1) + (c_j/Ctot)*[(TP,TQ)(H3)-(TP,TQ)(H1)].
```
Indeed, the 1→3 clock increment per unit source capacity is the fixed vector `(A,1/4+v/6)`, with strictly positive first coordinate `A`. Therefore any point in the LR exposed face with the same TP as W_j is uniquely `H_j^mix=H1+(c_j/Ctot)*(H3-H1)`.

The error increments 1→3 per unit source capacity are `((p_s-4)/12,(q_s+4)/48)`. Direct substitution gives the **exact error-fiber residual**
```
W_j - H_j^mix =
(c_j*(p_j-pbar)/12, c_j*(q_j-qbar)/48, 0, 0).          (★)
```
If either p or q varies across sources, some j differs from its corresponding strictly positive weighted mean, so (★) is nonzero. Were W_j in the LR four-hull, n0 would expose its LR representation, restricting that representation to [H1,H3]. Matching TP forces precisely H_j^mix, contradicting (★). Therefore W_j lies outside the LR convex hull. Both hulls are finite polytopes, so strict real linear separation follows. This proof establishes the theorem for every declared real parameter, rather than by finite sampling.

### Explicit mixed-direction separation with a locally exact gap

Let `eps>0` be sufficiently small. Because the deterministic LR clock face contains exactly H1,H3 and there are finitely many other deterministic LR vertices, the following small perturbations leave all other LR vertices strictly suboptimal. The analogous FULL extrema retain the full-capacity upstream choice and stage 1/3 choices (the time gains g1>0 and the strict gap to 0/2 at eps=0 guarantee this in a common neighborhood).

For heterogeneous p, put
```
nP=(eps,0,-nu + eps*(4-pbar)/(12*A),1).
```
All LR clock-face endpoints have equal support under nP, while the FULL incremental gain for source s when changing stage 1 to 3 is exactly `eps*c_s*(p_s-pbar)/12`. Consequently
```
h_FULL(nP)-h_LR(nP) = (eps/12)*sum_s c_s*(p_s-pbar)_+ > 0
```
for all sufficiently small eps. For heterogeneous q, put
```
nQ=(0,eps,-nu - eps*(4+qbar)/(48*A),1).
```
Then
```
h_FULL(nQ)-h_LR(nQ) = (eps/48)*sum_s c_s*(q_s-qbar)_+ > 0.
```
The exact gap is witnessed by stage 3 on sources above their weighted mean and stage 1 on the rest. These formulas are local-in-eps analytic statements, with an explicit numerical eps checked in VERIFY.py for the stated two rational clock kernels.

## Exact Fraction experiments

Inputs `(r,v)=(1/5,2/5)` and `(2/5,4/5)`, terminal profiles `pHet=(1/4,1/3,2/3,3/4)`, `qHet=(3/4,2/3,1/3,1/4)`, and `uniform=(1/2,1/2,1/2,1/2)`. Four p/q combinations per clock kernel: p-only heterogeneous, q-only heterogeneous, both heterogeneous and uniform/uniform. At every configuration, enumerate ALL 1,536 FULL and 16 LR deterministic observations with Python standard-library Fraction. Check the exact clock support equality, exact two-endpoint LR exposed face, all four formulas (★), and the expected presence of nonzero residuals. For each heterogeneous error family, check the exact mixed-support gap at `eps=1/1024`, an actual maximizing FULL deterministic policy, and the Holder `L_infinity` distance lower bound `gap/||n||_1`. Eight models checked. The actual transcript and executable source are `EXACT_OUTPUT.txt` and `VERIFY.py`.

Example: r=1/5, v=2/5, p=pHet and q=uniform. Then `nu=19/68`. With
```
nP=(1/1024,0,-10030121/35930112,1)
```
the exhaustive exact support values are
```
hF=7803358973/3449290752
hLR=7803347005/3449290752
gap=11/3170304
dist_inf_lower=374/137985963.
```
The FULL maximizing policy is `(x,y,i)=(0,1,1)` and stages `(1,1,3,3)`. These are precise finite-model certificate values; the theorem's all-real scope follows from the analytic face proof.

## Research consequence, scope and authority

This establishes the terminal-heterogeneity **necessary condition** throughout the hitherto unclassified `v/r>1` branch. The remaining specific research question is sufficiency for homogeneous p and q, plus the boundary `v=r` and any broader mother-target topology. Sample rational LP evidence for homogeneous cases is exploratory and not promoted to proof. BRC source identities and their four observer contributions are retained; the projected clock observer is used only as a separating-face tool, not as a certified lossless native-state quotient.

Verified GitHub identity: awdawmip, repository admin; Enterprise Math private Sites configured read-only `research_authority_granted=false`. The native owner inventory is currently inaccessible (`CONTROL_QUOTA`). No current Source CLAIM, authenticated Researcher-ID, Result, independent review, or formal admission is asserted.