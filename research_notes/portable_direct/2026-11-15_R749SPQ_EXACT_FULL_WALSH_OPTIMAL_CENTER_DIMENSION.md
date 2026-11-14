# R749SPQ — Exact affine dimension three of the full calibrated Walsh minimax-center set and a strict extension beyond the R749SPP octahedron

**Research status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen scientific pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Immediate input:** R749SPP exact octahedral calibrated-center theorem, same Draft PR #2456. **Provenance:** 2026-11-15 independent TASK_RESEARCH, Researcher-ID EM-DIRECT-4200AE, original Activity RA-9E4E568D1C7DC3CE3B7F51CE.

## 1. Sharpened result at the precise Walsh fiber

The 16-atom model is

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

For fixed (t,s)=(1/10,1/2), let \(\mathcal C\) be the *complete* set of calibrated minimax centers in the source fiber, i.e. every feasible \(q=p_{1/10,1/2,h,u,v,w,z}\) with \(\max_{P\in F(1/10,1/2)}TV(P,q)=9/20\). The common free and calibrated minimax radius equals 9/20 by the R749SPO/R749SPP exact proof.

**Theorem A (complete affine dimension):**
\[
\boxed{\quad q\in\mathcal C\Longrightarrow w(q)=z(q)=0,\qquad \dim_{\rm aff}\mathcal C=3.\quad}
\]
Here the dimension is in the full five-free-coefficient calibrated source fiber, *not* a hand-selected 3D subproblem.

**Theorem B (strict octahedral containment):** The calibrated center
\[
\boxed{q_*=p_{1/10,1/2,\,-1/10,\,+1/10,\,-1/5,\,0,\,0}}
\]
has maximal source risk exactly 9/20. It lies outside the R749SPP octahedron \(|h|+|u|+|v|\le1/5\), since here the absolute sum equals 2/5. Thus the 3D octahedron is a proper subset of \(\mathcal C\). No assertion that the whole 3D set is yet classified is made.

## 2. Exact elementary necessity: four signed Walsh witness sources

For each k=0,...,15 and any two probability laws P,Q on these atoms, the variational characterization of total variation supplies
\[
2TV(P,Q)\ge|\mathbb E_P\chi_m-\mathbb E_Q\chi_m|
\]
for every character \(\chi_m\in\{\pm1\}\). Because a Walsh coefficient is its corresponding moment, for calibrated candidates the fourth and fifth source coefficients are precisely the moments \(w=\mathbb E_q\chi_4\) and \(z=\mathbb E_q\chi_8\).

Construct the following **four complete compatible source laws**, all with (t,s)=(1/10,1/2) and h_source=1/10, u_source=v_source=0:

\[
P_{w,\pm}=p_{1/10,1/2,1/10,0,0,\ \pm9/10,\ \pm4/10},
\qquad
P_{z,\pm}=p_{1/10,1/2,1/10,0,0,\ \pm4/10,\ \pm9/10}.
\]

Each satisfies the 16 frozen atomic nonnegativity inequalities; the companion Python certificate checks them one by one using exact rationals (they are also vertices of the exact 5D source polytope).

Any q in \(\mathcal C\) has TV(P,q)≤9/20 for all these four laws. The pair \(P_{w,\pm}\) therefore yields
\[
|9/10-w|\le9/10,\qquad |-9/10-w|\le9/10,
\]
whose intersection is exactly \(w=0\). The pair \(P_{z,\pm}\) analogously yields \(z=0\). Every optimal calibrated center therefore belongs to the three-dimensional linear carrier \(w=z=0\).

R749SPP already exhibited a full-dimensional positive-volume three-dimensional octahedron inside \(\mathcal C\), so \(\dim_{\rm aff}\mathcal C\ge3\). The moment witness restrictions establish the opposite inequality and prove \(\dim_{\rm aff}\mathcal C=3\). This is a dimensional characterization of the **full calibrated** optimum set, not merely an upper bound for one selected center family.

## 3. Exact strictness witness beyond the octahedron

Take \(q_*\) as displayed. In scaled coordinates Q=10(h,u,v,w,z)=(-1,1,-2,0,0), verify all sixteen inequalities
\[
10+\chi_3(k)+5\chi_{12}(k)+Q\cdot(\chi_{15}(k),\chi_1(k),\chi_2(k),\chi_4(k),\chi_8(k))\ge0.
\]
For any compatible source P_Y at the same fixed observed moments,
\[
TV(P_Y,q_*)=\frac1{320}\sum_{k=0}^{15}|a_k\cdot(Y-Q)|,\quad a_k=(\chi_{15},\chi_1,\chi_2,\chi_4,\chi_8)(k).
\]
As proven and independently enumerated in R749SPP, the complete 5D source-fiber polytope has 50 distinct rational vertices, obtained by exhausting all \(\binom{16}{5}=4368\) active bases with exact integer Bareiss. The new verifier imports the same precisely pinned source construction, reconstructs the entire 50-vertex set, and checks
\[
\max_{\text{all 50 vertices}}\left[\sum_k|a_k\cdot(Y-Q)|-144\right]=0.
\]
Exactly 21 source vertices are tight. Convexity implies the TV risk is at most 9/20 against *every* compatible source. R749SPP's explicit antipodal source pair has TV distance 9/10, so the common lower bound 9/20 is attained. This proves q* is an optimal calibrated center and that \(\mathcal C\) strictly exceeds the original octahedron.

## 4. Evidence, scope, remaining science

Execute \`python3 R749SPQ_WALSH_EXACT_CENTER_DIMENSION_CERT.py > R749SPQ_WALSH_EXACT_CENTER_DIMENSION_RESULTS.json\` in the same directory as its R749SPP exact certificate dependency. Both scripts rely solely on Python's standard library, Fraction and integer Bareiss arithmetic; the produced JSON is PASS with all four complete sign witnesses, 50 reconstructed source vertices and 21 tight source vertices for q*.

The exact parameters, six-dimensional X6 worldview, signed-source identity and BRC typing remain distinct from the *auxiliary Walsh* representation, for which this theorem is proved. Mathematical status: AUTHOR_EXACT_NOT_REVIEWED; no independent review or native X6/V29/V39 promotion.

**Next specific question:** determine a complete irredundant rational facet description for the three-dimensional optimal center polytope in (h,u,v) at (1/10,1/2), then track how its vertices and supporting witness events change over nearby (t,s) parameter chambers. The R749SPP octahedron is now a certified inner carrier and q* a certified outer-to-octahedral point.
