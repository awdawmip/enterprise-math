# X6 R34 — Global Markov quotient versus one-fiber hidden-history compression

Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_CHECK_PASS / NOT_REVIEWED  
Date: 2026-11-20 (Asia/Shanghai)  
Task: RS-X6-NATIVE-TIME-DYNAMICS; researcher EM-X6-214D9C; original session MCP-d467c19ce42d4d7fa65a3901db1cf6b2.  
Frozen science: P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.  
Immediate input: R33 feedback-sensitive pair-product Boolean-BRC quotient at 4ce40e8b47cfd564fd6e15bb04ea452abd2593ac.

## Proposition: globally minimal full-future Markov state

Let Q be a finite reachable set of *complete decorated states* (θ,s), each with a deterministic partial transition T(q,a) for every fully named ordered source/Port event label a∈Σ. Let L(q) be the set of all successful finite event words from q. Define q~q' precisely when L(q)=L(q'). Then the quotient Q/~ is a well-defined deterministic partial labelled transition system: the label a is enabled at [q] iff it is enabled at q, and if enabled, [q] --a--> [T(q,a)]. It is the coarsest (minimum-number-of-states) deterministic quotient preserving all successful future languages from **every** reachable state.

**Proof.** The one-letter word a belongs to L(q) iff T(q,a) is defined; therefore equivalent states agree on enabled labels. When a is enabled, the suffix residual of L(q) after a is exactly L(T(q,a)). Equivalent states have equal suffix residuals, so their a-successors are equivalent. This proves transition congruence. Any quotient preserving exact future languages must separate unequal languages, so it has at least one state per equivalence class. The construction attains that lower bound. QED.

This is the standard labelled residual-language/Myhill–Nerode argument applied to preserved provenance-bearing X6 conditional event states. It is not offered as a new general automata theorem. A fixed-horizon initial-history quotient and a global ungraded Markov quotient answer different questions: the latter includes all reachable phases, Link flags and post-event states, rather than reusing an initial-fiber encoder after arbitrary transitions. If instantaneous public-state values are independently observed, encode that readout in the observation before quotienting.

## Exact feedback model separation

Reuse R33's two-source probe→Link feedback automaton: hidden θ0,θ1; initial Link x0=0,x1=1; Q0 succeeds iff θ0 and resets x1=0; Q1 succeeds iff θ1 or x1; each probe is one-use. Fully named event labels remain distinct. From the four possible hidden histories and common initial public state, there are **three** future-language classes, requiring 2 fixed bits if one stores only which initial history language is present.

However the union of states reachable after *any* allowed word from those four starting states has **12** decorated (θ,s) pairs. Their infinite-future successful-word languages are exactly the following five distinct sets (ε is the empty word):

1. {ε}
2. {ε,Q0}
3. {ε,Q1}
4. {ε,Q0,Q1,Q1Q0}
5. {ε,Q0,Q1,Q0Q1,Q1Q0}

They define **five** globally minimal Markov states, with optimal fixed-length state index \(\lceil\log_2 5\rceil=3\) bits under the stipulated labels-only observer, versus 2 bits for the initial hidden-history fiber. All words have length at most two in this construction, so the classification is exhaustive, not merely truncated-horizon agreement. Source/probe identity and order remain encoded; a state count is not an argument for erasing any physical provenance before verifying the observer map.

The distinct state lower bound is immediate from the five unequal languages. The corresponding quotient transitions are well-defined by the proposition. Thus this example directly distinguishes a historical-information compression statement from an actual minimal Markov state for the whole future dynamics.

## Exact check and next frontier

The runnable R34 verifier imports the already saved R33 exact automaton, enumerates the complete reachability closure of all four initial histories, computes literal successful-word signatures through depth 12, checks the five distinct signatures and explicitly verifies right congruence of all representatives under Q0/Q1. It records the 12 decorated states and their five fibers in JSON.

Next: repeat this exact *global-state* quotient for candidate native TRIADIC_CLOSURE_E transition signatures only after proving event-admission and observer-label equivalence. Preserve six-axis Cell identity, ordered Port/source/Link and branch provenance, and separate physical event index from periodic phase and precision-refinement coordinates. P000 remains unchanged; there is no native-event admission or independent Review from this conditional result.