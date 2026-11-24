# Exact relative density of the one-W exact-nine branch on R3

Sources: [v15 one-W branch proof](https://github.com/awdawmip/enterprise-math/blob/745a30dae754df0e2d57d044e067680f33c70251/research_notes/portable_direct/riesel_nine_complete_20261124/one/proof.md) and [v13 complete budget-eight predicate](https://github.com/awdawmip/enterprise-math/blob/e78c84e2516caff59d206123bdc5e348e9733a6a/research_notes/portable_direct/riesel_eight_classification_20261124/observer/proof.md).

Let \(E\) be the roots in \(R_3\) of exact supplemental cost nine admitting a complete nine-prime supplement containing exactly one of \(W=\{19,73\}\). Let \(G,K,H,I,B,D,C\) be the coordinate groups in the two pinned proofs (\(G\) is denoted \(Z\) in the v15 proof). Their 36 distinct primes are coprime to \(S_3\). Thus the Chinese remainder theorem makes these groups independent and uniform in natural density relative to the progression \(R_3\).

For a fixed missing row \(c\in\{1,2,3,4,5\}\), the four primes in \(G\) occupy the other four rows in \(4!2^4=384\) ways, giving probability \(g=384/\prod G\). These \(G_c\) events are mutually exclusive. The three candidate phases for the remaining \(K\) primes are \(c,c+7,c+14\) modulo 21. They have distinct mod-three residues. A one-W completion uses two of these three phases: \(W=19\) covers mod-three class 0 and \(W=73\) covers class 1. Occupying classes 0 and 1 alone cannot be completed by either W. The actual event is that class 2 and at least one of class 0 or 1 are occupied. The three phase categories at each prime are disjoint sign pairs.

Write \(M=\prod K\). The K occupancy probability is
\[
k=\frac{M-\prod_{q\in K}(q-2)-\prod_{q\in K}(q-4)+\prod_{q\in K}(q-6)}{M}.
\]
The two exclusion events are absence of mandatory class 2 and simultaneous absence of classes 0 and 1. Their intersection is absence of all three.

Given \(G_c\), the complete budget-eight event is the union of \(J=E_B\lor E_D\lor E_C\) and \(H_c\lor I_c\), with \(I_c\) possible only for \(c=1,5\). The probabilities of its phase events are determined by
\[
p_d(X)=\frac{\sum_{j=0}^d(-1)^j\binom dj\prod_{q\in X}(q-2j)}{\prod X},
\]
the probability of occupying every one of \(d\) required categories across group \(X\). All groups except \(G\) are conditionally independent at any fixed \(G_c\). The exact density of \(E\) is
\[
gk[1-p_2(B)][1-p_2(D)][1-p_3(C)][1-p_2(H)][5-2p_2(I)]
=5.280148727142647171319245586036566355907672968265348793\ldots\,10^{-17}.
\]
The factor \(5-2p_2(I)\) adds the three ordinary missing rows to the two special rows, where \(I_c\) must also fail. The formula is exact.

The unfiltered density of the classified one-W geometry is \(5gk\approx5.28057346985272823\,10^{-17}\), with overlap \(4.24742710081063222\,10^{-21}\) with the budget-eight event. The unfiltered event is not a classification of lower-cost padded nonminimal nine-prime coverings. At exact cost nine, any nine-prime dictionary is irredundant, so the v15 one-W theorem applies in both directions. A root counted here may also permit a zero-W or a two-W cover. The statement does not count exclusive branches, the total nine-budget density, or the unrestricted total-cost-28 density.

Run python verify_one_w_density.py for exact rational arithmetic. Both the individual phase-family probabilities and the three-phase K probability are checked independently by a weighted mask recurrence. No native BRC execution or external writes are claimed.
