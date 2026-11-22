# R762JA — Eight-triple 47→45 Port–Euler compression; k=0 upper bound ≤46

Date: 2026-11-22 (Asia/Shanghai).
Scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (frozen; not rebased).
Scope: six-axis **composite Port–Euler observer**; no signed native P000 Cell/time/force/rotation lifting.
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATES_VERIFIED / NOT_REVIEWED**.
Predecessors: R762IR, R762IU (≤47), R762IV, R762IW, R762IX, R762IY, R762IZ.
No native Result/Review or shared-task CLAIM is inferred.

## Exact model and new theorem

Let (A={0,1,2,3,4,5}). The 15 Ports are (P=inom A2), and the 20 support types are (mathcal S=inom A3). An event of support (S={a,b,c}) joins any two of the three Ports (ab,ac,bc), allowing repeated edges. A legal closed history with active Port set (Vsubseteq P) and prescribed start (pin V) is a connected multigraph on precisely (V), all active degrees positive and even, and no inactive incidence. Let (N_{p,V}(n)>0) mean such a history with support-count vector (n).

**Theorem R762JA (complete eight-triple terminal class).** For every legal 47-event history with precisely eight supports of multiplicity 3, eleven of multiplicity 2, and one of multiplicity 1 (no absent supports), there is a legal 45-event history with the same (V,p), all 20 positive supports and per-support parity, obtained by reducing exactly one triple multiplicity (3	o1):

[
N_{p,V}(n)>0,quad (t,d,s,z)=(8,11,1,0)
quadLongrightarrowquad
exists j:n_j=3, N_{p,V}(n-2e_j)>0.
]

This is a complete computer-assisted proof at the composite-observer level. The certificate checker below uses only Python's standard library and exact integers, independent of the numerical candidate generator.

## Exhaustive three-way reduction

**(i) Some triple support contains an inactive Port.** Every support has a positive event count. Therefore two inactive Ports cannot share an axis: their three-axis union would provide a positive support with fewer than two usable Port vertices. Thus inactive Ports form a matching in (K_6). If an inactive Port lies in a triple support (j), precisely two Port vertices in that support remain active. The three events of (j) must lie along their unique edge. Delete two parallel copies. This keeps an edge of type (j), all active degrees' parity, the active set and connectivity.

**(ii) Every triple support is fully active, but some triple is not essential to its triangle union.** Write (T) for the eight triple supports and (G(T)) for the graph formed by *all three possible edges* of each support triangle. If (jin T) is not essential to the connected-component partition of (G(T)), then its three Port vertices are connected in (G(Tsetminus{j})). Replace its three events by a single allowed edge (uv). The resulting parity change at those vertices is an even GF(2) boundary, either zero or two odd Port vertices. Route that boundary along a path of edges in (G(Tsetminus{j})). For each remaining triple support, group path contributions into a local even boundary. Any such local boundary is realized by **exactly three edges connecting all three Port vertices**: the 3-cycle for zero boundary, or one edge between the odd pair and two parallel edges to the third vertex otherwise. This restores overall even degrees. Since the other triple supports now each connect their entire Port triples and (j)'s vertices are connected through them, reachability in the original graph is preserved. Other supports are unchanged. The result is a legal 45-event history.

**(iii) All eight fully active triple supports are essential.** Enumerate every (inom{20}{8}=125{,}970) eight-support family by integer union-find over the fixed 15 Ports. Exactly **4,920** are all-essential; under the complete six-axis permutation group (S_6) they form **16** orbits. The union of their support triangles covers **13, 14, or 15** Ports. Since every triple is fully active, the inactive matching (M=Psetminus V) must lie in the complement of those covered Ports. For each orbit representative, enumerate every such matching and each of the 12 possible singleton supports outside (T); select the first support (jin T) and prescribe (n'_j=1), the other seven triples remaining 3, the singleton remaining 1 and the other eleven supports remaining 2.

This gives **exactly 300** representative parameter cases, grouped by uncovered Port count 0/1/2 as 120/96/84, or by inactive Port count 0/1/2 as 192/96/12. All 300 have explicit 45-edge allocations satisfying exact support counts, positive even degrees on exactly (V), zero degree outside (V), and connectivity. The 300 integer edge-allocation certificates are in `R762JA_CERTS.b64`; they are checked in the same deterministic orbit/matching/singleton order by `R762JA_VERIFY_CERTS.py`. Axis equivariance transports each representative witness to all its labelled (S_6) configurations. A connected even-degree graph admits an Euler circuit beginning at every (pin V).

The three cases exhaust all legal histories in this histogram. This proves the theorem without relying on an unverified optimizer output. The candidate constructor used SciPy/HiGHS integer optimization and connectivity cuts, but the published certificates are checked by a separate exact standard-library program.

## Independent exact-verification details

- (4,920) all-essential eight-support sets; (16) permutation orbits.
- (300/300) exact 45-event certificates passed.
- Certificate stream: each of the 60 support-edge counts is an integer in ({0,1,2,3}); four 2-bit integers are packed per byte, so 15 bytes per witness. Exactly 4,500 raw bytes, zlib-compressed and base64 encoded.
- Raw stream SHA-256: `6b30b9be0cea2a021f894c2e5b3d82fec736b910faf52a0409a6145aa6b21980`.
- Compressed stream SHA-256: `808000aeed1e01de0d9ff3c0336be6c22b80f92b6a467b8d204f79aacff741f5`.
- Local author validation on 2026-11-22: **PASS**, 300 cases, no unresolved case. Integer verification checks the actual certificates, not MILP tolerance, solver status, or just a hash.

## Derived improvement of the full k=0 bound

The existing R762IU author-side theorem gives at most 47 events for any legal vector (nin{0,1,2,3}^{20}), preserving the original active set, starting Port, positive supports, and support-count parity. If a compressed witness has exactly 47 events, its histogram with (tle10) is exactly one of:

| ((t,d,s,z)) | Terminal 47→45 source |
|---|---|
| ((7,13,0,0)) | R762IV |
| ((8,11,1,0)) | **R762JA (new)** |
| ((9,9,2,0)) | R762IY + R762IZ, with nonessential reduction |
| ((9,10,0,1)) | R762IW, with nonessential reduction |
| ((10,7,3,0)) | R762IY |
| ((10,8,1,1)) | R762IX |

For (tge11), the earlier R762IR triangle-redundancy lemma supplies a reducible triple, and the explicit GF(2) repair above handles a fully active nonessential triple; if its triangle has only two active Ports, parallel-pair deletion applies. Hence every 47-event witness has a 45-event witness, while witnesses already at 46 or less need no change. **Consequently, conditional on the cited author-side antecedent theorems, the entire k=0 composite Port–Euler class has a uniform bound of 46 events**:

[
oxed{N_{p,V}(n)>0, nin{0,1,2,3}^{20}
Longrightarrow exists hle n: N_{p,V}(h)>0, 
operatorname{supp}h=operatorname{supp}n, hequiv n (mod2),sum_S h_Sle46.}
]

This improves the previously published author-side bound 47. All cited lemmas and finite checks retain their actual author-verification status; **no independent mathematical Review or canonical theorem admission has occurred**. The 54-event upper bound previously stated for the broader fourfold-support case remains unchanged.

## Preservation and next questions

A deleted pair of same-support Port–Euler events can be inserted as a parallel pair on an existing edge of that support. The preserved observer is **active Port set + support presence + support parity + existence of a closed Euler history + chosen start**. This compression is not a proof of equality of the full path-order/branch/time/native signed X6 residual state.

Next, test 46-event terminal histograms for a 44-event compression or construct an invariant lower-bound witness; independently audit the load-bearing prior reduction and all-essential orbit counts; then investigate the fourfold critical support and native signed P000 bridge. The original scientific pin remains unchanged.
