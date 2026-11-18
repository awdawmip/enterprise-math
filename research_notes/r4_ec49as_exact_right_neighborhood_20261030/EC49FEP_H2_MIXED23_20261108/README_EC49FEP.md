# EC49FEP — Minimal nine-state observer supports and H2-mixed 23-path classification

Date: 2026-11-08. Research mode: **author-side analytical derivation + exhaustive finite model + numerical MILP optimum records**, not independent Driver admission. Exact frozen science pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Native model: original six signed spatial axes (ordered steps), positive *complete* BRC keys `(x,y,z)`, nine-state deterministic observation automaton, and endpoint `(+2,0,0,0,0,0)`. Research baseline: EC49FEO `1df1dd9682b881ef6ebb3f96f599bf5ce3a849e4`, fixed-22 support family minimum 94 edges.

## 1. New analytic observer-support classification

The 9-rank observer requires every observation window to intersect four signature masks `(18,20,33,40)` in the six singleton signature alphabet `{1,2,4,8,16,32}`. A direct enumeration of the `2^6=64` subsets, eliminating proper rank-preserving subsets, yields **exactly four inclusion-minimal hitting supports**:

\[
\{16,32\},\quad \{1,8,16\},\quad \{2,4,32\},\quad \{1,2,4,8\}.
\]

This is a finite set-theoretic classification, verified independently by `EC49FEP_INDEPENDENT_AUDIT.py`. A window displaying any of 16 or 32 is called *high-bearing*. Each high-bearing horizon needs at least two paths; a low-only horizon needs at least four paths. From exact BRC positive counts of a length-`h` operation word,

\[
  x+y = h+1 + \#c+\#d.
\]

The high signature words have `#c+#d=0` by the original nine-state grammar, hence a key used for a high-bearing horizon `h` has `x+y=h+1`. **One full BRC key cannot serve as a high-bearing key for two distinct horizons.** With at most five keys and the eight horizons H2–H9, if `k` horizons are high-bearing, `0<=k<=5`, the number of distinct required operation words is at least

\[
  2k+4(8-k)=32-2k\geq22.
\]

Therefore there is no 20- or 21-word solution in this exact observer model. If equality 22 holds, `k=5` and every high horizon has precisely signatures `{16,32}`, every low horizon `{1,2,4,8}`. H2 cannot be high in such a five-key 22-word equality configuration: at H2 its 16 and 32 representatives require two distinct high keys, whereas the other four high horizons each require their own distinct high key. H3 must be high because the H2 low quartet consumes the separate key `(3,1,1)` (`x+y=4`): if H3 were low, all five high horizons would have `h>=4`, and their five mutually distinct keys would all have `x+y>=5`, requiring a sixth key. Choosing four of H4–H9 yields exactly `C(6,4)=15` fixed-22 support families already treated by EC49FEO. This derivation adds a **structural completeness argument** for that earlier 15-family partition in the minimum-word regime.

## 2. First 23-word alternative: high-bearing H2 with one mixed triple

We change one H2 high support to the 3-word mixed support `{1,8,16}` (type B) or its involution partner `{2,4,32}` (type C). The H2 words for B are exactly `de`, `ec`, `fe`, using keys `(3,1,1)` and `(3,0,1)`; C uses the original native signed-word involution `I=(c d)(f g)` and induced full-key involution `J(x,y,z)=(y+2z,x-2z,z)`. H3 has the high pair `{16,32}` and key `(3,1,1)`. Choose three additional high-pair horizons `u<v<w` from H4–H9; all other late horizons require low quartets. The path quota becomes `3+2+3*2+3*4=23`, with exactly five distinct complete keys.

The six high-pair horizons H4,H5,H6,H7,H8,H9 have respectively `(2,4,6,9,12,16)` possible full BRC keys (original `high_keys`, explicit finite grammar). Therefore the complete key-inventory census per involution half is

\[
 \sum_{4\le u<v<w\le9} m_u m_v m_w = 8732,
\]

and both types together have 17,464 inventories. Their low-quartet signature feasibility check leaves **2,562** type-B inventories and **2,562** type-C mirrors, i.e. **5,124 quota-feasible**; the remaining **12,340** fail at least one required low signature. All feasible configurations have H9 high: otherwise every available key has `x+y<=9`, but H9 needs `x+y>=10` for any length-9 word.

## 3. Exact native-prefix lower bounds for all feasible inventories

For the four possible early B variants (each includes `de,ec,fe` at H2 and one 16, one 32 word at H3), the minimum H2+H3 native signed-prefix count is **31**, while their union contains **43** signed-prefix nodes. We *give all 43 nodes free* to every late construction, which only lowers the measured cost; we charge 31 as the universally valid early lower bound.

For each depth `d` in the ordered native signed step expansion, all candidate words for every required H4–H9 (horizon, signature) group determine a finite set-cover instance. Find the exact integer minimum `m_d` of new depth-`d` prefixes that hit every group. Discarding consistency between depths and granting additional free early nodes are relaxations, so

\[
 C_{\rm native}(W) \ge 31+\sum_d m_d(K).
\]

Census program `EC49FEP_CENSUS_H2_MIXED.py` uses the pinned native word enumerator and exact bitmask set-cover dynamic program inherited from EC49FEO. Among 2,562 type-B feasible inventories, **2,558** give a certified bound `>=94` (search truncation at `>=94` is safe). The involution proves the identical result for the 2,558 type-C mirrors, covering **5,116** inventories.

Only **four** type-B inventories (and their four C mirrors) have the conservative bound 93. They share high late horizons `(H5,H8,H9)` and key inventories:

```text
(3,0,1),(3,1,1),(4,2,1),(5,4,1),(5,5,1)
(3,0,1),(3,1,1),(4,2,1),(5,4,1),(6,4,1)
(3,0,1),(3,1,1),(4,2,1),(6,3,1),(6,4,1)
(3,0,1),(3,1,1),(4,2,1),(6,3,1),(7,3,1)
```

## 4. Complete joint native-prefix 0–1 optimization for the last eight

For each of the four B inventories and all four early variants, construct an exact full-prefix 0–1 mixed-integer program using one binary `x_w` per eligible complete BRC word and one binary `y_p` for each distinct non-free signed native prefix. For every required late `(h, signature)` group `G`, impose `sum_{w in G} x_w = 1`; force `x_w <= y_{Native(w)}` and `y_p <= y_{parent(p)}` for non-free ancestors. Minimize `early_cost+sum y_p`.

The corresponding native-prefix set of any selected 23-word system gives a feasible ILP assignment of the same cost; conversely the constraints require every selected native word and all its non-free ancestors, so the objective equals the exact union of ordered signed native prefixes. This is an exact mathematical *model equivalence*, for the specified fixed inventory and early variant. The solver's optimality proof is currently **computational HiGHS evidence**, not an independently replayed rational dual/integer certificate.

All 16 models report `status=0`, `mip_gap=0`, integer primal objective equal to reported dual bound. For the four inventories, early variants 0 and 1 have exact optimal cost **101**; variants 2 and 3 have **105**. A standalone auditor `EC49FEP_INDEPENDENT_AUDIT.py` reconstructs and rechecks all **16 explicit complete 23-word witnesses / 368 paths** directly from the original signed-operation alphabet, observer automaton, endpoint, complete full keys, signed-prefix cost and rank mask requirements. All pass. Type-C counterparts inherit these native costs under the already proved involution.

**Result (bounded finite problem):** For every complete five-key inventory in this H2-mixed 23-path family (both symmetric mixed triples, all admissible choices of three late high horizons and all within-window mixed-key choices), either the required signature quota is impossible or every legal system has native-prefix cost **at least 94**. Thus none attains `<=93` within the stated family.

This result expands the previous fixed-22-path classification by an exact adjacent 23-path subfamily. The mother objective remains to construct a <=93-edge signed native-X6 witness with <=5 full BRC keys, or establish wider lower bounds. Unexamined 23-path cases include mixed triples at H4–H9; ≥24-path observer supports remain open.

## 5. Exact source, verification and preservation

- Frozen science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Previously verified native grammar modules: `EC49FEJ_SIEVE.py`, `EC49FEJ_CONSTRUCT.py`, `EC49FEJ_DEPTH_FILTER2.py`, `EC49FEK_ALT_TEST.py`, `EC49FEM_FEASIBILITY_6.py` inherited from EC49FEO proof dependencies and included in the evidence archive.
- This run's source: `EC49FEP_CENSUS_H2_MIXED.py`, `EC49FEP_JOINT_MILP.py`, `EC49FEP_SOLVE_UNRESOLVED.py`, `EC49FEP_INDEPENDENT_AUDIT.py`. Actual result files: `EC49FEP_H2_MIXED_CENSUS.json` (all 2,562 B lower-bound cases), `EC49FEP_16_JOINT_SOLVES.json` (16 explicit optimal witnesses and solver metadata), `EC49FEP_INDEPENDENT_AUDIT_REPORT.json`, plus compact `EXACT_REPORT_EC49FEP.json`.
- Mathematical status: analytic elementary lemmas plus finite integer-DP computation; last eight key configurations resolved by explicitly described integer programming and numerical HiGHS certified-optimum status. Independent *witness* validation is not independent mathematical review of 8 optimality claims.
- Official control state read (2026-11-08): current service shows `research_authority_granted=false`, task inventory `execution_authorized=false`; no native CLAIM or Result/Review authority claimed. This is an **author-side continuation**, not task-machine acceptance. P000 / protected worldview unchanged.

**Next discriminating research question:** Classify 23-path configurations in which the 3-word high mixed support appears at H4, H5, ... H9 instead of H2. Prefer the exact same depthwise set-cover screen, only invoking joint prefix optimization on remaining configurations. Compare a second direction that allows more than 23 words or alternative rank-9 supports while holding the original complete BRC key bound.