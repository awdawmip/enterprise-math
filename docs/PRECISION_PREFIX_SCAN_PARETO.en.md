# Prefix-Observable OR Semantics: Scan Work/Depth Pareto

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The prefix-observable boundary fixes the semantic object first: for H action masks, the executor must output every inclusive cumulative OR, not merely the final terminal effect.

Only after that semantic requirement is fixed is it valid to compare execution representations.

Two exact scan implementations expose a clean work/depth/storage tradeoff.

## 1. Declared semantic output

Given k-bit action masks

`A_1,...,A_H`,

output all prefixes

`U_t=A_1 OR ... OR A_t`, `t=1,...,H`.

This is exactly the cumulative-mask normal form of the parent prefix-observable word semantics.

Any representation returning only `U_H` is semantically insufficient for this task.

## 2. Sequential streaming scan

Compute

`U_1=A_1`,

`U_t=U_(t-1) OR A_t`.

Resource counts:

- word-level binary OR gates: `H-1`;
- bit work: `k*(H-1)`;
- batch dependency depth: `H-1`;
- extra working state beyond an output sink: one k-bit current mask.

The outputs can be streamed as they are produced.

## 3. Sequential scan is globally work-minimal in the OR-only model

The final required prefix `U_H` is itself the OR of H independent input masks.

Even if no earlier prefixes were requested, a fan-in-two OR-only circuit needs at least `H-1` word-level OR gates to compute that final output.

The sequential prefix chain uses exactly those `H-1` gates, and every intermediate gate output is already one required prefix.

Therefore no extra OR work is needed to expose the other prefixes: sequential scan attains the global word-gate lower bound for the **entire** prefix output task.

This does not make it depth-optimal.

## 4. Prefix depth lower bound

The final H-input OR has fan-in-two depth at least

`ceil(log2 H)`.

Therefore every exact full-prefix circuit has critical-path depth at least this value.

A depth-optimal circuit must pay some other resource because the H-1-gate sequential chain has depth H-1.

## 5. Hillis-Steele parallel inclusive scan

Use synchronized offsets

`1,2,4,...`.

At offset s, every position `i>=s` computes

`old[i] OR old[i-s]`

from the previous round.

Let

`r=ceil(log2 H)`.

Then exact resource counts are:

- parallel depth: `r`;
- word-level OR gates:
  `sum_j (H-2^j) = rH-(2^r-1)`;
- bit work: `k * [rH-(2^r-1)]`;
- one simple synchronized double-buffer implementation uses `2H` working masks;
- all H prefix outputs are available after the final round.

The owner cross-checks every result against sequential prefix semantics on exhaustive small mask families.

## 6. Hillis-Steele hits the unavoidable depth lower bound

Its number of synchronized rounds is exactly

`ceil(log2 H)`,

the lower bound forced by the final prefix.

So it is depth-optimal in the fan-in-two OR model.

No claim is made that Hillis-Steele minimizes **work** among all depth-optimal or near-depth-optimal prefix circuits. Classical parallel-prefix networks provide additional size/depth points.

The purpose here is to lock two exact, easily auditable extremal resource points.

## 7. Sharp H=8 comparison

For H=8 and k=5:

### Sequential

- word OR gates:7;
- bit work:35;
- depth:7;
- extra streaming working masks:1.

### Hillis-Steele

- word OR gates:`3*8-(1+2+4)=17`;
- bit work:85;
- depth:3;
- double-buffer working masks:16.

Thus10 extra word ORs plus more buffer storage buy a four-layer critical-path reduction.

## 8. Sharp H=20 comparison

For H=20:

`r=5`.

### Sequential

- word OR gates:19;
- depth:19.

### Hillis-Steele

- word OR gates:`5*20-(32-1)=69`;
- depth:5.

So50 extra word ORs buy14 layers of batch critical-path depth.

## 9. Terminal-only balanced reduction is not a valid Pareto point for this semantic task

A balanced reduction tree can compute only the final mask using

- `H-1` word ORs;
- `ceil(log2 H)` depth;
- one final output.

Those resources look strictly attractive because they combine the sequential work lower bound with the parallel depth lower bound.

But the representation does **not** produce the H prefix states required by the declared future language.

Therefore it is not a better implementation of the same semantic object. It is an implementation of the **coarser terminal-only semantic language** from the parent boundary.

This is a concrete warning against mixing semantic loss into a resource Pareto.

## 10. Batch depth and streaming latency are different resources

The sequential scan's batch critical path is H-1 when all H inputs are considered available at time zero.

But if actions arrive causally one at a time, the same scan is naturally online:

- retain one current prefix mask;
- consume the next action;
- perform one OR;
- immediately emit the next prefix.

It therefore has O(1) extra state and one update operation per arriving action.

Hillis-Steele's logarithmic depth is an offline/batch parallel result that assumes simultaneous access to the batch and synchronized rounds.

So execution-depth claims must declare whether they measure:

- offline batch critical path;
- online per-arrival latency;
- total work;
- live working storage.

## 11. Prefix semantics changes the optimal representation question

For terminal-only OR semantics, the parent one-shot fused tree is enough.

For full prefix semantics, every cumulative state must be exposed. The work-minimal structure becomes the sequential prefix chain, while lower batch depth requires a genuine prefix network with additional work/storage.

Thus changing the observation language changes not just the number of semantic states, but the entire execution-resource frontier.

## 12. Stage131 ordering discipline

The complete procedure is now explicit:

1. declare terminal versus prefix-observable semantics;
2. derive the exact semantic normal form;
3. choose an execution model (online/offline, fan-in, working-memory assumptions);
4. compare work/depth/storage only among implementations of that same semantic object.

A terminal-only balanced tree must not appear as a dominating point on a prefix-semantic Pareto frontier.

## Owner-local assets

- `src/enterprise_math/prefix_or_scan_pareto.py`;
- `tests/test_prefix_or_scan_pareto.py`;
- this bilingual theorem note.

## Prior art / status

Parallel prefix scans, Hillis-Steele networks and OR-circuit lower bounds are standard prior CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the Stage131 prefix-semantic resource routing and exact resource accounting.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
