# P000 Philosophy-First Q27 — Frozen Return-Profile 1-WL n=11 Collision Frontier

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER`  
Publication: `TP2-875D6C62E617BCC7CE63`  
Researcher: `EM-P000-7A4951`  
Claim: `chatgpt-p000-q27-20260902-0920`  
Execution branch: `research/p000-phil-q27-return-profile-1wl-n11-collision-frontier`  
Hard target: `P000_RETURN_PROFILE_1WL_N11_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

## Terminal verdict

`SUCCESS / RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11`

The Q22/Q25 observable is unchanged:

\[
c_0(x)=m_X(x),\qquad
c_{t+1}(x)=\Bigl(c_t(x),\operatorname{multiset}_{y\sim x}c_t(y)\Bigr),
\]

where `m_X(x)` is the primitive simple-cycle multiplicity profile through root `x`, and the graph-level output is the anonymous stabilized semantic packet `R_inf(X)`.

Q27 proves, exactly at the first unresolved size,

\[
R_\infty(X)=R_\infty(Y),\quad X,Y\in U_{BR}(11)
\Longrightarrow X\cong Y.
\]

Together with the accepted Q22/Q25 prefix, the rigorous collision-free frontier is therefore

\[
4\le n\le 11.
\]

No claim is made for `n>=12`, and no universal reconstruction or canonical-label theorem is claimed.

## 1. Exact n=11 census and separation

For `n=11`, if `r` is the number of degree-3 Cells, handshaking forces `r` even. Since `U_BR(11)` requires at least one degree-3 Cell and all degrees are 2 or 3,

\[
r\in\{2,4,6,8,10\}.
\]

The final deterministic certificate gives:

| degree-3 count `r` | exact normalized connected realizations | graph-isomorphism types | stable packets | collision? |
|---:|---:|---:|---:|:---|
| 2 | 5,050,080 | 23 | 23 | no |
| 4 | 11,476,080 | 197 | 197 | no |
| 6 | 27,213,300 | 536 | 536 | no |
| 8 | 69,824,160 | 482 | 482 | no |
| 10 | 194,934,600 | 114 | 114 | no |
| **total** | **308,498,220** | **1,352** | **1,352** | **no** |

Thus every equal frozen-packet fiber in `U_BR(11)` contains exactly one graph-isomorphism type.

The complete n=11 packet image SHA256 is

`195df8a4567cec68de826035eee044c9915b3dafb207f260324a04e29a3535d2`.

Per-sector packet-image SHA256:

- `r=2`: `08d08ab8ce8ce8237ecada9ea9ec76c7a6c87a4bf06ef455c61aafb28cdc8738`
- `r=4`: `0527cbbeb5474498b2252d9e417dba49fa020ef0a9f6d39d2a26631c2f11cd71`
- `r=6`: `fd60fdc131487e40f0a40e26ef9e63fd5d7a0c6d2b2e01763c2fa4189055852d`
- `r=8`: `e94a4220802e9b99b446a619dd203194b0fb7007b47980559649313d68e1315c`
- `r=10`: `e84ca3046ab07862854cdb783e8ee0ac6d54eed061f53a2c28f03d5adc1f3fa0`

## 2. Completeness authority: exact count plus orbit-stabilizer cover

The terminal conclusion does not rely on the representative-discovery route.

For each degree sector `3^r 2^(11-r)`, the checker independently computes the exact number of labeled simple realizations using the same degree-state recurrence audited in Q25. It then obtains the connected count by subtracting all realizations in which the component containing a distinguished label is proper.

For every frozen representative `G`, the checker recomputes from adjacency alone:

1. connectivity and the exact degree sector;
2. every primitive simple unoriented cycle and all root profiles `m_X(x)`;
3. the frozen ordinary 1-WL recurrence and complete semantic packet serialization;
4. the exact automorphism-group order by adjacency-preserving backtracking.

Because every automorphism preserves vertex degree, the number of normalized labelings represented by an isomorphism type `[G]` in sector `r` is exactly

\[
\frac{r!(11-r)!}{|\operatorname{Aut}(G)|}.
\]

The 1,352 frozen representatives have pairwise distinct complete packet serializations. Since the packet is an isomorphism invariant, these representatives are pairwise nonisomorphic. The checker verifies, sector by sector,

\[
\sum_{[G]}\frac{r!(11-r)!}{|\operatorname{Aut}(G)|}=N_{11,r},
\]

with the five exact equalities

`5,050,080`, `11,476,080`, `27,213,300`, `69,824,160`, `194,934,600`.

The left side is a disjoint union of normalized labeling orbits of valid, pairwise nonisomorphic representatives; the right side is the independently computed total number of normalized connected realizations. Equality therefore leaves no unrepresented isomorphism type. The representative set is complete independently of how it was discovered.

Finally, all 1,352 complete packet serializations are distinct, including across degree sectors. Hence no nonisomorphic equal-packet collision exists at `n=11`.

SHA256 is used only to pin the already constructed complete packet image; packet equality itself is exact serialization equality.

## 3. Countermodel-first discovery route

The task required structural countermodel search before escalating to a full census. The discovery route exploited the mandatory presence of a degree-2 vertex at odd `n=11`.

Let `v` be degree 2 with neighbors `a,b`.

- If `a` and `b` are nonadjacent, suppressing `v` and adding the edge `ab` produces a connected simple graph in `U_BR(10)`. Thus the original graph is obtained by subdividing an edge of an n=10 object.
- If no degree-2 vertex is suppressible, then every degree-2 vertex has adjacent neighbors and lies in a triangle. Connectedness and the degree bound force exactly two local gadget types:
  1. one degree-2 vertex on an edge joining two degree-3 vertices (an edge-triangle gadget);
  2. two adjacent degree-2 vertices sharing one degree-3 vertex (a pendant-triangle gadget).

Delete all degree-2 vertices in the second case and let the remaining core contain `a` degree-1 and `b` degree-2 vertices. A pendant triangle consumes two deleted degree-2 vertices; an edge triangle consumes one deleted degree-2 vertex for a paired adjacent pair of degree-2 core vertices. Hence

\[
11-r=2a+\frac b2,\qquad 4a+b=22-2r.
\]

The feasible exceptional core signatures are exactly:

- `r=2`: none;
- `r=4`: none;
- `r=6`: `(a,b)=(2,2)`, core degree sequence `3,3,2,2,1,1`;
- `r=8`: `(a,b)=(0,6)` or `(1,2)`, core degree sequences `3,3,2,2,2,2,2,2` and `3,3,3,3,3,2,2,1`;
- `r=10`: `(a,b)=(0,2)`, equivalently a ten-vertex core whose two degree-2 vertices are adjacent before the edge-triangle expansion.

This decomposition generated the candidate surface from accepted n=10 representatives plus the finite exceptional cores. It was useful for discovery and adversarial checking, but it is deliberately **not** the completeness authority: terminal completeness comes from the independent exact count/orbit-cover equality in §2.

## 4. Frozen machine artifacts

Certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER/P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1.json`

Deterministic checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER_CHECK_20260902.py`

The checker is standard-library only and returns on the frozen certificate:

`PASS Q27 n=11 exact orbit certificate: representatives=1352 normalized_connected=308498220 stable_packets=1352 collision=0 lower_bound=n<=11`

## 5. Exact strength and negative boundary

The terminal class is

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11`.

The accepted-strength candidate for Driver review is:

`FROZEN_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_EXACT_GRAPH_LEVEL_INJECTIVITY_ON_U_BR_FOR_4_LE_N_LE_11_ONLY`.

This does **not** establish:

- any statement for `n>=12`;
- a universal finite-graph reconstruction theorem;
- vertexwise canonical identification or a canonical-label algorithm;
- 2-WL, spectra, zeta, full-cycle-incidence, or any strengthened observable;
- Working Truth, Foundation, L4, canonical promotion, or historical novelty.

The immediate mathematical question after Driver acceptance, if independently authorized, is the first possible collision at `n=12`; Q27 itself stops at `n=11` exactly as required by the taskbook.
