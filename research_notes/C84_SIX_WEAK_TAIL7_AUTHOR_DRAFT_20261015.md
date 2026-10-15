# C84 | Exact six-weak GF(2) spectrum and seventh-order TP2 bound (UNADMITTED)

Status: AUTHOR_EXACT_SELF_CHECKED / NOT_ADMITTED / NO_CLAIM. Date: 2026-10-15. This is an **auxiliary classical positive-weight BRC** finite computation, **not** a theorem about the native Heartbeat X6 Cell, C46, or quantum amplitudes. No native X6 embedding/readout/future-operation preservation has been proved; P000 unchanged.

## Frozen authority and inputs

GLOBAL_KNOWLEDGE_V1 main@14cb7de3fcfbd412755906faefc8e038fd5fbce6; EM main@7317568f2eca4aa89fa2f22266f390e5f07b6b5d. Frozen C83 portable input is `c83_graph_factors.tsv`, SHA256 `4017bb843a44df18ff68ce9536d1af12f009968cf387abe32f2813307d33dd98`, 76 non-core characters from C68 graph. Four strong faces: 8,11,44,61 (weight 1/2 each); free ports: 86,111; 70 weak faces, including anchors 89,118. Source shared with C80/C83; **not an independently reconstructed graph**. The core has 48 bits and conditional character dimension 45.

Let `Z_c(x,y)=A_c*x*y+B_c*x+C_c*y+D_c`, with `x,y>1`; `p=t_89*t_118`. Retain the full 76-factor joint GF(2) character structure and core sign provenance. All 70 weak parameters vary independently, `0<t_f<=R`.

## New exact degree-six enumeration

Among all `binom(70,6)=131115985` distinct weak six-sets and 16 strong subsets, matched the four coefficient characters and retained *every* matching weak subset, strong subset, and core parity mask.

| coefficient | strong degree 0 | 1 | 2 | 3 | 4 | matches | weighted absolute degree-six mass |
|---|---:|---:|---:|---:|---:|---:|---:|
| A |62|0|172|0|62|296|871/8|
| B |0|102|0|102|0|204|255/4|
| C |0|110|0|110|0|220|275/4|
| D |40|0|88|0|40|168|129/2|

**888 matching records**, checked exact-record equality using two different exhaustive MITM partitions: 3+3 and 2+4, with sorted-index splits uniquely covering all six-sets. This is exhaustive character matching, **not** a claim of 131115985 brute-force iterations. The independent 2+4 decomposition builds 2415 pairs and 916895 quadruples; its 888 masks and strong subsets match all 3+3 records.

## Tail bound / conditional theorem

For `0<R<8/63`, put `T7(R)=(81/16)*binom(70,7)*R^7 / (1-(63/8)*R)`. The total absolute weight of 16 strong subsets is `81/16`, and the ratio between consecutive binomial weak-degree upper budgets beyond degree seven is at most `(63/8)*R`; thus this bounds all unknown degrees >=7 rigorously.

Define
```text
a7 = 15/16 - 5R^3 - (173/8)R^4 - (235/8)R^5 - (871/8)R^6 - T7
b7 = (5/8)R^2 + (33/16)R^3 + (5/2)R^4 + (203/8)R^5 + (255/4)R^6 + T7
c7 = (5/8)R^2 + (25/8)R^3 + (25/8)R^4 + (125/4)R^5 + (275/4)R^6 + T7
e7 = (5/4)R^3 + (59/16)R^4 + (95/8)R^5 + (129/2)R^6 + T7
pcrit7 = (16/15)*(e7 + b7*c7/a7)
d7 = (15/16)*p - e7
```
Conditional on the C80 degree<=2 parity lemma and existing frozen graph, whenever `a7>0` and `p>pcrit7` the uniform exact bounds satisfy `a7*d7>b7*c7`; thus every feasible 48-bit core satisfies

`sgn(A_c*D_c-B_c*C_c)=(-1)^(c_18+c_19) != 0`,

i.e., TP2 or reverse TP2 of the two-port **positive-weight auxiliary partition function**. No statistical independence assumption; no claim this sufficient condition is optimal.

Exact Fraction certificates confirm three genuinely new independent-parameter boxes:
* `R=1/250`, anchors each `>=1/1500`: positive determinant margin about `2.1837424121e-7`. This **strictly contains** the C83 display box `R=1/350`, anchors `>=1/1500`.
* `R=1/120`, anchors each `>=1/170`: margin about `1.2718868163e-5`.
* `R=1/100`, anchors each `>=1/110`: margin about `9.6529168876e-6`.

C83 coarse degree-six tail certificates are **negative as proof margins** for all three expanded boxes; they do not represent actual sign flips. Exact rational numerators, denominators, 888 individual records, independent programs and C83 frozen input are preserved in the C84 portable evidence package accompanying this conversation (not automatically published to Source).

## Evidence and next task

Executed and locally passed:
`c84_sixweak_mitm33.py` -> `c84_sixweak_exact_spectrum.json` (888 matches);
`c84_sixweak_audit24.py` -> `c84_independent_24_audit.json` (888 record-for-record matches);
`c84_tail7_certificate.py` -> `c84_exact_tail7_certificate.json` (5 exact positive boxes, includes C83 comparison).

Limitations: both enumeration programs share frozen C83/C68 table; no independent graph reconstruction, no independent mathematical Driver acceptance, no native CLAIM or Source Result. This note is a **draft-research evidence frontier**, not a task/review/Working Truth/Foundation artifact.

Smallest open step C85: compute degree-seven reachable character spectrum or derive cancellation-sensitive signed bounds from the 888 degree-six records; seek a nondegenerate certified box with `R>1/100` and anchors strictly below `R`. Independently reconstruct all 156 integer edges and 142 faces from the model definition and compare fingerprints. A genuine sign reversal requires exact `A*D-B*C<=0` on the full 76-factor model, not merely a negative certificate margin.
