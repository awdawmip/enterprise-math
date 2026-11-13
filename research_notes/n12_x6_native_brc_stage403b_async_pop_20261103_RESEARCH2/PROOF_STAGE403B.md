# Stage403-B — exact sharp asynchronous boundary-memory window (native X6 Path-formal BRC)

Date: 2026-11-03. Parent: Stage402-B, author-proof commit `fadd86d363d80b58695843cf61ed7801cfe4c0d0`, Draft PR #1736. Researcher2 author-side computation and mathematical proof; UNREVIEWED / NOT_ADMITTED.

**Scientific inputs remain frozen:** Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; global scientific snapshot `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; original P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current control/rules read independently from 2026-11-03 global main `35f175fd8004bcd3e337478f346124e3dcf1ed22`, Enterprise Math main `cbbbbff41de9a9117869a88e423aac2e750074f8`. Original P000 is a fixed task scientific input, not replaced by the current P000 blob. The P000 12 signed native directions and source identity/order are retained.

## Exact new operation language and observer

Native signed alphabet `A_native={+E1,-E1,...,+E6,-E6}` with formal inverse `a -> -a`. Two initially aligned finite path words P,Q have common length m. Future operations are arbitrary paired `APPEND(a,b)` (append a to P and b to Q, including after desynchronization), at most one `POP_Q` (remove Q's last symbol when Q nonempty), and at most C paired `CANCEL` actions (remove the last two symbols from both histories, enabled iff both terminal pairs are inverse in their respective sources). The two paths may have different lengths after POP_Q. Budgets are cumulative, not reset by APPEND.

After every operation observe the ordered pair of lengths, six-axis displacements z_P,z_Q, the complete separate directed adjacency histograms J_P,J_Q, the 20 native triple-coordinate readouts of each displacement, exact native unweighted BRC endpoint masses N_{mP}(z_P),N_{mQ}(z_Q), and the absolute-index synchronous coincidence

```
K(P,Q) = sum_{i=1}^{min(|P|,|Q|)} 1[P_i = Q_i].
```

When specified, fixed nonzero per-direction multiplicative signed traces and positive rational weighted BRC endpoint masses are functions of the labeled counts/endpoints, respectively; they are not conflated with each other. Enabledness of POP_Q and CANCEL is observable. Path operations here are formal, not asserted to be physical time reversal or Cell-level dynamics.

## Theorem 403.1 — sufficient finite history for asynchronous continuation

**For every C>=0, every finite initial pair length m and all finite legal future operation words in this language:** if two initial pairs share all current observations and share their aligned last `L=min(m,2C+2)` paired symbols (the entire pair if m<L), then every identical legal future action yields equal observations and enabledness. Thus a uniform paired-history suffix window of length `2C+2` is sufficient, even when APPEND and CANCEL are interleaved arbitrarily before or after POP_Q.

**Proof.** Mark an initial cut before the last L pairs; for each marginal, the initial full J is the sum of (i) known edges wholly inside the last L original positions and (ii) the complementary aggregate of prefix-internal edges **together with the possibly unknown prefix-to-tail boundary edge**. That complementary aggregate is equal between histories, although the boundary edge need not agree individually. At most L-1 original Q symbols and at most L-2 original P symbols can ever be removed, so the first original tail symbol and its incoming boundary edge always remain. All removed edges therefore have two known labels. Initial displacement, letter multiplicities and K likewise split into equal hidden-prefix aggregates and known suffix contributions. Both continuations may be viewed as an unchanged hidden prefix followed by explicit known suffix stacks with future appended symbols. Because there is at most one Q-only POP and C paired CANCELs, the number of removed *original* symbols is at most 2C in P and 2C+1 in Q. Consequently the symbol immediately preceding every removed Q adjacency edge is still in the original last 2C+2 positions, and analogously for P. The initial hidden prefix never changes. Future APPEND creates fully known labels; any removal of appended labels is tracked by the explicit suffix stack. Every adjacency update uses the known departing/arriving boundary labels; all changes in six-axis coordinates and integer BRC length/endpoint observers are determined by known deleted/appended labels. K compares equal absolute indices; the contribution at unchanged hidden indices is fixed and equal, and every newly exposed/lost matching position has labels in the known stacks. Cancellation enabledness uses the last two known symbols in each source. Induction on future operations preserves the equal observer, remaining budgets and all future enabledness. If m<L, the whole initial history is retained and the statement is immediate. QED.

This theorem proves one *uniform suffix representation* is sufficient. The smaller exact minimal quotient of an individual observation fiber may merge further states.

## Theorem 403.2 — sharpness of the window, with K=1

**For every integer C>=0**, the window `2C+1` is insufficient in general even with the full individual J, z, exact native BRC and nonzero K, while Theorem 403.1 supplies `2C+2`. Thus `2C+2` is the sharp **uniform paired-suffix window** for this operation language.

Take A=+E1, B=-E1, T=+E3, with A and B formal inverses and T a distinct native direction. Let `U_C=(AB)^C A` (length 2C+1), and define words of common length m=2C+4:

```
P       = T T T A (AB)^C
Q_first = A A B U_C
Q_second= A B A U_C
```

Both Q words have the same marginal directed adjacency histogram because, with the shared tail beginning at A, the first three transitions of each `Q` consist of the same unlabeled multiset `{AA,AB,BA}`, in different order. They have the same signed-letter counts/endpoints, and the P word is identical. Across the pair, the first three positions never coincide (P has T, Q has A/B); at position four P=A=Q; and at all remaining positions P and Q have opposite A/B labels. Hence K=1 for both current pairs. All endpoint-dependent native BRC masses, all 20 triple readouts, per-direction signed traces and other stated current observers agree. The last 2C+1 paired letters are identical.

Apply `POP_Q`, then `C` paired `CANCEL` actions. These are legal because the remaining Q suffix and the P suffix are each `(AB)^C`. The resulting two states have P=`TTTA` and respectively Q=`AAB` or Q=`ABA`. Endpoints and K still match, but Q's directed adjacency differs:

```
J_Q(AAB) = {AA:1, AB:1};
J_Q(ABA) = {AB:1, BA:1}.
```

The future observation distinguishes the initial states. This proves the lower bound for every C, including C=0 (the distinguishing word is just POP_Q). QED.

**Minimal witness length within the equal-(2C+1)-suffix / equal-J construction:** m=2C+4 is first possible. If m<=2C+3, at most two symbols precede the known suffix; the leftover adjacency edge multiset is a directed walk of at most two edges with a known terminal vertex (first suffix symbol), which determines the ordered prefix uniquely. No distinct Q words with those equal data exist. This is a fixed-suffix structural minimality statement, not a claim about all possible different-suffix G_C equivalences.

For C=2 the exact witness is P=`CCCAABAB`, Q_first=`AABABABA`, Q_second=`ABAABABA`, where C denotes +E3 in these literal examples. Initially zP=(1,0,3,0,0,0), zQ=(2,0,0,0,0,0), K=1 and J_Q={AA:1,AB:3,BA:3}. The 12-direction integer BRC recurrence gives N8(zP)=68768 and N8(zQ)=385056. After the Q-only POP and two cancels the remaining Q words are AAB and ABA; the same current Stage401 G_2 signature (which only requires a suffix no longer than five pairs) did not preserve this enlarged future language.

## Exact computation and verification range

`REPRO_STAGE403B_ASYNC_BOUNDARY.js` uses only exact integers / BigInt; it executes C=0..6 witness assertions and independent full native twelve-direction BRC counts at n=8. It checks 254 binary Q words (length 1..7) grouped by endpoint, adjacency and last-five labels to crosscheck the C=2 fixed-suffix minimality. The executed stdout is included verbatim. Generality for every C and arbitrary finite future operations follows from the two written proofs, not from finite testing. No native Source authority, mathematical review or physical-heartbeat simulation is claimed.

## Stage404-B question

Construct a *symbolic* coupled Euler-histogram transfer that computes distributions of minimal asynchronous future-observation equivalence classes, rather than only a sharp uniform window. Use a 2C+2 tail-state, Q-only POP budget and shifted K observer, recover the Stage402 2C+1 transfer when the Q-only POP capability is absent; characterize which individual observation fibers admit further quotient savings. Account for the cost of the complete J-to-prefix transducer, output bit lengths, and signed/positive BRC carrier separation.
