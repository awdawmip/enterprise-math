# EC49EK — Exact all-horizon optimal native-prefix costs through H=8 using integer tree dynamic programming

**Date:** 2026-11-02. **Parent/frontier:** EC49EJ, EC49EI, EC49EH in Enterprise Math Draft PR #1730. **Result status:** `AUTHOR_FINITE_EXHAUSTIVE_PROOF / EXACT_INTEGER_DP_PASS / INDEPENDENT_SEAM_AND_BRC_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. This is an author-side research result, not a native CLAIM, Result, Driver review or Foundation decision.

**Frozen scientific inputs carried forward from EC49EJ:** GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavior read separately from canonical main on 2026-11-02. P000 and ACTIVE worldview were read, retained and not edited.

## 1. Mathematical question and exact model

For each integer horizon `h=2,...,H`, choose an arbitrary finite family of native return words of **exactly h** letters in the original grammar `a,b,c,d,e,f,g`:

```
a=(-E1,-E1), b=(-E2,-E2),
c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1),
e=(+E3,+E1,+E1,-E3), f=(+E1,-E1), g=(+E2,-E2).
```

Each word must return the fixed historical displacement `-2E1` by carrying `+2E1`. **Within each horizon**, all chosen words must have the same complete six-axis **positive native-step count** `p=(p1,...,p6)`. Distinct horizons may choose different `p`. The observer is the five terminal first-A/B occurrence buckets `N,A,B,AB,BA` on the nine real historical seam atoms `N0,N1,N2,A0,A2,B0,B1,AB0,BA0`; the selected terminal indicator columns must span all nine history directions over Q for **every horizon**. Both strictly positive BRC channel instruments multiply as `X(w)=∏x_i^{p_i(w)}` and `Y(w)=∏y_i^{p_i(w)}`; numerical value does not replace the word, seam state or provenance.

Cost `U_eq(H)` is the number of **distinct ordered signed-X6 primitive prefixes**, each prefix edge charged once across every chosen word at every horizon. This is the native-trie edge model, not CPU time or total bytes in memory.

## 2. New exact finite theorem

Under the preceding model,

```
U_eq(7) = 58,
U_eq(8) = 62.
```

These are **finite exhaustive exact-computation theorems** for fixed integer H=7,8, not an assertion of the unrestricted formula for all H. They agree with the earlier constructive bound `min(8H+12,4H+30)` at H=7,8. The earlier exact optima at H=2,...,6 are `28,36,44,50,54`; the present new direct DP reproduces the **two-window lower-bound** values `28,36,44,50,54,58,62` for endpoints H=2,...,8. For H=7 and 8 the endpoint lower bound meets a genuine all-intermediate-horizon construction and therefore proves the multi-horizon value.

**Certified counts:** At h=7, the complete returning language contains **58,947 words** in **50 positive-count fibers**, of which **43** have nine-dimensional rank. At h=8, it contains **340,064 words** in **70 fibers**, of which **62** have nine-dimensional rank. All 50 and all 70 fibers are included in the exact DP report, including rank-deficient fibers. Over the full h=2+h=7 exact optimization the smallest number of added prefix edges after the mandatory h=2 tree is **30**, giving `28+30=58`. Over h=2+h=8 it is **34**, giving `28+34=62`.

## 3. Proof of exhaustive lower bounds

**(i) Complete word domain.** The native return condition forces `n_b=0` and `n_e=n_a+1`; each `c,d,f,g` has zero native displacement. Thus generating all strings in `acdefg` of length h with `count(e)=count(a)+1` enumerates **every** valid word, with no sampling or bounded-coordinate projection. Group by the full six-axis positive-step count vector, preserving exactly the BRC equal-fiber constraint.

**(ii) Nine-atom exact transfer.** The first-A/B seam automaton has five terminal buckets on the nine historical atoms. Group words within a positive-count fiber by their complete nine-entry transfer signature. For any subset of signatures, form all corresponding 9-by-5 zero-one indicator columns and compute rank in F_1000003. A 9x9 zero-one determinant has absolute value at most `9^(9/2) < 1000003` by Hadamard. Consequently, rank 9 over F_1000003 is **equivalent** to rank 9 over Q in this declared nine-row model. Enumerating all signature subsets (at most `2^8-1` per fiber) gives all inclusion-minimal sufficient signature masks. Every rank-nine selection contains such a mask.

**(iii) Exact tree optimization for each mask.** Insert every real native primitive word belonging to each signature in the mask into a rooted trie. Mark edges belonging to the mandatory horizon-two tree as cost **0**, all other edges as cost **1**. For a node v, define `D_v(S)` as the smallest charged number of edges inside its subtree yielding at least one terminal word for every signature in subset S. Initialize `D_v(∅)=0`; a terminal word of signature i permits `D_v({i})=0`. For each child edge v→u with cost e∈{0,1}, merge current states and child states by union of signature subsets:

```
Dnew(S∪T) = min(Dnew(S∪T), Dold(S)+Du(T)+e) for T≠∅,
Dnew(S)   = min(Dnew(S), Dold(S)) for T=∅.
```

Induction on the finite prefix tree proves this recurrence is exact: every selected terminal word is in some child subtree, and the cost of the union of selected prefixes is the sum of included child edges and child subtree costs. The state space includes every subset of required transfer types. The root full-mask value is precisely the optimum added cost for that fiber/mask; minimize across all masks and all fibers. This proof does **not** rely on a mixed-integer solver or floating-point optimality tolerance.

**(iv) Mandatory base.** Complete h=2 enumeration yields eight return words in three count fibers. Only the fiber `p=(3,1,1,0,0,0)` has rank nine, and its sole sufficient signature mask forces `ce,de,ec,ed`. Their signed-primitive trie contains exactly **28** different prefix edges. No other h=2 family can satisfy the conditions.

**(v) Exact finite certificate.** The published executable performs (i)–(iv), records each candidate fiber optimum with actual witnessing words, and obtains `min_extra(7)=30` and `min_extra(8)=34`. These give the unconditional lower bounds `U_eq(7)≥58`, `U_eq(8)≥62`, since every full schedule contains a valid h=2+h=H subfamily.

## 4. Achieving the two lower bounds at all horizons

Keep the mandatory horizon-two words `ce,de,ec,ed`. For every h=3,...,H choose

```
F_h = f e g f^(h−3),        G_h = g e f f^(h−3).
```

Their native return displacement is `+2E1`, each word has `2h+2` signed primitives, and both have **exactly the same six-axis positive native-step count** `p_h=(h,1,1,0,0,0)`. As verified on the nine historical atoms and originally established at EC49EI, their nine terminal indicator columns include a unimodular 9x9 minor; hence each h≥3 has full observation rank nine. Each branch is a native prefix of its next-horizon branch. The two trees reuse precisely one root edge each from the h=2 tree. The union edge count is therefore

```
28 + 2 * ((2H+2)−1) = 4H+30,  H≥3.
```

For H=7 and 8 this is **58** and **62**, proving equality with the exhaustive lower bounds. This provides an actual schedule for *every* intermediate horizon; the lower bound and upper witness apply to the same objective.

## 5. Separate BRC and observation costs (constructive schedule only)

At H=8 the schedule contains **16** `(h,word)` observations: four at h=2 and two each at h=3,...,8. It uses **62 native prefix edges**, **six distinct positive-step count vectors** and **six distinct complete seam-transfer signatures**. All 16 words have been checked for both exact positive-BRC multiplicativity identities on nine actual signed-X6 histories under two positive integer weight instruments, in addition to the purely symbolic `X_p,Y_p` laws. In particular h=2 and h=3 share `p=(3,1,1,0,0,0)` while having different transfer signatures. Exact BRC monomial factors therefore need only be evaluated **once per channel per distinct p**, i.e. 6 per channel for this H=8 schedule instead of 16 per-word evaluations; the 16 labeled observations and path identities remain distinct.

For general H≥3, this same construction has `2H` labeled word observations, `H−2` distinct p-fibers, and six distinct nine-atom seam-transfer signatures. With a count-indexed cache, the number of **distinct factor evaluations** per positive BRC channel is `H−2`. For h≥3, `X_h=x1^h*x2*x3`, `Y_h=y1^h*y2*y3` and the recurrence `X_(h+1)=x1*X_h`, `Y_(h+1)=y1*Y_h` permits one multiplication per channel per further h≥4 after initial setup. These are **factor evaluation counts**, not a complete hardware-level arithmetic or storage complexity claim. Evaluation precision, integer bit growth, trie-node storage, and terminal-column assembly are separate costs.

## 6. Actually executed evidence and limits

- `VERIFY_EC49EK.py`: Python standard-library exhaustive word enumeration, exact nine-row prime-field rank with determinant bound, **integer prefix-trie DP** per positive-count fiber and minimal rank signature subset; nonempty exact reports for H=7 and H=8. Output `EC49EK_EXECUTED.json` (H=7) / `EC49EK_H8_EXECUTED.json` (H=8). Results: `PASS`, both new exact optima 58 and 62.
- `VERIFY_EC49EK_INDEPENDENT.py`: independent EC49EG nine-real-history seam simulator, all distinct `(positive-count fiber, transfer signature)` comparisons for H=7 and H=8 (**264** and **388** groups), two-instrument BRC identities for the full sixteen-word H=8 upper witness, and a fully independent h=3 subset brute force (**12,369** nonempty subsets; optimum 36). Output `EC49EK_INDEPENDENT_EXECUTED.json`, `PASS`.
Run the independent checker from this directory with `PYTHONPATH=../EC49EG_FULL_ALPHABET_MULTI_HORIZON:. python VERIFY_EC49EK_INDEPENDENT.py > EC49EK_INDEPENDENT_EXECUTED.json`; it imports the already-published `VERIFY_EC49EG.py` from the adjacent EC49EG research directory. To regenerate DP evidence, use `python VERIFY_EC49EK.py 7 > EC49EK_EXECUTED.json` and `python VERIFY_EC49EK.py 8 > EC49EK_H8_EXECUTED.json`.

- `EC49EK_SUMMARY.json`: small machine-readable counts, minima, explicit witness and provenance. Full per-fiber rows are in the two executed JSON files; hashes listed in `SHA256SUMS_EC49EK.txt`.

Finite coverage is the complete specified operation-word space at h=7 and 8. This work establishes `U_eq(7)` and `U_eq(8)` in the stated native path/BRC/observer model. The general exact formula for every H≥9 remains open. The actual GitHub artifact/branch is an author-side portable result, not an authenticated Source Result, independent Driver acceptance or a physical heartbeat runtime benchmark.

## 7. Next scientific unit EC49EL

Prove the unrestricted **all-H lower bound** `U_eq(H)≥min(8H+12,4H+30)` or find a native-X6 counterexample at some H≥9. First exploit the EC49EI split `r=0` versus `r≥1`: obtain an analytic prefix-edge lower bound for all `r≥1` families relative to the compulsory 28-edge h=2 tree. Alternatively apply the same exact tree DP at h=9 with chunked per-fiber generation and memory accounting. Keep the BRC factor cache keyed by **full p** and preserve horizon/operation-word/seam identity as separate coordinates. Use true end-to-end memory/bit-cost measures before claiming a processor-level speedup.

**Identity/owner:** Connected GitHub user `awdawmip`, collaborator permission `admin`, and observed PR #1730 author-side branch. A live native-session attempt returned `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`; native active-owner listing returned `CONTROL_QUOTA`. No formal RA, CLAIM, Result or Driver review has been obtained by this report. The next authorized formal Source action requires a live Researcher session and exact owner/claim verification; GitHub draft publication does not substitute for it.
