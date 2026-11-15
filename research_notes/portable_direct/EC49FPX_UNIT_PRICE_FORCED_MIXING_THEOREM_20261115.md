# EC49FPX — An exact forced-mixing interval up to equal sensor prices

**Date:** 2026-11-15. **Scientific status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Frozen input:** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, unchanged. Continuation: EC49FPN (PR #2479), EC49FPS (PR #2490), EC49FPT (PR #2494), EC49FPU–FPW (PR #2498).

## Domain and assumptions

The complete native BRC rooted-cost class first represented by configuration 16995 contains 242 original configurations, 112 distinct *named-root* cost states, 324 legal complete-allocation terminal scalar queries (type T, single price t>0), and 96 named-root/optional-demand subset scalar queries (type R, price r>0). The prior is uniform on 242 original configurations; duplicated rooted profiles retain their source multiplicities. The identification target is the **entire named-root cost profile**, with its root, subset and source semantics preserved. All responses are exact integers computed by the frozen native BRC Trie.

Original input SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
Root-cost table SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

Previous exact weighted Bellman evidence proves the pure-root and pure-terminal optima have 841 and 641 configuration-weighted sensor reads, respectively. These are author-verified scientific antecedents and have not undergone independent project mathematical Review. The earlier mixed tree EC49FPT uses (R,T)=(762,44) and is fully replayed.

## New one-query replacement witness

Start with the EC49FPN pure-terminal optimal tree whose first terminal action has index 150. The precise three-response prefix (210,205,205) reaches two named-root profiles with combined source-configuration multiplicity **37**. At this node, terminal action **4** is the final separating test; named-root action **327** gives two distinct responses on the same two profiles. Replace terminal action 4 by named-root action 327 and keep every other internal action and leaf unchanged.

This is still a complete identifying tree. Its configuration-weighted reads are exactly

\[
\boxed{(R,T)=(37,604)}.
\]

Independently rebuilding the native action responses from the frozen source and replaying the modified tree identifies all 112 rooted profiles correctly on **242/242** original configurations. The action indices, the two distinct response fibers, the total mass 37 and the configuration-weighted counts were checked exactly.

## Forced-mixing theorem

**For every positive r,t with**

\[
\boxed{\frac{44}{79}<\frac rt<1},
\]

**every globally minimum-expected-cost adaptive identifying strategy uses both R and T sensors on positive-prior paths.**

**Proof.** Any exact tree with weighted counts (R,T) has expected cost (Rr+Tt)/242. Since the best pure-R and pure-T trees cost 841r/242 and 641t/242, respectively, a mixed tree strictly beats both pure classes iff

\[
\frac{T}{841-R}<\frac rt<\frac{641-T}{R}.
\]

The prior EC49FPT tree (762,44) supplies the interval (44/79,199/254). The new tree (37,604) supplies the interval (604/804,37/37) = (151/201,1). They overlap: 151×254 = 38354 < 39999 = 199×201. Therefore their union is (44/79,1). On each price in this union a valid mixed tree strictly outperforms **all** pure-sensor trees. Any global minimizer must consequently mix sensors. Positive query costs and finitely many possible response partitions ensure that a global minimizer exists after deleting uninformative or repeated-state queries. QED.

The upper endpoint 1 is sharp as an endpoint of the **necessary-mixing** proposition: at r=t the previous EC49FPQ 420-action exact Bellman result shows a pure-terminal strategy attains the unrestricted global minimum 641t/242. For r>t, pure T remains optimal by pathwise cost monotonicity from the equal-cost point. The first global transition above r/t=1/2 is not yet determined.

## Additional scoped theorem: first single-splice threshold

Fix the antecedent EC49FPS optimal pure-R tree (841 weighted R reads). For each reachable internal node and each of all 324 legal T actions, form the T-response fibers and restrict the existing descendant tree to each fiber, deleting constant tests. Exactly 9,747 candidate replacements have a nonzero saving in weighted R reads. Among all these one-node substitutions, the least ratio of introduced weighted T reads to removed weighted R reads is

\[
\boxed{\min_{\text{single splices}}\frac{\Delta T}{-\Delta R}=\frac{44}{79}}.
\]

It is achieved at old-tree response prefix (70,64) by T-action indices 117,119,123,125: 44 new weighted T reads replace 79 weighted R reads. The complete finite search examines every candidate in the defined neighborhood using exact integer response partitions and rational comparisons. **This is a sharp result for that specified local transformation family, not an assertion that the unrestricted global first breakpoint is 44/79.**

## Verification, sources and open work

The full immutable-rooted-cost certificate and proof inputs are retained in the EC49FPX evidence archive: original master, root-cost CSV, EC49FPN pure-T and EC49FPS pure-R trees, EC49FPT mixed tree, new complete 112-leaf tree, both executed Python programs, the builder log, the separate independent raw-data replay log and file checksums. The local builder output was:

\`EC49FPX_PASS R 37 T 604 MASS 37 OLDQ 4 NEWQ 327 SINGLE_SPLICE_CANDIDATES 9747 BEST 44/79\`

The independent raw-data check reported:

\`EC49FPX_INDEPENDENT_242_CONFIGURATION_REPLAY_PASS root 37 terminal 604 changed_mass 37 changed_profiles 2 interval 151/201 1\`.

The sensor-cost analysis does not generate any new physical-time dynamics, classical rotation approximation, or new non-BRC model input. P000 and the ACTIVE worldview remain unchanged.

Next scientific unit: determine whether some **globally** optimal mixed strategy beats pure-R at any price 1/2 < r/t ≤ 44/79; compute the unrestricted 420-action Bellman optimum at r/t=3/5 and obtain exact rational breakpoints.

**Control:** Research-console observation 2026-11-15T11:36:25Z, request emr4-ec49fpx-owner-20261115-1931-v1: RS-EC49AS has NO_CANONICAL_PUBLICATION_DIRECTORY, Source d2abe977942b39693219535bde40d6265e1a2744. This note is an independent portable research artifact; no formal CLAIM, Result, Review or owner takeover is asserted.