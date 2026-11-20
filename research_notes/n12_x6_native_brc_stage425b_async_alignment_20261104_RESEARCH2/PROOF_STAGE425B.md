# Stage425-B — Exact asynchronous alignment updates and an unbounded-tail witness

**Date:** 2026-11-04. **Parent:** Stage424-B, commit b35d849007058e064d3dfdd1f19655295df30461, Draft PR #1736. Frozen scientific input: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavior/control read separately at global main 56541d57ab394b9ecb8c5e2cc9e937835b558d4a and EM main bd0f7743c4d1493c2bc944d525dd72aebbd4efc2. **Status:** author proof, finite integer checker executed, UNREVIEWED / NOT_ADMITTED.

## Definitions and observer

Let D be the 12 typed directions (+E1,−E1,...,+E6,−E6) of native X6. Each letter is a signed one-axis increment. Let P=p1...pm, Q=q1...qn be finite ordered direction words, possibly of unequal length. The observer is both six-dimensional chart-relative endpoints, both complete directed-adjacency histograms J of dimension 12×12 and an absolute-position matching count. Source positions are indexed from the beginning of their respective current word, not from its tail. The empty word is admitted only in this auxiliary stack model.

For a **fixed** alignment relation R⊆N_{>0}×N_{>0}, assume its intersection with any finite rectangle is finite. Define

\[
K_R(P,Q)=\sum_{\substack{(i,j)\in R\\i\le m,\ j\le n}}[p_i=q_j].
\]

The Stage424 observer is the diagonal relation R0={(i,i):i≥1}, giving

\[
K_0(P,Q)=\sum_{i=1}^{\min(m,n)}[p_i=q_i].
\]

No physical heartbeat trajectory or native residual attribution is asserted. The theorem uses exact combinatorial comparison of typed X6 path labels.

## Theorem 425.1 — Boundary-pair update under independent append and POP

Suppose one atomic operation either appends any finite suffix on P and/or Q, or removes any finite suffix from P and/or Q; each surviving prefix retains its letters. A POP then APPEND is a composition of two such operations. Write

\[
U=R\cap([1,m]\times[1,n]),\qquad
V=R\cap([1,m']\times[1,n'])
\]

for the old and new valid alignment-pair sets. Then

\[
\boxed{K_R(P',Q')-K_R(P,Q)
=\sum_{(i,j)\in V\setminus U}[p'_i=q'_j]
-\sum_{(i,j)\in U\setminus V}[p_i=q_j].}
\]

**Proof.** In the append case the original words are prefixes of the new words, U⊆V, and the symbols on every pair in U remain equal to their old values. The old contributions cancel. In the deletion case the new words are prefixes of the originals, V⊆U, and all remaining comparisons remain unchanged; only deleted comparison pairs contribute negatively. The formula is exact in either case. Telescoping proves it for an arbitrary finite composition of permitted atomic operations. Each sum is finite by assumption. □

For the diagonal relation set h=min(m,n), h'=min(m',n'). A joint or independent push adds the comparisons indexed by h+1,...,h'; a joint or independent POP removes those indexed by h'+1,...,h. In a synchronous push from **unequal** pre-operation lengths, the newly paired index can match a pre-existing symbol in the longer word, not its newly appended tail. For a synchronous deletion of two labels from both sources, the K decrement may contain zero, one or two paired comparisons depending on the length imbalance.

**Algorithmic corollary.** With indexed typed word stacks, K0 updates cost O(a+b) comparisons for append/deletion affecting at most a P positions and b Q positions. Endpoint and J changes cost O(a+b) native signed-integer operations, updating the removed/added letters and their incident directed-adjacency edges. For general R of maximum incidence Δ per index and enumerable alignment neighbors, the same boundary update costs O(Δ(a+b)); each newly valid/invalid pair is processed once even when both endpoints change. These are update costs for a sufficient implementation carrier with indexed stacks, not a minimal memory or full Euler-DP complexity bound.

## Theorem 425.2 — Arbitrarily long fixed tails cannot preserve future K for unequal-length asynchronous append

**Claim.** For every L≥1 there are two states with identical current P and Q six-coordinate endpoints, full J, K0, first labels, and last L *available* source labels, which yield different K0 after the same legal one-letter independent Q append.

**Construction.** Set A=+E1 and B=−E1. Use

\[
P=AAABA\,A^L,\qquad P'=ABAAA\,A^L,\qquad Q=A.
\]

Both P words start with A, end in A^L, have four plus L copies of A and one B, and have J(AA)=L+2, J(AB)=1, J(BA)=1, with every other directed-edge count zero. Their endpoints in the native six-coordinate chart are identical. The two Q words are identical and current K0 equals 1. After appending A to Q, the new Q is AA. At absolute aligned position 2, P has A and P' has B, so the resulting K0 are respectively 2 and 1. The witness works for every L and satisfies all the stated current-observer equalities. □

This distinguishes the **enlarged** language with unequal initial source lengths and asynchronous Q append. Prior symmetric/equal-length finite-tail sufficiency statements for their own future languages retain their stated scope. The result supplies a concrete structural memory residual: the old P position that the growing Q will next meet.

## Theorem 425.3 — Sufficient absolute alignment frontier

Maintain the two typed indexed word stacks, their J and six-coordinate endpoints, and K0. Independent append/POP and joint append/POP use Theorem425.1 to process exactly the matched positions crossing the shared-prefix boundary. A synchronized inverse-pair CANCEL is a two-letter suffix deletion on both sources, provided its separate inverse-pair legality condition holds. The update is exact for every finite valid operation sequence. The unmatched portion of the longer word must remain retrievable at the indices subsequently reached by the shorter word; an implementation may replace raw words by another structure only with an equivalence proof for its future operations and observer.

**Proof.** At initialization each stored observer is computed from its typed stacks. For each operation the endpoint and J changes follow from adding/removing the explicitly identified edge labels, and K0 follows from Theorem425.1. Induction on the operation sequence establishes maintained observer equality after every operation. □

## Exact executed evidence

The actual Python 3 standard-library program REPRO_STAGE425B.py performs deterministic integer and Boolean operations and independently recomputes both full 12×12 J histograms, both six-coordinate endpoints and K0 after incremental stack updates.

It checks **14,641** pairs of words of length 0..4 over a three-symbol subset of native directions, **263,875** operation instances, including independent/synchronous append, independent/synchronous POP and legal inverse-pair two-label synchronous removal. A further **144** simultaneous native-direction append combinations are included in that instance count. For fixed diagonal, offset and bounded-degree branching relations it checks **85,923** boundary-difference instances, and it verifies **128** explicit witnesses L=1..128. Output status: STAGE425B_ASYNC_ALIGNMENT_EXACT_PASS. The universal theorems above follow from their proofs; finite checks are cross-check evidence. All computation remains typed path-stack combinatorics, with no π, classical trigonometry or physical BRC dynamic simulation.

## Open question

Stage426-B: use a reachable alignment-frontier carrier in an unequal-length directed-Euler/J/K DP; establish sound memoization and input/output/bit costs or furnish an exact smallest counterexample. Separately derive Stage424's measured 68n−463 memo-state and 85n−628 transition formulas from the actual original pruning semantics. Formal Source authority, native CLAIM/Result and independent Driver admission remain separate from this author-side publication.
