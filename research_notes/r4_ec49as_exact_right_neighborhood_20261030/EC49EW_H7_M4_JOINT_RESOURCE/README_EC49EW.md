# EC49EW — Seven-window four-key BRC/native-X6 joint prefix optimum in the four-observer stratum

**Research date:** 2026-11-03 Asia/Shanghai. **Predecessor:** EC49EV, immutable author-side GitHub commit `7e2324bbaaaa546829bdc3180243cd72f9be84b3`, Draft PR #1730. **Classification:** `AUTHOR_FINITE_EXHAUSTIVE_PROOF / EXACT_TRIE_DP_PASS / INDEPENDENT_NATIVE_X6_PASS / MILP_WITNESS_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Frozen scientific inputs (unchanged):** Global Knowledge `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Normative reading updated independently under the verified canonical-main repositories. P000, ACTIVE Heartbeat World and source firewall remain intact.

## 1. Exact model and definitions

Retain the seven ordered operation codes as signed native primitive X6 axis steps, with the last three axes identically zero **only for this declared three-axis research slice**:

```
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2)
```

An operation word at horizon `h` has `h` letters, its expanded full primitive native steps must return signed X6 displacement `(2,0,0,0,0,0)`, and all chosen words at that horizon share one complete six-coordinate positive-step count `p_h`. The symbolic strictly positive two-channel BRC factor associated to a key is `(X_p,Y_p)=(∏ x_i^{p_i}, ∏ y_i^{p_i})`; the ordered word and observer provenance are retained separately. Each horizon `h=2,…,7` must recover rank nine from the nine frozen A/B historical seam input states using the five output buckets `N,A,B,AB,BA`. Let `E` be the number of distinct **signed native primitive prefix edges** in the union of all selected expanded words, `M` the number of distinct `p_h` positive-count keys globally, and `S` the number of distinct history-to-five-bucket transfer signatures globally. All rank checks are exact, not floating point.

## 2. Main exact theorem: M=4 and S≤4

**Theorem EC49EW-1.** Within the complete frozen seven-operation model just specified,

\[
\boxed{\min\{E:\ H=7,\ M=4,\ S\le4\}=92}. 
\]

Every horizon-two full-rank solution requires the four distinct transfer signatures `T4` and the four words `ce,de,ec,ed`, accounting for 28 paid primitive prefix edges. Thus `S≤4` forces those same four transfer signatures at all later horizons. Complete fiber enumeration gives the number of positive keys available at `h=2,…,7` as `1,3,7,13,22,34`; exactly **752** six-horizon key schedules have four distinct keys overall. For those schedules there are exactly **389** distinct key schedules for horizons 2 through 6.

For a fixed schedule, insert **all** eligible complete ordered returning words of every required `(h,signature)` category in one rooted trie of the **expanded signed native primitive steps**. The `K=4×5=20` colors represent the 20 compulsory `(h,signature)` pairs for `h=3,…,7`. Terminal nodes may cover multiple colors. The four h2 words and their 28 prefix edges are pre-paid. At each subtree, use exact integer dynamic programming `D_v[B]` to minimize added edges covering a subset `B` of colors; merge children by bitwise OR, charge a non-paid incoming edge once whenever a nonempty child solution is chosen. Induction on the finite trie proves this is the exact minimum of **all** legal sets of chosen words for the fixed key schedule, including arbitrary prefix sharing. The original exact C++17 kernel is **reused** from EC49EU with immutable blob `d08c90554d205730ce6a36e89a59754e28f36902`; the frozen Python enumerator is reused from blob `bcad085da0655d41753c166fd993cdb35e4d4815`.

Compute the exact H2–H6 minimum for all 389 distinct schedule prefixes. The seven native operation codes have pairwise-distinct first two signed primitive steps, so form a prefix-free code. Hence for any valid H7 extension the four different compulsory full-rank transfer signatures require at least four distinct **new terminal primitive edges**, none paid by any shorter completed operation word. For each schedule,

\[
E_{2:7}\ge E_{2:6}^{\rm exact}+4.
\]

Consequently 686 of the 752 H7 schedules have an **exact certificate** ruling out costs below the attained cutoff 92. The 66 remaining schedules were fully evaluated by exact integer native-trie DP with 20 mandatory colors; **all have E≥92**, and six of them attain 92. The full per-schedule results are retained in `EC49EW_M4_S4_FULL_EXECUTED.json.gz.b64` (gzip+base64 of exact JSON), while `EC49EW_H6_PREFIX_SCREEN_EXECUTED.json` retains the exact H6 cost distribution and screening counts. The execution was split into bounded resumed segments; a time field in the raw program report measures only the final resumed segment, not the entire research runtime.

**Attaining native-X6 witness** (all missing six-axis positive components are zero):

| Horizon h | Selected ordered words | Shared BRC positive key `p_h` | Rank / transfer types |
| --- | --- | --- | --- |
|2|`ce de ec ed`|`(3,1,1,0,0,0)`|9 / T4|
|3|`cec ded ecc edd`|`(4,2,1,0,0,0)`|9 / T4|
|4|`cefg degf ecfg edgf`|`(4,2,1,0,0,0)`|9 / T4|
|5|`cefgg degfg ecfgg edgfg`|`(4,3,1,0,0,0)`|9 / T4|
|6|`cefggc degfgd ecfggc edgfgd`|`(5,4,1,0,0,0)`|9 / T4|
|7|`cefggfg degfggf ecfggfg edgfggf`|`(5,4,1,0,0,0)`|9 / T4|

Independent native path expansion and nine-history rank checks confirm **`(E,M,S)=(92,4,4)`**. Together with prior full-model strata `min(E|H7,M=3,S=4)=116` and the impossibility of S≤4 with M=2, this establishes `(92,4,4)` as a **new nondominated Pareto point**. Adding one BRC key at fixed four transfer matrices reduces native prefix cost from 116 to 92, a saving of 24 edges (~20.7%).

## 3. Six-observer stratum: attained bound and exact fixed-pattern subfamily

**Constructive proposition EC49EW-2.** The full model admits

\[
\boxed{(E,M,S)=(72,4,6)},\qquad \min(E\mid H=7,M=4,S\le6)\le72.
\]

The actually independently verified witness is:

| h | Ordered words | Positive key | Types |
|---|---|---|---|
|2|`ce de ec ed`|`(3,1,1,0,0,0)`|T4|
|3|`feg gef`|`(3,1,1,0,0,0)`|T2|
|4|`fegg gefg`|`(3,2,1,0,0,0)`|T2|
|5|`feggg gefgg`|`(3,3,1,0,0,0)`|T2|
|6|`fegggc fegggd gefggc gefggd`|`(4,4,1,0,0,0)`|T4|
|7|`fegggfg gefggfg`|`(4,4,1,0,0,0)`|T2|

Each row has rational rank nine with the declared five-bucket observers. Across rows there are exactly four BRC keys, six distinct transfer signatures and 72 native signed primitive prefix edges.

**Restricted exact classification EC49EW-3.** Under the additional condition that horizons 3,4,5,6,7 use respectively full-rank signature patterns **`T2,T2,T2,T4,T2`**, all complete positive-key fiber schedules with exactly M=4 number **72**. Exact integer trie DP over every schedule yields `E≥72` and four schedules attain 72. The complete case-by-case results are `EC49EW_T2T4_EXACT_EXECUTED.json.gz.b64`. This is a fully exhaustive theorem **for the stated observer-pattern subfamily**. The unrestricted six-signature M=4 model contains further signature-pattern schedules; its global lower bound and exact value are left to EC49EX.

## 4. Exact evidence and independence status

- Re-run `EC49EW_M4_S4_FULL.py` against the unchanged native model and predecessor C++ DP to regenerate H6/H7 complete certificates; expect 752 schedules, 389 exact H6 cases, 686 screened, 66 full H7 DP cases, exact minimum 92.
- Re-run `EC49EW_M4_S6_T2T4_CASES.py` to regenerate 72 of 72 fixed-pattern schedules and exact minimum 72.
- `VERIFY_EC49EW_INDEPENDENT.js` was actually executed on Node.js. It independently enumerates **all** returning seven-operation words by h2..h7, giving populations `8,51,304,1770,10224,58947`; reproduces full-rank fiber counts, checks both actual native witnesses, their BRC keys and nine-history rank, and returns PASS (`EC49EW_INDEPENDENT_EXECUTED.json`). Rational rank uses a prime q=1,000,003; every 9×9 0/1 minor has |det|≤3^9=19,683<q, so rank nine mod q is equivalent to rank nine over Q for this model.
- `VERIFY_EC49EW_MILP.py` independently represents the fixed witness key schedules as binary prefix-tree closure and terminal-color-cover MILPs; SciPy/HiGHS returned exact reported primal and dual bounds 92 and 72 respectively with gap zero (`EC49EW_MILP_EXECUTED.json`). The **finite mathematical lower bound uses exhaustive integer trie DP**, not floating-point MILP optimality alone.
- `EC49EW_M4_S4_FULL_EXECUTED.json.gz.b64` and `EC49EW_T2T4_EXACT_EXECUTED.json.gz.b64` are lossless retained complete exact DP output JSON. `REPRODUCE_EC49EW.md` supplies all commands and references.

**Acceptance / model scope:** Theorems concern the frozen native X6 *restricted signed-path observer*, with six signed spatial fields retained and only the selected slice carrying nonzero steps, and two typed **symbolic positive BRC factors** per exact key. The source-backed independent Research Activity/CLAIM/Result/Driver review was not authorized by the available Site-scoped readonly service; authenticated GitHub author-side storage is separate from mathematical admission. Actual active task Owner was unconfirmed (`CONTROL_QUOTA`). No P000/worldview change or broad physical interpretation is made.

## 5. Next discriminating question

**EC49EX:** Determine the unrestricted `H=7,M=4,S≤6` minimum by covering all admissible observer-pattern schedules (the current full eligible count is 26,207). In particular, test whether any schedule has `E<72`; use exact lower bounds from shorter prefixes and color/signature requirements to prune, and run exact native-step OR-mask DP on every survivor. Independently measure `H=7,M=5,S=4` as a second line; retain truthful unfinished count and the exact new witness in interim reports.
