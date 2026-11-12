# R103 — Persistent AVL net overlays and certified symmetric-difference pruning

Date: 2026-11-12. Author: EM-DIRECT-DA0271 (TASK_RESEARCH). Research activity: RA-B83A20E963D8C41BB444A868.
Frozen science pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor R102: `15380f01577e2e461444fd4d5b27e8b653509531`; R101: `fb4776ca9a53ca42ceaf16d09aeb54cd73509773`.
Scope: finite rational circular-source auxiliary model. Native X6/P000 and the frozen scientific source remain unchanged. Author-side proof and computational audit; independent review pending.

## Exact setting

For a signature sigma=(j,x,a,b), j,a,b integers and x rational, and an identity u=(t,branch), set s={x+(t-j)θ}, A={aθ}, B={bθ}, fractional part in [0,1). Eligibility is membership in the directed half-open circular arc [A,B). When A=B the arc is empty. For A<B require A≤s<B; otherwise require s≥A or s<B. Identity ranking is descending lexicographic, retaining the entire branch identifier. Top_k(S,θ) returns the first k distinct eligible identities.

## R103.1 — Persistent AVL terminal-overlay theorem

Fix a finite base E and any terminal source set F. Its unique canonical base-relative overlay is D=E\F and H=F\E, satisfying F=(E\D)∪H, D⊆E and H∩E=∅. Store D and H as separate immutable AVL search-tree roots. An edit adding u removes u from D when u∈E and otherwise inserts it into H. Removing u inserts u into D when u∈E and otherwise removes it from H. Retain the edit-parent pointer separately for provenance.

**Theorem.** For every finite sequence of such edits the stored roots represent exactly its terminal set and preserve all earlier roots. For an overlay with m keys, each single edit creates O(log(m+1)) nodes with ordinary AVL path copying and rotations, treating identity comparisons as unit cost.

**Proof.** The four cases update the membership of precisely u relative to E and preserve all other memberships, establishing the invariant by induction. AVL recursive insert/delete and rotations preserve in-order keys, maintain logarithmic height and create new nodes along the affected path; constructors never mutate retained roots. Each rotation allocates constantly many new nodes. Therefore the number allocated per edit is bounded by a constant multiple of the logarithmic search path. If integers have unbounded bit length, comparison cost is separately charged. QED.

For d=|D|, R101 gives, for all real θ and k≥1,

Top_k(F,θ) = Top_k((Top_(k+d)(E,θ)\D) ∪ {u∈H : M_u(θ)}).

Thus the history-depth-independent terminal overlay can query an exact base Top prefix oracle without replaying historical operations. The reference implementation scans the sorted base, which is included in its actual query cost.

## R103.2 — Version-paired OUT equivalence theorem

For F_i=(E\D_i)∪H_i (i=1,2), where D_i⊆E and H_i∩E=∅, the symmetric difference is exactly

F_1 Δ F_2 = (D_1 Δ D_2) ⊔ (H_1 Δ H_2).

For a closed rational interval I suppose every identity in that symmetric difference has an exact certified OUT predicate M_u(θ)=false for **all real θ∈I**, matching the complete observation signature and time coverage.

**Theorem.** Under these hypotheses, for every θ∈I and k≥1, Top_k(F_1,θ)=Top_k(F_2,θ).

**Proof.** Inside E, an identity has different presence in the two terminal sets exactly when it belongs to D_1 Δ D_2. Outside E, the corresponding difference is H_1 Δ H_2, and these sets are disjoint. By hypothesis all discrepant identities are ineligible throughout I. The eligible identity sets of the two histories coincide pointwise, and their complete descending ranking and all Top-k prefixes coincide. QED.

The shortcut requires only the four net overlay maps, their symmetric differences and certified interval-index lookups. Neither a scan of the common base nor an explicit full-period profile is needed when the certificate succeeds. Absence of a box from the selected immutable historical certificate-index root means it is unavailable for that query.

If the sufficient shortcut does not apply, take the union of terminal source times and generate every rational cut in I where one of the six integer-slope phases aθ, bθ, (t-j)θ+x, (t-j-a)θ+x, (t-j-b)θ+x and (a-b)θ is an integer. Check every cut and a rational midpoint of every intervening open gap, respecting half-open equality at cuts. This is an exact complete finite interval comparison and returns a rational witness of any mismatch.

## R103.3 — Constructive all-real OUT family

For sigma=(0,1/4,0,1), choose rational 0≤L≤U<1/4 and a time bound 0≤t≤T with 1/4+TU<1. For θ∈[L,U], s_t=1/4+tθ belongs to [1/4,1), and θ<1/4≤s_t; the arc is [0,θ) (empty at θ=0). Therefore every source in that time range, with any branch ID, is OUT for every real parameter in the interval. Four such all-real boxes are inserted into an immutable balanced interval tree with augmented maximum upper bounds. A box is usable only if it covers the *entire queried interval*, exact time and exact signature. Indexed lookup cannot change the exact source predicate.

## Reproduction and evidence

Decode `check_r103.py.gz.b64` using Python: `gzip.decompress(base64.b64decode(open("check_r103.py.gz.b64","rb").read()))`, write `check_r103.py`, then run it with standard Python 3. It uses `fractions.Fraction` for every mathematical assertion, seed 10320261112, and writes `verification_r103.json`. SHA256 of decoded Python source: `8284bc2674676af65220476a754f977505ee8539838be3dc1ae2c7981cf33415`.

Observed exact audit: 120 AVL version invariants; 3,240 three-way historical point Top-k checks (direct set, lazy replay and persistent overlay), 59,456 local cut/midpoint Top-k checks, 40 history comparisons yielding 14 exact rational difference witnesses and 19 certificate-only equalities, and 50 additional adversarial equality cases using independently certified OUT boxes. A monotone AVL stress test preserved 480 historical roots, allocated 4,461 path-copy nodes, and observed at most 12 allocated nodes per edit. Two historical OUT index roots were checked without retroactive certificate inheritance. All assertions passed: `R103_PASS 3240 59456 40 19 14 160 72`.

Measured milliseconds, single Python process with repeated runs (resource observations only): 80 point queries on a 160-edit toggle chain, raw lazy replay 146.06, net overlay 13.68, direct source scan 37.85. For 80 narrow-range queries in [0,1/1024], explicit profile preparation 1.73 and subsequent profile queries 0.073, versus net overlay queries 13.78. For 80 wide-range queries in [0,1], explicit preparation 258.23 (276 cuts) and subsequent queries 0.421, versus net overlay 4.70. The experimental timings are stored in `verification_r103.json` and depend on workload and runtime. Structural counts are exact for the recorded process; live object byte costs, bit operation costs and future version mix are still to be measured.

## Control, mathematical status and next question

Exact native task read of `RS-S23-AV` returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`, request `em-research1-r103-20261112-2204-task`. The own native researcher session is `MCP-ebb177e030eb460c95571e2314fcfdb9`, Researcher ID `EM-DIRECT-DA0271`, activity `RA-B83A20E963D8C41BB444A868`; registration is not a CLAIM or independent review. This report documents author-side science, not a formally frozen Source Result.

R104: test version-aware checkpoint placement versus raw DAG and explicit interval materialization under mixed updates and historical query distributions; include actual retained Python object bytes, exact rational integer-bit work, interval-index visits and witness recovery. Seek a stronger version-paired domination certificate that can resolve some overlapping active symmetric differences without evaluating the common source profile.
