# R749SPP — A certified three-dimensional octahedron of calibrated minimax centers in the frozen Walsh fiber

Status: **AUTHOR_EXACT_NOT_REVIEWED**. Date: 2026-11-15. Researcher: EM-DIRECT-4200AE. Activity: RA-9E4E568D1C7DC3CE3B7F51CE.
Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
Immediate exact predecessor: R749SPO (existing canonical project artifact \`research_notes/portable_direct/2026-11-15_R749SPO_COMPLETE_WALSH_H_AXIS_MINIMAX_CENTER_INTERVAL.md\` at commit \`bc071b09d96f66246c781b93ea395094e64daf9b\`); R749SPN PR #2449.

## 1. Model, problem and theorem

For k=0,...,15 define the seven Walsh characters chi_m(k)=(-1)^{popcount(k&m)} at m=3,12,15,1,2,4,8. Fix moments (t,s) and set

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

The *source fiber* F(t,s) consists of all sixteen-atom nonnegative laws of this form. Equip it with total variation TV(P,Q)=sum_k|P(k)-Q(k)|/2. Define
\[
\rho(t,s)=\inf_{q\in\Delta_{16}}\max_{P\in F(t,s)}TV(P,q),\qquad
\rho^{cal}(t,s)=\inf_{q\in F(t,s)}\max_{P\in F(t,s)}TV(P,q).
\]

**Exact theorem.** At the fixed admissible parameter pair (t,s)=(1/10,1/2), the common optimum is
\[
\boxed{\rho=\rho^{cal}=9/20}.
\]
Moreover **every** law of the form
\[
\boxed{q_{h,u,v}=p_{1/10,1/2,h,u,v,0,0},\qquad |h|+|u|+|v|\le1/5}
\]
is an optimal calibrated center. This is a **three-dimensional octahedron** in the (h,u,v) affine subspace (volume 4/375 in these coefficient coordinates). In particular, R749SPO's exact one-dimensional h-axis optimal interval [-1/5,1/5] sits in a higher-dimensional continuum of optimal calibrated centers. The theorem asserts containment of the octahedron in the full minimax-center polytope; the entire polytope, its face lattice and possible nonzero w,z remain open.

## 2. Matching lower bound — complete two-source provenance

The same fully specified and nonnegative frozen-fiber laws used in R749SPN give
\[
P_\pm=p_{1/10,1/2,0,-1/10,-1/10,\ \pm1/2,\ \pm9/10}.
\]
Their exact total-variation distance is TV(P_+,P_-)=9/10. Any free predictive center q satisfies
\[
\max(TV(P_+,q),TV(P_-,q))\ge\frac12 TV(P_+,P_-)=9/20.
\]
This bounds both free and calibrated minimax radii below by 9/20.

## 3. Six exact upper certificates and convexity

The claimed octahedron is the convex hull of six signed axis vertices (h,u,v) equal to
\[
(\pm1/5,0,0),\quad(0,\pm1/5,0),\quad(0,0,\pm1/5).
\]
For each of the six, the 16 atomic probabilities are explicitly checked nonnegative; hence these centers are in F(1/10,1/2). Fiber convexity gives feasibility of their convex hull.

For the *source* law use variables Y=10(h_src,u_src,v_src,w_src,z_src), so the 16 inequalities become integer constraints
\[
\sum_{j=1}^{5} a_{kj}Y_j\ge -10-\chi_3(k)-5\chi_{12}(k),\qquad
a_k=(\chi_{15}(k),\chi_1(k),\chi_2(k),\chi_4(k),\chi_8(k)).
\]
This defines a compact, full-dimensional 5-dimensional rational polytope, with 16 affine halfspaces. The accompanying exact verifier examines every \(\binom{16}{5}=4368\) five-facet active combination by integer Bareiss elimination, identifies all 50 distinct rational vertices, and checks all six proposed center laws.

For each scaled center Q=10(h,u,v,0,0), we require
\[
TV(P_Y,q_Q)=\frac1{320}\sum_{k=0}^{15}|a_k\cdot(Y-Q)|\le\frac9{20},
\]
equivalently
\[
\sum_{k=0}^{15}|a_k\cdot(Y-Q)|\le144.
\]
The left side is convex in Y. Exhaustively checking this inequality on all vertices is sufficient to prove it for *every* compatible source law. The exact enumerator reports:

| Finite certificate | Observed |
| --- | ---: |
| Candidate five-facet combinations | 4,368 |
| Nonsingular bases | 3,008 |
| Feasible bases, repetition retained | 196 |
| Distinct exact feasible vertices | 50 |
| Max exact upper-bound excess at each of six centers | 0 |
| Vertices achieving upper bound (six centers) | 16, 22, 16, 16, 16, 16 |
| Result of locally executed exact test | PASS |

Finally, every center within the octahedron is a convex combination of its six vertices, and TV is convex in the center. Its source supremum cannot exceed 9/20. Matching the two-source lower bound proves the claim. No numerical tolerance, floating LP or sample-to-continuum extrapolation is involved.

## 4. Four-branch BRC interpretation, verification scope and next question

The original full signed and source-labeled atoms are retained. The four BRC blocks (a,b)=(chi_3,chi_12) satisfy 16p_{abcd}=M_ab+cU_a+dV_b, where M_ab=1+at+bs+abh, U_a=u+av, V_b=w+bz, and each block's exact admissibility is M_ab>=|U_a|+|V_b|. The derived 3D optimal polytope varies both the joint cross-moment h and two independent provenance-sensitive coefficients u,v, demonstrating a real enlargement beyond single-h-axis optimality in this auxiliary model.

Run \`python3 R749SPP_WALSH_3D_OPTIMAL_CENTER_OCTAHEDRON_CERT.py > R749SPP_WALSH_3D_OPTIMAL_CENTER_OCTAHEDRON_RESULTS.json\`. Python standard-library Fraction and exact integer Bareiss eliminate all 4,368 candidates. Results contain exact vertex counts and six separate upper certificates; the source pair verifies the lower bound.

**Next discriminating problem:** test optimal centers involving nonzero w,z at (t,s)=(1/10,1/2), and determine whether the full minimax-center set has affine dimension greater than 3. If it does, provide a new independent vertex and exact all-source certificate; if not, obtain an exclusion witness for all off-octahedral directions. Then classify center-polytope changes in neighboring (t,s) chambers.

This claim remains internal to the frozen *auxiliary* Walsh model. No original X6/V29/V39 event-level signed-source correspondence, independently reviewed proof or formal Lean checker is claimed.
