# OAI7-028-C r399 — Gaussian batch residue profile injectivity and the exact ordering entropy gap

Date: 2026-11-20. Status: **author-side mathematical proof and finite verification; not a frozen/native Result, independent review, or Task closure.**

## Exact external setting and scope

This note continues r398 (common residue-profile histogram). The external object is the pinned finite Gaussian group and checkpoint sampling from:

- openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex;
- same commit, build/schedule.tex;
- Enterprise Math r398@23f2057225777f77409504e19c319e1e9c488176.

The Gaussian ring below is the external mathematical model, **not** a P000-native six-axis identification or a proof of native path/Port transfer. The actual OAI7 Task remains RS-OAI7-028-C-20261007-6F2A81; its Researcher provenance and authority are unaffected.

Let \(\mathcal B_T\) be a finite batch of **distinct odd rational primes splitting in** \(\mathbb Z[i]\). For each \(p\in\mathcal B_T\), fix conjugate, coprime Gaussian prime factors \(\pi_p,\overline{\pi_p}\) of \(p\). Consider the *full common signed profile*

\[
\psi_T:\mathbb Z[i]\longrightarrow
\prod_{p\in\mathcal B_T}
  \bigl(\mathbb Z[i]/(\pi_p)\times\mathbb Z[i]/(\overline{\pi_p})\bigr).
\]
Write \(P_T=\prod_{p\in\mathcal B_T}p\). At an exact-start checkpoint the subsequent physical displacement has a common finite support \(\mathcal D\subseteq\{h\in\mathbb Z[i]:|h|\le R\}\). Conditional on an exact later checkpoint \(A=a\), the \(n\) displacements \(h_1,\ldots,h_n\) are independent with identical law \(\nu_a\) supported in \(\mathcal D\), as in the pinned transfer experiment. Write \(W_j=\psi_T(h_j)\), \(B_w=\#\{j:W_j=w\}\), \(Y=y(A)\), and \(\mathcal H=(h_1,\ldots,h_n)\).

## Theorem 1 — exact full-batch injectivity

If \(P_T>2R\), then the restriction of \(\psi_T\) to \(\mathcal D\) is injective.

**Proof.** Coprimality of the prime ideals above each split \(p\) gives \((\pi_p)\cap(\overline{\pi_p})=(p)\). Distinct rational primes yield comaximal ideals. Consequently

\[
\ker\psi_T=\bigcap_{p\in\mathcal B_T}
((\pi_p)\cap(\overline{\pi_p}))
=(P_T)\subset\mathbb Z[i].
\]

If two support points have the same profile, their difference lies in \((P_T)\), i.e. both integer Cartesian components are multiples of \(P_T\). But \(|h-h'|\le2R<P_T\), so the only possibility is \(h=h'\). QED.

**Application to the pinned schedule.** The prime-count input used in schedule.tex has \(k_T=|\mathcal B_T|\gg T/\log T\), hence \(\log P_T\ge k_T\log T\gg T\). The deterministic displacement support at \(A_{i+1}\) has radius \(R_{i+1}=D S_{i+1}\) with \(\log(1+S_{i+1})=O_D(T^{r_{i+1}})\) and \(r_{i+1}<1/4\). Thus \(\log(2R_{i+1})=O_D(T^{r_{i+1}})=o(T)\). For sufficiently large \(T\), the injection condition holds at every intermediate induction step \(0\le i<J(T)\), uniformly over the exact start times. This uses *all* signed factors in the batch; it does not assert injectivity for one coordinate or for an arbitrarily selected subset \(S\).

## Theorem 2 — exact loss of order, not physical information

Under the conditional iid hypothesis and the injectivity above, the common profile histogram \(B\) and the **unordered multiset of actual physical displacements** are in bijection. Let \(b=(b_w)_w\) range over nonnegative count vectors summing to \(n\), and put

\[
L(b)=\frac{n!}{\prod_w b_w!}.
\]

For every finite mixing law of \(A\) (even when \(Y=y(A)\) is strongly correlated with the sampled displacements),

\[
\boxed{H(\mathcal H)=H(B)+\mathbb E\log L(B)}
\quad\text{and}\quad
0\le H(\mathcal H)-H(B)\le\log n!\le n\log n.
\]

Moreover, for every deterministic observable \(X=f(A)\),

\[
\boxed{I(X;\mathcal H)=I(X;B).}
\]

The identity also holds with \(X=F_S(Y)\) for each fixed signed subset \(S\), and after averaging over an independently chosen \(S\).

**Proof.** For fixed \(A=a\) and histogram \(b\), every one of the \(L(b)\) orderings of the sampled support points has the same conditional mass \(\prod_w \nu_a(\psi_T^{-1}(w))^{b_w}\). Thus the ordering is uniform given \(A=a,B=b\), with a conditional distribution independent of \(a\). Mixing over \(A\) preserves uniformity, so \(\mathcal H\perp A\mid B\) and \(H(\mathcal H\mid B)=\mathbb E\log L(B)\). The profile histogram is a deterministic function of \(\mathcal H\), proving the entropy identity. The Markov chain \(A\to B\to\mathcal H\), together with \(B=f(\mathcal H)\), gives the mutual-information equality by the chain rule. Bounds follow from \(1\le L(B)\le n!\). QED.

This strengthens the scope of the r398 sufficient-statistic statement **in the full Gaussian batch**: even the ordered *raw displacement list* carries no additional information about the exact checkpoint after the unordered histogram has been fixed. It does not make the multiset Shannon entropy small; information and full Shannon cost remain distinct.

## Theorem 3 — the generic entropy-bound improvement has no leading exponent gain

For an arbitrary uniform conditional law on \(m\) distinct support points (a valid abstract finite-displacement model), the exact identity implies

\[
n\log m-\log n!\ \le\ H(B)\ \le\ n\log m.
\]

In particular, whenever \(\log n=o(\log m)\), the uniform-law model has

\[
H(B)=(1-o(1))\,n\log m.
\]

Thus r398's histogram counting bound **alone**, without extra information about the actual checkpoint-conditioned laws, cannot guarantee a leading-order reduction compared with the original \(n\log|\mathcal D|\) support bound. In the original schedule, \(n_i=\lceil T^{6\beta_i/5}\rceil\) and \(\log n_i=O(\log T)\), whereas the available support bound is \(O_D(T^{r_{i+1}})\) with \(r_{i+1}>0.23\). Therefore the maximum universal *order-removal* discount \(n_i\log n_i\) is \(o(n_iT^{r_{i+1}})\).

**Scope caution.** The uniform-law example is a sharpness witness for unrestricted abstract finite-support displacement laws, not a claim that a fixed self-avoiding Gaussian walk realizes that law. Special nonuniform walk laws may have dramatically smaller \(H(B)\). The original schedule already has a sufficient full-data budget, so this result does not disprove its coverage theorem or its constants. It identifies why the r396 information-aware cost \(I(F_S(Y);B)\), or additional structure in the true checkpoint laws, is the discriminating next object.

## Exact finite check

Take \(n=3\), two distinct support points and equiprobable checkpoint types \(A\in\{0,1\}\), with conditional point masses \((1/4,3/4)\) and \((3/4,1/4)\). Exhaust all \(2^3\) ordered words with exact rational probabilities. Direct summation yields:

\[
H(\mathcal H)=1.9964308002122153,\quad
H(B)=1.3784613878364036,\quad
\mathbb E\log L(B)=0.6179694123758117
\]
in nats; the two sides agree at displayed precision, while the probability identities are exact rational.

Reproduction sketch (Python 3, standard library):

~~~python
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import log, factorial, prod
laws = [(F(1,4), F(3,4)), (F(3,4), F(1,4))]
pword, phist = defaultdict(F), defaultdict(F)
for law in laws:
    for w in product(range(2), repeat=3):
        p = F(1, 2)
        for j in w: p *= law[j]
        pword[w] += p
        phist[(w.count(0), w.count(1))] += p
H = lambda ps: -sum(float(p)*log(float(p)) for p in ps if p)
lhs = H(pword.values())
rhs = H(phist.values()) + sum(
    float(p)*log(factorial(3)/prod(factorial(z) for z in b))
    for b, p in phist.items())
assert abs(lhs-rhs) < 1e-12
print(lhs, H(phist.values()), rhs - H(phist.values()))
~~~

## Research/authority accounting

One new author-side scientific analysis unit: complete proof of full-batch injectivity, exact entropy gap and abstract asymptotic sharpness; finite rational-probability check. It corrects a possible over-reading of r398's generic entropy reduction without changing its valid theorem. No native Result admission, independent Driver review, Source/Activity write, CLAIM, task completion, or mother-objective closure is asserted by this GitHub note. Preserve the original Researcher and Driver contribution identities. Follow-up: assess actual Gaussian exact-checkpoint \(I(F_S(Y);B_i)\) (or a certified upper bound) rather than infer a major schedule improvement from histogram alphabet size alone.
