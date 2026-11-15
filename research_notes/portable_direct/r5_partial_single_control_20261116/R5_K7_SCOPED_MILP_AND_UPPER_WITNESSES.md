# R5 k=7: scoped single-control MILP and exact source-labelled upper witnesses

Date: 2026-11-16 (Asia/Shanghai). Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

This exploratory computation continues the exact k=5 and k=6 single-control constructions. In the same genuine source-labelled cycle-of-triangles model, let k=7, q(u)=sum of cyclic adjacent products, additive slack s=2, and allow only named Set_0(0/1) control.

Three finite MILP instances produced zero solver-reported gap under SciPy 1.17.0 / HiGHS:

| Controller/cover class | Reported optimum | Selected source centres |
|---|---:|---|
| static canonical source outputs L(v) | 17 | 43,47,53,59,63,75,86,87,93,94,106,109,111,118,123,125,127 |
| maximal future-safe belief controllers B_r | 19 | 45,46,47,54,55,61,85,90,91,94,95,108,109,118,119,122,123,126,127 |
| inert single-node controllers, 32 bit-flip pairs | 24 | 43,47,55,59,63,75,79,83,85,87,91,93,95,101,103,107,109,111,115,117,119,123,125,127 |

All selected upper witnesses are checked by exact integer set inclusion, raw-state coverage and (for maximal-belief controllers) named reset containment; see `R5_K7_SINGLE_CONTROL_MILP_PROBE.py` and `R5_K7_SINGLE_CONTROL_MILP_EVIDENCE.json`.

**Evidence boundary:** The static and inert MILP instances use the complete canonical source dictionary, so these are solver-supported exact finite optimization candidates; their lower bound is currently the solver's numerical proof of optimality, without a separate integer-verifiable dual certificate. The *future* MILP searches only states of the form `B_r={u<=r:Delta_{J={0}}(r,u)<=2}` with a single maximal source-centre belief for each r. It establishes a genuine **19-state explicit controller**, and reported optimality **within this enumerated maximal-belief class**. The unrestricted controller may use proper nonmaximal beliefs and remains unresolved.

In particular, k=7 has a static candidate of 17 source outputs versus a known 19-state adaptive upper construction. The gap is an exact next research target, not evidence that 17 dynamic states are impossible. It is consistent with the rigorously proved k=5 dynamic=static=7 versus inert=8 and k=6 dynamic=static=10 versus inert=13.

P000 and ACTIVE native X6 worldview remain unchanged; this is an explicitly auxiliary source-labelled observer. Mathematical review NOT_REVIEWED. Historical contributor provenance `EM-DIRECT-B78E55`, Activity `RA-33C87C2B703418F0706695E9`; formal Task/CLAIM authority not established.

**Next:** Add carefully selected nonmaximal source-belief candidates to the k=7 dynamic set-cover/transition MILP, seek a fully integer-checkable lower or constructive witness for 17 or 18, and only then formulate an unrestricted theorem.
