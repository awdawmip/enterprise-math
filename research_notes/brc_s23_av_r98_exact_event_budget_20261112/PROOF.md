# R98 — Exact persistent-profile event bound and held-out cost audit

Date: 2026-11-12. Status: author-side proof and exact computation, pending independent review.
Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R97 commit `1c1caef2edf80c0df2034b57d7abe65c9860cfda`. Scope: auxiliary exact rational circular-source model, time/branch identities, fixed observer, and rational interval; not a native X6 transfer. P000 unchanged.

## Theorem R98.1 (certified constructor-event bound)

Let E be a finite set of M distinct source identities `(t,branch)` and I a closed rational interval. Define K using R97's exact crossing envelope: 2 plus the sum, over distinct source times and six affine forms `a*z, b*z, (a-b)*z, x+(t-j)*z, x+(t-j-a)*z, x+(t-j-b)*z`, of the number of integer levels crossed on I by nonzero-slope forms. Construct an R86 persistent AVL winner profile by inserting all identities in sorted order. Let C be allocated `make()` nodes and A the sum recorded by `counts['merged_atoms']`. Then

```
C <= 3*M*(M+1)
A <= 3*M*(M+1)*(2*K-1).
```

For E empty, C=A=0. Branch identities sharing a time remain distinct.

**Proof.** At insertion i, the AVL tree has at most i−1 existing time nodes, so `put` traverses at most i levels including a newly allocated leaf. On any level, it calls `make` once; a double rotation adds at most one extra `make` to reassemble the parent and two `make` calls each for inner and outer rotations. Thus at most 6 node allocations per level and 6i on insertion i. Summing i=1,...,M gives C <= 3M(M+1).

At a fixed time, R97 proves that every membership breakpoint is among the R97 six affine crossing families plus endpoints. R86 `tagged` uses exactly those cuts, and `overlay` takes unions of existing cuts, never introducing new cuts. Every intermediate winner profile therefore has at most K point atoms and K−1 open-gap atoms. Each newly allocated node runs at most one counted `overlay`, which contributes at most 2K−1 atoms. Hence A <= C(2K−1). QED.

This is an exact event-count bound on the specified R86 implementation; it gives two certified structural cost coordinates. CPU nanoseconds, Fraction bit operations, critical-cut enumeration, sorting, and retained graph memory are separate dimensions.

## Held-out experiment R98.2

From the unchanged R96 deterministic source-history stream, deduplicate 17 immutable (source-set, observer-signature) keys. Evaluate broad `[-1/4,3/5]`, medium `[0,1/12]`, and narrow `[1/16-1/1200,1/16+1/1200]` rational intervals. The split holds all three intervals for a key together: sorted-key index divisible by four is held out. Thus 36 profiles train, 15 profiles are held out, and 3 predeclared additional single-source-time stress profiles (100, 1000, 10000) have no train-key overlap.

Two cheap prebuild features are `F_count=M(K+1)(1+ceil(log2(M+1)))` and `F_bits=F_count*(1+max_affine_endpoint_bit_length)`. Calibrate each empirical nanosecond ceiling on training only: `ceil(F * max_training(build_ns/F))`. Audit both on held-out profiles. **These fitted price ceilings are not certified mathematical runtime bounds.** The count-only ceiling missed 1/15 heldout profiles and the bit-weighted ceiling missed 2/15 on the recorded execution. Both covered all 3 stress profiles.

The program independently verifies each exact R86 full winner profile at every source-time cut and every gap midpoint against `r90.member`, plus 3 exact subinterval classifications per profile against `r90.reference`. Every CHANGES result has two exact rational witnesses checked against the full identity set. It records source and certificate-respecting events, constructor counts, exact K, peak rational operand size, graph accounting proxy, full-domain first-query and same-interval repetition times.

**Verified run**: 54 full-profile constructions; 162 exact reference classifications; 79 changed-query intervals, all witnessed. Medians over 17 keys/domain:

| Domain | Build (ms) | Profile points | Merged atoms | Graph byte proxy |
|---|---:|---:|---:|---:|
| Broad | 123.300 | 581 | 8975 | 83000 |
| Medium | 9.791 | 54 | 844 | 9320 |
| Narrow | 0.879 | 2 | 51 | 2432 |

The one-process `perf_counter_ns` readings and fitted multipliers vary across executions. Count and equivalence assertions use exact rational arithmetic. The full original output and source are in the accompanying gzip/base64 UTF-8 files.

## Next frontier

R99 should create an exact weighted-operation model for endpoint rational arithmetic, cuts generation, sorting, AVL overlay, branch retention, history graph memory, and CHANGES witness recovery. With proven per-operation charges, R98's structural ceilings can contribute to a certified P upper bound for the R97 uncertainty theorem, while CPU forecasts remain heuristic until certified for an execution model.

Decode `check_r98.py.gz.b64` using `base64 -d | gzip -d`; run beside the unchanged R97 bundle dependencies `check_r82.py`, `check_r86.py`, `check_r90.py`, ..., `check_r97.py`. Run `python check_r98.py`; deterministic output signature is `R98_PASS 54 162 79`, and a fresh JSON of exact checks and current timings is generated. The original `verification_r98.json.gz.b64` contains the complete recorded validation payload.
