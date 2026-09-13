# Cell address adapter V2: stable identity, frame aliases and layer views

Progress-Event-ID: cell-address-adapter-v2-20260913-a8d47f21
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21
Session: local-chat-gap-origin-a8d47f21 (locally assigned, not platform-authenticated)
Status: CONDITIONAL_HAND_PROOFS_AND_EXECUTED_EXPERIMENTAL_ADAPTER; NOT_FOUNDATION; NOT_WORKING_TRUTH
Source snapshot: awdawmip/enterprise-math@06919d4de82c339e34e8470a9a8aa263a65e0cea.
User scope: continue the compatibility audit for address-only Cell coding, with displayed origin/axes excluded from operations.

## Recovery and source boundary

Consume, do not restart, research_notes/CELL_ENCODING_COMPATIBILITY_CHECKLIST_20260912_A8D47F21.md at 7bd3ae92e0fd2207742fe0c4418a260405e886ac. It is already bound in the canonical activity record. The earlier Chat attachment's pending-write status is no longer sufficient evidence of missing source. Its eight-file manifest was verified locally; its old PASS report was not rerun or merged with the separate repository report.

Current native definition blob remains d5afee11cea0ace14a11f984e6374a95d399a953. Current geometry.py blob remains a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152. The attached exact original geometry.py is reused unchanged. This is an experimental reference adapter, not a production migration. No Cell is deleted; the old zero-labeled Cell remains. No native direction, metric, unit, transition, physical dimension, time law, boundary, Foundation, or worldview is changed.

## 1. Identity is not a layer or address spelling

Keep separate: CellKey=(fixed-native-chart namespace, complete signed X6 coordinates); Address=(namespace, immutable full frame descriptor, six positive digits, version); LayerView=(Address, LayerScheme, layer); DisplayReference. Only Address is accepted at address-operation interfaces. LayerView and DisplayReference are rejected as operands. CellKey is spatial identity, not the complete decorated packet state. Ports, fields, time and branch history must remain separately typed.

For a frame f=(b,p), with integer offset b and an axis permutation p, define eta(n)=2n+1 for n>=0 and eta(n)=-2n otherwise. E_f(x) has digits eta(x[p_j]-b[p_j]); decode sets x[p_j]=b[p_j]+eta_inverse(digit_j). Odd positive a decodes to (a-1)/2; even positive a to -a/2. Bijectivity of eta and p proves D_f E_f=id and E_f D_f=id on that frame's valid codes. Frame descriptors must match the immutable registry; same tag with changed offset/permutation is rejected. No hash is asserted collision-free.

Layer schemes are finite nonempty seed sets in the reference implementation. L_S(x)=1+min_s ||x-s||_1 is explicitly the unobstructed full-lattice layer, not an obstacle-domain graph layer. Changing S changes a view only, not CellKey or Address. No final production S is selected. The code schema is an experimental candidate.

## 2. Multiframe aliases require semantic equality

Let A be the disjoint union of valid address sets across frames. The aggregate decoder D:A->C is surjective but not injective when multiple frames are used. Therefore the single-frame bijection theorem must not be misapplied to A as a whole.

Define a~b iff D(a)=D(b). Then A/~ is bijective with C. Operations and scalar observers must respect this equivalence. Same-cell tests use D(a)=D(b), not raw address equality. H_gf=E_g D_f satisfies H_hg H_gf=H_hf by cancellation of D_g E_g. This proves consistent frame conversion without a distinguished physical origin.

For native transition T_i, use E_g T_i D_f; i remains a native direction label, not the index of a displayed axis. The adapter's distance delegates to the existing geometry.l1_distance on decoded coordinates. Its native squared metric uses the existing sum-of-squares displacement law. Passing Address itself into the old sequence-based l1 function fails rather than silently computing on digits. Deliberately extracting digits remains misuse, not a valid metric.

## 3. BRC: deduplicate aliases, preserve physical branches

REUSE_APPLIED: prior labeled-walk transport theorem and native signed-path BRC. REUSE_EXECUTED: unchanged geometry.l1_distance and graph_distance. This is an address-adapter extension, not a new BRC family.

An imported edge declaration retains an authoritative edge ID, decoded source/target, native axis/sign and exact positive rational weight. Repeated identical declarations of the same edge ID are aliases and deduplicated. A conflicting declaration for one ID is rejected. Distinct established edge IDs are never merged merely because endpoints match. The importer assumes IDs name actual branches in one import context; it does not authorize inventing new native transitions.

Proof: after vertex canonicalization and edge-ID normalization, the decoded vertex/edge incidence structure is identical to the original. A walk is an ordered sequence of those physical edge IDs with matching endpoints. It is unchanged as such a sequence; product weights and alternative-branch multiplicities are therefore unchanged. Compression retains edge identity/ports before computing counts or weight histograms. No signed/phase cancellation conclusion follows from positive weights.

Exact witness: a two-edge directed chain represented in three charts yields six edge declarations. Naively treating all declarations as independent gives 3*3=9 two-step paths; normalization yields the original one. With edge weights 1/2 and 1/3 its histogram is {1/6:1}, not {1/6:9}. A synthetic already-declared parallel first edge of weight 3/4 is retained as a distinct branch, giving {1/6:1,1/4:1}. This fixture tests branch identity; it does not extend the native graph.

## 4. Moving reference frames are not motion

For time-dependent charts E_t and native evolution F_t, the correct representation is a_(t+1)=E_(t+1) F_t D_t(a_t). Induction gives D_t(a_t)=x_t. If F_t=id, reframe alone leaves the native Cell unchanged. Keeping digits but substituting a new frame descriptor generally changes the decoded Cell: it is not a valid reframe. The former global time-law questions are not newly solved or invalidated.

Finite domains must be transported as sets E_f(Omega), including boundaries and initial states. Integer code range 1,2,3 decodes to 0,-1,1, not the old domain 0,1,2. This known migration issue is retained in the new regression suite.

## 5. Actual new verification

PASS with Python 3.13.5, exact integer/Fraction arithmetic and hash-verified unchanged geometry backend:
- 729 native keys with 2187 distinct three-frame aliases and 2187 serialization roundtrips;
- 6561 cross-frame same-cell/zero-displacement checks;
- 8748 signed moves with permuted input/output frames;
- 2187 independently changed layer-view pairs; a fixed address changes view layer from 1 to 10 without changing identity;
- 4096 mixed-frame endpoint pairs using the original graph_distance backend;
- 8748 time-varying-frame updates;
- 29 malformed/type/version/frame/origin/edge-conflict rejection tests;
- alias-path inflation and genuine-parallel histogram witnesses above.

Executable siblings: research_notes/cell_address_adapter_v2_20260913_a8d47f21/cell_address_adapter.py; test_adapter.py; results.json.
SHA256: adapter d93dd2d74057bb7221ca4ef5c114da3d0233fa903b6c617421074ffcba1e5832; checker 6d7adbe3a075fe739edfd5fbbb55d5582bb421011a6f5d86b76ad928206aaa21; results e457e2a93cb62351f3125f40762e590d8aed4f0538bca581400bc6ab9a324c1c.
Run locally with the bundled original backend, or in the repository with test_adapter.py --geometry src/enterprise_math/geometry.py. The checker rejects a changed backend hash pending an explicit compatibility review.

## 6. Updated obligation boundary

Closed at conditional-proof + prototype level: stable identity separated from changing layer labels; invertible integer frame codec; canonical multi-chart equality; strict serialized-frame validation; transported movement/distance; physical-edge alias normalization with branch preservation; tested time-varying chart transport. These do not constitute Lean or production admission.

Not to restart: the already-verified unchanged native distance, adjacency, path/BRC, common-depth and symmetry mathematics. The prior compatibility checklist remains the controlling inventory.

Still required for production adoption: select the actual first-layer population and finite/obstacle graph semantics; freeze the production schema and canonical namespace; audit every caller, storage key, boundary and cache; make physical edge IDs authoritative at the data producer; preserve full packet decorations; run complete repository and Lean gates. No performance gain or all-paper migration claim is made. This continuation delivers the next experimental adapter, proofs and tests; it does not silently choose those deployment/modeling policies.

Standard background checked: official mathlib4 Logic.Equiv.Defs (two-sided inverse equivalence) and Combinatorics.SimpleGraph.Maps (relation-preserving relabeling). No Lean execution is claimed.
