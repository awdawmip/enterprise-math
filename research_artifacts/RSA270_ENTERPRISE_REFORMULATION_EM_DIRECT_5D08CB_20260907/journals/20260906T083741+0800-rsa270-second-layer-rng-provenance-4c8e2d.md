# RSA-270 二层端点树与生成器/RNG 路线检查点

Progress-Event-ID: `rsa270-second-layer-rng-provenance-4c8e2d`
At: `2026-09-06T08:37:41+08:00`
Scope: `enterprise-math / RSA-270 factor-blind semiprime research`
Source: `ChatGPT project conversation / exact integer experiments / current Enterprise Math sources / public RSA Challenge and historical RSAREF sources`
Kind: `HANDOFF`

## Event

Parent objective remained factor-blind recovery of a nontrivial factor of RSA-270. No factor was found in this stage.

BRC reuse was applied with observer/provenance discipline. The earlier shell-only branch label `k` is not adequate once factor interpretation is required: for `k=ab`, the factor-bearing identity is

`(a*p+b*q)^2 - 4*a*b*p*q = (a*p-b*q)^2`.

Therefore the enriched branch identity must retain `(a,b,j)`, not merely `(k,j)`, because the same product `k` can encode distinct factor-ratio directions. The exact second-layer defect is

`d_(a,b,j) = (ceil(sqrt(4abN))+j)^2 - 4abN`.

A factor endpoint occurs only when this defect is an exact square. This is an application of existing BRC provenance rules, not a new top-level tool family. The current Prime Toolkit was also checked; its bounded/least-factor interfaces are explicitly not safe for large production factorization, so no claim of executing it against RSA-270 is made.

Conversation-local exact integer scans produced the following negative evidence:

- root layer `j=0`: all `k<=5,000,000` checked; no exact-square endpoint and no nontrivial gcd;
- previous low-shell identities `k in {20,47,52,62,18,10,1}`: each second-layer path checked through `j<=10^9` using necessary modular quadratic-residue filters followed by exact integer-square tests; no endpoint;
- path-resolved rational directions in the construction-family feasible band, including `(2,1)`, `(9,4)`, `(9,5)`, `(11,5)`, `(11,6)`, `(13,6)`, `(13,7)`, `(15,7)`, `(15,8)`, `(17,8)`, `(16,9)`, `(17,9)`, `(19,9)`, `(20,9)`, `(19,10)`, `(21,10)`, were each checked through `j<=10^9`; no endpoint;
- cheap classical probes (Pollard p-1 to low-million smoothness bounds and a small ECM probe) returned no factor.

The near-square minima seen during these scans were consistent with random extreme-value behavior at the candidate counts examined and are not promoted as signals.

A calibration against solved RSA Challenge moduli showed why deeper linear `j` scanning is not scalable: for solved RSA-170 through RSA-250, after optimizing over `k<=64`, true factor-bearing endpoint offsets have roughly 268--404 bits, while `j<=10^9` is only about 30 bits. Thus mechanically extending the present local scan by a few decimal orders cannot bridge the relevant scale.

Construction-family evidence materially changed the path prior. The original RSA Challenge specification documents that the decimal-list factors were random approximately equal-length primes chosen `2 mod 3`. A 2026 forensic study of the solved formal Challenge corpus reports all 44 recovered factors beginning in binary `11`; this is a family-level empirical signature, not proof about the still-unfactored RSA-270 target. Conditional on carrying that signature to RSA-270 (895-bit modulus), the factors would have bit lengths 447 and 448 and the factor ratio would lie approximately in

`1.7649891612 < q/p < 2.2663028692`.

Under that conditional model, the earlier visually strong `k=20` / `5:4` interpretation is outside the feasible factor-ratio band and is a false low-shell valley; the primitive `(a,b)=(2,1)` direction becomes the more relevant old branch. No `(2,1)` endpoint occurred through `j<=10^9`.

The newly public RSA-260 factorization (reported 2026-09-03) was independently multiplied and primality-checked in the conversation. Both factors are 431-bit, begin `11`, are `2 mod 3`, and have ratio about `1.14358`, continuing the solved-family construction pattern. As of this checkpoint, the factorization method has not been publicly disclosed in the sources checked.

A new higher-leverage historical-generator route was opened. Contemporary RSA Laboratories RSAREF source code (1991 lineage) exactly implements several observed Challenge-family features:

- key generation restricts each prime to `3*2^(b-2) <= p < 2^b`, forcing binary prefix `11`;
- candidate search proceeds in steps of 2;
- with public exponent `e=3`, the RSA filter enforces `gcd(p-1,3)=1`, hence prime factors are `2 mod 3`;
- `GeneratePrime` starts from bytes supplied by `R_GenerateBytes`, maps into the allowed interval, then scans upward;
- the RSAREF random generator has a 128-bit state and emits `MD5(state)` blocks while incrementing the state.

This mechanism is a striking exact construction-family match, but attribution is NOT established: no evidence found yet proves that the RSA DSP used to generate the Challenge decimal list reused RSAREF keygen or its PRNG, nor that one seed/state stream was shared across moduli. The 2026 forensic study likewise does not identify source code, seed, initial candidates, or retry histories.

Known-factor prime-gap analysis under the hypothetical RSAREF mechanism shows why sibling factors could be informative but not immediately decisive. For RSA-260, the previous-prime gaps of the two recovered factors are 330 and 540, leaving only hundreds of possible upward-search candidate offsets per factor. That could expose many candidate MD5-output blocks if the exact RSAREF generator were confirmed. However published cryptanalysis of the RSAREF `MD5(counter), counter++` generator does not give a practical output-only state recovery; timing/chosen-input/state-compromise attacks require capabilities unavailable for this historical generation event, and full-MD5 preimage recovery remains computationally prohibitive. Thus the RNG route is a conditional research frontier, not a break.

Status: `NO_FACTOR_FOUND / LOCAL_SQUARE-TREE_SCAN_SCALE-NOGO / RNG-PROVENANCE_ROUTE_OPEN`.

## Artifacts

- Prior durable shell-neighbor audit: `journal/enterprise-math/2026-09-05/20260905T211800+0800-rsa270-semiprime-tree-neighbor-audit-7f31c2.md`.
- Current Enterprise source reviewed: `research_artifacts/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY/experiment_summary_20260829.json` and `research_artifacts/BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY/result_summary.json`.
- Historical external source code reviewed: RSA Laboratories RSAREF `r_keygen.c`, `prime.c`, and `r_random.c` from a public preserved source tree.
- Exact large-integer scans and RSA-260 multiplication/primality checks were conversation-local; no source-repository artifact was created.

## Next

Highest-leverage continuation is to seek authenticated RSA DSP Challenge key-generation / seed / random-source implementation evidence. If RSAREF-compatible generator provenance is established, compile each solved sibling factor into a BRC candidate-offset / output-block / counter-trajectory constraint system and test cross-modulus state consistency before any state-recovery claim. If provenance cannot be established, do not continue linear `j` scanning; redirect to a valuation-preserving relation-collection route (GNFS/Hart/Lehman compatible) where BRC may rank or compress relations without discarding provenance. Also ingest the RSA-260 method immediately if Eric Lu publishes it, because that would dominate speculative local-shell continuation.
