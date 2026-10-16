# Same-E identification: pointed rigidity and a genuine covering-label ambiguity

Author EM-DVR-F73673. FROZEN UNREVIEWED paper note, classical external elliptic models over Q/R only. This is a same-method-family extraction of standard facts with a concrete counterexample to a stronger evidence claim; it is not a new Task, shared Tool, portable certificate, independent vote or external novelty claim. No program was run. It neither changes the fixed core98 candidate/code/input/clock nor supplies its actual mixed bit, rank, selected four-cover or map exports. The active frozen full-bundle review continues separately.

## 1. A pointed isomorphism cannot arbitrarily permute the three real roots

Let E over Q have nonsingular model y²=(x-e1)(x-e2)(x-e3), with three distinct real rational e_i, and marked origin O at infinity. Every Q-automorphism of E fixing O is ±1. In fact the same holds for every R-automorphism fixing O.

Proof. By the standard pole spaces L(2O)=<1,x>, L(3O)=<1,x,y>, an automorphism fixing O has x'=a x+b and y'=c y+d x+e with a,c nonzero. Substitution into y'²=product(x'-ei), using the free Q(x)-basis{1,y}, makes the coefficient2c(dx+e) of y vanish, so d=e=0. Comparing highest powers of x gives c²=a³, hence a>0 over R. The affine function ax+b therefore preserves real order and permutes the three branch roots, so it fixes their minimum and maximum. Two distinct fixed roots imply a=1,b=0, then c=±1. This proves the assertion; no numerical j-invariant or rank hypothesis is needed.

For core98, the roots are ordered in the input as(0,25921,16129), though their REAL sorted order is0<16129<25921. The proof uses real ordering only to establish rigidity; it does NOT sort or relabel the frozen CRT input. Any two pointed Q-isomorphisms from the SAME auxiliary elliptic model to this exact E differ by ±1. In particular their induced action on E[2] is identical, since −T=T for every2-torsion point. Merely replacing a pointed same-E isomorphism by its negative cannot secretly exchange the root labels. This is a conditional assertion about two actual pointed isomorphisms, not evidence that a returned map has been exported or certified.

## 2. The pointed hypothesis cannot be dropped from a covering certificate

Consider a primitive P11 core for which the already proved no-rational4-torsion result applies, and write T0=(0,0) in E(Q)[2], T0 nonzero. The same underlying smooth genus-one curve C=E and the same Jacobian E admit two Q-defined degree4 morphisms

    pi0(P)=[2]P,                 piT(P)=[2]P+T0.

Both are genuine2-coverings. Their classes in H1(Q,E[2]) differ by the Kummer class delta2(T0), which is NONZERO. Indeed choose S in E(Qbar) with[2]S=T0. Then piT=[2] composed with translation_by_S. The descent cocycle of that trivialization is sigma(S)-S, exactly delta2(T0). If delta2(T0)=0, the exact Kummer sequence would give T0=[2]P for some P in E(Q). Then[4]P=O and[2]P=T0≠O, a rational point of order4, contradicting the reused no4 result. Thus the two covering classes are different even though their domain equation, bare Jacobian and all Jacobian invariants coincide.

The concrete example is deliberately a rational-point Kummer class: both underlying E-torsors have zero class in Sha. It proves a LABEL/COVERING-DATA ambiguity, not a change in a Cassels–Tate value. Pairings descending to Sha annihilate rational Kummer classes. One must not use this example to claim that the existing Magma routine returns a wrong bit, that ±1 reverses a half-valued bit, or that different valid lifts in the already proved first-form-zero setting give different values.

## 3. What the boundary requires, and what it does not

A statement that a genus-one model has Jacobian isomorphic to E does not alone certify that its specified2-covering class is U2 or U3, nor that a particular four-cover has the required lower cover and maps. Pointed isomorphism rigidity removes one possible permutation concern but leaves the covering morphism and its translation/normalization data to be checked. Existing exact API contracts may supply those mathematical identifications at IMPLEMENTATION-observation strength; exporting actual degree2/degree4 maps and verifying their equations is stronger portable evidence. An unreadable printed Map rule is not a polynomial identity certificate.

For the current candidate, the exact CRT classes, TwoCover calls with E:=E, ordinary FourDescent and associated-cover maps remain the already frozen route. This note adds no invocation or runtime gate. The Task can at most report a version/model-bound implementation candidate with retained actual exports/limitations. If a later independent assessment requires a portable class-labelled certificate, the actual defining equations/maps or another rigorous identification proof must be supplied separately; this note does not manufacture them. Actual C4, exported f/localpoints/support, e=beta(U2,U3) and rank remain UNKNOWN.

## Sources and reuse

The pole-space form and Kummer exact sequence are standard classical elliptic-curve facts; their necessary argument is given above rather than attributed to an unseen new primary source. The P11 primitive no4 input is reused from accepted Source3fca728daf92abc5a4cad36102f5ec58c82aba0f, research_artifacts/mcp/RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC/MCP-b4bf84ccfffc4affacc0f551cb1fa0ad/e486dcbc06d80c035317/RETURN.md,13858B SHAc4bc0846af97b5f15eca90af7122ec44c2227a9a3152360cf3aa864cb2a3ed24, section3. Its accepted review is research_result_reviews/RR-C1F5BD75CF29E3970097/DR-2F805343ED6728A5CD35.json at that same Source. Do not reopen or reprove that accepted Task.

The separate uniform torsion paper Sourcea68132d8f8155e94723533417e04fa45f7ea3d81, research_notes/owner_goal_20261016/p11_uniform_torsion/P11_UNIFORM_TORSION_AND_EMPTY_OR_INFINITE_STRICT_FIBER_PAPER.md, and its genuine separate review Sourceb194ffe515e2b7e3dfdf885d27aa451a9085df24 strengthen the larger family's torsion description; this note needs only the primitive no4 conclusion. It does not reuse those paper verdicts as an independent verdict for this new note. The root dictionary/API and evidence boundaries remain those in the separately reviewed9118B exact-input bridge at Sourcee98bf97fb3773523e307d6b6d8160b5e65101f3d, peerSourcebb54b2b275090772ab579f02fa9b0bd5a6b81f8a.
