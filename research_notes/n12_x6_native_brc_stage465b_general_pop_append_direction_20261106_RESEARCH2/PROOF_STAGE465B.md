# Stage465-B — arbitrary POP horizons: exact Q-APPEND redundancy in binary X6, and a three-direction strict witness

Date: 2026-11-06. Status: author-side proof and finite execution, unreviewed/not admitted. Current registered identity: EM-DIRECT-7338E4; RA-E9AD490EE7A9DE3C0304C3C6. No formal Task CLAIM.
Frozen scientific pins from Stage464-B handoff (not refreshed as normative policy): GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Prior frontier: Stage464-B commit e147402956f08a72ad57d51a792b9a5e04fd71d5. Current rules read from global main@673b1531d66a8b0ca7f3ab19677e28bd83430d76 and project main@dca6a0718b8a6dd922f8e7ac674603aeb485e4de.

## Model and observation

Original source-distinct histories P,Q of lengths 2<=m<n. For the principal theorem, original letters lie in the native signed-X6 two-letter subset {A=+E1,B=-E1}, fixed A endpoints; the original isolated-B restriction of Stage464 is compatible but not needed for the redundancy argument. Future actions are labeled POP_P, POP_Q and APPEND_P(u), APPEND_Q(u), with u ranging over the full 12 signed native directions, action budgets hP,hQ,r,s any nonnegative integers. A POP can delete a previously appended letter. At every intermediate action state the observation consists of both lengths, both exact six-coordinate signed displacements, complete directed 12x12 edge-count matrices, and K=sum_{i<=min(lengths)}[P_i=Q_i]. Only legal action histories are compared, including their intermediate observations.

## Theorem 465.1 (binary original P: Q APPEND never refines the future partition)

Fix one full initial observation fiber. For every hP,hQ,r,s>=0, equality of complete future observation trees with budget (hP,hQ,r,0) is equivalent to equality with budget (hP,hQ,r,s). In particular, this is an *all finite horizons* statement, and it contains no assumption that hQ is small relative to n-m.

Proof. Compare two histories with equal (hP,hQ,r,0) trees and couple any common action prefix in the extended tree. Every original Q letter that has been removed by POP_Q is reconstructible from the observed endpoint/edge difference at its removal (the complete directed adjacency and signed end displacement also handle the singleton-to-empty case). Whenever an original P_j is still present and a POP_Q removes original Q_j from position j, the observed decrement in K reveals the bit [P_j=Q_j]. As P_j is binary, the known Q_j together with this bit identifies P_j exactly. If at the time of that removal P_j is no longer original, it can never reappear as original: any future letter at j is a known appended action label, or j is absent.

Consider an APPEND_Q(u) that produces a comparison at index j with a still-original P_j. It necessarily follows deletion of original Q_j (because j<=m<n), while P_j must have survived throughout; so the same Q_j and equality bit had already been recoverable by the Q-POP-only observation history. Hence P_j, and the new K contribution [P_j=u], are known from the base tree. If the compared P letter is appended, it is action-known. If there is no comparison, K is unchanged. The APPEND_Q edge and endpoint changes are action-known, and subsequent POP_Q of an appended letter is likewise action-known. Inductively erase Q-APPEND actions from the data-dependence proof, reconstructing every extended observation from the base observation tree and the action word. Adding actions can only refine a partition, so sufficiency yields equality. This argument uses exact source-separated observation and never collapses BRC provenance into a total-only weight.

## Proposition 465.2 (alphabet-independent no-new-direction region)

For an arbitrary original signed-X6 alphabet with fixed original P_m=A, Q-APPEND is also redundant whenever hQ <= n-m+hP+1. Indeed, a Q-APPEND at an original P index j must satisfy j>=n-hQ+1. Under the inequality, j>=m-hP; every such original P_j is already recovered by hP P-only POPs from the complete endpoint/edge observer, or is fixed A at j=m. Thus any direction probe targets a previously reconstructible P direction. This sufficient region does not assert a converse for every initial fiber.

The first *potentially genuinely hidden* original P index accessible by Q-APPEND has j <= m-hP-1 and j>=n-hQ+1. Thus the earliest possible budget is hQ>=n-m+hP+2, subject to non-fixed interior index and compatible initial fibers.

## Strict three-symbol signed-X6 counterexample at this boundary

Take A=+E1, B=+E2, C=+E3, m=7, n=9, hP=2, hQ=6, r=0, Q-APPEND allowance s=1:

P1 = A B A C A A A;
P2 = A C A B A A A;
Q  = A A A A A A A A A.

All directions are genuine native signed-X6 directions, not a lower-dimensional native plane. Initial signed six-coordinate endpoints of P1/P2 agree (five A, one B, one C), and directed adjacency counts agree: AA=2 and AB=BA=AC=CA=1. Their initial K agrees (=5), and Q is the same source. Under all legal POP-only action words with at most two P POPs and six Q POPs, the complete observations agree: P's exposed suffix is AA, Q's exposed original letters are A, and both relevant discrepancies at P positions 2 and 4 remain Q-mismatches without direction identity.

But after six Q POPs, Q=A^3, and APPEND_Q(B) yields Q=A A A B. The resulting K values are 2 (P1) and 3 (P2). Therefore adding just one Q-APPEND strictly refines future equivalence. The budget satisfies hQ=n-m+hP+2=6, showing the sufficient-region threshold is sharp in existence, not universally necessary for every fiber.

## BRC carrier and contribution

The future-equivalence classes are a Boolean support partition of a population of source-distinct histories. Each original (P,Q) has positive unit mass. Binary Q-APPEND adds no repair coordinate at *any* POP/APPEND horizon, so existing positive-integer completion counts remain valid with arbitrary s; exact class masses are unchanged. For alphabet >=3, the equality bit [P_j=Q_j] is not an action-complete direction detector; a distinguishing APPEND_Q(u) tests [P_j=u]. Retain the original direction label or the vector of 12 tests for each newly accessible hidden P position before any BRC quotient. This is not a claimed polynomial counting algorithm for arbitrary hP,hQ or multi-symbol populations.

## Reproduction and limits

Companion Python standard-library source recursively enumerates all legal labeled future trees, including all 12 APPEND directions; compare their full observation signatures. Executed finite certificate: 72 tested binary horizon configurations; 108 initial fibers with multiple histories; 234 history-pair equality comparisons; no split on introducing one Q APPEND; three-symbol witness exactly separated by the trace. This finite check supports the hand proof but does not replace its all-horizon quantifiers. The source prints actual observed results, not an expected-output stub.

## Next research unit

Extend the multi-symbol detector to a minimal observation key for arbitrary hP,hQ and arbitrary r,s, with exact population/rank/unrank via a visible-interval BRC transfer; identify uniform hidden-completion fibers when both sources' probe windows grow and overlap. Distinguish symbol identity from match bits and preserve source labels, directed edge counts, original signed six-axis displacement and independent review.
