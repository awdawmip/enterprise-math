# Stage454-B — Exact signed-X6 POP observer quotient and ternary obstruction
Date: 2026-11-05. Classification: AUTHOR_SIDE_PROOF / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Provenance and scientific scope
Stage453-B frozen science: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Stage453 proof commit `7b8227a64ecd9c88a5ac4877a1b5aa7bccb9f948`. Current normative inputs separately read from canonical main (2026-11-05). No ontology or Foundation mutation.

Let the initial ordered native X6 source words `P,Q` have lengths `1<=m<n`, letters in a finite subset `S` of the 12 signed unit directions, and their **terminal P letter fixed by the model** at `P_m=A`. The observer is `O=(m,n,V(P),V(Q),J(P),J(Q),K(P,Q))`, with native signed six-component endpoint `V`, directed 12x12 edge histogram `J`, and positional match count `K`. We condition on an entire initial O-fiber, retaining source-distinct history-pair multiplicity.

Only P may perform labeled `POP` (at most p) and `APPEND(z)` (at most r) with all 12 native directions z; Q remains unchanged. Operations may be interleaved legally, including deleting appended letters. Compare the full observer after **each prefix** of every legal labeled operation sequence. Set `a=min(p,m)` and use one-based indexing. The notation `P[i:j]` is the ordered indexed subword, with an empty range allowed.

## Theorem 454.1 (exact all-horizon future quotient for a fixed Q)
For any allowed initial finite alphabet S and all p,r>=0, two histories from the same O-fiber have identical complete future observer trees **if and only if** they agree on the following repaired data:

* POP predecessor tail `T=P[max(1,m-a):m-1]` (the fixed P_m=A is implicit).
* If r=0: ordered equality-bit word `E=([P_i=Q_i])_{i=m-a+1}^m`.
* If r>=1: ordered actual Q-direction word `W=Q[m-a+1:min(n,m+r)]`.

If a=0 and r=0, the key is empty.

**Proof of sufficiency.** From initial V,J and T plus fixed P_m, the change in P endpoint and every removed directed edge under any legal trace is reconstructible. Every appended letter and corresponding edge is explicit in the trace. The unchanged original P prefix `P_1...P_{m-a}` makes a constant contribution to K. When r=0, each removal reduces K by exactly its corresponding equality bit in E. When r>=1, the initial contribution of the original suffix and every match involving an appended letter at an index <=n are reconstructible from T, W and the known trace. The fixed prefix contribution is obtained from initial K by subtraction. All Q observer components stay at their initial values. Thus every future O is determined by the repaired data and the initial O.

**Proof of necessity.** Follow the trace of j consecutive POPs for j<=a. Differences of the directed edge histogram J recover each removed edge `(P_{m-j},P_{m-j+1})`; the fixed P_m gives the predecessor letters recursively. When the last original letter is removed from a singleton word, the change of six-component V recovers its signed native direction. Thus T is observable. At each POP, the exact change in K yields E, proving necessity when r=0. For r>=1, for any `i` in W's index range, reach P-length i-1 by `m-i+1` POPs if i<=m, or by `i-m-1` APPENDs if i>m; budgets allow each action. Append a chosen native direction z. The K-increment at that prefix is `[z=Q_i]`. Running the same labeled test separately for each z in S (or all 12 native directions) uniquely identifies Q_i. Therefore all letters of W are observable. This proves the iff claim.

The index range and budgets matter: for r=0, the observer can reveal a **match bit**, not an arbitrary native direction, at each removed position. A binary original alphabet makes the direction recoverable from the bit and known P direction, explaining Stage453-B's binary repair.

## Theorem 454.2 (explicit three-direction strict over-refinement witness)
Take signed native A=+E1, B=+E2, C=+E3, m=5,n=7,p=2,r=0:
`P=AAAAA`, `Q1=ABACAAA`, `Q2=ACABAAA`.
Both Q words begin and end in A, have internally isolated non-A letters, and have the same full signed endpoint (A five times, B once, C once) and directed edges AB,BA,AC,CA,AA,AA once/twice as appropriate. P has the same endpoint and edges; both initial match counts are K=3. The POP-only future K values are [3,2,2] for both. Hence complete future trees coincide. Yet `Q1_4=C` and `Q2_4=B`. The raw-Q-letter key obtained by applying Stage453's binary iff criterion to this ternary fiber distinguishes two future-equivalent histories. The match-bit repair above identifies them as the same class.

This provides a concrete route to a more economical general signed-X6 residual representation, replacing unnecessary raw coordinates with observer-specific equality bits when probing is unavailable.

## Executed evidence
The self-contained `STAGE454B.js` enumerates finite A/B/C initial word families with fixed A endpoints and isolated non-A defects, uses complete six-vector V and 12x12 J, enumerates the full 12-direction APPEND future trees with interleaved POP operations, and compares the theorem key versus exact canonical subtree identifiers on each fixed-O fiber. The identifiers use exact JSON structural interning (no probabilistic hashes). The exact numbers and witness assertions are in `STAGE454B_EXECUTED.json`. The mathematical proof above covers the stated all-horizon P-only operations; executed coverage is the explicitly finite audit.

## BRC residual interpretation
Carrier = ordered, source-distinct `(P,Q)`; observer = full native O along legal labeled future operations; Boolean support = existence of a history in a class; integer population = number of histories in a class. The exact quotient retains P predecessor tail plus E or W according to the probe budget; erased coordinates are preserved as a class population rather than silently identified with a single history. The classification theorem identifies the correct class key, while grouped class-population counting for unrestricted two-source budgets remains an open implementation target.

## Next unit
Stage455-B: (1) build a grouped exact-population transfer for arbitrary two-source POP/APPEND without enumerating all keys (Stage453 C/T/U); (2) generalize the probe/equality-bit quotient to Q POP and signed alphabets of cardinality 3..12; (3) derive polynomial arithmetic, bit and rank/unrank bounds and test actual BRC population consistency.