# Stage421-B — A third Q POP splits all eight non-singleton two-POP BRC future classes

Date 2026-11-04. Continued from Stage420-B immutable commit b32b9a9c4497b6680fce981877e558047943d24e on Draft PR #1736. Author-side exact counterexample certificate and parametric bounds; INDEPENDENT REVIEW PENDING, NOT ADMITTED.

Frozen science remains GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative rules are read separately. This is the same ordered path observer embedded in native signed-X6, with no changed source premises.

## Question and statement

Continue Stage420's parametric fiber F_n: P_i=A^(i-1) B A^(n-i), Q_(r,s)=A^(r-1) B A^(s-r-1) B A^(n-s) for 2<=r, r+2<=s<=n-1, i in {r,s}; A=+E1, B=-E1 and n>=11. The full observer retains both lengths, each six-component endpoint, both full *directed* adjacency histograms J, joint absolute-position matching K, and the success/failure of every attempted operation.

Let L(p,c) admit arbitrary paired APP(a,b) for all 12-by-12 native signed directions, at most p Q-only POP operations, and at most c paired CANCEL operations deleting the last inverse adjacent pair from *each* source when enabled. Every successful intermediate observation is visible. Define q_(p,c)(F_n) as the exact number of future observational equivalence classes for this observer and action language.

Stage420 proved q_(2,2)(F_n)=16. We now change only p from 2 to 3, keeping c=2 and all observation semantics unchanged.

**Theorem 421.1 (eight strict splits, universal n):** For every n>=11,

q_(3,2)(F_n) >= 24.

For n>=12, a valid safe-suffix construction gives q_(3,2)(F_n)<=44; for n=11 the exact safe-suffix count is 43. In particular, for n>=12:

24 <= q_(3,2)(F_n) <= 44.

This is a sharp *lower-bound construction*, not yet an exact minimal-quotient theorem.

## Eight exact separating histories

Stage417's fixed three-trace test partitions Stage420's two-POP quotient into exactly sixteen classes; the first eight contain more than one distinct original-suffix key and the remaining eight are singletons. For n=11 we choose one pair from **each** of the first eight classes. A history is written (r,s,i), referring to its exact P_i and Q_(r,s) defined above.

Use the trace abbreviations:
p = Q-only POP, x = APP(B,B), y = APP(B,A), c = paired inverse CANCEL.

| Old class | first (r,s,i) | second (r,s,i) | separating legal trace | first differing component |
|---|---|---|---|---|
| 0 | (2,4,2) | (2,6,6) | p p p x c x c | Q directed J |
| 1 | (2,7,2) | (5,7,7) | p p p x c y c | absolute K: 6 vs 5 |
| 2 | (2,8,2) | (6,8,6) | p p p y c x c | Q directed J |
| 3 | (2,8,8) | (6,8,8) | p p p y c x c | Q directed J |
| 4 | (2,9,2) | (6,9,6) | p p p x c x c | Q directed J |
| 5 | (2,9,9) | (5,9,9) | p x c c p p | Q directed J |
| 6 | (2,10,2) | (6,10,6) | p p p x c x c | Q directed J |
| 7 | (2,10,10) | (5,10,10) | p c p p x c | Q directed J |

Every trace uses exactly three Q POPs and two paired CANCELs, with only legal native ±E1 directions. On both histories, every listed operation succeeds, all intermediate O match until the last operation, and the final O differ. The executable attached script constructs the *complete original words*, evaluates all operations, validates legality and confirms first divergence on that final step. Group membership uses the same stable Stage417/420 32-key ordering; the pairs occur in eight different prior classes.

**Proof of the lower bound.** In L(3,2), all old L(2,2) distinguishing traces remain legal. Therefore the sixteen old classes remain mutually distinguishable. The eight displayed additional traces split *each of eight different old classes* into at least two subclasses, yielding at least 16+8=24 classes at n=11. For n>11 prepend A^(n-11) to both original words of each witness. No displayed trace reaches this added common prefix; endpoints and directed adjacency histograms on both sides receive the same prefix contributions, and the absolute K count at every step receives the same (n-11) matching aligned-prefix positions. Thus the same last-step observable differences persist for every n>=11. Distinguishing signatures between different old classes persist by the same argument. This proves Theorem421.1's lower bound for all n>=11. QED.

## Safe upper bound at the changed budget

The general Stage416 sufficient-history theorem under p Q POPs and c paired CANCELs uses original suffix lengths

L_P = max(2c+1, p+2c), L_Q = p+2c+1.

At p=3,c=2 this gives (L_P,L_Q)=(7,8), guaranteeing full O and enabledness conservation for arbitrary finite APP words over all twelve directions. Count the distinct (P-last-7, Q-last-8) keys on F_n. For n>=12:

* Both B's in Q lie earlier than the Q 8-tail: 1 key.
* Only Q's second B is in the tail: s=n-7 contributes 1 key (either P B lies outside the P 7-tail), and s=n-6,...,n-1 contributes 6*2=12 keys.
* Both Q B's appear within the last 8 letters: their positions range over the seven positions n-7,...,n-1 with separation at least 2; there are C(7,2)-6=15 such pairs, and either P-B choice gives a distinct tail => 30 keys.

Therefore there are 1+1+12+30=44 sufficient states for n>=12. At n=11 the first case is absent, leaving 43. This proves the stated upper bounds. No general algorithmic bit-complexity improvement is asserted from these fixed-size state counts.

## Verification, BRC significance, next action

Actual Python standard-library integer/categorical execution, run twice with byte-identical stdout, returns STAGE421B_THIRD_POP_EIGHT_STRICT_SPLITS_PASS. The companion JSON records all eight exact (r,s,i) pairs, traces, first differing observer components, complete first-divergence step and K values. The finite n=11 witnesses plus the algebraic front-padding proof establish the infinite-n lower bound. All APP choices in the **future definition** remain available, although these witnesses use only the permitted ±E1 subset.

For BRC, the third asynchronous removal exposes ordered-history residuals hidden by the sixteen-state two-POP quotient. The previous quotient retains precisely the future information needed for L(2,2), and this new exact falsifier shows why changing the allowed observer language requires revisiting the retained residual. Neither the local model nor its class counts automatically transfers to every P000 process.

Next Stage422-B: identify the true minimal quotient for p=3,c=2, beginning with an exact classification of the 44 safe (7,8) suffix keys, and derive a general minimal-state algorithm from Stage412's remaining-Euler-edge/J/K counts. A further independent review and native Source Result remain separate governance steps.
