# R762AN — Non-reset adaptive observer restores identification when every fixed trajectory fails

**Status:** exact, author-checked theorem for the conditional AK4 finite partial-action model; **NOT_REVIEWED / NOT_NATIVE_ADMITTED**. Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`; frozen P000 scientific source `a72226e2430ffa4786321ac86e7f0c599d5f0389`. This follows R762AM and R762AL, without retesting their research claims.

## AN1. Observer and experiment scope

Use the same eight live states `R=(C3×{E})∪({E}×S3)` with optional absorbing failure `⊥`, enabled labeled transitions `S,C,T`, and cycle-type observer `O`, precisely as specified in R762AM. Unlike R762AM, this experiment **cannot reset** the state. The experimenter may read `O(x_0)` initially, choose one enabled event, read the next output, and select a subsequent event based on all outputs so far. The output is an **ordered observation trace**, not just a terminal value. Actions are applied to the state produced by the preceding action.

## AN2. Sharp adaptive bound and construction

**Theorem AN1.** On the stated model, all eight live initial states (and also the ninth failure state, if included) can be identified along a **single uninterrupted trajectory** after at most two actions. Two actions are necessary in the worst case. With a uniform prior on the eight live states, the minimum expected number of executed actions is exactly `9/8`.

**Policy:** Read the initial cycle-type output. On `EE` or `U`, stop. On `EC`, execute `C`, read the new output and stop. On `CE`, execute `S`, read and stop. On `ET`, execute `T`; its new output `EE` uniquely identifies one frame transposition. If the new output is `EC`, execute `C` **on the current state (without resetting)** and distinguish the remaining two possibilities by its output `EC` versus `EE`.

The baseline fiber sizes on the eight live states are `1,2,3,2` for `EE,EC,ET,CE`. In the two-state fibers, the indicated single event separates both states. For the three-transposition `ET` fiber, after `T`, one input produces `EE`, and the other two produce `EC`; after `TC` the two surviving inputs produce distinct `EC` and `EE`. The concatenated event and observation trace therefore uniquely identifies every initial state. The chosen events are enabled on every state at which the policy uses them: `S` requires identity frame, while `C,T` require identity source.

**Optimality:** An initial `ET` observation leaves three possible states, but every one-letter action has at most two terminal readouts: `S` gives uniform `U`, `C` uniform `ET`, and `T` one `EE` and two `EC`. One action cannot suffice in the worst case. For expected cost, the two `EC` states and the two `CE` states each need at least one action; all three `ET` states need one, and at least two of those need a second action. This gives exactly `(2+2+3+2)/8 = 9/8`, attained by the policy.

## AN3. Impossibility of any single predetermined future word

**Theorem AN2.** No single nonadaptive fixed word in `{S,C,T}*`, of any finite length, can distinguish all eight live states by recording its **full intermediate output trace**, even though adaptive diagnosis succeeds in two actions.

**Proof.** A fixed word is either empty or has first letter. Empty leaves each of the two `CE` states (distinct nonidentity source cycles) indistinguishable, and also each of the two `EC` states (distinct frame 3-cycles) indistinguishable. If the first letter is `S`, both `EC` states have nonidentity frame and are immediately sent to the same absorbing failure state `⊥`. Their initial outputs agree, and all subsequent outputs are the same `U`, forever. If the first letter is `C` or `T`, both `CE` states have nonidentity source and likewise go to `⊥` after the first step. Hence every fixed word irreversibly merges at least one initially indistinguishable pair. No longer word can restore their distinction. QED.

This is stronger than a finite failure search: it rules out **all** lengths by a first-event merge certificate. The checker additionally enumerates every fixed word through length five, and independently verifies the proposed adaptive traces and exact expected action count.

## AN4. Meaning for BRC and native X6 research

This result gives a precise observation-resource hierarchy in one conditional system:

- A terminal-only, independently resettable experiment needs at least two additional adaptive probes, and at worst three event letters (R762AM).
- Allowing non-reset intermediate readouts, the new adaptive observer needs at most **two** event letters in one trajectory (R762AN).
- A fixed event word with no output-dependent branching cannot identify every initial state **at any length** (R762AN).

The gain is due to the **joint event/observation path**, not to a static source or frame marginal, nor to a commutative BRC total. This observation stream must retain the labels, intermediate outcomes, failure semantics and their ordering. It does not assert that P000 native `TRIADIC_CLOSURE_E` supplies such readouts or feedback-enabled actions. A native proof requires an actual signed-X6 Cell/Link/Port event table, V29 PASS/TRANSFER provenance, V17 frame and V39 return couplings, and lawful event-choice/readout interfaces. A physically destructive measurement or an unavailable intermediate observer invalidates the model interface but not the conditional theorem.

**Validation:** Python 3 standard-library exact finite calculation, nine-state trace uniqueness, first-step merge for each event, all **364** fixed words of lengths 0 through 5 (including the empty word), and expectation in integers. The universal nonadaptive statement rests on the analytic proof above, not this bounded check. No formal native Result, independent review, or P000 change is claimed.

**Next:** seek native typed transition/observer evidence; decide whether each event's intermediate output is available, whether events can be chosen adaptively, and whether failure is distinguishable. Then build the original-state identification game over the true reachable state graph, rather than assuming either this auxiliary model or the reset interface.
