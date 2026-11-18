# OAI7 r305 — Weighted-average conditional coverage and enlarged exceptional budget

Date: 2026-11-18. Status: Driver-authored mathematical proof, not independent Native Result admission. Provenance: continuing r304 under contributor EM-DVR-DEBB5E; preserve predecessor OAI7 researcher EM-EMF6D046-5A2844 and existing scientific source pins.

## Exact source and statement

Source: \`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a\`, \`preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex\`, theorem \`thm:transfer\` (Git blob \`9deffea159476e7b2c6dfb115abd8d832f87569f\`). Retain that theorem's lattice, signed coordinate homomorphisms, randomly chosen signed subsets, variable \(A\), position \(Y=y(A)\), conditionally iid displacements \(h_1,\ldots,h_n\mid A=a\sim\nu_a\), common data \(\mathcal H=(h_1,\ldots,h_n)\), terminal point \(Z=Y+h_1\), and every entropy/sample-size/log inequality except its original \(\eta'\) bound.

Define \(C(a,c)=1\) if the conditional terminal coordinate \(\phi_c(y(a)+h_1)\mid A=a\) fails \((\tau+4\delta,\beta')\)-coverage; otherwise \(C(a,c)=0\). In place of *every exact \(a\)* having at most an \(\eta'\) fraction of bad coordinates, require only

\[
\boxed{\mathbb E_A\!\left[\frac{1}{2k}\sum_c C(A,c)\right]\le\eta'.}\tag{A}
\]

The fixed-start experiment that determines the law of \(A\) is chosen before applying (A). Replace \(\eta'\le\eta\delta/100\) by the sharper sufficient bound

\[
\boxed{\eta'\le\eta\left(\frac{\delta}{\tau+\delta}-\frac{\delta}{100}-\frac{\delta}{2}\right).}\tag{B}
\]

Under all unchanged hypotheses, the original conclusion follows: at most an \(\eta\) fraction of signed coordinates fail \((\tau,\beta)\)-coverage for \(\phi_c(Z)\). Since \(0<\tau\le3/8\) and \(0<\delta\le1/64\),

\[
\frac{\delta}{\tau+\delta}-\frac{\delta}{100}-\frac{\delta}{2}\ \ge\ \frac{41}{20}\delta.
\]

Thus one convenient uniform sufficient choice is \(\eta'\le(41/20)\eta\delta\), allowing **205 times** the original exceptional-coordinate budget \(\eta\delta/100\), with the same conclusion and all other parameters unchanged.

## Proof

Let \(\mathcal D\) be the set of deficient unconditional terminal signed coordinates, with fraction \(\theta=|\mathcal D|/(2k)\). Assume \(\theta>\eta\). For each \(c\in\mathcal D\), choose the original set \(K_c\) of \(u_p=\lceil p^{1-\beta}\rceil\) terminal residues of probability \(<\tau/p\). Use the original common-data list

\[
\mathcal L_c(\mathcal H)=
\left\{x:\sum_{\ell=1}^n {\bf1}_{\{x+\phi_c(h_\ell)\in K_c\}}
\le n(\tau+\delta)u_p/p\right\}.
\]

Every \(Y+h_\ell\) has terminal law \(Z\); Markov gives, independently of whether the trials are unconditionally independent,

\[
\Pr\{\phi_c(Y)\in\mathcal L_c\}\ge a_0:=\frac{\delta}{\tau+\delta}.
\]

At an exact \(a\) with \(C(a,c)=0\), the unchanged incidence estimate and conditional-iid Chernoff/union bound imply

\[
\Pr\{|\mathcal L_c|>p^{1-\beta'/2}\mid A=a\}\le\delta/100.
\]

At a bad \(a\), use the trivial bound \(1\). Averaging, for every deficient \(c\),

\[
\Pr\{|\mathcal L_c|>p^{1-\beta'/2}\}\le
\delta/100+\Pr\{C(A,c)=1\}.
\]

Assumption (A) implies

\[
\frac{1}{|\mathcal D|}\sum_{c\in\mathcal D}\Pr\{C(A,c)=1\}
\le\frac{\eta'}{\theta}.
\]

Let \(a_c\) denote the probability that the true residue lies in a list no larger than \(p^{1-\beta'/2}\), and let \(\overline a\) be its mean over deficient coordinates. Consequently,

\[
\overline a\ge \frac{\delta}{\tau+\delta}-\frac{\delta}{100}-\frac{\eta'}{\theta}
>\frac{\delta}{2},
\]

where the last inequality follows from \(\theta>\eta\) and (B). Apply the original short-list entropy lemma to each \(c\), then average over \(\mathcal D\). Concavity of binary entropy gives \(\overline{h(a_c)}\le h(\overline a)\le\overline a\log(2e/\delta)\). The unchanged logarithmic condition then gives a mean conditional entropy deficit at least \(\delta\beta'\log T/8\) over deficient coordinates. All other deficits are nonnegative. Since \(\overline L\le\log(2T)\le2\log T\), the mean over all \(2k\) coordinates is strictly greater than \(\eta\delta\beta'\overline L/16\), contrary to the unchanged shared-data budget \(\epsilon+\kappa\le\eta\delta\beta'/16\). Therefore \(\theta\le\eta\).

For the constant, \(\tau+\delta\le3/8+1/64=25/64\), so \(\delta/(\tau+\delta)\ge(64/25)\delta\); subtracting \(\delta/100+\delta/2\) leaves \((41/20)\delta\). At \(\tau=3/8,\delta=1/64\), exact rational arithmetic yields \(\delta/(\tau+\delta)=1/25\) and \(1/25-\delta/100-(41/20)\delta=1/128=\delta/2\).

## Separation of hypotheses and next scientific interface

(A) is genuinely weaker than uniform-in-\(a\) coverage: for example, an exceptional checkpoint of probability \(w\) may have all coordinates deterministic while all other checkpoints have uniform conditional terminal laws. Its average bad-coordinate fraction is \(w\) but its worst-exact-checkpoint bad fraction is \(1\). This example demonstrates non-equivalence of the local assumptions, rather than claiming a complete example satisfying every other transfer inequality.

The external Gaussian-prime schedule proves coverage from **every** exact start; that existing stronger construction already supplies the pointwise hypothesis. A new scheme using (A) must verify the weighted-average bound separately from every fixed start at which the claimed conclusion is required. This result concerns the finite-abelian transfer interface and does not assert a native X6/Port/Link realization.

All arguments are explicit; no \`sorry\`, \`admit\`, or custom target axiom.
