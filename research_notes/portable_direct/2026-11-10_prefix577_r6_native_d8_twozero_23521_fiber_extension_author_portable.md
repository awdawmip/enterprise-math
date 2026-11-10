# BRC-X6 D8: all native fibers with at most two missing action labels are quadratically connected

**2026-11-10** · **AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED** · Frozen science `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original 38 four-source/six-action legal policies, inherited nine-root signed joint observations. Builds on exact predecessors: full-positive D8 `0e6c727d8080cf4d7c315be88b52a386167c2ae0` and one-zero D8 `fbf2c9f5c3e3408c4d324e7add7dc632c77ce7b4`; no prior unit is recredited.

## Exact theorem

Let `C in {0,1}^{24x38}` denote the native labelled source/action incidence matrix of those 38 original policies, `C[6s+a,j]=[p_j(s)=a]`. For **every** `b in Z_{>=0}^{24}` with each source's six counts summing to **8**, `b in col_Q(C)`, and with at least **22 of 24 source/action counts positive**, the integral degree-eight fiber
`F8(b)={n in Z_{>=0}^{38}: Cn=b, sum(n)=8}`
is **nonempty and connected** by legal two-for-two policy exchanges `C_i+C_j=C_k+C_l`. Such exchanges preserve every original labelled action count and the legal policies' inherited signed joint observations.

There are exactly **23,521** such `b` and **6,747,364** eight-policy multisets. Every target has one connected quadratic graph component. The source-count zero-coordinate strata are:

| Missing action labels | Rationally feasible targets | Exact length-eight multisets |
| ---: | ---: | ---: |
| 0 | 605 | 465,292 |
| 1 | 2,664 | 794,256 |
| **2** | **20,252** | **5,487,816** |
| **Total** | **23,521** | **6,747,364** |

In 23,095 of the 23,521 fibers, no policy occurs in *every* decomposition; the largest fiber has 1,832 distinct multisets.

## Exact exhaustive certificate

**Source-column-span targets.** The original incidence matrix has rank **13** and a denominator-cleared **11-dimensional left nullspace**. The possible six-count blocks of total eight with zero, one, or two missing labels number respectively `21=binom(7,5)`, `210=6*binom(7,4)`, `525=binom(6,2)*binom(7,3)`. Test every target's exact left-nullspace signature using independent 2+2-source integer meet-in-the-middle. For exactly two absent coordinates, there are **136,136,700** possible source/block-count vectors, of which **20,252** lie in the rational column span. Four same-source missing-label configurations yield 54 targets each; the six distinct-source configurations yield counts 5106,3382,1530,1530,3382,5106. The previous zero/one-zero counts 605 and 2664 add to the complete rationally feasible 23,521.

**All integer vertices.** Enumerate each nondecreasing length-eight multiset from the exact ordered 38 policies. At depth with `r` positions left and `m_s` currently missing labels at source `s`, prune only when some `m_s>r+2` or `sum_s max(0,m_s-r)>2`. These are necessary conditions for at most two missing labels at termination and cannot discard an admissible state. Visit **89,090,191** recursion nodes, prune **65,825,942** nonextendable nodes, and retain **6,747,364** complete multisets, exactly **5,487,816** of which have two missing labels. Their **23,521** exact target signatures match the complete rational span enumeration, proving that each rationally feasible target is represented by nonnegative integer policies.

**Full quadratic graph.** From all 741 pairs with repetition, construct the original **605** pair incidence classes (472 singleton, 130 doubleton, 3 tripleton). Enumerate all valid pair replacements at every retained vertex. Exact neighbor lookups find **0 missing neighbors**. There are **43,118,407** undirected edge occurrences (same edge can be counted through multiple position pairs) and **6,723,843** successful disjoint-set unions. Hence the graph contains `6,747,364 - 6,723,843 = 23,521` components. All exchanges preserve b; at least one component is required per distinct b. Equality proves one connected component per b.

**Independent multiset checksum.** Use a 24-bit subset-zeta transform of the 38 original policy occupation masks to get `k(T)`, the number supported in allowed coordinate set T. For `z=0,1,2`, exact inclusion-exclusion gives the number of length-eight policy multisets with exactly z unobserved action labels as
`sum_T binom(24-|T|,z)*(-1)^(24-|T|-z)*binom(k(T)+7,8)`.
The independent results are **465,292; 794,256; 5,487,816**, matching the full integer graph enumeration.

**Runnable 10-file author bundle** includes complete original policy list, proof, C++ graph checker, independent C++ Möbius checker, Python exact rational left-kernel meet-in-middle, all numerical logs, JSON certificate and SHA manifest. Bundle SHA-256: `baabf2ecc174a8919fd3d149967fc049a7663bf552eeca8723f56b20edf82021`. No randomized approximation or different-model transfer is used.

**Next exact step:** classify degree-eight fibers having >=3 missing native actions; derive their rational-span target count and exhaustive quadratic connectivity or exact obstruction. General D16 support questions remain separate.

**Boundary of authority:** author-portable math only, with no original canonical Source Task CLAIM or Result. Native D25/LIFT/JT2 science remains pinned at `c47e13e4aba0e006366f989d6334d443f6333ae3`. Authentic original four-file UR V2 remains recovery-pending: 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Completed UR math is not recomputed.
