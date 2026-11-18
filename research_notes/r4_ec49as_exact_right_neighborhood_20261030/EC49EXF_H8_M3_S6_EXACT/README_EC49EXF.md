# EC49EXF — Exact eight-window minimum-edge theorem at three symbolic BRC cache keys

**Date:** 2026-11-03 (Asia/Shanghai). **Classification:** AUTHOR_FINITE_EXHAUSTIVE_PROOF / INTEGER_OR_MASK_DP_PASS / INDEPENDENT_NATIVE_WITNESS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. **Parent:** EC49EXE, immutable `71d4df8126df03beda2980badbfddfeabfe79472`, Draft PR #1730.

**Frozen scientific input pins:** GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Behavioral rules were separately checked at current canonical `main` on 2026-11-03: global `f697bd1909b684251aa9937b6831ece8bad7282d`; Enterprise Math `aa0bfca9019f367b426577257033363e0718ed52`. P000, ACTIVE worldview, task source firewall and mathematical admission state are unchanged.

## 1. Precise theorem and original model

Fix the seven native signed-X6 operation words in the existing finite symbolic model:

```
a=(-1,-1)          b=(-2,-2)          c=(+1,+2,-1,-2)
d=(+2,+1,-2,-1)   e=(+3,+1,+1,-3)   f=(+1,-1)   g=(+2,-2)
```

For every horizon `h=2,...,8`, choose a set of ordered h-operation words whose expanded signed native X6 path ends at displacement `(2,0,0,0,0,0)`. All chosen words of a horizon must share the same **complete six-axis positive primitive-count key** `p_h`. The stacked nine-history-to-five-bucket observer (buckets `N,A,B,AB,BA`) must have rank nine over Q at every horizon. Preserve complete ordered signed primitive paths, observer histories, branch identities and symbolic strictly-positive paired BRC factors `X_p=product_i x_i^(p_i), Y_p=product_i y_i^(p_i)` separately. `E` is the cardinality of the union of nonempty **native signed primitive-step prefixes**, `M` is the number of globally distinct complete BRC keys, and `S` is the number of distinct nine-to-five transfer signatures used anywhere.

**Theorem EC49EXF-1.** In this complete finite operation language,

\[
\boxed{\min\{E\mid H=8,\ M=3,\ S\le6\}=112.}
\]

It is attained by a real path family with `(E,M,S)=(112,3,6)`. The already proved H8 minimum-memory result establishes that `M=3` itself is the smallest feasible number of positive BRC keys.

## 2. Finite universe and observer reduction

Operation `b` has net native displacement `(0,-2,0,0,0,0)` while the other operations contribute zero on native axis two; thus `b` is excluded from every returning word. Operations `a` and `e` contribute `-2` and `+2` on native axis one respectively, so return requires `#e=#a+1`. All remaining operations have net zero native displacement. Consequently enumerating `a,c,d,e,f,g` with this exact occurrence equation is exhaustive.

Complete returning operation word populations at horizons 2 through 8 are **8, 51, 304, 1,770, 10,224, 58,947, 340,064**, for a total of **411,368**. The union has exactly **11** distinct history-transfer signatures. The unique rank-nine positive key at h2 is `p0=(3,1,1,0,0,0)`, requiring the four words `ce,de,ec,ed`, four signatures `T4={1836687,1867942,1872656,1873981}`, and 28 native prefix edges. Its nine-history observer rank is exactly nine.

There are seven further possible transfer signatures. Among their 21 unordered pairs, **only** `T2={1836425,1866380}` has rank nine by itself. For every fixed horizon/key fiber among h2..h8, direct exhaustion proves: under global signature set `T4 ∪ Q`, `|Q|≤2`, a full-rank fiber requires either all four `T4`, or (only when `Q=T2`) both `T2`. No mixed fiber is full rank without meeting one of these two conditions. Every rank-nine claim here is tested exactly by modular integer row reduction over `F_1000003`; Hadamard bounds any 9-by-9 0/1 minor by `3^9=19683 <1000003`, so rank nine over this field is equivalent to rank nine over Q for these observer matrices.

For each all-`T4` non-`T2` pair, the already-established H7 three-key optimum within that all-`T4` class has E7 at least 116 (EC49EU). Appending a new horizon needs at least four distinct primitive terminal edges, so such families have E8≥120. Other admissible global signature arrangements are contained in the unique `T2` pair class.

## 3. Exact reduction from all H7 schedules to fourteen H8 instances

At horizon eight with `M=3`, the first seven horizons use either two or three keys. With two keys, the inherited strict H7/M2 bound gives `E7≥116` (EC49ET), and every valid new horizon contributes at least four new primitive suffix edges; hence `E8≥120`.

With three keys in the first seven horizons and the `T2` pair allowed, the inherited **complete** EC49EV H7 exact report lists **465** possible horizon-key/signature-pattern schedules, including the three all-T4 cases. It is preserved in the immutable EC49EV evidence file `EC49EV_EXACT_EXECUTED.json.gz.b64` (author-side source `7e2324bbaaaa546829bdc3180243cd72f9be84b3`). The new H8 enumeration checks each reported schedule's three keys against every rank-nine h8 fiber. Exactly **270** schedules admit H8 with one of their existing keys.

**Terminal-prefix lemma:** Each chosen new h-operation word has at least two primitive steps belonging to its last native operation, which cannot already be part of any shorter complete-operation-word path. At a fixed horizon, words with the same complete positive-count key have distinct final two primitive edges: if the words differ earlier, their native prefixes are disjoint from the divergence onward; if only the last operations differ, those operations have equal positive counts and different first signed primitive steps (the only repeated positive-count operation classes are `{a,b}` and `{c,d}`). Thus two essential words add at least **four** new primitive edges, while four essential words add at least **eight**. This argument uses the prefix-free native operation codes and applies independently of prefix sharing at earlier horizons.

For each of the 270 extendible H7 schedules, add `+4` if H8 has a two-`T2` solution or `+8` if H8 requires the four-`T4` solution. All but **14** schedules have an inherited strict lower bound already at least 112. The 14 remaining schedule IDs are `9,11,47,50,76,79,83,119,159,163,191,195,200,232`; each permits a unique H8 key and requires the two `T2` signatures. Their complete exact native-prefix optimizations are:

| H7 case ID | Strict H7 cost | Exact H8 cost | Native trie nodes | Terminal colors |
|---:|---:|---:|---:|---:|
| 9 | 102 | 114 | 4,778 | 18 |
| 11 | 102 | 114 | 9,156 | 18 |
| 47 | 100 | **112** | 9,156 | 18 |
| 50 | 100 | **112** | 9,156 | 18 |
| 76 | 106 | 114 | 4,212 | 18 |
| 79 | 106 | **112** | 7,370 | 18 |
| 83 | 106 | 114 | 7,370 | 18 |
| 119 | 106 | 126 | 9,156 | 20 |
| 159 | 102 | 114 | 9,156 | 18 |
| 163 | 102 | 114 | 4,778 | 18 |
| 191 | 106 | 114 | 7,370 | 18 |
| 195 | 106 | **112** | 7,370 | 18 |
| 200 | 106 | 114 | 4,212 | 18 |
| 232 | 106 | 126 | 9,156 | 20 |

Every cost is obtained by the **integer OR-mask dynamic program on the complete signed-native primitive trie**, not by path-token compression, heuristic sampling or a floating-point termination test. For each node `v`, `DP_v[mask]` minimizes the number of non-baseline edges in the subtree used to realize `mask` terminal colors. For each child `u`, update

`new[mask OR t] = min(new[mask OR t], DP_v[mask] + DP_u[t] + (t!=0 and edge(v,u) not prepaid))`.

Root initialization is empty mask with cost zero; legal terminal nodes contribute their declared color mask at zero local cost. Induction over child subtrees and the OR of covered colors proves the recurrence gives the exact minimum over every selection of legal native paths; paid h2 prefixes contribute 28. All fourteen native integer DP runs return `PASS`, with state masks up to `2^20`, and values exactly as in the table. Independently formulated SciPy/HiGHS 0–1 integer programs return the same 14 optima and zero reported gap; the exact integer DP is the mathematical finite proof kernel.

The above cases cover every H8/M3/S≤6 solution, hence **E≥112**.

## 4. Explicit 112-edge attaining native construction

| Horizon h | Selected original operation words | Common complete positive BRC key |
|---:|---|---|
| 2 | `ce`, `de`, `ec`, `ed` | `(3,1,1,0,0,0)` |
| 3 | `feg`, `gef` | `(3,1,1,0,0,0)` |
| 4 | `fegd`, `gefd`, `gefc`, `fegc` | `(4,2,1,0,0,0)` |
| 5 | `fegfg`, `geffg` | `(4,2,1,0,0,0)` |
| 6 | `fegdgd`, `gefdgd`, `gefcgc`, `fegcgc` | `(5,4,1,0,0,0)` |
| 7 | `fegdggf`, `gefdggf`, `gefcgfg`, `fegcgfg` | `(5,4,1,0,0,0)` |
| 8 | `fegfgfgg`, `geffgfgg` | `(5,4,1,0,0,0)` |

An independently written JavaScript checker reconstructs every ordered signed primitive path, all six native displacement and positive components, all nine histories, each horizon's exact rank and the primitive-prefix union. Its actual execution report is `PASS`, exactly `(E,M,S)=(112,3,6)`, with nine-dimensional rank at every horizon. Hence **E≤112**, completing the proof.

Relative to the EC49EXE eight-window bound `E≤120`, the strict optimum reduces edge cost by **8** (6.67%) at the same minimum three BRC keys and six observation signatures.

## 5. Evidence and reproduction

- `ENUM_EC49EXF_WORDS.cpp`: independent signed-step and nine-history operation enumerator for h2..h8, generating the complete 411,368-row CSV with six-axis key, transfer signature, original operation word and horizon.
- `REPLAY_EC49EXF.py`: rechecks every return displacement/key, the 11-signature/21-pair rank reduction, the exact inherited 465-case EC49EV report, the 270/14-case reduction, generates all fourteen full signed-prefix trie files and executes the exact integer kernel.
- `VERIFY_EC49EXF_OR_DP.cpp`: exact 64-bit integer subset-OR dynamic-programming kernel, unchanged from the immutable EC49ET source where its induction invariant was established.
- `VERIFY_EC49EXF_INDEPENDENT.js`: independent concrete witness and exact rank/prefix check.
- `EC49EXF_FULL_EXACT_EXECUTED.json` and `H8_14_EXACT_DP_EXECUTED.tsv`: actually executed complete fourteen-case results; `EC49EXF_INDEPENDENT_EXECUTED.json`: actual witness check output. `SHA256SUMS_EC49EXF.txt` records payload integrity. Big generated trie inputs and the CSV can be reproduced from the retained source. The original H7 report is an unchanged, immutable predecessor artifact rather than a new mathematical assumption.

Local replay (C++17, Python 3, Node.js):

```
g++ -O3 -std=c++17 ENUM_EC49EXF_WORDS.cpp -o enum_words
./enum_words > ALL_RETURN_WORDS_H2_H8.csv
g++ -O3 -std=c++17 VERIFY_EC49EXF_OR_DP.cpp -o verify_dp
python REPLAY_EC49EXF.py ALL_RETURN_WORDS_H2_H8.csv EC49EV_EXACT_EXECUTED.json.gz.b64 ./verify_dp evidence/
node VERIFY_EC49EXF_INDEPENDENT.js
```

The preserved predecessor archive `EC49EV_EXACT_EXECUTED.json.gz.b64` is located in the immutable EC49EV GitHub artifact directory. The generated CSV and 14 trie instance text files are derivable deterministic execution inputs; use the H7 frozen report unchanged. Science pins remain the above immutable pair; current normative rules are independently refreshed. This is a rigorous finite-model result under the defined symbolic paired BRC keys and native-path observation map, with no separate claim about actual Heartbeat physical dynamics, numerical BRC implementation or experimental residuals.

## 6. Real source state and next question

Authenticated GitHub identity: `awdawmip` (repo admin/push). On the 2026-11-03 native service check, Enterprise Math gateway v0.6.11 reported `research_authority_granted=false`, and the authenticated task-owner inventory request returned `CONTROL_QUOTA`. Therefore activity owner is **unconfirmed** and the author-side result is **portable/unreviewed/not admitted**; no formal CLAIM, Result or independent Driver acceptance is asserted. P000 and ACTIVE worldview have not been modified.

**EC49EXG:** Determine exact eight-window tradeoffs at `M=4,S≤6` and `M=3,S≤4`, using this optimum `(112,3,6)` and the existing all-H four-signature optimum `(76,7,4)` as anchors. Reuse the 11-signature fiber reduction, prefix DP and lower-dimensional key-support theorem; seek new nondominated finite-model tradeoff points before assembling the complete H8 Pareto frontier.
