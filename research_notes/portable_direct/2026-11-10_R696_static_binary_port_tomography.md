# R696 — Exact binary-static-port BRC tomography and finite three-probe lower bound

2026-11-10 · Author-side exact theorem and finite certificate · UNREVIEWED / NOT ADMITTED
Researcher-ID: EM-X6-ED0814 · Research-Activity-ID: RA-B4B8B98ACA15A669CF5D0795 · Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS (no CLAIM).

## Source model and exact scope

Reuse immutable R692C E* X6 returning-square counts from commit 3dacca5010104893d96301af4d61608d5a5a0879, file research_notes/portable_direct/R692C_ESTAR_MASK_RETURN_EXACT.js, blob 0c6d51f99eac5903a30770c8c393c972a68d93ad. The four directional positive labelled 15-path BRC group kernels in bins (e,t,c,c²) are K0=(6,9,0,0), K1=(6,6,3,0), K2=(6,3,0,6), K3=(6,0,3,6). Total 60 labelled paths with group histogram N=(24,18,6,12).

R695b immutable commit c7f1f35e69dc4c7525ccedd33cf52a9534ecb1a8 constructs a candidate binary static Cell port field in which each labelled returning square has its own third-step directed port. Each gate can independently be on/off. After selecting nonempty paths, v=(v_e,v_t,v_c,v_c²) with 0≤v≤N and |v|>0, and the declared coarse group observer is μ_v=v/|v|. Full labelled-source and port records are retained upstream of this group quotient.

Future test 0 observes one-macro return T0=μ_v(e). For each mask m=1..15, select externally a fixed independent R692C directional continuation ν_m=(sum K_j for bits j in m)/15*popcount(m); test Tm=(μ_v*ν_m)(e). Since inverse swaps c and c² but fixes e and t, each Tm is a rational linear functional of μ. These external mask choices and independent static gates remain an E* candidate observer, not a native V29/V39 event-law permission.

## Theorem A: exact number of fields, histograms and normalized group laws

There are 2^60−1 nonempty binary port fields. Every integer histogram v with 0≤v≤(24,18,6,12), v≠0, is attained, hence exactly (25·19·7·13)−1=43,224 different count histograms. Two nonzero v,w have identical normalized group law iff they lie on the same positive rational ray. Each ray has a unique attainable primitive vector u=v/gcd(v_e,v_t,v_c,v_c²). Möbius inversion counts these primitive rays:

    R = Σ_{d=1}^{24} μ_arith(d) ( ∏_{n∈{24,18,6,12}} (⌊n/d⌋+1) − 1 ) = 38,618.

The −1 removes the zero vector. The complete integer primitive-ray enumeration independently agrees with the Möbius value. Therefore the exact number of distinguishable normalized group kernels is 38,618.

## Theorem B: one suffix distinguishes the four single-deletion holonomy bins

Deleting exactly one group-g path produces μ_g=(N−δ_g)/59. Suffix mask m=3 has inverse-ordered count row (12,15,0,3)/30. In deletion bin order (e,t,c,c²), the four return values are exactly (97/295,193/590,99/295,197/590). They are distinct, with minimum separation 1/590. All 15 suffix masks were exhaustively compared: the maximum achievable minimum separation in this menu is 1/590, attained at masks 3,6,9,15. This identifies the deleted *group holonomy bin*, not the original port ID: the bins have 24,18,6,12 different labelled sources, respectively.

## Theorem C: exactly three scalar tests required for all deterministic binary static fields

Consider the 16 nonadaptive scalar tests T0,...,T15 just declared. Three tests T0,T1,T4 are sufficient: with (r,x,y,z)=(μ_e,μ_t,μ_c,μ_c²), set r=T0, A=T1=(2r+3x)/5, B=T4=(2r+x+2y)/5, then reconstruct x=(5A−2r)/3, y=(5B−2r−x)/2, z=1−r−x−y. These identities hold for any group law on these four bins, hence all 38,618 binary-field kernels.

Three are also **necessary for this finite deterministic family**: there are C(16,2)=120 possible unordered two-test designs. For each pair, the attached exact raw JSON gives two distinct realizable primitive histograms with ≤8 surviving paths each and identical rational readings of that pair. The executable verifier constructs and checks all 120 collisions using exact integer/rational signatures. Any single test cannot be more injective than a two-test extension. Among the 120 pairs, the best pair (3,14) distinguishes 38,159 of 38,618 kernels, a deficit of 459, while (1,4) distinguishes 16,924. This finite lower bound strengthens R695b's dimension-only lower bound on continuous *mixtures*.

Explicit deterministic witness: v=(0,2,2,0), w=(3,0,0,1), each with exactly four retained labelled paths. Both yield T1=T4=3/10, but T0(v)=0 and T0(w)=3/4. These are pure binary gate configurations, not randomized mixtures.

## Execution and research meaning

Independent exact Python stdlib/Fraction verifier was executed with result R696_ALL_EXACT_ASSERTIONS_PASS 43224 38618 120 1/590 (38159, [(3,14)]). The source-attached executable JS reproduces the exact primitive-ray count, Möbius count, full 120 two-test witness set and maximal two-test gap; only the finite ranking of singleton suffix separations uses JS Number, and this ranking was independently replayed in Python with Fraction. All group-count and collision identities use exact integers and reduced rational strings.

Reuse: REUSE_APPLIED exact R692C labelled group-count kernels; COMPOSE_APPLIED R695/R695b contextual return functional and static unique-port candidate. The original task science locator a72226e2430ffa4786321ac86e7f0c599d5f0389 was reported DRAFT_OR_UNVERIFIED in native immutable manifest read; no scientific pin was rebased, and this calculation explicitly uses the verified historical R692C and R695b blobs.

## Next discriminating question

Retrieve the native X6 Link/Port, V29 PASS/TRANSFER ledger and V39 time-event transition semantics. On a bounded exact event-state set, enumerate *legally reachable* suffix-event readout rows, preserving full 60-path identity, port state and ledger history. Compute their rational row rank and possible source-specific fibers; determine whether T0,T1,T4 can actually be implemented, and if not construct exact minimal observable memory repair. Mother task triadic closure law, native rotation covariance and true Cell/path update remain open. No formal CLAIM, Result, independent review or Foundation admission is asserted.
