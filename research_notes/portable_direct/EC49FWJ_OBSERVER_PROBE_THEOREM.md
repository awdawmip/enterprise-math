# EC49FWJ — Uniform versus spectrum-adaptive membership probes on Z/10

Date: 2026-11-22 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
Frozen scientific input: BRC16943 (unchanged).
Immediate parent: EC49FWI, immutable commit 216155b1194e436607e9ba7e3e24a61ca8e53989.
Provenance: continuation of independent portable research, without a current authenticated native Researcher/CLAIM binding. Existing historical authors and Activity records remain unchanged.

## Question and definitions

For a binary support S ⊆ Z/10, let Δ_S(c)=|S △ (c−S)| for all indexed c∈Z/10. Let H(S)=S+5, C(S)=Z/10 \ S. The exact parent classification (EC49FWI) states that the complete indexed defect spectrum has fiber {S,H(S),C(S),CH(S)}, with coincident elements identified. The parent supplies a complete 1024-word integer certificate for the reverse inclusion. We use the theorem at precisely that ten-cycle scope.

A membership probe at j reports the bit 1_S(j). A **fixed observer** uses the same position set Q regardless of the observed Δ. A **spectrum-adaptive observer** may choose its positions from the known Δ fiber, before learning membership bits. The question is the smallest number of probes that makes (Δ,probe answers) injective on the declared word domain, either when |S| is supplied or not.

## Theorem A — Universal fixed probe positions: exactly five

For the domain of all 1024 ten-bit supports, both with Δ alone and with (Δ,|S|), a fixed Q distinguishes every pair in every observation fiber if and only if

    Q ∩ {j,j+5} ≠ ∅ for each j=0,1,2,3,4.

Thus the optimum number is 5, and exactly 2^5=32 optimal 5-position choices exist. Q={0,1,2,3,4} is one choice.

**Proof of sufficiency.** Partition positions into five antipodal pairs P_j={j,j+5}. On each pair, S differs from H(S) in both positions if and only if its two bits are unequal. S differs from CH(S) in both positions if and only if its two bits are equal. S differs from C(S) at every position. If Q intersects every P_j, it detects each *nonidentical* one of H(S), CH(S), C(S). By the parent exhaustive classification these are all other candidates sharing Δ. Adding |S| cannot create a new candidate.

**Proof of necessity, even with weight.** Suppose Q avoids P_j. Construct a five-element S whose two bits on P_j are unequal, whose bits on two of the other four antipodal pairs are both 1 and whose remaining two pairs are both 0. Then S≠H(S), |S|=|H(S)|=5, and S△H(S)=P_j. The parent invariance Δ_S=Δ_{H(S)} also follows directly because translating by five sends reflection center c to c+10=c modulo 10. Q observes identical bits on S and H(S); hence Q is insufficient. The construction works for any omitted P_j. Choosing one member of each pair gives precisely 32 minimum sets.

Concrete j=0 witness: S={0,1,2,6,7}, H(S)={1,2,5,6,7}; both weights are 5 and their only differing positions are {0,5}.

## Theorem B — Adaptive versus fixed cost

After Δ has been read, **two probes suffice in every ten-cycle fiber and are sharp** in the worst case, whether |S| is separately available or not.

For a four-element fiber, there is at least one antipodal pair with equal bits and at least one with unequal bits. Probe one position from each type. H changes only the unequal-pair bit, CH changes only the equal-pair bit, and C changes both, giving four distinct two-bit strings. A size-two fiber needs one membership probe at a differing coordinate; a singleton needs zero.

There are genuine four-member fibers even with |S|=5 (e.g. two equal pairs, one with two 1s and one with two 0s, and three unequal pairs); hence one adaptive bit cannot universally distinguish. This is a membership-observation statement, not a claim that changing the site of a physical sensor costs nothing.

## Theorem C — Frozen P10 subfamily: exactly three universal fixed probes

Using the inherited 44-cell four-slope P10 predicate and all 72 primitive mod-10 directions, the Source map yields exactly 50 distinct ten-bit supports. These produce 38 Δ fibers (26 singletons and 12 doubletons), or 40 (Δ,|S|) fibers (30 singletons and 10 doubletons).

Across both observation choices, the complete list of **distinct nonzero pairwise difference supports** inside fibers is

    {0,1,2,3,4,5,6,7,8,9},
    {1,4,6,9}, {2,7}, {3,8},
    {1,2,6,7}, {3,4,8,9}, {2,4,7,9}.

This list is certified by exact finite enumeration of all 72 primitive directions and deduplication to 50 words. Three pairwise-disjoint difference supports, A={1,4,6,9}, B={2,7}, C={3,8}, occur in both the Δ and (Δ,|S|) domains. Every fixed distinguishing observer must hit each of A,B,C, requiring at least three probes. Conversely any Q selecting exactly one site from each of A,B,C intersects every displayed difference set: all the remaining supports contain all of B, all of C, or all ten sites. Consequently:

    minimum fixed probes = 3;
    exactly 4×2×2 = 16 optimal triples;
    an explicit optimum Q = {1,2,3}.

Every frozen fiber has size at most two, so the worst-case adaptive cost is just one bit; this is sharp because doubletons exist.

The theorem concerns recovering one of the **50 support words**, not recovering the originating one of 72 direction labels, a full BRC state, or a moving-Farey height evolution.

## CRT readout consequence

For a known mod-11 factor V, W={(u,v):u∈U,v∈V} under CRT. At any v∈V, a full 110-site membership probe at the unique t satisfying t mod10=j and t mod11=v returns 1_U(j). For the one-hole factor V=Z/11\{0}, choose v=1: sites t=1,12,23 correspond to j=1,2,3 and recover U from (Δ_U, |U|, these three bits) in the frozen P10 family. The parent EC49FWI gives |U| and Δ_U from the full indexed 110-cycle defect spectrum for fixed known one-hole V, so the same three physical site probes reconstruct the ten-cycle factor U at this model scope.

For the complete factor V=Z/11 the full defect spectrum supplies only Δ_U, but the same three probes remain sufficient in the restricted frozen family.

## Verification and exact scope

Companion standard-library Python verifier independently rebuilds the inherited 44-cell P10 predicate, 72 primitive direction words, every ten-center defect, all spectral and weighted fibers, and all fixed probe sets Q⊆Z/10, an exact finite search over 2^10 position sets. It checks all 1024 supports against the parent orbit condition and confirms:
- all-words: 272 Δ fibers, 473 weighted fibers; minimal fixed size 5, exactly 32 minimizers; maximum fiber 4.
- frozen P10: 50 words, 38 / 40 fibers; minimal fixed size 3, exactly 16 minimizers; maximum fiber 2.
- difference-support enumeration and the concrete j=0 necessity witness; direct CRT indices 1,12,23.

The proof of Theorem A is structural once the parent fiber theorem is accepted; Theorem C has a complete finite classification step. No claim here tests a native Farey transition, establishes future-observer sufficiency, changes P000, or admits a Result/Review.

## Next discriminating question

Read the actual frozen moving-Farey update F and downstream observation Y, then check whether the two words within each of the 10 frozen (Δ,|U|) doubletons remain indistinguishable after Y∘F. If a difference is found, determine whether the fixed three-site observer is minimal under that *specific* transition/readout, or whether one targeted adaptive site is sufficient at the desired horizon. This must use the actual frozen F and Y rather than a guessed dynamics.
