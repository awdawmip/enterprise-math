# EC48J — Beyond the six-cycle: sharp seedless memory separation

**Verified author-side frontier (EC48I, 2026-10-27):** For a finite positive two-stage ROC observer with private history encoding and no persistent common seed, the model

```
P_raw = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], sum=36
Q_raw = [[2,2,2],[2,2,2],[2,2,2],[2,2,2],[2,2,2],[2,2,2]], sum=36
```

has `K_hull=3` but **`K_seed=4`**. At critical ratio `r=1`, the optimal-history compatibility graph is `C6`, and every optimal K=3 encoder partitions it into one of two perfect matchings, forcing all six tied bits to 0 or all to 1. The full zonotope face has `(alpha,beta)=(1/2+z,1/3+z)`, `z∈[0,1/3]`; K=3 realizes only `z=0,1/3`. The rational point `(2/3,1/2)` is therefore a strict nonattainability certificate. An explicit six-phase four-state policy traverses all tied masses with interval increments 1/18; two other critical faces need three states; reflection and star-shapedness give full `S4=Z`. The direct proof does not depend on the encoder-component graph theorem.

**Source bundle:** `research_notes/r4_ec48i_six_cycle_20261027/EC48I_SIX_CYCLE_GAP_THEOREM.md`, `EC48I_VERIFY.py`, `EC48I_REPORT.json`, and this file at one immutable GitHub research commit. Exact code checks 729 K3 / 4096 K4 encoders, and a complete 13,570-case abstract sign-pattern audit for a bounded 3-label, 3-memory setting. The computational bounded result is not a proof for unbounded history/future alphabets.

**First next problem:** For arbitrary positive source measures and K_hull=k, improve the prior general `K_seed<=2k` upper bound in terms of the graph of feasible (lower,upper) binary words. Investigate whether the six-cycle is a minimal obstruction for a sequence of `k`-ary source/target incidence graphs and whether `K_seed<=k+1` is possible when future-label count is three. A useful output is either a constructive theorem with fully specified memory-slot scheduling or a new rational counterexample with strict interval lower bound and exact normalization. Avoid recycling the resolved conjecture `K_seed=K_hull` as if still open.

**Independent review obligations:** Re-derive the 3-state lower bound from the convex constraints, independently validate the six-phase schedule (not just a checksum), and check the finite enumeration assumptions and duplicate-row synchronization. Do not claim native formal Result, independent Driver acceptance or native-X6 consequence until authorized review and embedding proofs exist.

**Provenance:** `RA-EMR4-20261027-1215-EC48I-SIXCYCLE`; GLOBAL_KNOWLEDGE_V1 main@cc9bb8a39531f5b6dc06133d6575cf6f48d21a17; project main@713861ee37a8e027afa8843141a768d55f072547 at research initiation. Native owner query returned CONTROL_QUOTA and native session start STATIC_READONLY_SCOPE_DENIED (operation_sent=false); local Researcher-ID `EM-R004-EC48I-20261027-1215-LOCAL`, no task CLAIM.
