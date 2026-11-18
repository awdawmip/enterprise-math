# EC49EXA — All-window four-transfer BRC key-sharing family; seven-window exact fixed-schedule certificate

Date: 2026-11-03 (Asia/Shanghai). Research parent: EC49EW (`awdawmip/enterprise-math` Draft PR #1730, verified branch head `98eb5202dfa0d7c65d155d2ddfe4d66253085dbe` at intake). This note independently advances its secondary H7 `M=5,S=4` line. Classification: **author-side constructive all-parameter proof + finite exact fixed-key schedule optimization, independently checked; unreviewed, not admitted**.

Frozen scientific inputs: Global Knowledge `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral rules read separately from canonical main. P000, six signed native axes (three unused coordinates retained as zeros in this restricted slice), preserved ordered native steps/observer provenance, nine seam histories, five output buckets and strictly positive symbolic BRC two-channel key factors are unchanged. This is a static finite-word combinatorics result in the frozen observer model.

## Model and resources

Use the seven primitive native signed-axis operation words

```
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
```

At each integer horizon `h=2,...,H`, all chosen operation words have `h` letters and signed X6 displacement `(2,0,0,0,0,0)`, share one complete six-component **positive native step count** `p_h`, and their five-bucket observer transfer matrices over the nine fixed seam-history states jointly have rational rank nine. Define E as the cardinality of the union of nonempty **native primitive signed-step prefixes**; M as the number of distinct six-component `p_h` keys, indexing symbolic BRC factors `(∏x_i^{p_i},∏y_i^{p_i})`; and S as the number of distinct nine-history transfer signatures over the chosen words. No token-trie or BRC-numeric approximation is substituted for these resources.

## Theorem EC49EXA-1 (all integer H≥4, constructive)

**For every integer `H≥4`, an admissible construction attains**

\[
\boxed{(E,M,S)=(8H+24,\; H-2,\;4).}
\]

Define the four selected words at horizons two, three and four by

```
h=2: ce, de, ec, ed
h=3: cec, ded, ecc, edd
h=4: cefg, degf, ecfg, edgf
```

and for every `h≥5`, append `f` exactly `h−4` times to **each** of the four `h=4` words:

```
h≥5: cefg f^(h−4), degf f^(h−4), ecfg f^(h−4), edgf f^(h−4).
```

Spaces in the display separate descriptions, not operation tokens.

**Proof.** Each of `c,d,f,g` has net zero signed displacement and `e` has displacement `(+2,0,0,0,0,0)`, so every displayed word returns by the declared X6 displacement. The complete positive-count key for `h=2` is `p_0=(3,1,1,0,0,0)`; for both `h=3,4` it is `p_*=(4,2,1,0,0,0)`; and for each `h≥5` it is `p_h=(h,2,1,0,0,0)`. Hence exactly `H−2` distinct keys occur.

The four selected words in each row have precisely the same four transfer signatures as `ce,de,ec,ed`, in that order. This follows by direct inspection of the nine-history finite-state seam update, and the append-`f` induction: each `h≥4` word ends with `f` or `g`, whose last primitive step is `−1` or `−2`; appending the loop `f=(+1,−1)` introduces no consecutive `(+1,+2)` or `(+2,+1)` seam transition at the word boundary or within `f`. The original signatures therefore persist for all `h≥4`. The 20×9 zero-one five-bucket observation matrix of `ce,de,ec,ed` has a 9×9 integer minor with row indices (zero-based, in word/bucket order) `(1,3,4,7,8,11,13,17,18)` of determinant `−1`. Thus every horizon has rational observer rank nine and precisely four global signatures.

The native primitive prefix union sizes through `h=2,3,4` are respectively **28,44,56**, directly counting the distinct expanded signed-step prefixes. For every `h≥5` the four new words are obtained by attaching one additional `f` to the corresponding four paths in horizon `h−1`. All four parent native prefixes are distinct and no earlier, shorter operation word includes a primitive prefix beyond those parent terminals (the seven native operation codes are prefix-free as primitive-step words). Each append contributes **two** new primitive signed edges on **four** distinct parent branches, exactly eight new edges. Therefore `E(H)=56+8(H−4)=8H+24`. QED.

**Seven-window instance:** `(E,M,S)=(80,5,4)`. It is a feasible five-BRC-key, four-matrix point and improves the previous four-key/four-matrix construction `(92,4,4)` in primitive-edge count by 12 at the cost of one more BRC cache key. Its three-resource Pareto status against other yet-unclassified five-key cases is still open.

## Proposition EC49EXA-2 (exact optimality within this fixed key schedule, H=7)

Fix the six complete positive-count keys at horizons `2..7` to

```
(3,1,1,0,0,0), (4,2,1,0,0,0), (4,2,1,0,0,0),
(5,2,1,0,0,0), (6,2,1,0,0,0), (7,2,1,0,0,0).
```

Among **all** returning ordered seven-operation words on those keys, requiring rank nine at each horizon and globally at most four transfer signatures, the exact minimum primitive-prefix cost is

\[
\boxed{E_{\text{fixed keys}}=80}.
\]

**Finite proof/certificate.** The `h=2` full-rank key forces signatures `T4={sig(ce),sig(de),sig(ec),sig(ed)}` and 28 distinct baseline edges. For only these four signatures, a rational-rank calculation gives ranks **3,5,7,9** for every subset of size 1,2,3,4 respectively; each later horizon consequently must contain all four T4 signatures, since S≤4. Enumerate **all** returning operation words for each `(h,p_h)` without pruning operation order, and retain all admissible terminal words with T4 signature. There are `K=20` required `(h,sig)` colors for h=3..7; a word can satisfy multiple colors only when the actual complete path/horizon matches them. Insert every expanded native signed-step sequence into the trie, marking the four original h2 paths as paid edges. Apply the integer subset-cover tree DP, where a selected child of a node pays the entering edge exactly once if not already paid, and the union of terminal colors is bitwise OR. The subtree recurrence is exhaustive by induction because native path prefixes form a tree and every selected terminal induces a unique edge-closed path to the root.

Actual execution on the immutable predecessor model (`MODEL_EC49EU.py`, Git blob `bcad085da0655d41753c166fd993cdb35e4d4815`) and original C++17 DP (`VERIFY_EC49EU_EXACT_DP.cpp`, Git blob `d08c90554d205730ce6a36e89a59754e28f36902`) returned:

```
PASS min_extra=52 total=80 nodes=3251 colors=20 largest_states=1048576 convolutions=18029858
```

The all-H construction above attains 80, proving equality for this fixed schedule. This certificate checks one **specified** schedule, not the entire unrestricted five-key stratum.

## Independent verification and reproduction

`VERIFY_EC49EXA_FAMILY.py` independently reimplements X6 operation expansion, nine-history seam state transitions, complete six-axis return/positive counts, exact rational Gaussian elimination, exact Bareiss integer determinant, and the primitive prefix union. The executed test for `h=2..32` returned PASS, including `(E,M,S)=(280,30,4)` at h=32 and the determinant `−1`. General validity is provided by the preceding analytic proof; the finite test is a cross-check of the implementation and boundary cases.

`BUILD_EC49EXA_FIXED_TRIE.py` constructs the exhaustive color-marked native-step trie for the fixed H7 schedule. With the pinned predecessor model/kernel copied into the same directory, reproduce using:

```
python3 VERIFY_EC49EXA_FAMILY.py 32 > EC49EXA_FAMILY_EXECUTED.json
c++ -std=c++17 -O2 VERIFY_EC49EU_EXACT_DP.cpp -o ec49exa_dp
python3 BUILD_EC49EXA_FIXED_TRIE.py | ./ec49exa_dp > EC49EXA_FIXED_DP_EXECUTED.txt
```

The execution data and regenerating source are included with this note; the predecessor frozen scripts are referenced by original Git blob and have not been modified.

## Next question

EC49EXB: determine whether the five-key/four-signature global seven-window minimum is 80, or find an actual native witness `<80`. The full five-key T4 schedule count is **26,037**, computed by exact key-set counting from the per-horizon T4 fiber counts `1,3,7,13,22,34`; full DP across that population remains outstanding. Independent six-signature/four-key question from EC49EW remains open at upper bound E≤72. Compare both against the known unrestricted E≥58. No formal native CLAIM/Result/Driver review was available in this author-side work; the Owner query returned `CONTROL_QUOTA` in this run. Record source branch/commit and readback separately when published.
