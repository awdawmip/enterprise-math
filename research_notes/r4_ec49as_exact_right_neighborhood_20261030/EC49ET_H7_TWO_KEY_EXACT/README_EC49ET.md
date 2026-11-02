# EC49ET — Exact two-BRC-cache H=7 optimum in native signed-X6 three-resource research

**Research date:** 2026-11-03 (Asia/Shanghai). **Parent:** EC49ES (`d1c0a0b8450bf0ca5caca926909e1c02c7c44668`), Draft PR #1730. **Classification:** `AUTHOR_FINITE_EXHAUSTIVE_PROOF / EXACT_INTEGER_DP_PASS / INDEPENDENT_RATIONAL_WITNESS_PASS / MILP_CROSSCHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Frozen scientific pins:** `awdawmip/chatgpt-global-knowledge@773d538180bfb49e24cffeb35c3ee75eb0628e2e`, `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, inherited without modification from EC49ES/EC49ET. **Current behavioral rules, separately read:** GLOBAL canonical `main@d520a0252531cd8b5b8a31744dd6402181d7b36a`, Enterprise Math canonical `main@8ddead488745b4b0d1a73717aed869ac76613d9f`; project P000, ACTIVE Heartbeat World, joint-relation preservation, BRC-only arithmetic, and portable-research protocol also read.

## 1. Model and exact theorem

The ambient native spatial carrier is the six-axis signed integer X6 torsor, and the historical displacement is `-2E1`. Its future words are constructed from **seven ordered operations** with the following complete primitive signed-X6 strings:

```
a=(-1,-1), b=(-2,-2),
c=(+1,+2,-1,-2), d=(+2,+1,-2,-1),
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
```

A word of operation horizon `h` returns if its signed X6 displacement is `(2,0,0,0,0,0)`. Each selected window `h=2,...,7` must independently give rank nine for the nine historical first-A/B seam states under the five-bucket `N,A,B,AB,BA` future terminal observer, with all its selected words sharing the **complete** six-axis positive primitive count `p`. Preserve original operation identity, signed native primitive order, path provenance and the nine-state observer; reuse symbolic strictly-positive two-channel BRC multipliers only across equal `p`.

The three resources are `E` = number of distinct nonempty signed native primitive prefixes in the union of all selected paths; `M` = number of distinct complete six-component `p` vectors; and `S` = number of distinct terminal transfer matrices on the nine historical states. The resulting **new sharp finite theorem** is

\[
\boxed{\min\{E\mid H=7,\ M=2\}=116.}
\]

Every feasible two-key solution uses exactly the following **two positive-count vectors**:

\[
p^{(0)}=(3,1,1,0,0,0) \quad (h=2,3),\qquad
p^{(1)}=(5,3,1,0,0,0)\quad(h=4,5,6,7).
\]

Such a solution must retain at least six terminal transfer matrices, and `(116,2,6)` is attained by the explicit primitive-native witness in §4. Combining with the previous `U_eq(7)=58` gives an exactly determined primitive-prefix premium of `116-58=58` for **the minimal two-BRC-key regime** at H=7. This is a resource-theoretic comparison in the declared fixed finite observer/path model, not a measured wall-clock speedup.

## 2. Analytic classification of two cache keys

By EC49EI/EJ, a returning fiber with positive counts `p=(p1,p2,e,0,0,0)` and `e>=1` exists at precisely the consecutive horizons

\[
H(p)=[\max(p_1-1,p_2+2e-1),\ p_1+p_2-1]\cap \mathbb Z.
\]

The unique rank-nine h=2 fiber is `p^(0)=(3,1,1,0,0,0)`, whose supported horizons are 2 and 3. Thus a two-key solution for all windows 2–7 needs one other `p` supporting each of 4,5,6,7. Its support must contain 4 and 7, so `p1-1<=4`, `p2+2e-1<=4`, and `p1+p2-1>=7`. Since `e>=1`, these imply `p1<=5`, `p2<=3`, `p1+p2>=8`; hence `p1=5`, `p2=3`, and necessarily `e=1`. This proves the two-key assignment is unique.

At h=3, p^(0) has no internal `c/d` event, and rank nine requires both F/G first-seam transfer types. At h=4,5,6, p^(1) has at least one internal event and rank nine requires **all four** EC49EI mandatory types represented by `ce,de,ec,ed`. At h=7, p^(1) again has zero such events and requires both F/G types. The four event-bearing matrices and the two F/G matrices are distinct, so `S>=6`; the given witness uses exactly six. These are necessary full-rank types by EC49EI's exact left-kernel and unimodular minor certificates, not a heuristic signature restriction.

## 3. Complete finite optimum certificate — 116 native-prefix edges

The primitive-code strings are prefix-free as **operations**, so distinct complete operation words map injectively to native signed primitive strings. In each of the five horizons h=3,..,7, the count equations `b=0`, `e=a+1`, `r=c+d=p1+p2-h-1`, `f=p1-2e-r`, `g=p2-r` enumerate **all** returning words with the uniquely forced `p`.

| h | All words in the selected `p`-fiber | Words bearing a mandatory rank-nine type | Number of required type bits |
|---:|---:|---:|---:|
| 3 | 6 | 4 | 2 |
| 4 | 32 | 8 | 4 |
| 5 | 240 | 120 | 4 |
| 6 | 360 | 360 | 4 |
| 7 | 140 | 120 | 2 |

The independent verifier enumerates **all** words of each fiber, including mixed c/d words, and verifies the middle column. Every extraneous transfer type may be discarded without harming the required four/two type coverage or increasing the prefix cost; the necessary types form a 16-bit terminal coverage universe. The h=2 base has exactly four mandatory words `ce,de,ec,ed` and 28 distinct already-paid native-prefix edges.

Insert every eligible native signed primitive string from the second column's mandatory subset and the four base words into one rooted trie. The resulting tree has **3779 nodes including its root**. Terminal nodes carry the bit for their `(h,necessary-type)` requirement; each nonroot edge costs one unless its prefix belongs to the 28-edge base tree, in which case it costs zero additional edges.

**Exact all-integer DP recurrence.** For each node v and bitmask b in `[0,2^16-1]`, let `D_v[b]` be the minimum number of *additional* charged descendant edges needed to select terminals covering exactly the OR of bits b. At v the available local choices are no terminal, or its own terminal bit. When merging a child u with mask c, add `D_u[c] + I[c != 0] I[edge(v,u) not in base]` and set the combined mask to `b | c`, minimizing any repeated output mask. Induction on subtree size proves this recurrence enumerates every allowable subset of full ordered words, charges each shared native prefix exactly once, and returns the exact minimum for every terminal coverage mask.

The executed C++17 integer-DP checker, using the completely recorded input trie and this recurrence, returns:

```
PASS min_extra=88 total=116 nodes=3779 colors=16 largest_states=65536 convolutions=1103092
```

Thus **every** feasible two-key H=7 selection has `E>=28+88=116`. This is a finite exhaustive integer certificate; no numerical optimization tolerance is used for its proof. Independent SciPy/HiGHS 0–1 MILP on the same native trie also returned `status=0`, `objective=116`, `mip_gap=0`, `dual_bound_extra=88`. The MILP is a crosscheck, not the load-bearing lower bound. The exact trie text and both executed reports are preserved with the sources in this directory.

## 4. A real native-X6 attaining construction

Each row's words have the same complete `p` vector indicated in §1. The original signed primitive strings are generated from the declared `a`–`g` operations, and the independent checker computes full rational rank nine on every horizon.

| h | Complete operation words |
|---:|---|
| 2 | `ce`, `de`, `ec`, `ed` |
| 3 | `feg`, `gef` |
| 4 | `cecc`, `dedd`, `eccc`, `eddd` |
| 5 | `cecfg`, `dedgf`, `eccfg`, `eddgf` |
| 6 | `fegfgc`, `fegfgd`, `geffgc`, `geffgd` |
| 7 | `fegfggf`, `geffgfg` |

The independent Python verifier confirms every selected word has signed displacement `(+2,0,0,0,0,0)`, each horizon's BRC cache key matches, every observation matrix has rank 9 over **Q** (using `fractions.Fraction` elimination), and the union has **exactly `(E,M,S)=(116,2,6)`**. The MILP's separately emitted attaining solution is also checked independently (and need not be identical to the displayed solution).

## 5. Verification procedure and evidentiary scope

Run from this directory (Python 3.11+; SciPy/NumPy needed only for MILP):

```sh
python VERIFY_EC49ET_MILP.py
python VERIFY_EC49ET_INDEPENDENT.py
g++ -O3 -std=c++17 VERIFY_EC49ET_EXACT_DP.cpp -o verify_ec49et_dp
./verify_ec49et_dp < EC49ET_TRIE_INPUT.txt
```

Exact executable inputs, printed trace, both JSON reports, and individual source SHA256 digests are included. The independent Python program **does not import** the MILP's word/observer generator; it expands mixed-event words directly and checks the two independently constructed rank-nine witnesses. The exact C++ checker uses the supplied finite trie input and only native integer bitmask arithmetic; its mathematical correctness follows by the recurrence above and the independently audited complete terminal universe.

The strictly-positive two-channel BRC part of the result is the **symbolic positive-step multiplier interface** `X_p=prod_i x_i^{p_i}`, `Y_p=prod_i y_i^{p_i}` on fully retained native ordered X6 paths. It studies signed path **directions**, but does not conflate positive BRC weights with signed or complex phase cancellation. The exact calculation uses a restricted three-coordinate family embedded in ambient six-axis X6; the unspecified project layer-selection operator is not inferred from the three displayed components. Axes 4–6 are fixed zero for this input family, not removed from the world ontology. The proof's current time/horizon is an operation-count parameter and is not a claim about physical heartbeat spacing. P000, ACTIVE worldview, and frozen input references remain unchanged.

## 6. Authority / next discriminating problem

At this work's verification time, GitHub authenticated identity is `awdawmip` with `admin` permission on the Enterprise Math repository. Native service `em_status` reports `research_authority_granted=false` (v0.6.11). An owner inventory read returned `CONTROL_QUOTA`, so the currently active authenticated Owner is not independently confirmed. This is an **author-side portable research result**, not a native Research Activity, CLAIM, Result, independent Driver review or canonical admission.

**Next EC49EU:** determine the `H=7, M=3` resource stratum, first separating S=4 versus S=6. Start with the rigorous H=6→H=7 terminal-edge bound, reuse the exact `p`-fiber interval and 16-bit trie-DP kernel, and calculate one exact lower/upper match or an explicit strict improvement witness. The complete three-resource H=7 Pareto frontier remains open; this unit closes only the minimum-cache stratum.
