# R712 | Exact X6 triad-to-pair shadow fibers and the minimum BRC source repair

**Parent task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS. **Research status:** author-side finite combinatorics with two independent exact integer checks; native V29/V39 event admissibility and independent Driver review remain open. **Native Researcher-ID:** EM-X6-536D3B; **Research-Activity-ID:** RA-039BDE12EFED1D1976153479. Source registration verified at 7838373729a751a165e2e82a3b11fe7698596fdf; neither registration nor GitHub authorship grants a task CLAIM.

**Immutable frozen scientific-input pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. No P000 or ACTIVE worldview change. **Starting frontier:** R711 pairwise-triad closure and its 6,115 pairwise-representable support maps; prior author PR #2052.

## Exact question and BRC carrier

Let V be the six labeled X6 native-axis indices {0,1,2,3,4,5}. Let T=choose(V,3), |T|=20, be candidate triple-source labels. A 20-bit license set H⊆T preserves individual triadic source identity. Its pairwise shadow is

    s(H) = ∂₂H = { {u,v} : exists t in H with {u,v}⊆t },

a 15-bit observer. The shadow is a projection, not a claim that pairwise relations are the physical primitive. Define the shadow fiber F(G)={H⊆T:s(H)=G}, and f(G)=|F(G)|. G is feasible exactly when f(G)>0.

**Future-operation scope:** a future query may test individual tagged triad licenses, or an event may use such a gate; those operations distinguish members of a fiber. If future operations use only the shadow, the shadow remains sufficient for that declared observer.

## Theorem R712.1: the complete shadow is the unique maximally ambiguous image

For every finite vertex set V with |V|=n≥4 and the 3-uniform pair shadow map s, the largest fiber occurs **uniquely** at the complete pair graph K_n.

*Proof.* Fix any feasible G=s(H). Write T(G) for the triangles of G, i.e. triples all of whose pairs belong to G; necessarily H⊆T(G). Let C_G=T\T(G). Define

    I_G(H)=H ∪ C_G.

Every edge of G is covered by H, and every edge not in G is in at least one triple of C_G (indeed in n-2 such triples). Thus s(I_G(H))=K_n. Because H⊆T(G) and C_G is disjoint from T(G), intersecting I_G(H) with T(G) recovers H. Hence I_G is an injection F(G)→F(K_n).

If G≠K_n, C_G is nonempty. Select c∈C_G. The hypergraph T\{c} still covers every pair because every pair belongs to n-2≥2 triples. It belongs to F(K_n) but cannot lie in the image of I_G, whose members all contain C_G. The injection is therefore strict. □

The proof gives a general-n source-fiber theorem; it is independent of any particular X6 event implementation.

## Theorem R712.2: exact six-axis worst-case source information

On six labeled vertices, f(K_6)=477,965. There are exactly 6,115 feasible shadows. The maximum is attained only at the all-15-edge mask, 32767.

Consequently, if s(H) is **already known exactly** and the next observer must recover an arbitrary H, the smallest *uniform fixed-length auxiliary code* has

    ceil(log2(max_G f(G))) = ceil(log2 477965) = 19 bits.

*Lower bound.* At the complete shadow, 477,965 distinct H have exactly the same 15-bit observation. An auxiliary alphabet of at most 2^18 words cannot distinguish all of them.

*Achievability.* For each feasible G, order its fiber F(G) by the ordinary 20-bit H mask and save its zero-based rank. Since all fibers have size at most 477,965 < 2^19, the rank fits in 19 bits, and (G, rank) uniquely recovers H. This is a mathematical coding existence result; the ordinary 20-bit raw-H encoding may be shorter than materializing both G (15 bits) and a fixed 19-bit side channel (34 bits). The side-channel bound describes the missing information *conditioned on* the pair-shadow observation.

## Independent inclusion-exclusion count

For a set S⊆choose(V,2) of forbidden pair edges, let i_3(S) be the number of 3-vertex sets containing none of the forbidden pairs (the number of independent triples of the graph S). By inclusion-exclusion over the 15 pair edges, the number of H covering every pair is

    f(K_6) = Σ_{S⊆choose(V,2)} (-1)^|S| 2^{i_3(S)} = 477965.

Reason: a selected triad family avoids covering every pair in S precisely when all selected triples are among the i_3(S) independent triples, admitting 2^{i_3(S)} choices. This computes f(K_6) using 2^15 pair masks, independently of enumerating 2^20 source supports.

An independent 2^20-mask recurrence using s(H)=s(H\{t})∪choose(t,2) recovered all 6,115 nonempty fibers, the maximum above, and the exact size distribution:

    fiber size : number of 15-bit feasible shadows
    1:2713, 2:480, 3:180, 5:75, 6:630, 7:810,
    29:60, 30:180, 35:420, 42:180, 125:20,
    159:180, 388:6, 417:60, 799:45, 1850:60,
    21450:15, 477965:1.

The identity Σ_G f(G)=2^20 is also checked.

## R712.3: exact information-loss witness and dynamic interpretation

Let H_all=T, and H_minus=T\{{0,1,2}}. Both have complete 15-bit shadows: every pair belongs to four possible triples, so removing a single triple leaves pair coverage unchanged. The source query "is {0,1,2} licensed?" returns 1 on H_all and 0 on H_minus.

Any admitted event transition that conditionally reads that exact triple gate can therefore distinguish these states after one step. This witness states a precise possible future operation; the native frozen X6 Cell/Link/Port + V29 PASS/TRANSFER + V39 j update needs its own interface check before it is called an actual native event.

Under the **declared auxiliary model** where each of the 2^20 triad supports is equiprobable, the probability of observing a complete pair shadow is exactly 477965/1048576. This is an observation-model calculation, not a measured physical frequency.

## Source reuse and literature positioning

- R711 same-task source: https://github.com/awdawmip/enterprise-math/pull/2052, establishes the shadow closure operator and 6,115 image supports.
- The 3-uniform hypergraph 2-shadow is an established combinatorial object; e.g., Z. Füredi and Y. Zhao, "Shadows of 3-Uniform Hypergraphs under a Minimum Degree Condition", SIAM J. Discrete Math. 36(4), 2022, DOI 10.1137/21M1450227. No priority claim is made for the general notion or inclusion-exclusion technique.
- BRC applied as the *tagged Boolean source family and observation map*, with the exact future-query interface and lost-fiber information identified. No signed cancellation or positive-mass dynamics was silently introduced.

## Verification and remaining research unit

Validated locally with standard-library Python exact integers: all 1,048,576 triadic source supports; independent inclusion-exclusion over all 32,768 forbidden-pair masks; complete fiber histogram; exact nontrivial equal-shadow pair; rank/unrank samples. Result:

    R712_SHADOW_FIBER_EXACT_PASS 6115 477965 19 2713 477965

Program: R712_SHADOW_FIBER_VERIFY.py. JSON evidence: R712_SHADOW_FIBER_RESULTS.json.

**Next smallest discriminating native test:** Read the frozen original Cell/Link/Port, V29, V39, closure, signed/time semantics. Construct a *single admitted common Cell/state/time* for which the twenty triples have a well-defined Boolean gate vector H. Determine whether two legal states in one s-fiber exist and whether the actual native event reads a source-specific triple. Record exact typed state, link/port inventory, conservation ledger, j flow, outcome and rotation-covariant address transform. If the actual native operation can read only s, use the smaller observer; if it reads H or a refinement, retain the required BRC source coordinates. Do not transfer arbitrary 20-bit-pattern statistics into native physics without admissibility evidence.
