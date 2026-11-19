# OAI7 r396 — Charge only information revealed by the auxiliary sample, not all sample entropy

Date: 2026-11-20 (Asia/Shanghai). Task context: \`RS-OAI7-028-C-20261007-6F2A81\`, immutable publication \`TP2-96FAC49786245691AE19\`. Scientific status: **new author/Driver-side mathematical derivation and exact finite check**; neither a frozen Native Result nor an independent Native Review. Original task Researcher \`EM-EMF6D046-5A2844\` retains their own contribution history. This note follows r385–r395 without retrospectively changing their proof statements or native statuses.

## 1. Information-aware conditioning lemma: strictly weaker hypothesis

Use the exact signed-coordinate setting of [the pinned source, \`coverage-transfer.tex\` § One shared conditioning cost](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex): \(\Lambda\) a lattice, \(\phi_c:\Lambda\to G_c\) indexed by \(2k\) signed coordinates with \(|G_c|=p_c\), \(T\le p_c\le2T\), \(\bar L=k^{-1}\sum_{j=1}^k\log p_j\); \(S\) is the independent uniform selection of \(s\) distinct indices with one fair sign each. Let \(Y\) and a finite auxiliary variable \(\mathcal H\) have **any** joint law. All entropy/information uses natural logarithms. For fixed \(S\), \(F_S(Y)=(\phi_c(Y))_{c\in S}\).

**Theorem 1 (joint information charge).** If
\[
\mathbb E_S H(F_S(Y))\ge(1-\epsilon)s\bar L,\qquad
\mathbb E_S I(F_S(Y);\mathcal H)\le\kappa s\bar L
\]
for \(\epsilon,\kappa\ge0\), then
\[
\boxed{\frac1{2k}\sum_{c}\bigl[\log p_c-H(\phi_c(Y)\mid\mathcal H)\bigr]
\le(\epsilon+\kappa)\bar L.}\tag{1}
\]
The original conditioning lemma assumes the **stronger** inequality \(H(\mathcal H)\le\kappa s\bar L\), which implies the new condition by data processing and \(I(U;V)\le H(V)\).

**Proof.** For each fixed independent choice \(S\),
\[
H(F_S(Y)\mid\mathcal H)
=H(F_S(Y))-I(F_S(Y);\mathcal H)
\le\sum_{c\in S}H(\phi_c(Y)\mid\mathcal H).
\]
Take expectations over \(S\). Every signed coordinate has inclusion probability \(s/(2k)\), so the right side is \(s\) times the mean signed-coordinate conditional entropy. The first two assumptions lower bound the left side by \((1-\epsilon-\kappa)s\bar L\). The mean alphabet logarithm equals \(\bar L\). Subtraction proves (1). \(\square\)

Two **alternative sufficient checks** for the new information assumption are
\[
\boxed{I(Y;\mathcal H)\le\kappa s\bar L}\tag{2}
\]
or, writing \(\overline I_c=(2k)^{-1}\sum_c I(\phi_c(Y);\mathcal H)\),
\[
\boxed{\overline I_c\le\kappa\bar L.}\tag{3}
\]
Indeed, (2) implies the joint charge via \(F_S(Y)=f_S(Y)\) and data processing. The coordinatewise identity
\[
\frac1{2k}\sum_c[\log p_c-H(\phi_c(Y)\mid\mathcal H)]
=\frac1{2k}\sum_c[\log p_c-H(\phi_c(Y))]+\overline I_c
\]
proves (3) using subadditivity and the high-joint-entropy hypothesis. Depending on redundancy between coordinates, (2) or (3) may give different certificates; neither is asserted to dominate the other in every model.

## 2. Exact law-type factorization and the Gaussian checkpoint setting

Let \(A\) have finite support and \(Y=y(A)\). Suppose the **entire conditional joint law** \(\mathcal L(\mathcal H\mid A=a)\) depends on \(a\) only through a finite type \(V=V(A)\). In particular, this holds for conditionally iid trials \(\mathcal H=(h_1,\dots,h_n)\) drawn from \(\nu_A\), taking \(V\) to be the exact probability-law type \(\nu_A\). It also holds for a correlated sampler with law-type-determined support order and coupling kernel, including the specified r388/r392 canonical cyclic samplers.

Then \(Y\longrightarrow V\longrightarrow\mathcal H\) is a Markov chain, and
\[
\boxed{\mathbb E_S I(F_S(Y);\mathcal H)
\le I(Y;\mathcal H)\le I(V;\mathcal H)\le H(V).}\tag{4}
\]
Consequently **\(H(V)\le\kappa s\bar L\) suffices for Theorem 1**, no matter how large \(H(\mathcal H)\) is. An even sharper certificate is the actually observed \(I(V;\mathcal H)\).

**Proof.** The conditional law of \(\mathcal H\) given \(V=v\) is constant over \(A=a\) with type \(v\). Therefore \(\mathcal H\) is conditionally independent of \(A\), hence of \(Y=y(A)\), given \(V\). Apply data processing successively to \(F_S(Y)\), \(Y\), \(V\). \(\square\)

For the pinned [\`schedule.tex\` § Coverage from every exact checkpoint](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex), the conditional continuation is run after fixing the exact random checkpoint time \(A=A_{i+1}\), and the source uses \(\mathcal H\mid A=a\sim\nu_a^{\otimes n_i}\). Thus its **existing iid auxiliary sample itself** satisfies (4) for the type \(V_i(a)=\nu_a\). It is unnecessary to modify its sampling law to obtain the information-aware alternative. The source's valid original entropy certificate
\[
H(\mathcal H)\le n_i\log|\mathcal D_{i+1}|
\]
may be retained; for this specific conditioning step the sharper available charge is
\[
\mathbb E_S I(F_S(Y);\mathcal H)
\le\min\{H(\mathcal H),\,I(Y;\mathcal H),\,H(V_i)\}.
\]
The middle entry already bounds the left side and is not presumed easy to compute. If the fixed walk is self-avoiding, then \(a\mapsto z_a\) is injective, so \(Y=z_A\) determines \(A\), and this gives the exact identity
\[
\boxed{I(Y;\mathcal H)=I(A;\mathcal H)=I(V_i;\mathcal H).}\tag{5}
\]

This observation changes the **sufficient information-cost hypothesis**, not the source's proved result. A meaningful Gaussian schedule improvement requires an actual bound for \(H(V_i)\), \(I(V_i;\mathcal H)\), or the exact selected-coordinate information, and comparison against the source \(\eta_i\delta_i\beta_{i+1}s_iL_*/16\) budget. No low type entropy is inferred merely from finite support or self-avoidance.

## 3. Information-aware coverage transfer

The proof of r386 ([correlated conditional sampler with property (CS)](2026-11-19_oai7_028c_dependent_conditional_sampler_coverage_transfer_r386.md)) invokes the original conditioning lemma only at the final entropy-deficit contradiction. **Theorem 2.** In r386, replace just the hypothesis \(H(\mathcal H)\le\kappa s\bar L\) by
\[
\boxed{\mathbb E_S I(F_S(Y);\mathcal H)\le\kappa s\bar L.}\tag{6}
\]
Keep the high joint entropy premise, one-trial conditional marginals, conditional coverage, (CS), geometric bounds, and \(\epsilon+\kappa\le\eta\delta\beta'/16\) unchanged. Then the same terminal \((\tau,\beta)\)-coverage conclusion holds.

**Proof.** The true-residue list inclusion uses only equality of the one-trial unconditional marginals. The small-list probability uses only (CS), exceptional-set double counting, and the source's geometric inequalities. Neither step invokes \(H(\mathcal H)\). The averaging/short-list deficit lower bound is identical. Apply Theorem 1 in place of the original conditioning lemma to contradict that lower bound. \(\square\)

For the **original iid** source experiment, its original Chernoff inequality is still a sufficient certificate for (CS); therefore Theorem 2 also yields a **strictly weaker entropy assumption for the same original iid one-step transfer**. The necessary iid Shannon cost from r385 remains correct for the *original \(H(\mathcal H)\)-based budget*, but it is not a universal necessary cost for the information-aware transfer theorem.

## 4. Explicit separation and finite arithmetic check

Take \(k=s=1\), \(G_{1,+}=G_{1,-}=\mathbb Z/p\mathbb Z\), \(\phi_{1,\pm}(y)=\pm y\bmod p\), and \(Y=A\) uniform on \(\{0,\dots,p-1\}\subset\mathbb Z\). Conditional on every \(A=a\), take \(n\) iid displacements \(h_\ell\) uniform on those same \(p\) integers, **independent of \(A\)**. Then \(F_S(Y)\) is uniform for either sign and
\[
\mathbb E_S H(F_S(Y))=\log p,\quad
H(\mathcal H)=n\log p,\quad
I(Y;\mathcal H)=\mathbb E_S I(F_S(Y);\mathcal H)=0.
\]
Each conditional signed terminal law is uniform (no exceptional residues); the unconditional terminal law of \(Y+h_1\) is uniform. For any admissible fixed \(\tau,\delta,\beta',\beta,\eta\), choose \(p\) and \(n\) sufficiently large to meet the original geometric and Chernoff-size inequalities. Then the refined transfer applies with \(\epsilon=\kappa=\eta'=0\), while the **original small-\(\kappa\) entropy hypothesis fails** because \(n\log p>0\). This proves strict separation of the two theorem hypotheses, rather than merely a relabeling of \(H(\mathcal H)\).

The following tiny exact finite check verifies the information separation for \(p=3,n=2\). It is an algebraic sanity check, not a finite verification of the large-\(p\) geometric hypotheses.

~~~python
from fractions import Fraction as F
from collections import defaultdict
from math import log

p=3
joint={(y,h1,h2):F(1,p**3)
       for y in range(p) for h1 in range(p) for h2 in range(p)}
py=defaultdict(F); ph=defaultdict(F)
for (y,a,b),mass in joint.items():
    py[y]+=mass; ph[(a,b)]+=mass
assert all(joint[(y,a,b)]==py[y]*ph[(a,b)]
           for y in range(p) for a in range(p) for b in range(p))
Hh=-sum(float(v)*log(float(v)) for v in ph.values())
assert abs(Hh-2*log(3))<1e-12
print("I(Y;H)=0 exactly; H(H)=",Hh)
~~~

## 5. Finite-type information saturation (iid, not a new sampler)

Assume the finite set of conditional law types \(V\) consists of pairwise **distinct** probability laws \(\nu_v\) on a common finite alphabet, each with positive type probability, and \(\mathcal H_n\mid V=v\sim\nu_v^{\otimes n}\). Then
\[
\boxed{I(V;\mathcal H_n)\uparrow H(V),\qquad
I(Y;\mathcal H_n)\longrightarrow I(Y;V).}\tag{7}
\]
Indeed empirical symbol frequencies consistently identify the finitely many distinct \(\nu_v\), so the optimal type-decoding error tends to zero and the finite-alphabet Fano bound gives \(H(V\mid\mathcal H_n)\to0\). For the second assertion, \(Y-V-\mathcal H_n\), so
\[
0\le I(Y;V)-I(Y;\mathcal H_n)
=I(Y;V\mid\mathcal H_n)\le H(V\mid\mathcal H_n)\to0.
\]
Monotonicity in (7) holds for the first mutual information because prefixes are nested. This makes precise the saturation of the iid information cost in \(n\), even when \(H(\mathcal H_n)\) grows at least linearly whenever \(H(h_1\mid V)>0\).

## 6. Review and control scope

The derivations above are elementary Shannon chain-rule, data-processing, and finite-type consistency arguments checked against the pinned source. Claims of improvement are **conditional on the new information charge**, which is a stronger theorem with a weaker hypothesis; the actual Gaussian schedule's improved constants are not yet established. Independent review should examine the exact \(S\)-averaging, conditional type Markov condition, and whether any downstream use of \(\mathcal H\) beyond the list/conditioning proof changes the application. The pinned original transfer and schedule remain intact.

No native claim, Result acceptance, Source/Activity link, or mother-objective completion is asserted by this Source note. The next high-value calculation is a certified bound on the exact Gaussian checkpoint law-type mutual information (or directly \(\mathbb E_S I(F_S(Y);\mathcal H)\)), preserving the source's exact-time quantifiers, conditional coverage and terminal geometry.