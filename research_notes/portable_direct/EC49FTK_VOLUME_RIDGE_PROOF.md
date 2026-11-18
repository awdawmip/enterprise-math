# EC49FTK — Exact phase volumes, price-gap ridge and average BRC16943 swap advantage

**Status:** AUTHOR_PROVED (exact rational deduction conditional on prior EC49FTH native Bellman theorem) / EXACT_RATIONAL_REGRESSION / NOT_INDEPENDENT_NATIVE_BELLMAN_RECHECKED / NOT_REVIEWED.

**Date:** 2026-11-19. **Frozen scientific input:** awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

**Verified mathematical parent:** [EC49FTH PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774), commit 999bf1069403306b3813e0e390dae4435d7b4b8c, particularly research_notes/portable_direct/EC49FTH_NATIVE_43_USE_FAN_PROOF.md and EC49FTH_NATIVE_43_USE_FAN_CERT.json. This contribution reuses the parent author-proved global optimal-value formulas, and **does not** rerun the underlying unrestricted Bellman solver.

## Scientific question and native observer scope

Determine exact sizes of the three original-price optimal policy regions, the q140 price discount that maximizes q32/q34-swap advantage at each fixed (a,b), and the uniform-parameter average advantage. The 141 individually named native response profiles, 228 original physical queries and four complete trees keep their provenance from the parent. The three discount parameters are external query prices, **not** P000 spatial Cell coordinates. No original observer or named state has been quotiented out.

The closed, dimensionless price box is

\[
\Omega=[3/4,49/64]\times[7/16,57/128]\times[11/16,3/4].
\]

On this box the parent theorem asserts the exact unrestricted native Bellman values

\[
D=\min\{329-36a-68b-141z,\;334-141a-62b-45z,\;326-141a-47b-43z\},
\]
\[
S=332-141a-8b-105z.
\]

The original-price candidates are called Dmid (141 q140 uses), D45 (45 uses), D43 (43 uses), and the sole swapped-price candidate S105. The following are **exact consequences** of these stated formulas; their validity as claims about unrestricted native trees inherits the parent theorem's evidence status.

## Theorem A — ordered full-dimensional phases

Put

\[
T_{23}(b)=4-\frac{15b}{2},\qquad
T_{12}(a,b)=\frac{105a-6b-5}{96},\qquad
b_c=\frac{53}{120},\quad a_c(b)=\frac{77+6b}{105}.
\]

Throughout the entire box,

\[
T_{12}-T_{23}=\frac{105a+714b-389}{96}
\ge\frac{17}{768}>0,\quad
T_{23}<\frac34,\quad T_{12}>\frac{11}{16}.
\]

Subtracting the respective affine values shows that the **complete optimal-strategy partition**, with intervals clipped to \(\Omega\), is

* D43 for \(11/16\le z<T_{23}(b)\); nonempty exactly when \(b<53/120\);
* D45 for \(T_{23}(b)<z<T_{12}(a,b)\);
* Dmid for \(z>T_{12}(a,b)\); nonempty exactly when \(a<a_c(b)\).

Boundary equalities are native-tree ties. No direct D43/Dmid common facet is active here. The phase ordering is strict wherever two distinct intervals have positive length.

Proof: D45-D43 equals \(8-15b-2z=2(T_{23}-z)\); Dmid-D45 equals \(105a-6b-5-96z=96(T_{12}-z)\). Their order follows the displayed strict separation; below T23 D43 is smallest, between sheets D45 is smallest, above T12 Dmid is smallest. The bounds on T23/T12 follow by checking the box endpoints, with minimal T12 \(4549/6144\) and maximal T23 \(23/32\).

## Theorem B — exact continuous three-dimensional phase volumes

The Lebesgue volume of the price box is \(1/131072\). The exact volumes and their fractions of this box are

| Native D phase | Absolute volume | Fraction of box |
|---|---:|---:|
| D43 | \(1/983040\) | \(2/15\) |
| D45 | \(66581/10569646080\) | \(66581/80640\) |
| Dmid | \(3307/10569646080\) | \(3307/80640\) |

Proof for D43: its b-z section is a right triangle with b-width \(53/120-7/16=1/240\), z-height \(T_{23}(7/16)-11/16=1/32\); it extends through the a-width \(1/64\). Hence \(V_{43}=(1/64)(1/2)(1/240)(1/32)=1/983040\).

Proof for Dmid: at fixed b, a varies from \(3/4\) to \(a_c(b)\), and its z-thickness is \(3/4-T_{12}=(77+6b-105a)/96\). Integrating in a gives \((24b-7)^2/322560\). Therefore

\[
V_{\mathrm{mid}}=
\int_{7/16}^{57/128}\frac{(24b-7)^2}{322560}\,db
=\frac{3307}{10569646080}.
\]

D45 has the complementary volume. These are geometric fractions of **chosen price parameters**. They have no asserted probabilistic interpretation for native states, paths or physical frequencies; a random-parameter interpretation would require an explicit uniform price design.

## Theorem C — unique maximizing q140 discount and saturation plateau

Write \(G=D-S\). Its three phase formulas are

\[
G_{43}=-6-39b+62z,\quad
G_{45}=2-54b+60z,\quad
G_{\mathrm{mid}}=-3+105a-60b-36z.
\]

For **each** allowed fixed pair (a,b), G strictly increases with z across D43 and D45 (slopes 62 and 60), then strictly decreases on Dmid (slope -36). T12 is strictly above the lower face and the D43/D45 switch always precedes it. The **unique** constrained maximizer is thus

\[
\boxed{z_*(a,b)=\min\left\{\frac34,\frac{105a-6b-5}{96}\right\}.}
\]

Its attained value, including consistent equality on the threshold, is

\[
\boxed{\max_{11/16\le z\le3/4}(D-S)=
\begin{cases}
(525a-462b-9)/8,& a\le a_c(b),\\
47-54b,& a\ge a_c(b).
\end{cases}}
\]

For \(a\ge a_c(b)\), the q140-optimized gap becomes independent of a, a genuine **parameter-price plateau** (not a claim of structural invariance of all native trees). This is not a global optimum over unrestricted discount values outside the stated box.

## Theorem D — exact uniform-box average gap

For uniform Lebesgue averaging in the displayed parameter box,

\[
\boxed{\mathbb E_\Omega[D-S]
=\frac{1317531013}{61931520}
\approx 21.27399768324756.}
\]

Proof by partition integration: extend \(G_{45}=2-54b+60z\) over the whole box. Its mean is exactly \(2725/128\). Over D43, its difference from the correct gap is \(8-15b-2z\), giving normalized signed correction \(-1/360\). Over Dmid, its difference from the correct gap is \(96z-105a+6b+5\), giving normalized signed correction \(-152191/12386304\). The exact sum

\[
\frac{2725}{128}-\frac1{360}-\frac{152191}{12386304}
=\frac{1317531013}{61931520}
\]

proves the claim. No sampling approximation is involved.

## Reproducibility and interpretation

See EC49FTK_VOLUME_RIDGE_VERIFY.py, EC49FTK_VOLUME_RIDGE_CERT.json and EC49FTK_RUN_LOG.txt (same directory). The pure-stdlib Fraction program checks the exact rational integration formulas, all three phase inequalities on a 17 x 17 x 17 grid (4913 test points), and the maximum-gap relation on 289 fixed-(a,b) grid pairs plus tested z values. The **continuous proof** rests on the exact affine comparison and integrals above; the finite rational grid is a reproducibility regression, not its substitute.

**Evidence boundary:** no new 228-physical-query Bellman search, no new four-tree replay, no independent raw94 reconstruction, no formal checker, no third-party review, no change to P000, and no Result/CLAIM/Activity success is claimed here. Parent EC49FTH remains AUTHOR_PROVED / NOT_REVIEWED. The present result is a rigorous postprocessing theorem conditional on that parent.

**Next unresolved mathematical question:** locate the first new unrestricted native optimal tree below z=11/16 and test whether the ordered increase/decrease geometry, unique ridge and volume partition persist; separately extend beyond a=49/64 without extrapolating unverified Bellman equalities. Preserve the original 228 observation identifiers and all 141 separately named states.
