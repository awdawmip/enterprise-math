# X6 / R063 — Gaussian residual-fiber lift to the signed native Z3 slice (2026-11-15 09:00)

**Scope:** RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2; original Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. Frozen mathematical input P000 V5 at 59538f585d037d09ef687b28715c4bc1a3f9fe03; historical pre-rebase comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3. This is author-side, exact, portable **new factorization-first constructive algorithm**. It neither changes P000 nor reruns/adopts the original R063 C3/C4 Stage 0 512-case benchmark.

## New factorization-to-native theorem

Fix a named signed native three-axis affine subtorsor with a genuine Cell anchor. For every nonnegative integer N, let

`R2(M) = {(a,b) ∈ ℤ² : a²+b²=M}`.

The native signed three-axis shell has the exact **disjoint** residual decomposition

`R3(N) = ⨆_{c=-⌊√N⌋}^{⌊√N⌋} {(a,b,c) : (a,b) ∈ R2(N-c²)}`.

Here c is the actual named signed third native coordinate; it is never an omitted coordinate or a coordinate assumed to be zero. The positive shortest signed-axis word count is

`B3(a,b,c) = (|a|+|b|+|c|)!/(|a|!·|b|!·|c|!) = C(|a|+|b|, |a|) · C(|a|+|b|+|c|, |c|)`.

Hence the exact BRC mass is the sum of `B3(a,b,c)` over all signed residual layers and their factorization-generated pair roots, preserving c, sign and provenance. This is a constructive bridge from **general-norm Gaussian C4** to selected signed native three-axis BRC; it does not imply that the old C3 square-only scaled lift computes nonsquare residuals.

For M>0, factor M in ordinary integers. An odd exponent of any prime congruent to 3 modulo 4 gives `R2(M)=∅`. For every prime p congruent to 1 modulo 4, fix Gaussian prime `π=x+iy` of norm p and exponent e, allocating `π^j · conjugate(π)^(e-j)` for j=0,...,e. The factor p=2 contributes `(1+i)^e`, and primes congruent to 3 modulo 4 with even exponent contribute scalar factors. Multiply all factors, apply the four Gaussian units, and deduplicate signed ordered pairs. Gaussian unique factorization establishes completeness; each returned pair has norm M. For M=0 use `R2(0)={(0,0)}`. Searching a representation of each **Gaussian prime** is not a brute scan of the target equation `a²+b²=M`.

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

## Necessary non-square residuals: a quantitative C3-to-C4 obstruction

Among the 17 signed third-coordinate layers, six have **non-square** residual norms: c = ±18, ±24, ±32. Their exact residuals are 2176, 1924, 1476, respectively. These six layers contain **64/150** signed native endpoints, with total shortest signed-word BRC mass **17907199673506715190850275622180431628800**. The other 86 endpoints occur at square residual norms. This classification was extracted from the actual factorization-first certificate and checked by exact `isqrt` comparisons against every returned layer.

For example the native triple `(18,24,40)` lies on `G=2500`, but its fixed-third-coordinate `c=18` gives `24²+40²=2176`, which is not any integer square `r²` for any integer `r`. The frozen R063 C3 scaled-square interface `discover_c3`r`` accepts integer radius `r` for a **square** target `r²`, whereas its `discover_c4(N)` and `gaussian_norm_root_set(M)` take general **positive** integer norm arguments. The zero residual `M=0` must instead use the separate exact singleton `R2(0)={(0,0)}`; the original C4 path calls `factor_integer(0)` and raises `ValueError`. Therefore simply ranging over c and invoking only square-input C3 leaves at least these 64 native endpoints ungenerated. Using the already-existing general-norm C4 Gaussian-factor construction at each residual `M=N-c²` is sufficient for completeness of this selected native `ℤ³` shell; path multiplication then proceeds through the explicitly typed binomial insertion factor. This is a certified **interface-domain obstruction**, not a claim that an old consumer actually made this mistaken promotion.

## Executed certificate and strict verification order

An independent Python standard-library implementation actually executed locally, exited 0 and printed `PASS_X6_GAUSSIAN_RESIDUAL_FIBER_NATIVE_SIGNED_Z3_NOT_ORIGINAL_R063`. It first generated each R2(M) through Gaussian prime allocations, formed the signed R3 shell, and computed a SHA256 digest of sorted discovered integer triples **before** invoking a separate target-shell brute verifier. All N=25 and N=2500 endpoints matched exact independent verification, including N=25 count 30 / mass 846. Discovery snapshot hashes (the sorted integer-triple payloads encoded as compact JSON) were:

- N=25: `d75d61de42cdd9dd5503250239f0cb7e78f785cb25f300b616aafb774ff05d22`.
- N=2500: `9f95ba75af727e521f834d1ef7391e0a7237db473558ccef023e95a919685618`.

The **exact byte-identical published and independently executed checker** is `research_checks/X6_R063_GAUSSIAN_RESIDUAL_FIBER_BRIDGE_20261115_0900.py`, [immutable commit `910afac001bf9340097ea233e43ff7640486ccb4`](https://github.com/awdawmip/enterprise-math/blob/910afac001bf9340097ea233e43ff7640486ccb4/research_checks/X6_R063_GAUSSIAN_RESIDUAL_FIBER_BRIDGE_20261115_0900.py), Git blob `bd2ddd78a62333bc6a7981dd3dbff8dbb0dfa01a`, source SHA256 `c4883125f56dd2946c7cd80a5dde29fcfd4cc93627a928d75a2d62c467ff3f67`; byte-identical executable reran locally with exit 0 and stdout SHA256 `90269b4863226cb15ee0cc7b8b34afc103ce2e3b93d6f1b130d7942e59d43a0f`. Original historical Stage0 reader `scripts/r063_stage0_validate_path_valued_sqrt_2500.py` (blob b4e000a6377f2858ae434eb0eecd0c25c33e8592) and its five named part sources are untouched. The historical `gaussian_norm_root_set(M)` takes general **positive integer** M but raises `ValueError` at M=0. This new third-axis residual algorithm uses a distinct zero guard at c=±sqrt(N) and the original C4 factorization for positive residual norms; the original `discover_from_scalar_root(N)` and C3 certify ordered nonnegative component pairs for positive square N.

## Precise remaining frontier

The factorization bridge demonstrates how one can construct the selected signed 3D shell without promoting the historical two-generator `PathSqrt_E(N)` certificate. It does **not** demonstrate an actual historical/current source call doing an invalid promotion, nor an LP019 positive-natural-mass signed cancellation, nor an LP011 native argmax miscall. Those provenance obligations remain open, as do the 28-LP consumer closure and independent Driver REQUEST_REVISION. The exact original R063 `--N 2500 --regression-max-r 512` benchmark in support #2416 is still **unexecuted in the required authorized runner**; this new factorization check cannot satisfy its 17 gates or 512-case acceptance. The 17:00 host-denied prose mutation remains unattempted.

**Evidence classification:** AUTHOR-PROVED mathematical theorem + independently executed exact finite computation; UNREVIEWED / NOT_ADMITTED / NOT_ORIGINAL_NATIVE_R063_REPLAY. Next exact action: inspect the source tree for an executable call that projects the original R063 C4 two-generator positive chart to signed native three-axis completeness; if no such call is located preserve UNRESOLVED_PROVENANCE. Separately obtain a real assigned authorized runner for issue #2416 and consume the original native job once.

## 2026-11-15 10:00 source-domain clarification

The exact unmodified R063 five-part source was re-read. `part00.inc` defines `factor_integer(n)` with domain `n>=1`, and `gaussian_norm_root_records(M)` calls it first; `part01.inc` routes `discover_c4` and `gaussian_norm_root_set` through that function. Therefore **original C4 does not accept M=0**. The zero fiber in this author's constructive algorithm is already correctly handled by its separate `two_squares_factorization(0)={(0,0)}` branch. For N=2500, this branch supplies c=±50, exactly two signed axial endpoints of total BRC mass 2. The complete original-source analysis and precise regression scope are saved as [X6_R063_C4_ZERO_RESIDUAL_NATIVE_AXIS_BOUNDARY_20261115_1000.md](X6_R063_C4_ZERO_RESIDUAL_NATIVE_AXIS_BOUNDARY_20261115_1000.md). Original frozen R063 sources and historical acceptance are unchanged.
