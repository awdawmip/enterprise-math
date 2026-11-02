# EC49EP — Complete exact H=4 Pareto frontier of native-X6 prefix, symbolic BRC, and observer resources

**Scientific date:** 2026-11-02. **Mode:** author-side exact finite research. **Evidence status:** two independently executed exhaustive implementations PASS; portable draft, unreviewed/not admitted in canonical Enterprise Math task state.

## 1. Scope, frozen inputs, and objective

This unit continues EC49EO at immutable GitHub commit `24f951017edde9e2e37b6b5a8a9c1e0cf4d58349`, notably its exact H=3 Pareto result and H=4 conditional point `(56,2,4)`. The **scientific inputs remain frozen** at `GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e` and `enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` as the inherited research note specifies. Current global/project behavioral rules were read separately (2026-11-02) rather than used to move the scientific pins.

We work over the declared Heartbeat World six native spatial axes and an ordered trace of signed native primitive steps. The seven **allowed operations** are:

```
a = (-E1,-E1)                       b = (-E2,-E2)
c = (+E1,+E2,-E1,-E2)              d = (+E2,+E1,-E2,-E1)
e = (+E3,+E1,+E1,-E3)
f = (+E1,-E1)                       g = (+E2,-E2)
```

A word of operation length `h` is legal exactly when its signed native-X6 displacement is `+2E1`. At each `h=2,3,4`, select a nonempty collection of legal words whose **complete six-coordinate positive native-step count** is one fixed vector `p_h`. It must distinguish the nine historical seam atoms:

`(N,0),(N,1),(N,2),(A,0),(A,2),(B,0),(B,1),(AB,0),(BA,0)`.

Here A denotes the first adjacent positive-step `(+E1,+E2)` event, B the first `(+E2,+E1)` event, and the ordered first-occurrence history persists. Terminal buckets are `N,A,B,AB,BA`. Observational completeness means the nine-by-(5 × number of words) terminal 0/1 matrix has **rank nine over Q**. Each word's transfer signature is its complete map from nine initial atoms to five terminal buckets. The ordered primitive path and provenance remain part of the computational evidence, distinct from the transfer signature.

The exact resource triple for *the union of all selected horizons* is:

* `E`: number of distinct **nonempty ordered signed-native primitive prefixes**, i.e. edges in the joint primitive-step trie.
* `M`: number of different **complete positive-count vectors** `p_h`; these are symbolic paired BRC multiplier keys `X_p=∏x_i^{p_i}` and `Y_p=∏y_i^{p_i}` for strictly positive BRC weights. Coincidental equality of evaluated multipliers does not merge keys.
* `S`: number of distinct **full nine-by-five transfer matrices** (signatures), rather than just output buckets.

The objective is Pareto minimization of `(E,M,S)` in this fixed finite problem. These typed, positive BRC operations preserve the full ordered path and nine-state history separately; no phase or signed-amplitude cancellation is asserted.

## 2. Main finite theorem: the complete H=4 Pareto set

**Theorem EC49EP-1.** Under the hypotheses in §1, the exact set of nondominated feasible triples is:

```
(E,M,S) = (44,3,4), (46,2,6), (56,2,4).
```

In particular, **the unrestricted-observer two-BRC-key optimum is**

`E_min(H=4 | M=2) = 46`.

That is ten native prefix edges below the previously certified `E_min(H=4 | M=2,S=4)=56`: allowing six instead of four observer signatures saves ten native edges while keeping the same two BRC cache keys.

**Exact attaining witnesses**, ordered by operation horizon:

| Resources `(E,M,S)` | h=2 | h=3 | h=4 | Complete positive vectors by horizon |
| --- | --- | --- | --- | --- |
| **(44,3,4)** | `ce,de,ec,ed` | `cef,def,ecf,edf` | `ceff,deff,ecff,edff` | `(3,1,1) ; (4,1,1) ; (5,1,1)` |
| **(46,2,6)** | `ce,de,ec,ed` | `feg,gef` | `fegg,gefg` | `(3,1,1) ; (3,1,1) ; (3,2,1)` |
| **(56,2,4)** | `ce,de,ec,ed` | `cec,ded,ecc,edd` | `cefg,degf,ecfg,edgf` | `(3,1,1) ; (4,2,1) ; (4,2,1)` |

All vectors above append three literal zeroes for axes 4,5,6; these are actual zero counts in the **explicit chosen native paths**, not omitted unknown coordinates. Each horizon is rank nine. Native union prefix counts, respectively, are `28→36→44`, `28→42→46`, and `28→44→56`.

## 3. Complete finite proof: returned words, observer rank and primitive trie

**Step 1 — complete raw legal universe.** Exhaustively enumerate all `7^h` words of length `h=2,3,4`. Expand **each operation** into its ordered signed native steps and retain exactly displacement `(+2,0,0,0,0,0)`. The legal word counts are exactly **8, 51, 304**. Group each horizon's words by its full six-coordinate positive-count vector, and group each such fiber by its complete nine-history transfer signature.

At h=2, complete enumeration of all 255 nonempty subsets proves that the *unique feasible rank-nine fixed-vector core* is `ce,de,ec,ed`, with `p0=(3,1,1,0,0,0)`, four transfer signatures and **28** native prefix edges. Other h2 choices can only add words/cost, so the core can be fixed without loss of Pareto optimality.

There are exactly **four** rank-nine positive-count fibers at h=3 and exactly **nine** at h=4. The h4 fibers contain no words with `p=p0`. Therefore every feasible reduced selection has either **M=2** or **M=3**. Precisely **4×9=36** cross-fiber cases remain: 12 two-key and 24 three-key cases.

**Step 2 — observer signature reduction with full rank preserved.** For a fixed `(h,p)`, words having the same transfer signature have exactly the same five terminal observer columns. Thus any rank-nine choice contains a *minimal rank-nine collection of distinct signatures*; deleting any other selected word cannot increase `E`, `M` or `S`. We enumerate all minimal signature collections of the h=3 fiber, then one representative word per signature. This produces, over the 36 cross-fiber cases, **1,224 complete h=3 representative configurations**. Every original feasible selection has one reduced representative no more costly in any coordinate. h=4 is searched without assuming a particular rank-nine signature set.

Observer-rank certification uses Gaussian elimination modulo the prime `1,000,003` on exactly the real 0/1 transfer columns. The Euclidean norm of any 9-row 0/1 column is at most 3. Consequently the absolute value of any nine-by-nine integer minor is at most `3^9=19,683 < 1,000,003` by Hadamard. Thus rank nine over Q **if and only if** rank nine modulo that prime, and the finite search decides rational rank exactly.

**Step 3 — exact joint prefix-tree optimization.** For each h=3 representative `W3`, let `T0` be the signed-primitive prefixes already paid by h=2 and h=3. For every possible h=4 fixed-vector fiber, build the *complete native primitive trie* of its words; leaves carry complete transfer signature labels. At a trie node of prefix `q`, define `D_q(B)` as the minimum count of previously unpaid edges within the rooted subtree using words whose union of selected transfer signatures is **exactly** `B`. The empty choice is `D_q(∅)=0`. For each child edge `q→qk`, joining nonempty descendant choices incurs the exact edge charge `1_{qk∉T0}`; child signature sets are combined by bitwise union, with minimum cost taken for each union mask. Distinct child subtrees have disjoint native edges, so induction on trie depth proves the recurrence calculates the exact union-prefix minimum for **every** signature mask.

For every mask reaching rational rank nine, evaluate `E=|T0|+D_root(mask)`, `M=|{p0,p3,p4}|`, and `S=|signatures(h2∪h3)∪mask|`. Taking the smallest E for each `(M,S)` produces the following complete normalized-representative minima:

| M | S → least E among reduced choices |
|---|---|
| 2 | `4→56`, `6→46`, `7→51`, `8→74`, `9→78`, `10→82` |
| 3 | `4→44`, `5→56`, `6→54`, `7→59`, `8→68` |

An unreduced feasible selection may use additional redundant signatures, producing further dominated resource triples. **Every such selection is dominated by a reduced one in the table.** Dominance pruning of the exact table leaves precisely the three theorem points. The three explicit rows of §2 directly verify attainability, so all lower bounds are tight.

This proof does not rely on a MILP solver or on previously claimed H=4 optimality. The independently implemented Python and JavaScript checks each execute all 36 cross-fiber cases and all 1,224 reduced h=3 choices. Within each case, all h=4 transfer signature masks are computed by an exact dynamic program over the complete primitive trie.

## 4. All-window corollary: resource count of the known edge-optimal nested family

**Proposition EC49EP-2.** Consider the h=2 base `ce,de,ec,ed`, followed, at each integer h≥3, by the two native words

`F_h = feg f^(h−3)`, `G_h = gef f^(h−3)`.

For **every integer H≥3**, the exact three-resource cost over all horizons `2,...,H` is

`(E,M,S) = (4H+30, H−2, 6)`.

**Proof.** The h≥3 two-word family returns `+2E1`. Both words have the same full positive vector `p_h=(h,1,1,0,0,0)` and distinguish all nine seam histories; the two transfer signatures are invariant as terminal buckets under appending the neutral ordered operation `f=(+E1,-E1)`, since no new adjacent *positive* A/B event crosses that appended boundary. Their two signatures are distinct from the h=2 four-signature set. Thus `S=6`. The h=3 count vector equals the h=2 vector, and h=4,...,H contribute H−3 further distinct full vectors, so `M=H−2`. At h=3 each eight-step branch overlaps the base tree on exactly its initial signed primitive edge, giving `E=28+7+7=42`; increasing h appends exactly two new primitive steps to each of the disjoint f/g branches, so `E=42+4(H−3)=4H+30`.

In particular, **H=5** has a valid witness `(50,3,6)`, attaining the previously established *global minimum E=50* at that horizon; H≥5 in this family likewise attains the EC49EM edge-only optimum `E=4H+30`. This is an explicit resource-accounting corollary and an independent constructive foothold for computing H=5's full three-resource Pareto set, which remains the next question.

## 5. Actual execution, provenance, and evidence limits

`VERIFY_EC49EP.py` (Python standard library) exhausts h=2/3/4 words, makes exact finite-field rational-rank decisions, normalizes h=3 signatures, calculates every exact signed-primitive h=4 trie DP, performs three-coordinate dominance pruning and verifies each witness. Raw execution: `EC49EP_EXECUTED.json`.

`VERIFY_EC49EP_INDEPENDENT.js` (JavaScript/V8) separately expands signed paths, builds transfer matrices and h=4 tries, and independently evaluates all cross-fiber signature masks. Raw execution: `EC49EP_INDEPENDENT_EXECUTED.json`. Both returned **PASS** on 2026-11-02, independently agreeing on all `(M,S)` minima, the exact three Pareto points, the 36-case/1,224-option coverage and the witnesses. The all-H family was separately checked by both programs for `H=3,4,5,6,8,16,32,64`; its all-H statement is proved by the structural argument in §4.

The domain is the declared discrete positive-weight two-channel BRC symbolic-multiplier cache and **ordered native six-axis** observer model. Exact symbolic rank and trie costs quantify this model's information and resource use; they are not benchmarks of processor latency, physical heartbeat time or arbitrary phase-amplitude cancellation.

**Actual authority:** GitHub-authenticated identity `awdawmip` has repository write access. The Enterprise Math native gateway version `0.6.11` returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`, for session creation, and `CONTROL_QUOTA` for owner inventory. Thus this author-side proof and durable branch artifacts do not constitute a native RA, CLAIM, Result, independent Driver review or admission. The active authenticated research owner remains unconfirmed. Source publication/readback status is recorded in the run summary after actual remote verification.

## 6. Continuation — EC49EQ

Determine the H=5 **complete** three-resource Pareto set. Use this unit's exact signature-mask trie DP and extend it to simultaneous h=4/h=5 positive-vector key sharing (rather than assuming all horizons have new keys). The analytic starting witnesses include `(E,M,S)=(50,3,6)` from §4 and `(52,4,4)` from EC49EO. First establish **the smallest E at H=5 under M=2**, and investigate whether H=5 admits a three-key witness with `E=50,S<6` or a four-signature witness with `E<52`. Publish actual counterexample words or an exact finite cover/trie certificate, including native steps, positive vectors, nine-history rank and explicit resource counts.