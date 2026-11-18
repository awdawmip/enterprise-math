# EC49FFE extension — exact 106-edge optimum by integer group-prefix dual

Date: 2026-11-09 (Asia/Shanghai). Classification: **author-side exact finite mathematical proof / standard-library independent integer verification PASS / unreviewed / not Source-native admitted**. Frozen science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## The exact proposition

Fix original signed-X6 alphabet `a,c,d,e,f,g`, the original nine-state DFA, strictly positive complete BRC keys

`K = {(3,1,1),(3,2,1),(3,4,1),(3,6,1),(3,7,1)}`,

and horizons H2–H9. Require all low labels `{1,2,4,8}` at H2,H3,H5,H7, and both high labels `{16,32}` at H4,H6,H8,H9. Select one original legal word for each required (h,label), 24 words total; any selected word may use any key in K. Let `C_native` count the distinct nonempty **ordered signed six-axis microstep prefixes**.

**Theorem:** In exactly this model, `min C_native = 106`.

The earlier EC49FFE census classifies the 12,276 feasible inventories of a larger ten-template family; **this theorem is a single fixed-inventory optimum**, not an optimum over all of them. The user's general five-key, cost≤93 target remains open.

## Exact finite lower-bound proof

For the 24 observation groups `g`, let `W_g` consist of **all** words satisfying the fixed key-count equations, original DFA terminal signature, and prescribed horizon. Full exact enumeration by `VERIFY_OPT_EC49FFE.py` produces **287** group-word incidences. For any word `w`, let `P(w)` denote its set of nonempty ordered signed primitive X6 prefixes. There are **1,327** distinct prefixes in the full candidate universe.

The published integer certificate `DUAL_INDEX_CERT_EC49FFE.json` supplies nonnegative weights `T[g,p] ∈ {0,1}` and charges `gamma[g] ≥ 0`. Its denominator is **Q=1** and `sum gamma[g]=106`. Two finite inequalities are checked:

1. For **every** candidate prefix `p`, `sum_g T[g,p] <= 1`.
2. For **every** candidate `w ∈ W_g`, `sum_{p∈P(w)} T[g,p] >= gamma[g]`.

For any legal choice of one word `w_g∈W_g` per group, summing gives the integer argument

```
106 = sum_g gamma[g]
    <= sum_g sum_(p in P(w_g)) T[g,p]
    <= sum_(p in UNION_g P(w_g)) sum_g T[g,p]
    <= |UNION_g P(w_g)| = C_native.
```

The certificate is losslessly index-coded: `groups` has 24 entries in observation order; sort all 1,327 distinct original signed prefixes by `(len(prefix),prefix)`; `weights_by_group[g]` contains the indices whose weight is one. No unknown rounding, tolerance or solver result enters this **published proof checker**. Its exact test covers **1,055** nonzero binary weights, all **1,327** prefix budget inequalities and all **287** candidate-word charge inequalities. The check also independently validates the 106-edge explicit full-key witness in `README_EC49FFE.md`.

Therefore the lower bound is 106. The explicit 24-word construction in the primary EC49FFE manuscript has exactly 106 signed-native edges, yielding the equality and **exact fixed-key optimum**.

## Independent executed checker and reproducibility

From this directory run

```bash
python3 VERIFY_DUAL_EC49FFE.py
```

This uses Python standard library only, with adjacent `VERIFY_EC49FFE.py` (original signed steps, DFA, word/check functions), `VERIFY_OPT_EC49FFE.py` (enumeration helper) and `DUAL_INDEX_CERT_EC49FFE.json` (the complete actual weights). The actually executed output is **`EXACT_INTEGER_DUAL_PASS`**, with `exact_fixed_key_optimum=106`, `candidate_words=287`, `prefixes=1327`, `nonzero_integer_weights=1055`, `denominator=1`.

For independent exploratory crosschecking, run `python3 VERIFY_OPT_EC49FFE.py --milp` (optional SciPy/HiGHS): the associated zero-gap 0–1 formulation reported `objective=106`, `dual_bound=106`, `status=0`, and `mip_gap=0` with 287 word variables, 1327 prefix variables and 4850 constraints. It additionally independently constructs 20 disjoint-prefix depth certificates totalling a valid **104-edge** lower bound. The 106 integer dual above proves the stronger exact result **without depending on numerical solver acceptance**.

A separate one-word order test in the primary paper changes H3 label 8 `ecg` to `gec`, preserving exact key, signature, endpoint and horizon but raising the cost to 109. This proves an operational order residual remains invisible to interval-cover key semantics.

## Scope, source and next action

Provenance: upstream EC49FFC original signed-X6 operations and full-key length/endpoint identity at immutable author commit `2dd856c416f111d90d523dcb10cde952248ec814`; EC49FFD original DFA observer staircase at `df0dbc54707a6926db858631e5a03fea189dccde`; original science pin unchanged. P000 and ACTIVE worldview were read separately and left unchanged.

Portable next unit: reuse the 12,276 known signature-feasible H3-full-low24 inventories, preserve the ordered native prefix semantics, and seek either an explicit <=93-edge legal configuration or an **inventory-specific exact lower-bound certificate**, using the group-prefix integer dual as a reusable tool. Do not re-enumerate the settled signature inventory. Source-native task Owner/CLAIM/Result/Driver review remain independently controlled; this manuscript is not admission.
