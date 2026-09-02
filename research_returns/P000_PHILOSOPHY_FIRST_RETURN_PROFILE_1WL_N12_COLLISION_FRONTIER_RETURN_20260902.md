# P000 Philosophy-First Q28 — Frozen Return-Profile 1-WL n=12 Collision Frontier (independent control-valid re-execution)

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N12-COLLISION-FRONTIER`  
Publication: `TP2-C74E704488CBF01A602D`  
Researcher: `EM-P000-AED46E`  
Claim: `chatgpt-p000q28-reexec-20260902-1920-8c7a2d`  
Execution branch: `research/p000-q28-n12-reexecution-em-p000-aed46e`  
Execution branch base: `0afd9a3021c86225eb1b79a8c79e69bf8fbe513d`  
Hard target: `P000_RETURN_PROFILE_1WL_N12_FIRST_COLLISION_OR_EXACT_LOWER_BOUND_CLASSIFIED`

## Terminal verdict

`SUCCESS / RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12`

The Q22/Q25/Q27 observable is unchanged:

\[
c_0(x)=m_X(x),\qquad
c_{t+1}(x)=\Bigl(c_t(x),\operatorname{multiset}_{y\sim x}c_t(y)\Bigr),
\]

where `m_X(x)` is the primitive simple-cycle multiplicity profile through root `x`, and the graph-level output is the anonymous stabilized semantic packet `R_inf(X)`.

This re-execution proves

\[
R_\infty(X)=R_\infty(Y),\quad X,Y\in U_{BR}(12)
\Longrightarrow X\cong Y.
\]

Together with the accepted Q22/Q25/Q27 prefix, the rigorous bounded frontier is

\[
4\le n\le 12.
\]

No statement is made for `n>=13`, and no universal reconstruction, canonical-label, 2-WL, spectral, zeta, or stronger-observable theorem is claimed.

## 1. Control-integrity / independence note

The current `main` removed the earlier Q28 result/execution records because that evidence package was bound to a non-winning claim. This run therefore treated Q28 as a fresh mathematical re-execution under the current winning claim.

To avoid silently inheriting the withdrawn conclusion, this run read only the current Q28 taskbook plus the accepted Q27 frozen definition/checker until the new n=12 certificate had independently closed. It did **not** read the surviving earlier Q28 return/checker/artifacts during discovery or certification. Only after the new certificate passed was the earlier Q28 return opened for comparison.

Post-freeze comparison found exact agreement in every sector count and every packet-image digest. Thus the old mathematical evidence is independently replicated, while the present Result is bound to the current authenticated claim and execution record.

## 2. Countermodel-first discovery route

Handshaking forces the number `r` of degree-3 Cells at n=12 to lie in

\[
r\in\{2,4,6,8,10,12\}.
\]

Before claiming completeness, the run searched all six sectors countermodel-first with deterministic seeded degree-preserving configuration-model sampling. The complete frozen observable was recomputed directly from adjacency for every candidate. No nonisomorphic equal-packet witness appeared.

Discovery was deliberately not used as completeness authority. One useful adversarial signal occurred in the `r=6` sector: the first seed left an exact orbit deficit of `32,400`, equal to

\[
\frac{6!6!}{16}.
\]

A second independent seed found exactly one additional packet representative with automorphism order 16, closing that deficit. This is recorded as discovery evidence only; the terminal proof is the independent exact count/orbit cover below.

Frozen discovery runs:

- `r=2`: seed 1202, 40,000 samples;
- `r=4`: seed 1204, 70,000 samples;
- `r=6`: seed 1206, 60,000 samples, then seed 2206, 60,000 samples;
- `r=8`: seed 1208, 100,000 samples;
- `r=10`: seed 1210, 70,000 samples;
- `r=12`: seed 1212, 30,000 samples.

## 3. Independent exact completeness authority

For each sector `3^r 2^(12-r)`, the checker independently computes the exact number `N_(12,r)` of connected simple normalized-label realizations using the accepted degree-state recurrence.

Every frozen representative is then independently recomputed from adjacency for:

1. connectivity and exact degree sector;
2. every primitive simple unoriented cycle and root profile `m_X(x)`;
3. the unchanged ordinary 1-WL recurrence and complete semantic packet serialization;
4. the exact automorphism-group order by adjacency-preserving backtracking.

Every automorphism preserves degree, so one isomorphism type contributes exactly

\[
\frac{r!(12-r)!}{|\operatorname{Aut}(G)|}
\]

normalized labelings in sector `r`.

The exact sector certificate is:

| degree-3 count `r` | exact normalized connected realizations | representatives | stable packets | collision? |
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

The representatives in a sector have pairwise distinct exact packet serializations, hence are pairwise nonisomorphic. The orbit sum equals an independently computed total normalized connected count, so no connected isomorphism type is missing. Finally, the 4,565 exact packet serializations are pairwise distinct globally, including across degree sectors.

Therefore no nonisomorphic equal-packet collision exists at `n=12`.

## 4. Frozen packet-image digests

SHA-256 pins the already constructed exact packet serialization images; hash equality is not used instead of packet equality.

- `r=2`: `ed91e3ff2a67244632fb7c85b06b4f99f04d90e6e41f18728677a92af498ab6a`
- `r=4`: `a883a730d51d50cadd0ec89615c1ea88a5a4077a7de24ccba9aeeeef84a8d3b1`
- `r=6`: `65390b31b86c6a4c8a3833603045ec8310e05e6fd8a101746ebc0e15ec6c80fb`
- `r=8`: `1f9d61310be9c5dffeff5d0c4d496537c2c4b8bbcee0afd49fcfc80b94f006f9`
- `r=10`: `7de0d6a3d5371fe4994ee41ea38d2dde7540c1bbebc862567ecdd50eaee54922`
- `r=12`: `9c0c68896bb50488c16d2805920c75b46dcb6ddaa18bae43217366ffcf0b8c47`
- combined: `0503bb2767926a155c8ceb09c15ebffdf4d5750fe1584b214108cc74c99ff814`

## 5. Frozen machine artifacts

Independent re-execution certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N12_COLLISION_FRONTIER/P000_Q28_RETURN_PROFILE_1WL_N12_EXACT_ORBIT_CERTIFICATE_REEXEC_AED46E_V1.json`

Deterministic standard-library checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N12_COLLISION_FRONTIER_CHECK_20260902.py`

The checker returns:

`PASS Q28 n=12 exact orbit certificate: representatives=4565 normalized_connected=16937557920 stable_packets=4565 collision=0 lower_bound=n<=12`

## 6. Exact strength and negative boundary

The terminal class is

`RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N12`.

The exact Driver-review candidate strength is:

`FROZEN_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_EXACT_GRAPH_LEVEL_INJECTIVITY_ON_U_BR_FOR_4_LE_N_LE_12_ONLY`.

This does **not** establish:

- any statement for `n>=13`;
- a universal finite-graph reconstruction theorem;
- vertexwise canonical identification or a canonical-label algorithm;
- 2-WL, spectra, zeta, full cycle incidence, or any strengthened observable;
- Working Truth, Foundation, L4, canonical promotion, or historical novelty.

Q28 stops exactly at n=12. Any n=13 investigation requires a separately published successor after Driver review.
