# P000 Philosophy-First Q29 — Frozen Return-Profile 1-WL n=13 Collision Frontier

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N13-COLLISION-FRONTIER`  
Publication: `TP2-2BB590EA80230A7A7D4C`  
Researcher: `EM-P000Q29N13-6C1B4E`  
Claim: `chatgpt-p000q29n13-20260902-2030-6c1b4e`  
Execution branch: `research/p000-phil-q29-return-profile-1wl-n13-em-p000q29n13-6c1b4e`  
Execution record: `ER-B045187F5EDFF39075A8`  
Hard target: `P000_RETURN_PROFILE_1WL_N13_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

## Terminal verdict

`SUCCESS / RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N13`

The Q22/Q25/Q27/Q28 observable is kept bit-for-bit unchanged:

\[
c_0(x)=m_X(x),\qquad
c_{t+1}(x)=\Bigl(c_t(x),\operatorname{multiset}_{y\sim x}c_t(y)\Bigr),
\]

where `m_X(x)` is the primitive simple-cycle multiplicity profile through root `x`, and the graph-level output is the anonymous stabilized semantic packet `R_inf(X)`.

This execution proves the exact bounded statement

\[
R_\infty(X)=R_\infty(Y),\quad X,Y\in U_{BR}(13)
\Longrightarrow X\cong Y.
\]

Together with the accepted Q22/Q25/Q27/Q28 prefix, the rigorous finite frontier is now

\[
4\le n\le 13.
\]

No statement is made for `n>=14`.

## 1. Countermodel-first discovery

At `n=13`, handshaking forces the number `r` of degree-3 Cells to lie in

\[
r\in\{2,4,6,8,10,12\}.
\]

Each sector was attacked first by deterministic seeded configuration-model sampling. Every sampled graph was checked directly from adjacency using the frozen primitive-return profile and unchanged ordinary 1-WL packet. Unique packet representatives were accumulated until the exact orbit-stabilizer cover closed.

The recovery/re-execution seeds that produced the frozen representative set were:

- `r=2`: seed 1302, 232 accepted samples;
- `r=4`: seed 1304, 21,346 samples;
- `r=6`: seed 1306, 90,000 samples; seed 2306, 36,680 samples;
- `r=8`: seeds 1308 and 2308, 100,000 samples each; seed 3308, 71,139 samples;
- `r=10`: seeds 1310, 2310, 3310, 100,000 samples each; seed 4310, 38,467 samples;
- `r=12`: seed 1312, 36,727 samples.

The sampling route is discovery only. Terminal completeness comes from the independent exact count/orbit certificate below.

## 2. Independent exact completeness authority

For every sector `3^r 2^(13-r)`, the checker independently computes the exact number `N_(13,r)` of connected simple normalized-label realizations using the same accepted degree-state recurrence used in Q27/Q28.

For every frozen representative it independently recomputes from adjacency:

1. connectivity and exact degree sector;
2. all primitive simple unoriented cycles and every root profile `m_X(x)`;
3. the unchanged ordinary 1-WL recurrence and complete anonymous packet serialization;
4. the exact automorphism-group order by adjacency-preserving backtracking.

Every automorphism preserves degree, hence one isomorphism type contributes exactly

\[
\frac{r!(13-r)!}{|\operatorname{Aut}(G)|}
\]

normalized labelings in sector `r`.

The exact sector certificate is:

| degree-3 count `r` | exact normalized connected realizations | representatives | stable packets | collision? |
|---:|---:|---:|---:|:---|
| 2 | 858,211,200 | 35 | 35 | no |
| 4 | 2,430,570,240 | 581 | 581 | no |
| 6 | 6,963,440,400 | 3,159 | 3,159 | no |
| 8 | 21,063,218,400 | 6,374 | 6,374 | no |
| 10 | 68,047,938,000 | 4,541 | 4,541 | no |
| 12 | 235,189,785,600 | 839 | 839 | no |
| **total** | **334,553,163,840** | **15,529** | **15,529** | **no** |

For every sector the checker verifies exactly

\[
\sum_{[G]}
\frac{r!(13-r)!}{|\operatorname{Aut}(G)|}
=
N_{13,r}.
\]

The 15,529 frozen packet serializations are pairwise distinct globally, including across degree sectors. Different packets are isomorphism invariants, so the selected representatives are distinct isomorphism classes. Since their exact orbit sizes sum to the independently computed total number of normalized connected realizations, no connected isomorphism class is missing. Consequently there is no hidden second isomorphism class inside any equal-packet fiber.

Therefore no nonisomorphic equal-packet collision exists at `n=13`.

## 3. Frozen packet-image digests

SHA-256 pins the exact packet-serialization images; hashes are transport/integrity pins, not substitutes for exact equality.

- `r=2`: `c038bf95a0315e04e8bff7bafacd5dd3276295b446cc796c7b008f86a57d92c1`
- `r=4`: `35776ac6c676164c5137d6ffd7262d3dbed7f9669fce891ed5c577f64e87cc38`
- `r=6`: `9ec3a4c5cadf74b5e20a5bca26d9098139939dab7a841dbb3c488cb653e16168`
- `r=8`: `d9bd46ae70d16a3424392f17f5b80dc1551ea764e30925047af1e289bf529cd2`
- `r=10`: `6a35f902944152c785925454f6bd4e238c68bff641da0f464533708558859571`
- `r=12`: `62988e4b43c090df2300b8e56bd32358f21442cc565194d7d08b6643660746c4`
- combined: `67cb46560ac86552b1ac0103de24a01192f5d85ccc6ec98e9e46e239308efbae`

## 4. Frozen machine artifacts

Exact orbit certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N13_COLLISION_FRONTIER/P000_Q29_RETURN_PROFILE_1WL_N13_EXACT_ORBIT_CERTIFICATE_V1.json`

Representative payload shards:

- `P000_Q29_N13_REPRESENTATIVES_R2_A_V1.json` — sectors 2,4,12;
- `P000_Q29_N13_REPRESENTATIVES_R2_B_V1.json` — sector 6;
- `P000_Q29_N13_REPRESENTATIVES_R2_C_V1.json` — sector 8;
- `P000_Q29_N13_REPRESENTATIVES_R2_D_V1.json` — sector 10.

Deterministic standard-library checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N13_COLLISION_FRONTIER_CHECK_20260902.py`

Fresh local replay returned:

`PASS Q29 n=13 exact orbit certificate: representatives=15529 normalized_connected=334553163840 stable_packets=15529 collision=0 lower_bound=n<=13`

### Recovery provenance

A prior interrupted response had already persisted a partial discovery package on the same execution branch (`A`, `B1`, `B2`, `C1` plus a compact metadata certificate). Recovery inspection preserved those files as provenance only: they do not contain a complete six-sector terminal payload and are not used as completeness evidence. The terminal certificate above binds only the independently re-executed complete `R2_*` shards.

## 5. Method reuse and exact boundary

This task does not create a new general-purpose tool. It reuses the accepted Q27/Q28 exact finite-enumeration pattern and the project finite-symmetry/orbit-stabilizer calculus: exact degree-state count, primitive-return profile, ordinary 1-WL semantic packet, automorphism backtracking, and orbit-cover completeness.

The terminal class is

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N13`.

The exact review candidate strength is:

`FROZEN_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_EXACT_GRAPH_LEVEL_INJECTIVITY_ON_U_BR_FOR_4_LE_N_LE_13_ONLY`.

This does **not** establish:

- any statement for `n>=14`;
- a universal finite-graph reconstruction theorem;
- vertexwise canonical identification or a canonical-label algorithm;
- 2-WL, spectra, zeta, full cycle incidence, or any strengthened observable;
- Working Truth, Foundation, L4, canonical promotion, or historical novelty.

Q29 stops exactly at `n=13` by its kill rule.
