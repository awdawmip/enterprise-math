# R90 — Persistent residue-envelope AVL pruning theorem

Date: 2026-11-12. Status: author-side proved lemma and exact executable verification. This is the auxiliary rational circular-source model, with frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; it does not change P000 or native X6. Predecessors: R87 champion (`6c7908dd76cb4114e2c37c2f7f8d36b75e111305`), R88 persistent time fibers (`a74395dcf54b4f437cfab0b7b2105ca3a1c259ad`), R89 exact union-box exclusions (`bd6838c52bef14257aa934fbfaeee689bfe9167e`).

## Model and exact deliverable

Let E be a finite collection of integer source identities (t,branch), let j,a,b be integers, x rational, and θ real in a closed rational query interval I=[L,U]. Put s_t(θ)={x+(t−j)θ}, A(θ)={aθ}, B(θ)={bθ}, where {z}=z−floor(z). Source time t qualifies if s_t belongs to the directed half-open circle arc [A,B) (empty for A=B). W_E(θ) is the lexicographically latest qualifying identity, or NONE. Compute STABLE_NONE, STABLE(identity), or CHANGES with two rational witnesses of distinct directly evaluated winners for **all real** θ in I.

Fix one reduced rational phase anchor θ0=p/q, q>0. An R89 OUT box is a fully verified certificate for a parameter interval J, congruence class r mod q, source time interval H=[lo,hi], and exact signature (j,x,a,b). It asserts no source with that congruence in that time interval is a member for any θ∈J. R89 proved its source-lift/target-enclosure construction and finite closed-rectangle coverage algorithm.

## Theorem R90.1: persistent subtree residue summary

For every nonempty subtree v of an immutable AVL keyed by source time, define S_v as the set of (r,minimum source time in residue r,maximum source time in residue r), taking only residues present in v. Store the complete branch-identity fiber at each source-time node independently of S_v. Derive S_v by merging the exact child summaries with the current node's time. All AVL insertions, deletions, successor replacements and single/double rotations create new nodes and recompute S_v from their actual child pointers.

**Proof.** For a leaf, the summary has one residue and exact singleton extrema. For an internal subtree the set of source times is precisely the disjoint union of child times and the node time. Minimum and maximum in each congruence class therefore equal the merged extrema. Structural induction applies after every balancing operation; the rotations need no special semantics beyond correct reconstructed child relationships. Persistent updates retain all previous roots and branch fibers, hence the statement holds independently for each historical version. For m distinct times and fixed q, an AVL edit allocates O(log(m+1)) structural nodes and requires O(q log(m+1)) summary comparisons, with big-integer bit costs additional.

## Theorem R90.2: exact whole-subtree exclusion

For query I and signature σ, suppose for **each** triple (r,l_r,h_r)∈S_v that the union of previously certified matching R89 OUT rectangles covers I×[l_r,h_r]. Then every identity in v is disqualified at every θ∈I.

**Proof.** Fix any (t,branch) from the subtree and any θ∈I. Its residue r occurs in S_v, and t lies in its certified time interval. The rectangle coverage selects a valid matching OUT box containing (θ,t), which yields ¬M_t(θ). This is valid for every such identity and parameter. Branch data need not enter membership certification, but remains stored for winner recovery and future deletions. The proof holds separately on any old immutable root. If a cover test fails, traverse normally; failure to construct a box is not evidence of qualification.

**Closed boundary detail.** Test every clipped parameter-box endpoint and the rational midpoint of every adjacent open gap. At each atom the union of active *closed* time intervals must contain the full requested [l_r,h_r]. For a zero-width time range [t,t], the implementation explicitly verifies an active interval contains t; an empty active family does not cover it. Consequently the proof includes isolated real parameters and endpoints, not merely samples.

## Theorem R90.3: champion correctness with certified pruning

Compute w0=W_E(L) directly. Test candidates with time greater than time(w0), or all times if w0=NONE, descending through the AVL. Reject an entire subtree only by Theorem R90.2, and otherwise use the exact R77/R87 polarity oracle P_t=∃θ∈I M_t(θ) at each remaining candidate time, cached by (t,polarity,I,j,x,a,b). If a positive witness z occurs, W_E(z) differs from w0 and gives a verifiable CHANGES pair. If no candidate succeeds and w0=NONE, return STABLE_NONE. Otherwise test N_time(w0)=∃θ∈I ¬M_time(w0)(θ). A true N gives a CHANGES witness evaluated against the complete identity set. A false N means w0 qualifies everywhere and no later time qualifies, proving STABLE(w0).

**Proof.** Every pruned subtree is universally OUT by R90.2. Every unpruned positive polarity test is exact by the six-family integer-crossing critical partition. If any source later than w0 is ever qualified, a returned positive witness establishes the change; otherwise w0 can change only by losing its own membership, witnessed by N. The cases exhaust the possibilities. The algorithm preserves complete branch identities, tie order and history. Correctness is exact for the declared finite E and real θ∈closed rational I. Worst-case visitation remains O(m); cover scans, exact rational arithmetic and index construction have additional costs.

## Executed verification, November 12, 2026

A pure standard-library Python/Fraction implementation performs 192 persistent identity edits and 192 historical-version full-real interval comparisons, plus 120 signed-observer/label/signature variations. At the complete independent critical partition's endpoint and open-cell midpoint probes, it checks both the accelerated and unaccelerated classifiers against direct full-identity winner evaluation; 6,015 reference parameter atoms were inspected. CHANGES witnesses are checked directly. The 193 retained historical roots share 513 reachable AVL node objects; 3,684 total construction calls occur across histories and benchmarks. All assertions passed. Dynamic comparison only: 212 accelerated vs 227 baseline exact polarity oracle calls. The additional 120 stress queries are counted only in the accelerated aggregate (455).

Controlled family: E_n={(5,1)}∪{(18+16k,0):0≤k<n}; θ0=1/16; j=x=0, a=4,b=8, I_n=[1/16−1/(10000(n+1)),1/16+1/(10000(n+1))]. A verified one-box certificate excludes all higher times, while time 5 remains qualified throughout. The comparator uses the *same* persistent AVL and exact polarity oracle but no OUT-box pruning. Nine cold evaluations of each query on one Python process:

| Higher OUT times | R90 oracle calls | Comparator calls | Cover tries | Skipped identities | R90 median ms | Comparator median ms |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 4 | 17 | 6 | 13 | 0.419 | 1.014 |
| 64 | 6 | 65 | 10 | 59 | 1.077 | 4.694 |
| 256 | 8 | 257 | 14 | 249 | 2.851 | 17.323 |

Timings are illustrative single-process medians, not statistically independent machines or a full amortized three-index benchmark. The complete lossless source is in `check_r90.py.gz.b64`, decode using `base64 -d check_r90.py.gz.b64 | gzip -dc > check_r90.py`; run `python check_r90.py`. The command produces the JSON fields in `verification.json`. Expected banner: `R90_PASS 192 455 227 16 3684`. Local complete paper, plaintext code and proof bundle have matching source content; source and the entire result remain reproducible without external libraries.

## Actual control status and next discriminating unit

Native session start request `r90-20261112-research1-continuation-v1` returned `SESSION_ISSUANCE_QUOTA`. Exact current `RS-S23-AV` task lookup request `r90-20261112-r1-s23-lookup-v1` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`. There is no authorized RA, shared CLAIM, independent Review or Result for this author-side result. No P000 or native X6 promotion is implied.

Next R91: compare the end-to-end exact STABLE/CHANGES systems (R83 temporary heap, R86 merged profile, R90 cached persistent subtree), **including** GCD/phase-index construction, box generation, large-integer bit cost, whole-history retained memory, and rational witness recovery. Examine changed query intervals with a dynamic certificate index.
