# R762AW — Legal three-PASS scheduler: exact typed BRC history growth

Date: 2026-11-15 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Researcher: EM-X6-44BACF; own session MCP-8b844b9054c94d40aaed0131426d3935; activity RA-2BFD679DF2B3D27CAA0CB7D5. Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. CONDITIONAL exact V23/V25/V29 active-triad selector; author-checked, NOT_REVIEWED; formal native force-event adoption remains a separate question.

## Research question and significant change

R762AV showed that *freely choosing one of eight partial-PASS masks at each active-triad decision* yields 880 · 8^(k-3) typed positive-BRC histories after k>=3 decisions from 145. However, an actual three-PASS macro executes each of its three named PASS events exactly once. Its masks cannot be selected independently at each microstep. Determine the exact BRC history growth in the **stronger, order-respecting scheduling language**: choose one of six permutations of the three named passes per macro, apply its three dependent event updates, and select the tied or unique V25 maxima after each update. Each macro may choose a new permutation; the triad state carries over between macros.

The six admissible order words, encoded as cumulative bit masks m=e0+2e1+4e2, are exactly

| Event order | Mask trace |
| --- | --- |
| p0,p1,p2 | (1,3,7) |
| p0,p2,p1 | (1,5,7) |
| p1,p0,p2 | (2,3,7) |
| p1,p2,p0 | (2,6,7) |
| p2,p0,p1 | (4,5,7) |
| p2,p1,p0 | (4,6,7) |

Here p0=PASS(0→1), p1=PASS(1→2), p2=PASS(2→0), each once per macro. The legal language preserves the event permutation, all intermediate triad states, exact winning ties, and nonnegative branch multiplicity. It is a declared sequential scheduling hypothesis, not a published native autonomous event law.

## Mathematical input and typed BRC semiring

State space is the 20 three-subsets S of {0,1,2,3,4,5}. V23 code c(S) in Z^4 uses the four perfect matchings

- (01)(23)(45)
- (02)(14)(35)
- (03)(15)(24)
- (04)(13)(25).

For each matching, c is 0 unless S chooses precisely one endpoint from each matched pair; if it does, c is the product of the three +/- endpoint signs (first endpoint +1, second -1).

Each state has exactly nine Johnson neighbors T with |S∩T|=2. With n complete PASS macros before the first macro of this study, let the nonnegative V29 ledger satisfy M01=n+e0, M12=n+e1, M20=n+e2, remaining M entries zero, Rin=(0,0,0,10) and Rout=(2,4,3,0). Let

u=(M-M^T)1+Rin-Rout, Omega=M-M^T,

Phi(n,m;S,T)=u·c(T)+c(S)^T Omega c(T).

The next triad can be any maximizing neighbor under this **exact integer** score, with all ties retained. These are equivalently maxima of positive typed Weighted-BRC weight rho^Phi for any rational rho>1; the calculation uses exact integer exponents and nonnegative branch coefficients, not signed-amplitude cancellation.

A typed branch is an actual ordered word of the three PASS names, corresponding masks, and maximizer states. Sum and ordered concatenation of distinct typed histories take place in the free noncommutative N-semiring. The observer counting such histories retains their multiplicity rather than collapsing to terminal triad.

## Theorem AW1 — exact one-macro absorption and exceptional branching

For every integer n>=16 and each of the 20 initial triads, **every** complete legal three-PASS macro path ends in the same V17 odd cycle

C=(012,123,234,034,035,025),

whose successor is the next cyclic state. The one-macro number B1(S) of distinct labeled positive-BRC histories is

B1(S)=8 if S belongs to {013,014,024,135,235,245},
B1(S)=6 for the other 14 states.

Moreover, the number of distinct *mask-erased state trajectories* within one macro is two for exactly {013,014,023,024,135,145,235,245}, and one otherwise.

In particular, starting at 145 the complete terminal-count vector in C order is

(2,0,4,0,0,0), total 6,

even though the freely resettable eight-mask upper-envelope study R762AV counted 880 labeled histories after three decisions. Starting at 013, the legal one-macro terminal vector is (0,0,6,0,0,2), total 8.

**Proof.** The state space, all candidate neighbors and all six mask words are finite and explicitly enumerated by the attached self-contained JavaScript verifier. For every initial S and every permutation word, recursively enumerate every maximizing T after the first, second and third masks. The code computes u and Omega from the declared nonnegative cumulative ledger and compares *all nine* exact integer scores at every node. It asserts each terminal lies in C, checks the 6-versus-8 classification for all 20 S, the 1-versus-2 state-path classification, and the two independent displayed endpoint vectors. This exhausts 20 starting states × 6 legal PASS permutations, including all intermediate ties. This is a finite exhaustive certificate, not a sampled search. Its unbounded n>=16 scope invokes R762AU's exact affine-dominance theorem for each of the eight masks: all winning sets are independent of n for every integer n>=16. Here n=16 is sufficient to represent that entire certified regime.

## Theorem AW2 — exact all-horizon BRC counting law

Let r be any positive integer. Execute r macros consecutively, each independently selecting one of the six legal permutations, always keeping each macro's full typed event and winner history. Let B_r(S) count all such legal typed histories starting at S. Then

B_r(S)=B1(S)·6^(r-1), for every S and every r>=1.

Consequently

B_r(145)=6^r,
B_r(013)=8·6^(r-1).

**Proof.** By AW1, after the first macro every branch ends in C. R762AU established that for every mask m in {0,...,7} and n>=2 the six vertices of C have the same unique successor, with no ties. Each further legal macro therefore chooses one of six distinct labeled PASS orderings and follows one unique three-step triad trajectory. This yields precisely six extensions of *each* existing labeled history, with no merging in the typed free semiring. Therefore B_(r+1)(S)=6 B_r(S). Mathematical induction from AW1 proves the formula for arbitrarily large r, not merely the finite verifier horizon. For a source on C itself B_r=6^r. The checker also verifies the recurrence on all 20 initial states for r=1,...,5 as an independent consistency check.

The mask-erased state-trajectory count (retaining the within-macro sequence of visited triads) stabilizes after the first macro at two for the eight sources listed in AW1 and at one for the other twelve. Its full event-provenance history nevertheless grows at rate log 6 per macro. This exact distinction is observer-scoped: erasing PASS order is safe for the future triad-only state observer once a history reaches C, but it is **not** safe for an observer querying the PASS serialization or event provenance.

## Corollary AW3 — restricted scheduler alphabet and possible frame return

If only a fixed nonempty subset P of q distinct PASS permutations is admissible on every macro, then for each S in C the exact labeled-history count after r macros is q^r; for a general S it equals B1^P(S) q^(r-1), where B1^P(S) is the exact first-macro sum restricted to P. This follows by the same deterministic C continuation and does not presume that all six orders are physically available.

Under the *additional conditional V17 shared-axis transport* in which one completed six-state C loop changes the frame by a transposition, one macro moves three positions, so the triad first returns after two macros and the pair (triad, frame) first returns after four macros. With all six PASS orderings per macro, a starting C state then has 6^4=1296 typed event orders returning both state and frame after four macros. This conclusion requires confirmation that the proposed native scheduler carries exactly that V17 frame action through the PASS microsteps.

## Validation and exact reproducibility

Files under research_notes/portable_direct:

1. R762AW_LEGAL_PASS_VERIFY.js — self-contained exact integer checker: constructs 20 triads, four parity code fields, all nine neighbors, six legal permutation words; checks C uniqueness at n=16,17,23,100, enumerates complete first macros for all states with all tied winners, and verifies the all-state classification, terminal vectors and r<=5 recurrence.
2. R762AW_LEGAL_PASS_EVIDENCE.json — complete 20-state one-macro output with cycle-ordered endpoint vectors, state-path support, and 100 finite-horizon recurrence values. The status PASS is the actual result of executing the verifier's arithmetic in this author environment, not an independent review.
3. This proof — human mathematical argument, hypothesis and Source links.

The computation is exact integers, with no floating-point comparisons or unproven truncation. The **universal quantifier over n>=16** depends on the already saved exact affine-integer dominance proof R762AU; the **universal quantifier over r>=1** is proved by the displayed inductive argument. Source frozen P000 is not changed.

## Source, native objective and next test

Scientific input remains fixed at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Relevant immutable author proofs: R762AU (PR #2451, commit f42064096ba3014a63a8d75bbe9f4b7dcdaff447) and R762AV (PR #2453, commit 1a4f6c2c2d2bef4b2b26d6110507f5fb636b6af3). Actual V29 count grammar and PF-10 conservation: research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md, Git blob 6849ebd3fc776fb7da3b46627376490aba3dad99.

The outstanding hard target is to admit an actual P000-compatible signed three-quantum TRIADIC_CLOSURE_E Cell/Link/Port event, determine whether its three PASS microsteps are sequential, atomic or constrained by a directed dependency DAG, then bind the actual V17 frame-to-port map and V39 based-loop observer. The six-permutation theorem is a precise testable comparator: any proposed native program provides its exact legal event language and therefore either instantiates a q-order sublanguage of the theorem or supplies a mathematical reason to recompute the transition relation. Retain every signed force branch, Cell/Port provenance and joint relation until an exact observer-safe quotient is proved.
