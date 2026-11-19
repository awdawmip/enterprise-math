# OAI7 r363 — Fixed-step-cycle no-go for sharp all-marginal support

Date: 2026-11-19. Author-side mathematical continuation of r360 and r362. It generalizes the previous northwest-order obstruction to **arbitrary exact support/weights** with a fixed-step cycle connector skeleton. Original OAI7 researcher and task provenance remain intact; this is not a Native Result review.

## Theorem

Let \(p\ge3\) be prime, \(m\ge p-1\), \(n_x\in\mathbb Z_{>0}\), \(N=\sum_x n_x\), and \(\gcd(N,p)=1\). Fix pairwise translation-inequivalent ordered shapes \(W_x=(w_{x,1},\ldots,w_{x,d})\in(\mathbb Z/p\mathbb Z)^d\), \(d\ge2\). A positive atom \((x,t)\) of weight \(z_{x,t}\) outputs coordinate \(i\) equal to \(w_{x,i}+t\) and has per-profile total \(\sum_tz_{x,t}=n_x/N\).

Suppose the law has the **sharp support size** \(S=m+p-1\) and its first-coordinate marginal is exactly uniform. Suppose further that:

* Precisely \(p-1\) profiles have degree two (two supported translations each), and the other \(m-(p-1)\) profiles have degree one.
* For a fixed nonzero \(g\in\mathbb F_p\), the two first-coordinate residues of each degree-two profile \(x\) are \(a_x\) and \(a_x+g\) (orientation may be chosen for each profile).

If another coordinate \(i\) is exactly uniform, then its relative shape offsets are **identical on every degree-two profile**:
\[
\boxed{w_{x,i}-w_{x,1}=\beta_i\pmod p
\qquad\text{for every degree-two }x.}\tag{1}
\]
For given weights, once this condition holds, coordinate \(i\) is uniform if and only if the singleton-profile numerator sums at each residue agree with the translate by \(\beta_i\) of their first-coordinate singleton sums.

**Corollary (all-coordinate no-go).** If \(p\ge3\) and all \(m\) ordered shapes are pairwise inequivalent under common translation, the above fixed-step-cycle support cannot be exactly uniform in all \(d\) coordinates. Indeed, (1) for all coordinates would make all \(p-1\ge2\) connector shapes translates, contradicting pairwise inequivalence.

**OAI7 consequence.** The exact \(p=29,m=350,d=5\), \(N=13,297,022,452\) 350-fiber minimax profile law of r351/r357 has \(\gcd(N,29)=1\) and pairwise translation-inequivalent base shapes. Consequently, **any** possible 378-atom five-uniform law must have at least one of:

1. A profile using **three or more** supported translations; or
2. If all positive-profile degrees are at most two, the 28 connector first-position residue pairs have **at least two distinct unoriented cyclic differences** (not all \(\{a,a+g\}\) for one common \(g\)).

This is a genuine new search-space exclusion: it applies to arbitrary selected connector profiles, non-northwest first-position assignments, arbitrary exact positive weights, and any permutation of the 350 fibers. It leaves the general 378-versus-490 support-minimum question open.

## Proof

For any uniform coordinate \(i\), form the bipartite profile/residue incidence graph with one labeled positive atom edge for each \((x,t)\). Coprimality gives connectivity: if a component contains \(c\) residues and source-profile numerator sum \(s\), its total mass is both \(s/N\) and \(c/p\), so \(p\mid c\). Hence all positive-mass profiles and all \(p\) residues lie in one component. Since it has \(m+p\) vertices and \(S=m+p-1\) edges, it is a tree.

Deleting singleton-profile leaves and suppressing the degree-two connector vertices produces a tree on all \(p\) residues with \(p-1\) edges. By hypothesis, each first-coordinate connector pair is a step-\(g\) edge \(\{a_x,a_x+g\}\). Because \(g\ne0\) is a generator of the additive group \(\mathbb F_p\), these are edges of a single \(p\)-cycle. A spanning tree using only such edges is that cycle with exactly one edge deleted. Let its missing oriented start be \(h_1\).

In coordinate \(i\), each connector pair is translated by its profile-specific relative offset \(\delta_i(x)=w_{x,i}-w_{x,1}\), hence it is again an edge of the same step-\(g\) cycle. Since the coordinate is uniform, its incidence graph is a tree, so its connector skeleton is the step-\(g\) cycle with one oriented edge start \(h_i\) deleted.

For a connector \(x\), fix the labeled atom \(e_x\) attached to its first-coordinate residue \(a_x\), rather than the other atom attached to \(a_x+g\). In coordinate \(k\), deleting \(e_x\) splits the tree; let \(c_k(e_x)\) be the number of residue vertices on the connector/profile side of the cut and \(s_k(e_x)\) its profile numerator sum. The edge has the same positive mass in every coordinate; the exact tree-flow cut identity is
\[
pN z_{e_x}=p\,s_k(e_x)-N\,c_k(e_x).
\]
Subtracting the \(k=1\) and \(k=i\) identities and using \(\gcd(N,p)=1\), with \(c_k\in\{1,\ldots,p-1\}\), gives
\[
\boxed{c_i(e_x)=c_1(e_x).}\tag{2}
\]

On the directed step-\(g\) path with missing edge start \(h_k\), the number of residues on the connector side after deleting its atom at start \(a_x+\delta_k(x)\) is the least positive representative of
\[
(h_k-a_x-\delta_k(x))g^{-1}\pmod p .
\]
Therefore (2) implies
\[
(h_i-a_x-\delta_i(x))g^{-1}
\equiv (h_1-a_x)g^{-1}\pmod p .
\]
Multiplication by \(g\) yields \(\delta_i(x)=h_i-h_1\), independently of \(x\). This proves (1).

If all connectors shift by \(\beta_i\), their entire mass contribution to coordinate \(i\) is the common translate of their first-coordinate contribution. Since that first-coordinate column mass is exactly \(1/p\), uniformity in coordinate \(i\) is then equivalent to the singleton mass-vector being the same translate. The equality can be checked by exact integer numerator sums, as in r362. This proves the classification and both corollaries.

## Exact non-northwest illustration

Take \(p=5\), \(m=10\), numerator vector \((2,1,1,1,1,1,1,1,1,1)\), \(N=11\). First compute the standard rational northwest allocation from r362, then relabel **every first-position column \(a\) as \(2a\bmod5\)**. It remains first-position uniform, has 14 positive cells, and its four connectors now bridge \((0,2),(2,4),(4,1),(1,3)\): step \(g=2\), not the northwest step 1 in the ordinary residue ordering.

Giving the four connectors coordinate-2 offsets \(1,2,3,4\), and all singleton profiles offset 1, yields the exact second-position distribution
\[
\boxed{(9,14,9,9,14)/55},
\]
rather than uniform \((11,11,11,11,11)/55\). No alternate singleton offsets can repair this choice of distinct connector offsets, by the theorem. Equal offsets on **all** profiles produce a uniform second coordinate by global translation.

The example only illustrates the theorem; the proof handles all admissible rational masses and all first-coordinate step-\(g\) trees, not only a relabeled northwest allocation.

## Scientific provenance and next discriminating step

This extends r362's entire northwest-order no-go to every fixed-step cyclic residue skeleton. The remaining possible sharp-support OAI7 graphs must mix connector gaps or introduce degree-three-or-higher profiles. Those candidates can be checked by r360's exact simultaneous tree / labeled cut-signature criterion, keeping positive rational weights and true 350-profile contributions.

Reused exact sources: OAI7 original Task RS-OAI7-028-C-20261007-6F2A81, immutable TP2-96FAC49786245691AE19, original researcher EM-EMF6D046-5A2844; r357@22bd6c41175866bc05595faf26ec7745f84b3b54; r359@12c7809e30111287c70430fdaae51bd402be626d; r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a; r361@9a8ac6b7f013efd808ae101d9fdb1ff7a436b953; r362@56be4c9f0b13b12ab781fced72b2a8ca019d0756. Author-side theorem, no independent Native review, freeze, Activity association, CLAIM, Task DONE or mother-objective completion.
