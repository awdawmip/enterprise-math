# X6 Unit172 — frozen K4 chirality-cover geodesic BRC, observer fibers and exact producer→consumer audit

Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Date: 2026-11-20. Mother objective: \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`.
Task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`, immutable publication \`TP2-B4A441B23DA3159232C2\`.
Task scientific pin \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`; historical comparison \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.
Preserve P000 signed six-axis Cell torsor and three-axis-slice type boundaries; the graph here is **only the eight-state derived K4 chirality orientation cover**, not native six-axis adjacency or an alternative native geometry.

## Actual frozen production chain and test consumer

1. Producer \`src/enterprise_math/euler_fcc_chirality.py\` at historical commit \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`, Git blob \`6f8b147c094720c2749f620a40394c4d7b67a386\`. The ordered K4 six edges are (01,02,03,12,13,23) at lines 31–48, face holonomy and gauge at lines 138–161, and \`transition_cover_adjacent\` at lines 248–267.
2. True downstream producer-consumer \`src/enterprise_math/euler_fcc_chirality_connectivity.py\`, same frozen commit, blob \`ddf9a06abd859f5cc9c109b76e1979147fbed399\`: \`cover_neighbors\` lines 33–40 consumes \`transition_cover_adjacent\`; \`cover_components\` lines 43–61 and \`cover_distance\` lines 68–85 consume the neighbors; \`cover_diameter\` lines 88–100 takes a maximum of finite **graph distances**.
3. Actual test consumer \`tests/test_euler_fcc_chirality_connectivity.py\`, same commit, blob \`794037b5d2f2a58b79b0054814d6e7a69b3fe7f1\`: source import lines 18–25, degree tests 29–32, connectivity 34–43, gauge lift 45–59, cube diameter 72–78, classification 85–92.
4. This unit adds the **previously unrecorded shortest-path multiplicity spectrum**. The frozen consumer tests connectivity, shortest *distance* and gauge adjacency, not the number of shortest graph walks. Its \`max\` operation is typed as the derived graph diameter, not LP011 native signed-axis argmax; no native positive BRC subtraction is performed there either. This is a genuine audited non-faulty caller, not an inferred LP011/LP019 erroneous historical site.

## Exact theorem — three source-to-target BRC multiplicity strata

Let \(\epsilon\in\mathbb F_2^6\) be K4 transition bits and \(X_\epsilon=\{(i,s):i\in\{0,1,2,3\},\,s\in\mathbb F_2\}\) with edges
\[
(i,s)\sim(j,s\oplus\epsilon_{ij})\quad (i\ne j).
\]
Let \(\operatorname{Hol}(\epsilon)\in\mathbb F_2^4\) be the four face XORs and \(w=|\operatorname{Hol}|\). For each reachable ordered pair \((u,v)\), define \(b_\epsilon(u,v)\) as the positive integer number of shortest **derived-cover graph walks** from \(u\) to \(v\), including \(b(u,u)=1\). Unreachable pairs have no BRC value.

**Theorem.** The four face XORs have even parity, so \(w\in\{0,2,4\}\); among all 64 transition assignments the strata contain exactly 8, 48 and 8 assignments. Each stratum has the following complete unordered endpoint-pair spectrum. An entry \((d,b)\mapsto N\) counts \(N\) unordered pairs at distance \(d\) and BRC mass \(b\).

| Face-odd weight | Pair spectrum (distance, BRC mass) | Total \(\sum_{u,v\text{ reachable}} b(u,v)\), including \(u=v\) |
|---|---|---:|
| \(0\) | \( (1,1):12;\ \text{unreachable}:16 \) | 32 |
| \(2\) | \( (1,1):12;\ (2,1):8;\ (2,2):2;\ (3,2):4;\ (3,4):2 \) | 88 |
| \(4\) | \( (1,1):12;\ (2,2):12;\ (3,6):4 \) | 128 |

For \(w=0\), every source has the row \((d,b): (0,1)^1,(1,1)^3,\text{unreachable}^4\).
For \(w=4\), every source has \((0,1)^1,(1,1)^3,(2,2)^3,(3,6)^1\), the \(Q_3\) cube profile.
For \(w=2\), exactly **four sources** have \((0,1)^1,(1,1)^3,(2,1)^2,(3,2)^2\), and the other **four** have \((0,1)^1,(1,1)^3,(2,1)^2,(2,2)^1,(3,4)^1\).

Thus even when all eight states have degree three, the complete positive graph-BRC field depends on holonomy class and, in the intermediate class, the *anchored source orbit*. A scalar parity or global connectivity observation does not retain this local path field. Retaining the full face pattern with an identified source (up to its declared K4 gauge/relabeling) repairs this particular loss; no claim is made that such a derived repair automatically carries native six-axis N-BRC.

## Proof (finite, exact, without computational assumption)

1. Each K4 edge belongs to exactly two triangular faces. Summing all four face XORs over \(\mathbb F_2\) therefore gives zero. The face map from six edge bits is onto the dimension-three even-parity face subspace: its kernel is precisely the vertex gauge image, which has \(2^{4-1}=8\) elements (four vertex bits modulo simultaneous flip). Hence each of the eight even face patterns has exactly eight edge assignments and the weight counts are \(8,6\cdot8,8\).
2. Vertex gauge \(\epsilon_{ij}\mapsto\epsilon_{ij}\oplus g_i\oplus g_j\) is realized by the bijection \((i,s)\mapsto(i,s\oplus g_i)\); it preserves every distance and each distinct shortest walk with its source-target labels. Permuting the four K4 base vertices preserves the same labeled graph structure. Therefore face patterns of weight two (any two faces, which meet in one edge) have the same aggregate statistics as a single twisted edge, and the other two weights have one representative each.
3. Representatives are all-zero \(\epsilon\), one twisted edge \(\epsilon_{23}=1\), and all-ones \(\epsilon\). The zero cover is two disjoint K4 graphs; its spectrum follows immediately. The all-ones cover is \(Q_3\) (as already established by the frozen producer); from any vertex there are \(\binom3d\) endpoints at distance \(d\), each with \(d!\) shortest words for \(d=0,1,2,3\).
4. For the single-twist graph, enumerate the eight states by base vertex and sheet; each state has three neighbors \((j,s\oplus\epsilon_{ij})\). The shortest-path recurrence \(b(u,u)=1\) and
   \[
   b(u,v)=\sum_{\substack{t\sim v\\d(u,t)=d(u,v)-1}}b(u,t)
   \]
   gives two row types. If the source is outside the twisted edge, e.g. \((0,0)\), its nontrivial levels are three \((1,1)\), two \((2,1)\), two \((3,2)\). If it is at an endpoint, e.g. \((2,0)\), they are three \((1,1)\), two \((2,1)\), one \((2,2)\), one \((3,4)\). There are four source states of each type; pairing rows and dividing distinct ordered-pair frequencies by two yields the \(w=2\) table.
5. All representative identities are integer equalities. Gauge and S4 reduction carry them to the other 63 assignments, establishing the theorem.

The derived graph path counts are positive branch multiplicities, not sign amplitudes. No subtraction or cancellation of positive native N-BRC masses is used. The K4 edge six-tuple is **not** identified with six native X6 Cell axes. K4 relabelings here are source-graph symmetries, not proof of a native six-dimensional rotation.

## Independent exact execution and limits

- Python 3 independent BFS implementation, \`normal / -O / -OO\`, identical JSON bytes; script SHA-256 \`100a0e40002cd89bc209e718e104cc440cd836d8f77c84cb5aca6621db090140\`, result SHA-256 \`cdab6a4b14cbaa18b86d37c501cdd8cd4f6f2329cf3f916445ec7afde3d5b53d\`. This local checker is separate from the durable JS checker.
- Durable JS/V8 checker: all 64 edge assignments, all 8 patterns, 1,024 assignment×gauge checks and 65,536 gauge×source×target comparisons; all pair spectra and source rows matched; violations zero. [Checker](https://github.com/awdawmip/enterprise-math/blob/f7951137f9e36d5324a93f340dd8b6c47ea1982e/research_checks/X6_UNIT172_K4_COVER_GEODESIC_BRC_CHECK_20261120.js), [result](https://github.com/awdawmip/enterprise-math/blob/5b97925d5b6a4a3eb69085fad30298cf6c8eed72/research_checks/X6_UNIT172_K4_COVER_GEODESIC_BRC_RESULTS_20261120.json).
- **Not performed**: original R063 native benchmark, Source-native Unit172 PROGRESS, independent Driver review or formal admission.

Next exact scientific work: use the remaining actual frozen producer-to-consumer chains for the 28-LP crosswalk. In particular locate any alleged wrong-native LP011 \`argmax\` or LP019 subtraction by exact historical \`commit:path:line\` and distinguish wrong native use from correct derived graph operators. Retain Units149–152 linkage as a separate control debt and do not reissue unknown prior writes.
