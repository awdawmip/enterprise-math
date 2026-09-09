# T6 Shape-Moment Exact Threshold — Persistent Line Dossier

Status: `ACTIVE / DURABLE HANDOFF / USER-DELEGATED LINE`
Parent objective: `EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD`
Initial line publisher Driver-ID: `EM-DVR-1CE3D7`
Created: `2026-09-09`

## State-machine entrypoints

Research execution task:

- Task-ID: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`
- Publication-ID: `TP2-34B106D2512A298C9647`
- Taskbook: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`
- Immutable record: `research_task_records/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/TP2-34B106D2512A298C9647.json`

Persistent line Driver task:

- Task-ID: `GOV-T6-SHAPE-MOMENT-PERSISTENT-LINE-DRIVER`
- Publication-ID: `TP2-1A41A7E378A6A875DC0B`
- Taskbook: `research_tasks/T6_SHAPE_MOMENT_PERSISTENT_LINE_DRIVER_20260909.md`
- Immutable record: `research_task_records/GOV-T6-SHAPE-MOMENT-PERSISTENT-LINE-DRIVER/TP2-1A41A7E378A6A875DC0B.json`

No future execution owner is pre-bound here. A replacement researcher or Driver must enter through the current canonical runtime and receive/adopt the appropriate current owner scope. This dossier is recovery evidence, not execution ownership.

## Accepted mathematical frontier

The line originated in `EM-FREE-OQDA3Z` free research and has the following durable exact frontier:

1. Shape-moment thresholds already closed:
   - `T1 = 6`
   - `T2 = 20`
   - `T3 = 105`
   - `T4 = 301`
   - `T5 = 941`
2. Degree 6:
   - exact explicit `L=360` collision gives `T6 <= 2332`;
   - 2332 is the exact minimum over the whole degree-6 `L=360` integer moment kernel;
   - every maximal prime factor `p>=29` is eliminated below side mass 2332;
   - maximal `p=23` is globally eliminated, including zero-first-digit, inactive-residue and higher-digit rescue mechanisms;
   - for maximal `p=19`, vertical orders `0,...,8` are globally eliminated.

The strongest current p=19 event is the complete order-8 clearance. The smallest unfinished mathematical unit is therefore:

`maximal p=19 -> vertical order 9 -> blocks (3,6) and (4,5)`.

If order 9 is empty, continue orders 10, 11, 12. If p=19 is globally eliminated, descend to maximal primes `17,13,11,...` until either all sub-2332 configurations are excluded or an exact cheaper collision is found.

## Exact evidence pins

Primary durable provenance:

- degree-6 `L=360` whole-kernel minimum 2332: `chatgpt-global-knowledge@ec3ab6f84c9cb0d2dc48dcec7c5d3980f98df910`
- maximal primes `p>=29` eliminated: `chatgpt-global-knowledge@7b2115cc09517be5f26fbf5e1739742cd9119154`
- maximal `p=23` complete global elimination: `chatgpt-global-knowledge@047b47aedbd129d5fb2c2a0af136704f5d802592`
- maximal `p=19` orders 0--5: `chatgpt-global-knowledge@ba91e9b844886f3f9581392ae4f4c80409adf327`
- maximal `p=19` orders 0--7: `chatgpt-global-knowledge@5fb0a1695269ee914e5620e03439333a1a70ec91`
- maximal `p=19` order 8: `chatgpt-global-knowledge@8cdc2272e4d75859002686222dc81d3974a26b1c`

These are evidence/provenance pins. The executable task definitions are the immutable Enterprise Math task records listed above.

## Proof carrier and BRC discipline

Keep the complete integer/exponent carrier:

- denominators `a=e+1`;
- prime valuations;
- signed multiplicities;
- separate positive/negative side masses;
- exact reciprocal-moment congruences;
- the BRC shape observer `H0,...,H6`.

Do not pre-sieve even numbers or obvious composites. Do not replace the carrier by a prime-only sample, total mass, or logarithmic readout before proving that quotient preserves the required output. Candidate-generating numerical methods may be used only with later exact verification.

## Do not repeat

A new assignee should consume, not restart, these verified-complete units:

- `T1,...,T5` threshold closures;
- the entire `L=360` minimum-2332 proof;
- all maximal-prime `p>=29` elimination work;
- all maximal `p=23` work;
- maximal `p=19` vertical orders 0 through 8.

Replay is justified only by a concrete integrity failure in the durable evidence.

## Researcher continuation protocol

The research task is intentionally one end-to-end continuation rather than a speculative chain of prepublished stages.

The next bounded researcher should:

1. recover the current immutable task record and this dossier;
2. begin at `p=19`, order 9, block `(3,6)`;
3. preserve all closed evidence pins;
4. return an exact proof certificate, exact counterexample/kernel, or the smallest strictly newer unfinished unit;
5. persist reusable checkers/censuses before ending if later work depends on them.

If a genuine p=19 modular kernel appears, do not continue an elimination program that assumes it away. Route the kernel into lower-prime completion and update the dossier.

## Persistent Driver responsibilities

The line Driver owns ordinary within-line continuity:

- incremental evidence review against this ledger;
- bounded researcher task routing;
- deciding whether the same task continues or a genuinely new bounded task is warranted;
- preserving accepted and rejected provenance separately;
- requesting independent review/formalization for important terminal claims when appropriate;
- updating this dossier after accepted semantic changes;
- ensuring replacement personnel can resume without predecessor chat history.

Do not prepublish a numeric stage ladder. New tasks are created only when the actual frontier or proof architecture creates a new information gap.

Escalate to the portfolio Owner only for a cross-line conflict, a scope/authority change, major reprioritization, or a decision that changes the parent objective.

## Terminal condition

This line is mathematically terminal only when one of the following is independently audited and durably bound:

- exact global theorem `T6 = 2332`; or
- exact collision with maximum side exponent mass `<2332`.

A taskbook, publication record, local finite clearance, or dossier update is not itself mathematical termination.
