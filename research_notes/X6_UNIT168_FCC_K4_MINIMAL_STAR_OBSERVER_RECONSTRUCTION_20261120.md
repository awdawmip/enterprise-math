# X6 Unit168 — Sharp minimal FCC/K4 STAR observer reconstruction theorem

Date: 2026-11-20 (Asia/Hong_Kong).
Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2; parent objective: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905.
Source-author lineage: Researcher EM-X6-FB6990, session MCP-082892eb480e45dea6d4b9fcc0491034, logical Research conversation chatgpt-research-onhour-enterprise-math-20260923. Maintenance lane is separate.
Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. No independent Driver review, Foundation promotion, or P000 amendment.

## Source pins, actual scope, and prior art

Frozen scientific input: awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03.
Frozen earlier plane comparison: awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3.
Direct foundation producer: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, frozen blob b4d49a1bbcccad0521618c6d20f6dcfa242b420a, sections 5, 6 and 9.
Native three-axis slice producer: definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md, frozen blob b0988c9fa0f2f7c3314784673cf21a2df2340ebe, sections 3, 6, 7 and 15.
Real original source checker consuming one selected triple: experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_rebase.py, frozen blob 406b1eea574ac3235c490dc362ce76d4b072458e, source selection S=(0,1,2) and its exact min-zero recovery tests.

The frozen foundation already proves that *all twenty* three-axis coordinate observers jointly recover Z^6 modulo the common diagonal. This unit does not claim that known fact as new. The incremental result identifies the **smallest sufficient subset of the four actually established FCC/K4 STAR-slice observers**, proves the observer-connection criterion, and establishes a complete finite three-of-twenty observer classification. The historical single-slice checker does not already provide this minimum-subatlas theorem.

**Additional prior-art correction from the existing V10 source.** The already-published research_notes/X6_20_SLICE_INVERSE_LIMIT_RECONSTRUCTION_V10_20260905.md, immutable commit f5246fd204222d6c6903536f9336d02d367de173, sections 3–6, proves all-20 inverse-limit reconstruction, explicitly gives a *different sufficient four-slice cover*, and acknowledges that the established FCC four-STAR atlas already had a V2 canonical-min-zero chart-gluing theorem. Therefore neither "four STAR suffice" nor "min-zero chart gluing" is newly asserted by Unit168. The genuinely additional statement is **every three of those four STAR observers suffices and two triples never suffice** (with an exact finite classification 480/600/60 for all abstract three-subset choices). The proof here concerns source-consistent observation tuples F(z); for arbitrary independently supplied local triples, pair-overlap/gluing cycle-consistency constraints must be checked by the BFS edge-label agreement test before claiming existence of a global z. A common axis label on two STAR selections is not itself a two-axis relative overlap; this is why this decoder retains its global consistency test instead of invoking the V10 pair-overlap inverse-limit construction unmodified.

## Definitions and the exact general fiber theorem

Work in the signed native Cell displacement group Z^6, with native axis indices 0,...,5. For each three-coordinate subset S and z in Z^6 define the *relative-coordinate observer*

    Obs_S(z) = can3((z_i)_{i in S}),  can3(a,b,c)=(a,b,c)-min(a,b,c)(1,1,1).

The observer preserves the ordered/labeled three-coordinate differences but forgets the common offset in S. This is not an assertion that an arbitrary full X6 state belongs to the corresponding centered affine three-axis sub-torsor.

Let F be any family of such subsets and define G_F on the six axis indices, connecting any two indices occurring together in some S in F. Let C_1,...,C_c be its connected components. Then, for every x,y in Z^6,

    (Obs_S(x))_{S in F} = (Obs_S(y))_{S in F}
    if and only if
    x_i-y_i is a constant independently chosen on each component C_j.

**Proof.** Equality of can3 observations is exactly equality of all within-S differences x_i-x_k=y_i-y_k. Thus x-y is constant on each three-vertex clique; transitivity along graph paths makes it constant on each connected component. Conversely any component-wise constant cancels in each observed triple's min subtraction. Every S lies in one component by construction. No analytical approximation, physical-circle assumption, or unproved reduction occurs. QED.

Hence the kernel of F is isomorphic to Z^c. The family determines the original native displacement modulo the global diagonal D=Z(1,1,1,1,1,1) **if and only if G_F is connected**. Connectedness is the exact certificate for relative signed-coordinate recovery for all integer states.

## Sharp threshold for the four realized FCC/K4 STAR observers

Index the six signed-X6 axis *labels* by the edges of an abstract K4 tetrahedral incidence graph:

    0:01, 1:02, 2:03, 3:12, 4:13, 5:23.

The four native coordinate selections belonging to the already established FCC/K4 STAR subatlas are

    S_0=(0,1,2), S_1=(0,3,4), S_2=(1,3,5), S_3=(2,4,5).

**Theorem.** Each three-star subfamily out of these four is sufficient to determine the complete signed displacement modulo D, and no two three-coordinate observers, even if chosen from the entire set of twenty, suffice. Thus **three is the exact minimum** for this declared connected-subatlas reconstruction problem.

**Proof.** Two three-element supports contain at most six distinct indices. If they intersect, their union has size at most five and leaves at least one isolated index; if disjoint, they form two disconnected graph components. Therefore two can never connect all six indices. Any three K4 stars, however, have pairwise shared edge labels, and together cover all six K4 edge labels: the only omitted base vertex is a singleton, containing no internal edges. Their incidence-clique union is connected. The criterion proves sufficiency and sharpness. QED.

The exact finite classification of all C(20,3)=1140 unordered triples of different 3-axis observers, by number of components of G_F, is:

    c=1: 480 families; c=2: 600 families; c=3: 60 families.

These are an exhaustive integer combinatorial enumeration certificate over the specified finite family, independently reproducible with the checker. Of the four established STAR triples-of-three, 4/4 are connected; among six STAR pairs, 0/6 is connected, with two components each. The 480 connected three-triple families are abstract coordinate-observer families; only the actual four STAR selections are established as the present FCC full carrier-realization subatlas, and this result does not promote any of the other sixteen selections to a realized carrier.

## Constructive exact decoder, path-count consequence and witnesses

For a connected family, form directed edges with integer labels

    (i -> j): Obs_S(z)[j]-Obs_S(z)[i] = z_j-z_i.

Start any index at potential 0 and propagate potentials along a spanning tree, checking agreement on all remaining edges. The resulting integer vector equals z up to a common additive constant. Subtracting its minimum yields r=can6(z). Retain one unbounded integer depth h=min_i z_i to reconstruct the native signed displacement exactly:

    z = r + h(1,1,1,1,1,1).

Thus all native outputs depending only on z, including squared component length L_E^2(z)=sum_i z_i^2, shortest primitive event count N_min(z)=sum_i |z_i| and **positive shortest ordered native N-BRC word multiplicity**

    B(z) = (sum_i |z_i|)! / product_i (|z_i|!),

are computable after this exact repair. This concerns endpoint path *multiplicity*, not full per-path provenance or separately decorated packets; such information needs its separately declared carrier.

Sharp failure of two STAR observers S_0,S_1: the native states

    x=(1,0,0,0,0,0), y=(1,0,0,0,0,1)

give exactly the same S_0/S_1 observations, because axis index 5 is absent. Yet their native BRC multiplicities are respectively 1 and 2, and squared lengths are 1 and 2. No decoder from those two observations alone can distinguish them.

Even all four STAR observations identify z only modulo D: x=(0,0,0,0,0,0) and y=(1,1,1,1,1,1) both give four zero triples, while native shortest N-BRC masses are 1 and 720. The integer common-depth parameter is unbounded, so a universally lossless full raw-coordinate codec from relative observations requires an unbounded integer coordinate or an equivalent lossless integer representation, not a fixed single Boolean flag.

## Exact executable finite certificate

Independent integer checker research_checks/X6_UNIT168_FCC_K4_MINIMAL_STAR_RECONSTRUCTION_CHECK_20261120.py calculates all 1140 three-subset families, checks every two-subset, reconstructs every vector z in {-1,0,1}^6 for each of the four STAR three-family choices, validates depth restoration, and tests the signed native BRC witness states. It reports 2,916 restoration checks, connectivity frequencies (480,600,60), four valid three-STAR choices, six invalid two-STAR choices, and zero violations.

The exact checker was run under Python, Python -O and Python -OO, with byte-identical JSON output and explicit exception-based checks that remain active under optimization. The original R063 six-file/512-case native benchmark was **not rerun**. The finite check supports the combinatorial classification and the bounded implementation; the all-integer fiber/three-STAR theorems have the independent proof above.

## Parent-objective and Source/control state

Disposition for the frozen X6 reconciliation corpus: PRESERVE_TYPED_RELATIVE_OBSERVER and PRESERVE_LOSSLESS_DEPTH_REPAIR. This is an additional exact source-to-observer implication of the existing native foundation, not a demonstrated erroneous LP011 argmax or LP019 subtraction. The precise alleged LP011/LP019 faulty historical commit:path:line is still unverified. Do not erase the complete R063 evidence, prior Unit157/P022 prior-art correction, or previous native Source checkpoints.

At the beginning of this unit the original request onhour-20261119-2208-x6-own-units162164-native-progress-v1 had been read back SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED at Source aad579fa1ade1a2e45762749cde76573f4065f56. The distinct original Units165–166 request onhour-20261120-0015-x6-own-units165166-native-progress-v1 remained RUNNING/SOURCE_PUBLICATION_CONTENTION when last observed; preserve it and consume original receipt only. Unit167 author proof and Activity183 were already Source-persisted when this work began. No new native mutation, new researcher session, or maintenance identity is asserted by this author evidence.

The parent task stays OPEN: remaining historical 28-LP consumer audit; LP011/LP019 provenance; Units149–152 native association debt; and independent Driver Review/Result handling. Next exact control action: consume the original Unit165–166 PROGRESS outcome and check current own winning claim/run before any new native semantic association. Next science action: continue actual frozen production-consumer traces and avoid treating correct derived code as an erroneous native import.
