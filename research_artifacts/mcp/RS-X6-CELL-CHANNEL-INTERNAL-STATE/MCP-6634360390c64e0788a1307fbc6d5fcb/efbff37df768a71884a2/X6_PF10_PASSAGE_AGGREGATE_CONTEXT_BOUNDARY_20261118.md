# PF-10 relational passage aggregate: exact observation-dependent trace fibers (2026-11-18)

Task: RS-X6-CELL-CHANNEL-INTERNAL-STATE. This is a **conditional formal trace theorem**, not a native X6 event-admissibility theorem. Researcher EM-X6-C7A253; preserve predecessor EM-EMF6D046-5A2844 and its signed-axis 144-history/73-endpoint lemma.

## Typed domain and assumptions

PF-10 allows *relational* ordered channel labels p=(a,b), where a,b in {0,...,5}, ingress/egress totals I[a], O[b], passage-count matrix M[a,b]. These are **not** the twelve signed spatial X6 directions. Fix a declared finite passage alphabet P. A formal trace w=(p1,...,pN) belongs to P^N, and every permutation of a passage multiset is admitted **only inside this free-order formal model**, not by P000/PF-10's native transition authority. Let M[p] count occurrences of p; I and O are M's row/column sums.

## Exact fiber theorem

For a fixed multiset M, sum_p M[p]=N, the complete-trace fiber over (I,O,M) has exactly

 F(M)=N! / product_p M[p]!.

Proof: orderings of a labelled multiset are N! modulo permutations among its identical labels. Consequently an auxiliary binary register that, given M, reconstructs the entire chronological trace requires and is sufficient with ceil(log2 F(M)) bits (encode the lexicographically ordered fiber index). If a full final relational passage pN=p with M[p]>=1 is separately observed, the remaining fiber is

 F(M,p)=(N-1)!/((M[p]-1)! product_(r != p) M[r]!) = M[p]*F(M)/N.

The corresponding exact register bound is ceil(log2 F(M,p)). There is no uniform bounded memory for reconstructing an unbounded trace under the formal free-order hypothesis if |P|>=2.

## Contextual quotient theorem

For an explicitly given family C of **legal** future contexts and their answers A(w,c), define w~v iff A(w,c)=A(v,c) for all c in C. An encoder supporting every such query must refine this equivalence, and the equivalence-class label is a minimal sufficient state. This is elementary but crucial: future closure depends on which native operations/queries are legal, not merely on the aggregate's information loss.

If every legal query factors through M, the aggregate alone suffices. If an admissible query reads the last passage while M does not retain it, a two-symbol trace (p,q) and (q,p), p!=q, are observationally distinguished despite equal M. If the last passage is supplied as observation, the two-symbol fiber has zero auxiliary-bit reconstruction cost. Full chronological queries require the entire fiber index.

## Exact formal six-channel test

Take all 36 ordered relational pair types P={0,...,5}^2 as a **formal alphabet** (no claim that all pairs are physically legal). At N=2 there are 36^2=1296 words and C(37,2)=666 aggregate matrices. Fibers: 36 of size 1; 630 of size 2. Worst trace reconstruction memory given M: 1 bit; if final pN is provided: 0 bits.

At N=3 there are 36^3=46656 words and C(38,3)=8436 aggregates. Fibers: 36 of size 1; 1260 of size 3; 7140 of size 6. Worst memory given M: 3 bits. After disclosure of final pN, worst remaining fiber is 2 (1 bit). All exact enumerations passed.

## Native unfinished question

Specify actual PF-10 pair admissibility and Cell/Port/triadic transition and observation laws, including signed phase, positive branch mass and BRC provenance, then apply context equivalence. P000's six spatial axes, native triadic force closure and PF-10 relational six-channel structure remain separate types. A universal numeric native Cell hidden-state lower bound remains undetermined until these maps are known.

Inputs: PACKET_PATH_FOUNDATION.md#PF-10, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md, at frozen Source a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor Source: 676737967878b598252b3ccce0ac740bfe1cc55e, _checkpoint.json, X6_CELL_TWO_STEP_ENDPOINT_LAST_PORT_CORRECTION_20261117.md.
