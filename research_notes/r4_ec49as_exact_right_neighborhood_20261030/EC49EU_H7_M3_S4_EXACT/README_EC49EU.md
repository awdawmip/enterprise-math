# EC49EU — Exact seven-window three-cache / four-observer native-X6 prefix optimum

**Research date:** 2026-11-03 (Asia/Shanghai). **Predecessor:** EC49ET, immutable GitHub commit `750913871c0a16ef22b7e79afa86e7402d0d10cf`, `research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49ET_H7_TWO_KEY_EXACT/`. **Handoff:** Draft PR #1730. **Status:** `AUTHOR_FINITE_EXHAUSTIVE_PROOF / INTEGER_DP_PASS / INDEPENDENT_JS_PASS / MILP_CROSSCHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Frozen scientific pins:** Global knowledge `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, retained exactly from EC49ET. **Current applicable behavioral rules read separately:** Global canonical `main@203add364273ab2682b0bb135d877c6b3a5092ef` and Enterprise Math `main@6c70c75bc9c846c3f4d81917acdbd420e9c5a570` (verified 2026-11-03). P000, ACTIVE Heartbeat World, joint observer preservation and BRC typing are unchanged.

## 1. Precise scientific question and theorem

In the historical native six-axis signed-X6 model of EC49ET (historical displacement `-2E1`), the seven allowed *ordered primitive* operation strings are

```
a=(-1,-1), b=(-2,-2),
c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
```

The signed steps refer to the primitive native axes `E1,E2,E3`; all six raw native displacement and positive-count components are retained, with components four through six zero for this restricted input family. No assertion of a complete three-dimensional slice-selection operator is made. A returning future word of operation length `h` must have native displacement `(+2,0,0,0,0,0)`. At each horizon `h=2,...,7` choose a nonempty set of returning operation words with **one identical complete six-axis positive primitive count vector** `p_h`; its five-bucket `N,A,B,AB,BA` observation of the nine specified historical seam states has rational rank nine. Different horizons may reuse a `p`, and original word/branch identity and signed path order remain available.

Let `E` count different *nonempty signed primitive prefix edges* across selected words; let `M` count different complete `p_h` vectors (the keys of the symbolic strictly-positive, two-channel BRC factors `X_p=∏x_i^{p_i}`, `Y_p=∏y_i^{p_i}`), and let `S` count different nine-history terminal observation transfer matrices. In this exact finite model:

\[
\boxed{\min\{E\mid H=7,\ M=3,\ S=4\}=116.}
\]

Furthermore, every feasible `M=3, S=4` case has `p_2=(3,1,1,0,0,0)`, `p_3=p_4=(4,2,1,0,0,0)`, and a shared `p_5=p_6=p_7` selected from **exactly three** possibilities:

\[
(5,4,1,0,0,0),\quad(6,3,1,0,0,0),\quad(6,4,1,0,0,0).
\]

Their respective *exact* minimum `E` values are `116`, `116`, and `128`. Therefore both the first two assignments attain the theorem. Combined with the predecessor's exact two-cache point `(116,2,6)`, this produces a four-matrix alternative `(116,3,4)` with equal prefix cost and one more symbolic BRC cache key. This **solves the M=3, S=4 stratum only**; it does not classify all H=7 Pareto points.

## 2. Complete classification of cache-key assignments

Write `e=#e`, `r=#c+#d`, and `a=#a`, `f=#f`, `g=#g` for a returning operation word of length `h`. From the full native displacement equation (with `b=0`),

\[
 a=e-1,\qquad r=p_1+p_2-h-1,\qquad f=p_1-r-2e,\qquad g=p_2-r.
\]

All counts are nonnegative integers, `e>=1`, and any arrangement of the resulting multiset of `a,c,d,e,f,g` tokens is tested, without a signature-based deletion before the complete domain is formed. The case `S=4` must use the four necessary distinct `T4={signature(ce),signature(de),signature(ec),signature(ed)}` transfer matrices in every event-bearing horizon. This follows from the inherited EC49EL exact rank classification: each individual horizon's full nine-state observation has rank nine with the four signatures; any alternative non-event rank-nine horizon requires the *additional* distinct pair of first `f/g` signatures, making `S>4` across the forced `h=2` signatures. Hence all horizons here use T4, and the four mandatory observation types must be covered separately at each horizon.

The h=2 full-rank p-fiber is uniquely `p0=(3,1,1,0,0,0)` and forces the four base operation words `ce,de,ec,ed`, whose primitive-native prefix union contains exactly `28` edges. Fully enumerate all candidate returning words with their complete six-axis `p` and transfer signatures for h=3,...,7 (generator `MODEL_EC49EU.py`). For each horizon filter keys for which the fiber contains all four `T4` signatures. In this declared finite domain, the number of such fibers is:

| horizon h | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|
| all returning seven-letter operation words | 8 | 51 | 304 | 1,770 | 10,224 | 58,947 |
| positive-count fibers covering all `T4` | 1 | 3 | 7 | 13 | 22 | 34 |

The complete finite domain is bounded by `e=1,...,floor((h+2)/2)`, `0<=p1<=2h`, `0<=p2<=h`, `p4=p5=p6=0`; these are necessary bounds from the primitive code and returning displacement and include all feasible fibers. For each key the generator enumerates every multiset permutation for `c=0,...,r`. The independent JavaScript checker instead enumerates **all** `7^h` operation strings, checks displacement and terminal signatures directly, and obtains exactly the same returning populations and candidate sets. Intersecting the available T4-keys with the requirement that the total number of distinct keys across h=2,...,7 equal three yields precisely the three assignments in §1. This is a complete, independently checked finite classification, not an assumed pattern from sampled schedules.

## 3. Exact signed-prefix tree lower bound

For each of the three key assignments, retain every eligible complete ordered word of horizon `h=3,...,7` whose terminal signature is one of the four necessary `T4` signatures. Label each word's trie terminal with bit `(h,signature)`, yielding `5×4=20` required terminal colors. Include the four h=2 base words; their `28` prefix edges are pre-paid. Insert the candidate words using their full ordered signed native primitive string into one rooted trie. The three true native trie populations are respectively `8,049`, `8,049`, and `11,117` **nodes including the root**. Each optional nonbaseline signed prefix edge costs `1` if used by at least one chosen terminal; a baseline edge costs `0` additional.

Let `D_v[b]` be the least number of additional prefix edges inside the subtree rooted at trie node `v` for coverage bitmask `b`. Initialize at each node `D_v[0]=0`; if the node is an eligible terminal for color `t`, additionally `D_v[1<<t]=0`. On merging a child `u`, set

\[
D^{new}_v[b\lor c]\leftarrow \min\left(D^{new}_v[b\lor c],\ D_v[b]+D_u[c]+\boldsymbol1_{c\ne0}\boldsymbol1_{(v,u)\notin\text{baseline}}\right).
\]

By induction over the finite trie, all eligible terminal subsets are represented by one bitmask and all shared edges are charged exactly once. The terminal-choice initialization and OR merge therefore give the exact global optimum at the root for mask `2^20-1`. The original operation code is prefix-free at operation boundaries, so different complete operation words cannot accidentally alias as complete native strings; original token identities are retained in candidate generation. No floating arithmetic enters the lower-bound kernel.

The actually executed C++17 all-integer checker (`VERIFY_EC49EU_EXACT_DP.cpp`), supplied with each fully generated native trie, prints:

| p on h=5,6,7 | trie nodes | exact new edges | E including baseline | largest live DP states | integer state-pair convolutions |
|---|---:|---:|---:|---:|---:|
| `(5,4,1)` | 8049 | 88 | **116** | 1,048,576 | 134,632,426 |
| `(6,3,1)` | 8049 | 88 | **116** | 1,048,576 | 134,632,866 |
| `(6,4,1)` | 11117 | 100 | **128** | 1,048,576 | 67,316,176 |

The finite integer lower bounds are `116,116,128` for the complete three-case domain. The separately executed 0–1 MILP formulation in `VERIFY_EC49EU_M3S4.py` independently produced the same three objective values, `mip_gap=0` and matching dual bounds. That independent solver serves as a crosscheck; the preceding integer recurrence supplies the exact proof kernel.

## 4. Attaining authentic signed-X6 paths

Use the h=2 base words `ce,de,ec,ed` and the following first exact-optimal assignment (the *second* 116-edge case's fully checked witness is also recorded in `EC49EU_M3S4_EXECUTED.json`):

| h | selected **complete ordered** operation words | p for the window |
|---|---|---|
| 2 | `ce`, `de`, `ec`, `ed` | `(3,1,1,0,0,0)` |
| 3 | `cec`, `ded`, `ecc`, `edd` | `(4,2,1,0,0,0)` |
| 4 | `cefg`, `degf`, `ecfg`, `edgf` | `(4,2,1,0,0,0)` |
| 5 | `ceccg`, `dedgd`, `eccgc`, `edddg` | `(5,4,1,0,0,0)` |
| 6 | `cefggc`, `dedggf`, `eccgfg`, `edgfgd` | `(5,4,1,0,0,0)` |
| 7 | `cefggfg`, `degffgg`, `ecfgfgg`, `edgfggf` | `(5,4,1,0,0,0)` |

Independent full-space JavaScript code checks each word's actual primitive signed-X6 return `(2,0,0,0,0,0)`, the complete positive-count vector per window, the full nine-history observation matrix rank `9`, the unique transfer count `S=4`, three symbolic BRC keys `M=3`, and the distinct signed primitive prefix-edge union `E=116`. Modular elimination at prime `1,000,003` gives rank nine and is sufficient to certify rank nine over `Q` because the observer entries are integers; the finite exact-DP bound plus this witness proves equality. The symbols `x_i,y_i` are strictly positive and independent BRC factors, with no signed/complex phase cancellation, order loss or physical time calibration asserted.

## 5. Executed evidence and reproducibility

Research program source and executed report files in this folder:

- `MODEL_EC49EU.py`: exhaustive p-fiber generator and native history transfer signatures.
- `VERIFY_EC49EU_M3S4.py` and `EC49EU_M3S4_EXECUTED.json`: all three full assignments, exact rationally typed native inputs, independent MILP numerical crosscheck, and attaining operation words.
- `VERIFY_EC49EU_EXACT_DP.cpp`, `RUN_EC49EU_EXACT.py`, and `EC49EU_EXACT_EXECUTED.json`: exact C++ finite integer DP, generation of full native signed-prefix tries, actual executable outcome for every assignment.
- `VERIFY_EC49EU_INDEPENDENT.js`, `EC49EU_INDEPENDENT_EXECUTED.json`: independent direct enumeration of all operation strings, complete assignment classification, true signed-X6 witness check, modular nine-rank audit.
- `EC49EU_THREE_TRIES.tar.gz.b64`: lossless Base64(gzip TAR) of the three **actual** full finite DP input text files; unpack with `base64 -d EC49EU_THREE_TRIES.tar.gz.b64 | tar -xz` in a trusted local directory. SHA256 digests of each raw text input are present in `EC49EU_EXACT_EXECUTED.json` and `SHA256SUMS_EC49EU.txt`.

Reproduction from unpacked source directory with Python 3.11+, C++17, Node.js, SciPy/NumPy (MILP only):

```bash
OPENBLAS_NUM_THREADS=1 python VERIFY_EC49EU_M3S4.py 60
python RUN_EC49EU_EXACT.py
node VERIFY_EC49EU_INDEPENDENT.js
```

All three commands were executed successfully for this submission. The exact input archive permits reexecution without regenerating the candidate tries. Evidence completeness is for the specified finite typed model. Current control permissions do not supply a native research CLAIM, Result or independent Driver acceptance.

## 6. Research identity and next unit

GitHub client authenticated as `awdawmip`; project write via an authorized ordinary author-side research PR. Native Enterprise Math service v0.6.11 reported `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false` for session creation. The active-Owner query returned `CONTROL_QUOTA`. No native Research Activity, CLAIM, Result, independent Driver review or canonical admission was obtained. Prior historical authorship and task identities are unchanged.

**Next EC49EV:** classify `H=7, M=3, S=6` and find a precise Pareto candidate/lower-bound pair; reuse this unit's full signed-X6 p-fiber enumeration and the integer trie DP, with a compact rigorous pruning argument for cases that reach many different keys. Compare `(116,2,6)`, `(116,3,4)` and `U_eq(7)=58` only at their relevant constrained scopes. Full H=7 Pareto enumeration remains open.
