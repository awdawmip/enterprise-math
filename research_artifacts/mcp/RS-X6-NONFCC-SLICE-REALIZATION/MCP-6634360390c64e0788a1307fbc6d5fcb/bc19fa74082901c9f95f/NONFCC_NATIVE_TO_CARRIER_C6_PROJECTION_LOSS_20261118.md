# X6 signed C6 native-to-carrier projection loss (2026-11-18)

Task: RS-X6-NONFCC-SLICE-REALIZATION, immutable publication TP2-A3C8E1D754209B6F31D4. Scope: the signed 3-axis Cell graph and, **only where an FCC/K4 STAR carrier is already admitted**, its exact triangular-center quotient. For a non-STAR triple the same map is an algebraic auxiliary quotient, with no assumed physical carrier.

Let S=(i,j,k), and let W contain the 6!=720 permutations of (+i,-i,+j,-j,+k,-k), once per signed symbol. Every word closes in native Z^3. A native simple word has six distinct preterminal Cell vertices. The triangular quotient is q(a,b,c)=(a-c,b-c), equivalently the known STAR carrier-center kernel Z(1,1,1); its projected word is simple when six preterminal projected vertices are distinct.

Exact exhaustive integer-coordinate enumeration produces this complete contingency table:

| Native simple | Quotient simple | Count |
| --- | --- | ---: |
| yes | yes | 84 |
| yes | no | 108 |
| no | yes | 0 |
| no | no | 528 |

The 0 cell follows directly because q preserves equality: repeated native vertices project to repeated quotient vertices. All other counts are proven for the **finite W family** by the attached exhaustive 720-word checker. Thus 192 native simple words split into 84 quotient-simple and 108 which lose vertex distinctness under q.

Constructive counterexample: w=(+i,+j,+k,-i,-j,-k) is a simple six-Cell loop in native Z^3, but after the first three steps its quotient endpoint is q(1,1,1)=(0,0), the same as the starting quotient, while native endpoint (1,1,1) is different. Hence even a genuine native simple C6 loop does not imply a simple C6 trajectory in the existing STAR circle-carrier readout. This sharpens the native/carrier distinction beyond min-zero endpoint equality.

All 20 selected triples have the same pure native combinatorics by the S6 axis-permutation skeleton. Only the four STAR triples have the presently admitted FCC carrier geometry; applying q to FACE/PATH is a typed observer experiment, not an extension of that carrier. The result does not establish TRIADIC_CLOSURE_E dynamics, new physical carriers or a complete native rotation group.

Reproduce by Python 3 standard library: run check_nonfcc_projection_cycle_loss_20261118.py. Scientific inputs are the pinned signed X6 Cell torsor and centered 3-axis slice foundations at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Next hard-target unit: specify and test a non-STAR carrier relation/compatibility map; preserve known four STAR carrier conclusions.
