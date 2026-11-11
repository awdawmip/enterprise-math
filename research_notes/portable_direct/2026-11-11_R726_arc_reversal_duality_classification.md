# R726 — Arc-reversal duality, orientation-free classification and positive history counts for sharp V17/CNB carriers

Date: 2026-11-11 (Asia/Shanghai). Research continuation of R725, R723, R721b. Model: rooted five-axis, directed V17 slot replacement with cyclic nonbacktracking (CNB). Task context: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen scientific baseline: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5).

Evidence type: exact elementary bijection and arithmetic finite checks, author-side draft; independent scientific review open. Reuses R725 complete six-orbit classification at source commit a9ba60cab51fc98e4b39f73e5d0eda7f49c51bb3, not an independent re-enumeration of 60 choose 15.

## Definitions

The ten triads are the three-subsets of axis labels 0,1,2,3,4. There are 60 directed Johnson-neighbor arcs (u,v) where the triads share two axes. The root triad and initial ordered frame are both 012. A length-m positive rooted closed walk v_0=012,v_1,...,v_m=012 is CNB if v_(i-1) != v_(i+1) for all cyclic indices (including the seam). V17 transport replaces the one departed axis in its original frame slot with the one entered axis. For an arc-permission set E, H_m(E) is the set of six possible resulting root-slot frames. Let N_m(E,h) count positive walks with that frame (counting multiplicity of distinct ordered walks).

Let r(E) = {(v,u):(u,v) in E} be simultaneous reversal of every permitted arc. Let G=S3 x S2 act by bijective axis relabelings that keep the root triad set 012 fixed. Relabeling preserves the full-support property but changes the initial root-frame gauge as appropriate.

## Theorem R726-A: all-length reversal bijection

For every directed permission set E, every length m>=3 and every h in S3,

    N_m(r(E),h^(-1)) = N_m(E,h).

Consequently H_m(r(E)) = {h^(-1):h in H_m(E)} and full six-state support is preserved by r for each length.

**Proof.** Reverse the list of triad vertices of a rooted closed walk. All consecutive transitions (u,v) become (v,u), so the walk lies in r(E). CNB is invariant under reversal, including v_(m-1) != v_1 at the closing seam. For any adjacent triads u,v, V17's replacement transport T_(u,v) is a bijection on ordered frames with inverse T_(v,u). It also commutes with permutation of the three slot positions. Thus a closed path with total root-frame permutation h has reverse path with permutation h^(-1). Reversing twice returns the original ordered path, proving a multiplicity-preserving bijection. No signed cancellation or floating arithmetic occurs. QED.

## Theorem R726-B: classification modulo physical-edge direction reversal

For the 72 labeled size-15 carriers classified by R725 from the exact conditions H_4(E)=H_5(E)=S3, the G-orbit indices map under r as

    1 <-> 2,    3 <-> 4,    5 <-> 6.

In particular none of the six G-orbits is reversal-invariant. The action of G x C2 has three orbits, each of size 24, on these 72 networks. Exactly two 24-member extended orbits (48 labeled networks) realize H_m(E)=S3 for all m>=4; one 24-member orbit passes lengths 4,5 and fails at m=6.

**Proof.** R725 gives six exact canonical 60-bit masks and proves that their six disjoint G-orbits, each of size 12, exhaust the 72 candidates. Define bit reversal using the explicitly ordered 60 Johnson arcs. The finite exact verifier below reverses the arcs in each canonical mask and checks membership in each canonical G-orbit. The resulting unique matches are [2,1,4,3,6,5]. Thus r pairs the G-orbits without fixed orbit. Reversal and axis relabeling commute, so the extended group has order 12*2=24 and each paired union is one orbit of size 24. R725 classifies orbit indices 1,2,3,4 as all-length carriers and 5,6 as first failing at length 6; the reversal bijection preserves these properties. QED.

## Corollary R726-C: typed size is orientation-dependent

R725's directed-forward lifted-state stability certificates have counts (270,180,180,270,nonpersistent,nonpersistent) for classes 1,...,6. Reversal pairs a 270-state representative with a 180-state representative twice, while preserving all positive closed-path counts and all six-state support properties. Therefore forward stable lifted-state cardinality alone is not an orientation-invariant information complexity of the unoriented carrier. It remains valid as a cost measure for the specified forward execution direction and algorithm.

For example, exact positive rooted CNB history totals at m=4,5,6,7 for representatives by reversal-extended pair are:

| m | orbit-pair {1,2} | orbit-pair {3,4} | orbit-pair {5,6} |
|---|---:|---:|---:|
|4|7|7|6|
|5|8|8|6|
|6|13|14|6|
|7|42|43|24|
|8|97|97|60|
|9|163|169|88|
|10|309|329|132|
|11|721|751|312|
|12|1556|1608|692|

The two all-length *unoriented* types differ in exact history multiplicity already at m=6 (13 versus 14), although each has complete six-state Boolean support.

## Verification and scope

The executable Python program R726_DIRECTION_DUAL_VERIFY.py contains the six canonical masks, independent arc reversal, G-orbit generation, exact integer positive-path dynamic programming through m=12, and per-frame inverse checks against the actual arc-reversed masks. It asserts the three paired extended orbits, nonexistence of a self-dual G-orbit among the six, the total 72 candidate masks and the counts above. It emits R726_DIRECTION_DUALITY_PASS with a complete exact JSON data table.

The finite orbit conclusion depends on R725's documented complete classification as a source theorem. The reversal bijection itself is independent of the R725 enumeration and holds for every directed V17/CNB network, not merely 15-edge networks. These are precise combinatorial path/permission statements in a five-axis slice of the P000 six-axis world. Actual V29 Link/Port inventory and event-time constraints and V39 future-observer quotient have yet to be checked.

## Next discriminating unit

Use the two orientation-free viable carrier classes, not four directional G-classes, as the two nonredundant structural comparison targets. Retain directed execution orientation when event-time and inventory are nonreversible. First map both pairs to V29 signed force incidences and positive port ledgers, and measure genuine forward/reverse staging costs under the actual permitted transition relation. Then compare observer-specific BRC histograms, not only Boolean six-state support.