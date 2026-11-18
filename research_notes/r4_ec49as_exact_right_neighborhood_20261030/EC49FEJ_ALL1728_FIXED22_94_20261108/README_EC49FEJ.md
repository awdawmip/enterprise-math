# EC49FEJ — Global exact 94-edge optimum across all 1,728 five-BRC-key inventories in the fixed 22-path regime

Date: 2026-11-08. Status: **author-side finite exact theorem and audited computation; independent Driver mathematical admission pending**. Frozen science input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (unchanged). Main source: EC49FEI at PR #1730 HEAD `928fe316791833d8cd091631351198b06755e76a`, supported by EC49FEH and EC49FEF; the *project rules* are read currently, separately from this frozen scientific pin.

## Theorem and domain

Use the original six typed signed native-X6 primitive operators `a,c,d,e,f,g`, nine-state DFA signatures and complete positive native-BRC key `K=(x,y,z)` from the frozen source. Every word ends at signed displacement `+2E1`. For horizons H2...H9 impose exactly `(4,2,2,4,2,2,4,2)` distinct ordered primitive words and rank-nine observer clauses `(18,20,33,40)` at each horizon. Count the **distinct nonempty ordered signed-native-step prefix edges** across all 22 words. Allow the 22 words to use **any of the globally at most five complete BRC keys**, including arbitrary within-window key mixtures, and any legal word ordering.

**Exact theorem:** The minimum native-prefix cost over the entire stated finite 22-path model is

\[
\boxed{\min C_{\mathrm{native}}=94.}
\]

The EC49FDN/EC49FEH explicit 22-word system attains 94. The original broader mother objective `at most five BRC keys and at most 93 native edges` remains the next search target, now outside this fully classified quota family.

## Proof part 1: exhaust the complete five-key search space

At every two-word horizon (H3,H4,H6,H7,H9), rank-nine coverage forces signature pair `(16,32)`. From the native six-operator count identities, any high-signature word at horizon h has `x+y=h+1`. The five mandatory high horizons have mutually different sums `4,5,7,8,10`, so the global five-key limit forces exactly one complete key for each mandatory sum. At H3 the sole high-capable key is `(3,1,1)`. At H4,H6,H7,H9 the complete high-capable key families have sizes respectively `2,6,9,16`. These were independently re-enumerated in EC49FEJ using the original integer operator-count formulas, permutations and true nine-state DFA. Thus **every** eligible five-key system belongs to exactly one of `2×6×9×16=1,728` inventories, not merely a neighborhood of the earlier 94 witness.

H2 necessarily uses `(3,1,1)` and its four low signatures require exactly `ce,ec,de,ed`. H3 allows exactly four pairs: `(feg or fge)` crossed with `(gef or gfe)`. Each of these four early word sets costs exactly **42** signed-native-prefix edges; the union of all their prefix sets has **54** edges. At H5 and H8 none of the five mandatory high-key sums equals `h+1` (6 and 9, respectively), so each four-word horizon requires the four low signatures `(1,2,4,8)` individually. An exact constructive finite check confirmed that **all 1,728 inventories** have a complete legal 22-word system, not just a rank-only assignment. A deterministic lexicographic witness for every inventory is retained. Its cost range is 114–286; these are constructions, not optimum values.

## Proof part 2: depthwise exact cover lower bound, using only one representative per involution pair

Let `U` be the union of all **54** signed-native prefixes of the four early H2/H3 variants. For a five-key inventory `K`, take each of the 16 mandatory `(h,signature)` groups for H4...H9 and enumerate *all* its legal primitive words from **any key in K**. For positive depth d, retain only groups all of whose candidate words have at least d native steps. Each native signed prefix at that depth covers exactly those retained groups having a candidate with that prefix. Treat **every** prefix in U as free, even though a real early set contains only 42 of them; this deliberately relaxes the optimization. On groups not already covered by these free prefixes, solve the exact minimum unit-cost set cover with bitmask dynamic programming, obtaining `m_d(K)`. Choosing depths independently is another relaxation. For **every** legal 22-word system with inventory K,

\[
C_{\mathrm{native}}\ge 42+\sum_{d\ge1}m_d(K).
\]

The finite code evaluates each needed cover *exactly*, with integer masks and memoized recursion; it stops early once the running certified lower bound reaches 94, which suffices to reject ≤93. For all **864** inventories having H4 key `(3,2,1)`, the calculated bound reached **at least 94**. The complete per-case inputs, integer bitmasks' exact cover counts by depth, stop depth, and lower-bound certificates are retained in four `EC49FEJ_GLOBAL_LOWER_PART_*.json` files. All indices 0...863 were covered once.

Apply the previously proved EC49FEF native operator involution `I=(c d)(f g)` with positive BRC-key map

\[
J(x,y,z)=(y+2z,x-2z,z),\qquad J^2=1.
\]

It maps `(3,2,1)` to `(4,1,1)`, each of the three other high-key families to itself, permutes the rank-nine observer signatures, and preserves signed native-prefix costs for all finite operation-word sets. The two H4-key halves therefore form **864 disjoint involution pairs**. A counterexample of cost ≤93 in the other half would map back to a counterexample in the exhaustively checked first half. This proves the global lower bound **94** over all 1,728 inventories. The pre-existing explicit 94-edge witness (22 words, 94 edges) gives equality.

## Validation and reproducibility

The lossless archive `EC49FEJ_complete_evidence.tar.xz.b64` contains all standard-library proof enumerators, full inventories and lex witnesses, full 864-index partial-cover certificates, the independent MILP audit, input provenance and this README. Reproduce with:

```bash
python EC49FEJ_SIEVE.py > EC49FEJ_RESULTS.json
python EC49FEJ_CONSTRUCT.py > EC49FEJ_CONSTRUCT_RESULTS.json
python EC49FEJ_GLOBAL_LOWER.py 0 216
python EC49FEJ_GLOBAL_LOWER.py 216 432
python EC49FEJ_GLOBAL_LOWER.py 432 648
python EC49FEJ_GLOBAL_LOWER.py 648 864
python EC49FEJ_INDEPENDENT_AUDIT.py > EC49FEJ_AUDIT.json  # optional SciPy/HiGHS
```

All **1,728/1,728** lexicographic 22-word witnesses passed independent native endpoint, full positive key, observer signature and native-prefix construction checks; **83,474** individually generated words were recomputed for signed endpoint, positive key and DFA signature. In an independently coded SciPy/HiGHS 0–1 set-cover formulation, **326 depth instances** sampled across **20** geographically distributed inventories exactly matched the integer bitmask proof DP. This MILP corroboration is separate from the all-864 exact DP. The exact pair involution was sourced from EC49FEF and tested on representative complete systems and all finite high-key families; no model modification is used.

## Next research unit: EC49FEK

Now that the **entire fixed 22-word quota class** has optimum 94, search admissible alternate horizon quota and rank-nine signature structures while maintaining the native six-axis path grammar and no more than five complete BRC keys. First test a concrete changed H7 path-count/signature family, but allow simultaneous changes in key allocation and affected horizons. Reuse the depth-cover sieve as a valid lower-bound filter, then joint-prefix optimize promising cases. Preserve the user objective ≤93 and the exact 94 witness as reference.

## Source/authority provenance

Frozen operator/observer/BRC semantics were carried from EC49FEG/EC49FEH/EC49FEI on PR #1730. No P000/worldview changes, no physical heartbeat/residual attribution, no π or classical trigonometric science calculation. This is a finite positive-key and signed-native-word combinatorial result. The user-authorized GitHub owner identity is `awdawmip`; the current MCP researcher activity is `EM-DIRECT-088D77`, registered by the actual current native session. Current task owner/CLAIM and independent Driver acceptance remain separate current Source authority checks. The author-side branch commit and file readback establish durable evidence only.
