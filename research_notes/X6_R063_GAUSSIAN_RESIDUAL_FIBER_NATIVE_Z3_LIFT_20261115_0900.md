# X6 / R063 — Gaussian residual-fiber lift to the signed native Z3 slice (2026-11-15 09:00)

**Scope:** RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2; original Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. Frozen mathematical input P000 V5 at 59538f585d037d09ef687b28715c4bc1a3f9fe03; historical pre-rebase comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3. This is author-side, exact, portable **new factorization-first constructive algorithm**. It neither changes P000 nor reruns/adopts the original R063 C3/C4 Stage 0 512-case benchmark.

## New factorization-to-native theorem

Fix a named signed native three-axis affine subtorsor with a genuine Cell anchor. For every nonnegative integer N define the signed integer pair fiber
[
R_2(M)={(a,b)inmathbb Z^2:a^2+b^2=M}.
]
Then the signed three-axis shell has an **exact disjoint residual decomposition**
[
R_3(N)=igsqcup_{c=-lfloorsqrt Nfloor}^{lfloorsqrt Nfloor}
 {(a,b,c):(a,b)in R_2(N-c^2)}.
]
Here c is an actual named signed third native coordinate, not an omitted or inferred zero. The positive shortest signed-axis word count at a native endpoint is
[
B_3(a,b,c)=
 {(|a|+|b|+|c|)!over |a|!,|b|!,|c|!}
 = { |a|+|b|choose |a|}{|a|+|b|+|c|choose |c|}.
]
Consequently the exact mass equals (sum_csum_{(a,b)in R_2(N-c^2)}B_3(a,b,c)), with explicit c and Gaussian factorization channel provenance. This is a constructive bridge from **general-norm Gaussian C4** to selected signed native three-axis path BRC; it does not assert that the original C3 square-only scaled lift already computes non-square residual fibers.

For M>0, factor M in ordinary integers. An odd exponent of any prime 3 mod 4 gives R2(M)=empty. For every 1 mod 4 prime p=x²+y² and exponent e, allocate between its conjugate Gaussian prime factors as (pi^jarpi^{e-j}) for j=0,...,e; p=2 contributes (1+i)^e; 3 mod 4 primes with even exponent contribute a scalar. Multiply and apply the four Gaussian units. Gaussian unique factorization proves completeness and absence of extra roots; deduplicate equal signed ordered pairs. For M=0 use {(0,0)}. Crucially, the factor search is at the Gaussian **prime** level, not a brute scan of the target equation a²+b²=M.

## New N=2500 residual-stratum certificate

A factorization-first discovery found representations for exactly **17 signed third-coordinate layers**, whose absolute c values are ({0,14,18,24,30,32,40,48,50}). All other 84 values c in [-50,50] have no Gaussian two-square residual representation. Here are the nonnegative layers; negative layers with c>0 contribute the same endpoint count and BRC mass.

| c | M=2500-c² | signed ordered R2(M) count | exact BRC mass in this layer |
|---:|---:|---:|---:|
| 0 | 2500 | 20 | 442782153097022856828 |
| 14 | 2304 | 4 | 116315937399900 |
| 18 | 2176 | 8 | 1173342555394017617096941468703688000 |
| 24 | 1924 | 16 | 4476799918376678797712568905545107907200 |
| 30 | 1600 | 12 | 4475626575821284780316862924308978247712 |
| 32 | 1476 | 8 | 4475626575821284780095471964076404219200 |
| 40 | 900 | 12 | 1173342555394017838487901701277716512 |
| 48 | 196 | 4 | 116315937399900 |
| 50 | 0 | 1 | 1 |

The layer count identity is 20 + 2(4+8+16+12+8+12+4+1)=**150**. Summing exactly across signed layers yields **26860799510260072787603759892561716013678** shortest native signed words, with support-size endpoint counts 6 / 48 / 96 for 1 / 2 / 3 used axes. This reproduces the previously independently counted shell without using its five absolute-coordinate orbits as the discovery algorithm; the new information is the **factorization-first constructive fiber partition** and exact third-coordinate source map.

## Executed certificate and strict verification order

An independent Python standard-library implementation actually executed locally, exited 0 and printed `PASS_X6_GAUSSIAN_RESIDUAL_FIBER_NATIVE_SIGNED_Z3_NOT_ORIGINAL_R063`. It first generated each R2(M) through Gaussian prime allocations, formed the signed R3 shell, and computed a SHA256 digest of sorted discovered integer triples **before** invoking a separate target-shell brute verifier. All N=25 and N=2500 endpoints matched exact independent verification, including N=25 count 30 / mass 846. Discovery snapshot hashes (the sorted integer-triple payloads encoded as compact JSON) were:

- N=25: `d75d61de42cdd9dd5503250239f0cb7e78f785cb25f300b616aafb774ff05d22`.
- N=2500: `9f95ba75af727e521f834d1ef7391e0a7237db473558ccef023e95a919685618`.

The **exact byte-identical published and independently executed checker** is `research_checks/X6_R063_GAUSSIAN_RESIDUAL_FIBER_BRIDGE_20261115_0900.py`, [immutable commit `910afac001bf9340097ea233e43ff7640486ccb4`](https://github.com/awdawmip/enterprise-math/blob/910afac001bf9340097ea233e43ff7640486ccb4/research_checks/X6_R063_GAUSSIAN_RESIDUAL_FIBER_BRIDGE_20261115_0900.py), Git blob `bd2ddd78a62333bc6a7981dd3dbff8dbb0dfa01a`, source SHA256 `c4883125f56dd2946c7cd80a5dde29fcfd4cc93627a928d75a2d62c467ff3f67`; byte-identical executable reran locally with exit 0 and stdout SHA256 `90269b4863226cb15ee0cc7b8b34afc103ce2e3b93d6f1b130d7942e59d43a0f`. Original historical Stage0 reader `scripts/r063_stage0_validate_path_valued_sqrt_2500.py` (blob b4e000a6377f2858ae434eb0eecd0c25c33e8592) and its five named part sources are untouched. The historical `gaussian_norm_root_set(M)` takes general M but the original `discover_from_scalar_root(N)` and C3 certify ordered positive pairs for square N; this new third-axis residual algorithm is **separate**.

## Precise remaining frontier

The factorization bridge demonstrates how one can construct the selected signed 3D shell without promoting the historical two-generator `PathSqrt_E(N)` certificate. It does **not** demonstrate an actual historical/current source call doing an invalid promotion, nor an LP019 positive-natural-mass signed cancellation, nor an LP011 native argmax miscall. Those provenance obligations remain open, as do the 28-LP consumer closure and independent Driver REQUEST_REVISION. The exact original R063 `--N 2500 --regression-max-r 512` benchmark in support #2416 is still **unexecuted in the required authorized runner**; this new factorization check cannot satisfy its 17 gates or 512-case acceptance. The 17:00 host-denied prose mutation remains unattempted.

**Evidence classification:** AUTHOR-PROVED mathematical theorem + independently executed exact finite computation; UNREVIEWED / NOT_ADMITTED / NOT_ORIGINAL_NATIVE_R063_REPLAY. Next exact action: inspect the source tree for an executable call that projects the original R063 C4 two-generator positive chart to signed native three-axis completeness; if no such call is located preserve UNRESOLVED_PROVENANCE. Separately obtain a real assigned authorized runner for issue #2416 and consume the original native job once.
