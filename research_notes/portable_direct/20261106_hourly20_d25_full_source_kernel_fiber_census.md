# D25 — Full three-source p-adic kernel charts and exact second-digit fiber census

Date: 2026-11-06. Role: TASK_RESEARCH portable author evidence; logical lane label: `chatgpt-research-hourly-enterprise-math-20260923` (configured label, not a platform-issued conversation attestation). The separate maintenance label is not used for role-bound mutations.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication: `TP2-B6F4FC938FF94941C1B7`. Frozen science pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Status: **AUTHOR-DERIVED / EXACT FINITE-FIELD ALGEBRA / EXACT INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

## Precise population, sources and observation

Fix a prime \(p=6m+1\ge7\) and labelled sources \(s=(2m,3m,4m)\). Over \(\mathbb Z_{(p)}\), set
\[
U_j(\mathbf x)=(-1/2)^j\prod_{i=1}^3 {s_i+x_i\choose j},\qquad
F_p(\mathbf x)=\sum_{j=0}^{p-1}(6j+1)U_j(\mathbf x).
\]
The original 216-series direction is \(\mathbf v_*=(-1/3,-1/2,-2/3)\). The observed scalar is \(F_p(p\mathbf v)\bmod p^3\). This is an **auxiliary signed and labelled source observer**, not an original H0/B0, a Frobenius operation or a native dimensional embedding. A separate labelled observation is \(U_1(p\mathbf v)\bmod p^2\). The entire integer binomial-index range is retained.

Let \(A_i=\partial_iF_p(\mathbf0)\bmod p^2\) and \(H_{ij}=\partial_i\partial_jF_p(\mathbf0)\bmod p\). Every denominator \(j!\), \(j<p\), and 2,3 is a \(p\)-adic unit. The following theorem applies when at least one \(A_i\not\equiv0\bmod p\).

## Theorem A — canonical-by-rule p-adic kernel lift

Choose the **first** index \(r\in\{1,2,3\}\) with \(A_r\not\equiv0\bmod p\), and denote the other two indices in increasing order by \(u,w\). Define two source-labelled vectors \(b_u,b_w\in(\mathbb Z/p^2)^3\) by
\[
(b_i)_i=1,\quad (b_i)_r=-A_i A_r^{-1}\pmod{p^2},\quad
(b_i)_k=0\quad(k\notin\{i,r\}), \qquad i=u,w.
\]
Then \(A\cdot b_u=A\cdot b_w=0\bmod p^2\). For all \(x,y\in\mathbb F_p\), choose the displayed representatives and the explicitly lifted input
\[
\delta(x,y)=x b_u+y b_w \pmod{p^2},\qquad
\mathbf v(x,y)=\mathbf v_*+\delta(x,y).
\]
The following identity holds for **all \(x,y\)**, not just sampled witnesses:
\[
\boxed{F_p(p\mathbf v(x,y))-F_p(p\mathbf v_*)
\equiv p^2 Q_p(x,y)\pmod{p^3}},
\]
where
\[
Q_p(x,y)=a x^2+bxy+cy^2+\ell_0x+\ell_1y \pmod p,
\]
\[
a=\tfrac12 b_u^THb_u,\quad b=b_u^THb_w,\quad c=\tfrac12 b_w^THb_w,
\quad \ell_0=\mathbf v_*^THb_u,\quad\ell_1=\mathbf v_*^THb_w.
\]
**Proof:** Taylor-expand the finite polynomial \(F_p(p\mathbf v)\) to order 2 modulo \(p^3\). The linear term in the difference is \(pA\cdot\delta=0\bmod p^3\) by construction. All higher terms are multiples of \(p^3\). The displayed Hessian and labelled basis give \(Q_p\). Changing the lift of the kernel changes this coordinate chart and its second-digit readout; the theorem is for the declared lift, not an unspecified quotient.

## Theorem B — exact whole-fiber counts

Let \(D=b^2-4ac\). Assume \(D\ne0\) in \(\mathbb F_p\), let \((x_0,y_0)\) solve
\[
2ax_0+by_0=-\ell_0,\qquad bx_0+2cy_0=-\ell_1,
\]
and set \(\tau=Q_p(x_0,y_0)\). For **every** \(d\in\mathbb F_p\), the size of the entire source fiber \(\{(x,y):Q_p(x,y)=d\}\) is
\[
\boxed{\#Q_p^{-1}(d)=
\begin{cases}
2p-1,&D\text{ a square},\ d=\tau,\\
p-1,&D\text{ a square},\ d\ne\tau,\\
1,&D\text{ a nonsquare},\ d=\tau,\\
p+1,&D\text{ a nonsquare},\ d\ne\tau.
\end{cases}}
\]
**Proof:** Translate to the unique critical point. The nondegenerate binary quadratic part is split (isomorphic to a nonzero scalar times \(XY\)) exactly when \(D\) is a square. Counting \(XY=t\) gives \(2p-1\) at \(t=0\) and \(p-1\) elsewhere. In the nonsplit case it is a scalar norm form \(\mathbb F_{p^2}\to\mathbb F_p\), with one zero and \(p+1\) preimages of every nonzero norm. The linear translation maps the exceptional level to \(d=\tau\). This proves the count for the full \(p^2\) labelled input plane.


## Theorem C — pivot-independent adjugate invariant

Write \(T=A\bmod p\in\mathbb F_p^3\), and let \(H\) be the full symmetric source Hessian modulo \(p\). Define the original-coordinate scalar
\[
\boxed{\mathfrak D_p=-T^{\mathsf T}\operatorname{adj}(H)T\pmod p.}
\]
For the explicitly normalized kernel chart of Theorem A, the binary discriminant satisfies
\[
\boxed{\mathfrak D_p=T_r^2D\pmod p.}
\]
This holds whether or not \(H\) is invertible, since the adjugate is defined through cofactors. Thus **nondegeneracy and the quadratic character** of the second-digit kernel observer are independent of which nonzero gradient component is used as chart pivot; the complete source-labelled jet \((T,H)\) already determines the split/nonsplit fiber regime.

**Proof:** With the columns of the reduced kernel basis collected in the \(3\times2\) matrix \(B\), their cross product equals \(\pm T/T_r\). The three-dimensional cofactor/Cauchy–Binet identity gives
\[
\det(B^{\mathsf T}HB)=(b_u\times b_w)^{\mathsf T}
\operatorname{adj}(H)(b_u\times b_w)
=T^{\mathsf T}\operatorname{adj}(H)T/T_r^2.
\]
Because \(a=\frac12(B^{\mathsf T}HB)_{11}\), \(b=(B^{\mathsf T}HB)_{12}\), \(c=\frac12(B^{\mathsf T}HB)_{22}\), the discriminant is \(D=-\det(B^{\mathsf T}HB)\). No global inverse of the Hessian and no new geometric axiom is used.

The code checks this independent cofactor formula in every one of the 330 scanned primes. Explicit values of \(\mathfrak D_p\) are \(1,2,26,314,327,2346\) at \(p=13,19,211,373,1093,3511\), respectively. The remaining open algebraic target is a closed finite-sum/WZ simplification of \(\mathfrak D_p\), not merely a change of coordinates.

## Exact samples and formerly unresolved full-plane behavior

All entries below are generated from the undivided source jet recurrence. The first pivot is 0-based, the Hessian coefficients and linear vector are modulo \(p\).

| \(p\) | pivot | \((a,b,c;\ell_0,\ell_1)\) | \(D\) | \(\tau\) | zero fiber | exceptional fiber | other fibers |
|---:|---:|---|---:|---:|---:|---:|---:|
| 13 | 0 | (12,10,5;6,5) | 3 square | 8 | 12 | 25 | 12 |
| 19 | 0 | (16,5,10;8,11) | 12 nonsquare | 7 | 20 | 1 | 20 |
| 211 | 1 | (11,29,91;29,150) | 2 nonsquare | 87 | 212 | 1 | 212 |
| 373 | 0 | (289,157,67;141,327) | 163 square | 125 | 372 | 745 | 372 |
| 1093 | 0 | (84,166,761;920,602) | 297 square | 920 | **1092** | 2185 | 1092 |
| 3511 | 0 | (59,444,1757;2326,1833) | 166 nonsquare | 1710 | 3512 | 1 | 3512 |

In particular the previous \(p=1093\) **single-point collision on the fixed diagonal \((1,0,1)\)** coexists with **1092** sources in the zero fiber of this explicitly lifted full two-dimensional first-digit kernel. A one-dimensional line and a two-dimensional source plane have different, both well-defined, observation fibers. This supplies a constructive route to source recovery analysis beyond a single direction.

Exact nonzero witnesses with \(x=0,\ y=-\ell_1c^{-1}\) have equal complete weighted sums modulo \(p^3\), while their individually labelled \(j=1\) coefficients differ modulo \(p^2\):

| \(p\) | \(y\) | \(\delta\) modulo \(p^2\) | both \(F_p\bmod p^3\) | \((\Delta U_1/p)\bmod p\) |
|---:|---:|---|---:|---:|
| 13 | 12 | (129,0,12) | 13 | 10 |
| 19 | 16 | (92,0,16) | 19 | 15 |
| 211 | 54 | (0,2743,54) | 211 | 101 |
| 373 | 151 | (101980,0,151) | 373 | 242 |
| 1093 | 680 | (524227,0,680) | 1093 | 923 |
| 3511 | 2289 | (420098,0,2289) | 3511 | 2061 |

The labelled check uses
\[
(\Delta U_1/p)\bmod p
=-\frac12\sum_{i=1}^3\left(\prod_{k\ne i}s_k\right)\delta_i \pmod p.
\]
For \(p=13,19\), independent complete \(p\)-term sums were executed for **every** \(p^2\) chart input and matched the quadratic formula; for \(p=211,373\), the entire \(p^2\) quadratic histogram was checked, and direct full sums checked the displayed witnesses; direct complete sums also checked the 1093 and 3511 witnesses. A new exact scan of all **330 primes \(7\le p\le5000,\ p\equiv1\bmod6\)** found nonzero \(D\) throughout: 177 split, 153 nonsplit. This is a **finite observation** about \(D\), not a universal nondegeneracy theorem.

Reproduction: `research_notes/portable_direct/d25_full_source_kernel_fibers_20261106.py`; dependency: earlier persisted `research_notes/portable_direct/d25_outer_fiber_strata_20261106.py`. No floating-point arithmetic. Source data, sums, and comparisons are exact modular integers.

## BRC information-fiber consequence and next science

The population here is the affine two-parameter family of *labelled, three-source* \(p\)-adic inputs. The observation is the first two digits of the complete weighted scalar \(F_p\bmod p^3\). The allowed future observation \(\Delta U_1/p\bmod p\) discriminates the explicit equal-weight examples. Therefore the scalar quotient is **not source-faithful for this declared future observation**, even on the exact kernel-lift chart. The full labels, Hessian interactions, and lift information are retained in the certificate.

Next exact discriminating unit: simplify the pivot-independent cofactor invariant \(\mathfrak D_p=-T^{\mathsf T}\operatorname{adj}(H)T\) by symbolic finite sums or WZ certificates; classify where it vanishes beyond the tested bound, then connect this source-preserving chart to the open \(T_{1,p}+T_{3,p}=0\) and \(k_p=-3q_p(2)\) claims. The frozen mother goal remains \(\Delta_p-R_p=0\bmod p\) for \(p\equiv13,19\bmod24\); same-original-class 373 H0/B0, \([X]U\bmod p^2\), Frobenius, \(\eta,\kappa\), and independent audit remain open. No native experiment or reviewer acceptance is inferred.

## Authority / recovery boundary

Last exact known native continuation had `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` with no authorized new run. Original read request IDs `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` were reconciled under their own IDs on 2026-11-06; subsequent receipts still report `WAITING_RESOURCE / EVENT_COLLECTION_IO`. Current gateway status is `0.6.11`, exposing a recovery contract but no callable `recovery_status` or `session_preserve_staging` operation in the present client. Existing support: Enterprise Math issue #1558. No new Source session, CLAIM, OPEN, native checkpoint or result admission was made. Author-side GitHub persistence does not overwrite prior native checkpoint or purport to represent authenticated native research ownership.
