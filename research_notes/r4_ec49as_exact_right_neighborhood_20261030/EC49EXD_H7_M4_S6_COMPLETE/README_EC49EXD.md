# EC49EXD — Exact global seven-window optimum with four symbolic BRC keys and at most six observation transfers

Research date: **2026-11-03** (Asia/Shanghai). Publication mode: **portable author-side finite exhaustive mathematical proof**, pending native role/independent review. This extends EC49EXC (`c62ceee909de245af8351684f73654a5a92a5ef0`) and resolves its explicit next scientific question EC49EXD. The attained 72-edge construction is from EC49EW; the new contribution is the complete unrestricted global lower bound and its independent replication.

**Frozen scientific input pins:** `awdawmip/chatgpt-global-knowledge@773d538180bfb49e24cffeb35c3ee75eb0628e2e` and `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The applicable behavioral rules were refreshed separately at global `main@4812a94c6de3a2342a0e959f0ef8232a1fc04a9d` and EM `main@2c66512b55a9710a58578920a20ed0aefcd517d4`. P000 and ACTIVE Heartbeat World are retained unchanged.

## The exact model

Seven operations are ordered, primitive **signed native-X6** step paths:

```
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
```

The coordinate entries above name the signed E1/E2/E3 primitive axes, with the E4/E5/E6 components identically zero in this *specified three-axis slice*. Each horizon `h=2,...,7` selects legal **operation words of exactly h letters**, each returning to full native six-component displacement `(2,0,0,0,0,0)`; all words selected at that horizon have one identical **complete six-component positive-step count vector** `p_h`. The paired strict-positive symbolic BRC monomials `(X_p,Y_p)=(∏_i x_i^{p_i},∏_i y_i^{p_i})` carry these cache keys. Actual ordered native paths and nine historical seam states are preserved as separate typed information; this is a symbolic BRC resource question, not a physical-time or phase-amplitude calculation.

Nine frozen seam-history initial states are `(N,0),(N,1),(N,2),(A,0),(A,2),(B,0),(B,1),(AB,0),(BA,0)` and outputs occupy five buckets `N,A,B,AB,BA`. Positive adjacent axis steps `(+E1,+E2)` and `(+E2,+E1)` trigger first A/B event transitions. Every horizon's selected words must yield **rational observation rank 9**. A word's complete nine-to-five transfer map is its **signature**. Let `E` be the number of distinct nonempty signed primitive **path prefixes** over all horizons; `M` the number of different complete positive keys `p_h`; and `S` the total number of different transfer signatures.

## Theorem EC49EXD-1 (global exact minimum)

Under the complete frozen model above,

\[
\boxed{\min\{E:\ H=7,\ M=4,\ S\le6\}=72.}
\]

In particular, `(E,M,S)=(72,4,6)` is **globally exact** for this resource class, rather than merely an upper bound or the previously proved `T2,T2,T2,T4,T2` signature subfamily.

### Finite-model complete coverage and rank reduction

Exhaustively generating `7^h` operation words for each h and filtering exact signed X6 displacement gives h2..h7 return-word counts `(8,51,304,1770,10224,58947)`. For each complete positive count key, exhaustive signature-subset checking and rational-rank certification prove that *every full-rank key fiber* has a **unique inclusion-minimal rank-nine signature set**, either:

- `T4` = the **four** signatures of the forced h2 words `ce,de,ec,ed`, or
- `T2` = the **two** signatures of `feg,gef`.

The full-rank `(T4,T2)` key counts at h2..h7 are `(1,0),(3,1),(7,2),(13,4),(22,6),(34,9)` respectively. No fiber has a second incomparable minimal full-rank signature set. Thus an optimum may cover only its required signatures: optional extra words increase or leave the union-prefix cost and cannot reduce the number of required signatures. The h2 fixed-vector rank-nine core is uniquely `ce,de,ec,ed`, with exactly **28** primitive prefix edges.

All remaining full-rank key fibers need T4 or T2, so any signature-family combination uses at most six distinct transfer matrices (T4 ∪ T2). Precisely **26,207** ordered key schedules `p2,...,p7` use **exactly four** distinct keys. Every schedule of the stated resource class belongs to this complete finite set.

The rank-nine decisions can be made modulo `q=1,000,003` without loss of correctness: every 9×9 minor of the nine-row 0/1 observation matrix has absolute determinant at most `3^9=19,683<q` by Hadamard. Hence rank nine over Q is equivalent to rank nine mod q. The independent checker actually re-enumerates all signature subsets, confirming the unique-minimal-set classification.

### Terminal-edge lemma (finite exact 101-fiber verification)

For every allowed later horizon `h=3,...,7`, every full-rank key fiber has a compulsory set of `k=2` or `k=4` transfer signatures. The union of all selected words realizing them contributes **at least `2k` new signed primitive prefixes beyond earlier-horizon words**.

The associated *complete finite certificate* proceeds as follows. Define `U_{h-1}` as the signed primitive prefixes of the **mandatory h2 four-word base** plus **all legal returning words** for every intermediate horizon 3..h-1 (irrespective of key or signature). This is a superset of the actually paid earlier prefixes in every admissible selection. Give any prefix already in `U_{h-1}` zero cost, any other prefix unit cost. For each of the `4+9+17+28+43 = 101` full-rank h3..h7 fibers, form the complete native signed-prefix trie for its words carrying each of the `k` essential signatures; compute the minimum new cost that covers all k signatures, using exact integer OR-mask DP. **All 101 resulting minima are at least `2k`** (`EC49EXD_TERMINAL_LEMMA_EXECUTED.json`). In particular the statement applies independently to each of h6 and h7, regardless of which BRC keys or previously selected words occur. An admissible earlier-prefix set is contained in `U`, so the true incremental edge charge is at least the optimistic minimum. This is a complete finite proof of the stated lemma within h<=7, not an arbitrary-horizon assertion.

### Exact signed-prefix trie optimization

For any fixed key schedule prefix, put **every** required `(h,signature)` word into a joint trie over its expanded ordered signed primitive axis steps, with terminal bit masks identifying the mandatory `(h,signature)` colors. Pre-charge the h2 core's 28 prefixes. At a trie node `v`, `D_v(B)` is the minimum additional integer edge cost inside that subtree needed to cover exactly the union mask `B`. The empty subtree choice has cost zero; child subtrees combine by bitwise OR and sum of their edge costs; an occupied incoming edge costs 1 unless its prefix is prepaid. An optional global cutoff prunes any intermediate partial cover already above that cutoff, as all later edge costs are nonnegative. By induction on the trie, the DP computes the exact minimum union-prefix cost for the fixed color requirements. This is a finite connected-rooted-subtree covering recurrence, not a heuristic or approximate solver.

### Complete lower-bound partition

The 26,207 M4 key schedules are partitioned without overlap into three stages:

| Stage | Number of key schedules | Sound lower-bound computation |
| --- | ---: | --- |
| Exact h2..h5 optimization | **25,995** | 426 distinct h5 key-schedule prefixes solved by exact trie DP; `E7 >= E5_exact + 2 k6 + 2 k7 >=72`. |
| Exact bounded h2..h6 optimization | **208** | Of 212 remaining schedules, 196 distinct h6 prefixes solved with cutoff 67 for h7=T2, or 63 for h7=T4; all 208 satisfy `E6+2k7>=72`. |
| Four final schedules, optimistic-free h7 optimization | **4** | Each has `E6_exact=66` and mandatory h7=T2. Give **all** earlier admissible fiber prefixes for that key schedule free; exact two-signature h7 trie DP yields `new_edges_min=6`, so `E7>=66+6=72`. |
| **Total** | **26,207** | **All schedules certified E7≥72.** |

The four final cases, abbreviating the six-component keys to the first three entries (axes 4–6 are literal zero), are:

| `p3,p4,p5,p6,p7` | h6 exact E | h7 optimistic min new | Superset free prefixes | h7 trie nodes |
| --- | ---: | ---: | ---: | ---: |
| `(3,1,1),(3,2,1),(3,3,1),(4,4,1),(4,4,1)` | 66 | 6 | 1,761 | 697 |
| `(3,1,1),(3,2,1),(4,2,1),(5,3,1),(5,3,1)` | 66 | 6 | 2,522 | 893 |
| `(3,1,1),(4,1,1),(4,2,1),(5,3,1),(5,3,1)` | 66 | 6 | 2,522 | 893 |
| `(3,1,1),(4,1,1),(5,1,1),(6,2,1),(6,2,1)` | 66 | 6 | 1,761 | 697 |

For each final case the free set is formed only from that case's mandatory h2 core and **all** h3..h6 words with the case's fixed positive key and necessary full-rank signature family. This union may be strictly larger than any actually chosen earlier-prefix forest, so making it free produces a valid optimistic lower bound. Both the Python and the independent JavaScript implementations return **six** for all four cases.

### Attaining complete-six-axis witness

The following words attain the global lower bound while retaining full signed six-component origin, BRC-key and observer-history semantics:

| h | selected ordered operation words | observer signature requirement |
| --- | --- | --- |
| 2 | `ce,de,ec,ed` | T4 |
| 3 | `feg,gef` | T2 |
| 4 | `fegg,gefg` | T2 |
| 5 | `feggg,gefgg` | T2 |
| 6 | `fegggc,fegggd,gefggc,gefggd` | T4 |
| 7 | `fegggfg,gefggfg` | T2 |

Direct ordered primitive-path decoding checks that **every** word returns `(2,0,0,0,0,0)`; the words of each horizon share exactly one full BRC positive key, and their exact nine-to-five observation matrix has rank nine. The resulting union has exactly **72 signed primitive prefix edges, 4 distinct full BRC positive-count keys, and 6 transfer signatures**. Together with the exhaustive lower bound this establishes the theorem.

## Two independent executed implementations and evidence

**Python exact computation** uses the unchanged pinned native model helper `VERIFY_EC49ER.py` and the exact earlier signed-prefix H7 DP core from EC49EXC. Its stages are `EC49EXD_PREP.py`, `EC49EXD_H5_SCREEN.py`, `EC49EXD_H6_SCREEN.py`, `EC49EXD_CHECK_TERMINAL.py`, `EC49EXD_FINAL4.py`, all **actually executed** on 2026-11-03. Native enumeration and exact rank-fiber precheck, all 101 terminal costs, all 426 h5 prefix minima, all 196 bounded h6 minima, and all four final free-prefix minima returned the counts above and PASS. Raw JSON: `EC49EXD_H5_SCREEN_EXECUTED.json`, `EC49EXD_H6_SCREEN_EXECUTED.json`, `EC49EXD_TERMINAL_LEMMA_EXECUTED.json`, `EC49EXD_FINAL4_EXECUTED.json`.

**Independent Node.js/V8 22** script `VERIFY_EC49EXD_INDEPENDENT.js` does **not import Python or pinned helper code**. It independently defines all seven native operation paths, enumerates every h2..h7 legal word, derives nine-history transfer signatures, verifies the unique essential signature family per positive key, solves 426 h5 cases and 196 h6 cases using its own exact integer trie, recomputes all four final six-edge lower bounds, and verifies the actual 72-edge witness. Its actual output is `EC49EXD_INDEPENDENT_EXECUTED.json`, `status=PASS`. All cross-implementation coverage and target numbers agree. The only modular arithmetic is finite-field Gaussian rank; no floating-point mathematical optimality assumption is used.

The exact computation is described above; a portable replay script, execution summary, precise predecessor source location and subsequent mathematical question accompany this publication. The original larger per-case transcript and the 8MB schedule expansion were generated during author-side computation but are not included in this GitHub write; regenerate them from the published replay procedure. This distinction is reflected in the evidence summary.

## Provenance and remaining research

The result is a precise **finite symbolic positive-BRC/native-X6 three-resource theorem** in this frozen observer model. Complete project scientific parent objective remains the full H7 Pareto classification, plus tool/result reuse across Enterprise Math. The fixed model retains the original joint observation and signed path rather than collapsing them into a BRC key. This author-side research can be published as a GitHub draft with actual readback; formal native Activity/CLAIM/Result and independent Driver admission require the corresponding active service authority and owner state. On this run authenticated GitHub identity was `awdawmip`; native site gateway 0.6.11 reported `research_authority_granted=false`, and the owner inventory returned `CONTROL_QUOTA` (actual owner unconfirmed). This report asserts no native Result or review receipt.

**Next EC49EXE:** use the now-complete M=2,3,4,5 strata to solve the remaining exact `H=7,M=6,S<=4` best prefix cost, and assemble the global H7 Pareto front with the all-H edge-optimal `F_h,G_h` family `(E,M,S)=(4H+30,H-2,6)` (hence H7 `(58,5,6)`) from EC49EP. Check all candidate points against dominance with exact witnesses and certified lower bounds.