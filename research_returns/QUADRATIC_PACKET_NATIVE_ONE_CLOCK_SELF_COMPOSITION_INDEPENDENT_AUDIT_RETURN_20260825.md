# Quadratic Packet Native One-Clock Self-Composition — Independent Audit Return

Status: `FINAL FROZEN / INDEPENDENT RAW PRESERVED / NC3 KILLED AT EXPLANATORY STRENGTH`

Researcher-ID: `EM-QPNCA-4F0348`

Task-ID:

`RS-QUADRATIC-PACKET-NATIVE-ONE-CLOCK-COLLAPSE-BRIDGE-INDEPENDENT-AUDIT`

Hard target:

`NC3_OBSERVABLE_COMPLETE_SELF_COMPOSITION_INDEPENDENTLY_DERIVED_NARROWED_OR_REFUTED_WITH_SEMANTIC_CIRCULARITY_AUDITED`

Final target status:

`ACHIEVED`

Final candidate classification:

`KILL / REJECT AX-QP-OCSC-20260825 AS AN OBSERVABLE-COMPLETENESS CONSEQUENCE`

Exact recommendation:

`REJECT`

A separately named, explicitly stipulated `OBSERVABLE_HEIGHT_2` sector axiom could be considered in a future control-plane task if independent evidence exists for a two-stage capacity law, but that would be a new explicit capacity assumption rather than a derivation or survival of NC3.

## 0. Raw freeze and independence provenance

Mandatory raw return:

`research_returns/QUADRATIC_PACKET_NATIVE_ONE_CLOCK_SELF_COMPOSITION_SEMANTIC_AUDIT_RAW_20260825.md`

Raw freeze commit:

`f85908066b10641bd0cb612188087468dff11bf6`

Raw blob:

`002a06a70d10ce8081d802961ab68f63c8351012`

Frozen primary raw verdict:

`REFUTED`

Frozen-packet mapping:

`REFUTED_BY_ADMISSIBLE_COUNTERMODEL`

The raw artifact was committed before any originating theorem, originating candidate/Phase-B audit, QP-R2 source work, or higher-residual source work was opened. It has not been modified after source comparison.

### Input-pin provenance defect retained

The taskbook/dispatch/current instruction name the blind packet path

`research_inputs/QUADRATIC_PACKET_NATIVE_ONE_CLOCK_SELF_COMPOSITION_SEMANTIC_AUDIT_PACKET_20260825.md`

with claimed blob

`8f5e5a6866bde5381e4d9e4fec4463c8b9753b7c`.

The dispatch also pins frozen input commit

`3383d7c94ac9eb65f8d64e2c74448b5cfb0e9e2a`.

At that exact commit, the unique frozen audit packet is actually

`research_inputs/QUADRATIC_PACKET_OBSERVABLE_COMPLETE_SELF_COMPOSITION_INDEPENDENT_AUDIT_PACKET_20260825.md`

with Git blob

`72c43ee09b81d4d53e75e7e800b5da0f0206e1bc`.

The metadata-named path is absent there and the claimed `8f5e5a...` object is not repository-resolvable through the connected service. No hash equivalence is asserted. The semantic audit used the unique packet actually frozen by the dispatch-pinned commit. This remains a control-plane metadata/provenance defect for later Driver repair; it is not converted into mathematical evidence and does not alter the verdict.

## 1. Exact operational semantics used independently

Let `C=(X,0,c)` be finite deterministic with `c(0)=0`, let `X*=X\{0}`, and let

`R_j = c^j(X*) ∩ X*`.

The task-local sector declarations are:

### One-clock

`|X*\R_1|=1`.

Meaning: exactly one nonzero source state has no nonzero predecessor. This is a source-count condition, not a bound on the number of future-distinguishable states.

### Downward

Every nonzero state reaches `0` after finitely many iterations, with a nontrivial collapse operation. Meaning: finite well-founded termination, not two-step termination.

### Declared future language

Fix an observation map `o:X->A`. Define the complete future trace

`T_o(x)=(o(c^k(x)))_{k>=0}`.

Define `x≡_o y` iff these traces agree and let `q:X->Q=X/≡_o` be the coarsest predictive quotient.

### Primitive

The state language is primitive when `Q` is minimal sufficient for the declared future language: no strict quotient preserves all future predictions together with the induced dynamics.

### Observable state capacity

The capacity is the state/type structure of that minimal predictive quotient. It is determined by the future language. It is not the number of graph sources and is not pre-fixed to two residual stages.

### Self-composition complete

The language is self-composition complete when the same predictive state object supports every repeated application of `c`: there exists `c_bar:Q->Q` such that

`q∘c = c_bar∘q`,

and all declared future observations are generated from iterates of `c_bar` without state refinement.

For full-future equivalence, this factorization is automatic because applying `c` left-shifts the future trace.

### Hidden residual precision

A distinction is hidden if the declared descriptor identifies two states but an allowed future composition distinguishes them. A minimal full-future predictive quotient contains no such omitted distinction.

A residual depth that is itself future-distinguishable and represented by a state of `Q` is a legitimate predictive state, not hidden precision.

These meanings are operational, relabeling-invariant, and do not mention `R_2`, rank, dimension two, dual numbers, or the desired quadratic conclusion.

## 2. Independent structural derivation: S1+S2 give one chain, not depth two

Under S2 the nonzero transition graph is finite and acyclic toward `0`, with every nonzero state having one outgoing edge.

If some nonzero state had two distinct nonzero predecessors, following those predecessor branches backward must terminate at two distinct nonzero source states, contradicting S1. Hence every nonzero state has at most one nonzero predecessor.

Every nonzero state must trace backward to a source; S1 makes that source unique. Therefore all nonzero states lie on one forward orbit:

`x_{m-1}->x_{m-2}->...->x_1->x_0->0`.

So S1+S2 classify the sector as the chain family `J_m`, for arbitrary finite `m` allowed by the declarations.

For `m>=3`,

`R_1={x_0,...,x_{m-2}}`,

`R_2={x_0,...,x_{m-3}}`,

hence

`empty proper-subset R_2 proper-subset R_1`.

Thus neither one-source semantics nor well-foundedness contains a two-stage bound.

## 3. Decisive `J_3` countermodel

Take

`x_2 -> x_1 -> x_0 -> 0`.

Then

`R_1={x_1,x_0}`,

`R_2={x_0}`,

so `R_2` is proper and nonempty.

Use the extremely weak instantaneous observation

`o(0)=0`,

`o(x_0)=o(x_1)=o(x_2)=1`.

This observation only asks whether collapse has already reached zero. It does not import a residual-depth coordinate.

The full future traces are

`0      : 0000...`,

`x_0    : 1000...`,

`x_1    : 1100...`,

`x_2    : 1110...`.

All four are distinct. Therefore the coarsest future-predictive quotient is the identity quotient.

`J_3` is consequently:

- one-clock under the task's S1 definition;
- downward and well-founded under S2;
- primitive/minimal for the declared future language;
- future-sufficient;
- composition-safe;
- self-composition complete without any state refinement;
- free of hidden future-relevant residual precision;
- nevertheless equipped with `empty proper-subset R_2 proper-subset R_1`.

This meets the taskbook's explicit kill condition.

## 4. Longer-residual pressure

For every `m>=3`, use the same binary zero/nonzero observation on

`J_m : x_{m-1}->...->x_0->0`.

State `x_i` has a future trace consisting of exactly `i+1` leading ones followed by zeros. Hence every depth is future-distinguishable, the minimal predictive quotient is again the identity, and repeated composition is closed on that minimal state object.

Thus the failure is not isolated to `J_3`. There is an unbounded finite family of primitive/minimal, one-clock, downward, future-complete systems with proper intermediate residual layers.

## 5. Predictive quotient comparison

Current E002-style predictive minimization does not imply NC3.

It minimizes only subject to preservation of the declared future behavior. On `J_m`, different remaining lifetimes are behaviorally distinguishable even when the only instantaneous observation is zero/nonzero.

Therefore predictive minimality may require arbitrarily many residual depths. “Minimal” means no redundant predictive state; it does not mean “small enough to be quadratic”.

This independently agrees with the source-side Phase-B observation that predictive minimization does not force the chain height to two, but the raw verdict established the point before that source was visible.

## 6. Composition-safe quotient comparison

The generic composition-safety obligation is the congruence/factorization condition

`q(x)=q(y) => q(c(x))=q(c(y))`.

It guarantees that repeated self-composition acts on the quotient without needing hidden state. It does not bound the height or cardinality of the quotient transition graph.

`J_m` with its minimal predictive quotient satisfies this for every finite `m`.

Therefore P023-style operation factorization does not imply NC3. The missing assumption is an explicit capacity/height law.

Post-freeze method-reuse classification:

`COMPOSE_EXISTING_TOOLS`.

The surviving behavioral replacement uses the already-canonical predictive quotient (`quotient.predictive_partition`) plus composition-safe quotient (`quotient.composition_safe_collapse`) mechanisms. No method novelty is claimed.

## 7. Well-founded stabilization comparison

P020-style well-founded finite stabilization supports S2-type eventual termination but supplies no fixed transient-depth bound.

Every `J_m` is finite and well-founded. Hence stabilization cannot exclude `J_3` or derive NC3 without a separately justified height bound.

## 8. Strictly weaker semantic replacement

The correct non-circular operational principle for “no undeclared state is exposed by repeated self-composition” is:

### FCSC — Future-Complete Self-Composition

For the fixed declared observation/future language, let `q:X->Q` be the minimal predictive quotient. Require:

1. all declared observations factor through `q`;
2. `q` is a congruence for `c`, so an induced `c_bar:Q->Q` exists;
3. `Q` is minimal among quotients preserving all declared future predictions and the induced dynamics.

This condition is invariant under state relabeling and implementation choices. It excludes genuinely hidden future-relevant distinctions but permits legitimate multi-depth predictive states.

FCSC is strictly weaker than NC3 because every `J_m` satisfies FCSC while every `J_m`, `m>=3`, violates NC3.

However, FCSC does **not** preserve the originating quadratic/rank-two payoff: for `J_3`, the canonical free linearization has

`rank(E)=2`,

`rank(E^2)=1`.

Thus the weaker principle supplies honest self-composition control, but not rank dichotomy.

## 9. No-go for a payoff-preserving semantic weakening without a capacity axiom

The originating linear readout proves from NC2 that

`rank(E^2)<rank(E)`.

The desired NC3 readout requires

`rank(E^2) in {0,rank(E)}`.

Together these force

`rank(E^2)=0`.

For the canonical free linearization,

`rank(E^2)=|R_2|`,

so the desired payoff forces

`R_2=empty`.

Hence, inside the declared downward sector, any universal condition that preserves the exact rank-dichotomy payoff must be strong enough to exclude every proper nonempty `R_2`.

With S1+S2 already forcing a single chain, this is exactly a two-stage height/capacity restriction. There is no generic predictive-minimality, quotient-factorization, or well-foundedness theorem that can deliver the same payoff while still admitting `J_3`.

A relation-only restatement such as `|R_2| in {0,|R_1|}` is formally weaker than type-isomorphism language but, combined with NC2's strict drop, collapses to `R_2=empty`; it therefore merely restates the required rank dichotomy at cardinality level and does not cure target leakage.

## 10. Relabeling and invariance pressure

FCSC is invariant under any allowed relabeling because future equivalence and transition factorization are conjugacy-invariant behavioral properties.

By contrast, the frozen `R_2 ~= R_1` branch needs an exact definition of `~=`. If it is ordinary bijective type-preserving relabeling of finite residual state sets, it preserves cardinality.

Under S2, nonempty residual levels strictly shrink along the chain, so the equal-cardinality/relabeling branch is impossible in the nonempty case. The operational content of NC3 inside the declared downward sector is therefore simply `R_2=empty`.

If `~=` is intended to ignore cardinality through some coarser type quotient, that quotient must be independently declared. Defining the type so that the intermediate residual is ignored would be exactly the semantic circularity under audit.

## 11. Originating theorem comparison

Originating theorem:

`research/QUADRATIC_PACKET_NATIVE_ONE_CLOCK_COLLAPSE_RANK_BRIDGE_20260825.md@c3a20f937e362bfe447f444bff3c1d6aa37af96f`.

### What matches

The independent audit and originating theorem agree that:

- NC1 is the one-source condition;
- NC2 is finite downward exhaustion;
- NC1+NC2 force a single chain;
- `J_3` is the first higher-residual pressure case;
- the canonical free linearization satisfies `rank(E^j)=|R_j|`;
- NC1 yields corank one;
- NC2 yields strict rank drop;
- NC3, if assumed at exact relation strength, yields the rank dichotomy;
- PF-N0 alone does not imply NC3.

The downstream algebraic proof is therefore conditionally correct **if NC3 is supplied as an explicit extra assumption**.

### Material semantic disagreement

The source states that a proper nonzero `R_2` must mean either:

1. an additional observable residual-depth type, so the sector was not one-clock/primitive; or
2. hidden state, so the descriptor was not future-complete.

`J_3` gives a third case omitted by that dichotomy:

3. several future-distinguishable predictive states are legitimate states of one single-clock minimal predictive automaton, all are represented, and no hidden state exists.

One source does not imply one predictive state. Minimality does not imply a preassigned two-stage capacity.

Therefore the source's transition from “primitive + complete” to NC3 is not derived from the weaker operational semantics.

## 12. Originating candidate and Phase-B comparison

Candidate freeze:

`research_freezes/QUADRATIC_PACKET_OBSERVABLE_COMPLETE_SELF_COMPOSITION_AXIOM_CANDIDATE_FREEZE_20260825.md@087c18666a0c727274cef208974fd9f9e1d8cd93`.

Phase-B audit:

`research_reviews/QUADRATIC_PACKET_OBSERVABLE_COMPLETE_SELF_COMPOSITION_PHASE_B_AUDIT_20260825.md@c14ec4941dddbdac439da54b6ea4cdc6521429b1`.

Phase B already correctly established that:

- predictive quotient does not imply NC3;
- composition-safe quotient does not imply NC3;
- well-foundedness does not imply NC3;
- `J_3` is predictive and composition-safe if its states are admitted;
- the remaining question is purely whether “primitive one-clock minimum observable capacity” itself excludes that hierarchy.

The independent audit resolves exactly that remaining question against NC3.

The candidate freeze lists as an explicit falsifier a primitive one-clock downward system with a proper intermediate residual that is required for future prediction while the state semantics remains complete/minimal. The binary-observation `J_3` model is precisely such a falsifier.

Therefore the Phase-B `AUDITED_AXIOM_CANDIDATE` status does not survive independent audit at the same explanatory label.

## 13. Semantic circularity certificate

There is no formal algebraic circularity in the originating theorem: rank two and dual numbers are not literally inserted into NC3's syntax.

The defect is semantic/explanatory circularity.

Under defensible standard meanings:

- primitive = minimal future-predictive state representation;
- complete = no future composition requires refinement of that representation;

NC3 is false by `J_3`.

To make NC3 follow, one must strengthen a premise to an explicit restriction equivalent in effect to the desired depth-two conclusion, for example:

`OBSERVABLE_HEIGHT_2: the minimal future-complete predictive quotient has no nonzero residual after two induced applications.`

That is coherent and falsifiable, but it is an additional capacity axiom. Calling the same restriction “primitive” or “complete” does not explain it.

Within S1+S2, the candidate therefore either:

- is false under ordinary predictive/compositional completeness; or
- becomes tautological if “complete/minimal capacity” is defined to exclude exactly `J_3`-type residual depth.

## 14. Relation-to-linear readout at surviving strength

The originating free linearization is faithful for the finite relation object:

`rank(E^j)=|R_j|`.

Accordingly:

- S1 faithfully gives corank one;
- S2 faithfully gives nilpotence and strict rank drop;
- FCSC supplies legal repeated composition on the predictive quotient but gives no rank dichotomy on the original state linearization;
- an explicit height-two axiom would give the desired zero second image, but then rank two is conditional on that extra axiom rather than explained by generic observable completeness.

So the relation-to-linear bridge remains mathematically valid, but the independent audit narrows its epistemic statement to:

`ONE-CLOCK + DOWNWARD + EXPLICIT HEIGHT-TWO/CAPACITY AXIOM -> RANK TWO`.

It cannot validly be advertised as

`ONE-CLOCK + ORDINARY PRIMITIVE/MINIMAL OBSERVABLE COMPLETENESS -> RANK TWO`.

## 15. Foundation-scope classification

NC1:

`TASK-LOCAL N1 SECTOR TYPING / NOT UNIVERSAL FOUNDATION AXIOM`.

NC2:

`TASK-LOCAL N1 DOWNWARD/WELL-FOUNDED TYPING / GENERIC STABILIZATION SUPPORT EXISTS`.

FCSC:

`CONDITIONAL_DERIVED / COMPOSITION OF EXISTING PREDICTIVE + SAFE-QUOTIENT SEMANTICS`.

NC3 / AX-QP-OCSC-20260825:

`REJECT AS FOUNDATION-FACING OBSERVABLE-COMPLETENESS CLAIM`.

Possible separately named height-two sector restriction:

`NOT ADMITTED / NEW EXPLICIT AXIOM WOULD REQUIRE SEPARATE DRIVER TASK AND INDEPENDENT MOTIVATION`.

No Foundation mutation is authorized or performed by this return.

## 16. Final disposition

The hard target is closed by an independent countermodel plus a semantic circularity classification.

The strongest defensible conclusion is:

1. S1+S2 force a single chain but permit arbitrary finite chain length.
2. `J_3` and all `J_m`, `m>=3`, are defensible primitive/minimal, future-complete, composition-safe one-clock downward systems for a fixed binary terminal observation language.
3. Therefore NC3 is not implied by predictive sufficiency, future equivalence, composition factorization, well-foundedness, or ordinary primitive/minimal observable completeness.
4. The exact originating rank-two proof remains conditionally valid if NC3 is separately assumed.
5. The generic weaker replacement FCSC is non-circular and sufficient for honest self-composition control, but it does not yield rank dichotomy.
6. Any condition preserving the exact rank-two payoff in this model must reintroduce an explicit height-two/capacity restriction; that restriction needs independent justification and cannot be obtained merely by naming it “complete”.
7. The originating candidate's own listed `J_3` falsifier is realized.

Final candidate classification:

`KILL / REJECT`

Exact recommendation:

`REJECT`

Stop condition:

`FINAL AUDIT RETURN FROZEN — STOP. FOUNDATION INTAKE OR A REPLACEMENT HEIGHT-TWO AXIOM TASK REQUIRES A SEPARATE CONTROL-PLANE DECISION.`
