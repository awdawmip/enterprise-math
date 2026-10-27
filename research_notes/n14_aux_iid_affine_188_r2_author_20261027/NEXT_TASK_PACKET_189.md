# Stage189 portable next task — X and T tied; exact dual-only candidate

Frozen model: independent ternary N14 IID with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), arbitrary history-dependent randomized stopping at n<=14 and dual/primal definitions in adjacent Stage188 proof. This is an **external auxiliary model**.

Author-level Stage188 exact full-real endpoint:
`alpha188=9370003598922725167379/26711406663770723844096`, `V188=1153476444134184737662789/106845626655082895376384`. Stage188 four-corner, DFS and legal randomization proof are finished; do not rerun without discrepancy.

Stage189 **dual-only** weights and Bellman root:
`K189=241967493/1388612`, `L189=59424392/347153`, `H189=209137371682549614928313/1584768521683668566016`. Bellman exact sweep: 680 states, only `X=(8,0,1):Q/C`, `T=(13,6,4):Q/C` ties, 1238 strictly positive competitor gaps, minimum `66370340952961/3582466457075712`. Stage188 endpoint policy attains the new dual root.

**Immediate scientific unit:** Compute the four deterministic corner observation vectors O(x,t) for Q-vs-continue choices at X and T under (1) rational suffix DP and (2) independent unmerged ordered-path integer-weight DFS. X can precede T, and the mixed term in `O=B+xDX+tDT+xtC` must be measured, not assumed zero. Count T first-hit histories through X with preserved P/Q masses. Derive exact error balance x(t) or t(x), legal coin interval anchored at Stage188, time dominance, full-real optimality and strict support sharpness for every history-dependent policy, or give the first precise rational obstruction. A Stage190 dual scan follows only after a proved Stage189 endpoint.

Evidence: exact P/Q branch masses, 680-state Bellman constraints, four corners, nonzero/zero cross-term witness, full DFS node accounting, exact monotonicity and legal bounds, proof/source/checker/log. Save to the research branch with immutable readback and an explicit scientific admission boundary. Preserve P000 and real owner/CLAIM gates; no native-X6 transfer inferred. Reuse BRC positive-rational carrier and order/path provenance.
