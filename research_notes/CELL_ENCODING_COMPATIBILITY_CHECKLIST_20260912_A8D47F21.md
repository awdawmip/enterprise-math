# Cell address-only compatibility audit and proof-obligation checklist

Progress-Event-ID: cell-encoding-compatibility-checklist-20260912-a8d47f21
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21
Session: local-chat-gap-origin-a8d47f21 (locally assigned, not a platform ID)
Status: CONDITIONAL_HAND_PROOFS_AND_EXACT_EXECUTED_INTEGRATION; NOT_FOUNDATION; NOT_WORKING_TRUTH
Source snapshot: awdawmip/enterprise-math@c2211215146d000f0a08038af02f3005d835ee81.
Question: first try compatibility of address-only Cell coding, with displayed axes/origin excluded from operations; identify what must be recalculated/reproved and what need not.
Prior frontier consumed, not restarted: ADDRESS_ONLY_CELL_CODING_20260912_A8D47F21.md at 7b5379fc6fb5077d6ae906f21b76b94029fc6797. This audit adds current-module execution, a six-axis box, exact weight histograms, symmetry/layer checks and a migration checklist.

## 1. Exact sources and scope

At the source snapshot:
- definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; blob d5afee11cea0ace14a11f984e6374a95d399a953; full file read.
- definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md; blob b0988c9fa0f2f7c3314784673cf21a2df2340ebe; current sections 1-4 read, later mathematical sections reused from the preceding source audit.
- src/enterprise_math/geometry.py; blob a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152.
- src/enterprise_math/diagonal_quotient.py; blob 3ac387c0103665943f13ba9e306a6167080c701d.
- src/enterprise_math/operation_quotient.py; blob 758a65de02a434446936cd7e37b2ae604eade863.
The last three complete files were retrieved through GitHub, locally materialized, matched byte-for-byte by Git blob hash, and executed unchanged by path imports. Unrelated package initialization was not loaded. The source directory tree and __init__.py were used for routing, not as an exhaustive dependency audit.

Freeze: same Cell population, same twelve signed primitive transitions, same native metric, same state/port/weight decorations, same physical boundaries/initial conditions. The display reference is a separate nonoperational type. The former chart-zero Cell remains present. Arithmetic zero and zero displacement remain valid. No physical dimension is added. Final production first-layer membership and within-layer code are not chosen by this test.

## 2. Compatibility proofs

P1 Encoding and typed operations. Let E:C->A_valid be a bijection with inverse D. Transport each existing operation by F_E=E F D (decode every Cell argument for multivariate operations); preserve partial domains. Scalar observers use f_E=f D; relations are transported argumentwise. For a signature with additional state sorts, transport the entire required decorated state and leave unrelated scalar sorts unchanged. Induction on terms and then formulas proves preservation of the corresponding typed identities and propositions. Numeric code operations are not automatically the transported operations. No primitive Cell addition is introduced by this statement.

P2 Display independence and native action. The combined representation is (encoded model, display metadata) and all operational maps factor through the first projection. Changing only display origin/axes leaves every output unchanged. Native translations satisfy T^E_v=E T_v D, hence T^E_0=id, T^E_v T^E_w=T^E_(v+w), and D(T^E_v(a))-D(a)=v in the retained signed chart. Display nonparticipation does not erase native direction labels.

P3 Paths and BRC. Map every vertex and every labeled edge of a walk via E. D is the inverse walk map; length, order, orientation, composition, reversal and transported edge weights are preserved. This is a bijection of labeled realizations, not merely a bijection of endpoint support. Thus shortest lengths, shortest multiplicity and fixed-length weighted histograms are preserved. Apply the existing exact native laws N_min(z)=sum|z_i| and B_min(z)=N_min(z)!/product|z_i|!. Empty paths still have length zero and multiplicity one. REUSE_APPLIED to the native BRC theorem; no signed/phase cancellation is inferred from positive weights.

P4 Native metric and observables. d_E(a,b)=d(Da,Db), so d_E(Ep,Eq)=d(p,q). Common-depth repair and selected-slice membership are evaluated after decoding. The previous min-zero kernel is not turned into a new identification of Cells. For s=can(x)+1 and h=min(x), x=s+(h-1)1. For the existing chart-coordinate composition on repaired states, s_new=can(s+t)+1 and h_new=h+k+min(s+t)-2. Positive-path depth repair becomes k=(m-sum(s)+d)/d when s=r+1. These are translated formulas, not new native distance or group laws.

P5 Symmetry, frames, and layer covariance. For an admitted native action R_g define R^E_g=E R_g D. Then R^E_g R^E_h=R^E_(gh), preserving S6 and its admitted subgroups. For two encodings define H_BA=E_B D_A. It has inverse H_AB and satisfies H_CB H_BA=H_CA. If L_S(x)=1+d_G(x,S), a graph automorphism M satisfies L_(MS)(Mx)=L_S(x). Keeping S fixed gives invariant layer numbers for all x if and only if MS=S, because S is exactly the level-one set. Thus an asymmetric first-layer fixture need not retain its layer number under a rotation. No proper nonempty S is invariant under every translation of a transitive lattice. This is an observer limitation, not loss of native symmetry.

P6 Evolution and finite-domain operators. For a fixed encoded full-state map U, F_E=U F U^-1 implies F_E^n U=U F^n. On a finite graph a simultaneous reindexing gives A_E=P A P^-1 and likewise for degree matrices/Laplacians, preserving characteristic polynomials and exact reindexed field evolution. This is a conditional transfer theorem, not a claim that all simulation software has been audited. Domains, initial states, weights, time labels and boundaries must be transported. A time-varying representation requires F_E,t=E_(t+1) F_t E_t^-1; ignoring frame changes is not justified.

P7 First layer and compression boundary. For any nonempty S in the connected integer-step graph, L_S(x)=1+min_(s in S)d_G(s,x) is well-defined; L=1 exactly on S and neighboring levels differ by at most one. It adds no O vertex or edge, does not assert radial distance one, and allows an infinite S. Layer alone does not generally determine a transition. The current operation_quotient API confirms failure for a concrete finite endomap fixture below. Within-layer identities and any required state/port data must remain available.

## 3. Actual candidate and integration results

Fixture: S={0,e1,e1+e2} in Z^6; f(n)=2n+1 for n>=0 and f(n)=-2n for n<0. E(x)=(L_S(x),f(x1),...,f(x6)). Its inverse uses odd/even decoding and validates the layer checksum. Display-origin markers, zero fields, malformed codes and booleans are rejected. This seven-field code represents six native coordinates plus an observer, not seven spatial axes.

Executed exact checks PASS:
- 729 Cells in {-1,0,1}^6; 5,832 directed adjacency entries; 531,441 ordered endpoint pairs: decoded coordinates, graph shortest lengths, shortest multiplicities and native squared metrics agree. Shortest counts were additionally compared with the native multinomial formula. The integer box is geodesically convex for these shortest signed-axis paths.
- Unchanged geometry.graph_distance: 48 pairs before/after relabeling; unchanged directed_graph_distance: 24 directed pairs.
- 8,748 primitive-action/inverse tests, including transitions outside the finite box using the infinite-code adapter.
- 9,360 S6 action probes covering all 720 permutations on zero and the twelve signed unit states; 1,215 generator-relation checks; 9,360 layer-covariance checks.
- Unchanged diagonal_quotient functions: 343 min-zero/min-one repaired roundtrips and 2,401 common-depth carry checks.
- Existing same-source squared-radius-25 three-axis shell transported: 30 endpoints and 846 shortest paths. This does not test a different layer-origin shell.
- Exact positive-rational weight histograms for all twelve-direction words of lengths 0..4: 1,12,144,1728,20736 words; endpoint counts 1,12,73,304,985; histogram-bin counts 1,12,78,364,1365. Histograms agree endpoint-by-endpoint, not only in total mass.
- Unchanged operation_quotient API on an explicitly 3-periodic x-endomap over a finite 27-state fixture: layer-only observer fails descent; full code passes; before/after refinement class counts both 4,11,15. The periodic fixture is not asserted to be an infinite native translation.
- Finite graph Laplacian reindexing: four integer field updates, 2,916 node checks.
- Seven invalid-code/origin-rejection tests and preservation of the former zero-labeled Cell.

New concrete migration witnesses:
1. geometry.l1_distance accepts the positive code digits as integers but returns 2 for E(0),E(e1), whereas the correct native step distance is 1. This is silent API misuse, not a bug in the old coordinate API.
2. Swapping axes 1 and 3 sends e1 from fixture layer 1 to fixed-fixture layer 2. A rotation wrapper that keeps the old layer checksum is invalid.
3. can(0,0,0)=can(1,1,1); a min-one offset alone does not repair identity loss.
4. Numeric code range 1..3 decodes to {0,-1,1}, not {0,1,2}; copying loop bounds can silently change the simulation domain.
5. Adding a real unit-edge origin to both ends of a two-step chain keeps distance 2 but doubles shortest paths from one to two. This is excluded by the user's address-only premise.

## 4. Checklist: old mathematics not to restart

A1 Cell population and native signed Z6 torsor; A2 twelve primitive direction actions and reverse cancellation; A3 component metric and its symmetry/triangle inequality; A4 N_min and primitive-line classification; A5 shortest/fixed-length BRC laws when labeled paths/weights retained; A6 S6 group relations and admitted subgroup action; A7 original selected-slice projection kernels, common-depth decomposition and carry identities; A8 the same Cell-relative shell counts; A9 same carrier overlap/incidence/coverage geometry under coordinate-only changes; A10 independent arithmetic results that do not use changed addresses. A9/A10 are dependency-conditional reuse claims, not a declaration that all carrier or arithmetic application code was executed. The original theorem status is not promoted by this audit.

## 5. Checklist: new bridge proofs / interface work required

B1 exact production encode/decode domain, uniqueness and roundtrip; B2 typed separation of display origin from Cell and of addresses from displacements; B3 primitive-action, reversal and path composition commuting diagrams; B4 all scalar observers decode first; B5 complete spatial/state/port/weight information retention; B6 min-one and common-depth adapter formulas if that option is selected; B7 rotation/frame conversions with a recomputed layer field; B8 first-layer membership and layer-code validation; B9 identical boundaries, initial conditions and update order after remapping; B10 compatibility aliases in documentation/schema and a Lean bridge/rebuild when machine-checked admission is sought. P1-P7 supply the general hand proofs and the candidate passed finite checks. These do not mean that an unspecified final production codec or every existing caller has already passed.

Concrete code touchpoints: geometry.graph_distance and directed_graph_distance need only relabeled graph/endpoints; geometry.l1_distance needs a decoder adapter; geometry.lattice2_sphere/ball must map their existing anchor-relative sets rather than reinterpret numeric address bounds; diagonal_quotient must receive decoded signed triples and preserve depth outside its quotient result; operation_quotient accepts arbitrary hashable identities, so preserve the operation table and observer under relabeling. No edits to these source modules were made.

## 6. Checklist: recalculate representations, not old physical answers

C1 generated address tables, reverse indexes and serialized keys; C2 plot ticks/legends/origin annotations; C3 first-layer and later-layer populations if a new S is selected; C4 caches and layer-dependent classifications after frame/seed changes; C5 encoded finite-domain membership/boundary tables; C6 performance, storage and migration checksums. Pure relabeling gives a correctness result, not a speedup theorem. Stable within-layer numbering should not renumber old Cells on domain growth unless a versioned migration is specified.

## 7. Checklist: changes that genuinely require affected new theory

D1 deleting the old chart-zero Cell; D2 making the external origin an actual neighbor/path endpoint; D3 identifying all layer-one Cells as one operational state; D4 replacing the native metric by direct code-digit arithmetic; D5 dropping common depth, omitted coordinates, ports or weights without a safe quotient proof; D6 turning a display recess into a physical spatial axis or changing units; D7 changing update/time rules or the actual boundary/initial state. These changes are not authorized or needed for the current goal. Reprove only the dependency closure actually affected, not unrelated arithmetic.

## 8. Evidence limits and disposition

This is a source-linked compatibility trial, not an exhaustive repository dependency scan, complete historical-paper review, full test-suite run, Lean build, or formal theorem admission. General native rotation dynamics, physical time calibration, and model bridges already open in the source remain open; they do not become newly invalid merely because of address coding. No Foundation/P000/worldview/Working Truth modification, production migration, task claim, or physical hypothesis promotion occurred.

Local reproducible bundle: cell_compatibility_audit, with three hash-verified original modules, check_compatibility.py, results.json, report and manifest. Checker SHA256: 8f113b57c1cbca1229e292bfb33915fe6b3a313cb8e2bbb4711fcf3108970e57. Results SHA256: ccc4e070863f50bd87a33d09f2611b10f904fb68f5f740053f266760d3e17668. The checker includes a local-vendor path and a repository-relative fallback; the hash-verified local-vendor execution is the observed test route.

Conclusion: conditionally compatible as a reversible address adapter on the existing native model. The trial and checklist objective is complete. Production adoption remains separate: fix S and the stable full codec, audit every numeric-address caller, then seek the relevant formalization/review gates without restarting unchanged native proofs.

Standard references checked: official mathlib4 Algebra.Torsor.Defs; Combinatorics.SimpleGraph.Maps; Combinatorics.SimpleGraph.Walk.Maps (length_map, map_append, reverse_map). These are background formal interfaces, not evidence of an executed Lean proof of this candidate.
