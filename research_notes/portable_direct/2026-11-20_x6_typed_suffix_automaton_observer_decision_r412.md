# X6 r412 — Exact typed-admissibility test for suffix-calibrated signed-frame orbit observers

Date: 2026-11-20 (Asia/Shanghai)
Status: **author-side deductive research / finite verification**, not an independent native Result review.
Task context: RS-X6-NATIVE-ROTATION-DYNAMICS; task ownership and original contribution attribution unchanged.
Continuity: r411 fixed-source note \`5e3d07b05799754cb1b4327e97bb30aaf12f0652\`, and original signed-word orbit classification at \`9d09f6bc13b36a8d47d11b524fae4dd5254ac333\`.

## Question and native typing

r411 proves that a fixed suffix must exhibit all six unsigned axes to make the *unrestricted signed-primitive-word* orbit observer injective. That need not be the sharp threshold for a **restricted legally composable typed event language**. Derive a test using the actual admissibility predicate, rather than silently treating any signed letter as a stable native event.

Fix the previously derived **candidate static frame action**, not a proved physical rotation:
\[
\Sigma=\{\pm e_1,\ldots,\pm e_6\},\qquad
H=(C_2)^6\rtimes A_6,\quad |H|=23040.
\]
Let \(E\) be a **finite candidate event alphabet** with injective primitive representation \(c:E\hookrightarrow\Sigma^3\); each event is given a chosen ordered three-letter **record code**, not automatically three successive native displacements. P000's simultaneous three-force closure must not be identified with a three-step path merely because both use three labels. The eligibility of any element of \(E\) for P000's native nonzero three-force closure \(E_{\mathrm{closure}}\) is an *input to be established*, not an axiom introduced here. For an event word \(w=a_1\cdots a_n\), put \(c(w)=c(a_1)\cdots c(a_n)\). If a native event carries extra source, Cell, branch, or time data, these must be preserved in the admissibility machine or encoded into an injective observer before a claim of full native-state preservation.

Let \(L\subseteq E^*\) be a regular language of *allowed completed event trajectories*, represented by a DFA \(\mathcal A=(Q,E,\delta,q_0,F)\). Such a DFA is a conditional finite-state **representation** of typed closure/composition/Cell/time constraints. We do not claim native P000 legality is automatically finite-state. Fix a prescribed suffix \(s\in E^*\), and define the actually appendable prefixes
\[
U_s=L/s=\{u\in E^*:us\in L\},\qquad
\mathcal O_s(u)=[c(us)]_H .
\]
The suffix is fixed in the **same reference frame** when comparing two prefixes; we do not independently relabel the suffix.

## Theorem A: exact regular-language decision criterion

For each \(g\in H\), define
\[
D_g=\{(a,b)\in E^2:g\,c(a)=c(b)\}
\]
and the suffix pointwise stabilizer \(K_s=\{g\in H:g\,c(s)=c(s)\}\).
For each \(g\in K_s\), form a directed graph on
\[
Q\times Q\times\{0,1\}
\]
with start \((q_0,q_0,0)\), and for every \((a,b)\in D_g\) a transition
\[
(q,q',d)\longrightarrow
(\delta(q,a),\delta(q',b),\,d\lor[a\ne b]).
\]
A vertex is accepting when \(d=1\) and
\(\delta^*(q,s)\in F\), \(\delta^*(q',s)\in F\).

**Exact result.**
\[
\boxed{\quad
\mathcal O_s\text{ is injective on }U_s
\iff
\text{for every }g\in K_s\text{ its graph has no reachable accepting vertex}.
\quad}
\]

If the observer is not injective, the procedure returns an **explicit pair of distinct allowed prefixes** \(u,v\in U_s\), a common-frame element \(g\in K_s\), and the equality \(g\,c(us)=c(vs)\). There is always such a witness of at most \(2|Q|^2-1\) **event blocks per prefix**. For fixed \(H\), using a dictionary for the injective three-letter event encodings, the graph part of the exact decision has time \(O(|K_s|\,|Q|^2\,|E|)\) and space \(O(|Q|^2+|E|)\) per group element, apart from group enumeration and fixed-suffix processing.

**Proof.** Equality of two whole-word \(H\)-orbits is equivalent to \(g\,c(us)=c(vs)\) for some single \(g\in H\). Because \(g\) acts letterwise and the event encoding has constant length three, comparing the last \(|s|\) event blocks gives \(g\in K_s\), and comparing the first blocks gives a sequence of pairs from \(D_g\). Conversely, such paired transitions concatenate to \(g\,c(u)=c(v)\) and therefore to the full orbit equality. The DFA components exactly express \(us,vs\in L\); the Boolean component exactly expresses \(u\ne v\), using injectivity of \(c\). Thus any accepting path is a counterexample, and every counterexample produces an accepting path. A shortest accepting path in a graph with at most \(2|Q|^2\) vertices has no repeated vertex and hence at most \(2|Q|^2-1\) edges. Since \(c\) is injective, each \(g\) supplies at most one \(b\) per \(a\), giving at most \(|E|\) outgoing edges per graph state and the stated graph bound. QED.

## Corollary B: sharp test for arbitrary concatenations of admissible events

When \(L=E^*\) (all candidate events concatenate freely), the exact condition reduces to
\[
\boxed{\quad
\forall g\in K_s\ \forall a\in E:
\quad g\,c(a)\in c(E)\Longrightarrow g\,c(a)=c(a).
\quad}
\]
A violating pair of one-event prefixes already certifies failure. If \(E\) is \(H\)-invariant, this is \(K_s\subseteq\ker(H\curvearrowright E)\). With \(E=\Sigma\) and one-letter encoding (the corresponding length-one variant of the same proof), the faithful action restores r411: \(K_s=\{1\}\). For a proper event language, a nontrivial \(K_s\) can be harmless because its moved prefixes are inadmissible.

## Explicit algebraic checks (candidate triples, NOT asserted P000-legal triads)

Put \(a=(e_1,e_2,e_3)\), \(b=(e_4,e_2,e_3)\), and \(d=(-e_4,e_2,e_3)\), with fixed suffix \(s=a\).
The \(H\)-stabilizer of \(a\) has exactly \(3\cdot 2^3=24\) elements: an even permutation of the three unused axes, and arbitrary flips on them.

- If the candidate alphabet is \(E_1=\{a\}\) and \(L=E_1^*\), the orbit observer \(u\mapsto[c(us)]_H\) is injective for all prefix lengths despite \(|K_s|=24\). Every stabilizer fixes the only permitted event.
- For \(E_2=\{a,b,d\}\) and \(L=E_2^*\), the element that flips the sign of axis 4 fixes \(s=a\) and maps \(b\leftrightarrow d\). Hence the distinct allowed prefixes \(b,d\) give a concrete counterexample: \([c(bs)]_H=[c(cs)]_H\).

A direct exact enumeration of all 360 even unsigned permutations and 64 sign choices verified \(|H|=23040\), \(|K_s|=24\), absence of one-event collisions in \(E_1\), and the explicit \(b,d\) collision in \(E_2\). These finite checks illustrate the theorem; the graph-equivalence proof applies to arbitrary finite DFAs and word lengths.

## Integration and remaining native input

This resolves a specific overgeneralization risk after r411: **six-axis coverage is sharp for unrestricted primitive signed words; the exact typed event threshold is the stabilizer's action on the admissible contextual language**. Once the genuine P000 triadic closure predicate, Cell/branch provenance and permitted time-ordered transitions are specified, construct their exact admissibility recognizer when finite-state, or use the unbounded-language characterization directly. A legal-event witness must first be checked against that actual typed model. If the event encoding hides time/Cell distinctions, enlarge the observer or retain that data before attempting native-state losslessness.

This is a static candidate group-action theorem and an exact conditional decision algorithm. It preserves the locked X6 + time ontology and triadic closure requirement; it neither constructs a native physical rotation nor asserts task completion. Existing X6 group/orbit authors retain their actual provenance. The current Driver's derivation is author-side and shares this research context, so it is **not** an independent formal Native Review, source Activity association, accepted Result or CLAIM.

Relevant fixed inputs:
- r411: https://github.com/awdawmip/enterprise-math/blob/5e3d07b05799754cb1b4327e97bb30aaf12f0652/research_notes/portable_direct/2026-11-20_x6_signed_frame_contextual_calibration_r411.md
- Prior original researcher: https://github.com/awdawmip/enterprise-math/blob/9d09f6bc13b36a8d47d11b524fae4dd5254ac333/research_artifacts/mcp/RS-X6-NATIVE-ROTATION-DYNAMICS/MCP-c618a61189764f23846a391a08518a1a/0f0e002ae5e625394259/X6_SIGNED_WORD_ORBIT_SPLITTING_AND_CONCATENATION_20261116.md
- P000: \`projects/enterprise-math/P000_REALITY_FOUNDATION.json\` (global canonical).
- Native time/Cell basis: \`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json\` (project).
