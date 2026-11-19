# OAI7 r397 — Cluster-relative KL certificate for the original iid Gaussian auxiliary list

Date: 2026-11-20. Target \`RS-OAI7-028-C-20261007-6F2A81\` / \`TP2-96FAC49786245691AE19\`. Scientific status: **author-side derived theorem and exact finite-rational diagnostic**, not native independent review or Gaussian schedule improvement. This directly strengthens the usable certificate in [r396](2026-11-20_oai7_028c_information_theoretic_cost_refinement_r396.md), preserving the original conditional-iid sampling mechanism of pinned [\`coverage-transfer.tex\`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex).

## Theorem — the information cost of an iid auxiliary list can be certified by approximate-law clusters

Let \(A\) be a finite exact checkpoint, \(Y=y(A)\) an arbitrary deterministic observable, and \(\nu_a\) a probability law on one common finite alphabet \(\mathcal V\). Conditional on \(A=a\), let \(\mathcal H_n=(h_1,\ldots,h_n)\) comprise \(n\) **independent** samples from \(\nu_a\). Choose any finite deterministic cluster \(C=C(A)\). For each cluster \(c\), choose an arbitrary reference law \(\mu_c\) such that \(\nu_a\ll\mu_{C(a)}\) for all supported \(a\). Then, in nats,
\[
\boxed{
I(Y;\mathcal H_n)\ \le\ I(A;\mathcal H_n)\
\le\ \min\left\{H(A),\,
H(C)+n\mathbb E_A D_{\rm KL}(\nu_A\Vert\mu_{C(A)})\right\}.
}\tag{1}
\]
The tighter intrinsic estimate is
\[
\boxed{I(A;\mathcal H_n)\le
H(C)+n\mathbb E_A D_{\rm KL}(\nu_A\Vert\overline\nu_{C(A)}),}
\quad
\overline\nu_c=\mathbb E[\nu_A\mid C=c],\tag{2}
\]
and the reference-law gap is exactly
\[
\mathbb E[D_{\rm KL}(\nu_A\Vert\mu_C)\mid C=c]
= I(A;h_1\mid C=c)+D_{\rm KL}(\overline\nu_c\Vert\mu_c).\tag{3}
\]
For the information-aware transfer of r396, it follows that
\[
\mathbb E_S I(F_S(Y);\mathcal H_n)
\le H(C)+n\mathbb E D_{\rm KL}(\nu_A\Vert\mu_C).
\tag{4}
\]
Thus its required information budget can be certified by a **cluster-count term plus within-cluster KL divergence** while retaining exactly the original iid trials and their conditional Chernoff inequalities.

### Proof

Since \(Y=y(A)\), data processing gives \(I(Y;\mathcal H_n)\le I(A;\mathcal H_n)\). The chain rule gives
\[
I(A;\mathcal H_n)
=I(C;\mathcal H_n)+I(A;\mathcal H_n\mid C)
\le H(C)+I(A;\mathcal H_n\mid C).
\]
Conditional iid entails
\[
H(\mathcal H_n\mid A,C)=nH(h_1\mid A,C)
\quad\text{and}\quad
H(\mathcal H_n\mid C)\le\sum_{\ell=1}^nH(h_\ell\mid C)
=nH(h_1\mid C).
\]
Therefore \(I(A;\mathcal H_n\mid C)\le nI(A;h_1\mid C)\). For fixed \(c\), the conditional one-trial mixture law is \(\overline\nu_c\), so direct expansion of relative entropy yields
\[
I(A;h_1\mid C=c)
=\mathbb E[D_{\rm KL}(\nu_A\Vert\overline\nu_c)\mid C=c].
\]
Expanding the same expectation relative to any dominating \(\mu_c\) proves (3), as the difference is \(D_{\rm KL}(\overline\nu_c\Vert\mu_c)\ge0\). The universal \(I(A;\mathcal H_n)\le H(A)\) completes (1)–(2). For (4), \(F_S(Y)\) is deterministic given \(Y\), so its mutual information with \(\mathcal H_n\) is bounded by \(I(Y;\mathcal H_n)\) for every independent fixed \(S\). \(\square\)

**Optimal cluster reference.** For a fixed partition \(C\), the exact mixture \(\mu_c=\overline\nu_c\) minimizes the average conditional KL cost, with equality in (3). A simpler surrogate \(\mu_c\) may be used with a certified divergence penalty. In contrast to an \(L^1\)-CDF cluster, KL control needs support domination or an explicit regularization. There is no claim that closeness in CDF alone automatically makes the KL divergence small.

**Quadratic certificate.** Since \(D_{\rm KL}(P\Vert Q)\le\chi^2(P\Vert Q)=\sum_v(P(v)-Q(v))^2/Q(v)\) when \(P\ll Q\), any verified within-cluster \(\chi^2\) bound also certifies (1). If \(C\) equals the **exact** law-type variable, the KL term vanishes and (1) reduces to the r396 \(H(C)\) bound. If \(C\) is constant, (2) gives \(I(A;\mathcal H_n)\le n I(A;h_1)\), with \(I(A;h_1)\) the Jensen–Shannon information of the mixture.

## A 128-law, one-cluster exact-rational separation

Let \(A=j\) be uniform on \(j=0,\ldots,127\), \(C\) constant, and \(h_\ell\in\{0,1\}\), where
\[
\nu_j(1)=p_j=\frac12+\frac{2j-127}{200000},\qquad
\nu_j(0)=1-p_j.
\]
All 128 exact conditional laws are distinct, so the exact law-type entropy is \(H(V)=\log128\approx4.852030264\) nats. The mixture has exactly \(\overline p=1/2\). Finite rational summation gives
\[
\operatorname{Var}(p_A)=\frac{5461}{40000000000},
\quad
\mathbb E\chi^2(\nu_A\Vert(1/2,1/2))
=4\operatorname{Var}(p_A)
=\frac{5461}{10000000000}.
\]
For **\(n=1000\) conditionally iid samples**, (1) therefore yields
\[
\boxed{I(A;\mathcal H_{1000})
\le \frac{5461}{10000000}=0.0005461\ {\rm nats}.}\tag{5}
\]
The exact one-trial Jensen–Shannon information, evaluated only after rational probability construction, is \(\approx2.73050044731\cdot10^{-7}\) nats; using (2) yields the sharper bound \(\approx0.000273050044731\) nats. Both are far below the \(H(V)\) bound. Meanwhile the sample vector itself has large unconditional entropy; the point is that its **information about the checkpoint** is very small.

This example is a finite information-cost certificate, not a Gaussian residue-coverage instance. It proves that large type count does not by itself force high information disclosure.

~~~python
from fractions import Fraction as F
from math import log
J,n=128,1000
p=[F(1,2)+F(2*j-127,200000) for j in range(J)]
mean=sum(p,F(0))/J
variance=sum(((x-mean)**2 for x in p),F(0))/J
chi=variance/(mean*(1-mean))
assert mean==F(1,2)
assert variance==F(5461,40000000000)
assert chi==F(5461,10000000000)
assert n*chi==F(5461,10000000)
kl=sum((float(x)*log(float(x/mean))+
        float(1-x)*log(float((1-x)/(1-mean))))
       for x in p)/J
assert 0<=kl<=float(chi)
print("exact n*chi2",n*chi,"nats:",float(n*chi),
      "n*meanKL",n*kl,"H(type)",log(J))
~~~

## Application criterion and provenance

At an actual Gaussian checkpoint of [pinned \`schedule.tex\`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex), define \(A=A_{i+1}\), \(\nu_a\) as the **entire physical displacement** law from that exact start to the terminal time, and \(n=n_i=\lceil T^{6\beta_i/5}\rceil\). An admissible cluster \(C_i(A)\) with verified
\[
H(C_i)+n_i\mathbb E D_{\rm KL}(\nu_A\Vert\mu_{C_i})
\ \le\ \kappa_i s_iL_*
\]
is sufficient for the information budget in r396's transfer, retaining all of the source's other geometry, conditional coverage and Chernoff-size requirements. The source's original stronger \(\kappa_i\) certificate is already valid; this is an optional **refinement opportunity**. Actual \(\nu_a\), common physical support, exact-start uniformity, and high-\(M\) scaling must be checked before asserting improved Gaussian constants. The cluster may depend on the fixed outside start of the experiment but must be selected before the auxiliary independent signed subset \(S\).

This note extends r396 under precisely stated conditional iid assumptions. It does not assert a new frozen Result, independent review, Source/Activity association, formal Task DONE, or parent-objective closure. Original OAI7 Researcher \`EM-EMF6D046-5A2844\` and existing Driver-side contribution history are preserved.