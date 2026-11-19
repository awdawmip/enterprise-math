# U27F-05 | Strict committed-prefix loss vs potential-reference connectivity (first frozen check)

Task: RS-CELL-U27F-05-EVENT-SEPARATION-20261012
Researcher: EM-X6-C7A253; scope: author-level exact finite observer calculation from fixed inputs, not independent audit, Result freeze or admitted native law.
Frozen inputs: enterprise-math@e91d67d0d2a8bee62fc264c26e9deb2166a6af93:
- research_inputs/U27F_20261012/fixtures/base_case.json (Git blob 15ccb3ad4037d60193a9d9b06ff4865754b8e6ec);
- research_inputs/U27F_20261012/fixtures/interrupted_after_carry.json (Git blob e35281e64806f3dd9e1f2ad6520449c7bf0e2416);
- research_inputs/U27F_20261012/fixtures/recorded_oracles.json (Git blob 0d20ce26e1d1c3f7e18a0e137014bd54af49f20f).
The original full code archive em_u27_followup_tasks.zip (SHA256 a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7) was NOT available for source-code replay.

## Exact static event distinction

Let V={0,1,2,3}, representing bodies A,B,C,D. The interrupted_after_carry.data.bound entries expose the committed/bound edge carrier E_b={(0,1),(0,3)}.
Its connected components are {0,1,3} and {2}; therefore the Boolean observer
D_bound(s) := [ (V,E_b) is disconnected ]
has the exact value TRUE in this saved snapshot. This is a direct graph calculation, independent of an assumed Markov law or BRC weight.

The reference pending_reference.paths.links additionally lists (2,3), while lost_edge explicitly equals [2,3]. Define, for comparison only, E_ref := E_b union {(2,3)}.
Then (V,E_ref) is connected (path 1--0--3--2). Hence D_bound(s)=TRUE while D_ref(s)=FALSE for this same record. E_ref is a possible reference/readout comparison, NOT an operative-contact assertion: a listed lost edge is not automatically restored by appearing inside pending_reference. Similarly held token 2 at [1,0,1,0,0,0], free token 3 at [1,1,0,0,0,0], and incidence=PENDING do not themselves certify that the missing edge is currently operative.

Consequence: a prefix observer defined from current bound edges, an observer defined from historical/pending reference edges, and a future-repair target are distinct functions. They may disagree before any terminal repair. A transition law must identify which carrier has operative-contact meaning before any probabilities of effective global loss can be claimed; F01 (operative continuity) and F03 (interruption successor) remain explicitly referenced dependencies.

## Delta-zero logic and recorded evidence

For a process in which the ONLY source of new work-loss events is a Bernoulli hazard with parameter delta on each eligible step, delta=0 implies
P(new work loss occurs before repair)=0.
This statement is conditional on the stated hazard exhaustiveness and says nothing by itself about prefix detachment or whether repair occurs almost surely.

The provided recorded_oracles.json contains an author's historical, not independently rerun, cap4_d0 reference:
B=4, epsilon=1/16, delta=0, repair_before_new_loss=1, new_loss_before_completion=0, expected_executed_work_to_stop=50405/32; it is a U26 stop-model record, NOT a probability computation for the continued interrupted U27 process. The interrupted snapshot may be unreachable at delta=0 under the frozen stochastic kernel; it must not be substituted unconditionally into the delta-zero sample space.

## Event-order bookkeeping to carry forward

Define four typed observables separately: N = first NEW_DAMAGE event, S = first strict-prefix loss of committed connectivity, G = first effective whole-system loss under a future verified operative-contact predicate, R = final repair. S is an observation of a prefix, not an extra absorbing state; the same trajectory can satisfy S and later R. Thus P(S)+P(R) is not a general conservation partition. An exact BRC exit partition must use mutually disjoint terminal outcomes, with prefix flags carried as state memory if needed.

This establishes a finite exact observer-separation instance and identifies the missing input that affects the full hard target: the executable F01 operative-contact predicate plus F03 continuation/first-step transition, tested on the actual frozen archive. No 56-state re-run, new BRC probability, general-delta bound, native causal promotion, or independent acceptance is claimed. Next independent unit: explicitly pin F01/F03 successor transitions or document their unresolved ambiguity; only then calculate the first delta=0 prefix event with a valid reachability condition.
