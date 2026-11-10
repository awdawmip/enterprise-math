# BRC-X6 / Full-positive degree-8 fibers are quadratically connected (author portable)

**Date:** 2026-11-10. **Status:** AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is author-side evidence, not a native Source Task publication, independent review, or claimed D25 execution.

**Frozen science pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Reuses the original 38 policies of the d=2..7 quadratic fiber certificate at immutable commit `215c77873ea2f3779ee0236a7594de8f4449e834`; four sources, six labelled actions at each source and the nine frozen roots' joint conservation. No new scientific premise.

## Theorem (all strictly positive denominator-eight targets)

Let `C in {0,1}^{24x38}` have entry `C[6s+a,j]=[p_j(s)=a]` for original labelled policies `p_j in {0,...,5}^4`. For every `b in Z_{>0}^{24}` with each 6-entry source block summing to 8 and `b in col_Q(C)`, the exact integer fiber
`F_8(b)={n in Z_{>=0}^{38}:Cn=b, sum(n)=8}`
is **nonempty and connected** by 2-for-2 policy swaps `e_i+e_j -> e_k+e_l` satisfying `C_i+C_j=C_k+C_l`.

Exactly **605** such positive targets exist, supporting **465,292** distinct length-eight policy multisets. Their quadratic-exchange graph has **605 connected components**, one per target. All 605 target fibers have some two disjoint-support decompositions and no universal common policy anchor. The largest fiber has 1,832 vertices.

A verified disjoint-support witness (zero-based indices into the inherited exact list) is
`(0,9,13,19,27,36,37,37)` and `(3,11,15,21,28,31,33,35)`; both produce the native 4x6 integer target
```
1 1 1 1 1 3
1 1 1 1 1 3
1 1 1 1 2 2
1 1 1 1 2 2
```
so this cannot be dismissed as direct cancellation of a policy shared by the two decompositions.

## Exact proof and finite coverage

1. For each source there are `binom(7,5)=21` positive six-coordinate integer count patterns summing to eight. A *separate* exact SymPy rational left-kernel computation finds `rank_Q(C)=13`, hence 11 integer left-nullspace constraints. Among all `21^4=194481` positive targets, exactly **605** lie in `col_Q(C)`. Their set equals `{J+C_i+C_j:0<=i<=j<38}` where `J=(1,...,1)`, so every target has a legal length-eight realization.
2. Exhaustively enumerate nondecreasing 8-tuples of the original 38 policies. The sole branch pruning tests whether a source has more missing action labels than remaining policy slots; no positive leaf can be removed. Enumeration visits **23,449,161** recursive nodes, prunes **18,686,432**, and retains **465,292** strictly positive policy multisets. Every such multiset is included exactly once.
3. The 741 unordered (repetition permitted) pairs of legal policies form **605** four-source incidence-signature classes: 472 singletons, 130 doubletons, 3 tripletons. Build all exact legal pair-swap moves, substitute each into each multiset, check the resulting neighbor belongs to the enumerated set, then union vertices with the same target. **3,233,067** undirected edge *occurrences* are checked (repeat position choices may duplicate an edge), **0** neighbors are missing, **464,687** DSU unions succeed. The graph thus has `465292-464687=605` components. Swaps preserve all 24 counts, so there are at least 605 components; equality proves exact connectivity of every target fiber.
4. Independently confirm the count 465,292 without positive enumeration or DSU. Label each policy by the four occupied source-action coordinates in a 24-bit mask. Apply a 24-bit subset-zeta transform to obtain `k(T)`, the number of policies supported in allowed-coordinate set T. Integer inclusion-exclusion gives
```
sum_(T subset {0,...,23}) (-1)^(24-|T|) * binom(k(T)+7,8) = 465292.
```
The same independent code gives 268 and 17,357 for degrees 6 and 7. All three checkers agree.

Computations use exact integers except SymPy's rational nullspace which is cleared to integer constraints. Full source code, logs, JSON certificate and the more detailed theorem are preserved in the companion 10-file author bundle, **SHA-256 `22d23a44612318c8361074ed7faf68c362984d624ef198c865c5b4b7d8e9e196`**. Code filenames: `native_d8_full_positive_fiber_connectivity.cpp`, `independent_d8_positive_mobius_count.cpp`, `independent_d8_positive_linear_span.py`.

## Exact boundary and next unit

This theorem covers denominator-eight targets with **all 24 source/action counts strictly positive**. Boundary fibers having zero counts are not globally certified by this result. A direct all-state degree-eight DSU attempt (`binom(45,8)=215553195` states) exceeded its execution limit and has **no** valid completion certificate. Next: classify the zero-coordinate degree-eight fibers by exact support strata, or prove general Markov-basis saturation.

**Source isolation:** The canonical D25/LIFT/JT2 science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` and its Source CLAIM remain independent. UR V2 four-file original remains at **94,687 bytes**, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`, still awaiting exact original-byte recovery and authorized writer/provenance; this result neither redoes nor publishes UR.
