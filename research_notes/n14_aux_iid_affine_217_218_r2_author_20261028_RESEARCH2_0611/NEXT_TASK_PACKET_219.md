# Stage219 exact primal continuation — unproved, not admitted

Read proof PROOF_STAGE217_218.md, immutable exact certificates certificate217.json and certificate218.json, dual-only first-switch certificate219_dual.json, and actually executed REPRO_STAGE217_218.py. The prior stages are author-level proof, not independent mathematical admission.

External ternary IID N=14: P=(3,1,20)/24, Q=(2,2,20)/24; complete ordered-history randomized stopping; eP,eQ<=alpha, minimize max(tP,tQ).

Frozen right endpoint:
alpha218=7505060794177169429/21035720123168587776;
V218=4093942756303281817/438244169232678912.

Stage219 *dual-only*:
K219=314587800/3377071;
H219=28050139715601809024924983/369995418708693051506688;
new tie T=(9,4,3), Q/continue, and terminal Z=(14,0,0), P/Q.
Bellman: 680 states, 1238 positive action gaps, min 7442425/1641256506. H219=H218+2*alpha218*(K219-K218) where K218=590392/6235. Exact right-side strictness of fixed Stage218 support is established; Stage219 primal has not been established.

Next: (1) enumerate all four tie policy corners using exact Fraction suffix DP and a separate full ordered-history positive-integer P/Q mass DFS, preserving branch provenance; (2) compute mixed coefficient and prove/disprove its zero by path ancestry; (3) solve balanced-coin equation eP=eQ and derive its maximal *real* admissible parameter interval, including irrational values; (4) verify increasing equal-error alpha and positivity of tP-tQ, predecessor endpoint equality, dual-primal contact; (5) prove the full-real interval or give exact rational obstruction; (6) only then scan Stage220 dual. Do not relabel the dual-only finding as primal.

Source pin of this packet: GLOBAL_KNOWLEDGE_V1 main@d9859d053564a0c5b87ad606d6a885f85780880d; Enterprise Math main@d69d13f84e26004821ff24936d750088065c4975; P000 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Keep project P000 X6 and joint observer preservation binding, and preserve all existing authors, active owner and claim boundaries. Native CONTROL_QUOTA prevents authoritative owner confirmation from this run; portable work is UNREVIEWED/NOT_ADMITTED.
