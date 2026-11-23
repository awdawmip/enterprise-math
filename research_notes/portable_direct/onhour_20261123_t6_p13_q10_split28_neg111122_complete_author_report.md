# T6 author exact finite exclusion — p13 q10 signed split(2,8), negative q-pattern (1,1,1,1,2,2)

Date: 2026-11-23.  Scientific input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`.  Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Status: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Exact domain and finite result

Positive vertical q-patterns are (2) (12 named residue choices) and (1,1) (78 nondecreasing choices), hence 90 positive rosters. Negative q-pattern (1,1,1,1,2,2) has C(15,4)C(13,2)=106,470 named rosters, in CWR source order. Thus exactly 9,582,300 original signed named pairs. They partition as 3,883,464 pairs with a common named vertical atom (allocated to previously established lower-q cancellation), and 5,698,836 pairs searched by exact integer/rational 12D GS enumeration. The latter produced 12,303,306 recursive nodes and exactly 14 affine modular-sphere witnesses. **None** satisfies both original signed mass caps of 2,331. This closes the *uncancelled finite slice*; interpreting shared-atom cancellation as a lower-order reduction remains dependent on the cited earlier work.

The complete last 16,358 negative rosters [90112,106470) were executed in four disjoint slices with 1,472,220 signed named pairs, 534,438 cancellations, 937,782 exact GS searches, 2,007,785 nodes, three ball witnesses, zero legal uncanceled candidates. No negative roster remains for this q-pattern.

## Auditable exact arithmetic

Work uses the frozen original H1..H6 13-adic mixed congruences (mod 13,169,2197,28561,371293,4826809), full named composite denominators, signed q0 integer multiplicities u1..u12 and weights `13*r-1`, separate exact side caps. The homogeneous weighted q0 kernel has index `13^21` and exact positive GS length minimum `78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349`. Every candidate with both side masses bounded lies inside the stated exact GS radius. Enumeration visits the integer-nearest candidates per GS coordinate with exact rational pruning; 12D leaves are checked modulo every 13-power and reweighed from the original signed data. Named overlaps are not silently dropped: they are counted and classified as lower-order cancellation.

Three new modular-sphere witnesses in the final slice have (positive mass, negative mass) respectively **(2558,4619)** at negative index 98440, **(2177,4881)** at index 100749, and **(3299,4639)** at index 106179; the six residues are all zero, and each fails at least one side budget. Exact signed u vectors and full named atoms are in the certificate.

## Evidence and succession

- Last-slice and combined finite certificate: `research_checks/T6_P13_Q10_SPLIT2_8_NEG111122_90112_106470_AND_FULL_FAMILY_AUTHOR_EXACT_CERT_20261123.json` at `d9f7c66674b09b1d81a08316563dd63783e640dd` (readback verified).
- Prior non-overlapping ranges: [0,53248) source continuation `64861b98243c6949d1b66c9be4cac11ad11539c8`; [53248,65536) `8fb34d123ba4ff0d8ef012f544d65ebd68fa4ba5`; [65536,77824) `727e0811571bf687f800b41ece411979b040d6da`; [77824,90112) `6894f6d02e949d4ee96cf81a25f2deab3992cd29`.
- Existing author replay code `research_checks/T6_P13_Q10_SPLIT2_8_NEG111122_SLICE_REPLAY_20261123_1900.py` pinned at `ca7c63f911780e4cdb3e9f5219ee9d8cba88623c`. New segments were run in a locally reconstructed, mathematically identical exact-arithmetic version, with per-segment roster/pair SHA256 digests and local-result SHA256; an independent execution of the published file is not yet reported.

Mother T6=2332 remains OPEN; p17 q14 Native preflight, remaining p13 splits/patterns, lower primes and H0 are not resolved by this local finite exclusion. Separate Native ownership/CLAIM, semantic PROGRESS/Result, Activity author attribution and independent review remain due. Next natural q8 negative pattern for this split is (1,1,1,1,1,1,2), to be checked against current canonical continuation and overlap before execution.
