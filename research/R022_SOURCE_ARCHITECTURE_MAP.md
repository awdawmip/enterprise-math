# R022 Source Architecture Map

**Task:** RS-R022-HASHCLASH-BRC-TOOL-MINING  
**Researcher:** EM-R022-HC7B4A  
**Status:** CANDIDATE RESEARCH HANDOFF / NOT CANONICAL  
**Taskbook:** `research_tasks/R022_HASHCLASH_BRC_TOOL_MINING_20260811.md` @ `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`

## Source locks

- `zhijieshi/md5collgen` `master@19592490cf62d2168e2c2fd8ec4a288236dd9238`
- `cr-marcstevens/hashclash` `master@892f02e6e1faf71c4ae70ad98a98cc707d6ac664`

No operational collision generation was executed. Source use in R022 is structural and bounded.

---

## A. md5collgen: static continuation router

### A1. Routing site

**File/function:** `block1.cpp :: find_block1`

The source first tests a Stevens-family eligibility guard on the IV and then routes to one of:

- `find_block1_stevens_11`
- `find_block1_stevens_10`
- `find_block1_stevens_01`
- `find_block1_stevens_00`
- fallback `find_block1_wang`

The physical source bits relevant to the five-way route are:

1. `IV[1][31]`
2. `IV[2][31]`
3. `IV[3][31]`
4. `IV[1][25]`
5. `IV[2][25]`
6. `IV[3][25]`
7. `IV[1][0]`
8. `IV[2][0]`
9. `IV[1][6]`

The Stevens eligibility predicate is equivalent to:

- the three bit-31 values are equal;
- the three bit-25 values are all zero;
- `IV[1][0] = IV[2][0]`.

Within the eligible region, `IV[1][6]` and `IV[1][0]` select `S11/S10/S01/S00`.

### A2. BRC interpretation

Source state:
`large IV payload -> small control discriminant -> specialized continuation kernel`.

Important non-cheating boundary:

- the route label can be compiled into five labels, hence three fixed-width control bits;
- **the full IV payload is still passed to the selected continuation**;
- therefore this is source evidence for **control-signature compression**, not for full-state compression.

### A3. Specialized continuation kernels

Representative files:

- `block1stevens11.cpp`
- `block1stevens10.cpp`
- `block1stevens01.cpp`
- `block1stevens00.cpp`
- Wang fallback implementation

The Stevens kernels initialize the internal Q-state from the IV and then use branch-specific masks/constants and stochastic search. There is no dispatcher-level dynamic branch/recoalescence loop after the five-way route is chosen.

**Abstract transition:**

`fine input state x --sigma_route(x)--> continuation procedure A_sigma carrying x`

This motivates the generic **Branch Signature Router (BSR)** problem, but the source alone does not prove that the route token is the complete future state.

---

## B. HashClash: staged branch-cone pipeline

### B1. Orchestration

**File:** `scripts/cpc.sh`

Pipeline:

1. `md5_birthdaysearch`
2. append birthday blocks to the two prefixes
3. `md5_diffpathhelper --startnearcollision`
4. `md5_diffpathforward`
5. `md5_diffpathbackward`
6. `md5_diffpathconnect`
7. `md5_diffpathhelper --findcoll`
8. append the found near-collision block and proceed to the next stage

With the script default `TTT=12`, connection uses:

- low side: `paths(TTT-1)`
- high side: `paths(TTT+4)`

The script exposes explicit resource controls such as `-a` path-count bounds, autobalance limits, birthday memory, thread counts, tunnel minima, and a connection timeout.

### B2. Failure backtrack

The outer loop runs an autokiller. When `workdir$k/killed` exists:

`failedk = k`  
`k := (k > 1 ? k-1 : 0)`  
`backtracks += 1`

This is a **timeout-driven one-stage rollback heuristic**. It is not evidence that the source computes the earliest causal distinction that must be restored.

R022 therefore treats the script as a motivating controller trace, not as an exact causal-rewind certificate.

---

## C. Forward and backward branch cones

### C1. Carrier

**Type:** `hashclash::differentialpath` in `lib/hashclash/differentialpath.hpp`

The carrier is a partial differential constraint path:

- stage offset;
- a vector of word conditions;
- condition counts and path tests;
- partial-state constraints rather than only concrete MD5 states.

This is best viewed as a **constraint-cell/support branch carrier**, not as a literal single-world state.

### C2. Forward cone

**File:** `src/md5forward/main.hpp`

`path_container_autobalance` stores path populations bucketed by condition count and prunes/balances them against a bound. It also applies user conditions, path verification, and tunnel-related thresholds.

Abstractly:

`F_t = bounded population of partial forward constraint tokens at stage t`.

### C3. Backward cone

**Files:** `src/md5backward/*`

The backward side analogously constructs populations of reverse/upper differential paths.

Abstractly:

`B_t = bounded population of backward residual constraint tokens`.

The forward/backward pair is a genuine source witness for **bidirectional branch cones**, but bidirectionality itself is standard meet-in-the-middle structure.

---

## D. Connection core: residual-state BRC

### D1. Rolling connector token

**File/type:** `src/md5connect/main.hpp :: connect_bitdata`

The rolling connector state contains exactly six 32-bit fields:

- `dQt`
- `dQtp1`
- `dFt`
- `dFtp1`
- `dFtp2`
- `dFtp3`

The implementation defines equality and ordering on all six fields.

Raw fixed-width size of this struct's semantic fields:

`6 * 32 = 192 bits`

This is **not a self-contained global branch state**. Its sufficiency is conditional on fixed external connection context, including:

- current connection stage `t`;
- lower path;
- upper path;
- message differences and MD5 step functions;
- current bit position.

Call this a **context-relative residual token**.

### D2. Bitwise split/execute/recoalesce

**File/function:** `src/md5connect/connect.cpp :: md5_connect_bits`

For bit `b = 0..31`:

1. expand every current `connect_bitdata` through `connectbits`;
2. if no successor survives, return the failing bit;
3. otherwise sort the successor tokens;
4. erase exact duplicate `connect_bitdata` values.

This is the strongest direct source witness of BRC found in R022.

Under fixed `(lower, upper, t, bit)` context, the remaining continuation is computed from the rolling connector token plus that fixed context. Exact-equal connector tokens therefore have the same remaining connector continuation.

**Semantic scope of the source-backed merge:**

- safe for connector feasibility / final-support existence;
- does not preserve multiplicity or provenance;
- not a proof that arbitrary nonidentical tokens with equal endpoint values may merge;
- not a proof that the six-field interface is globally minimal.

The code later rebuilds transition chains (`bitdatastart`, `bitdataend`, `bitdatanewcond`) to recover full path conditions and score them. Thus first-pass duplicate removal is best interpreted as **feasibility-state recoalescence**, not as deletion of every full-path alternative.

---

## E. Failure-prefix / negative-cone certificate

**File/function:** `src/md5connect/connect.cpp :: md5_connect`

If `md5_connect_bits` fails at bit `b`, the connector:

1. records the failure depth;
2. uses sorted lower paths and `binary_search_lower_paths` to find later lower paths sharing the same relevant lower-path prefix through `b`;
3. builds masks for `dFt`, `dFtp1`, `dFtp2`, `dFtp3`;
4. includes bit `b` only for the residual terms that `connectbits2` determined were actually involved;
5. marks matching later lower paths as skippable (`isgood[j]=b+1`).

This is structurally a **context-relative no-completion certificate**:

`same relevant prefix + same consulted residual prefix -> same failure through bit b`

The certificate is revalidated/invalidated when upper-path context changes.

BRC abstraction:

**No-Completion Cone Certificate (NCC)**

`NCC = (context, stage, failure_depth, prefix_signature, dependency_mask, proof_mode)`

Contract:

Every branch matching the certified prefix signature under the same context has empty residual completion support for the tested continuation.

Prior-art boundary: this is closely rooted in nogood recording, memoized failure, prefix pruning, and conflict-directed search. R022 does not claim a new search algorithm here.

---

## F. Path scoring / branch-local freedoms

Connection results are cleaned, verified and ranked by condition count / tunnel strength / combined score before becoming `bestpaths`.

Marc Stevens' MD5 work describes tunnel freedoms whose changes leave an earlier path segment unaffected until a later MD5 step. Structurally this motivates **branch-local partial safe moves**.

R022 does not treat “tunnel” or “neutral bit” as new mathematics. Generic transfer requires:

- an explicit legal domain;
- preservation of the current branch/interface invariant;
- a declared future horizon;
- composition-domain checks.

---

## G. Architecture-to-BRC mapping

| Source mechanism | BRC object | Exact transfer status |
|---|---|---|
| five-way md5collgen dispatch | Branch Signature Router | exact as control routing; not payload compression |
| forward path populations | forward branch cone | exact structural carrier |
| backward path populations | backward branch cone | exact structural carrier |
| six-field `connect_bitdata` | context-relative residual branch token | source-backed sufficient token; minimality unproved |
| per-bit expansion | branch split/execute | exact structural trace |
| `sort + unique` | safe local recoalescence | exact for connector feasibility/support under fixed context |
| failure-depth prefix skip | No-Completion Cone Certificate | exact source mechanism; generic algorithm rooted in nogood/prefix pruning |
| tunnel/neutral freedom | branch-local partial safe move | useful analogy; legality is context-specific |
| timeout and `k -> k-1` | rollback controller | heuristic only; not causal-minimal |
| birthday/forward/backward/connect split | bidirectional BRC-Connect | algorithmically MITM-like; BRC value is typed exact interface semantics |
| path-count / condition bounds | adaptive branch budget | valid resource axis; heuristics may lose global exactness |

---

## H. Source-grounded conclusions

1. md5collgen gives a clean example of **small control signature over a larger payload**, but not of full state collapse.
2. HashClash gives a much stronger BRC witness: **runtime branch expansion followed by exact residual-state recoalescence**.
3. The connector also carries a dual negative mechanism: **failure-prefix certification that removes an entire homologous branch cone**.
4. Endpoint equality alone is not the connector interface. The code explicitly carries residual/carry information and lower/upper path constraints.
5. HashClash's one-stage timeout rollback must not be upgraded into an exact causal-rewind theorem.
6. The strongest reusable extraction is not “parallel search”; it is a typed split/execute/recoalesce/connect/prune interface with explicit semantic scope.
