# R749SPH — exact risk of the canonical Walsh center on the entire upper parameter triangle

Date: 2026-11-15. Status: AUTHOR_EXACT_NOT_REVIEWED. Independent portable research, auxiliary 16-atom Walsh compatible-source observer. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

Immediate predecessor: R749SPG, Draft PR #2431, scientific commit e985f1c8f8d7fe2a7ff2914b1835d68d5ef5b6fc. That predecessor established exact minimaxity of the canonical center on two zero-gap triangles. This note proves a complementary **worst-source-risk** theorem and combines the certificates over the full upper half-square; it does not change the R749SPG minimaxity domain.

## 1. Model and new all-real theorem

For \(k\in K=\mathbb F_2^4\), define \(\chi_m(k)=(-1)^{\operatorname{popcount}(k\mathbin{\&}m)}\) and the normalized Walsh law
\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]
The compatible fiber \(F(t,s)\) contains all laws in this family that are nonnegative at all sixteen atoms. Define the *particular calibrated center*
\[
q_0(t,s)=p_{t,s,t+s-1,0,0,0,0}.
\]
It is a probability law for all real \(0\le t,s\le1\) with \(t+s\ge1\).

Let
\[
D_0=\operatorname{conv}\left\{(\tfrac12,\tfrac12),(\tfrac35,\tfrac25),(1,1)\right\}
=\{(t,s):t\ge s,\ t+s\ge1,\ 3t-2s\le1\}.
\]

**New theorem (exact, continuous parameter domain):** For every real \((t,s)\in D_0\),
\[
\boxed{\sup_{p\in F(t,s)}\operatorname{TV}(p,q_0(t,s))=1-t.}
\]
The total-variation metric is \(\operatorname{TV}(p,q)=\tfrac12\sum_{k\in K}|p(k)-q(k)|\).

By exchanging the two bit pairs, the same formula holds on \(D_0^\top\), with \(t,s\) swapped. Each of these triangles has area \(1/20\), so their combined parameter area is \(1/10\).

**Combination with the previously proved R749SPG theorem:** The upper-right half of the unit parameter square, \(t+s\ge1\), is partitioned by \(t=s\) and \(3\max(t,s)-2\min(t,s)=1\). Put \(M=\max(t,s)\), \(m=\min(t,s)\). Then, for *every real* \(0\le t,s\le1\) with \(t+s\ge1\),
\[
\boxed{\sup_{p\in F(t,s)}\operatorname{TV}(p,q_0(t,s))
=\max\left\{\frac{3-M-2m}{4},\,1-M\right\}.}
\]
R749SPG supplies the first branch on its two triangles (combined area \(2/5\)); R749SPH supplies the complementary two triangles (combined area \(1/10\)). Together their union is the complete upper parameter triangle (area \(1/2\)). The changeover is exactly \(3M-2m=1\).

This combined formula characterizes the worst-case risk **of this specified center**. The free minimax radius and calibrated minimax radius optimize over centers; R749SPG already proves that this center is jointly optimal on the original two triangles.

## 2. Explicit source attaining the new lower bound

On \(D_0\), the law
\[
H(t,s)=p_{t,s,1-t+s,0,0,0,0}
\]
is compatible. Indeed its four branch masses are nonnegative: for \(a=\chi_3\), \(b=\chi_{12}\), the block coefficient
\[
M_{ab}=1+ta+sb+(1-t+s)ab
\]
takes values \(2+2s,\ 2t-2s,\ 2-2t,\ 0\), in some block order. The assumptions \(0\le s\le t\le1\) make each value nonnegative.

The two laws \(H\) and \(q_0\) differ only in the \(\chi_{15}\) coefficient:
\[
(1-t+s)-(t+s-1)=2(1-t).
\]
Since \(|\chi_{15}(k)|=1\) on all sixteen atoms,
\[
\operatorname{TV}(H,q_0)
=\frac12\sum_{k=0}^{15}\frac{2(1-t)}{16}
=1-t.
\]
This lower witness applies individually to **every real parameter point** in the triangle, rather than merely to its corners.

## 3. Exact universal upper certificate

The positivity constraints of the source are precisely the sixteen affine inequalities
\[
1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)
+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)\ge0
\quad (k=0,\ldots,15).
\]
Intersect these with the three inequalities
\[
t-s\ge0,\quad t+s\ge1,\quad -3t+2s\ge-1.
\]
They define a bounded seven-dimensional rational polytope \(\mathcal P\) in \((t,s,h,u,v,w,z)\). Boundedness follows because the source is a normalized nonnegative Walsh probability law: each of its seven Walsh coefficients is an expectation of a sign character, hence lies in \([-1,1]\).

The function
\[
\Phi(t,s,h,u,v,w,z)=
\operatorname{TV}(p_{t,s,h,u,v,w,z},q_0(t,s))-(1-t)
\]
is convex on \(\mathcal P\), since each source atom and each center atom is affine in the seven variables and \(1-t\) is affine. On a compact polytope a convex function is at most the maximum of its values at the vertices.

The accompanying exact Python Fraction / integer Bareiss program enumerates all \(\binom{19}{7}=50,388\) seven-facet active sets. It solves every nonsingular basis exactly, checks all nineteen inequalities, deduplicates complete rational vertices and evaluates \(\Phi\) without floating point. The executed certificate is:

| Metric | Exact result |
|---|---:|
| Candidate seven-facet bases | 50,388 |
| Nonsingular bases | 28,288 |
| Feasible bases (repetitions counted) | 3,116 |
| Distinct rational vertices | 38 |
| Vertices with zero upper excess | 10 |
| Maximum risk excess \(\max_{\mathrm{vert}(\mathcal P)}\Phi\) | **0** |
| Result | **PASS** |

All 38 vertices project to one of the three parameter corners: 17 at \((1/2,1/2)\), 20 at \((3/5,2/5)\), one at \((1,1)\). This exact projection fact is part of the certificate, not an assumed corner-only test. Convexity now proves \(\Phi\le0\) everywhere in the joint polytope, establishing the asserted worst-source-risk upper bound for every real \((t,s)\in D_0\). The lower witness gives equality.

The bit-pair swap \(k\mapsto((k\mathbin{\&}3)\ll2)\mathbin{|}((k\mathbin{\&}12)\gg2)\) swaps the \(t,s\) coefficients and permutes the four linear-source coefficients. It preserves probability positivity and TV, transferring the exact theorem to \(D_0^\top\). This is the already established automorphism from R749SPG; no new observer quotient is taken.

## 4. BRC carrier interpretation and a discriminating example

The four-branch positive carrier keeps \(a=\chi_3\), \(b=\chi_{12}\), \(c=\chi_1\), \(d=\chi_4\) with
\[
16p_{abcd}=M_{ab}+cU_a+dV_b,\quad
M_{ab}=1+ta+sb+hab,\quad U_a=u+av,\quad V_b=w+bz.
\]
The sixteen atomwise inequalities are equivalent to
\[
M_{ab}\ge |U_a|+|V_b|\quad(a,b=\pm1).
\]
This preserves the signed coefficients and the composite \(\chi_{15}=\chi_3\chi_{12}\) interaction. The witness \(H\) changes that retained joint-interaction coordinate without changing \(t,s\).

For example, at \((t,s)=(3/5,3/5)\), which lies inside \(D_0\), the canonical center has exact risk \(1-t=2/5\). The previously published R749SPD–SPF minimax results for the same frozen Walsh fiber give \(\rho=8/25\) and \(\rho^{\rm cal}=18/55\), hence \(g=2/275\). Thus the new formula quantitatively detects how much this *particular* center can be improved at a point where the genuine calibrated minimax cost is positive.

The two existing minimax triangles and the two complementary risk triangles cover the upper parameter triangle. This is a complete exact center-risk classification on that domain, with the separate global minimax phase boundaries inside the complementary region still to be mapped.

## 5. Reproduction, provenance, remaining problem

Files in research_notes/portable_direct:
- R749SPH_UPPER_WEDGE_CENTER_RISK_EXACT_CERT.py
- R749SPH_UPPER_WEDGE_CENTER_RISK_RESULTS.json

Execute with Python 3 standard library: python3 R749SPH_UPPER_WEDGE_CENTER_RISK_EXACT_CERT.py > R749SPH_UPPER_WEDGE_CENTER_RISK_RESULTS.json. The submitted exact result is PASS, 38 distinct vertices, and maximum excess zero. The previous R749SPG certificate independently covers the first branch; the present script covers the complementary triangle. Source code and results are author-executed evidence pending independent mathematical review.

This research is scoped to the auxiliary 16-atom Walsh observer under the unchanged frozen scientific pin. P000, Heartbeat World native X6, signed provenance and formal native Result/Review authority retain their existing separate meanings.

**Next mathematical unit:** derive a precise two-dimensional piecewise formula for the true minimax gap \(g(t,s)\) inside \(D_0\), starting at \((3/5,3/5)\) and at the return boundary \((11/15,3/5)\); seek matching free/calibrated affine centers and source/event dual certificates. Compare this center-risk phase boundary with the actual minimax phase boundary, rather than identifying them.
