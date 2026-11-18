# EC49FKN — all five-key BRC realizations need at least 99 signed X6 native prefixes

Date: 2026-11-11. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Status: author-side exact finite theorem, two executed source implementations (Python and independent compiled C++); independent Driver mathematical review pending. This continues EC49FKM on the same PR; P000 remains unchanged.

## Exact theorem

In the frozen nine-state BRC model, the 24 prescribed observation labels admit 178,850 full legal signed-X6 operation words on 94 complete raw cache keys. EC49FKM proved that five complete keys are necessary for full 24-label coverage, and that exactly 16 five-key subsets can cover all labels. They are `K0 ∪ {u,v}` for

```
K0={(2,1,1),(3,0,1),(3,1,1)}
U={(3,3,1),(4,2,1),(5,1,1),(5,1,2)}
V={(5,5,1),(6,4,1),(7,3,1),(7,3,2)}
u∈U, v∈V.
```

**New proved lower bound:** every legal assignment of the 24 observation labels to full BRC operation words that uses exactly five complete raw cache keys requires **at least 99 distinct nonempty, ordered, signed native-X6 microstep prefixes**. Accordingly a solution costing at most 93 native prefixes must use **six or seven** complete raw cache keys. A prior five-key 136-prefix construction is a feasible upper bound; the exact optimal five-key prefix count is still open.

## Analytic lower-bound lemma (independent of the number of paths)

Fix one eligible key set K. For each required label `i`, let `W_i(K)` be every literal BRC word of this label whose complete raw key is in K, and define its least signed microstep length

```
L_i=min_{w∈W_i(K)} |microsteps(w)|.
```

For each native microstep depth d, define the **forced labels** `A_d={i:L_i≥d}`. Any selected realization of a forced label must contain a native signed prefix at depth d. Let `S_d(p)` be the set of forced labels having *some* legal K-word with exactly prefix p at depth d, and define

```
M_d=max_p |S_d(p)|.
N_d=|A_d|.
r_d=ceil(N_d/M_d).
```

Every single chosen prefix of depth d can serve at most M_d of those N_d forced labels. Hence a valid 24-word completion must use at least r_d distinct prefixes at that depth. Prefixes of different depths are different objects. Therefore **for every legal choice of words**:

```
|union_i P(w_i)| >= SUM_{d=1}^{max_i L_i} ceil(N_d/M_d).
```

This counts signed ordered native X6 paths, not unsigned endpoints, cache keys or scalar readouts. Every L, N and M is obtained from the entire frozen legal catalogue; the certificate makes no assumption about choosing the same words at different depths, so the bound is valid even if the per-depth optima cannot be realized simultaneously. This is an ordinary exact lower bound rather than a claim that each layer's bound is attained.

## Executed exact 16-set certificate

Index U in the order displayed, V in the order displayed, and enumerate `for u in U: for v in V`. The independently cross-verified 16 lower bounds are:

```
[101,101,109,115, 101,99,101,114,
 109,101,101,115, 112,111,112,114].
```

Every value exceeds 93. The **smallest is 99**, from K0 plus U[1], V[1] (zero-based, u=(4,2,1), v=(6,4,1)). Each of the 16 certificate rows has its 20–22 explicit layer `(d,N_d,M_d,r_d)` values in the 57,822-byte expanded JSON report, saved byte-for-byte as `EXACT_RESULT_EC49FKN.json.gz.b64`. Its SHA256 as expanded UTF-8 JSON is `1dcb328d1abc571bc82196f239eed66e0d6087a2ca64a0c1a85f30cc17b62ca2`.

The exact Python verifier `VERIFY_EC49FKN.py` was executed using the previously published original frozen BRC generator from sibling `EC49FJD_RELEASE_B11_COMPLETE_20261111/`; it returned:

```
EC49FKN_ALL_FIVE_KEY_PREFIX_LOWER_BOUNDS_PASS 16 global_min_bound 99 bounds [101, 101, 109, 115, 101, 99, 101, 114, 109, 101, 101, 115, 112, 111, 112, 114]
```

Independently coded C++17 `INDEPENDENT_EC49FKN.cpp` directly enumerated the full nine-state DFA and signed-X6 step streams without calling the Python generator. Compiled with `g++ -std=c++17 -O2`, it returned:

```
EC49FKN_INDEPENDENT_CXX_PASS 178850 94 24 sixteen_sets=16 universal_min=99
101 101 109 115 101 99 101 114 109 101 101 115 112 111 112 114
```

Run Python in this directory with `python VERIFY_EC49FKN.py` (set `EC49FKM_INPUT_DIR` to the original frozen source folder if necessary); Python writes full `EXACT_RESULT_EC49FKN.json`. Decode the published report by:
```
python -c 'import gzip,base64,pathlib;p=pathlib.Path("EXACT_RESULT_EC49FKN.json.gz.b64");pathlib.Path("EXACT_RESULT_EC49FKN.json").write_bytes(gzip.decompress(base64.b64decode(p.read_text().strip())))'
```
The report is a direct exact, complete layer certificate, not an illustrative sample.

## Source, scope and next action

Frozen generator `EC49FGW_RADIUS5_SCREEN.py` and witness `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` were already stored in the sibling EC49FJD directory and verified at the frozen scientific pin. EC49FKM had separately established the 16 complete five-key sets through exact 476-quintuple cover enumeration. The two present implementations agree on all depthwise bounds; independent Driver review is pending. This author research supplies no current EC49AS CLAIM or formal Result.

**Next:** study six-complete-key allowed sets under the same frozen catalogue, first with this exact depthwise forced-label lower-bound sieve, then apply signed-prefix union optimization for survivors. The mother question remains `C_min(7) ?= 94`.
