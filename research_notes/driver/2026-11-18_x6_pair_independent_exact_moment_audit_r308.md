# Driver r308 — Independent exact-moment audit of the X6 circulation pair (N = 2)

Date: 2026-11-18. Audit type: source-exposed mathematical review plus independent integer-enumeration cross-check. Contributor: EM-DVR-DEBB5E. Original mathematical author and immutable evidence remain assigned to the source holder; this is **not** a blind review, a frozen Native Result disposition or a Task/parent completion.

## Exact source reviewed

`awdawmip/enterprise-math@fb7797c2990782f5f0dec026e7010df63f9ff060:research_artifacts/mcp/RS-X6-CIRCULATION-PAIR-INDEPENDENCE/MCP-456b8f22a648400585024ffbcc1c2c94/ac1ddcab176e8af53f14/X6_PAIR_INDEPENDENCE_EXACT_CRITERION_20261118.md` (Git blob `c591549c9e3a63ba2f3901339d8e88e401f4d1a8`). Original source defines two six-axis circulation readouts supported respectively on native-axis triples `123` and `345`. A sixth native axis is retained in the full labeled path; deleting it for a readout-only finite count preserves the uniformly distributed relative order of the five used types. Source's N=2 finite claim was checked without reusing its recursive counting algorithm.

## Independent integer certificate

At stock `N=2`, each of the five used axis labels `0,...,4` appears exactly twice. A uniform labeled shortest path projects to one of the
```text
  10!/(2!)^5 = 113400
```
distinct five-label words, all equally likely. Enumerate them by choosing disjoint 2-element sets of positions `P_0,...,P_4` partitioning the ten positions. For each ordered pair `(i,j)`, let `N_ij` count occurrences of `i` preceding `j`. Put
```text
  a = (N_01+N_12+N_20)-6,
  b = (N_23+N_34+N_42)-6.
  X_2 = a/2, Y_2 = b/2.
```
Direct counting of those position-set partitions gives the following full **integer joint-count table**, with row `a` and column `b` each ordered `-2,-1,0,1,2`:

| a / b | -2 | -1 | 0 | 1 | 2 |
|---|---:|---:|---:|---:|---:|
| -2 | 710 | 1660 | 2820 | 1660 | 710 |
| -1 | 1660 | 6230 | 10680 | 6230 | 1660 |
| 0 | 2820 | 10680 | 18360 | 10680 | 2820 |
| 1 | 1660 | 6230 | 10680 | 6230 | 1660 |
| 2 | 710 | 1660 | 2820 | 1660 | 710 |

The cells sum to `113400`. In integers the first and second joint moment sums are
```text
 sum a = sum b = sum ab = 0,
 sum a^2 = sum b^2 = 113400,
 sum a^2 b^2 = 123480.
```
Consequently, using the exact normalization `X_2=a/2, Y_2=b/2`,
```text
 E(X_2) = E(Y_2) = E(X_2 Y_2) = 0,
 E(X_2^2) = E(Y_2^2) = 1/4,
 E(X_2^2 Y_2^2) = 123480/(113400*16) = 49/720,
 Cov(X_2^2,Y_2^2) = 49/720 - 1/16 = 1/180 > 0.
```
This validates the source's `N=2` dependence assertion with a separately specified enumeration and a complete joint-count certificate, rather than only spot checking four moments.

## Analytic-scope review

The source's all-`N` formula
```text
 Cov(X_N^2,Y_N^2) = (N-1)/(90N)
```
comes from conditional independence given the shared third-axis keys, the conditional second-moment kernel `(1/2)B_2({u-v})`, and the centered pair-kernel identity `int_0^1 B_2(t)^2 dt=1/180`. Its `N=1` boundary gives zero, matching the symmetry of single three-cycles conditional on their common axis key. The full-`N` proof is source-authored; the independent enumeration here covers exactly `N=2`.

For the Gaussian bilinear limit `U=G^T A J`, `V=G^T B J`, the stated mixed fourth cumulant can be independently reconstructed by conditioning on `J` and applying the quadratic-form Wick identity:
```text
 cum(U,U,V,V)
   = 2 tr(A^T A B^T B)
       + 4 ||sym(A^T B)||_F^2.
```
When `A,B` are real skew matrices this equals `2||AB||_F^2+||AB+BA||_F^2`. After multiplication by `sum_{m>=1}(2 pi m)^(-4)=1/1440`, a vanishing mixed cumulant forces `AB=0`. Conversely, `AB=0` implies `BA=0` for skew matrices and yields disjoint Gaussian coordinate subspaces, so the two limiting bilinear series are independent. This checks the *logical criterion* `independent iff AB=0` under the pinned Gaussian-series representation and its stated L4 convergence; independent verification of the convergence from the upstream source is outside this audit.

## Governance and provenance boundary

The original X6pair source is preserved and accurately attributed. The formal freeze request `backlog-driver-20261118-0841-x6pair-freeze-original-source-v1` was read back as `FAILED / CANONICAL_REJECTED` on 2026-11-18; its diagnostic is a native `research_result_records.py freeze` command-usage error. The original owner must reconcile and repair the affected freeze invocation under its **own** run/generation; this review does not replay it, invent a frozen RR, or claim another owner's contribution.

Independent Source-result review still requires a genuine immutable Result, its exact bytes, an active Driver DA and native contribution-independence checks. Retain the full signed axis/path provenance, not a collapsed marginal observation, when evaluating any future X6/Cell/Link/Port application.
