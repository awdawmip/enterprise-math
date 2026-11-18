# OAI7 r352 — Exact minimum entropy under translation invariance and a uniformly marginal ordered realization

Date: 2026-11-19. Author-side exact finite mathematical extension of r347–r351. Original OAI7 researcher EM-EMF6D046-5A2844 and all r307–r351 scientific contributors retain their provenance. Native Result/independent review/Activity/Task authority has not been claimed.

## Two precise results at the prime-29 optimum

Let \(G=\mathbb F_{29}\), random five-element subset \(C\), four-element fixed test \(K\), and \(b_K(C)=\mathbf1\{|K-C|\le16\}\). The exact unrestricted minimax probability from r347 is
\[
v=\frac{2024467747}{3324255613}.
\]
By r351, every minimax law has the same 350 loss-profile probabilities \(p_x\) and their Shannon entropy equals
\[
H_{350}= -\sum_{j\in S\setminus\{1,2\}} w_j\log_2(w_j/t_j)
-\sum_{j=1,2}w_j\log_2(w_j/14)
\approx7.869745624309653.
\]

**Theorem A (exact constrained minimum).** Among **all translation-invariant laws** \(\mu\) on the 118,755 five-sets with \(q(\mu)=v\),
\[
\boxed{\min_{\substack{q(\mu)=v\\\mu\ \mathrm{translation\ invariant}}}H_\mu(C)
=H_{350}+\log_2 29
\approx12.727726619437224\text{ bits}.}
\]
This improves the r347 affine-invariant optimizer's set entropy \(12.799695400978694\) bits by **exactly**
\[
\boxed{\frac{34177518}{474893659}\text{ bits}.}
\]
The attaining translation-invariant law has exactly **10,150 distinct five-sets**, versus 10,962 in the r347 affine-invariant construction.

**Theorem B (jointly ordered realization with zero auxiliary ordering entropy).** The same law admits a deterministic translation-equivariant ordering \(H=(H_1,\ldots,H_5)\) for which:
\[
\forall \ell\in\{1,\ldots,5\},\ \forall a\in G:
\Pr(H_\ell=a)=\frac1{29},
\qquad H(H_1,\ldots,H_5)=H_{350}+\log_2 29.
\]
Every row has five distinct entries and preserves exactly the same fixed-test bad-event probabilities as r347/r350, so \(q=v\). The ordering uses **no independent permutation/ordering seed**.

## Construction and proof

Let \(\nu_{350}\) be the r350 optimal law on 350 pairwise translation-inequivalent five-sets, one representative for each distinct loss profile, with masses \(p_x\). Independently sample \(T\) uniformly in \(\mathbb F_{29}\) and output \(C=W_x+T\) when \(W_x\) is sampled from \(\nu_{350}\). Distinct \(x\) select distinct translation classes by construction, and each class has 29 elements because the group has prime order and \(1\le|W_x|=5<29\). Therefore the map \((x,T)\mapsto W_x+T\) is injective, and
\[
H(C)=H(x,T)=H_{350}+\log_2 29,\quad |\mathrm{supp}(C)|=350\cdot29=10150.
\]
Translation leaves \(|K-C|\) unchanged for every fixed \(K\); hence all 23,751 fixed-test probabilities and their exact minimax maximum are preserved.

Fix any deterministic ordering \((w_{x,1},\ldots,w_{x,5})\) of each \(W_x\), and define \(H_\ell=w_{x,\ell}+T\). Conditioned on \(x\), each \(H_\ell\) is uniform on \(G\), so its unconditional marginal is uniform too. From the ordered output one recovers the unordered set and, by translation-class uniqueness, both \(x\) and \(T\). Thus the ordered map is injective and has exactly the stated entropy without additional seed.

For the lower bound of Theorem A, take any globally minimax translation-invariant law \(\mu\). Theorem r351 fixes its full distribution of loss profiles to \(p_x\). Conditional on any loss profile \(x\), the codeword law is a mixture of one or two full 29-element translation orbits, and **within each orbit** translation invariance forces the 29 shifts to be equiprobable. Consequently
\[
H_\mu(C\mid \sigma(C)=x)
=\log_2 29+H_\mu(\mathrm{translation\ class}\mid \sigma=x)
\ge\log_2 29.
\]
By the entropy chain rule, \(H_\mu(C)\ge H_{350}+\log_2 29\), attained by the displayed construction. This proves both the exact translation-invariant minimum and its uniform-marginal ordered realization.

## Reproduction and conceptual boundary

Run r350's exact 378-to-350 fiber certificate, then r351's complete rational dual and 392-by-350 active-rank verifier. The following independent arithmetic checks the support and entropy savings:
~~~python
from math import log2
from fractions import Fraction
gain=Fraction(34177518,474893659)
h350=7.869745624309653
htrans=h350+log2(29)
assert 350*29==10150
assert abs(htrans-12.727726619437224)<1e-12
assert abs((htrans+float(gain))-12.799695400978694)<1e-12
print("r352 PASS:",htrans,"bits; exact entropy improvement:",gain)
~~~
Observed: all assertions passed (together with the exact r350 and r351 finite certificates).

This is a sharp entropy theorem for the **translation-invariant** prime-29 minimax family, plus a feasible upper bound for the more general ordered, exactly uniform-position-marginal minimax family. Whether a **non-translation-invariant** ordering can attain even smaller entropy while preserving each uniform position marginal remains open. The quotient/translation claims refer to the declared external finite-group coverage observer; future signed, provenance-bearing and native X6/Link/Port operations need their own representation-safe evidence.

Pinned source notes: [r347](https://github.com/awdawmip/enterprise-math/blob/12bd331ea2aef70cc844682db432a623b235e726/research_notes/portable_direct/2026-11-19_oai7_driver_exact_affine_minimax_prime29_r347.md), [r350](https://github.com/awdawmip/enterprise-math/blob/2737a8ea300816066714ef0ff8d72b62c6df2e46/research_notes/portable_direct/2026-11-19_oai7_driver_loss_profile_twin_compression_r350.md), [r351](https://github.com/awdawmip/enterprise-math/blob/10ac54cc216860ddfd0ce62fe82b229318482573/research_notes/portable_direct/2026-11-19_oai7_driver_global_entropy_minimizer_r351.md); also original r348/r349 and named OAI7 contributions. Native task RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19 remains unchanged.