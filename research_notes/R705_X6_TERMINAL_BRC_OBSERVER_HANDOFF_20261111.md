# R705 research handoff — terminal Port BRC observer hierarchy

Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / `TP2-8B7E13C5904A2D6F1142`; immutable science `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Previous: R704 PR #2025 (`4112fd8d076cf03f7040960803d7cb6e48a7f84c`).

Author theorem: for static terminal-only Boolean gates, count plus r named last-axis bits gives per-endpoint classes 2^r(4-r), r=0,1,2,3. With 160 endpoints, optimal global exact encodings are 320, 414, 480, 480 bits. Two named gate observations plus total count recover all three terminal gate memberships and hence the ordered source mask. One named observation differentiates an explicit equal-histogram pair (2 vs 0 source paths at axis 0). The observer family is S6-equivariant if its query addresses co-transform; the stabilizer S3 precludes a natural intrinsic nontrivial axis-subset selector.

Validation: exact Python `experiments/R705_TERMINAL_GATE_OBSERVER_VERIFY_20261111.py`; evidence `experiments/R705_TERMINAL_GATE_BRC_OBSERVER_EVIDENCE_20261111.json`; test marker `R705_TERMINAL_GATE_BRC_OBSERVER_LATTICE_EXACT_PASS`; 960 paths, 480 terminal-gate source pairs, 17,280 S6 covariance checks.

Next: consult pinned actual X6 Link/Port, V29 PASS/TRANSFER, V39 j sources; either construct two genuinely realizable native packets with same count/different named gate behavior, or compute the smaller reachable quotient. Build a separate Cell-attached typed TRIADIC_CLOSURE_E update and rotate with actual source generators. Frozen science, formal CLAIM and independent Driver review remain separate.
