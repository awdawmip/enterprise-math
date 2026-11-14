# R749SOQ — Exact Walsh common floor on the unit square and zero calibration gap on both axes

**2026-11-14.** Author-side exact mathematics; **NOT_REVIEWED**. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Independent auxiliary 16-state Walsh source/observer model. Scientific predecessors: R749SOP (Draft PR #2392, head eeba38373007e38d89f0e965904b3b0f4732745e, upper-triangle common-floor decomposition); R749SOF (#2370, real-line minimax theorem). No claim of a faithful native X6/V29/V39 mapping or P000 alteration.

## 1. Model

Let G=F_2^4, with \(\chi_m(k)=(-1)^{\operatorname{popcount}(k\mathbin{\&}m)}\), \(A=\chi_3\), \(B=\chi_{12}\), \(C=\chi_{15}=AB\). The fiber \(F_{t,s}\), for \(0\le t,s\le1\), consists of all nonnegative normalized laws

\[
\mu_{t,s,h,u,v,w,z}(k)=
\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

Define \(\rho(t,s)=\min_{q\in\Delta_{16}}\max_{\mu\in F_{t,s}}\mathrm{TV}(q,\mu)\) and \(\rho^{cal}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}\mathrm{TV}(q,\mu)\), where \(\mathrm{TV}(p,q)=\frac12\sum_k|p_k-q_k|\). The pointwise greatest shared subprobability floor is \(\ell_{t,s}(k)=\min_{\mu\in F_{t,s}}\mu(k)\).

## 2. Theorem: exact coordinatewise common floor for the entire unit square

For **all real** \(0\le t,s\le1\) and every atom \(k\),

\[
\boxed{\ell_{t,s}(k)=
\begin{cases}
(t+s-1)/4,& t+s\ge1\ \text{and}\ A(k)=B(k)=+1,\\
0,&\text{otherwise}.
\end{cases}}
\]

Thus the total greatest common subprobability mass is \(\max(t+s-1,0)\).

**New lower-triangle proof.** Fix an atom \(k_0\), write \(x=\chi_1(k_0)\) and \(y=\chi_4(k_0)\), and construct

\[
p_{00}=(1-x\chi_1)/16,\quad
p_{10}=(1+A)(1-x\chi_1)/16,\quad
p_{01}=(1+B)(1-y\chi_4)/16.
\]

By character orthogonality each is a nonnegative unit-mass source law. The products expand in the original allowed seven-character span because \(A\chi_1=\chi_2\) and \(B\chi_4=\chi_8\). Their retained moment pairs are respectively \((0,0),(1,0),(0,1)\). Each **vanishes at the chosen atom** \(k_0\). For every \(t+s\le1\), the source \((1-t-s)p_{00}+tp_{10}+sp_{01}\) belongs to \(F_{t,s}\) and vanishes at \(k_0\). Since \(k_0\) is arbitrary and all probabilities are nonnegative, the lower envelope is zero at each coordinate. This is an analytic proof on the complete real lower triangle.

**Upper triangle.** For \(t+s\ge1\), put \(\alpha=t+s-1\) and \(\beta=2-t-s\). The exact nonnegative four-sign identity proved in R749SOP gives \(F_{t,s}=\alpha\{\sigma\}+\beta F_{(1-s)/\beta,(1-t)/\beta}\), for \(\beta>0\), where \(\sigma=\mu_{1,1,1,0,0,0,0}\) has mass \(1/4\) on each of the four \(A=B=+1\) atoms and zero elsewhere. This makes \(\alpha\sigma\) a common floor. For sharpness the anti-diagonal source \(\nu=\mu_{a,b,0,a,a,b,b}\), \(a+b=1\), has a zero in every \(A,B\) sign orbit, and index translations by 3 and 12 preserve \(A,B\) while moving these zeros to each requested atom. Hence the common lower envelope of the residual source family is zero; the exact floor is \(\alpha\sigma\). At \((t,s)=(1,1)\), \(\beta=0\), the fiber is the singleton \(\{\sigma\}\). This proves the whole-square theorem.

## 3. Theorem: exact axis radii and zero calibration penalty

For **every real** \(s\in[0,1]\),

\[
\boxed{\rho(0,s)=\rho^{cal}(0,s)=1/2}.
\]

By swapping the two two-bit blocks, also \(\rho(t,0)=\rho^{cal}(t,0)=1/2\) for **every real** \(t\in[0,1]\).

**Matching analytic lower bound.** Two compatible sources are

\[
p_\pm(k)=\frac{(1\pm\chi_8(k))(1\pm s\chi_4(k))}{16}.
\]

Each has retained \(A\)-moment zero and \(B=\chi_4\chi_8\)-moment \(s\), since their expanded coefficients are \((s,h,u,v,w,z)=(s,0,0,0,\pm s,\pm1)\). Both are nonnegative and normalized. Their supports are disjoint; thus \(\mathrm{TV}(p_+,p_-)=1\). The TV triangle inequality forces every free or calibrated decoder to have worst-case radius at least \(1/2\).

**Exact upper bound.** The calibrated center \(q_s=(1+sB)/16\) belongs to the same fiber. The joint polytope in six real variables \((s,h,u,v,w,z)\) has sixteen affine source-atom inequalities and \(0\le s\le1\): in total 18 facets. It is bounded because each coefficient is the expectation of a \(\pm1\) Walsh character, and is full-dimensional since \(0<s<1\), \(h=u=v=w=z=0\) is strictly feasible. The function \((s,h,u,v,w,z)\mapsto \mathrm{TV}(\mu,q_s)\) is convex, so its maximum over the entire joint polytope occurs at an extreme point. Each vertex has six independent active facets. The attached exact checker exhausts all \(\binom{18}{6}=18564\) six-facet subsets, uses fraction-free integer Bareiss elimination and exact rational feasibility checks, and evaluates all deduplicated vertices:

| Certificate | Exact result |
|---|---:|
| Active six-facet subsets | 18,564 |
| Nonsingular bases | 9,536 |
| Feasible bases | 2,480 |
| Distinct vertices | 32 |
| Vertices at s=0 / s=1 / 0<s<1 | 26 / 2 / 4 |
| Bound-tight vertices | 12 |
| Maximum TV(mu,q_s) | **1/2** |
| Bound violations | **0** |

Therefore \(q_s\) has worst-case radius at most \(1/2\) for **every real** \(s\in[0,1]\). The explicit disjoint-support sources attain the bound. Interchanging the two bit-pairs yields the second axis theorem.

## 4. Distinction, evidence, and next frontiers

The common-floor boundary \(t+s=1\) is distinct from the calibration-gap boundary: the axes have \(g=\rho^{cal}-\rho=0\) while the previously proved frozen-model result at \((1/2,1/2)\) gives \(g=1/110>0\). In the full lower triangle the common floor is zero, so the *positive shared mass* homothety used in R749SOP has no direct extension below the anti-diagonal.

Run the accompanying standard-library Python 3 program R749SOQ_EDGE_FLOOR_EXACT_CHECK.py and compare stdout to R749SOQ_EDGE_FLOOR_RESULTS.json. The program performs complete integer/rational vertex enumeration, five exact disjoint-support witness checks and 96 exact atom-zero checks. The entire lower-triangle floor proof is analytic; the entire real-axis upper bound follows from complete polytope vertex enumeration and convexity. **Scientific evidence status:** AUTHOR_EXACT_NOT_REVIEWED; native X6/V29/V39 correspondence remains unresolved.

Next work: determine the exact minimax germ as \(t\to0^+\) at fixed \(s=1/2\), including the first positive-gap transition if present. This is a new lower-triangle question distinct from the already solved upper triangle. Preserve native source, branch and signed-port information when considering a future typed native observer.