# R762GR — Exact absorption-time moments via a 74-state BRC symmetry quotient

Research date: 2026-11-20 (Asia/Shanghai).
Frozen task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
Frozen science: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.
Prior work: R762GM/GN/GO/GP/GQ, in particular R762GQ PR #2837@3519d2a356768baa444b6df7b125b82f93a516be.
Historical contributor lineage: EM-X6-3050F6 (attribution only; current authenticated CLAIM not asserted).
Status: author-side theorem + exact finite certificate, NOT_REVIEWED.
Output type: constructed signed moving-Port K4-STAR model, not an admitted primitive TRIADIC_CLOSURE_E force law.

## Exact state, observer and problem

Let E=(01,02,03,12,13,23), indexed 0,...,5, and let S_v be the ordered triple of edge indices incident to v in this E-order. For each vertex v=0,1,2,3, let g_v in A6 cycle S_v and fix the remaining axes; sign s=+1 or -1 selects g_v^s. Let p in A6 denote an even orientation permutation and x in Z^6 the *complete* six-dimensional relative Cell displacement. The initial state is (0,id), with an initially named unoriented Port 01. At (x,p), Port p(01)=E[p(0)] admits exactly the signed letters (v,s) where v is an endpoint of that edge. A candidate letter changes

    x' = x + s p H_v,    p' = p g_v^s,

where H_v is the six-axis incidence vector of S_v. The four distinct admitted source letters each have BRC counting weight 1/4. Their ordering, sign, multiplicity and provenance remain in the full-path representation.

For the *specific stopping observable* tau := first step m>=0 such that p_m(01)=23, the orientation projection (x,p)->p is exact: future Port permissions and absorption depend only on p. This is not a whole-State or all-observer quotient; Cell return, signed history, native force status and time are not discarded for those other purposes.

Earlier R762GN/GO/GQ prove that A={p in A6:p(0)=5} has 60 orientations and is closed under legal transitions; the initial reachable part has 350 states, with 290 outside A. A sharp eight-step survival bound holds uniformly on reachable transient states:

    Pr(tau>m+8 | survival to m) <= 9913/16384 < 1.

In particular tau is finite almost surely. R762GQ used 600-step exact integer source counts to give extremely tight decimal moment intervals. Here we remove the tail estimate altogether.

## New theorem 1 — exact observer-safe finite quotient, 75 total states

Let H be the order-four subgroup of vertex S4 that stabilizes the *unoriented* initial edge {0,1} as a set. For each sigma in H, let q_sigma in S6 permute the six unordered edges by induced relabeling. Define on orientations

    Phi_sigma(p) = q_sigma p q_sigma^{-1}.

Then Phi_sigma preserves A, the initial orientation, and the BRC transition multiset up to a bijective renaming of legal signed letters. Specifically, conjugation sends every g_v^{+/-1} to some g_{sigma(v)}^{+/-1}; the sign may reverse, but both signs are present with equal weight. Moreover q_sigma fixes the index of 01 and fixes the index of 23. Consequently the current named Port relabels equivariantly, including its legal endpoint set.

Among the 290 reachable transient states the H-orbits consist of precisely 72 orbits of size four and two singleton orbits (290=72*4+2). Each orbit has the same multiplicities of successor *orbits* for every member. Thus these 74 orbits define an all-horizon BRC lumping for tau. Merge the 60 already-absorbed orientations into one absorbing sink; the resulting exact Markov representation has 75 states: 74 transient plus one sink.

**Scope-specific optimality.** Start the entire 350-state reachable orientation graph with one transient and one absorbing color, and refine colors by the ordered pair (old absorbing status, multiset of successor color multiplicities) until stable. The finite exhaustive algorithm stabilizes after seven signature rounds at 75 classes. The 74 transient H-orbits and absorbing sink are exactly those classes. Hence this 75-state partition is the *coarsest strong probabilistic lumping that distinguishes absorption* of the complete reachable orientation graph. This is a finite, explicitly checked claim; it is not a universal minimal state description for other observables.

For each transient orbit i define Q_ij as the number (0,...,4) of its four signed letters leading to transient orbit j. The rows are independent of representative. The exact 74x74 integer matrix Q has 256 nonzero entries; 40 rows have no immediate sink letter, 34 rows have one. Its substochastic transition matrix is Q/4.

## New theorem 2 — exact rational first and second moments

Let 1 denote the length-74 vector of ones. Let m_i=E_i[tau] and s_i=E_i[tau^2] for starting orientation orbit i. The first-step identities are exact:

    (4I-Q)m = 4*1,
    (4I-Q)s = 4*1 + 2 Qm.

The eight-step strict contraction proves rho(Q/4)<1, so 4I-Q is invertible over Q; the two systems have unique rational solutions. For the orbit of p=id the exact values are

E[tau] =
6409738399123005412954656583577
/495363346840489578328015271562

E[tau^2] =
54390632463292690076320354262525376494819244381842931604456288
/206346347262304852800932979802953488641109919587409691341687

Var(tau) =
873052213612776278536712503410057102839600395090537335909824299
/9079239279541413523241051111329953500208836461846026419034228

Approximate decimal *readouts* (exactness is supplied by the fractions):
E[tau] = 12.9394684528142641972144...;
E[tau^2] = 263.5890248842254023722656...;
Var(tau) = 96.1591810428498342847044....

All values strictly fall in the previously published R762GQ rationally certified intervals. This strengthens the finite-horizon interval computation to exact closed rational constants, without claiming a native physical waiting-time distribution.

## Proof, exhaustive certificate and arithmetic

The signed letters and orientation successor graph are reconstructed directly from E, S_v and g_v; no prior computed adjacency file is trusted. A complete BFS verifies 350 reachable orientations, 290 transient and 60 absorbing. The four vertex relabelings fixing initial edge 01 are generated directly; H-conjugation orbits are then constructed from actual permutations. Each transient orbit's 4-letter outgoing multiset is compared with every other member to certify the quotient. The separate color-refinement algorithm starts only from the absorbing/nonabsorbing bit and verifies the coarsest-equitable 75-state partition, including equality to the orbit partition. It is independent of the moment linear system.

The verifier forms M=4I-Q using exact integers. SymPy exact rational matrix inversion, not floating-point fitting, solves both systems. It asserts each result is strictly contained in R762GQ's certified decimal intervals interpreted as exact rational endpoints. A second forward source-count recurrence on the full 290-state transient orientation graph reproduces R762GQ's 12-step and 16-step survivor totals, 6,534,252 and 1,118,196,052. The verifier prints a JSON evidence summary with all exact numerators and denominators. All checks passed in local author execution. Mathematical verification is author-side; independent review remains NOT_REVIEWED.

## Residual/provenance discipline and next question

This quotient is exact for the BRC-weighted all-horizon absorption observable tau and for its future observation under the specified stochastic candidate transitions. It need not preserve the signed path word, distinct branches, Cell coordinates, six-axis common depth, time trace, or a future native TRIADIC_CLOSURE_E test. Such future questions use the original lifted state plus source provenance, not the collapsed sink/74-orbit state alone.

Next native discriminator: specify a legal signed primitive triadic Cell/Link/Port/time event and check whether its permitted transitions actually commute with H's four edge relabelings while preserving full provenance. A single violating event disproves the lifted symmetry for that law. Independently, analyze which source-sensitive future observers force a repair coordinate beyond the 75-state absorption quotient.

Files: R762GR_EXACT_ABSORPTION_QUOTIENT.md (this proof), R762GR_CHECK.py (reproducer), R762GR_EVIDENCE.json (author-side certificate). The GitHub commit is durable portable research only; no native protected PROGRESS, accepted Result, live CLAIM or independent Review is asserted.
