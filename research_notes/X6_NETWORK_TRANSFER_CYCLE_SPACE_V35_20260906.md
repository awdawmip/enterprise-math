# X6 upper V35: conservative transfer-skew memory is an integer incidence circulation; trees cannot store stationary chirality

Status: `FREE_RESEARCH / EXACT T3 CIRCUIT-CALCULUS REUSE + NETWORK NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Method reuse: `T3_TYPED_INCIDENCE_CIRCUIT / CIRCUITS + CIRCUIT_DECOMPOSE`.
Depends on:
- `X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`;
- `X6_TRANSFER_SKEW_CHIRALITY_MEMORY_V33_20260906.md`;
- `TOOL_DISCOVERY_NATIVE_ORIENTED_MATROID_CIRCUIT_CALCULUS_RESULT_20260822.md`.
Checker: `experiments/x6_network_event_ledger_v29_20260906/check_network_circuit_holonomy.py`.

## 1. Typed T3 reuse

The current cross-Cell interaction network is a finite typed incidence skeleton, exactly the admitted ground type of T3.

Choose an arbitrary reference orientation for every undirected admissible Cell-connection edge. This orientation is gauge only.

For edge e let

`N_e^+`

count completed transfers along the reference orientation and

`N_e^-`

count completed transfers in the reverse direction.

Define the integer net transfer chain

`j_e=N_e^+-N_e^-`.

Thus

`j in C_1(G;Z)=Z^E`.

No negative primitive transfer count is introduced; j is a signed contrast of two nonnegative occurrence counts.

## 2. Incidence boundary is the Cell scalar bias

Use T3's combinatorial boundary

`partial(e)=target(e)-source(e)`.

Then for each Cell x,

`(partial j)_x = completed incoming transfer count - completed outgoing transfer count`

at the scalar Cell level.

Internal PF-10 PASS events do not affect this scalar because each completed internal passage contributes one ingress and one egress at the same Cell.

Therefore, in the V29 closed-network ledger with no external source/sink residual,

`q_x := sum_a u_x,a = (partial j)_x`.

This is the network-scale continuity identity corresponding to the port-level V28 identity.

## 3. Stationary conservative transfer skew is exactly a circulation

If every Cell has zero scalar net accumulation over the declared window,

`q_x=0 for all x`,

then

`partial j=0`.

Hence

`j in ker(partial)`.

By the reused T3 CIRCUITS theorem, every nonzero integer j in this kernel decomposes into signed primitive incidence circuits/simple cycles.

So persistent conservative transfer nonreciprocity is not arbitrary edge data:

`STATIONARY CONSERVATIVE TRANSFER SKEW = INTEGER CYCLE CHAIN`.

The decomposition into simple circuits need not be unique on a multi-cycle graph; if future operations distinguish circuit provenance, BRC/T3 circuit witnesses must be retained rather than only the total chain.

## 4. Tree no-go

For a connected tree with n vertices and n-1 edges, the incidence map has zero cycle kernel:

`ker(partial)=0`.

Therefore

`partial j=0 -> j=0`.

So a closed stationary tree network cannot store a nonzero conservative transfer-skew chirality using only edge transfer counts.

Any persistent directed bias on a tree requires at least one of:

- nonzero Cell accumulation / boundary residual;
- an external source/sink;
- additional internal memory not represented by net transfer edge counts;
- time-dependent nonstationarity.

This is an exact network obstruction, not a continuum approximation.

## 5. Cycle rank

For a finite graph with c connected components,

`rank_Z ker(partial)=|E|-|V|+c`.

Thus the number of independent integer transfer-circulation coordinates is the ordinary graphic cycle rank.

This is a count of relational loop degrees, not a count of Enterprise spatial dimensions.

The result is gauge-independent: reversing a reference edge flips the corresponding j coordinate and T3 circuit signs but not the circulation lattice.

## 6. Triangle is the minimal simple chirality store

For a simple connected graph, the smallest nontrivial circuit has three vertices.

On the three-Cell complete/triangle graph,

`rank ker(partial)=1`.

Choose one primitive oriented triangle circuit c. Every stationary net transfer current is uniquely

`j=m c`,

`m in Z`.

For `m!=0`:

- `|m|` is the transfer-circulation magnitude in this circuit coordinate;
- `sign(m)` chooses one of the two ring orientations.

This is exactly the V33 transfer-skew chirality memory, now identified as the primitive T3 circuit coordinate of the triangle network.

The zero state m=0 retains the V33 two-branch orientation ambiguity if an oriented ring seed is demanded next.

## 7. Closed-loop transfer event as chirality increment

A sequence of matched TRANSFER events that traverses one full directed simple network cycle adds one primitive circuit chain c to j.

Because `partial c=0`, this complete loop returns every Cell's scalar transfer balance to its previous value while changing the circulation state

`j -> j+c`.

Thus relation-event history can write persistent chirality into the cycle lattice without net Cell accumulation.

The reverse loop writes `-c`.

This is the general-network form of V33's reinforcement layer.

## 8. BRC / observer boundary

The projection from raw inter-Cell transfer history to j erases:

- event order;
- repeated forward/backward pairs that cancel in net chain;
- decomposition provenance when multiple circuits overlap;
- temporal interleaving with internal PASS events.

Therefore j is operation-safe only for futures proved to depend on net transfer circulation alone.

V30 already supplies a concrete warning: order-erased ledgers can lose frame transport after nonlinear active-state updates.

## 9. Structural consequence

The network now has a precise relational storage hierarchy:

`RAW TRANSFER EVENT TRACE`

`-> NONNEGATIVE DIRECTED EDGE COUNTS`

`-> INTEGER NET EDGE CHAIN j`

`-> CYCLE-LATTICE STATE ker(partial) WHEN STATIONARY`

`-> scoped chirality / circuit observers`.

No layer is identified with X6 spatial coordinates.

## 10. Next frontier

V35 classifies where stationary conservative network nonreciprocity can live.

The next question is how a network circuit acts on active-triad relational states. V36 proves a universal loop-to-ring realization: every closed active-triad walk can be realized as a deterministic directed Cell ring using the canonical V20 pure-triadic coupling.
