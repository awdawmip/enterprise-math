# Stage461-B — Exact future quotient with two POPs and one signed APPEND per source

**Date:** 2026-11-06. **Status:** author-side exact derivation; finite executable checks complete; independent mathematical review and native Source Result not claimed.

## Sources and mathematical model

Reuses the Stage460-B theorem (commit 451f48f41df015b29a77faf57ceada2f5bcc0960). Frozen scientific pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Behavioral rules read at current normative context, without repinning science.

Two *source-distinct* original words P and Q, with 2<=m<n, use the binary signed native X6 alphabet A=+E1, B=-E1. Both begin/end A; interior B defects are pairwise nonadjacent. Fix B counts kP,kQ and mismatch count d in their first m slots. Each original history pair carries a distinct weight-1 positive BRC branch; arithmetic is exact nonnegative integers, not signed cancellation.

The full initial and future observation consists of both lengths, six-component signed endpoints, 12x12 directed adjacency counts for each source, and exact positional match count K across their current overlap. A labeled future action may POP either source at most twice (only on nonempty path), APPEND to P at most once with any of all 12 signed X6 directions, and APPEND to Q at most zero or once with any of the same directions. Actions may interleave arbitrarily; APPEND may subsequently be POPped.

## Theorem 461.1: exact iff and unchanged partition after Q APPEND

Using one-based original positions, let IP={m-2,m-1} intersect {1,...,m-1} and IQ={m-1,m,m+1,n-2,n-1} intersect {1,...,n-1}, sorted with repetitions removed. Define R461=((P_i) for i in IP,(Q_j) for j in IQ). Its length is <=7 binary coordinates, and fixed original endpoint A is implicit.

**Claim:** Inside each fixed full initial-observation fiber, two original histories have identical full *labeled* future observation trees if and only if their R461 keys are equal, for BOTH append budgets (rP,rQ)=(1,0) and (1,1). Accordingly, adding the first Q APPEND in the presence of one P APPEND does not change the equivalence partition or any BRC class population under these hypotheses.

**Sufficiency:** After at most two POPs and at most one APPEND on each source, each current word is a surviving original prefix (at least m-2 original P positions, at least n-2 original Q positions) with at most one known appended action letter; a letter appended earlier may be removed. The two original signed endpoints update using the deleted original terminal directions and appended action letters; every original deleted direction needed lies in the indexed P/Q terminal tails or is the fixed A endpoint. The directed adjacency updates delete/add a pair whose original predecessor is likewise among those original terminal coordinates; action-selected letters are known. In the positional match observable, comparisons of surviving original-original positions <=m-2 are included in initial K and remain unchanged. Original-original comparisons changed in positions m-1 and m are computable from the indexed directions and fixed P_m=A. The sole P APPEND can probe at most Q_{m+1}; if preceded by P POPs it instead probes Q_m or Q_{m-1}. All these original Q values are in the key or fixed endpoints. Q APPEND (if available) can occupy index no smaller than n-1>=m; any new comparison with an original P letter is at position m, where original P_m=A; a P appended letter, if present, is action-known. Appended-appended comparison is also action-known. Thus the entire observation after any labeled legal action prefix is a function of initial observation, R461, and the prefix; legal-next-action sets depend only on budget and current lengths. Induction on remaining operations proves equality of the complete labeled future trees.

**Necessity:** The no-APPEND future subtree is present under both budgets and, by Stage460-B's POP-grid edge-deletion/match recovery, determines all nonconstant original coordinates from the old repair set: P_{m-2},P_{m-1},Q_{m-1},Q_m,Q_{n-2},Q_{n-1}. The new direction Q_{m+1} is obtained by executing APPEND_P(A) immediately at the root: n>=m+1 guarantees that the positional match change is K_new-K_old = [Q_{m+1}=A]. For binary A/B that determines Q_{m+1} exactly. Coincident or fixed endpoints add no information. The full future tree therefore determines the entire R461 key. QED.

The exact iff is *within this specific binary isolated-defect model*, not arbitrary initial direction alphabets, variable budgets, heartbeat time, or full X6 rotations.

## Independent strict witness: old Stage460 repair loses information

m=3,n=9, P=AAA, Q1=AAABAAAAA, Q2=AAAAABAAA. Both Q words contain a single isolated B, have the same endpoint and complete directed adjacency histogram; initial positional K=3; all old Stage460 coordinates P_1,P_2,Q_2,Q_3,Q_7,Q_8 equal A. But Q1_4=B whereas Q2_4=A. Execute APPEND_P(A): K becomes 3 and 4 respectively. Thus the additional Q_{m+1} coordinate is truly required in general.

## Theorem 461.2: positive BRC population and rank

A source-ordered integer transfer over original positions 1..n tracks (a,b,h,lastP,lastQ), with a and b the B defect counts, h original mismatch count, and previous letters to forbid adjacent B. Enforce first/last A and each specified key bit. Terminal count at (a,b,h)=(kP,kQ,d) equals the *exact source-distinct BRC mass* M(w) of every complete repair key w: each original history pair yields exactly one accepted transfer path, and conversely.

For a key prefix u define S(u)=(q(u),mass(u)) recursively by summing the two children, with complete-key leaf (1,M(u)) for positive M and (0,0) otherwise. Then q_F=q(empty), |F|=mass(empty). Lexicographic rank adds q(u0) when the next letter is 1; unrank uses q(u0) to choose a child. No raw-history list or supported-class roster is needed. At most 2^7=128 complete candidate leaves and 255 cached support-tree nodes suffice; one leaf DP takes O(n(kP+1)(kQ+1)(d+1)) arbitrary-precision integer operations. Every count has O(m+n) bits since |F|<=2^(m+n). After support-tree construction a single rank/unrank takes O(s), s<=7. This is a fixed-budget polynomial result and does **not** assert polynomiality when action budgets grow with n.

## Actually executed checks and exact numbers

The Python standard-library file STAGE461B.py independently enumerates eligible original pairs for small instances; builds a **complete** labeled future operation tree with every legal POP/APPEND interleaving and all 12 signed letters, using 6-dimensional integer endpoints, full directed edges and exact K at each node; interns trees by full observation and child-identity tuples rather than probabilistic signatures; and compares grouped positive-integer populations and rank/unrank against independent enumeration.

22 small configurations from m=2,n=3 through m=6,n=7 passed, including POP to empty, n=m+1 and both rQ=0,1: 226 initial fibers, 616 original source pairs, 514 supported-class population/rank checks, 1302 within-fiber history pair comparisons, and 389116 memoized future states. Full case results in STAGE461B_EXECUTED.json. Large integer DP without enumerating source histories: (8,10,2,2,1) gives q=4, |F|=20; (64,80,15,17,1) gives q=34, |F|=5061384194832966 (Stage460-B no-APPEND baseline q=21); (92,126,20,25,3) gives q=45, |F|=1121449082621221549433213976. First/middle/last ranks invert correctly. General theorem follows from the proof, not finite-test extrapolation. No native Source Result or independent Driver acceptance is claimed.

## Next Stage462-B

Increase P APPEND budget to 2, initially Q APPEND budget 0 then 1. Determine whether Q_{m+2} and further original-vs-new-letter boundary data must be retained; find earliest strict witness, prove or repair a future-sufficient key and implement count/rank with variable key size and explicit integer bit costs. Preserve source identity, the frozen pins and actual authorization boundaries.
