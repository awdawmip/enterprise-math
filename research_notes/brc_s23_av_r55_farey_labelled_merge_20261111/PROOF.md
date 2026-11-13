# R55 — Exact circular phase merge and complete frozen S23/AV risk recompilation

Status: author-side mathematical derivation with finite exact computation, 2026-11-11. This is an **auxiliary irrational-circle rotation** calculation; it does not assert new native X6 dynamics or a formal accepted Result.

Scientific input held fixed at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Antecedents: R45 exact Farey risk observer; R49 two-state/source-age compiler; R51 Floor Sum rank/select; R52 incidence; R53 labelled age structure; R54 exact Farey phase successor (PR #2027, head e83b08d5cf956ba19634c838c07816715b372ad5).

## Proposition R55-A — Circular merge of labelled historical and source points

Fix an irrational `0<theta<1`, `m,H>=1`, and integer `j`. Historical boundaries are `{z theta}`, labelled by the **original** `0<=z<m`. Source ages `1<=r<=H` have phase `{(j-r)theta}`. Set `t0=min(0,j-H)`, `t1=max(m-1,j-1)`, and `K=t1-t0`.

Assume the exact R54 Farey-neighbor successor for indices `1..K` (when `K=0`, retain the singleton). Let `s_1,...,s_K` be ordered by increasing **upper** error `{-s theta}`. Then

`[t0, t0+s_K, t0+s_(K-1), ..., t0+s_1]`

is the counterclockwise circular order of all indices `t0..t1` by the point `{t theta}`, starting at `t0` (the list is circular and not necessarily numerically anchored at fractional phase zero).

Find the last historical label in this circular list, then traverse once. At each historical point `z`, set `owner=z`; at each source point `t=j-r`, assign source age `r` to the current `owner`. If a point belongs to both sets, process its historical boundary **first** (right-inclusive source assignment). The minimum age assigned to each historical label is exactly its last-source age `tau` in the R49/R45 observer.

**Proof.** Translation of every indexed phase by `t0 theta` preserves circular order. R54 visits positive indices in increasing `{-s theta}`; reversal visits them in increasing `{s theta}`. Thus the displayed cyclic list correctly orders all phases. Between two successive labelled historical boundaries, each source point has precisely the preceding historical label. The initial label is the last historical point preceding the first point under cyclic wrap. Updating the label on an equal-phase historical/source occurrence implements `bisect_right` membership. Taking the smallest positive age for each owner recovers the latest absolute source time. No label quotient is performed. QED.

With a pre-certified Farey pair, the streaming merge uses `K` successor index updates and `K+1` scan positions, `O(m+H+K)` live words if materialized (or `O(m+H)` for a streamed reversed-phase traversal), and `O(K+m+H)` index operations. Its exact `K` depends on the separation of the historical and source index blocks; no universal `O(m+H)` claim is made when `|j|` is unbounded. Each operation has a nonconstant bigint bit cost.

## Frozen S23/AV end-to-end evidence

`m=128`, `H=225`, `J=10^12+128`, `theta in (262204504569236716045286/10^24,262204504569236716045287/10^24)`; both rational endpoints are used to certify stable finite orders. For the two R49 source states:

- `j=61`: contiguous union indices `[-164,127]`, `K=291`.
- `j=225`: contiguous union indices `[0,224]`, `K=224`.

The two parameter endpoints together require 1,030 R54 successor updates and 900 source-age tags; each age vector retains all 128 original historical labels. Full R49 frozen 78 Farey stages reuse state `j=61` twice and state `j=225` 76 times. The R55 implementation checks both endpoint age vectors against independent integer-remainder sort/bisect for each of the 78 stages (156 full comparisons).

The full compiled output has **9,697** positive risk events and **298** maximal affine runs, identical byte-for-byte to the frozen R32/R46/R49 reference, with 15,356 output bytes and SHA-256:

`2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`.

The last affine value is `R_(10^12+128)=-4017401528447+15321634290944 theta`.

Separate full local verifier `VERIFY_R55_FULL.py` checked **594** additional exact small rational configurations, `m=1..9, H=1..11, j in {-7,0,1,3,12,24}`, against independently sorted historical point sets. The published compact verifier `VERIFY_R55_PUBLISHED.py` reproduces the full 298-run SHA and the 156 stage-owner checks. The executed R49 reference verifier regenerated an independent 298-run TSV; a byte comparison with the R55 file and frozen R46 TSV passed.

## Cost accounting and comparison

For bit complexity let `B=ceil(log2(qK+2))` for rational precision `p/q`, and `M(B)` denote multiplication cost. A complete call includes (i) constructing/certifying a rational parameter enclosure, charged separately as `C_precision`; (ii) Farey bracket search, cost measured by its exact integer comparisons on operands up to `O(B)` bits; (iii) `k` R54 successor updates on `O(log K)`-bit indices; (iv) for labelled age merge, `K+1` scan positions, `H` source-age tags, and `m` retained labels; (v) exact Farey stage generation, event formation, and at least `Omega(output_bytes)` serialization.

In the same 82-bit frozen rational midpoint, the measured cut-oracle comparisons were: for `(K,k)=(352,12)` R54 36 Farey integer comparisons + 12 successor updates versus R51 1,271 Floor Sum invocations / 22,481 Euclidean loops; `(352,352)` R54 36 + 352 versus R51 35,507 / 637,819; `(100000,12)` R54 133 + 12 versus R51 1,552 / 32,389; `(1000000,12)` R54 180 + 12 versus R51 1,672 / 37,956. Direct R53 heap/sort oracles inspect all `K` exact residues; the R54 top-`k` oracle is output-sensitive after bracket acquisition. The benchmark certificate includes three-run host medians; they are descriptive, not machine-independent complexity bounds. For complete S23 risk output R49's *389* age source inspections per endpoint remain fewer than R55's *515* successor updates per endpoint; R55 is useful as an independent label-preserving path and for cut-stream composition, not a claim of universal end-to-end speed superiority.

BRC carrier audit: the carrier here is finite labelled source identity `(z,r)`; the observer is youngest age per original historical interval plus the stage-specific risk functional. The event observer factors through the complete age vector on the declared finite frozen horizon; scalar coverage counts alone do not preserve this vector. Positive weighted BRC recurrence and native X6 residual dynamics are not invoked.

## Remaining work (R56)

Find a grouped source-age update representation that does not generate every cut or scan widely separated index spans, and prove an observer-safe compression lease for all subsequent stage-risk and future-query operations. Measure bit complexity in varied `m,H,J,q` regimes, including precision construction and integer serialization, and test whether the R54 cut stream offers a real end-to-end win once Farey state caching is enabled. Formal shared CLAIM/Result and independent review require their distinct current authorities.
