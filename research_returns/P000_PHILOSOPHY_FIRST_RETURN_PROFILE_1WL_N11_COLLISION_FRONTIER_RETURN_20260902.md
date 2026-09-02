# P000 Philosophy-First Q27 — frozen Return-Profile 1-WL n=11 collision frontier

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER`  
Publication: `TP2-875D6C62E617BCC7CE63`  
Researcher: `EM-PQ27-6F3A9C`  
Claim: `chatgpt-pq27-20260902-0923-6f3a9c`  
Execution branch: `research/p000-phil-q27-return-profile-1wl-n11-collision-em-pq27-6f3a9c`  
Hard target: `P000_RETURN_PROFILE_1WL_N11_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

## Terminal verdict

`SUCCESS / RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11`

Q27 keeps the accepted Q22/Q25 observable bit-for-bit unchanged:

\[
c_0(x)=m_X(x),\qquad
c_{t+1}(x)=\Bigl(c_t(x),\operatorname{multiset}_{y\sim x} c_t(y)\Bigr),
\]

where `m_X(x)` is the primitive simple-cycle multiplicity profile through root `x`, and the graph-level output is the anonymous complete stabilized packet `R_inf(X)`.

Q25 had already proved exact injectivity on `U_BR(n)` for `4<=n<=10`. Q27 now proves exact injectivity also on `U_BR(11)`. Therefore the rigorous collision-free frontier of this **unchanged** low-information observable is

\[
\boxed{4\le n\le 11}.
\]

No claim is made for `n>=12`, and this task stops at `n=11` as required by its kill condition.

## 1. Exact n=11 classification

Let `r` be the number of degree-3 Cells. Under the frozen `U_BR(11)` normalization inherited from Q22/Q25, the admissible sectors are `r in {2,4,6,8,10}` and the degree-3 labels are normalized to the first `r` labels.

The deterministic checker closes all five sectors exactly:

| degree-3 count `r` | exact normalized connected realizations | graph-isomorphism classes | distinct stable packets | collision? |
|---:|---:|---:|---:|:---|
| 2 | 5,050,080 | 23 | 23 | no |
| 4 | 11,476,080 | 197 | 197 | no |
| 6 | 27,213,300 | 536 | 536 | no |
| 8 | 69,824,160 | 482 | 482 | no |
| 10 | 194,934,600 | 114 | 114 | no |
| **total** | **308,498,220** | **1,352** | **1,352** | **no** |

Together with the accepted Q22/Q25 prefix through `n=10`, the exact checked prefix through eleven Cells therefore contains `327,707,557` normalized connected realizations and `2,050` graph-isomorphism classes / stable packets.

## 2. Why this is a complete proof rather than a search statistic

Representative discovery is intentionally separated from completeness authority.

### 2.1 Exact universe count

The checker reuses the Q25 exact degree-sequence recurrence. A distinguished maximum-degree label is connected to subsets of the remaining degree classes; binomial multiplicities retain labeled choices while sorted residual degree states only memoize permutation-equivalent recursion states. Connected counts are then obtained by subtracting all realizations in which the connected component of a distinguished label is proper.

Before accepting the new `n=11` totals, the same recurrence reproduces every frozen Q22 connected sector count for `4<=n<=9` and every accepted Q25 `n=10` sector count exactly. It then independently obtains the five `n=11` totals in the table above.

### 2.2 Discovery is deterministic but nonauthoritative

To avoid importing a graph-classification package, the checker uses a self-contained `SplitMix64` stream plus configuration-model pairing only to **discover** candidate representatives. The fixed stream closes the five sectors after respectively `179`, `1852`, `13207`, `10701`, and `1707` sampled connected simple realizations.

Those sample numbers carry no probabilistic theorem strength. If the stream had failed to find a rare class, the exact certificate below would simply fail to close.

### 2.3 Exact orbit-stabilizer closure

For every newly observed **complete packet serialization**, the checker retains one graph and recomputes its exact automorphism-group order by adjacency-preserving backtracking. Because automorphisms preserve the degree partition, a representative in sector `r` contributes exactly

\[
\frac{r!(11-r)!}{|\operatorname{Aut}(G)|}
\]

normalized labeled realizations.

Crucially, isomorphic graphs necessarily have the same frozen packet. Therefore representatives with distinct complete packet serializations are automatically pairwise nonisomorphic, and their normalized-label orbits are disjoint.

The exact disjoint orbit sums are

- `5,050,080` for `r=2`;
- `11,476,080` for `r=4`;
- `27,213,300` for `r=6`;
- `69,824,160` for `r=8`;
- `194,934,600` for `r=10`.

Each is **equal** to the independently computed exact connected degree-sector total.

This equality is the decisive completeness certificate. If any nonisomorphic graph class were missing — including a hypothetical second nonisomorphic class sharing a packet already represented — that omitted class would contribute a strictly positive normalized-label orbit, so the selected disjoint orbit sum would be strictly smaller than the exact sector total. Equality rules that out.

Hence every `U_BR(11)` isomorphism class is represented exactly once by a distinct packet, and no stable-packet collision exists at `n=11`.

## 3. Exact packet separation

For every retained representative the checker recomputes from adjacency alone:

1. every primitive simple unoriented cycle and root profile `m_X(x)`;
2. the frozen ordinary 1-WL recurrence;
3. the same lossless complete finite-DAG packet serialization used by Q25;
4. the exact automorphism-group order.

Hashing is never used to decide packet equality. Full serializations are dictionary keys and are compared directly. SHA-256 is applied only after exact equality/separation has already been decided, to pin the finite packet image.

Per-sector packet-image SHA-256 values are:

- `r=2`: `08d08ab8ce8ce8237ecada9ea9ec76c7a6c87a4bf06ef455c61aafb28cdc8738`
- `r=4`: `0527cbbeb5474498b2252d9e417dba49fa020ef0a9f6d39d2a26631c2f11cd71`
- `r=6`: `fd60fdc131487e40f0a40e26ef9e63fd5d7a0c6d2b2e01763c2fa4189055852d`
- `r=8`: `e94a4220802e9b99b446a619dd203194b0fb7007b47980559649313d68e1315c`
- `r=10`: `e84ca3046ab07862854cdb783e8ee0ac6d54eed061f53a2c28f03d5adc1f3fa0`

Combined `n=11` packet-image SHA-256:

`195df8a4567cec68de826035eee044c9915b3dafb207f260324a04e29a3535d2`.

All `1,352` complete packet serializations are distinct even across degree sectors.

## 4. Verification surface

Deterministic checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER_CHECK_20260902.py`

Frozen certificate summary:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER/P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1.json`

The checker is Python standard-library only and reproduces the candidate discovery with an explicitly coded PRNG. Its required terminal line is:

`PASS Q27 n=11 exact orbit certificate: representatives=1352 normalized_connected=308498220 stable_packets=1352 collision=0 lower_bound=n<=11`

The certificate summary freezes exact sector totals, representative counts, deterministic closure samples, automorphism-size census, stabilization census and packet-image digests. The random-looking discovery stream is not trusted for completeness; the independently computed exact orbit equality is.

## 5. Tool reuse and method boundary

Tool coverage was resolved before introducing task-local machinery:

- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA` supplies the collision/fiber viewpoint;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE` supplies the orbit/stabilizer and automorphism viewpoint.

The Q25 degree-count / orbit-stabilizer certificate pattern and frozen packet semantics are reused directly. No new general-purpose Enterprise tool family is proposed.

Method harvest:

`RESULT_ONLY / DETERMINISTIC_DISCOVERY_PLUS_EXACT_ORBIT_STABILIZER_COMPLETENESS_CERTIFICATE`.

Ordinary 1-WL/color refinement, finite graph automorphisms, degree-sequence recurrence, configuration-model discovery and orbit-stabilizer accounting are standard mathematics/algorithms. No historical novelty claim is made.

## 6. Scope guard: graph-level injectivity is not canonical labeling

The theorem proved here is graph-level injectivity of one anonymous stabilized packet on a bounded finite universe. It does not promote the observable to a pointwise canonical labeling, a universal reconstruction theorem, a stronger WL hierarchy, a spectral/zeta invariant, Working Truth, Foundation authority or L4.

The taskbook explicitly forbids repairing the observable before its first failure is located; Q27 obeys that restriction and changes no observable component.

## 7. Terminal boundary

The legal terminal class reached is

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11`.

The exact accepted-strength candidate for Driver review is:

`FROZEN_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_EXACT_GRAPH_LEVEL_INJECTIVITY_ON_U_BR_FOR_4_LE_N_LE_11_ONLY`.

The first possible collision now begins at `n=12`, but the Q27 task explicitly forbids continuing to `n=12` inside this execution. No successor is self-published here.

Next control-plane action: Driver review this exact `n=11` bounded certificate. If accepted and a continuation is still justified, only a separately published task may address `n=12`; it must keep the observable frozen unless an independent governance decision says otherwise.
