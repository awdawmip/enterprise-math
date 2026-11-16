# R214 — Green-J congruence, optimal bilateral ideal-query quotient, and class-contiguous action code

Date: 2026-11-16 (Asia/Shanghai)
Evidence status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED

## Provenance and precise scope

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Antecedents: R200, R209–R213; specifically R213_FULL_MONOID_GREEN_IDEALS_20261116.md from immutable commit 26bccd30c4afb00bf143acd7627eff9cdf954693.

This is the finite paired-event observer quotient, *not* a quotient of complete Heartbeat World state. X6 has six spatial axes, twelve signed native directions and a separate time dimension. No native BRC physical propagation, signed amplitude/phase cancellation, or empirical residual attribution is claimed. The only permitted compressed observations are the principal right- and two-sided-ideal predicates and their composition closure explicitly proved below. Other observations require retaining the richer carrier.

Let m≥1 directions, k≥0 selected provenance tags plus neutral tag 0, and L≥1 paired-event tail depth. The alphabet is A=[m]×({0}∪[k]), with a=m(k+1). For a word w, let s(w) be its partial permutation of nonneutral tags ordered by final appearance (oldest to newest), and t_L(w) its final min(L,|w|) complete direction/tag pairs. J={F(w)=(s(w),t_L(w)):w∈A*} is the chronological observer monoid. S(x) denotes the set of nonneutral tags in the source order. If tail length is shorter than L, x is uniquely represented by the literal short word u. The full-tail sector E is the idempotent ideal from R211–R212.

## Theorem A: Green-J equivalence is a two-sided congruence here

Define the typed disjoint union

Q = A^{<L} ⊔ P([k]).

Elements of the second summand are marked FULL; in particular, the empty full subset is different from the empty short word. For a short word u, let σ(u) be its nonneutral source support. Define multiplication as follows:

1. Two short words u,v multiply to their literal concatenation uv when |uv|<L.
2. Two short words multiply to the FULL set σ(u)∪σ(v) when |uv|≥L.
3. Whenever at least one factor is FULL, replace each short factor u by σ(u) and multiply the resulting subsets by union.

Then q:J→Q, given by q(x)=t_L(x) for a short state and q(x)=S(x) in the FULL sector, is a *surjective monoid homomorphism*, with

ker(q) = Green-R = Green-J

as equivalence relations on J. Consequently Green-J is a congruence for this particular J, and Q is J-trivial. Its FULL part is the union semilattice P([k]).

**Proof.** The source support of a chronological product is the union of the source supports of its factors. When both factors have tails shorter than L and the concatenated length stays shorter than L, the product state is their literal word. In every other case the product tail is full; its q-image is the union support. Thus q preserves the product in all cases. Associativity of the displayed multiplication follows by homomorphic image from J. Every short word is realized by itself; a FULL subset U is realized by emitting each tag of U at least once, followed by L neutral events. So q is onto. R213 establishes that every short state is its own Green-R/J class and that two full states are Green-R/J equivalent exactly when their support sets coincide. This exactly identifies ker(q). In Q, distinct short words have distinct shortest short factors in their principal two-sided ideals, full sets have distinct union-upward ideals, and no full and short elements share one. Therefore Q is J-trivial. QED.

## Theorem B: minimal exact state for right/two-sided ideal predicates

For x,z∈J consider predicates R(x,z)=[z∈xJ], I(x,z)=[z∈JxJ]. Both descend exactly through q:

- FULL x with support U: both are true iff z is FULL with support V⊇U.
- Short x=u and FULL z with support V: both are true iff V⊇σ(u).
- Short x=u and short z=v: R(x,z) iff u is a literal prefix of v; I(x,z) iff u is a contiguous factor of v.

These are R213's exact principal ideal formulas. Since q is a homomorphism, these predicates remain decidable after arbitrary future left/right monoid multiplications of either argument; this is an *unbounded-composition certificate for this declared query language*, not for arbitrary physical observers.

Any deterministic code from which I(x,z) is decidable for every ordered pair of original states must assign distinct codewords to distinct Green-J classes. Indeed, if x and y share a code, every I(x,z) and I(y,z) must agree for each z, giving JxJ=JyJ and x Green-J y. Q attains this minimum. Therefore

|Q| = Σ_{h=0}^{L−1} [m(k+1)]^h + 2^k,

and the optimal fixed-width code for this exact query language has ceil(log₂|Q|) bits.

**Strict limitation / exact counterexample.** With m=2,k=1,L=1, the two full one-event histories ((0,1)) and ((1,1)) both map to the FULL support {1}, but have different paired-event tails and are distinguishable by the exact tail/direction readout (and distinct Green-L classes). Hence the ideal quotient is NOT a replacement for R209/R210's full-action code, physical BRC Affine effects, port/signed-phase information, multiplicities, joint associations or complete time histories. The project residual-fidelity contract permits this compression only for the proved predicate family.

## Theorem C: minimal full-action code reordered into contiguous Green classes

R209 ranks all original J states in a minimum-width interval, but groups the full states by source permutation before tail. A different bijection groups by *source support* first. Let

B=Σ_{h=0}^{L−1} a^h, C(r,L)=Σ_{j=0}^{min(r,L)} Stirling₂(L+1,j+1),
V_r=m^L C(r,L), W_r=r! V_r.

For a source set U={u₁<...<u_r}, define its colex rank c(U)=Σ_{i=1}^r binom(u_i−1,i), which ranges from 0 to binom(k,r)−1. Let p_U(s) be the lexicographic rank of a permutation s of U and let τ(s,t) in [0,V_r) be the paired-tail rank calculated by R209's backwards Stirling completion DP. Define for a full state with S(s)=U and |U|=r:

R_grouped(s,t)
= B + Σ_{i<r} binom(k,i)i!V_i + c(U)W_r + p_U(s)V_r + τ(s,t).

For short states use the ordinary length-block, base-a word rank from R209.

For each chosen U, there are r! possible final-source orders and exactly V_r compatible full paired tails for each order (by R209's Stirling fibre theorem). Colex subsets, source permutations and compatible tails are each exhaustively and injectively indexed by the indicated blocks. The displayed ranking is consequently a bijection J→[0,|J|). Every Green-J class of full states occupies one contiguous interval of length W_r. This reordering preserves R209's optimal full-state width.

A grouped full rank can be reduced to the optimal ideal-query code without reconstructing the source permutation or paired tail: locate its r block, divide the within-r offset by W_r, colex-unrank U, then return B+mask(U). A short rank maps to itself. The compressed Q-code is precisely [0,B+2^k). Ranks can also be fully decoded and re-encoded by the inverse block operations, so original full-action information is not destroyed by the grouped ranking itself.

**Complexity boundary.** Class extraction requires block subtraction, integer division and colex subset unranking; it does not require reconstructing an L-event tail or running the provenance DP for a code already in grouped form. Big-integer bit costs, code conversion from the original R209 ordering, preprocessing, full-effect construction and native BRC adapter cost must be charged before any end-to-end speed advantage is claimed. No performance benchmark was executed here.

## X6 instance

For m=12 signed native X6 directions, k=6 independent selected tags and L=2, a=84 and B=85. Earlier exact cardinality is |J|=1,407,685, so the full reachable-action code needs 21 bits. The new query-specific quotient has |Q|=85+64=149 classes and a proven-optimal **8-bit fixed-width code**. The 64 full support classes have sizes W_r=144, 576, 1,440, 4,320, 17,280, 86,400 and 518,400 for r=0..6 respectively, each repeated binom(6,r) times; they sum to 1,407,600 full states. These figures are exact observer algebra, not native physical data compression.

## Exact verification and continuation

The standard-library Python companion R214_green_quotient_exact_check.py independently constructs 11 finite parameter models by generator closure. It checks all complete grouped-rank round trips, support-code projection, quotient homomorphism, and (for models up to 100 states) exhaustive principal right/two-sided ideals by explicit original-J multiplications. One 403-state model has pairwise sampled homomorphism tests; 3,009 deterministic full-rank samples cover the large X6 example. The accompanying JSON gives the exact counters and model boundaries. All computations are exact integers without floats. The general theorem rests on the displayed proofs; finite tests are executable corroboration, not a universal proof. Independent review remains NOT_REVIEWED; native installed EffectHistogram integration is NOT_EXECUTED.

Next: preserve the full R210/BRC typed carrier while using the 8-bit quotient only as an indexed right/J ideal-query readout; benchmark grouped vs original R209 code in an actual BRC adapter; investigate intermediate observation languages retaining exact Green-L / provenance-sensitive queries. No Task CLAIM, formal Result, independent review or Foundation promotion is asserted by this GitHub research publication.
