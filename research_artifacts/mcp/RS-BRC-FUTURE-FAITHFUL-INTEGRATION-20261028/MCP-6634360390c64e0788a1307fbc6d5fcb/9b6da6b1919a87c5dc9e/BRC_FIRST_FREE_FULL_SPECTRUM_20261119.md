# BRC first-free allocator: complete finite color spectrum (2026-11-19)

Status: new scoped constructive proof and exhaustive author check; not independently reviewed. Task: RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028, package 2A/2B.

## Model

Fix one target event h, r>=1 registered reference slots initially empty, and r+1 reusable colors {0,...,r}. When h is absent, CREATE(h) picks the least color currently unreferenced by any registered slot or live event. BIND(i,h) replaces slot i by the current live h instance, RELEASE(h) removes that live event while keeping any slots holding its now-invalid identity, and COPY(i,j) copies the identity of slot j over slot i. Identity names are opaque except same/valid/target. Requests are registered and closed; operations are sequential; a single event carrier supports the repeated create/release cycles.

A desired final snapshot has one live event h with color 0 and r nonempty, invalid references to h with color tuple c=(c_1,...,c_r) in {1,...,r}^r.

## Theorem and explicit finite witness

For every r>=1 and every tuple c in {1,...,r}^r, the specified initial state reaches that exact final snapshot in at most 4r+3 API commands. If c contains k distinct colors, the construction uses exactly 3r+4+(r-k) commands. Consequently this first-free closed-reference model reaches all r^r well-formed static color tuples, whose equality-partition projection has Bell(r) states.

Proof: Pick a distinct fixed anchor slot for each color d actually appearing in c. Reserve a designated slot s_r: if r occurs, use its anchor; otherwise choose any currently unassigned slot. Assign each d=1,...,r-1 to its anchor if used and otherwise to a distinct remaining slot. Temporarily assign color 0 to s_r. For d=0,1,...,r-1 perform CREATE(h), BIND(the slot for d,h), RELEASE(h), in that order. At each creation the used colors are exactly 0,...,d-1, so first-free returns d. Next CREATE(h) assigns color r; BIND(s_r,h) replaces the 0-reference; RELEASE(h). The registered slots now hold colors 1,...,r exactly once, so one more CREATE(h) selects the freed color 0. All slots hold invalid instances, and the live current event is color 0. For each slot that is not its desired final color, COPY from the fixed anchor for that final color; these anchors remain intact. Exactly r-k copies are needed. The initial r triplets cost 3r operations, the additional color-r triplet costs 3, the final creation 1, and copies r-k. All steps satisfy the typed API and closed-reference capacity r+1. QED.

For r=6 the target set comprises 6^6=46,656 tuples and exactly Bell(6)=203 distinct equality partitions. A deterministic companion checker enumerated all tuples for 1<=r<=6: 50,069 targets, each reaching the requested final state. Reported maximum lengths for r=1,...,6 are 7,11,15,19,23,27. This is an exhaustive finite check of the construction at those r, alongside the general symbolic proof.

## Exact boundary and source reuse

The proof resolves a specific reachability question left separate in research_notes/brc_alias_counting_bridge_20261028/PROOF.md: a deterministic first-free color policy under one target, closed registered references, overwritable slots, and sequential API. The source abstract behavior quotient is research_notes/chatgpt_direct/20261028_residual_dynamic_alias_52c8e1/RESULT.md. Its r=6 Bell-count and full color-tuple count are reused inputs, not newly discovered values. We establish reachability for the declared physical allocation language, not equal multiplicity of execution histories, other allocator policies, external hidden references, concurrent mutation, or actual triadic macro execution-cost bounds. Next: map CREATE/BIND/COPY/RELEASE to actual typed triadic macro costs and exact event constraints, or extend to a specified constrained alias observation.
