# OAI7 r349 — Translation-quotient minimax compression and the marginal-entropy boundary

Date: 2026-11-19. Status: exact mathematical lemma and explicit finite prime-29 construction, author-side Driver research. Uses the verified r347 primal/dual certificate and r348 rigidity theorem. This proof shares prior Driver scientific context and is not an independent Native Result review.

## General translation-quotient theorem

Let \(G\) be a finite abelian group of cardinality \(p\). Fix \(1\le n\le p\), \(1\le u\le p\), and any threshold \(T\). For a random \(n\)-subset \(C\) and deterministic \(u\)-subset \(K\), define

\[
V_C(K)=p-|K-C|,\qquad
q_T(\mu)=\max_{|K|=u}\Pr_{C\sim\mu}\{V_C(K)>T\}.
\]

Let \(\pi(C)\) be any deterministic representative of the translation orbit
\(\{C+t:t\in G\}\), and denote its induced law by \(\bar\mu=\pi_\#\mu\).
Then, **for every distribution** \(\mu\) on \(n\)-sets,

\[
\boxed{q_T(\bar\mu)=q_T(\mu).}
\]

In fact the failure probability is unchanged **for each particular test \(K\)**, not merely after taking the maximum. Consequently, unrestricted minimax over distributions on all \(n\)-sets is exactly equivalent to minimax over translation-orbit representatives.

**Proof.** For any \(t\in G\),
\[
K-(C+t)=(K-C)-t,\qquad |K-(C+t)|=|K-C|.
\]
Thus the bad-event indicator is constant on every translation orbit of \(C\). Pushing a probability measure forward along \(\pi\) preserves the expectation of every such indicator. QED.

If \(G=\mathbb Z/p\mathbb Z\) with \(p\) prime and \(1\le n<p\), every translation orbit of an \(n\)-set has exactly \(p\) members. If a law \(\mu\) is translation-invariant, its conditional law given the translation class is uniform over all \(p\) shifts. Therefore, with Shannon logarithms in base 2,

\[
\boxed{H(\pi(C))=H(C)-\log_2p.}
\]

The compression requires no approximation or new random seed. It is a theorem about the set-valued coverage failure event; a separate equal-position-marginal requirement on an ordered shift sequence is not retained automatically.

## Exact prime-29 consequence for the r347 optimum

Fix \(G=\mathbb F_{29}\), \(n=5\), \(u=4\), \(T=29^{3/4}\). Let \(v\) be the r347 exact unrestricted optimum

\[
v=\frac{2024467747}{3324255613}.
\]

The r347 exact certificate provides 14 positive affine-orbit weights \(w_j=a_j/D\), with \(D=474893659\). Use the exact orbit enumeration from r347; each such affine orbit splits into \(t_j\) translation classes, with \(t_j=28\) for 13 of the selected affine orbits and \(t_6=14\) for the one exceptional affine orbit (index 6, following the pinned r347 enumeration).

Define a probability law \(\nu\) supported on precisely one deterministic representative from each selected translation class. Give every representative in affine orbit \(j\) the weight

\[
\boxed{\Pr_\nu\{C=c\}=\frac{a_j}{D\,t_j}.}
\]

This produces **378 distinct five-sets**, rather than r347's 10,962 translated five-sets, with no change in the exact worst-test failure value:

\[
\boxed{q_T(\nu)=v.}
\]

Its set entropy is

\[
\boxed{
H_\nu(C)
= -\sum_{j\in S}w_j\log_2\!\left(\frac{w_j}{t_j}\right)
=7.941714405851122\ \text{bits}.
}
\]

This is exactly \(\log_2(29)=4.857980995127572\) bits below the **particular** translation-invariant r347 optimizer with entropy \(12.799695400978694\) bits. Consequently, the unrestricted minimax problem has at least two distinct optimal measures and the 12.7996954-bit figure is the cost of the specific fully translation-invariant r347 realization, **not** a universal entropy minimum for arbitrary minimax laws.

Theorem A of r348 remains in force: every optimal law, including \(\nu\), has the same 14 total affine-orbit masses. Its uniqueness concerns these orbit masses and the affine-invariant optimal law, while the within-orbit realization has nontrivial freedom.

## Proof of exact attainment and finite reproducibility

For every deterministic test \(K\) and each selected affine orbit \(j\), the complete r347 orbit measure distributes \(w_j\) uniformly over its \(29t_j\) translated five-sets. Each of its \(t_j\) translation classes has total mass \(w_j/t_j\), identical to \(\nu\). The general translation-quotient theorem therefore gives identical bad-event probabilities for **all** \(\binom{29}{4}=23751\) tests, not merely for 33 orbit representatives. The r347 exact rational primal and dual certificate establishes that their maximum equals \(v\).

A reproducible extension to the r347 Python standard-library checker is:

    import math
    support = sorted(pc)
    trans_class_count = sum(len(C[j]) for j in support)
    full_set_count = sum(29*len(C[j]) for j in support)
    assert trans_class_count == 378
    assert full_set_count == 10962
    assert [j for j in support if len(C[j]) == 14] == [6]
    assert all(len(C[j]) == 28 for j in support if j != 6)
    compressed_entropy = -sum((a/D)*math.log2((a/D)/len(C[j]))
                              for j,a in pc.items())
    full_entropy = compressed_entropy + math.log2(29)
    assert abs(compressed_entropy - 7.941714405851122) < 1e-12
    assert abs(full_entropy - 12.799695400978694) < 1e-12
    assert all(sum(A[i][j]*a for j,a in pc.items()) <= D*v
               for i in range(33))
    print("r349: 378-class exact-optimal law and entropy verified")

The complete 33-by-150 matrix, all exact primal and dual inequalities, active equality rows and source ordering were rerun from r347 using rational arithmetic in this continuation. The entropy decimals are descriptive approximations; the probability weights and \(q_T=v\) are exact rational facts.

## Actual scope of the entropy tradeoff

For a deterministic ordered tuple selected by sorting each canonical representative, the ordered output remains injective in the set and has the same \(7.941714405851122\)-bit entropy. Such canonical representatives are highly nonuniform in position: the least binary representative of each translation class contains element 0, so the first sorted coordinate is always 0. Thus this construction does **not** meet the exactly uniform/equal-position marginal condition used by r347's 12.7996954-bit ordered realization. Optimizing exact coverage plus that additional marginal condition is a different constrained problem; no smaller entropy for it is claimed here.

## Provenance

Pinned r347: Enterprise Math commit 12bd331ea2aef70cc844682db432a623b235e726, file research_notes/portable_direct/2026-11-19_oai7_driver_exact_affine_minimax_prime29_r347.md, Git blob a7fe2e565ba13f10b2049073485595a2392fb288. r348 rigidity: commit f41c2690daba467ecbde99615a1337e67be46ffd, file research_notes/portable_direct/2026-11-19_oai7_driver_affine_minimax_rigidity_r348.md. Retains original OAI7 researcher EM-EMF6D046-5A2844, r307–r347 contributions, and native task RS-OAI7-028-C-20261007-6F2A81/publication TP2-96FAC49786245691AE19. No Native review, source Activity publication, Task completion, X6 transfer or parent closure is asserted.
