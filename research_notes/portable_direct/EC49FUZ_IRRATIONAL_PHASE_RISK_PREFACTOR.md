# EC49FUZ — irrational lattice phase and sharp second-order minimax risk prefactor

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_RATIONAL_VALUATION_WITNESS / FINITE_FRACTION_CHECKED / ASYMPTOTIC_ARGUMENT / PARENT_DEPENDENT / NOT_REVIEWED.

Scientific pin: BRC16943 frozen \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Direct predecessor EC49FUY, Draft PR #2864, commit \`b2ea28d6b5d7ff7b7016bf6f6cdabbe0e70cd143\`. Parent endpoint-dual reduction: EC49FUQ/FUR, author-proved and not independently reviewed. This work uses only the frozen Bernoulli observation model, not a new native X6 dynamics claim.

## Statement and exact input

Use the predecessor notation
\[
E=\frac{31597745}{1653649},\quad \beta=\frac3{637},\quad
u_\theta=\frac{21829245984}{45529434409-456083905\theta},
\]
\[
T_\theta(x)=(1-x)(1-\beta x+\beta\theta x),\quad
p_\theta=1-T_\theta,\quad q_\theta=1-u_\theta T_\theta.
\]
Fix \(\displaystyle x=\frac7{20}\) and let
\[
a=p_0=\frac{983}{2800},\qquad
b=q_E=\frac{122610119576}{203307125225}.
\]
As in EC49FUY, the other endpoint parameters obey \(0<p_E<a<b<q_0<1\).
Define
\[
R=\frac{1-a}{1-b}=\frac{642450515711}{392959331856},\quad
S=\frac{b(1-a)}{a(1-b)}
=\frac{9686199446504}{3448919850129},
\]
\[
A=\log S,\qquad t=\frac{\log R}{A},\qquad
C=D(t\Vert a)=D(t\Vert b),
\]
\[
r_a=\frac{a(1-t)}{t(1-a)}\in(0,1),\qquad
r_b=\frac{b(1-t)}{t(1-b)}>1,
\]
\[
L=\frac{r_a(1-r_b^{-1})}{1-r_a},\qquad
c=\frac{\log L}{A},\qquad
d_n=\lceil nt+c\rceil-nt\in[c,c+1).
\]
The convention at an integer switching phase chooses the right-hand representative; the prefactor is continuous across that identification.

Put
\[
\boxed{\quad h(d)=\frac{1}{2\sqrt{2\pi t(1-t)}}\,
\frac{r_b^d}{1+e^{Ad}}
\left(\frac1{r_b-1}+\frac1{1-r_a}\right).\quad} \tag{1}
\]
This is a positive, continuous function on the circle obtained by identifying \(d=c\) and \(d=c+1\).

**Theorem A — irrationality certificate.** The exact \(t\) above is irrational. Consequently \(\{nt\}\) is dense in \([0,1]\). Under the endpoint-dual reduction of FUQ/FUR, the set of accumulation points of all exact least-favorable endpoint weights (for arbitrary selection when the finite game has ties) is **exactly**
\[
\boxed{
\left[\frac1{1+e^{A(c+1)}},\;\frac1{1+e^{Ac}}\right].
} \tag{2}
\]
This strengthens the two-subsequence nonconvergence result of EC49FUY.

**Theorem B — second-order risk with nonvanishing phase.** Let \(V_n(7/20)\) be the equal-prior common-nuisance composite minimax error probability. Conditional on the same endpoint-only reduction as EC49FUY, there exists a constant \(K<\infty\) depending only on these fixed exact parameters such that, for all sufficiently large \(n\),
\[
\boxed{
V_n(7/20)=\frac{e^{-nC}}{\sqrt n}
\left[h(d_n)+O(n^{-1})\right].
} \tag{3}
\]
The \(O(n^{-1})\) is **uniform in the lattice phase** (including the exceptional phase); hence the original risk error is \(O(e^{-nC}n^{-3/2})\). The elementary cross-pair Bernoulli subgame version of (3) is unconditional within that subgame.

Moreover, the set of accumulation points of \(\sqrt n e^{nC}V_n(7/20)\) is exactly
\[
\boxed{[\,h(c),h(d_*)\,]},\qquad
d_*=\frac1A\log\left(\frac{\log r_b}{-\log r_a}\right)\in(c,c+1). \tag{4}
\]
In particular this normalized risk **does not converge**, although its leading exponential rate does. These statements are for fixed width \(7/20\); no uniformity in width is asserted.

## Proof of Theorem A (exact integer witness)

The displayed fractions are obtained by rational substitution, without floating-point operations. Check
\[
29\mid642450515711,\quad
29\nmid392959331856,\quad
29\nmid9686199446504,\quad
29\nmid3448919850129.
\]
Thus \(v_{29}(R)=1\) and \(v_{29}(S)=0\). If \(t=p/q\) were rational, \(q\ge1\) and \(R^q=S^p\). Taking the 29-adic valuations gives \(q=0\), contradiction. Hence \(t\) is irrational. Kronecker's elementary one-dimensional rotation lemma yields density of the fractional phases.

EC49FUY proves, for each nonexceptional limit phase \(\rho\), convergence of every finite maximizing weight along \(\{nt\}\to\rho\) to
\[
\Lambda(\rho)=\frac1{1+\exp(A[\lceil c+\rho\rceil-\rho])}.
\]
As \(\rho\) traverses either open continuity interval, the bracket traverses \((c,c+1)\); its image is the open interior of (2). Both endpoints are subsequential limits by approaching the exceptional phase from opposite sides, using a diagonal choice of \(n\) based on phase-density and the already-proved subsequence stability. At the exceptional phase, the limiting dual maximizer set is the closed segment (2); compact-uniform convergence of the normalized dual and compact confinement of its maximizers exclude further limit values. This proves exactly (2) without claiming that every finite \(n\) has a unique maximizing weight.

## Proof of Theorem B

Write \(P_{n,z}(k)=\binom nk z^k(1-z)^{n-k}\). For the cross-pair simple-mixture Bayes subgame,
\[
G_n(\lambda)=\frac12\sum_{k=0}^n
\min\{(1-\lambda)P_{n,a}(k),\lambda P_{n,b}(k)\},
\quad M_n=\max_{\lambda\in[0,1]}G_n(\lambda).
\]

**Uniform local lattice approximation with rate.** Put \(m=k-\lfloor nt\rfloor\) and \(\rho_n=\{nt\}\). Stirling's formula with its standard uniform \(O(1/n)\) remainder, followed by Taylor expansion of \(D(z\Vert a),D(z\Vert b)\) at \(t\), gives, for \(|m|\le n^{1/3}\),
\[
\sqrt n\,e^{nC}P_{n,a}(\lfloor nt\rfloor+m)
=\frac{r_a^{m-\rho_n}}{\sqrt{2\pi t(1-t)}}
\left[1+O\left(\frac{1+m^2}{n}\right)\right],
\]
and the analogous expression with \(a,r_a\) replaced by \(b,r_b\). Constants are independent of \(m,n,\rho_n\) in this range. For \(m\ge0\), the \(a\)-binomial right-hand mass ratios are uniformly bounded above by a fixed \(r'_a<1\) for all large \(n\). For \(m<0\), the \(b\)-binomial left-hand ratios are uniformly bounded by a fixed \(1/r'_b<1\). The minimum is controlled by the \(a\) mass on the right and the \(b\) mass on the left. Hence the portion \(|m|>n^{1/3}\) of the scaled overlap is \(O(e^{-\kappa n^{1/3}})\), uniformly in \(\lambda\). Summing the local errors weighted by these geometric tails yields
\[
\sup_{\lambda\in[0,1]}
\left|\sqrt n e^{nC}G_n(\lambda)-H_{\rho_n}(\lambda)\right|
\le K_0/n, \tag{5}
\]
where
\[
H_\rho(\lambda)=\frac1{2\sqrt{2\pi t(1-t)}}
\sum_{m\in\mathbb Z}
\min\{(1-\lambda)r_a^{m-\rho},\lambda r_b^{m-\rho}\}.
\]
Uniformity across the breakpoints follows from the 1-Lipschitz property of \(\min\) in the two masses, not from differentiating a nonsmooth optimizer.

**Exact supremum of the bilateral geometric sum.** EC49FUY identifies a maximizing kink \(j=\lceil c+\rho\rceil\), at
\[
\lambda_j=\frac1{1+e^{A(j-\rho)}}.
\]
At this kink the two weighted masses at \(m=j\) coincide. Summing the lower \(b\)-geometric tail \(m<j\) and upper \(a\)-geometric tail \(m\ge j\), their common boundary mass is \(r_b^{j-\rho}/(1+e^{A(j-\rho)})\). Therefore
\[
\max_\lambda H_\rho(\lambda)=h(\lceil c+\rho\rceil-\rho). \tag{6}
\]
At the exceptional phase there is a plateau of optimizers, but its **value** is still (6).
Since \(e^{Ac}=L\), the elementary identity
\[
r_b(1+e^{Ac})=1+e^{A(c+1)}
\]
gives \(h(c+1)=h(c)\), including the jump-point agreement.

**Transfer to the full composite endpoint mixture.** Write
\[
F_n(\lambda)=\frac12\sum_{k=0}^n
\min\{(1-\lambda)P_{n,a}(k)+\lambda P_{n,p_E}(k),\,
(1-\lambda)P_{n,q_0}(k)+\lambda P_{n,b}(k)\}.
\]
The endpoint-reduction premise asserts \(V_n=\max_\lambda F_n(\lambda)\). Clearly \(F_n\ge G_n\).
Choose \(\delta>0\) so small that every maximizer of every phase-function \(H_\rho\) lies in \([3\delta,1-3\delta]\). By continuity of \(H_\rho\) on the phase-circle, its strict increase on the far-left interval and strict decrease on the far-right interval are uniform. On compact \(\lambda\)-intervals inside \((0,1)\), the cross-pair Bayes boundary equals \(nt+O_\delta(1)\). Applying this cross-pair Bayes test to the full mixture adds only the two positive error tails
\[
\lambda P_{n,p_E}\{K\ge nt+O_\delta(1)\}
+(1-\lambda)P_{n,q_0}\{K<nt+O_\delta(1)\}.
\]
The strict gaps \(D(t\Vert p_E)>C\) and \(D(t\Vert q_0)>C\) bound these tails by \(O(e^{-n(C+\eta)})\) for some \(\eta>0\) uniformly on \([\delta,1-\delta]\). Thus
\[
0\le F_n(\lambda)-G_n(\lambda)
\le K_1e^{-n(C+\eta)}
\qquad(\delta\le\lambda\le1-\delta). \tag{7}
\]
For sufficiently large \(n\), (5)–(7) also give \(F_n(2\delta)>F_n(\delta)\) and \(F_n(1-2\delta)>F_n(1-\delta)\), with the inequalities taken inside the compact interior. Concavity of \(F_n\) then confines *all* its maximizers to \([\delta,1-\delta]\). Maximizing (5), using (6) and (7), gives
\[
\sqrt n e^{nC}\max_\lambda F_n(\lambda)=h(d_n)+O(1/n)
\]
uniformly in \(\rho_n\). This is (3).

**Complete prefactor range.** The log of the \(d\)-dependent factor in (1) has derivative
\[
\frac{d}{dd}\log h(d)
=\log r_b-\frac{Ae^{Ad}}{1+e^{Ad}},
\]
and negative second derivative \(-A^2e^{Ad}/(1+e^{Ad})^2\). Thus \(h\) is strictly log-concave on \([c,c+1]\), with equal endpoint values and unique interior maximum at \(d_*\) in (4). Since \(\{nt\}\) is dense and the jump is glued by equality of endpoint values, the limit-point set of \(h(d_n)\) is exactly the range (4). The uniform \(O(1/n)\) error transfers this exact accumulation set to the normalized minimax risk.

## Finite checks, scope, and next problem

Companion \`EC49FUZ_PHASE_PREFACTOR_VERIFY.py\` uses standard-library \`Fraction\` to certify the exact \(R,S\) identities, the 29-adic valuation obstruction, four finite \(n\) exact endpoint dual optimizations and cross-pair comparisons. Its logarithms, prefactor evaluations and decimal display are explicitly numerical crosschecks; the universal asymptotics follow from the proof above. Example orientation (floating displays):
\[
t\approx0.476045064293,\quad C\approx0.032883732402,
\]
\[
\operatorname{Acc}(\lambda_n)\approx[0.375678958792,0.628248755001],
\]
\[
\operatorname{Acc}(\sqrt n e^{nC}V_n)\approx
[0.765045670356,0.790681027223].
\]
In the **full** game, the finite \(n=30,50,80,100\) weights are not expected to track the limiting phase precisely because the extra cross-endpoint tails decay at a separate exponential gap. They are preserved as exact finite checks, not used as a proof of the limit.

P000 remains the protected six-native-axis/one-time-axis, three-dimensional-slice starting model. The present binomial hit observer is a typed, lossy readout; its lattice phase is an observer-relevant residual and does not promote a Bernoulli variable to a complete X6/BRC state.

Outstanding: obtain effective numerical bounds on the constants \(K,\eta,N\); classify scaling regimes \(x=x_n\to0\) or \(x_n\to1\); examine whether other rational widths yield explicit prime-valuation irrationality witnesses and whether some lead to rational phases.

Publication is independent portable research only. Provenance of predecessor remains EM-DIRECT-8454C6 / MCP-44cfc4e6f2094f96861854ebefc77e84 / RA-ED136F89271FD89288F3E58D; those historical identifiers are **not** asserted as this run's authenticated native identity. No new CLAIM, Result, Activity checkpoint or independent Review is claimed.
