# P000 Philosophy-First Q28 — Frozen Return-Profile 1-WL n=12 Collision Frontier

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N12-COLLISION-FRONTIER`  
Publication: `TP2-C74E704488CBF01A602D`  
Researcher: `EM-P000-89C4F2`  
Claim: `chatgpt-p000-q28-20260902-1302-89c4f2`  
Execution branch: `research/p000-phil-q28-return-profile-1wl-n12-em-p000-89c4f2`  
Hard target: `P000_RETURN_PROFILE_1WL_N12_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

## Terminal verdict

`SUCCESS / RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12`

The Q22/Q25/Q27 observable is unchanged:

\[
c_0(x)=m_X(x),\qquad
c_{t+1}(x)=\Bigl(c_t(x),\operatorname{multiset}_{y\sim x}c_t(y)\Bigr),
\]

where `m_X(x)` is the primitive simple-cycle multiplicity profile through root `x`, and the graph-level output is the anonymous stabilized semantic packet `R_inf(X)`.

Q28 proves, exactly at the first unresolved size,

\[
R_\infty(X)=R_\infty(Y),\quad X,Y\in U_{BR}(12)
\Longrightarrow X\cong Y.
\]

Together with the accepted Q22/Q25/Q27 prefix, the rigorous collision-free frontier is therefore

\[
4\le n\le 12.
\]

No claim is made for `n>=13`, and no universal reconstruction, canonical-label, 2-WL, spectral, zeta, or stronger-observable theorem is claimed.

## 1. Countermodel-first discovery

The task required searching for failure before escalating to a complete certificate. I kept the observable bit-for-bit frozen and traversed exact degree-preserving 2-switch neighborhoods in each admissible `n=12` degree sector.

For `r=#{v:deg(v)=3}`, handshaking forces

\[
r\in\{2,4,6,8,10,12\}.
\]

The switch search encountered the following isomorphism-class counts among all simple realizations, before connectivity filtering:

| `r` | all simple isomorphism classes seen | connected `U_BR(12)` representatives |
|---:|---:|---:|
| 2 | 73 | 29 |
| 4 | 486 | 351 |
| 6 | 1,545 | 1,373 |
| 8 | 1,999 | 1,892 |
| 10 | 872 | 835 |
| 12 | 94 | 85 |
| **total connected** |  | **4,565** |

At every discovery step, graphs with an already-seen complete frozen packet were checked for exact graph isomorphism. No nonisomorphic equal-packet pair was found. This search is useful discovery evidence only; terminal completeness does **not** rely on switch-graph connectivity.

## 2. Independent completeness authority

For each sector `3^r 2^(12-r)`, the checker independently computes the exact number `N_(12,r)` of connected simple realizations on normalized labels using a degree-state recurrence. Independently, every frozen representative is verified from adjacency alone for:

1. connectivity and exact degree sector;
2. every primitive simple unoriented cycle and every root profile `m_X(x)`;
3. the unchanged ordinary 1-WL recurrence and complete semantic packet serialization;
4. the exact automorphism-group order by adjacency-preserving backtracking.

Every automorphism preserves degree, so one unlabeled representative contributes exactly

\[
\frac{r!(12-r)!}{|\operatorname{Aut}(G)|}
\]

normalized labelings in its sector.

The exact sector certificate is:

| degree-3 count `r` | exact normalized connected realizations | graph-isomorphism representatives | stable packets | collision? |
|---:|---:|---:|---:|:---|
| 2 | 63,504,000 | 29 | 29 | no |
| 4 | 161,965,440 | 351 | 351 | no |
| 6 | 423,705,600 | 1,373 | 1,373 | no |
| 8 | 1,183,502,880 | 1,892 | 1,892 | no |
| 10 | 3,561,440,400 | 835 | 835 | no |
| 12 | 11,543,439,600 | 85 | 85 | no |
| **total** | **16,937,557,920** | **4,565** | **4,565** | **no** |

For every sector the checker verifies exactly

\[
\sum_{[G]}
\frac{r!(12-r)!}{|\operatorname{Aut}(G)|}
=
N_{12,r}.
\]

The left side is a disjoint union of normalized labeling orbits of valid pairwise nonisomorphic representatives. The right side is an independently computed total count. Equality leaves no unrepresented connected isomorphism type.

Finally, all 4,565 complete packet serializations are pairwise distinct globally, including across degree sectors. Hence no nonisomorphic equal-packet collision exists at `n=12`.

## 3. Frozen packet-image digests

SHA-256 is used only to pin already constructed complete serialization images; equality is tested on the raw complete serialization.

- `r=2`: `ed91e3ff2a67244632fb7c85b06b4f99f04d90e6e41f18728677a92af498ab6a`
- `r=4`: `a883a730d51d50cadd0ec89615c1ea88a5a4077a7de24ccba9aeeeef84a8d3b1`
- `r=6`: `65390b31b86c6a4c8a3833603045ec8310e05e6fd8a101746ebc0e15ec6c80fb`
- `r=8`: `1f9d61310be9c5dffeff5d0c4d496537c2c4b8bbcee0afd49fcfc80b94f006f9`
- `r=10`: `7de0d6a3d5371fe4994ee41ea38d2dde7540c1bbebc862567ecdd50eaee54922`
- `r=12`: `9c0c68896bb50488c16d2805920c75b46dcb6ddaa18bae43217366ffcf0b8c47`
- combined: `0503bb2767926a155c8ceb09c15ebffdf4d5750fe1584b214108cc74c99ff814`

## 4. Frozen machine artifacts

Certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N12_COLLISION_FRONTIER/P000_Q28_RETURN_PROFILE_1WL_N12_EXACT_ORBIT_CERTIFICATE_V1.json`

Representative payload shards:

- `P000_Q28_N12_REPRESENTATIVES_A_V1.json`
- `P000_Q28_N12_REPRESENTATIVES_B_V1.json`
- `P000_Q28_N12_REPRESENTATIVES_C_V1.json`
- `P000_Q28_N12_REPRESENTATIVES_D_V1.json`

Deterministic standard-library checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N12_COLLISION_FRONTIER_CHECK_20260902.py`

The checker returns:

`PASS Q28 n=12 exact orbit certificate: representatives=4565 normalized_connected=16937557920 stable_packets=4565 collision=0 lower_bound=n<=12`

## 5. Exact strength and negative boundary

The terminal class is

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12`.

The exact accepted-strength candidate for Driver review is:

`FROZEN_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_EXACT_GRAPH_LEVEL_INJECTIVITY_ON_U_BR_FOR_4_LE_N_LE_12_ONLY`.

This does **not** establish:

- any statement for `n>=13`;
- a universal finite-graph reconstruction theorem;
- vertexwise canonical identification or a canonical-label algorithm;
- 2-WL, spectra, zeta, full-cycle-incidence, or any strengthened observable;
- Working Truth, Foundation, L4, canonical promotion, or historical novelty.

If Driver accepts this result, Q28 stops exactly at `n=12`. Any `n=13` investigation requires a separately published successor.
