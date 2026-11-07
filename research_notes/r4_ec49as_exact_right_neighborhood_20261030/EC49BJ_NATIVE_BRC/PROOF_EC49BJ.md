# EC49BJ — Exact residual needed for native signed-X6 path reversal

2026-10-30. AUTHOR ANALYTIC PROOF / EXECUTED PINNED BRC TEST / PORTABLE DRAFT / UNREVIEWED / NOT_ADMITTED.

## Immutable inputs and scope

GLOBAL_KNOWLEDGE_V1 canonical main: `24e83b5deb3cb7fe6489792f4b6bf309ece8b00f`. Enterprise Math canonical main: `6b370f2eaef54781db2b2b31cbb6d219e594a65f`; original P000 projection metadata agree at Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. Verified native source `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` has Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. The established source defines signed-native X6 path length, shortest multiplicity and positive rational endpoint weight. We do NOT retype EC49BI's auxiliary three-label complex-linear residual R as a native six-dimensional coordinate or BRC port.

Choose a native spatial Cell P and signed X6 displacement d=(d1,...,d6)∈Z^6; Q=P+d, no distinguished ontic origin. A shortest path-formal BRC witness is an ordered word w of n=sum_i |di| primitive signed axis actions, with exactly mi=|di| occurrences of sign(di)Ei when mi>0. All other relative coordinates are explicitly zero when a three-axis example is embedded in X6. Every word realizes native signed-axis adjacency. There are B(d)=n!/product_i mi! ordered shortest words (B(0)=1). This is an exact *static* spatial BRC type; it does not specify heartbeat time or physical reversibility.

The derived path inverse operation T maps (w1,...,wn) to (-wn,...,-w1), an ordered shortest word Q→P with displacement -d. This preserves signed labels, path witnesses and B(-d)=B(d). It is **not** a claim of reversible physical time dynamics. Present aggregate observer O_end(w)=(P,Q,n,B(d)) forgets which particular word was realized. A declared path-formal future readout O'_k reads the first k signed labels of T(w), equivalent to the reversed and sign-inverted original k-suffix, 0≤k≤n. The exact sufficiency question is whether equal O_end necessarily entails equal O'_k∘T.

## Theorem A: exact number of irreducible future observation classes

Define
 C_k(d)=sum_{r_1+...+r_6=k; 0≤r_i≤m_i} k!/product_i r_i!.

Proof: An admissible original ordered k-suffix has some multiplicity vector r≤m with sum k. There are k!/∏r_i! ways to order that suffix, and every choice extends to a whole shortest path by preceding it with the remaining multiset. Distinct suffixes yield distinct reversed-prefix observations. This is an explicit bijection, proving the expression for every d∈Z^6, not an extrapolation from finite tests.

Within the fixed (P,d) shortest-witness fiber, O'_k∘T factors through O_end **if and only if** C_k(d)=1, equivalently k=0 or support(d)≤1. If support≥2 and k≥1, choose witnesses with different final axis labels; O_end agrees while the future reversed-first label differs. The least possible number of exact deterministic extra states making this readout sufficient is C_k(d), and the least worst-case fixed-length binary storage is ceil(log2 C_k(d)) bits. It can be realized by any injective encoding of the ordered terminal k-suffix. This is a discrete cardinality statement, not a complex-linear or physical bit-cost claim.

## Theorem B: sharp full-path reconstruction threshold

If support(d)≥2, the last n−1 original labels together with d reconstruct the remaining first label by subtracting their counts from m; therefore C_(n−1)(d)=C_n(d)=B(d). No smaller k suffices uniformly: for any k≤n−2 choose different available labels a,b and any ordering v of the remaining multiset; the distinct paths abv and bav have identical k-suffix but differ as full paths. If support≤1, B(d)=1 and endpoint data already determine the unique word. The empty path d=0 is covered separately.

## Theorem C: exact N-BRC / positive rational weighted fiber masses

For any admissible ordered terminal k-suffix s with counts r_i, its full path fiber cardinality is
 F_d(s)=(n−k)!/product_i (m_i−r_i)!.
This is the count of permutations of the remaining prefix multiset; hence sum_s F_d(s)=B(d). Uniform N-BRC path probability of that suffix equals F_d(s)/B(d)=∏_i (mi)_(ri)/(n)_k, with falling factorials for k>0 (1 for k=0).

For the established native positive rational Weighted-BRC source with positive rational signed primitive weights u_i^+ and u_i^-, every shortest word of displacement d has exactly the same product q_d=∏_{i:mi>0} (u_i^{sign(di)})^{mi}, since shortest words cannot insert inverse pairs. Thus native endpoint_weight(n,d,...)=B(d) q_d and the mass of suffix fiber s is F_d(s)q_d. The conditional suffix law remains F_d(s)/B(d). These are positive branch masses, **not** signed or complex amplitudes, and no cancellation/Born-rule claim is made.

## Concrete native counterexample

Take an actual chosen Cell P and full six-component signed displacement d=(2,-1,1,0,0,0). Two shortest words (integer label +Ei=i, -Ei=-i) are
 w=(1,1,-2,3), w'=(3,1,-2,1).
Both end at Q=P+d, with n=4, B(d)=12, identical O_end, yet T(w) begins -3 and T(w') begins -1. Thus the aggregate endpoint/multiplicity observer loses information needed for a legitimate *declared static path-formal* future reversal readout. This refutes **only** the proposed sufficiency scope and does not assert that branch reversal is an actual heartbeat update.

Exact class sequences by k=0,...,n:
- (2,-1,1,0,0,0): (1,3,7,12,12), least fixed bits (0,2,3,4,4).
- (3,4,0,0,0,0): (1,2,4,8,15,25,35,35).
- (1,1,1,1,1,1): (1,6,30,120,360,720,720).

## Executed verification and obligation boundaries

The companion locally **executed** Python `VERIFY_EC49BJ_NATIVE_BRC.py` loaded byte-identical source `signed_brc.py` at blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. It exhaustively checked all 1289 signed six-axis integer displacements with L1 norm ≤4, enumerating 13,849 shortest ordered words and all k-suffix fiber sizes and class counts. Separate exact `Fraction` weighted examples included the three displayed displacements plus zero. The recorded report is `EXACT_REPORT_EC49BJ.json`. A full local executed verifier and evidence are also preserved in the run's evidence package; any separately published compact verifier must be distinguished from the actual run if not executed. Universal validity rests on the explicit bijections above, not on finite test coverage.

Remaining independent questions: the source inverse path involution is a combinatorial operation, not a certified native physical BRC branch/port update; no original three-label auxiliary R→X6 typed map, signed/complex BRC amplitude interface, physical heartbeat trajectory, triadic force dynamic law or native time reversal is shown. P000 and ACTIVE worldview remain unchanged. No native Research-Activity, CLAIM, Result, independent Driver review, Working Truth or Foundation acceptance is asserted.

## Next research unit

EC49BK: classify the minimal sufficient typed observer under composition of *declared native signed-X6 path operations* (concatenation, axis-permutation S6, reversal) for future prefix/endpoint readouts including non-shortest loops. Determine whether a bounded suffix register suffices under arbitrary compositions or prove an exact unbounded-memory lower bound. Preserve all path labels, order, multiplicity and source until an operation/observer-specific quotient certificate is proved.