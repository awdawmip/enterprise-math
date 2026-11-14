# R762AM — Adaptive observer diagnostics outperform fixed probes in the partial triadic source/frame model

**Status:** Author-derived exact finite conditional result with reproducible Python integer enumeration; **NOT_REVIEWED**, **NOT_NATIVE_ADMITTED**.  
**Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable task publication `TP2-8B7E13C5904A2D6F1142`.  
**Frozen scientific basis:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; P000 and X6 triadic ontology unchanged.  
**Reused:** R762AK `#2414` (eight-state enabled-event counterexample); R762AL `#2418` (four fixed probes; 75-element transformation monoid; ordered BRC observer series).  
**New question:** How many *adaptively chosen, independently resettable* diagnostic future words are necessary to identify the hidden source/frame state, and what is the best event-letter budget?

## AM1. Model and exact observer

Let `E=(0,1,2)`, `c=(1,2,0)`, `t=(1,0,2)` be permutations, with composition `(pq)(i)=p(q(i))`. The live state space is

`R = (C3 × {E}) ∪ ({E} × S3)`, of cardinality eight, and an optional ninth state `⊥` represents an undefined event. Write a state `(s,h)` with `s∈{0,1,2}` representing source cycle `c^s` and `h∈S3` a separate frame value. Actions act as follows:

- `S(s,h)=((s+1) mod 3,h)` if `h=E`;
- `C(s,h)=(s,ch)` if `s=0`;
- `T(s,h)=(s,th)` if `s=0`;
- otherwise the action yields the absorbing failure state `⊥`.

The output `O(s,h)` is the pair of **cycle types** (source E versus C; frame E versus C versus T); `O(⊥)=U`. An experiment consists of choosing a finite word `w` in the alphabet `{S,C,T}`, applying it to a **fresh copy of the same unknown initial state**, and observing the output **at the end of that word only**. The empty word `ε` means reading the initial observer with no event. The next experiment may depend on previous observed outputs, and every experiment requires an independent reset. A fixed nonadaptive design cannot condition its words on observations.

This is a conditional **finite observer/decision-tree model**, not an assertion that native X6 Cell/Link/Port events or physical resets exist.

## AM2. Optimal adaptive identification with a free baseline read

**Theorem AM1.** When the initial output `O(x)` can be observed at zero event cost, the minimum worst-case number of **additional** reset experiments for identifying one of the eight live states is **two**. The bound remains two when `⊥` is also a possible initial state. An optimal policy has worst-case **three action letters** across all experiments, and both quantities are exact lower bounds. On the uniform distribution on the eight live states, this policy has exactly `9/8` expected additional reset experiments and `11/8` expected action letters; these expected costs are also optimal under the declared free-baseline and word-cost interface.

**Constructive policy.** First read the initial output `O(x)` (a word `ε`).

| Initial output | Remaining candidates | Action | Decision |
|---|---|---|---|
| `EE` | singleton `(0,E)` | none | identified |
| `U` | singleton `⊥` (if included) | none | identified |
| `EC` | two distinct frame 3-cycles | probe `C` | terminal output `EC` or `EE` identifies the state |
| `CE` | two nonidentity source cycles at identity frame | probe `S` | terminal output `CE` or `EE` identifies the state |
| `ET` | three distinct frame transpositions | probe `T` | terminal output `EE` identifies one; output `EC` leaves two |
| `ET`, then `T→EC` | two remaining transpositions | probe `CT` on **another reset copy** | terminal output `EE` or `EC` identifies the state |

The baseline partitions the eight live states into fibers of sizes `1,2,3,2` for `EE,EC,ET,CE` respectively. Every tree leaf has a distinct initial state. On the worst `ET` branch the experiments are `ε`, `T`, `CT`: three probes if the empty observation is counted as one, two actual interventions, and `0+1+2=3` action letters. The same initial read separately identifies `⊥` from all live states.

**Lower bound.** The baseline `ET` fiber contains all three transpositions `h` with source identity. Consider **any** single future word `w`, regardless of length. If `w` contains only frame operations `C,T`, its product `g∈S3` sends the three transpositions to either (i) three transpositions when `g` is even, or (ii) one identity and two 3-cycles when `g` is odd. The terminal cycle-type observer therefore has at most **two** outputs on this triple. If `w` contains a first `S`, then, before that `S`, only frame operations were applied; at most one initial transposition has become the identity (namely `g^{-1}` if `g` is a transposition). All other initial transpositions enter `⊥`, and the successful one yields a single terminal output. Again at most two output classes. Hence one additional probe can never identify the three states: **at least two** are required.

For event-letter cost, on the `ET` triple the one-letter words `S,C,T` respectively yield constant `U`, constant `ET`, and a two-class split by `T`. No two one-letter experiments (adaptive or fixed) can distinguish all three; and a single arbitrarily long experiment has at most two outputs by the preceding argument. Thus at least **three** event letters are required on some branch. The displayed policy attains both lower bounds.

For uniform prior, the `EC` and `CE` two-state fibers each require one action-letter probe for each of their two states, contributing four experiments/letters in total. The `ET` triple requires at least one informative initial probe on each of its three states and one further probe on at least two states, contributing at least five experiments. To minimize event letters, the first probe must be `T` (the only informative length-one word); it leaves two states that require a word of length at least two for separation, contributing at least `3·1+2·2=7` event letters. Thus uniform lower totals are `(4+5)/8=9/8` experiments and `(4+7)/8=11/8` letters, achieved by the policy.

## AM3. Adaptive vs nonadaptive optimality and global probe count

**Theorem AM2 (finite exhaustive certificate).** For this exact AK4 system, a policy that must count even an initial empty observation as an experiment needs **three** probes in the worst case, with or without `⊥`. If a baseline read is supplied free, a fixed nonadaptive protocol still needs **four nonempty words** in addition to that baseline; one such optimum is `{S,C,T,CT}`. Hence adaptive choice reduces the worst-case number of *intervening* reset experiments from **4 to 2**, a factor of two, under the same free-baseline interface.

The adaptive claim follows analytically from AM1 (upper bound three including `ε`, and lower bound for any tree with fewer probes can also be checked by complete finite enumeration below). The fixed-protocol lower bound is a finite exact combinatorial calculation over **all possible word transformations**, not an arbitrary word-length cutoff. Starting from the identity transformation and closing under postcomposition by `S,C,T` generates exactly 75 maps on the nine totalized states. Applying the observer gives 43 distinct full-state observation vectors, 19 pair-separation masks on nine states (18 masks when restricted to eight live states), and 19/18 distinct partitions respectively. For every combination of at most three masks, the union with the initial-output mask fails to separate all initial-state pairs. Four masks for `{S,C,T,CT}` suffice. The accompanying verifier executes this full closure, finite cover test and adaptive minimax subset recurrence on both state universes and asserts the expected results.

The adaptive recurrence is exact: for candidate initial-state subset `M`, consider every distinct word-induced partition of `M`. If a word splits `M` into at least two nonempty fibers `M_i`, its worst-case probe depth is `1+max_i D(M_i)`. Minimize this value over all distinct partitions; `D({x})=0`. The finite transformation closure ensures that every possible word is represented. Its result is `D(R)=3`, `D(R∪{⊥})=3`, with an optimal three-event-letter worst-case policy. This is a reproducible finite proof certificate, not an asymptotic or native physics claim.

## AM4. BRC observer scope, limitations and next experiment

An adaptive diagnostic protocol is a *decision tree on ordered, labeled BRC event words and observed outputs*. The policy must retain the branch choices `T→EC→CT` and the fact that each experiment starts from a reset copy. Replacing the words by commutative event-weight totals loses the ordering and may make the identification result invalid; R762AL's `ab` versus `ba` witness remains relevant. The observer quotient is safe only for the precise RESET + terminal-output interface declared here. It is **not** a theorem about a single irreversible trajectory, nor a proof of native `TRIADIC_CLOSURE_E` admissibility.

**Verified:** exact eight-/nine-state complete finite closure, diagnostic signatures, adaptive subset recursion, fixed-mask coverage, and rational cost counts, using Python standard-library exact integers. Analytic parts are proved above; the finite 75-map closure and set-cover bounds are reproducible by the adjacent checker. No stochastic simulation, floating-point fit, external physical calibration, Lean checking or independent Driver review is claimed.

**Next discriminating research unit:** obtain the actual native permitted-event and state-reset interface for V29 PASS/TRANSFER with V17/V39 frame/return transport in a frozen P000 signed-X6 fiber, including enablement and failure observations. Construct an actual reachable transition system, then solve both its fixed and adaptive observer experiments. If physical reset is disallowed, replace the present reset-query model by a single-trajectory information-game model rather than transferring the factor-two saving without evidence. Another useful conditional question is to bound adaptive-query complexity under non-reset experiments or partial/noisy terminal readouts.

**Materials:** `R762AM_ADAPTIVE_DIAGNOSTICS_VERIFY.py` and `R762AM_ADAPTIVE_DIAGNOSTICS_EVIDENCE.json`; no authority claims or protected ontology edits.
