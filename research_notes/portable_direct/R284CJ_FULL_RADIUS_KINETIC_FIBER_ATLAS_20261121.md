# R284CJ — Exact kinetic atlas for all Port-fiber expansion radii

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED. Independent portable continuation of frozen R284CI; not a formal Task CLAIM, Result or independent review.

## Frozen input and observer scope

Preserve the 34-bit Port model, not a changed parameter search: `p=17179869143`, `D=(1120832,6,13,1651128)`, `Z=(0,390139,394465,1497639)`, and `C in {1,2}^{4 x 4}`. Let `F(C)=det(diag(D)-C-Z_1 E_01-Z_2 E_02-Z_3 E_03) mod p`. The 64 coarse fibers are determined by the six lower coordinates `(C_10,C_11,C_12,C_20,C_21,C_22)`, as in R284CD–CI. Each has a *shortest containing arc* `A_k=[a_k,a_k+w_k]` (positive circular orientation), computed via the R284CE determinant extrema, with `0<w_k<p/2`.

Immutable scientific source: [R284CI theorem](https://github.com/awdawmip/enterprise-math/blob/7e030dac04d573dbd8cb1b872141da074cb946f8/research_notes/portable_direct/R284CI_100BYTE_SHARP_PARAMETRIC_EVENT_20261121.md); frozen original event source [R284CH](https://github.com/awdawmip/enterprise-math/blob/f16d56afb972886b65d65bb5c0a48cec29bf32cc/research_notes/portable_direct/R284CH_PARAMETRIC_128_EVENT_PORT_INDEX_20261121.md). Original full codeword SHA256: `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. The present work changes only the *observer-query radius* and data structure, not the codewords or the proved unique-matrix correction radius.

Define the exact radius-`rho` coarse observer `Sigma_rho(y)={k:dist_circle(y,A_k)<=rho}` for any real circular `y` and `rho>=0`. This is a set-valued observer signature. The original full-matrix correction limit remains `rho<29.5`.

## Theorem 1: full-radius event compiler

For each fiber k and nonnegative real rho:

* If `w_k+2rho>=p`, the enlarged arc is the whole circle; k is always present in the signature.
* Otherwise it is the unique proper closed circular arc with ENTRY `E_k(rho)=a_k-rho mod p` and EXIT `X_k(rho)=a_k+w_k+rho mod p`.

At a fixed rho, sort at most 128 remaining ENTRY/EXIT endpoints, collect equal positions into one event, start with the exact mask immediately to the left of the zero cut, and sweep: ENTRY sets its fiber bit; EXIT clears it. For each open interval use the mask to its right; at a boundary use the **union of both adjacent open-interval masks**. For any real `y`, the resulting signature equals `Sigma_rho(y)`, including simultaneous crossing events, endpoints equal to zero and exact saturation. After at most 128 endpoint sorts, binary search finds an interval in at most eight comparisons; initial event compilation is `O(64+128 log 128)` comparisons and `O(128)` masks. This bound concerns a fixed rho and queries against its index. A new rho requires a fresh compilation or a separately maintained kinetic update.

*Proof.* Each non-full neighborhood is exactly the stated closed circular interval. Membership changes only at its two endpoints, and only by adding/removing its own bit. A full neighborhood contributes its bit everywhere. Between consecutive distinct endpoints membership is constant. The union of the two limiting cell masks gives the exact endpoint membership for closed arcs, even when an EXIT and a different ENTRY coincide. Treat the zero cut as a distinguished query boundary and the same argument applies there. Sweep induction proves the claim for all real observations.

## Theorem 2: complete kinetic collision/saturation census

Write `t=2rho`. For EXIT i and ENTRY j to collide, their relative angular velocity is two, and their unique possible collision in `0<=t<p` is

`t_ij=(a_j-(a_i+w_i mod p)) mod p`.

Both endpoints still exist at collision precisely when `0<t_ij<min(p-w_i,p-w_j)`. Pairing all 64 EXIT and 64 ENTRY boundaries gives 4096 ordered candidate pairs; exact integer enumeration under the frozen observer yields:

| Exact finite classification | Number |
|---|---:|
| Collisions strictly before both fibers saturate | **3,955** |
| Distinct collision values t | **3,955** |
| Individual fiber saturation events `t=p-w_k` | **64** |
| Distinct saturation values t | **64** |
| Equal values shared by collision and saturation | **0** |
| Distinct circular event-topology breakpoints | **4,019** |
| Simultaneous distinct EXIT/ENTRY collision pairs | **0** |

Thus, **up to cyclic rotation of the angular zero cut**, the event topology has 4,020 open parameter regimes separated by 4,019 isolated breakpoint radii. Each collision is a single adjacent EXIT/ENTRY swap at its meeting coordinate; each saturation deletes that fiber's two endpoints and permanently sets its bit. For a fixed *linear* order measured from coordinate zero, endpoint passage across the zero cut also rotates the list and is handled by the compiler; it is not counted among the 4,019 circular topology changes.

The first two collision values of `t` are 4,226,124 (EXIT45/ENTRY8) and 6,843,522 (EXIT40/ENTRY4). Consequently after the R284CI first crossing, a single adjacency swap suffices for `2,113,062<rho<3,421,761` before the second collision; equality requires the merged-boundary rule. The first saturation is `t=16,729,687,768`, the last is `t=16,872,276,929`. At and beyond the last, `Sigma_rho(y)` equals the all-64-fibers mask for every real y.

*Proof of completeness.* Like-directed boundaries move with identical velocity and never collide (the 128 zero-radius endpoints are distinct). Oppositely directed boundaries have the explicit modular collision equation above. Since `0<=t<p`, each EXIT/ENTRY ordered pair has exactly one candidate. Filtering by the two independent full-arc thresholds excludes all obsolete pairs. The exhaustive 64-by-64 integer comparison is therefore complete, not a radius sampling. Saturation thresholds are also exact. The companion checker enumerates all 4096 pairs, finds the 3955 strict survivors, proves their values pairwise distinct and disjoint from all 64 saturation thresholds, and reproduces the frozen codeword SHA. After the last threshold the first theorem gives the full mask directly.

## Corollary: 760-byte reversible compiled event table

For `t=2rho` an integer, use the doubled circular coordinate `2y mod 2p`. It lies in `[0,2p)`, with `2p=34,359,738,286<2^35`, so every endpoint occupies exactly five bytes. For `n<=128` surviving endpoints (even n), a tag records the six-bit fiber key and one ENTRY/EXIT bit; pack tags consecutively into `ceil(7n/8)` bytes. Store an eight-byte left-of-zero base mask. The result is

`8 + 5n + ceil(7n/8) <= 760 bytes.`

The byte length uniquely determines even `n` in `0..128`. The mask sweep reconstructs the complete prefix index and handles simultaneous events; no 20-bit small-cardinality mask rank is assumed at large radii. At zero radius the frozen table is exactly 760 bytes, versus R284CH's 976-byte precompiled table (22.13% fewer persistent bytes); a 100-byte R284CI coefficient payload is still smaller but requires arc/event compilation. For arbitrary non-half-integer real rho the theorem still holds using exact real comparisons or declared rational precision; five-byte endpoint serialization is specifically for integer t.

The compact format is a compiled artifact, not an intrinsic information-theoretic lower bound. The constant decoder program, its frozen parameters, and scratch/prefix-mask memory are not included in 760 bytes.

## Local reproducibility and checked scope

Companion files: `R284CJ_kinetic_fiber_atlas_checker.py` and `R284CJ_kinetic_fiber_atlas_certificate.json`. The local Python standard-library run passed:

- all 65,536 frozen codewords (exact SHA match);
- all 4,096 kinetic pairs, 3,955 distinct active collisions and 64 distinct saturations;
- 4,020 compact-table round-trips (zero radius plus each kinetic breakpoint);
- 139,670 selected exact direct-versus-index queries at all 4,019 breakpoint radii;
- 2,708 additional shifted boundary checks and 393,216 complete-codeword queries across six radii.

The finite certificate covers the explicitly enumerated pair/domain and the tested cases; correctness for all real y and rho is the endpoint/sweep proof, not a generalization from the sample queries. No actual CPU microbenchmark or independent mathematical review was executed.

## Residual typing and next research

The coarse signature preserves exact membership in 64 declared circular arc neighborhoods at the selected radius, not arbitrary future information from the complete matrix or X6 native state. An exact complete-state reconstruction claim requires an operation-specific injectivity/safe-quotient certificate. This is an auxiliary finite Port observer within Enterprise Math; no X6-native BRC arithmetic or spatial dynamics is inferred by relabeling it.

Next: measure amortized latency and working memory for the 100-byte compile, the original 976-byte precompiled event index, the 760-byte packed event format, and direct determinant/fiber queries. Then examine kinetic event swaps with a persistent index under changing rho, including zero-cut rotations, saturation and exact tie events.

Provenance: historical `EM-DIRECT-20B766` / `RA-617F40704F37299B15489DCA`; these are source attribution, not possession of a current session capability. The current live owner census is a read-only as-of observation; this portable note asserts no formal CLAIM and is not an Activity mutation.
