# X6 R66 — D=5 common-bias positive-BRC tomography: complete error-radius staircase

Date: 2026-11-21 (Asia/Shanghai). Scientific status: CONDITIONAL_EXACT_FINITE_CERTIFICATE / AUTHOR_VERIFIED / NOT_INDEPENDENTLY_REVIEWED.

## Scope and source pins

This work continues the R61–R65 conditional **positive-weighted, independently reset repeated-A AB branch** observer. Each named successful A-Port/B-Port pair is a positive branch; t independent reset trials keep the same named A Port and freely choose t named B Ports. After normalization by known strictly positive branch weights, its total branch count is m_t=Σ_i r_i^t, for t=1,...,5. This is an exact branch-enumeration identity (not amplitude cancellation). Model input is the frozen Enterprise Math P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. The ACTIVE six-dimensional native Cell world, three-force TRIADIC_CLOSURE_E, three-dimensional research slice, and path/source residual fidelity remain unchanged. An actual native event-to-observer embedding is still unverified.

For integer p>=D=5, let c_d>=0 count named A Ports with success degree d∈{0,...,5}, Σc_d=p. Observe y_t=m_t(c)+b+e_t for t=1,...,5, with unknown single common real offset b and |e_t|<=η. The target is the high-degree subhistogram (c_2,c_3,c_4,c_5). Every such degree histogram is realizable in a labelled p×p Boolean success relation when p>=5.

## Theorem — all integer p>=5

The first closed error radius at which two realizable candidates with distinct high-degree targets can produce compatible observed vectors is

\[
\boxed{\eta^*_{p,5}=
\begin{cases}
15/2,&5\le p\le10,\\
6,&11\le p\le25,\\
1/2,&p\ge26.
\end{cases}}
\]

All η<η* guarantee uniqueness of the high-degree histogram. At η=η* exact ambiguous witnesses exist. There are **precisely two downward transition populations**, p=11 and p=26. This completes the D=5 intermediate range left by R65.

## Reduction and exact finite proof certificate

Let a_d=c_d-c'_d for d=2,...,5 and Δ_t=m_t(c)-m_t(c'). Degree-zero and degree-one terms contribute only a shared constant across t>=1. Define z_1=0 and z_t=Δ_t-Δ_1=Σ_{d=2}^5 a_d(d^t-d), t=2,...,5.

An integer difference vector a is realizable at population p iff
\[
q(a)=\max\bigl(\sum(a_d)_+,\ \sum(-a_d)_+\bigr)\le p.
\]
Necessity follows by counting positive and negative high-degree changes. For sufficiency place the positive mass in c, negative mass in c', and fill unused rows with degree-zero Ports; the rows can be realized as actual B-Port subsets because p>=5.

The R64 exact minimax bias quotient gives the ambiguity threshold
\[
\eta_{\rm pair}=\frac14\,\operatorname{osc}(0,z_2,z_3,z_4,z_5),\qquad
\operatorname{osc}=\max-\min.
\]
Every d^t-d is even; therefore every z_t is an even integer. The degree-2 difference a=(1,0,0,0) gives z=(2,6,14,30), q=1, and oscillation 30. Hence only cases with oscillation <30 can improve on 15/2.

Because z_1=0, any such candidate must have z_2,...,z_5 in {-28,-26,...,28}. Thus **all 29^4=707281** integer quadruples cover every possible improvement. The moment difference matrix is
\[
M=\begin{pmatrix}2&6&12&20\\6&24&60&120\\14&78&252&620\\30&240&1020&3120\end{pmatrix},
\qquad\det M=34560.
\]
Its exact inverse, multiplied by 120, is
\[
120M^{-1}=
\begin{pmatrix}
1070&-590&130&-10\\
-780&490&-120&10\\
305&-205&55&-5\\
-50&35&-10&1
\end{pmatrix}.
\]
So a candidate z comes from an integer high-degree difference iff every entry of (120M^{-1})z is divisible by 120. The companion C++ exact inverse verifier iterated all 707281 even quadruples, retained 221550 with 0<osc<30, obtained 116 nonzero integer inverse candidates and the **exhaustive exact minimum Port population** for each possible oscillation:

| Oscillation | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| min q(a) | 26 | 52 | 78 | 104 | 130 | 156 | 182 | 208 | 234 | 260 | 286 | 11 | 63 | 64 |

The independent *forward* C++ verifier enumerated all 53^4=7,890,481 integer a vectors in [-26,26]^4 and checked 1,440,270 nonzero candidates with q<=26. It separately recovered minimum oscillation 30 at p=5..10, 24 at p=11..25 and 2 at p=26. Both complete finite checks PASS. The inverse-domain enumeration proves that no missing smaller-oscillation a vector can exist for any p<=26. For every p>=26, R65's all-D algebraic theorem gives η*=1/2, completing all p>=5.

The finite certificate is exact and exhaustive under the stated domain, not a claim that a finite sample proves all dimensions D. Both executable verifier sources and a results record accompany this paper.

## Realizable, exact ambiguity witnesses

For p=5, take a=(1,0,0,0), c=(4,0,1,0,0,0), c'=(5,0,0,0,0,0). The moment differences Δ_1,...,Δ_5=(2,4,8,16,32), of oscillation 30.

For p=11, take a=(-6,9,-5,1), c=(1,0,0,9,0,1), c'=(0,0,6,0,5,0). The moment differences are (0,2,0,-22,0), of oscillation 24. In particular, this witness generates a new plateau of sharp radius 6 starting at exactly p=11.

For p=26, take a=(20,-15,6,-1), c=(0,0,20,0,6,0), c'=(10,0,0,15,0,1). The moment differences are (14,16,14,16,14), of oscillation 2, giving the final sharp radius 1/2.

Each witness extends to all larger p by adding the same number of zero-degree Ports to both candidates. For any pair, shifting model offsets to center the difference range and assigning opposite channel errors of size ≤osc/4 makes the observations exactly coincide at the bound. All BRC branch weights remain positive.

## Verification, provenance, next question

- Exact C++ inverse verifier: 221550 bounded z checks, 116 integral witnesses; records per-oscillation minimum required Port populations.
- Independent C++ forward verifier: 7890481 signed a combinations, 1440270 feasible at q<=26; checks the complete p=5..26 minima.
- Separate Python named positive-BRC enumeration over all 530 Boolean relation tables with p=1,2,3, at t=1,2,3, confirms 1590 named branch-mass identities. Three integer histogram witnesses checked exactly.
- Predecessor R65 proof: research_notes/portable_direct/2026-11-21_x6_r65_universal_half_radius_plateau.md at commit 60e554e6b93c773f1d315fe6de8106ab4ad796fd. Earlier R61–R64 define the observer, degree quotient, unknown-bias residual and minimax formula.

Scientific limitations: this is a conditional observer theorem with exact finite evidence and R65 analytic extension. There has been no independent mathematical review or formal Result acceptance. No native TRIADIC_CLOSURE_E time-evolution admission, stable cross-experiment Cell/Link/Port reset, or physical time interpretation is inferred.

Next: derive general-D certificates for intermediate plateaus (especially D=6); study unequal *raw* channel noise under positive weights; and establish or refute a provenance-preserving mapping of the named conditional repeated-A observer into frozen-P000 native whole-triad events.
