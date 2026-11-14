# R749SPI — exact full diagonal Walsh minimax radii and calibrated gap

**Date:** 2026-11-15. **Status:** AUTHOR_EXACT_NOT_REVIEWED.  
**Frozen science:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.  
**Immediate dependency:** R749SPH, Draft PR #2435, initial exact positive trapezoid theorem.  
This paper concerns the *auxiliary* 16-atom Walsh fiber; native X6/P000 premises are unchanged.

## Theorem

For \(K=\mathbb F_2^4\), define \(\chi_m(k)=(-1)^{\mathrm{popcount}(k\&m)}\) and
\[
p_{t,s,h,u,v,w,z}(k)
=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]
At fixed \((t,s)\), let \(F(t,s)\) be all nonnegative normalized laws of this form. Let \(\rho\) be minimax total-variation radius with arbitrary probability-law center, and \(\rho^{\mathrm{cal}}\) the radius with the center restricted to \(F(t,s)\).

**For all real \(r\in[1/2,1]\), at \(t=s=r\),**
\[
\boxed{\rho(r,r)=\frac{4(1-r)}5},\qquad
\boxed{\rho^{\mathrm{cal}}(r,r)=\frac{9(1-r)}{11}},\qquad
\boxed{g(r,r)=\frac{1-r}{55}}.
\]
Thus \(g(r,r)>0\) on the full half-open interval \(1/2\le r<1\) and equals zero at \(r=1\). This enlarges the exact R749SPH diagonal scope from \([1/2,11/15]\) to \([1/2,1]\).

Explicit optimal centers:
\[
q_f(r)=p_{1,(8r-3)/5,(8r-3)/5,0,0,0,0},\qquad
q_c(r)=p_{r,r,(18r-7)/11,0,0,0,0}.
\]
Each is a nonnegative normalized law on the entire interval, and \(q_c(r)\in F(r,r)\).

## Matching lower bounds

The four-branch BRC chart uses \(a=\chi_3,b=\chi_{12},c=\chi_1,d=\chi_4\):
\[
16p=M_{ab}+cU_a+dV_b,\quad
M_{ab}=1+ta+sb+hab,\ U_a=u+av,\ V_b=w+bz.
\]
Nonnegativity is exactly \(M_{ab}\ge |U_a|+|V_b|\) for all four branches, without dropping signed deviations.

Two explicit compatible source families on this full real interval are
\[
P_-(r)=p_{r,r,2r-1,r-1,r-1,r-1,r-1},\qquad
P_a(r)=p_{r,r,1,0,0,0,0}.
\]
The laws are affine in \(r\); the attached exact checker verifies nonnegativity and total mass one at both endpoints. Hence they remain compatible for all \(r\in[1/2,1]\).

Use the fixed events \(E_A=\{7,11,13,14,15\}\) and \(E_B=\{0,3,5,6,9,10,12,15\}\). Exact Walsh expansion gives
\[
P_-(E_A)=5/4-r,\qquad P_a(E_B)=1.
\]
Group averaging over \(G=\ker\chi_3\cap\ker\chi_{12}\) does not increase the maximum risk of any arbitrary free prediction center, and reduces it to the four per-atom sign-block masses \(x_0,x_1,x_2,x_3\) with \(x_i\ge0,4\sum x_i=1\). The event block counts are \((0,2,2,1)\) and \((4,0,0,4)\), so their weighted center masses equal \(2/5-(4/5)x_0\). Consequently
\[
\sup_{P\in F(r,r)}\operatorname{TV}(P,q)
\ge\frac45[P_-(E_A)-q(E_A)]+\frac15[P_a(E_B)-q(E_B)]
=\frac{4(1-r)}5+\frac45x_0
\ge \frac{4(1-r)}5.
\]
This is valid for **all free centers**, not merely the candidates.

A group-averaged calibrated center has the form \(q_h=p_{r,r,h,0,0,0,0}\). The same events yield the lower envelope
\[
\sup_{P\in F(r,r)}\operatorname{TV}(P,q_h)
\ge\max\left\{\frac{15-18r+3h}{16},\frac{1-h}{2}\right\}.
\]
The increasing and decreasing lines intersect at \(h=(18r-7)/11\) with common value \(9(1-r)/11\), so this is the calibrated minimax lower bound.

## Continuum upper certificate: all six-dimensional joint vertices

Consider the compact six-dimensional rational polytope in \(x=(r,h,u,v,w,z)\) defined by 16 Walsh nonnegative-atom inequalities and \(2r\ge1,\ -r\ge-1\). Its boundedness follows because each law's Walsh coefficients are in \([-1,1]\). The accompanying exact Python checker enumerates **all**
\[
\binom{18}{6}=18564
\]
potential independent active bases, solves them with integer Bareiss elimination and exact rational back-substitution, and discards singular and infeasible bases. It finds:

| Item | Exact result |
|---|---:|
| Potential active bases | 18,564 |
| Nonsingular bases | 10,848 |
| Feasible bases, with multiplicity | 1,644 |
| Distinct rational joint vertices | 18 |
| Vertex parameter projection | 17 at \(r=1/2\), 1 at \(r=1\) |
| Tight free / calibrated vertices | 6 / 6 |
| Maximum free TV excess | 0 |
| Maximum calibrated TV excess | 0 |
| Executed program | PASS |

At every joint vertex, source law and both candidate centers are nonnegative and normalized, and
\[
\operatorname{TV}(p_x,q_f(r))-\frac{4(1-r)}5\le0,\qquad
\operatorname{TV}(p_x,q_c(r))-\frac{9(1-r)}{11}\le0.
\]
Both expressions are convex in the complete joint variables, because all laws and centers are affine and the subtracted bounds are affine. A convex function over a compact polytope is bounded above by its maximum over vertices. Thus the verified complete vertex set proves the candidate upper bounds for **all real** compatible sources and all \(r\) in the interval. The explicit event lower bounds above match, proving the theorem.

## Reproducibility, mathematical meaning and next question

Run \`python3 R749SPI_FULL_DIAGONAL_POSITIVE_GAP_CERT.py > R749SPI_FULL_DIAGONAL_POSITIVE_GAP_RESULTS.json\`. It uses standard-library Python \`Fraction\`, integer Bareiss arithmetic, no numerical tolerances, and complete active-set enumeration. Actual local execution in this research run produced PASS. Source code and the PASS JSON accompany this paper.

This is author-side exact evidence pending independent mathematical review. It does not yet construct the source/ordered-operation-preserving map to native six-axis X6/V29/V39 dynamics or signed-Port rules.

Next: determine the maximal two-parameter positive-gap region around the full diagonal, including where these dual certificates or affine centers switch; compare the certified zero-gap triangles of R749SPG with the newly certified positive diagonal and identify the exact intervening polygon walls.
