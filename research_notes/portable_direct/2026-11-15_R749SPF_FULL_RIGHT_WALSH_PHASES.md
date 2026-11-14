# R749SPF — exact complete right-hand Walsh phase diagram and reentrant zero calibration

Date: 2026-11-15. Status: AUTHOR_EXACT_NOT_REVIEWED. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Predecessor: R749SPD–SPE Draft PR #2424 at \`ba2c4150f06a239a68f4431cb3c3f3193acc520e\`; older same-slice R749SPA–SPC PRs #2417 and #2420. This is an independent portable auxiliary-model result, not a shared CLAIM, Result or Review.

## 1. Model and exact theorem

Let \(K=\mathbb F_2^4\), \(\chi_m(k)=(-1)^{\mathrm{popcount}(k\&m)}\), and
\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]
At fixed \(t,s\), \(F(t,s)\) is the full fiber of all nonnegative normalized such laws. Define total variation \(\mathrm{TV}(p,q)=\frac12\sum_{k=0}^{15}|p(k)-q(k)|\), unrestricted minimax radius \(\rho(t,s)=\inf_{q\in\Delta_{15}}\sup_{p\in F(t,s)}\mathrm{TV}(p,q)\), fiber-calibrated radius \(\rho^{\mathrm{cal}}(t,s)=\inf_{q\in F(t,s)}\sup_{p\in F(t,s)}\mathrm{TV}(p,q)\), and gap \(g=\rho^{\mathrm{cal}}-\rho\).

**New theorem (all real parameters \(3/5\le t\le1\), \(s=3/5\)).** On the four consecutive closed intervals \(A=[3/5,13/20]\), \(B=[13/20,17/25]\), \(C=[17/25,11/15]\), \(D=[11/15,1]\),
\[
\rho(t,3/5)=
\begin{cases}
31/50-t/2,& A\cup B,\\
9/20-t/4,& C\cup D;
\end{cases}
\]
\[
\rho^{\mathrm{cal}}(t,3/5)=
\begin{cases}
36/55-6t/11,&A,\\
14/25-2t/5,&B\cup C,\\
9/20-t/4,&D.
\end{cases}
\]
The expressions agree at every shared endpoint. In particular \(g>0\) for \(3/5\le t<11/15\), while \(g=0\) for every \(11/15\le t\le1\). The exact new nonmonotone gap values at \(t=3/5,13/20,17/25,11/15,1\) are \(2/275,1/200,1/125,0,0\) respectively.

**Corollary incorporating the previously published R749SPA–SPE exact subintervals:** on the *entire real unit slice* \(0\le t\le1,s=3/5\), the zero-gap set is exactly \([0,2/5]\cup[11/15,1]\); \(g>0\) exactly for \(2/5<t<11/15\). The earlier intervals and their hypotheses are used at their original frozen scientific pin, not re-proved or upgraded here. This is a reentrant **zero calibrated minimax penalty**, not a claim of native X6 operational dynamics.

## 2. BRC four-branch representation and symmetry

Put \(a=\chi_3(k)\), \(b=\chi_{12}(k)\), \(c=\chi_1(k)\), \(d=\chi_4(k)\). Each \((a,b)\in\{\pm1\}^2\) carries four distinct atoms \((c,d)\), and
\[
16p(k)=M_{ab}+cU_a+dV_b,\quad
M_{ab}=1+ta+sb+hab,\quad U_a=u+av,\quad V_b=w+bz.
\]
Exact nonnegativity is \(M_{ab}\ge |U_a|+|V_b|\) for each branch. This is a *positive law with signed Walsh deviations*, not a collapse of signed amplitudes to positive mass.

The four-element translation group \(G=\ker\chi_3\cap\ker\chi_{12}\) preserves \(F(t,s)\) and TV and kills the four one-bit coefficients on averaging. Convexity of worst-case risk permits a \(G\)-invariant free center, specified by per-atom masses \(x_0,x_1,x_2,x_3\ge0\) on sign blocks \((--),(-+),(+-),(++)\), \(4\sum x_i=1\). A \(G\)-averaged calibrated center is \(q_h=p_{t,3/5,h,0,0,0,0}\).

## 3. Explicit matching lower certificates

Introduce three exact compatible source families:
\[
P_-(t)=p_{t,3/5,t-2/5,-2/5,-2/5,t-1,t-1},\quad
P_+(t)=p_{t,3/5,t-2/5,2/5,2/5,1-t,1-t},
\]
\[
P_a(t)=p_{t,3/5,8/5-t,3/5-t,3/5-t,0,0}.
\]
\(P_\pm\) are compatible on \([3/5,1]\); \(P_a\) on \([3/5,11/15]\). Each 16-atom law is affine in \(t\). Direct exact nonnegativity and normalization at the interval endpoints prove full continuous-parameter compatibility.

Define three fixed events
\[
E_A=\{7,11,13,14,15\},\quad E_C=\{3,7,11,13,14,15\},\quad E_B=\{0,3,5,6,9,10,12,15\}.
\]
Their numbers of atoms in the four sign blocks are respectively \((0,2,2,1),(0,2,2,2),(4,0,0,4)\). Exact source event masses are
\[
P_-(E_A)=19/20-t/2,\quad P_-(E_C)=19/20-t/4,\quad P_a(E_B)=13/10-t/2.
\]

For **unrestricted** free centers, use \(\mathrm{TV}(p,q)\ge p(E)-q(E)\). On \(A\cup B\), the weighted combination \(4/5\) of \((P_-,E_A)\) and \(1/5\) of \((P_a,E_B)\) yields
\[
R(q)\ge31/50-t/2+(4/5)x_0\ge31/50-t/2.
\]
On \(C\cup D\), the single witness \((P_-,E_C)\) yields
\[
R(q)\ge9/20-t/4+2x_0\ge9/20-t/4.
\]
Symmetrization makes these bounds valid for *all* unrestricted centers.

For **calibrated** centers \(q_h\), the exact event identities, valid for real \(t,h\), are
\[
\begin{split}
P_-(E_A)-q_h(E_A)&=3/5-9t/16+3h/16,\\
P_-(E_C)-q_h(E_C)&=1/2-3t/8+h/8,\\
P_a(E_B)-q_h(E_B)&=4/5-t/2-h/2.
\end{split}
\]
Minimizing the maximum of the first and third lines gives \(h=(5t+16)/55\), a universal lower bound \(36/55-6t/11\) on \(A\). Minimizing the maximum of the second and third gives \(h=(12-5t)/25\) and lower bound \(14/25-2t/5\) on \(B\cup C\). These lower bounds do not assume the resulting \(h\) is the only admissible optimum.

On \(D\), \(P_+\) and \(P_-\) have midpoint \(q_*=p_{t,3/5,t-2/5,0,0,0,0}\). Their exact TV distance is \(2(9-5t)/20\). This follows directly from the four-branch identity \(\mathrm{TV}(P_+,q_*)=\frac18\sum_{a,b}\max(|U_a|,|V_b|)\) with \((|U_-|,|U_+|)=(0,4/5)\), \((|V_-|,|V_+|)=(0,2(1-t))\); since \(t\ge3/5\), \(2(1-t)\le4/5\). Thus the general diameter/2 bound gives \(\rho\ge(9-5t)/20\).

## 4. Matching affine centers and universal upper certificates

For the four subintervals, use the following explicit optimal unrestricted centers:
\[
q_f(t)=
\begin{cases}
p_{1,9/25,9/25,0,0,0,0},&A\cup B,\\
p_{1,2t-1,2t-1,0,0,0,0},&C,\\
p_{t,3/5,t-2/5,0,0,0,0},&D.
\end{cases}
\]
Use calibrated centers \(q_c(t)=p_{t,3/5,h(t),0,0,0,0}\), where
\[
h(t)=
\begin{cases}
(5t+16)/55,&A,\\
(12-5t)/25,&B\cup C,\\
t-2/5,&D.
\end{cases}
\]
Their nonnegativity and unit mass are tested exactly at each interval endpoint and hence throughout by affine interpolation.

For each interval \(I\) define the **complete six-dimensional joint polytope** of variables \((t,h,u,v,w,z)\) with \(t\in I\), \(s=3/5\), all sixteen Walsh atom nonnegativity constraints. Boundedness follows from every Walsh coefficient of a probability law lying in \([-1,1]\). Every vertex is an intersection of six linearly independent facets among sixteen atoms and two endpoint inequalities. The accompanying independent standard-library Python program exhausts all \(\binom{18}{6}=18564\) potential active sets in each interval, using exact integer Bareiss elimination and rational reconstruction. No floating point and no missing vertex families.

At every exact vertex, the program verifies normalization and nonnegativity of source and both centers, and checks
\[
\mathrm{TV}(p,q_f(t))-\rho_{\rm candidate}(t)\le0,\qquad
\mathrm{TV}(p,q_c(t))-\rho^{\rm cal}_{\rm candidate}(t)\le0.
\]
Both differences are convex (absolute sum of affine expressions minus an affine bound) on the joint polytope. Therefore vertex checks prove the upper bounds over all feasible sources and **all real parameter values**, not just sampled rationals.

| Phase | Candidate bases | Nonsingular | Feasible bases (with repeats) | Distinct exact vertices | Max free/cal excess |
|---|---:|---:|---:|---:|---|
| A | 18564 | 9536 | 424 | 37 | 0 / 0 |
| B | 18564 | 9536 | 392 | 40 | 0 / 0 |
| C | 18564 | 9536 | 392 | 40 | 0 / 0 |
| D | 18564 | 9536 | 724 | 24 | 0 / 0 |

All four intervals PASS; 74,256 active-set combinations in total. Phase D has two interior-parameter vertices at \(t=4/5\), and those are explicitly counted and checked, so this is **not** an endpoint-only test. Matching lower and upper certificates prove the theorem.

## 5. Evidence, limits and next research

Reproduce with Python 3 standard library: \`python3 R749SPF_FULL_RIGHT_PHASE_EXACT_CERT.py\`. The associated full JSON is \`R749SPF_FULL_RIGHT_PHASE_RESULTS.json\`. Locally executed complete exact checker returned PASS and all vertex counts and gaps stated above. This is an author-side exact proof with independent mathematical review pending. Source files and byte-level publication are separately verified in GitHub.

The model is the **auxiliary 16-atom Walsh compatible-source model**. The original frozen scientific input, P000, six-native-axis and three-dimensional-slice semantics remain unchanged. A future native X6/V29/V39 signed-Port/causal-source observer map needs a separate provenance- and update-preserving construction.

**Next scientific question:** determine the two-dimensional zero-gap neighborhood of the returning boundary \((t,s)=(11/15,3/5)\), identify its exact adjacent polygonal walls (if any) and matching dual certificates, and examine whether the four-branch BRC carrier can be mapped losslessly to a specific native event alphabet. Do not replay older same-slice proofs or infer a native promotion from this auxiliary result.
