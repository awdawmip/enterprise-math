# OAI7 r336 — Near-minimal shared entropy can have certain small-list failure; arithmetic-progression obstruction

Date: 2026-11-18. This is an author-side exact counterexample and a robust structured-schedule obstruction in the **external finite cyclic group model**. The theorem targets the separate small-list **sufficient-condition certificate** of r307, not the actual terminal-marginal conclusion of that transfer theorem. No Native Result/Review/Source Activity admission or typed native Heartbeat-X6 trajectory is asserted. Original OAI7 researcher and all prior Driver/author provenance are retained.

## Theorem A: an exact all-fixed-K certificate failure despite equal full-lattice marginals and entropy within O(1/n) of its floor

Let \(p\) tend to infinity through primes, \(u=\lceil\sqrt p\rceil\), \(L=\log p\), \(b=17/64\), \(J_b=1-b+b\log b\), \(c_*=(4J_b)^{-1}\), and any fixed real \(d>4\log A_b\), where \(A_b=((1-b)\sqrt{2\pi b c_*})^{-1}\). Put

\[
n=\left\lceil c_*\sqrt p\,(L-2\log L+d)\right\rceil,\qquad N=n+1.
\]

For sufficiently large p, \(n+u<p\). Define the N ordinary integer labels \(U=\{0,1,\ldots,n\}\) and draw \(J\) uniformly from \(\{0,\ldots,n\}\). For \(\ell=0,\ldots,n-1\), let

\[
v_\ell=(J+\ell)\pmod N\quad\text{as an integer representative in }U,\qquad
h_\ell=(v_\ell,\ldots,v_\ell)\in\mathbb Z^k
\]

for any integer \(k\ge1\). Let \(H=(h_0,\ldots,h_{n-1})\).

Then:

1. Every realized shift schedule contains n distinct residues modulo p, and every position \(h_\ell\) is uniform over the same N integer diagonal vectors. Thus for every independent finitely supported integer-lattice \(Y\), the complete \(\mathbb Z^k\)-valued distributions of \(Y+h_\ell\) agree.
2. The random schedule entropy is exactly
   \[
   H(H)=\log(n+1)=\log n+\log(1+1/n).
   \tag{336.1}
   \]
   Hence the r334 near-floor rigidity estimate is saturated exactly, as proved in r335.
3. Set one **fixed deterministic** test set \(K=\{0,\ldots,u-1\}\subseteq\mathbb F_p\). For every realization, writing \(W=\{v_\ell\}_{\ell=0}^{n-1}\), the r307 bad-start count with integer threshold \(h=\lfloor bnu/p\rfloor\) obeys
   \[
   V_W(K)=\#\{x\in\mathbb F_p: |(x+W)\cap K|\le h\}
   \ \ge\ p-(n+u)\ >\ p^{3/4}.
   \tag{336.2}
   \]
   Therefore the exact worst-fixed-set failure probability \(q_+=1\) (not merely a large average). For each negative signed projection use the equally deterministic set \(-K\), giving \(q_-=1\). This applies to all \(2k\) signed diagonal coordinates.

**Proof.** The common position marginals, distinctness, and entropy are the n+1 cyclic construction of r335; they hold on the **integer lattice** before modular projection. For any realized \(W\subseteq U\), a starting residue x with at least one hit \((x+W)\cap K\neq\emptyset\) belongs to \(K-W\subseteq K-U=\{-n,\ldots,u-1\}\) modulo p. Since \(n+u<p\), this last set has exactly n+u residues. Every one of the remaining at least p-(n+u) starts has zero hits, thus belongs to the low-list set because \(h\ge0\). The asymptotic bound \(n+u=O(\sqrt p\log p)=o(p)\) yields \(p-(n+u)>p^{3/4}\) for sufficiently large p. The same K was fixed before J was sampled. Finally replacing W and K by their negatives preserves the count by the bijection x to -x. \(\square\)

This explicitly separates three conditions: identical **full integer** terminal laws, very low sampled shift entropy, and high-quality worst-fixed-K small-list tails. The first two hold here; the third fails with probability one at the r330–r333 sharp second-order sampling length. It is a counterexample to an attempted implication from the first two hypotheses to the small-list *certificate*, not a counterexample to r307's implication *when all its hypotheses hold*. In particular no failure of the **actual** terminal residue coverage is inferred.

For the r330 initial law with k independent coordinates uniform outside a fixed u-set, the entropy budget
\(H(H)+k[-\log(1-u/p)]\le(k/4096)\log p\) also holds for all sufficiently large p whenever \(k>2048\), since \(H(H)=\tfrac12\log p+\log\log p+O_d(1)\). Thus even a substantial slack in this information budget does not supply the missing small-list bound. The precise same signed-subset admissibility assumptions of r307 are retained.

## Theorem B: robust exclusion of arithmetic-progressive and near-progressive shift sets

Let p be prime, \(1\le u,n\) and \(n+u-1\le p\), and let \(W_0=\{a+id:0\le i<n\}\) be an n-term arithmetic progression of *distinct* residues in \(\mathbb F_p\), with \(d\neq0\). Let K be the fixed, same-step u-term progression \(\{b+jd:0\le j<u\}\). For any n-subset W with \(|W\triangle W_0|=2r\) and any nonnegative integer threshold h,

\[
\boxed{\quad V_W(K)\ge p-(n+u-1)-2ru.\quad}
\tag{336.3}
\]

**Proof.** The difference set \(K-W_0=\{b-a+td:-(n-1)\le t\le u-1\}\) has precisely \(n+u-1\) residues. Thus all other starts have zero hits against \(W_0\), proving \(V_{W_0}(K)\ge p-(n+u-1)\) for h≥0. The uniform Hamming-margin inequality r335.3 gives \(|V_W(K)-V_{W_0}(K)|\le2ru\). \(\square\)

Consequently, if \(p-(n+u-1)-2ru>p^{3/4}\), **every** law supported on n-subsets within swap distance r of this one fixed progression W0 has worst-fixed-K failure probability one. In the OAI7 regime \(n=O(\sqrt p\log p)\), \(u=\lceil\sqrt p\rceil\), any fixed r, and even any \(r=o(\sqrt p)\), meet this condition for sufficiently large p. The test K is the same for all W in the specified support.

The r335 n+1 cyclic construction is an especially explicit case: every \(W_j=U\setminus\{j\}\) is at most one swap away from the fixed progression \(\{0,\ldots,n-1\}\). Equation (336.2) is stronger for that precise family.

## Reproducibility and scientific handoff

All identities are finite elementary set calculations. A small direct check can be made at \(p=101,u=11,n=24,N=25\): for all 25 cyclic rows \(W_j=U\setminus\{j\}\) and fixed \(K=\{0,\ldots,10\}\), at least \(101-(24+11)=66\) starts have zero hits; \(101^{3/4}<32\). This is a finite illustration with the designated n=24, **not** verification of the large-p threshold formula at p=101 for arbitrary d. It is also independent of Chernoff or asymptotic source verification.

**Resolved local question:** Exact near-floor entropy and perfect integer-lattice position marginals, even with the optimal second-order schedule length, do not force r307's worst-fixed-set small-list tail hypothesis. A robust structured-schedule obstruction eliminates any random law supported in a sufficiently small Hamming neighborhood of one arithmetic progression.

**Open:** Existential all-K success of a single less-structured deterministic W; optimal entropy subject to the **combined** all-K condition; native valid ordered X6/Link/Port realization; independent Source-bound review of the prior author-side r329–r336 mathematics.

## Sources and contribution history

- OAI7 original Task RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19; original researcher EM-EMF6D046-5A2844.
- r307 integrated tail transfer, frozen source GitHub commit baaaabaacaf8543f62a45a00cdfcf03e95389075, path \`research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md\`.
- r329 distinct-law mean and concentration, source commit f1f35331daf48fbbbe01d8cf0cd43342dff85c01.
- r330 fixed-index codebook existence, source commit 67f57ab662493b6744df560c8358a293a08d1165.
- r334 near-floor bound, source commit 76bdaa0391769c8e4a9645cd4c129321624218ca.
- r335 sharpness witness and Hamming-margin bound, source commit 591f90fd482c56a3070e865f75801ddb7dc0dfde.
- New r336 contribution: a common-K certain certificate failure at optimal second-order n, explicit conservation of the integer-marginal/entropy conditions, and robust near-AP obstruction. No Native mathematical acceptance or claimed new owner.
