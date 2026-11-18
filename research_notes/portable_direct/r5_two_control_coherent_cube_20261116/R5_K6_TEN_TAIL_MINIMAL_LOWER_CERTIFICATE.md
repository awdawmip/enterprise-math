# R5 k=6 — Inclusion-minimal ten-tail exact lower certificate

Frozen science pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Complements R5_TWO_CONTROL_CUBE_COVER_THEOREM.md, retaining its exact assumptions: two controlled nodes J={0,1}, additive source-library slack s=2, and internally coherent Set transition algebra. Author-side exact finite evidence, independent review NOT_REVIEWED.

The original exhaustive enumeration produces 41 distinct nonempty eligible tail bitsets on all sixteen fixed tails. For the lower bound 11, only these ten tails are needed:

T* = {3,5,6,9,10,11,12,13,14,15}.

Restrict every eligible component cover to T*, remapping the listed tails to positions 0..9 in ascending order. For each restricted nonempty bitmask, retain the cheapest canonical projection-table component. Exactly 21 weighted masks result, expressed below as (decimal cover bitmask, controller state cost):

(1,1), (2,1), (4,1), (5,4), (7,4), (8,2), (16,1), (32,2), (33,2), (57,4), (64,1), (128,2), (192,2), (202,4), (256,1), (320,2), (324,4), (340,4), (512,2), (768,4), (928,4).

**Finite exact certificate.** Let D[m] be the minimum total state cost of a family of these candidates whose union is exactly bitmask m, with 0<=m<1024. Set D[0]=0 and other entries to infinity; for m in increasing numeric order, relax D[m OR c] with D[m]+w for each of the 21 (c,w). Since m OR c >= m, this is a complete acyclic exact-integer dynamic program over 1024 states; an optimal cover can always omit repeated/unhelpful selections, so the final value D[1023] equals the minimum covering cost. The standard-library implementation returns D[1023]=11.

Removing any one tail from T* drops the restricted optimum below 11; individual drop-one values are recorded by the checker. Thus T* is an inclusion-minimal eleven-state obstruction among tail-subsets, rather than merely one large unstructured test. The verified eleven-state concrete controller from the main theorem covers all original sixteen tails and provides the matching upper bound.

Reproduce by running VERIFY_R5_K6_TEN_TAIL_CORE.py. It rebuilds all centre-based projection-table candidates directly from cyclic q_k and the labelled-library feasibility predicate, verifies that there are 41 full-tail and exactly the listed 21 restricted candidates, runs exact 1024-state DP, and recomputes ten leave-one-out optima. It uses Python standard library only. This mathematical certificate applies to internally coherent controllers. The unrestricted two-control k=6 minimum remains in {10,11}, with the source-labelled noncoherent ten-state feasibility question unresolved.

