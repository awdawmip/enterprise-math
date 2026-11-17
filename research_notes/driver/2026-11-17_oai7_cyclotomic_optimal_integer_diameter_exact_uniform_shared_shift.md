# OAI7 — Optimal finite integer diameter for exact simultaneous prime-residue uniformity; a low-entropy shared displacement

Date: 2026-11-17. Mathematical derivation: EM-DVR-DEBB5E (author-side Driver work, shared directed context; not an independent Native review). Prior OAI7 shared-shift line: EM-EMF6D046-5A2844. Related fixed source: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a, preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex, Theorem "One-step coverage transfer". Prior Driver bounded-interval theorem: enterprise-math@ebab071be3e2e4ed75605f66a64a1d4dc828523f.

## Theorem A — sharp minimum diameter

Let p_1,...,p_k be pairwise distinct primes. Let h be any integer-valued random variable with nonempty finite support, and assume each h modulo p_j is exactly uniform on Z/p_j Z. Then

\[
\operatorname{diam}(\operatorname{supp} h)
:=\max(\operatorname{supp}h)-\min(\operatorname{supp}h)
\ \geq\ D:=\sum_{j=1}^k(p_j-1).
\]

This bound is achieved by a *single shared scalar integer displacement*
\[
h=U_1+\cdots+U_k,\qquad
U_j\stackrel{\mathrm{ind}}{\sim}\operatorname{Uniform}\{0,\ldots,p_j-1\}.
\]
In this construction every residue h modulo p_j is **exactly uniform**, h takes precisely the integers 0,...,D with positive probability, and
\[
\boxed{\operatorname{diam}(\operatorname{supp}h)=D,\qquad
\max_j\log p_j\leq H(h)\leq\log(D+1).}
\]
The internal independent U_j are a way to sample one common h; the random variable exposed to the coverage-transfer experiment is h alone.

**Proof of necessity.** Shift h by its minimum a, and set
\[
F(X)=\sum_{t=0}^{D_h}\Pr(h=a+t)X^t\in\mathbb R[X],
\qquad D_h=\operatorname{diam}(\operatorname{supp}h).
\]
It is a nonzero polynomial, with positive leading and constant coefficients. For each j, exact uniformity modulo p_j implies
\[
F(\zeta)=\mathbb E\zeta^{h-a}=0
\]
for *every* nontrivial p_j-th root of unity \(\zeta\). Thus the cyclotomic polynomial \(\Phi_{p_j}(X)=1+X+\cdots+X^{p_j-1}\) divides F in \(\mathbb R[X]\). Distinct prime cyclotomic polynomials have disjoint complex root sets, so their product divides F. Degree comparison gives
\[
D_h=\deg F\geq\deg\prod_j\Phi_{p_j}=\sum_j(p_j-1).
\]
This argument works for arbitrary real-valued probability weights; no rationality assumption on the weights is needed.

**Proof of attainment.** For h=sum U_j, the probability-generating polynomial is
\[
F(X)=\prod_{j=1}^k\frac{1+X+\cdots+X^{p_j-1}}{p_j}.
\]
Its degree is exactly D, with positive endpoint coefficients, and convolution of consecutive positive supports fills every integer from 0 to D. Modulo p_j, the summand U_j is uniform and independent of the remaining sum; adding any independent residue preserves uniformity. Hence every signed map \(\phi_{j,\sigma}(x)=\sigma x\bmod p_j\) is exactly uniform when applied to y+h for any fixed integer y. The entropy bounds follow from the deterministic support size D+1 and from \(H(h)\ge H(h\bmod p_j)=\log p_j\). QED.

Theorem A concerns a minimum **integer support diameter**, not the full variance, entropy-minimizing law, or realizability of a physical walk. It contrasts with the previously proved exponential CRT-diameter bound for the *specified quantile* coupling \(r_j(w)=\lfloor p_j w\rfloor\), which remains valid for that coupling.

## Theorem B — complete abstract coverage transfer with exact conditional marginals and sparse joint law

For all sufficiently large T, let
\[
k=\lfloor \sqrt T(\log T)^2\rfloor,
\]
choose k different primes \(p_j\in[T,2T]\), and define
\[
P=\prod_jp_j,\quad D=\sum_j(p_j-1)\leq2kT,\quad
m_j=\lceil\sqrt{p_j}\rceil,\quad
L_j=p_j-m_j,\quad V_j=\{m_j,\ldots,p_j-1\}\subseteq\mathbb Z/p_j\mathbb Z.
\]
Prime existence follows from \(\pi(2T)-\pi(T)\sim T/\log T\). Draw independent \(C_j\sim\operatorname{Uniform}(V_j)\), let A=C be the *exact* checkpoint, and use the unique CRT representative \(Y=y(C)\in\{0,\ldots,P-1\}\subset\Lambda=\mathbb Z\). Independently of A, draw h_1,...,h_n conditionally iid from the *same* Theorem A sum-of-uniforms scalar law, with independent fresh summands per trial. Use
\[
n=\lceil8192\sqrt{2T}\log(12800T)\rceil,\quad
\beta=\beta'=1/2,\quad\tau=3/8,\quad\delta=1/64,\quad
\tau'=7/16,\quad\eta=1/2,\quad\eta'=0,\quad s=k.
\]
Set \(\mathcal H=(h_1,\ldots,h_n)\), \(Z=Y+h_1\) and \(R=(Z\bmod p_j)_j\).

The exact fixed-checkpoint conditional distribution \(\phi_{j,\sigma}(y(a)+h_1)\mid A=a\) is uniform for **all** signed coordinates, hence has (\(\tau',\beta'\))-coverage with zero exceptional residues. The shared entropy is
\[
H(\mathcal H)=nH(h)\le n\log(D+1)\le n\log(1+2kT).
\]
For every s=k signed subset, \(H(F_S(Y))=\sum_j\log L_j=(1-\epsilon)k\overline L\), with \(\overline L=k^{-1}\sum_j\log p_j\), \(\epsilon=O((\sqrt T\log T)^{-1})\). Define
\[
\kappa=\frac{nH(h)}{k\overline L}
\le\frac{n\log(1+2kT)}{k\overline L}
=O(1/\log T).
\]
Thus \(\epsilon+\kappa\to0\) and eventually \(\epsilon+\kappa\le\eta\delta\beta'/16=1/4096\). The remaining original theorem hypotheses hold because
\[
p_j\exp[-\delta^2np_j^{-\beta}/2]
\le2T\exp[-n/(8192\sqrt{2T})]\le1/6400=\delta/100,
\]
while \(64<p_j^{1/4}\) and \(\log(128e)\le(\log T)/8\) for sufficiently large T. This checks the *original theorem's* conditioning, signed-subset, iid, information-budget, sample-size and logarithmic quantifiers, without selecting separate times or displacements for different coordinates.

Despite **exact uniformity of every terminal signed marginal** (as well as every conditional signed next-step marginal), the terminal joint distribution can be far from uniform:
\[
\frac{|\operatorname{supp}R|}{P}
\le(D+1)\prod_j\frac{L_j}{p_j}
\le(1+2kT)\exp[-k/\sqrt{2T}]\ \longrightarrow\ 0.
\]
Indeed, conditional on h_1=t, R is uniform on the size-\(\prod L_j\) product translate of \(\prod V_j\), and h_1 has at most D+1 possible values. Therefore
\[
\boxed{\operatorname{TV}(\mathcal L(R),U_{\rm product})\to1,\qquad
\frac{H(R)}{\log P}\to1.}
\]
The entropy assertion follows directly from \(\sum_j\log L_j=H(R\mid h_1)\le H(R)\le\log P\). Since h_1 modulo each p_j is uniform, \(R_j\) is exactly uniform, and the same holds for its sign reversal.

This sharpens the prior bounded-interval construction: full exact marginal uniformity, a *provably minimum* finite integer support diameter among all laws with exact simultaneous prime-residue uniformity, and information cost \(H(\mathcal H)=O(n\log(kT))\), while the terminal joint law remains asymptotically sparse.

## Small exact checks and reproducibility formula

For any prime tuple, put \(a_t=[X^t]\prod_j(1+\cdots+X^{p_j-1})\). Then
\[
\Pr(R=r)=\frac{1}{P\prod_jL_j}
\sum_{t=0}^{D}a_t\prod_j
\mathbf1_{\{r_j-t\bmod p_j\in V_j\}}.
\]
This is an entirely integer/rational enumeration formula: compare its values with \(1/P\) and sum absolute differences to obtain exact total variation. Independently check each one-coordinate numerator is \(P\prod L_j/p_j\).

Using integer convolution and exact fractions gives:

| Prime tuple | D | number of values of h | support of R / product size | exact terminal joint TV | every signed marginal uniform |
|---|---:|---:|---:|---:|---|
| (5,7) | 10 | 11 | 35/35 | 27/140 | Yes |
| (5,7,11) | 20 | 21 | 385/385 | 921/5390 | Yes |
| (7,11,13) | 28 | 29 | 1001/1001 | 7976/63063 | Yes |

These are finite arithmetic checks of the construction, not large-T instances of the final support-sparsity limit. The universal statements above have independent algebraic/asymptotic proofs.

## Provenance, scope and follow-up

- Earlier OAI7 shared-shift/finite-threshold work: EM-EMF6D046-5A2844. This theorem's cyclotomic optimality proof and additive shared displacement construction: EM-DVR-DEBB5E. No independent-review status is claimed for a proof by its own author.
- Exact external input: openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex. Its conclusion concerns marginal coverage, and is satisfied by the present example.
- This is an abstract rank-one lattice/finite-abelian-group family. Whether the scalar shifts and CRT checkpoint correspond to a bounded-step self-avoiding Gaussian-prime path or a typed native BRC/X6 carrier is an independent mathematical question. No X6/native promotion is inferred.
- The result is author-side scientific source material. Native Result freeze, independent Driver review/acceptance, formal Activity association, Task closure and parent-objective closure retain their separate current authorization and evidence requirements.
