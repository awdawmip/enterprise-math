# R749SMX — Disjoint-complement Walsh fibers: exact boundary minimax and future-observer residual

Date: 2026-11-13 (Asia/Shanghai). Independent author-side continuation of R749SMQ–SMW, particularly the disjoint-edge point R749SMW, in draft PR #2233. Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Current behavioral rules were separately read. The following $\mathbb F_2^4$ is an auxiliary signed-source observer, not a new P000 spatial axis or native V29/V39 Cell/Link/Port event. Independent scientific review is pending.

## Definitions and complete five-parameter fiber

Write $G=\mathbb F_2^4$, $\chi_a(x)=(-1)^{a\cdot x}$ and $C=\{1,2,4,8,15\}$. Retain the ten Walsh moments indexed by $B=\{3,5,6,7,9,10,11,12,13,14\}$. Specify $m_3=t$, $m_{12}=s$ and all eight other B moments zero. The masks 3 and 12 are disjoint edges in the $K_5$ representation of the ten pairwise sums of C.

Use independent binary sign coordinates $A=\chi_3$, $D=\chi_{12}$, $P=\chi_1$ and $Q=\chi_4$. Every $(A,D,P,Q)\in\{\pm1\}^4$ determines exactly one source label. The five omitted C characters become $\chi_1=P$, $\chi_2=AP$, $\chi_4=Q$, $\chi_8=DQ$, $\chi_{15}=AD$.

**Theorem 1.** For every real $t,s\in[-1,1]$, the complete compatible source fiber is
\[
\mu(A,D,P,Q)=\frac{1+tA+sD+hAD+uP+vAP+wQ+zDQ}{16},
\]
where $(h,u,v,w,z)\in\mathbb R^5$ satisfy exactly four inequalities:
\[
1+tA+sD+hAD\ge |u+vA|+|w+zD|\quad
\text{for every }(A,D)\in\{\pm1\}^2. \tag{1}
\]
In particular the permissible $h=\mathbb E[AD]$ necessarily satisfies
\[
-1+|t+s|\le h\le1-|t-s|. \tag{2}
\]
Every $(t,s)\in[-1,1]^2$ is feasible.

**Proof.** Full Walsh inversion on the sixteen source labels fixes the coefficients of the constant, $\chi_3,\chi_{12}$, and the remaining eight members of B, leaving exactly the five coefficients in C free. Rewriting these five in the independent $(A,D,P,Q)$ coordinates gives the displayed formula and uniqueness. For fixed $(A,D)$, minimizing its numerator over $(P,Q)$ gives precisely the left side of (1) minus its right side; hence (1) is both necessary and sufficient for sixteen probabilities to be nonnegative. Their sum is automatically one. Summing the formula over $(P,Q)$ yields marginal sign-cell probability $(1+tA+sD+hAD)/4$, whose positivity gives (2). Choosing $h=ts$ and $u=v=w=z=0$ yields $(1+tA)(1+sD)/16$, a valid law for each $(t,s)$; this also proves feasibility. QED.

## Every deterministic boundary edge has an exact nonlinear radius

Let $F_B(t,s)$ denote that fiber and
\[
\rho_B(t,s)=\inf_{q\in\Delta(G)}\sup_{\mu\in F_B(t,s)}
\operatorname{TV}(q,\mu),\quad
\operatorname{TV}(p,q)=\tfrac12\sum_x|p_x-q_x|.
\]

**Theorem 2.** For either $\varepsilon\in\{-1,+1\}$ and every real $s\in[-1,1]$,
\[
\boxed{\rho_B(\varepsilon,s)=\frac{1-|s|}{2}.} \tag{3}
\]
More precisely, the entire fiber is the segment
\[
\mu_u(A,D,P,Q)=
\mathbf1_{A=\varepsilon}\frac{1+sD+uP}{8},
\qquad |u|\le1-|s|, \tag{4}
\]
and the midpoint $\mu_0$ is minimax optimal.

**Proof.** As $\mathbb E[A]=\varepsilon$, every compatible law is supported on $A=\varepsilon$. On the two zero-mass cells $A=-\varepsilon$, (1) forces $h=\varepsilon s$, $u=\varepsilon v$ and $w=z=0$. The remaining eight probabilities become (4), all nonnegative exactly when $|u|\le1-|s|$. Thus the asserted segment describes **all** compatible laws. With $r=1-|s|$, its endpoints $\mu_{\pm r}$ have mutual total variation distance $r$ and the midpoint has distance at most $r/2$ from every member. The triangle inequality forces every decoder to incur at least $r/2$ against one endpoint. Equality follows. QED.

Permuting the two disjoint edges by the GL(4,2) source automorphism swapping the relevant circuit pairs gives the other deterministic boundary edges:
\[
\boxed{\rho_B(\pm1,s)=\frac{1-|s|}{2},\qquad
\rho_B(t,\pm1)=\frac{1-|t|}{2}.} \tag{5}
\]
The four corners have zero ambiguity. At $(\pm1,0)$ and $(0,\pm1)$ the radius is $1/2$, consistent with R749SMS. R749SMW's strictly interior calculation $\rho_B(1/2,1/2)=2/5$ is a separate known checkpoint.

On the edge $A=\varepsilon$, the **only** unresolved source moment is $u=\mathbb E[\chi_1]$; the other C moments are
\[
\mathbb E[\chi_2]=\varepsilon u,\quad
\mathbb E[\chi_4]=\mathbb E[\chi_8]=0,\quad
\mathbb E[\chi_{15}]=\varepsilon s.
\]
For $|s|<1$ retaining one further scalar $u$ reconstructs the entire source law exactly; for $|s|=1$ it is already unique.

## Exact future-operation criterion

For an arbitrary finite stochastic future observer $K:Y\leftarrow G$, define the signed contrast
\[
d_\varepsilon(x)=\mathbf1_{\chi_3(x)=\varepsilon}\frac{\chi_1(x)}8,
\quad \sum_xd_\varepsilon(x)=0.
\]
The edge-fiber laws satisfy $\mu_u=\mu_0+ud_\varepsilon$.

**Theorem 3.** The optimal worst-case prediction loss for the **complete future K output distribution**, conditional on the retained B moments with $t=\varepsilon$, is
\[
\boxed{\rho_K(\varepsilon,s)=\frac{1-|s|}{2}
\sum_{y\in Y}\left|
\sum_{x:\chi_3(x)=\varepsilon}\frac{\chi_1(x)}8K(y|x)
\right|.} \tag{6}
\]
An optimal output prediction is $K\mu_0$. For $|s|<1$, deleting the unresolved $u$ is exactly lossless for the chosen K **iff**
\[
\sum_{x:\chi_3(x)=\varepsilon}\chi_1(x)K(y|x)=0
\quad\text{for every }y\in Y. \tag{7}
\]

**Proof.** The image $K(F_B)$ is exactly the segment $K\mu_0+uKd_\varepsilon$, $u\in[-r,r]$ with $r=1-|s|$. Its endpoints have TV distance $r\sum_y|(Kd_\varepsilon)_y|$. The midpoint $K\mu_0$ attains one-half this distance against every point; the triangle inequality makes half the endpoint distance a universal lower bound. The resulting expression is (6), and it vanishes (when $r>0$) exactly under (7). QED.

If future K only observes $(A,D)$, then $Kd_\varepsilon=0$ and the compression is prediction-lossless. If K outputs a binary signed measurement of P with $\Pr(Y=y|x)=(1+y\lambda P(x))/2$, $|\lambda|\le1$, the exact prediction radius is $(1-|s|)|\lambda|/2$. This turns the missing named-Port moment into a quantified observer-dependent residual rather than a generic compression failure.

## Evidence, coverage and continuation

The companion standard-library Python file \`R749SMX_DISJOINT_PAIR_BOUNDARY_EXACT_CHECK.py\` uses integers and fractions.Fraction, with output in \`R749SMX_DISJOINT_PAIR_BOUNDARY_RESULTS.json\`. The execution returned PASS: 78,125 seven-parameter rational grid profiles compare all sixteen positivity inequalities with the four grouped conditions; 90 boundary probability/moment/TV checks cover both signs and nine rational s values; 150 three-output future stochastic-channel profiles verify (6), including zero and nonzero retained sensitivity. The analytical proofs above establish (1)–(7) for the full stated real-parameter ranges. A finite grid alone is not used to infer a continuum result.

Next: solve the **interior** disjoint-edge minimax $\rho_B(t,s)$, starting from exact $t=s=1/2$ from R749SMW. The five-variable four-inequality representation offers a reduced finite LP/dual certificate search. Afterwards address the full global nonlinear B risk and composition with licensed native V29/V39 Port observations. This artifact is author-side mathematical evidence, without a shared Task CLAIM, native event promotion, or independent review.
