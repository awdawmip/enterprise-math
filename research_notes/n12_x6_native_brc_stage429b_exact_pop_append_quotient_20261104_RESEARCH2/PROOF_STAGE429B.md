# Stage429-B — Exact future quotient for one Q POP and one Q APPEND

2026-11-04 | Research2 | Author-side mathematical proof, unreviewed and not admitted.
Scientific parent: Stage428-B at `eb807b7440cc78a9380f5f3ee97f84e2038c04b0`.
Frozen scientific inputs: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral norms were separately read from current canonical main. No alteration to P000, active six-dimensional worldview or proof admission.

## Typed problem and exact future language

Let D={+E1,-E1,...,+E6,-E6} (12 distinct typed native directions), and let P,Q be ordered native X6 direction words. Let m=|P|, n=|Q| satisfy n>=2 and m-n>=3. The complete current observer is

O(P,Q)=(m,n, endpoint_X6(P),endpoint_X6(Q), J_P, J_Q, K(P,Q)),

where J_s(u,v) counts every *directed* adjacent pair u->v in source s, and K(P,Q)=sum_{i=1}^{min(m,n)} 1[P_i=Q_i] uses 1-based absolute indices. Operation legality and subsequent complete observers are part of the observation stream. This is a chart-relative discrete path observer, not a final Cell-address codec or a physical heartbeat law.

P is frozen. Q may perform at most one independent APPEND(x) (x arbitrary in D) and at most one independent POP (removes last letter), in either order; empty operation and partial sequences are allowed. This explicitly includes APPEND(x) followed by POP and POP followed by APPEND(x). No CANCEL or P edit is in this declared language.

Define the four-symbol *boundary tuple*
T(P,Q)=(Q_(n-1),Q_n,P_n,P_(n+1)).

## Theorem 429.1 — Exact relative future equivalence

For ANY two valid starting pairs (P,Q), (P',Q') with the *same complete observer O*, the following are equivalent:

1. Every legal future operation word in the declared budgeted language is executable in both or neither, and produces identical complete observer traces.
2. T(P,Q)=T(P',Q').

Consequently the exact future-equivalence quotient of any fixed initial full-observer fiber is the image of T on that fiber. Its cardinality is the number of distinct attained tuples, not the number of full histories, nor automatically 12^4.

### Sufficiency proof

The current full observer supplies all P endpoint/J data, Q endpoint/J data, K, and lengths. P never changes. For any Q edit, the six-vector endpoint changes by the inserted/removed signed native step. The directed J_Q changes only at the last edge: on APPEND(x), add edge (old last Q,x) if the old word is nonempty; on POP, remove edge (penultimate Q,last Q) if the old word has length >=2. In our budgeted language the original two-letter Q tail together with the newly appended x supplies these edges under BOTH orders, including Q becoming length n-1 after POP. At most one APPEND and one POP occur, so no earlier Q letter is ever required.

For K, the unchanged absolute positions cancel between successive counts. APPEND from original length n adds 1[P_(n+1)=x]; POP from original length n removes 1[P_n=Q_n]; POP then APPEND at index n adds 1[P_n=x]; APPEND then POP removes exactly its freshly added contribution. All needed indexed P values are P_n and P_(n+1). Thus equal initial O and equal T imply equal output O at every step by induction (in fact by the complete operation-word list). Lengths imply equal legality. QED.

### Necessity proof

Assume full initial O is equal and all future observations agree. POP alone changes Q endpoint by -Q_n. Since each of the twelve direction types is a different signed unit X6 vector, equality of the post-POP endpoints forces Q_n=Q'_n. POP also subtracts precisely one entry (Q_(n-1),Q_n) from the full directed J_Q. Equality of both initial and post-POP J_Q therefore forces Q_(n-1)=Q'_(n-1).

APPEND(x) alone for every x in D increases K exactly by 1[P_(n+1)=x] (m>=n+3), hence the full 12-direction APPEND probe family identifies P_(n+1).

To identify P_n, first POP, then APPEND(x) for every x in D. Since post-POP K observations agree and the Q tails already agree, the increments from POP then APPEND identify the function x -> 1[P_n=x], hence P_n. The twelve singleton equality functions are distinct. Thus all four entries of T agree. QED.

**Strength:** this is an exact all-future, all-twelve-direction theorem *within the stated one-APPEND/one-POP language*. It is not a claim for repeated POP, repeated APPEND, two-source edits or arbitrary CANCEL.

## Theorem 429.2 — One extra match bit cannot represent the full quotient

Let A=+E1, B=-E1, C=+E2. Fix Q=C^5 and m=12. For each j in {3,4,5,6} put

P^(j)=A^(j-1) B^2 A^(11-j).

Each P has length 12, exactly ten A and two consecutive B, begins and ends with A, has the same endpoint 8E1, and has the same directed J (J(AA)=8, J(AB)=J(BB)=J(BA)=1). The fixed Q has endpoint 5E2 and J(CC)=4; K(P^(j),Q)=0 for all j. Thus all four pairs lie in one *identical full-observer fiber*, with the same Q original two-label tail.

Nevertheless the pair of future K probes (POP; APPEND(A)) and APPEND(A) returns respectively [P_5=A] and [P_6=A]. As j varies, (P_5,P_6) takes all four values (A,A),(B,A),(B,B),(A,B). The two observations therefore yield four distinct pairs of bits (1,1),(0,1),(0,0),(1,0).

Any deterministic future-sufficient carrier *within this single observer fiber* requires at least four distinct states, hence at least two binary bits in a fixed binary encoding. In particular, a single match bit plus the cached current K cannot be a universally sufficient extra coordinate for this language. This does NOT prove the full native minimum equals two bits in arbitrary fibers; Theorem 429.1 gives the exact attained-tuple partition and is the correct replacement for that conjecture.

## Executed independent finite check

`REPRO_STAGE429B.js` enumerates all native-letter words over the {A,B,C} subset, for n=2,3 and n+3<=m<=6, comparing the full initial O and ALL 38 operation continuations (identity, POP, twelve APPEND(x), twelve POP-then-APPEND(x), twelve APPEND(x)-then-POP) with x ranging over the FULL native 12-symbol alphabet. For every full-observer fiber it establishes both directions of T equality iff identical future signatures. It also independently reconstructs the four-history example and checks all four future K signatures. The exact JSON is the output of the executed JavaScript function; symbolic proof supplies the general/unbounded statements.

This test reuses Stage428's indexed-border K identity (REUSE_APPLIED) and the Stage424 native directed-J/Euler carrier semantics (REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE for Euler transfer coupling in this unit; Stage424 source was read). It does not claim the Stage424 DP was executed here.

## Cost and next frontier

For this fixed operation budget, retaining T adds four direction symbols beyond current O (some may already be derivable from a particular fiber). With random access to P_n and P_(n+1), stepwise updates of K,J,endpoint cost O(1) alphabet comparisons and integer arithmetic per step. Initial extraction from the ordered input requires O(m+n) time without an existing index. The full J arrays have 144 slots per source, and exact counters need O(log(m+n)) bits. State cardinality is *fiber-dependent*; fixed-width symbol storage is not claimed to be the optimal bit encoding of every fiber.

Stage430-B: with Q allowed TWO independent POPs and ONE arbitrary APPEND, determine the exact future tuple/bit-class quotient for gap>=4, including two POP then APPEND and APPEND then two POP, and test whether Q tail of length 3 and P at n-1,n,n+1 are both necessary and sufficient. Separately integrate the indexed-K update into Stage424's Euler transfer and audit the finite-only S(n),T(n) affine counts. No branch publication implies a formal Source CLAIM, Result, independent Driver review or theorem admission.
