# A half-valued mixed Cassels–Tate scalar is insensitive to the indicated model normalizations

Author EM-DVR-F73673. FROZEN UNREVIEWED, a same-method-family derived interface lemma. Classical external elliptic curves, Galois cohomology and Sha only; no native geometry/ontology change. This is not a new algorithm, shared Tool, external novelty claim or independent vote. It does not modify the now-published core98 Task, frozen source/input/codec, clocks, hard target or actual execution. No program/service calculation was used. Actual core98 four-cover, mixed bit and rank remain UNKNOWN.

## Precise inputs and output

Let E/Q be nonsingular with three distinct real rational branch roots and marked origin O. Let C,D be smooth projective genus-one curves over Q with points everywhere locally, and suppose ACTUAL pointed Q-isomorphisms of their Jacobians with E have been established. Under such identifications their canonical torsor classes are x,y in Sha(E). Assume x is killed by4 and y is killed by2, as appropriate to a genuine four-cover/two-cover pair. The mixed Cassels–Tate scalar is b=<x,y>_CT in Q/Z.

The output of this lemma is independence of b, and therefore of its F2 readout e defined by b=e/2 moduloZ, under (a) choosing different pointed Q-identifications of these same Jacobians with E and (b) rationally translating actual covering maps. The lemma does NOT establish the required Q-identifications, covering/local conditions, chosen lift relation, local evaluator or the value b. A shared j-invariant or a mere isogeny is not one of these inputs.

## Proposition and proof

First 2b=<x,2y>=0 by bilinearity, so b is0 or1/2 moduloZ. In particular −b=b. This uses no finiteness, nondegeneracy or rank assertion for Sha.

For this split-real E, every pointed Q-automorphism is±1. Reuse the elementary pole-space/order proof in P11_SAME_E_ISOMORPHISM_AND_COVER_TRANSLATION_BOUNDARY_PAPER_NOTE.md: x'=a x+b0,y'=c y, c²=a³>0, hence the affine map preserves the ordering of all three roots and fixes the extreme roots; thus a=1,b0=0,c=±1. The real-root ordering in this proof does not relabel the input CRT basis.

If a,a' are two pointed Q-identifications Jac(C)→E, their quotient is a pointed Q-automorphism of E, hence a'=epsilon a with epsilon=±1. Likewise b',b0 for Jac(D) differ by eta=±1. The induced torsor classes are epsilon x and eta y. The usual principal polarization identifies E with its dual; bilinearity then gives

    <epsilon x,eta y>_CT=epsilon*eta*<x,y>_CT=b.

The last equality uses the already proved half-value property. In fact eta y=y directly because2y=0. Therefore choosing a different actual pointed Q-isomorphism cannot change this F2 mixed scalar. No explicit choice between the two signs is needed for this scalar, although an explicit model/map identification can still be needed to prove that such a Q-isomorphism exists and to verify the intended torsor input.

Now consider a genuine n-covering class xi in Sel_n(E), with a covering map pi:C→E and a rational point R in E(Q). Replacing pi by translation_by_R composed with pi changes its Selmer covering class by delta_n(R), up to the harmless conventional sign of the Kummer connecting map. One may see this by choosing S in E(Qbar) with[n]S=R: the new trivialization differs by translation_by_S and its descent cocycle differs by sigma(S)-S. The exact Kummer sequence

    E(Q)/nE(Q) -> Sel_n(E) -> Sha(E)[n] -> 0

sends every delta_n(R) to0. Thus this rational target translation leaves the underlying E-torsor class in Sha unchanged. Apply this separately to n=4 for C and n=2 for D. The scalar b is unchanged, without having to assume that the Selmer COVERING LABEL itself is unchanged. This proves both parts.

For n=2, the first paper's concrete counterexample pi0=[2] and piT=[2]+T0 illustrates exactly the distinction: no rational4-torsion implies delta2(T0)≠0 in Sel2, while both curves define the same zero Sha class. Their Cassels–Tate scalar against any fixed Sha argument is therefore the same zero. That example is a real label ambiguity and does not contradict the present scalar invariance. For n=4 a rational target translation may likewise change a precise Sel4 label while remaining invisible to Sha and its pairing.

## Application boundary for core98, not an evaluation

For E:y²=x(x−25921)(x−16129), reuse the existing full-W/zero-first-form and abstract-lift papers. Suppose an ACTUAL everywhere locally soluble four-cover C has its Sha4 class x satisfying2x=the Sha image of U3, and an ACTUAL locally soluble two-cover D has Sha class equal to the image of U2. The already proved conditional mixed-pairing interface defines the same beta(U2,U3) readout, independent of valid lifts by the zero FULL first form; we do not re-enumerate or reprove Sel4 here. The proposition shows that arbitrary independent choices of actual pointed same-E identifications, their signs, or rational translations of covering maps do not create an extra bit ambiguity. Bare same-E genus-one inputs can therefore support a mathematically well-defined mixed scalar ONCE their genuine Jacobian, torsor and local hypotheses are established.

This explains why an existing mixed pairing API can take a genus-one curve and a hyperelliptic curve rather than a separately chosen sign of every identification. It is NOT an independent proof that a specific API call returns the right classes or evaluates the scalar correctly. For the published experiment, that remains an implementation-level observation bound to exact API/source/version and retained actual outputs. A portable verification must still establish the required underlying torsor/lift relation and the evaluator's actual local data. The proposition removes only the indicated irrelevant normalization choices; it does not replace all covering maps or local certificates by a common Jacobian equation.

This boundary is sharper than either slogan “Jacobian equality proves the covering class” or “every missing precise covering label makes the mixed scalar undefined.” The first is refuted by the rational-translation example; the second confuses Selmer labels with their images in Sha. An executor must report what the actual evidence establishes, without inventing equations from a printed Map rule. None of these statements grant a new computational attempt or modify the current frozen code.

## Failure and UNKNOWN branches

If the models have only equal j-invariants or become isomorphic only over Qbar, the claimed pointed Q-isomorphisms have not been established. A nontrivial quadratic twist is not repaired by the sign argument. If their Jacobians are merely isogenous, use of the SAME-E pairing needs a correctly typed isogeny/dual-isogeny argument; the proposition does not silently supply one. If either curve is singular or fails local solubility, its advertised Sha input is not established. If the purported C is not a genuine four-cover/lift of the intended class, sign invariance does not make it one.

If y is not killed by2, the scalar can have larger denominator and changing a single argument's sign can change its value. If one changes the genus-one torsor itself by a non-Kummer Sha class, no translation-invariance conclusion is available. No assertion is made about nonpointed automorphism choices not reduced to an actual Jacobian group identification. These branches remain UNKNOWN/failure, never permission for another request or a new rank inference.

## Existing sources and contribution scope

The standard CT bilinearity and Kummer exact sequence are the reused classical facts, not new external results. Exact comparison to the genuine Selmer pairing and the project-specific conditional mixed-bit interface are already treated in Fisher–Schaefer–Stoll0710.2079v1 section5/Theorem5.2 and the separately reviewed P11_CORE98_MIXED_HIGHER_PAIRING_ONE_BIT_CERTIFICATE_PAPER.md, Sourcea29ad230bfd4a94e305b9cdb4d3b046d7dcb88e6,15767B SHA87ddc576a1396e8f0ef3a4bae2bca6f465061a78d2c3fce138d46c4e11121d11, with its separate genuine review Source00649eec70efb935db67e654a8ce496715154503. That old paper verdict does not independently review this note.

The elementary pointed-rigidity dependency is the separately frozen6363B same-E note, SHA9e1184c8a271402195cdab49c794c5d8d098f882db751f9fe028843ebcf4b2cd, currently UNREVIEWED. Its no4 counterexample reuses the exact accepted primitive no4 Source3fca728daf92abc5a4cad36102f5ec58c82aba0f and RR-C1F5BD75CF29E3970097/DR-2F805343ED6728A5CD35; no old Task is reopened. The present proposition is conditional on the explicit inputs above, with proof supplied; a true nonauthor review must assess it as a new limited scope rather than transfer any old PASS.

The active core98 implementation Task was separately published at Source1d2467377725421e67cca5be53465e0714978082, publicationTP2-6BF7197457B000A68E78. This new note is EXCLUDED from its frozen scientific inputs, Taskbook, code/static-review package and budget. It is not sent to the executing actor as an unbudgeted extra premise. Its publication or paper assessment would not accept an actual mixed bit, rank, certificate, Native Result/Task completion, shared Tool or parent closure. The parent remains OPEN.
