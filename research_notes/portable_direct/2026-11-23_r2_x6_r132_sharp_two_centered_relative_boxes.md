# X6 R132 — sharp centered four-weight stability radii for two Port-10 strict-eight chambers

Date: 2026-11-23. Status: **AUTHOR EXACT FINITE CERTIFICATE / FRACTION REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.

## Scope and frozen source

Conditional four-positive-weight, six-pair BRC observer in the selected three-axis slice; physical integer Port **10**, strict factor **3/2**, all four weights positive. This is not a native time-dynamics or P000 theorem. Preserve R121's 18-row optimizer bank and R122's 20-row universal exclusion envelope, with their frozen source and membership conditions. R129, R130 identify the two eight-direction sets; R131 supplied non-sharp sufficient radii 1/641 and 1/961. The new question is the **sharp centered relative L-infinity radius**, allowing all four weights to vary independently.

For nonzero signed integer triples a=(x,y,z) modulo sign (positive multiples remain distinct), let
q(a)=max(sum max(a_i,0),sum max(-a_i,0)),
h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z),
g=(|h1-h0|,|h2-h0|,|h3-h0|,|h2-h1|,|h3-h1|,|h3-h2|),
s=(A+B,A+C,A+D,B+C,B+D,C+D),
F_w(a)=max_j g_j(a)/s_j,
eta_10(w)=min_{0<q(a)<=10}F_w(a), N_10(w)={a/± : q(a)<=10, 2F_w(a)<3 eta_10(w)}.

Define the **centered robust-set radius**
R(w0)=sup{r>=0 : for every 0<=rho<r and every w with |w_i-w0_i|<=rho*w0_i, N_10(w)=N_10(w0)}.
The theorem below also shows the first failure at rho=R, so endpoint semantics are explicit.

## Theorem: sharp stability, not just a sufficient small box

| Center w0=(A,B,C,D) | eta_10(w0) | |N_10(w0)| | R131 sufficient radius | **R132 sharp open radius** | First boundary witness |
|---|---:|---:|---:|---:|---|
| (136,8,176,185) | 1/48 | 8 | 1/641 | **1/369** | (1,0,0), also (7,-1,0) |
| (722,465,240,48) | 1/96 | 8 | 1/961 | **1/721** | (3,3,-1), also (7,-8,2) |

For **every real 0<=rho<1/369**, all w in the relative closed rho-box around the first center have exactly the same eight unoriented strict-near directions as at the center, namely:
(1,0,0), (1,3,-1), (4,-4,1), (5,-4,1), (5,-1,0), (6,-1,0), (7,-1,0), (9,-5,1).

For **every real 0<=rho<1/721**, the second center retains:
(1,0,0), (3,-4,1), (3,3,-1), (4,-4,1), (6,-1,0), (7,-8,2), (7,-1,0), (9,-5,1).

At each displayed sharp radius there is an actual weight in its closed endpoint box for which a listed near direction meets 2F=3eta and is no longer **strictly** near. Thus no larger uniform centered relative radius is possible for preservation of these exact sets.

## Proof: one affine vertex certificate for the whole continuous four-weight box

The physical Port-10 finite population contains precisely 1,935 unoriented triples, without primitive-vector quotient. The frozen R121 bank B18 has g(b)<=g(a) componentwise for some feasible b for **each** a in the population. The R122 envelope E20 contains exactly the directions a for which no b in B18 has 2g(a)>=3g(b) componentwise. Thus all 1,915 omitted directions are globally excluded for **all** positive w, not merely for sample weights.

For each center, use b*=(6,-1,0), and choose k=01 (first center), k=23 (second center). For every corner w of the proposed closed R-box, perform the following exact-integer/rational tests:

1. For every b in B18, find a fixed index j=j(b) such that g_j(b)*s_k >= 3*s_j at **all 16 corners**. This proves F_w(b)>=3/s_k for all w in the box. For b*, check g_j(b*)*s_k <=3*s_j for **all** six j and all 16 corners. Hence eta_10(w)=3/s_k throughout the box.
2. Let N0 be the exact eight-row center set. For every a in N0 and every six-pair index j, verify 2*g_j(a)*s_k <=9*s_j at **all 16 corners**. For every a in E20\N0, find one fixed j=j(a) for which 2*g_j(a)*s_k >=9*s_j at **all 16 corners**.
3. Every inequality just written is **affine** in the four physical weights w. Checking all 16 vertices proves each inequality on the entire box. At the center, every inside inequality is strict, and every outside row is strictly outside. For rho<R, any point in the smaller box is a proper convex combination of the center and a point of the R-box, hence the inside inequalities remain strict while each outside row remains excluded. All 1,935 directions are now classified.

The standalone exact Fraction verifier executes full-lattice bank/envelope regeneration, all vertex checks and equality extraction. Its actual result is:
- 1,935 full triples; B18 domination PASS; E20 exclusion PASS (1,915 excluded);
- first box: 18 bank lower-witness rows, 8 inside rows times 6 comparisons, 12 outside fixed-witness rows, 16 vertices; PASS;
- second box: same counts; PASS.

No floating-point tolerance, sampling of the continuous box, or assumption that the active atom cannot switch is used. The affine tests automatically cover all switches inside the box.

## Sharp endpoints by constructive witnesses

**First center.** Take w=(136(1+r),8(1+r),176(1+r),185(1-r)), r=1/369. Since eta=3/(A+B), the direction a=(1,0,0) has a pair score 6/(B+D) and
F_w(a)/eta >= 2(A+B)/(B+D) = 3/2.
The equality follows from 4*144*(1+r)=3*(193-177*r), equivalent to 1107*r=3. The finite vertex certificate supplies the reverse inequality and anchored eta, so it is an actual boundary departure. The row (7,-1,0) also reaches equality through indices 02 and 13.

**Second center.** Take w=(722(1-r),465(1-r),240(1+r),48(1+r)), r=1/721. The optimizer remains eta=3/(C+D). For a=(3,3,-1), the pair 02 has score 15/(A+C), and
F_w(a)/eta >= 5(C+D)/(A+C)=3/2.
Indeed 10*288*(1+r)=3*(962-482*r), equivalent to 4326*r=6. The finite certificate again proves equality and the exact optimizer. (7,-8,2) also reaches the boundary.

Therefore the two reported **sharp** open radii are 1/369 and 1/721. Compared with R131's previously sufficient estimates, the improvements are exact and concern the same four-weight perturbation metric, not a redefinition of stability.

## Reproducibility, source preservation and next question

The attached source \`x6_r132_sharp_centered_boxes_verify.py\` is a self-contained standard-library-only checker: regenerate the entire unoriented Port<=10 lattice, the R121 B18 bank and R122 E20 exclusion; calculate the 16 vertices with \`fractions.Fraction\`; assert each affine bound; print the endpoint equality witnesses. An author-local execution on 2026-11-23 produced **ALL PASS**, with both exact radii above. Mathematical acceptance / independent review is still **NOT_REVIEWED**.

Frozen source inputs:
- R121: https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md
- R122: https://github.com/awdawmip/enterprise-math/blob/0687aa24f5402da3b35f914dd6907967a9805b94/research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json
- R129/R130: https://github.com/awdawmip/enterprise-math/blob/59e7d1e4c4717c0aaa6d5db1f016f62f1180c36d/research_notes/portable_direct/2026-11-23_r2_x6_r129_class_iii_port10_D_ray.md and 2026-11-23_r2_x6_r130_class_iv_port10_D_ray.md
- R131: https://github.com/awdawmip/enterprise-math/blob/68df475b03efd23a78d26ab7f963ee3c5fa2e06a/research_notes/portable_direct/2026-11-23_r2_x6_r131_two_strict_eight_transverse_stability_boxes.md

Unresolved: determine full (not centered) polyhedral/semi-algebraic stability chambers, their facets and adjacencies across four-weight space; separate any conditional six-pair BRC observation from true native P000 six-axis/time evolution. No native CLAIM, PROGRESS, Result, Review or P000 change is inferred from this portable scientific artifact.
