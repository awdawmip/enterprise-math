# R708 — Feasibility, exact-source recurrence and BRC sampler for Cell-attached X6 triads

Date 2026-11-11 (Asia/Shanghai). Parent `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, previously observed publication `TP2-8B7E13C5904A2D6F1142`. Frozen science `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct successor to R707 (PR #2033). This is author-side candidate-subfamily mathematics.

## Carrier
At one chosen native X6 Cell c and fixed q>0 rational, let n_i distinguishable signed force tokens on each of six axes. Signs, individual source identity and provenance remain attached; candidate triad admissibility here depends on common c,q and **three distinct native axes**. Events add/remove full triples simultaneously, preserving the primitive three-force arity. This does not equate force balance with a three-step spatial return. The native V29/V39 dynamic interface and full rotations remain a further research obligation.

## Theorem A — Exact covering feasibility
For nonnegative n=(n_0,...,n_5), with sum n_i=3m, m a nonnegative integer, all tokens can be partitioned into m unordered candidate triads of three distinct axes **iff** max_i n_i <=m.

Necessity: each of m triples has at most one token on any particular axis. Sufficiency: for m>0 choose the three currently highest positive counts, pair one labeled token from each as a whole triad, and subtract one from these three coordinates. Three positive axes exist since otherwise sum <=2m<3m. At most three coordinates equal m, since four would exceed 3m; therefore all coordinates at maximum m were selected. The new nonnegative vector has total 3(m-1) and maximum <=m-1. Induction gives a full labeled witness, with empty partition as the m=0 base. QED.

The same argument works for rank-r uniform hyperedges across d>=r distinct axes. Polyhedral context: integer decomposition of matroid base polytopes; for example D. Gijswijt and G. Regts, *Polyhedra with the Integer Carathéodory Property*, 2010, arXiv:1004.4552. The proof here is an explicit specialization and constructive algorithm, not a priority claim about the general property.

## Theorem B — Exact labeled-source recurrence
Let D(n) be the number of unordered partitions of all uniquely labeled tokens, with D(0)=1 and D(n)=0 when the state is unfillable. Fix a distinguished labeled token whose axis is a with n_a>0. Then

D(n)=sum_{b<c, b,c!=a} n_b n_c D(n-e_a-e_b-e_c).

Each partition has a unique triple containing the distinguished token; select its other two distinct axes and one labeled token from each (n_b n_c choices), then partition the residual labels. Different choices are disjoint and exhaustive. QED.

Define a positive rational BRC sampler: choose axis pair (b,c) with mass n_b*n_c*D(n-e_a-e_b-e_c)/D(n); conditionally choose the individual labeled partners with probability 1/(n_b*n_c), and recurse. The recurrence normalizes the masses. For every particular labeled partition, the product of branch masses telescopes to exactly **1/D(n)**. Thus this is an exactly uniform labeled-source sampler, and it retains the complete branch identities rather than projecting to the six counts. Memoized D computes at most product_i(n_i+1) states, with at most C(5,2)=10 big-integer terms per state, plus integer-bit costs; input counts are numeric, and the bound is not claimed polynomial in their binary encoding.

## Theorem C — Number of feasible count profiles
F_6(m)=[x^(3m)](1+x+...+x^m)^6
= C(3m+5,5)-6*C(2m+4,5)+15*C(m+3,5)
= (m+1)(11m^4+44m^3+71m^2+54m+20)/20.

Here C(t,5)=0 for t<5, including m=0. Proof: unrestricted stars-and-bars profiles give C(3m+5,5). For each chosen coordinate >=m+1 shift by m+1 and subtract 6*C(2m+4,5); restore 15 pairwise intersections C(m+3,5). Three-fold intersections are impossible because 3(m+1)>3m. Expand. QED. Values m=0..4: 1,20,141,580,1751. This counts degree *vectors*, not labeled decompositions.

## Theorem D — New infinite BRC source family
For m>=1, D(m,m-1,m-1,1,1,0)=m!(m-1)!(2m-1).

Proof: all m triples contain one of the m axis-0 tokens; use their labels as slots. If the two rare (axes 3 and 4) tokens share one slot, choose it in m ways and permute the two groups of m-1 labels in ((m-1)!)² ways, giving m((m-1)!)². Otherwise the rare tokens occupy distinct slots and pair with the two large groups in either order. Choose those slots in m(m-1) ways, choose the pairing orientation in 2 ways and assign each large labeled group among its m-1 available slots, giving 2m(m-1)((m-1)!)². Total m(2m-1)((m-1)!)²=m!(m-1)!(2m-1). QED.

## Native restriction discriminant
Theorem A assumes all 20 unordered three-axis types are available at the Cell. Let A(c,state) be the *actual* allowed typed triples after checking native ports, conservation and loop flow. Coverings now satisfy n=sum_{T in A} k_T 1_T with k_T nonnegative integers. A necessary condition remains max n_i<=m; sufficiency can fail. Example: n=(m,m,m,0,0,0) requires {0,1,2}; excluding that triple forces D_A=0 for every m>0. This gives a concrete discriminating question for the frozen V29/V39 event model.

## Evidence, limits and next action
Executed standard-library Python exact integers and fractions. Full test program and JSON evidence are in experiments/R708*. Tested every n in {0,1,2,3}^6 with sum divisible by 3 and sum<=12: 1,309 profiles, of which 1,077 are feasible and 232 infeasible, using independent H^m coefficients, first-token count recurrence and greedy witness. Four six-token examples have exact uniform labeled partition probability 1/D, with D=4,10,6,4. Also checked the profile polynomial for m=0..10, and Theorem D for m=1..8. Marker R708_TRIADIC_FEASIBILITY_UNIFORM_BRC_EXACT_PASS. Proofs above apply for all indicated m; finite checks validate the implementation on the stated domain.

Next: inspect the *frozen* native X6 Cell/Link/Port, V29 PASS/TRANSFER and V39 j-flow input bytes; determine one typed A(c,state), enumerate or prove its integer semigroup cover feasibility, and execute a single admissible atomic three-token event with source identity, conservation and native rotation transformation. This candidate study does not claim a native authenticated task Result or independent Driver review.

## Theorem E — Rotation-equivariant, order-free BRC source law

In the same complete-permissive candidate model, for m>=1 and D(n)>0, choose the **next unordered labeled triad** S={u,v,w} of three distinct axes with probability

P(S|n)=D(n-1_{axes(S)})/(m D(n)).

The total mass is exactly 1: count ordered pairs (P,S), with P a full labeled partition and S one of its m constituent triads. There are m D(n) such pairs, while a particular labeled triad S occurs in exactly D(n-1_S) full partitions. The equal-positive-rational weighting is therefore normalized. After choosing S remove its three labeled tokens and recurse. For a fixed full unordered partition P, each ordering of its m distinct triples has probability

prod_{r=m,...,1} D(n_{r-1})/(r D(n_r))=1/(m! D(n)),

and the m! possible orders give the exact final probability 1/D(n). QED.

At the coarse *axis-type* BRC observer the next triple T={i,j,k} has probability

P(T|n)=n_i n_j n_k D(n-e_i-e_j-e_k)/(m D(n)),

where a missing axis makes the term zero. This records how positive mass is partitioned among the 20 types while preserving full token-level provenance upstream.

Let π∈S6 act on native axis indices and simultaneously transport every labeled token and its signed/source metadata; the corresponding count tuple is πn. The axis-type kernel and the labeled-triple kernel satisfy P(πT|πn)=P(T|n), respectively P(πS|πn)=P(S|n), because D(πn)=D(n). The complete labeled partition measure is consequently **exactly S6-equivariant**. This explicitly removes the arbitrary 'first nonzero axis' choice from the operational sampler. It verifies covariance under the known finite axis-permutation skeleton, not the currently open full native rotation generators.

Exact verification: a six-token sample n=(2,2,1,1,0,0) yields type probabilities 1/2 for {0,1,2} and {0,1,3} and zero for the other two possible triple types; all 720 S6 axis permutations preserve these positive-rational masses and their transformed type keys. This finite check illustrates the general proof.
