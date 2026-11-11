# R84 — Time-support quotient, envelope-subsumption cache, and matched three-index costs

Date: 2026-11-12. Author-side auxiliary rational circular-source model, NOT native X6/BRC dynamics. Frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34` unchanged. Continuation: R82 scientific source `731f9ca14e596d15f29e75ed3a89a2e0b043b65e`, R83 proof `d4451a0d8ffd359ec43565fa681f23932b6b0405`, and strengthened ALL_OUT construction `feb0c59dcc7fb7cca33a06c9c2c09642d88b764a`.

## Exact model and observation

A finite identity set E consists of pairs (integer time t, branch b). At integer observer j, rational x, integer original labels a,b0, and real parameter theta, the source-membership predicate is M_t(theta): {x+(t-j)theta} belongs to the directed half-open original-labelled target circular arc [{a theta},{b0 theta}); coincident endpoints mean empty arc. The latest-*time* observable is W_E(theta)=max({t : exists branch (t,branch) in E and M_t(theta)}), or NONE. The branch identity is retained separately for future operations and other readouts. A Task proof would require its own frozen task inputs and formal admission.

### Theorem A: time-support quotient for latest-time readout

Let T(E)={t: exists b with (t,b) in E}. If T(E)=T(E'), then for every real theta, observer and original-label query, W_E(theta)=W_E'(theta), including at wrapped/half-open boundaries. This is an identity of functions on the entire parameter domain, since M_t does not inspect branch. Therefore branch insertion/deletion preserving T does not invalidate a latest-*time* result or a time-only query certificate. The conclusion does **not** apply to a branch-specific winner identity: {(5,1)} and {(5,2)} have identical latest times but different provenance. A time-only quotient alone is not sufficient to execute arbitrary future branch deletions: an identity/branch registry must be retained. This is an observer-specific exact quotient, not wholesale elimination of BRC provenance.

### Theorem B: R71 exclusion certificates are downward closed under phase-envelope containment

Fix reduced rational anchor theta0=p/q, an original anchor phase class r (all t p mod q equal r), observer (j,x), original labels (a,b0), and a rational closed interval I=[L,U] containing theta0. Assume on I the two boundary floors are constant and the original target arc stays ordered and nonwrapping as in R71. Let C be a nonempty finite source class with min/max times lo,hi. Set beta={r/q+x-j theta0}, and let S(C,I) be the closed interval with endpoints given by the minimum/maximum of beta+(t-j)(theta-theta0) over (t,theta) in [lo,hi] x I. Four corner products suffice. Let Q(I) enclose the target arc over I with the R71 closed boundary floor construction. Suppose the exact R71 integer-shift exclusion test proves S(C,I) disjoint from Q(I)+Z.

For any new class C' of source identities with the same anchor residue and with ALL new times t in [lo,hi], and any rational closed I' subset of I, the *same old exclusion certificate* proves every source in C' OUT for every real theta in I'. Indeed S(C',I') subset S(C,I) by the rectangle inclusion, while Q(I') subset Q(I) using the unchanged affine boundary floor formulas. Thus all shifted intersections remain empty. In particular (i) arbitrary branch-only updates, (ii) internal-time insertions/deletions, and (iii) deletion of extremal times may reuse an old OUT certificate. The class root object need not be identical. No newly introduced time or interval expansion is admitted beyond its certified envelope; an explicitly checked stronger certificate can of course enlarge the coverage.

Counterexample to unguarded enlargement: theta0=1/4, a=1, b0=2, j=x=0, I=[1/4,31/120]. Source time 0 is always OUT and its singleton R71 envelope passes. Insert time 40 in the same residue class (40 mod 4=0). At theta=31/120, {40 theta}=1/3 lies in [31/120,31/60). The old singleton certificate cannot be reused for the enlarged group.

### Data-structure consequence

Maintain a full identity/branch registry and a separate time-support (or stable time-projection) index. Cache an OUT certificate by anchor phase, query signature, certified time envelope [lo,hi], and certified interval I, not only by immutable identity-root equality. A later group may reuse it if the current times and query interval are contained. Latest-time output may be cached under identical time support; a change in time support needs winner-specific checking even when a group OUT certificate remains reusable. Source GCD/phase/winner trees can continue to be maintained as in R82. This is a precise, extra sound cache-reuse rule; it is not an assertion about unsound branch erasure.

## Executed exact tests

Independent standard-library Fraction checker: 500 constructed random group envelopes under q=16, all 500 certified; 12,000 exact random point probes plus directed cases of interior insertion, branch duplication, endpoint deletion, new winning time 5, and expansion counterexample time 40. All assertions passed. The universal validity derives from Theorems A and B, not finite probes.

For a separate matched partial end-to-end experiment, the *full R82 local persistent time-GCD / phase-class / winner AVL source* was used in a local comparator, alongside a lazy-heap variant retaining the exact same time-GCD and phase trees but omitting the eager winner tree. Each case reconstructs an entire index by source updates, retains all version roots to count identity-distinct dataclass nodes, and performs R71 exact whole-interval group tests. Six R83-refined certified families: 32/128/512 phase classes, either highest-time EARLY_WINNER or ALL_EXCLUDED; five independent complete builds per case, seven queries per build. Summary figures are medians in nanoseconds; compare within this single CPython implementation.

| g | scenario | lazy build | eager build | lazy query | eager query | extra retained nodes |
|---:|---|---:|---:|---:|---:|---:|
| 32 | EARLY_WINNER | 567027 | 764125 | 49445 | 45249 | 168 |
| 32 | ALL_EXCLUDED | 517482 | 705105 | 1073282 | 1127815 | 161 |
| 128 | EARLY_WINNER | 3251014 | 4691120 | 79681 | 49514 | 906 |
| 128 | ALL_EXCLUDED | 2964811 | 3867195 | 3839513 | 4478388 | 897 |
| 512 | EARLY_WINNER | 15273716 | 20733078 | 205391 | 50637 | 4620 |
| 512 | ALL_EXCLUDED | 14893812 | 19476348 | 15721913 | 18664622 | 4609 |

Using the medians as *illustrative fixed-cost estimates*, at g=512 EARLY_WINNER the extra build cost 5,459,362 ns and per-query saving 154,754 ns cross after approximately 36 queries. For g=512 ALL_EXCLUDED, the lazy method won both build and query in this run. These measured finite examples refine R83's frontier-only test because both variants pay for Source time-GCD and phase-tree maintenance. They do not cover arbitrary CHANGES witness recovery, multiple distinct times in one phase group, complete arbitrary-precision bit-cost accounting, bytes of historical memory, or a native BRC computation. CPython runtimes and cache/GC effects are not a universal asymptotic theorem.

## R85 frontiers

(1) Implement envelope-containment cache in the full R82 dynamic index and measure cache hits when internal times and branch multiplicity change while certified extrema shrink. (2) Extend equal-output benchmark to full piecewise CHANGES witnesses and broad/narrow exact interval cases with explicit integer-bit counters and historical byte memory. (3) Test observer changes, original-label crossings and certificate recertification under strict query signatures. Preserve source identity and P000/native-type boundaries.

No shared task CLAIM, formal Result, independent mathematical Review or Foundation promotion is inferred from this author-side source.