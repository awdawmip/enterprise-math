# Fixed-source literature intake: finite two-way relation processing

Review date: 2026-10-07 UTC  
Repository: openai/math  
Fixed commit: adc7f1241b42e322a6451854ab7e4b4c146bf78a  
Decision: admit a narrowly scoped external research task for finite reentry certificates and a typed resource bridge. Do not adopt the headline lower bounds as established Enterprise Math results.

## 1. Result and scope

The two papers in family 129 are the strongest fit. Both work directly with finite binary relations and finite machines. Their relevant contribution is a proposed obstruction to replacing nondeterminism by unrestricted two-way read-only input motion with small finite control. This is more specific than standard subset construction, predictive quotients, or extensional word congruence.

The recommended task is to reconstruct a certificate-checkable four-direction boundary summary, including repeated reentry and stay cycles; audit symbol-local deterministic slot wiring; and either prove an explicit reduction from a declared EM resource model to the paper's machine model or exhibit the precise obstruction. This is an external finite-algebra/automata task. No inference about the native EM geometry follows.

The official [announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) is dated October 6, 2026. It describes released model-generated results and accompanying formalizations, with future revisions anticipated. The fixed [repository README](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/README.md) states that results have different verification stages and that unformalized results may have issues. Neither announcement nor README substitutes for checking an individual claim.

## 2. Selected papers and completed reading

### A. One-way liveness / deterministic two-way state cost

OpenAI, “An exponential two-way deterministic state lower bound for one-way liveness,” September 25, 2026. [Fixed PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf)

Complete text read from the fixed TeX sources: build/main.tex, build/preamble.tex, all five build/sections files (introduction, matching, rank, machines, separation), all four build/figures files, references.bib, and the manuscript README. No TeX or other repository code was executed.

The directly relevant proof sections are:
- [machines.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/sections/machines.tex): local matching representation, sink component, tree tour, candidate slots, symbol locality, acceptance conventions
- [matching.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/sections/matching.tex): rank/support, idempotent corner reduction, common support transport, minimum-rank unit lifts
- [rank.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/sections/rank.tex): the 32-conjugate/256-addition amplification and full relation-monoid requirement
- [separation.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/sections/separation.tex): singleton-context separation, surjective relation quotient, final state bound

### B. Nondeterministic two-way complementation cost

OpenAI, “An exponential state lower bound for two-way nondeterministic complementation,” September 25, 2026. [Fixed PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf)

Complete text read from build/paper.tex, all five build/sections files (introduction, diagrams, nesting, amplification, automata), both build/figures files, references.bib, and the manuscript README.

The directly relevant proof sections are:
- [diagrams.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/sections/diagrams.tex): four boundary relations, finite-path product, order reversal, recurrent classes, transport through fixed contexts
- [nesting.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/sections/nesting.tex): containment dichotomy and cumulative missing-class budget
- [amplification.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/sections/amplification.tex): minimal corners and the 128-generator/4096-addition argument
- [automata.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/sections/automata.tex): exact finite-computation representation, stay closure, endmarker treatment, and state accounting

### Deferred C. Prefix histories / forced flows

“Prefix Instructions and Incompressible Flows,” September 27, 2026, was screened from the catalog, manuscript README, source directory, and family-376 Lean scope documentation. Its full proof text was not read in this intake and it is not a selected absorption target.

The family-376 Lean scope names other manuscripts, not this one. Its continuous incompressible-flow realizations require substantially more than a finite branch-history analogy. Existing EM residual/history work already overlaps the general preservation idea. Defer unless a new finite lemma and an explicit embedding/readout/update bridge are identified. Do not describe it as checked or as supporting EM native geometry.

## 3. Exact external theorem statements and assumptions

All compositions below are in path order: (x,z) belongs to AB iff some y has xAy and yBz.

### A1. Paper A main theorem / actual Lean target

Let H have h elements, h ≥ 2. The input alphabet consists of ALL binary relations on H, of size 2^(h²). For a finite word w = R₁…Rₗ, let r(w) = R₁…Rₗ; the empty product is I_H. Define OWL_h by r(w) ≠ empty.

There is a nondeterministic automaton with h+3 states, using no left moves, recognizing OWL_h. Every s-state deterministic two-way automaton recognizing it on every finite word satisfies

2^floor((h−2)/31) ≤ 4(s+2)².

If reaching an accepting state at time zero counts, the stronger right-hand side 4(s+1)² applies.

Machine assumptions:
- One head on a finite read-only word with two distinct endmarkers
- Initial head position is the left endmarker, in a specified state
- The next state and left/stay/right move depend only on current state and scanned symbol
- No movement beyond either marker
- Partial transition rules allowed
- Acceptance is the existence of a finite run reaching an accepting state
- Infinite nonaccepting runs reject; global halting is not assumed
- No writable cells, extra heads, work tape, advice, randomness, or other mutable store
- All control states, including initial, accepting, rejecting, and any normalizing copies, are counted
- Equivalence is on all finite input words, not only bounded length or a promise subclass

The actual declaration in [Automata/Main.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Automata/Main.lean), OAI.OneWayLiveness.main_theorem, quantifies over h ≥ 2, Bool acceptance convention, s, and DMachine (Alphabet h) s. Its recognition hypothesis is exact all-word recognition. There is no additional unproved algebraic surjectivity hypothesis at this endpoint: the solution source derives that condition internally.

This is a state-succinctness statement uniform over growing finite alphabets. It is not a fixed-alphabet claim, a transition-table-size lower bound, a running-time lower bound, or a separation of uniform logarithmic-space classes.

### A2. Algebraic degree obstruction used by A1

Let D_k be the Brauer matching monoid on k labeled ports per boundary. Its elements are perfect matchings of the 2k ports; multiplication glues equal middle labels, contracts boundary-to-boundary paths, and discards internal components.

For finite H of size h ≥ 2, if an identity-containing submonoid S of D_k admits a unital surjection onto the ENTIRE relation monoid R_H, then

k ≥ 2^floor((h−2)/31).

A surjection onto only a small generated submonoid of relations is not enough. The stronger inductive statement assumes permutation-diagram lifts of every permutation and an idempotent whose image is I_H union one off-diagonal pair; its rank defect is at least the same quantity. The corollary removes the lift assumption by a minimum-rank idempotent corner. These are external manuscript claims with accompanying solution source, not independently kernel-checked here.

### B1. Paper B main theorem / actual Lean target

For every n ≥ 4, put H = {1,…,n−2} and Sigma_n = R_H. There exists an n-state two-way nondeterministic automaton A_n recognizing the nonempty relation-product language such that every two-way nondeterministic automaton recognizing its complement has at least

(1/2) 2^floor((n−4)/127) − 1

states. Equivalently, for a target with s states, 2(s+1) ≥ 2^floor((n−4)/127).

The conventions are the same one-read-only-head finite-acceptance model above, with accepting initial configurations counted. The source construction needs only h+2 states because missing transitions can reject instead of using an explicit rejecting sink. The alphabet size is 2^((n−2)²). Again, there is no fixed-alphabet or transition-table-size conclusion.

The actual endpoint is OAI.TwoWayComplementation.complementation_lower_bound_finite in [TwoWayAutomata/Main.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/TwoWayAutomata/Main.lean). It allows an arbitrary finite target state type Q, takes equality with the complement language, and concludes the real-valued inequality above.

### B2. Order-reversing image obstruction

For m ≥ 1, let T_m be the finite monoid of four-direction path diagrams with m labels in each direction. If S₀ is a submonoid of T_m and a surjective multiplicative map phi₀: S₀ → R_H, h ≥ 2, reverses componentwise inclusion,

z ⊆ w implies phi₀(w) ⊆ phi₀(z),

then 2m ≥ 2^floor((h−2)/127). Initial identity preservation need not be assumed; the proof passes to an appropriate idempotent corner. Full surjectivity and order reversal are essential.

## 4. Nontrivial proof bridge to reconstruct

### Four-direction composition and reentry

A diagram a has relations F_a: D+→D+, B_a: D−→D−, L_a: D+→D−, R_a: D−→D+. F and B are through paths; L and R are returns. Product means finite traversal from an outer entry to the FIRST outer exit, with earlier joins internal. Star is reflexive transitive closure, including zero repetitions.

The precise formulas are

F_ab = F_a (L_b R_a)* F_b  
B_ab = B_b (R_a L_b)* B_a  
L_ab = L_a union F_a (L_b R_a)* L_b B_a  
R_ab = R_b union B_b R_a (L_b R_a)* F_b.

These preserve arbitrary finite reentry. Omitting return relations or truncating the stars is not the same observation model. Segment substitution is exact only for the declared boundary observations and admissible gluing operations. It does not preserve path multiplicities, order histories, endpoint-conditioned moments, or provenance unless those are separately encoded and proved.

This monoid and its basic path-contraction interpretation are attributed in Paper B to Martin and Mazorchuk's partitioned binary relations (2013). Rebranding the four relations as an entirely new external discovery would be inaccurate.

### Symbol-local deterministic wiring

Paper A's key representation obligation is not just relation multiplication. Normalize acceptance to a unique terminal right-marker sink, then represent the sink's predecessor component as a tree. For each neighbor boundary, reserve a separate slot for each direction and ordered source/target state pair, with two traversal lanes.

A slot always attaches at its target to the designated target-state vertex. At the source, it attaches to the source-state vertex exactly if that symbol's transition row selects that transition; otherwise it attaches to its OWN fresh leaf. Thus no symbol diagram reads its neighbors, word position, or word length. Determinism gives injectivity of the source assignment. Identifying unused leaves, silently assuming injectivity for a nondeterministic source, or consulting neighboring symbols breaks this bridge.

After sink normalization, the port degree is k = 4(s+1)²; positive-transition-only acceptance first adds an initial copy, giving 4(s+2)². Port count is not the total explicit graph size or storage size of a compiler.

Exact solution-source checkpoints:
- [Automata/Network.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Automata/Network.lean): sourceAttach_injective, graph_step_from_state, graph_reach_state, graph_terminal, graphOrder
- [Automata/Tours.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Automata/Tours.lean): finite functional-graph tour infrastructure
- [Automata/Diagrams.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Automata/Diagrams.lean): fullDiagram_compatible, reach_excludes_separation, separation_of_not_reach, diagram_recognizes_reach
- [Automata/Recognition.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Automata/Recognition.lean): recognitionTest_iff, liveness_rank_bound, deterministic_lower_bound
- [Automata/Syntactic.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/Automata/Syntactic.lean): singleton_context, context_separates, matching_recognition_degree

The formal recognition test uses absence of a compatible Boolean coloring separating the outer test positions, rather than literally repeating the prose's one-pair test-port predicate. The source proves an exact reachability equivalence for that test; this is a concrete representation difference to record, not an identified failure. Only the normalized target configuration is required terminal; no all-runs-halting premise is introduced.

### Shared-loss budget, as a later optional audit

For idempotent path diagram e, define K_e+ = (L_e R_e)*, P_e+ = K_e+ F_e K_e+ and reflected minus versions. Recurrent classes are mutual P_e-related recurrent points, with signs kept distinct. For z in e T_m e, M_e(z) records classes lacking a surviving loop through K_e±, z's appropriate through relation, and K_e±.

The paper states:
- M_e(zw) is contained in M_e(z) union M_e(w)
- If e,d are idempotents and uev=d, one common missing-class set J transports to one common J' with |J'|≤2|J| for all admissible z in the e-corner whose uzv belongs to the d-corner
- For nested idempotents b_j b_(j−1)=b_(j−1) b_j=b_j, if all initial-relative missing sets lie in one J₀, then the sum of successive missing-set cardinalities is ≤2|J₀|

The crucial crossing argument is rectangle switching: two same-sign recurrent witnesses using a common middle recurrent class can exchange prefixes/suffixes, so they lie in the same outer recurrent class. This supplies the factor-two common-set transport, not merely a separate numeric bound for each replacement.

Exact source: TwoWayAutomata/Transport.lean, classInfluence_cross and transport; TwoWayAutomata/Nesting.lean, nested_class_containment, nested_unprotected_loss, nested_chain_bound. These are promising finite invariants, but a minimal first task need not adopt the full exponential amplification.

## 5. Verification status

The Lean toolchain is leanprover/lean4:v4.34.1. The fixed lake-manifest pins mathlib to d13f23b723b8a846827a245b89c10fc7d3f11612 and includes additional dependency revisions. The full manifest and comparator configurations are retained in the source ledger.

The [family-129 scope document](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/129.md) links separate comparator targets for complementation, same-family determinization, and one-way liveness. Its first scope paragraph excludes the separate liveness result from that particular description; a later paragraph explicitly describes the liveness formalization. Do not interpret the earlier sentence as excluding every liveness artifact.

The comparator JSONs point to actual solution modules and permit only propext, Quot.sound, and Classical.choice; enable_nanoda is false. Comparator challenge .lean files contain intentional sorry placeholders specifying the requested theorem. The solution Main files contain proof terms rather than these placeholders.

All 42 Lean files in Automata and TwoWayAutomata were retrieved and scanned for imports and the literal tokens sorry, admit, axiom, unsafe. No such tokens were found in those solution directories. Their source imports close within those directories plus Mathlib. This is a text-level screen only: it neither validates elaboration nor proves axiom closure or semantic equivalence.

Critical theorem statements and selected connecting proofs were read in detail. The entire TeX proof text of both papers was read. The large imported Mathlib body was not audited. Lean, Lake, Comparator, lean4export, landrun, repository build scripts, and repository executables were NOT run. No independent kernel verification or general theorem acceptance is claimed.

The fixed formalization.yaml calls the project scope “Partial progress.” and review status “unchecked.” The comparator README gives a checking recipe, not evidence that this intake executed it. Any later checking must retain the fixed source/dependency versions and report the actual checked declaration and tool result. Avoid unpinned lake update when claiming reproducibility.

No definite mathematical counterexample or hypothesis omission was found in this read. Equally, absence of an identified issue is not independent confirmation of these major claims.

## 6. Recommended single research task

Working title: Certify two-way relation reentry

Hard target:
Produce an independently specified finite certificate for composition under arbitrary reentry, audit the symbol-local deterministic representation with complete raw-resource accounting, and conclude either:
1. a typed, assumption-complete reduction for one declared EM observer/resource model, with the exact resulting conditional lower bound; or
2. a smallest explicit obstruction showing why that model does not reduce to the external machine model.

Minimum substantive obligations:
1. Define typed entry and exit ports, all four Boolean boundary relations, stay closure, endmarkers, and finite first-exit semantics
2. Give a certificate checker or proof specification that verifies every positive summary edge by a finite path and every absent edge by a closed reachability set; verify product via the four formulas and by direct glued-graph reachability independently
3. Include a case requiring a genuine return/reentry, a stay cycle, a nonaccepting infinite run, and an empty body word; a forward-only product must fail an intentional negative control
4. Verify symbol locality and distinct inactive-source leaves in deterministic candidate wiring; include an intentionally merged-leaf negative control
5. Account separately for h, s, the 2^(h²)-symbol alphabet, transition-table entries/encoding bits, normalizing states, 4(s+c)² ports, slot/leaf/stay-candidate counts, generated summary representation size, and computation cost
6. Prove preservation of the declared observations for every permitted word/operation, not just sample words or equality of the current readout
7. For headline transfer, map every piece of EM mutable state to the finite control count and identify the single read-only input head. Verify full alphabet availability, all-word recognition, no extra mutable tape/residual store, and the exact acceptance convention
8. If claiming an algebraic shortcut, certify a unital full-relation-monoid image for the matching branch or an order-reversing full image for the nondeterministic-complement branch. A generated subset or sampled image is insufficient

A bounded enumeration can be a regression test, but it cannot establish the all-h exponential theorem. Closing a finite generated-summary table also cannot silently stand in for the full relation monoid. Very large alphabet/diagram sizes are part of the cost and may be the practical obstruction.

Dedup baseline:
Existing EM relation_future_powerset.py already implements standard reachable-support subset construction; operation_quotient.py covers the coarsest finite all-word stable partition; relation_observable_composition.py handles future-signature descent; material_word_quotient.py already addresses extensional prefix/suffix congruence; material_future_quotient.py covers observer-relative branch retention; action_language_precision.py covers resource counts. Existing ordered-path residual work also asks for endpoint-conditional moments and resource costs. Therefore a generic quotient, history-retention argument, or support compiler is not a new target.

The elementary h-bit append-only-support and h²-bit arbitrary two-sided-relation distinguishability statements can be retained only as scope regression baselines. They do not replace the two-way representation/reentry obligation and do not themselves constitute the research result.

## 7. Negative stops and native boundary

Stop external-to-EM theorem transfer if:
- EM uses writable input, multiple heads, unbounded residual/history storage, arithmetic registers whose cardinality is not counted, randomization, or advice absent from the target machine model
- The observer language is only bounded horizon, a restricted alphabet, one fixed prefix, or a promise input family while the external theorem requires all finite words over all relations
- The proposed compiler preserves nonemptiness but claims preservation of counts, signed weights, moments, path identities, or cocycles
- Current readout equality is substituted for preservation of every declared future operation and observation
- Source locality, deterministic source injectivity, or distinct inactive leaves fails
- Star is truncated without an independently proved finite exact-closure bound
- The claimed lower bound changes the resource measure from state count to total raw input, table, wire, or implementation size without a proved reduction
- Kernel/Comparator checking fails, dependencies drift, or the stated theorem differs from the actual checked target

EM native premises remain internal premises: 6D discrete native cell space with separate time, enterprise pairwise orthogonality at native 120 degrees, and 3D slices rather than a native 2D plane. h and the diagram's two boundaries are combinatorial parameters, not native dimensions. Any later native transfer must explicitly specify the slice embedding, third-component meaning, readout, and preserved updates. External mathematics is not evidence of external agreement with those premises.

This literature report grants no theorem acceptance. Formal task existence is determined solely by the accompanying immutable V2 task-publication record, separate from this source assessment. The mathematical research target remains open.

