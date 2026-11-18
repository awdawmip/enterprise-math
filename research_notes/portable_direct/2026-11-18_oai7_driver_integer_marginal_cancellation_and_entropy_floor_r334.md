# OAI7 r334 — integer-lattice convolution cancellation and rigidity at the equal-marginal entropy floor

Date: 2026-11-18. Scope: external finite cyclic shared-shift model with **full integer-lattice** terminal-marginal equality and finite support. Evidence: author-side derivation and technical audit; not a clean independent Native Driver review. Original OAI7 researcher EM-EMF6D046-5A2844 retains original contribution. r331 proved the entropy floor assuming equality of the displacement marginals; this note proves the implication from full terminal marginals, classifies equality, and quantifies near equality.

## Theorem A. Cancellation of the integer initial distribution

Let \(Y\) be any finitely supported random variable on \(\mathbb Z^k\), and let \(H=(H_0,\ldots,H_{n-1})\) be a finitely supported random vector in \((\mathbb Z^k)^n\), **independent of** \(Y\). If

\[
\mathcal L(Y+H_i)=\mathcal L(Y+H_j)\qquad\text{as full laws on }\mathbb Z^k,
\]

then \(\mathcal L(H_i)=\mathcal L(H_j)\).

**Proof.** Associate each finite measure \(\mu\) on \(\mathbb Z^k\) with its Laurent polynomial \(P_\mu(z)=\sum_{a\in\mathbb Z^k}\mu(a)z_1^{a_1}\cdots z_k^{a_k}\). Independence gives \(P_{Y+H_i}=P_Y P_{H_i}\). Hence \(P_Y(P_{H_i}-P_{H_j})=0\). Since \(\mathbb R[z_1^{\pm1},\ldots,z_k^{\pm1}]\) is an integral domain and \(P_Y(1)=1\), cancellation yields \(P_{H_i}=P_{H_j}\). Equality of all coefficients proves the claim. \(\square\)

This proof concerns full \(\mathbb Z^k\) convolution, and does not assert injectivity of convolution on every finite quotient group.

## Theorem B. Equality classification for the entropy floor

Let \(H=(H_0,\ldots,H_{n-1})\) be any finite-valued random sequence with identical position marginals \(\nu\), such that every realization has \(n\) distinct entries. Then

\[
H(H)\ge H_\infty(H)\ge\log n.
\tag{334.1}
\]

Equality \(H(H)=\log n\) holds **if and only if** one fixed \(n\)-element set \(W\) supports exactly \(n\) ordered schedules, each with mass \(1/n\), arranged so that every element of \(W\) appears once in each position across the \(n\) schedules. Equivalently, the support rows form a Latin arrangement of \(W\). Uniform cyclic rotations of an ordering of \(W\) realize equality.

**Proof.** For any positive-mass atom \(h=(a_0,\ldots,a_{n-1})\) with probability \(t\), the \(a_i\) are distinct and \(\nu(a_i)\ge t\). Thus \(1\ge\sum_i\nu(a_i)\ge nt\); the maximum atom probability is at most \(1/n\). Shannon entropy dominates min-entropy, giving (334.1).

If Shannon entropy equals \(\log n\), equality in the two inequalities forces the joint law to have exactly \(n\) atoms, each with probability \(1/n\). For any atom, its \(n\) entries each carry common marginal probability at least \(1/n\), exhausting the entire marginal mass. Consequently \(\nu\) is uniform on that atom's entry set \(W\) and has no support elsewhere. Every other atom therefore uses precisely \(W\). Equal marginal probabilities in each position force each of the \(n\) elements to occur exactly once per position across the \(n\) equiprobable atoms. Conversely this arrangement evidently has the required marginal laws and exactly \(n\) equiprobable states. \(\square\)

## Theorem C. Quantitative near-floor rigidity

Under the hypotheses of Theorem B, if \(H(H)\le\log n+\delta\), \(\delta\ge0\), then some deterministic set \(W\) of \(n\) entries obeys

\[
\nu(W)\ge e^{-\delta},\qquad
\Pr\{\{H_0,\ldots,H_{n-1}\}=W\}
\ge \max\{0,1-n(1-e^{-\delta})\}.
\tag{334.2}
\]

**Proof.** If \(t\) is the probability of a maximal atom, then \(t\ge e^{-H(H)}\ge e^{-\delta}/n\). Let \(W\) be its distinct entries. Each has marginal mass at least \(t\), hence \(\nu(W)\ge nt\ge e^{-\delta}\). The expected number of entries of a sampled schedule lying outside \(W\) is \(n(1-\nu(W))\le n(1-e^{-\delta})\). Any realized distinct \(n\)-tuple with a different underlying set has an outside entry, so the indicator of that event is bounded by its outside count. Taking expectations gives (334.2). \(\square\)

Thus when \(\delta=o(1/n)\), the unordered schedule is a single deterministic set with probability tending to one. If that set fails a fixed-\(K\) coverage test, the schedule failure probability for that \(K\) is at least \(1-n(1-e^{-\delta})\). This implication is conditional on an actual obstructing \(K\), without assuming an unproved universal obstruction for all deterministic sets.

## Consequence for OAI7

The r330–r333 diagonal-integer codebook samples finitely many shift sequences, takes a finitely supported independent integer initial \(Y\), enforces full equality of the laws \(Y+H_i\), and has \(n\) distinct mod-\(p\) residues per schedule. Theorem A makes equal **shift** marginals a consequence of that full-lattice output requirement. Theorem B yields the r331 necessary floor directly:

\[
H(H)\ge\log n=\tfrac12\log p+\log\log p+O_d(1).
\]

At exact equality the underlying shifts form one fixed set \(W\); only their order varies. Every unordered-set failure event \(V_W(K)>p^{3/4}\) therefore has probability \(0\) or \(1\). Strictly improving the necessary asymptotic entropy coefficient would require an additional genuine all-\(K\) obstruction or a different information argument. The nonuniform construction's total deterministic advice/storage cost remains separate from the sampled Shannon entropy.

## Source lineage and status

- OAI7 immutable task: RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19; original researcher EM-EMF6D046-5A2844.
- r331 entropy floor: [@85b7b309](https://github.com/awdawmip/enterprise-math/blob/85b7b309a3383e9ce065fd39c68c32e80afee517/research_notes/portable_direct/2026-11-18_oai7_driver_fixed_index_entropy_failure_tradeoff_r331.md).
- Distinct-shift bounds and joint codebook: r329 @f1f35331, r330 @67f57ab6, r332 @52125fe8, r333 @51f54d5a.
- New here: convolution cancellation, entropy-floor equality classification, near-equality stability and its conditional event-level consequence.

GitHub scientific note only; no new CLAIM, Native Result, Source/Activity admission, independent formal review or Task/parent-objective completion is asserted.
