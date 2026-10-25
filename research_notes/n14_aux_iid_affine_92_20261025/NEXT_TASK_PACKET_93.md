# Stage93 portable research handoff — exact candidate, not proof

**Mother question:** Minimize the maximum of the P/Q expected sample counts over every ordered-history randomized sequential iid test T<=14 under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), with both errors <= alpha. Preserve exact separately labelled P and Q rational prefix weights, branch order, and terminal suffix multiplicity.

**Current verified author-side frontier:** Stage92 proves the full interval with alpha92=5172457130453937143/14900301753911083008, V92=24277747388885024249/1862537719238885376, balancing randomization s92=27568725674091547/41779200000000000 at B=(12,0,1). The Stage92 endpoint fixes A92=(12,8,3) to immediate P. Stage91 A91=(6,0,2) is fixed to immediate Q. Preserve earlier endpoints and their original proofs. Reuse unchanged derive88.py -> derive89.py -> derive90.py -> derive91.py -> derive92.py. These are exact author-side finite iid proofs, not independent Driver acceptance.

**One next unproved unit:** Test the exact Bellman-dual crossing
\[
K_{93}=\frac{36260219477628}{21860934947},\qquad
A_{93}=(5,4,0),\quad C\sim P\ {\rm (candidate)}.
\]
First verify the full 680-state Bellman gaps with the Stage92 endpoint policy. Enumerate nominal versus genuine first-hit ordered words under both P and Q, conditional continuation errors, additional samples and terminal suffix counts. Check whether the new state can reach the balancing state B before assuming disjoint cones (it has 0 symbol-1 occurrences at depth 5, whereas B has 1 at depth 12, so *intersection is possible* and must be computed); retain u*s interaction terms if any. Derive exact equal-error compensation and its feasibility, the true tP/tQ maximum, attainable full real-alpha interval, universal Bellman support, and the right-end sharpness. If it fails, record a rigorous obstruction and next neighboring action.

**Required deliverable:** Complete finite-model proof or explicit counterexample/no-go; exact runnable standard-library arithmetic; ordered DFS audit; reproducible rational certificate; source + immutable readback and next research problem. The native P000 premise holds, but this external iid model has no established faithful BRC/X6/Heartbeat transfer. No native active Owner, formal CLAIM, frozen Result, or independent Driver acceptance can be inferred from this handoff.

**Source:** Stage92 author proof + exact code in research_notes/n14_aux_iid_affine_92_20261025/; inputs pinned GLOBAL_KNOWLEDGE_V1 50e22254dac1b15435eed58a6ad87a3e9b8627f0, EM 0c20646ad4d9fa5345dcdbc28c35fdf52a2bc5d7 and prior Stage91 immutable source 966d52251166b4d17ea861ea4374639669abbee9. Native tool results: control CONTROL_QUOTA; researcher session start STATIC_READONLY_SCOPE_DENIED operation_sent=false.
