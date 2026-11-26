# EC49GAW — Minimum Hall threshold witnesses and certificate-oriented ordering

2026-11-26. Informed portable continuation of EC49GAV, frozen BRC16943. Historical provenance EM-DIRECT-23537B; current own private identity unconfirmed. No shared CLAIM or formal Result. This is a finite integer resource observer over the existing physical population; original target identities, branch masks and competition states remain intact. No new physical BRC dynamics claimed.

## Theorems

For a finite unit-credit target set T of size n, resource classes C with nonnegative integral capacities c_j and labeled eligibility neighborhoods E(t), write c(W)=sum of capacities on W, F(W)={t:E(t) subset W}, and H for maximum capacitated matching cardinality. Fix integer L and k=n-L>0. A threshold upper witness is A subset T with |A|-c(N(A))>=k, where N(A)=union E(t) over A. It proves H<=L because at most c(N(A)) members of A can be assigned and at most n-|A| others. A lower witness is a valid matching with L+1 or more distinct targets. For L>=n or L<0 the corresponding decision is trivial.

**Minimum-cardinality upper certificate theorem.** For k>0, if an upper certificate exists, its least target cardinality is

    m_k = k + min { c(W) : W subset C, |F(W)| >= c(W)+k }.

If this set is empty no upper certificate exists (equivalently H>L by capacitated Hall). Proof: any valid A has W=N(A), A subset F(W), so W is feasible and |A|>=c(W)+k>=m_k. Conversely select a minimizing W and any c(W)+k members of F(W); their union of neighborhoods is contained in W, hence their deficiency is at least k. The cardinality attains the bound. Zero-capacity classes do not change the proof. This is a minimum number of target identities, not minimum bit length of a certificate, nor a minimum physical decision tree. Count-only grouping is sufficient for the scalar minimization, while the original identity list is retained for witness reconstruction. The result applies to fixed unit-credit eligibility, not future changed goals or weights without recomputation.

A positive integer neighborhood histogram b(U)=#{t:E(t)=U} gives |F(W)|=sum_{U subset W} b(U); compute all these counts by subset zeta in O(m 2^m+n) integer operations, m=|C|, and all c(W) in O(2^m). Reconstruct a witness by a scan of original targets. This alternative is useful for small m, not a general polynomial algorithm in m. It reuses the existing BRC-style positive branch counting and class masks as the finite observer; no replacement of the actual labeled competition state by a histogram.

**Prefix witness theorem.** Reuse GAV prefix augmentations. When i-h_i>=k, let A be all processed target vertices reachable from all unmatched processed targets along alternating edges (target to eligible resource, resource to all its matched occupants). Every reachable positive-capacity resource is saturated, else an augmenting path exists. Every matched target in A is matched to a reached resource (a root is unmatched; the others were reached via their matched resource); all occupants of reached resources are in A. Every unmatched processed target belongs to A. Thus |A|-c(N(A))=i-h_i, including zero-capacity neighbors. For the first upper stop this equals k. A lower stop exports the current matching. Verify both certificates directly using original labels, neighborhood unions and capacities, without replaying augmentation. At each threshold, one or the other exists; H>L only says the Hall upper bound does not prune, not that physical cross-conflict exists.

Prefix witness need not be minimum in general: two classes capacities (1,3), target masks (2,1,2,1,2,2,2), L=5, n=7. Degree order returns targets [0,1,2,3,4,5], size 6, but [0,2,4,5,6] is size 5 and optimal (the first class alone has deficit 1, the second has deficit 2, both combined have deficit 3). This is a concrete executed counterexample to universal prefix minimality, while the actual frozen cases below exhibit exact minimality.

## Actual execution

Predecessor b3dc153fa18bf6ccc7b8ec5807e039172a35212e:research_notes/portable_direct/EC49GAV_THRESHOLD_HALL.md. Extracted GAV reproduction archive and checked its SHA256SUMS. Frozen ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0, gap_target.json SHA256 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5. Executed code 009998d5bf770f021f3b7d41591814e7f79fd875:research_artifacts/portable_direct/EC49GAW/witness_hall.py, SHA256 46a1520f4ef51ad812ab46deb77ccda21ab2cfc82a53ed45f71244a2934f943a, Git blob 29f9d48e7511c8223aa9476c28aeaf58bd266167 exact local/remote match.

Run python witness_hall.py > witness_hall.json in extracted GAV archive. Seed 49261129, 1000 arbitrary random graphs (1..7 classes, 0..11 targets, capacities 0..4). All integer L=-1..n, 7260 comparisons against exhaustive Hall cuts; upper minimality independently checked by enumerating every target subset. All decisions and returned witnesses correct.

Frozen 180 nodes, 360 budgets, 366 goals, each of three modes 87058 directed conflict checks, 14498 paired calls, 8680 paired prunes, 41334 allocation nodes and 358275 scalar misses; all graph adjacency and search counts agree with prior frozen GAP/GAQ/GAV evidence. All 43494 generated threshold witnesses checked directly (three modes x 14498). Full degree records retained with original options and threshold, including 8680 upper witnesses and 5818 lower witnesses. For degree mode, exact minimum computed by zeta on every upper witness: all 8680 already minimum. Upper witness size histogram: 1:3153; 2:4617; 3:215; 6:4; 10:507; 11:184. Total 20150 target identities, mean 2.32142857. 7770/8680 (89.52%) use <=2, 7985/8680 (91.99%) <=3. This is the empirical motivation for sparse certificate-first pruning. No inference that every input has these small witnesses.

Order comparison: degree 95919 augmentation attempts; capacity mass 96500; density floor(n*c(E)/frequency(E)) 94642. All 167894 input target records per mode and 8680/5818 upper/lower stops. Density saves 1277 attempts vs degree (1.33%) but one-run time including witness checks and sorting 2.104559536s vs mass 1.838719035s; degree 2.681823034s additionally includes exact minimum zeta computations and recording all witnesses. Thus no fair timing speedup claim for any order; retain degree by default. All modes slower than GAV Boolean-only reported 1.183s, not directly comparable across runs. Witness size totals equal across modes, exact minima explicitly checked only in degree mode.

Compact per-case evidence 46622cd32b0bbec9a46ad90ecc8fc3bf9d1c5019:research_artifacts/portable_direct/EC49GAW/witness_compact.zlib.b64, Git blob 778efdb0db3bd66062d6c24ec95840e0d230d157 exact local/remote match. Decode base64 then zlib; JSON SHA256 0d5b73ac5517a57a335587244b2a2e3b7326444ab9b76861cb84fff87896319a. Complete raw local files witness_hall.json SHA256 2b6ad2d568557dcba23c4821707fcca825d939a4ef28aa9e75961724d16ff0d9 and witness_records.json SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7; full raw witness records in local reproduction archive, reproducible from published code and frozen input, not copied verbatim into GitHub.

## Two fresh fourth-layer roots

Inherited fourth.json, gen.py, fourth_input.py and gak_solver.cpp, frozen status OPEN for IDs 1998 and 1999. Run python fourth_input.py 1998 2000 600000 > gaw_roots.in (SHA256 5cb384b40adadbe71a4421fc06f06671d9c37118ffd16c75bea8dbf2573d02f9). g++ -O3 -std=c++17 gak_solver.cpp -o gaw_solver. EM_DENSE=1 EM_FAST=1 EM_WORD=1 and EM_DENSE=1 EM_FAST=1 baseline.

Word raw CSV:
1998,1776,-1,88848,0,0,0,566,172,0,172,442,88494,76295
1999,1776,1,54648,0,0,0,951,235,0,235,682,54322,47079

Baseline raw CSV:
1998,1776,-1,128301,2651,0,0,4112,866,0,866,4068,0,0
1999,1776,1,92705,1821,0,0,7099,1311,0,1311,6520,0,0

Both configurations agree, 1776 labeled states replayed per YES, exhaustive NO below cap. Existing GAK, no GAW integration. From GAV evidence frontier: 1964 YES, 49 NO, 380 other, 2393 total (84.12% determined). If including GAR historically reported eight roots with incompletely preserved raw evidence: 1970 YES, 51 NO, 372 other. M14 remains 25<=M14<=27. GAR/GAS historical evidence recovery pending.

## Control and next

RS-EC49AS request r4-20261126-2127-ec49as-read-v1 terminal SUCCEEDED, Source 8eaa76b72b370162441ddc7914949a7971154976, NO_CANONICAL_PUBLICATION_DIRECTORY, native operational owner view not evaluated. No shared owner authority inferred, no new identity. Current research is independent portable, Activity association pending. Next: implement direct sparse witness detection for <=3 targets with labeled reconstruction; benchmark against degree-only GAV without paying minimum-zeta cost. Continue fresh IDs 2000 onward after checking evidence, and recover GAR/GAS missing original files without treating recomputation as original evidence.

AUTHOR_PROVED / EXACT_FINITE_MINIMUM_WITNESS_CHECK / EXACT_FINITE_FROZEN_CONFLICT_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
