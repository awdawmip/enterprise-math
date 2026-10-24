# Auxiliary iid N=14 exact stage90 — directional candidate, not yet proved

## Exact parent and frozen sources

Read \`research_notes/n14_aux_iid_affine_89_20261025/PROOF.en.md\`, \`derive89.py\`, \`crosscheck89.py\`, and \`certificate89.json\` at their immutable source commit. Preserve predecessor stage88 source commit \`a08b0e41d583dabefe00b8116c89d97b4d0bdf65\`; GLOBAL_KNOWLEDGE_V1 fixed author input \`3281f16647ce1fd82b58cad5939d6a0c165aa771\`.

Mother problem: arbitrary ordered-history randomized iid tests with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon 14; minimize max expected sampling time subject to both errors <=alpha.

Established author-side exact stage89 frontier:
\[
\alpha_{89}=5172392071501613543/14900301753911083008,\quad
V_{89}=24307502088163349729/1862537719238885376.
\]
Fix A89=(11,5,4) to deterministic Q at its right endpoint, retain the previously fixed predecessor table; balancing B=(12,0,1) immediate-Q probability is
\[
s_{89}=29743962535332427/41779200000000000.
\]
Stage89 exact affine segment and right sharpness are author-proved within the auxiliary finite model. Independent Driver review and native mapping remain pending.

## New unproved stage90 candidate

The next **directional dual crossing** of the selected-action table is
\[
K_{90}=3166224876/1665893,\qquad A_{90}=(7,2,3).
\]
Here continue versus immediate Q ties at the candidate K. This locates an algebraic crossing; it is not a proved stage90 segment.

First independent work: calculate exact 680-state Bellman gaps at K90; enumerate real first-hit prefixes and P/Q masses at A90; enumerate terminal suffix words and truncated complete paths; test future cone overlap with B and any other randomizer; derive exact eP/eQ/tP/tQ perturbations without double-counting overlapping cones; balance errors for all real u in [0,1]; prove tP dominance or provide a counterexample; show Bellman primal/dual equality and right sharpness. Revalidate the inherited stopping table, do not assume its arbitrary-provenance decisions are independent checks.

Method: reuse exact rational Bellman / positive ordered-prefix BRC-like path enumeration, preserving distinct branch multiplicities and probability masses. This is an auxiliary iid model only, not a native X6/Heartbeat/P000 theorem. Publish source, checked code, proof/evidence and one next problem with real immutable readback; no invented native CLAIM, active Owner, or independent Driver approval.
