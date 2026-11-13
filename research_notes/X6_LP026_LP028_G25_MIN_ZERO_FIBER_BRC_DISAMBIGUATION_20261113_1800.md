# X6 LP026/LP028 — exact min-zero fibers and BRC disambiguation on the full native G=25 shell

Date: 2026-11-13, 18:00 Asia/Hong_Kong. Parent Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; original Research lane `chatgpt-research-onhour-enterprise-math-20260923`. Researcher provenance: `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`. **Status: AUTHOR-PROVED / EXACT FINITE CHECK PASS / UNREVIEWED / NOT_ADMITTED.**

## Scope and theorem

Use P000 V5's centered six-axis signed displacement lattice `Z^6`, frozen scientific foundation `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Let `D=(1,1,1,1,1,1)`, `G(z)=sum_i z_i^2`, `rho(z)=z-min_i(z_i)D` (relative min-zero observer), `T(z)=sum_i |z_i|`, and `B(z)=T(z)!/prod_i |z_i|!`, the **free unweighted ordered signed-native-unit shortest-path word count**.

On the complete finite signed native shell `S25={z in Z^6:G(z)=25}`:

1. There are exactly **7812** native endpoints and exactly **6372** different `rho` readouts.
2. **4932** relative observer fibers are singletons; exactly **1440** fibers have two distinct native endpoints. No shell fiber has three or more members.
3. Of the 1440 double fibers, **1080** have positive common-depth separation `k=1` and **360** have `k=3`.
4. For every two different native endpoints `z,w in S25` with `rho(z)=rho(w)`, their free signed shortest BRC counts differ: `B(z)!=B(w)`. Thus `z -> (rho(z), B(z))` is injective **on S25 only**. The `G=25` membership condition is essential; this is not a universal `Z^6` decoder and does not reconstruct an ordered path's history or provenance.
5. The aggregate BRC word count for endpoints in double fibers (counting both native endpoints once) is **952106400**; the singleton-fiber total is **1586848212**, summing to the previously certified **2538954612**.

A representative depth-3 fiber is
`(-4,-2,-2,-1,0,0)` and `(-1,1,1,2,3,3)`; a depth-1 fiber is
`(-4,-2,0,0,1,2)` and `(-3,-1,1,1,2,3)`.
Each pair has the same min-zero readout and norm square, with distinct native axes/sign patterns and distinct shortest-BRC multiplicities.

## Mathematical proof

If `z,w` have the same min-zero readout, then `w=z+kD` for a unique integer `k`; sorting the two endpoints componentwise permits `k>0`. The exact norm difference is
`G(z+kD)-G(z)=2k sum_i z_i+6k^2`.
For both endpoints on `S25`, `sum_i z_i=-3k`. Since `sum z_i = sum z_i^2 (mod 2)`, that sum is odd and `k` must be odd. Moreover the squared midpoint norm is `G(z+kD/2)=25-3k^2/2 >=0`; hence `k^2<=50/3` and the only positive integer possibilities are `k=1,3`.

The preceding run provided and exactly checked the exhaustive five absolute-value orbit types of `S25`: `(5)`, `(4,3)`, `(4,2,2,1)`, `(3,2,2,2,2)`, `(3,3,2,1,1,1)`. For a type `lambda` with `r` nonzero components and multiplicity `m_a` of each absolute magnitude, its **exact signed-coordinate-sum distribution** is the Laurent polynomial

`F_lambda(q)=6!/((6-r)! prod_a(m_a!)) * prod_{j=1}^r (q^(lambda_j)+q^(-lambda_j))`.

The coefficients at `q^(-3)` and `q^(-9)`, respectively, are:

| Absolute-value type | Sum=-3 | Sum=-9 | B per endpoint |
| --- | ---: | ---: | ---: |
| (5) | 0 | 0 | 1 |
| (4,3) | 0 | 0 | 35 |
| (4,2,2,1) | 360 | 180 | 3780 |
| (3,2,2,2,2) | 180 | 0 | 415800 |
| (3,3,2,1,1,1) | 540 | 180 | 554400 |
| **Total** | **1080** | **360** | |

Every endpoint `z` with `sum z_i=-3k` yields exactly one corresponding endpoint `z+kD` in `S25`. Conversely each collision has such a unique lower endpoint. The equation in common depth is quadratic with a positive leading coefficient, so three endpoints of the same fiber cannot share a fixed `G`. Therefore 1080+360=1440 double fibers, `7812-2*1440=4932` singletons, and `7812-1440=6372` observer fibers.

For complete assurance on BRC separation, applying the same signed-permutation orbit enumeration to the shifted endpoints gives this complete **ordered lower-orbit -> upper-orbit** collision table:

| k | Lower absolute orbit | Upper absolute orbit | Number of pairs |
| ---: | --- | --- | ---: |
| 1 | (4,2,2,1) | (3,3,2,1,1,1) | 360 |
| 1 | (3,3,2,1,1,1) | (4,2,2,1) | 360 |
| 1 | (3,3,2,1,1,1) | (3,2,2,2,2) | 180 |
| 1 | (3,2,2,2,2) | (3,3,2,1,1,1) | 180 |
| 3 | (4,2,2,1) | (3,3,2,1,1,1) | 180 |
| 3 | (3,3,2,1,1,1) | (4,2,2,1) | 180 |

Each row connects different orbit types with different `B` values. The table is an exhaustive finite signed-permutation enumeration backed by the exact checker; the previous generating-function argument independently establishes the total fiber counts. This proves BRC disambiguation under the stated finite scope.

## Executed certificate, provenance and dependencies

Executed locally using Python (exact integers; no floating point), **exit code 0**, output `PASS_EXACT_X6_G25_RELATIVE_FIBER_BRC`. Checker:
`research_checks/X6_G25_RELATIVE_FIBER_BRC_EXACT_20261113_1800.py`, immutable commit `8e1177fbff419f45a2c3c606c731e8a5e67768f5`, Git blob SHA-1 `c220807348dae35c021398fdbe33ec37fbc0d81d`; actual executed checker SHA256 `d329946079de51750491e408af0ea9440d29dfdaf399cd4fb54bda2889b0a9c8`. The checker compares direct `[-5,5]^6` enumeration with independent signed permutations of all five orbit types, tests the exact two-fiber and k/orbit tables, and asserts injectivity of `(rho,B)` on all **7812** endpoints.

Predecessor full-shell checker and note: `research_checks/X6_LP028_G25_FULL_SIGNED_NATIVE_SHELL_20261113_1700.py` at commit `e17622834fafcecbe3edd76e08423fc12d03c6a6`; `research_notes/X6_LP028_FULL_SIGNED_G25_SHELL_AND_FROZEN_EXECUTABLE_CALLER_BOUNDARY_20261113_1700.md` at `82bdbcd0e98a866ea102fb47895553e18c3863d4`. They are consumed, not recomputed as a replacement result. The historical comparison stays pinned at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

This is a scope-typed observer certificate: the relative quotient alone merges real native endpoints even at fixed `G`; one particular retained BRC multiplicity refines that observer to an injective map **for this finite shell**. It is not a justification for deleting joint relations, native step order, path provenance, arbitrary signed amplitude, or history in future operations.

## Research continuation and outstanding native work

Mother target: reconcile the **28** original historical LP claims and actual current consumers with P000 signed X6. Existing 35 distinct current-main executable audits, 24 frozen definitions, seven frozen executable reviews, prior type repairs and source matrices remain completed evidence. This mathematical unit supplies a precise, bounded candidate for LP026/LP028 interfaces whose consumers collapse `G=25` through min-zero. The next exact action is to identify a remaining actual native-shell consumer expecting unique native endpoint from relative `rho`, run its original test against the 1440 collision fibers and only patch a confirmed type error. LP011/LP019 specific historical bad-call provenance and independent Driver `REQUEST_REVISION` remain open.

Own session/claim/run (historical identifiers, not standalone proof of present authorization): `MCP-082892eb480e45dea6d4b9fcc0491034` / `MCP-bdd4acf9d96a8f1f0dfab4e9` / `RUN-756de85b94c23b46b181f7b8`. Source G25 PROGRESS request `onhour-20261113-1714-x6-native-g25-progress-v1` is conclusively `FAILED:SOURCE_MAIN_CAS_RETRY_LIMIT` (preserve original failed receipt, no blind replay). Current exact continuation request `onhour-20261113-1802-x6-exact-continuation` initially `QUEUED` and requires original-ID receipt/reconcile. The current authority and possible next authenticated checkpoint must be freshly determined before publication.

**Not independently reviewed, not admitted, not the original native benchmark, and no formal Task or parent completion asserted.**
