# PREFIX-930 — Zero-origin two-flip certificates, exact 19-bit union beyond PREFIX-929

Date: 2026-11-19. Lane: 进取数论研究6. Scientific status: AUTHOR_PROVED / TWO_INDEPENDENT_EXACT_IMPLEMENTATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Direct mathematical dependency: PREFIX-929 fullrow/highband disjoint union, with the PREFIX-928 sorted U source set. Scope: auxiliary provenance-aware named XOR two-port observer, not native X6 evolution or a change to P000.

## Theorem — an explicit two-flip collision family

Let N=2^32 and Q={262145,262147,...,524287}, |Q|=131072. Named traces are Z_x=(x,x) and F_x^i=(x,x XOR 2^i), where 0<=x<N, 0<=i<32. Observation Phi_(a,b)(x,y)=(x mod a,y mod b) retains the underlying source label separately.

Define the finite oriented-pair certificate family

W={(a,b) in Q^2 : there exist 0<=i,j<=18 such that b=abs((a XOR 2^j)-2^i)}.

For EVERY (a,b) in W, Phi_(a,b) is noninjective, with two explicitly distinct, source-labeled witnesses

F_0^i=(0,2^i),  F_a^j=(a,a XOR 2^j).

Proof. Since a in Q, 0<a<2^19 and 0<=i,j<=18, all four endpoints belong to [0,2^32). The starts 0 and a are distinct but congruent modulo a. By W's condition the two endpoints differ by either b or -b and so are congruent modulo b. The named traces have distinct starts and hence are distinct regardless of their flip labels. This gives a genuine collision. Completeness is claimed only for the explicitly defined W family: enumerating every a in Q and all 19^2 choices of (i,j), then retaining precisely the b in Q and deduplicating ordered IDs, exhausts W. The construction uses no approximation and does not infer native X6 dynamics from the auxiliary observer.

As a concrete witness outside the PREFIX-929 certified union, take
a=316609, b=447679, i=1, j=17.
F_0^1=(0,2), F_316609^17=(316609,447681).
Both have port-1 residue 0 and port-2 residue 2; 447681-2=447679=b.

## Exact intersection with the existing prefix-929 certificate union

Reuse, with actual definitions and source pins, the earlier sets K = B union Z union S union U, and V = C union H union H^op, where:
- B: b < 33 ceil(2^32/a) or a < 33 ceil(2^32/b);
- Z: lcm(a,b)<2^32;
- S: second-port signed-power same-start alias moduli, exactly 24 b in Q;
- U: PREFIX-928 exact 5,295,478 ordered-ID set with sorted little-endian uint64 SHA-256 15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad; proven disjoint from B/Z/S;
- C: 104 complete second-port rows and their first-port transposes, L=D union E union {440665,524287};
- H: 1024-seed PREFIX-923 highband a in {500001,500003,...,524287}, seeds b=262145+2*((77081*t+12345) mod 131072) for 0<=t<1024;
- H^op: time reversal of H.
Thus the frozen previous union has cardinality |K union V|=7,505,960,064 (PREFIX-929). These are certified collision subsets, not an exhaustive classification of all noninjective observers.

The following disjoint classification of W is exact, in priority order:

| Category | Exact ordered-pair count |
|---|---:|
| Raw valid (a,i,j) parameter witnesses before pair deduplication | 35,782,672 |
| Distinct oriented pairs W | 29,360,142 |
| W intersect (B union Z union S) | 13,072,459 |
| W intersect U outside (B union Z union S) | 8,689 |
| W intersect V outside (B union Z union S union U) | 61,146 |
| W outside (K union V), genuinely new certificate pairs | **16,217,848** |

Consequently, in the strict 19-bit odd oriented-pair universe Q^2 of size 17,179,869,184,

|K union V union W| = 7,522,177,912,
|Q^2 \ (K union V union W)| = 9,657,691,272.

The final complement is a *certificate complement*, not a set of proved injective observers. Other generic two-flip and mixed-collision families are not yet globally intersected.

## Verification and reproducibility

Two independent actual runs agree exactly:
1. C++17 uses integer loops over a,j,i, direct XOR and residue checks, sorted unique uint64 pair IDs, and a monotone merge against the frozen PREFIX-928 U binary. It recomputes B/Z/S, the 91+13=104 complete row set L, and the 1024 highband seeds to classify each new candidate.
2. NumPy uses vectorized per-(i,j) generation, independently validates both port remainders, sorts and deduplicates all pair IDs, recomputes B/Z/S/V in vectorized chunks, and computes U intersection by searchsorted. Its arithmetic is entirely integral.

The complete sorted W binary from each implementation consists of 29,360,142 distinct ordered uint64 little-endian IDs (234,881,136 bytes), ID=((a-262145)/2)*131072+((b-262145)/2). Both byte streams were compared with cmp and have identical SHA-256:
b7d00da2269ac6d56ca1c612e9526a81a11aa8f47840db74780523a4e90ffba6.

Published exact source files:
- research_notes/portable_direct/PREFIX930_R6_ZERO_ORIGIN_TWO_FLIP_CPP.cpp
- research_notes/portable_direct/PREFIX930_R6_ZERO_ORIGIN_TWO_FLIP_NUMPY.py
- research_notes/portable_direct/PREFIX930_R6_ZERO_ORIGIN_TWO_FLIP_RESULTS.json

Build C++: g++ -O3 -std=c++17 PREFIX930_R6_ZERO_ORIGIN_TWO_FLIP_CPP.cpp -o prefix930
Run: ./prefix930 PREFIX928_R6_SORTED_PAIR_IDS.bin [optional_sorted_W.bin]
Python: python PREFIX930_R6_ZERO_ORIGIN_TWO_FLIP_NUMPY.py PREFIX928_R6_SORTED_PAIR_IDS.bin [optional_sorted_W.bin].
The archived original U input is a frozen, verified PREFIX-928 output; it is not silently regenerated or replaced.

## Evidence and scope

Exact source-trace collision theorem: proved by explicit construction and direct modular equalities.
Complete W enumeration and its intersection with the specified prior subsets: independently computed with matching sorted sets and matching counts.
Formal Result, independent mathematical review, shared X6 CLAIM, any native typed X6 equivalence or a lower bound on the mother problem B_fix,odd(32): not asserted.

Author provenance: original same-lane SID MCP-31edc522830749ad8775ca012e02ef30, Researcher EM-DIRECT-58C410, Activity RA-25432C4AAE9BF66A907F5115. Native session_start original request r6-20261119-prefix928-own-session-start-01 succeeded; the session registration is not a shared task CLAIM.

Next useful unit: extend F_0^i versus F_(k*a)^j to k>1, and/or source bits j>=19, retaining direct source names and comparing only the genuinely new ordered pair IDs with the exact K union V union W certificate. In particular avoid recounting any of the current 16,217,848 newly classified pairs.
