# BRC Square-Residue Static Tables — Build + Timing Check

Status: `STATIC TABLES BUILT / EXACT-INTEGRITY CHECKS / IMPLEMENTATION BENCHMARK / NO COMPLEXITY CLAIM`
Date: `2026-09-06`
Parent: `research_notes/BRC_MULTIPLIER_FACTOR_BRIDGE_20260906.md`

## 1. Built tables

Two production lookup tables are now checked into source as packed bitsets:

| modulus | quadratic-residue classes | raw packed payload | uniform pass fraction | SHA-256 |
|---:|---:|---:|---:|---|
| 4032 | 192 | 504 B | 1/21 = 4.7619% | `fde495a8ddeba79c9baa2646717d57a4ecbbee6212df51bbdd4b66a506e6a188` |
| 20160 | 576 | 2520 B | 1/35 = 2.8571% | `97c908db0d40f3f6109dc710d5427d80fb2cd656df7c36117c75b9867d168d94` |

Source: `src/enterprise_math/brc_square_gap_tables.py`.

The runtime facade `brc_square_gap_prefilter.py` uses the checked-in tables for those two moduli and keeps a deterministic cached generator only for arbitrary other positive moduli.

The bit-level membership law is unchanged:

`table[(gap mod M)//8] & (1 << ((gap mod M) mod 8)) != 0`.

Every integer square is accepted, so rejection remains zero-false-negative by construction. Passing remains only a necessary condition and must be followed by exact squarehood confirmation.

## 2. Integrity validation

The regression test rebuilds each table independently from all residues `x^2 mod M`, compares every byte with the checked-in payload, verifies the SHA-256 digest, verifies compatibility with the legacy integer bit mask, and repeats exact squarehood checks under both moduli.

Thus the checked-in table is not an opaque empirical artifact; it is a frozen serialization of the exact classical residue set.

## 3. Small structured sample: rejection is high but Python timing is worse

The Round-3 structured sample contains 1,015,300 semiprime×multiplier gaps, with 29,798 actual square gaps.

Static-table filtering reproduces exactly:

- `M=4032`: 64,294 survivors, 93.667% rejected;
- `M=20160`: 46,372 survivors, 95.433% rejected;
- zero false negatives.

However those gaps are small integers. On the current Python runtime, median timing over three passes was approximately:

- direct `isqrt` square test on every gap: `0.0691 s`;
- 4032 static table + survivor `isqrt`: `0.1023 s`;
- 20160 static table + survivor `isqrt`: `0.1020 s`.

So for this small-integer population the lookup overhead loses despite eliminating most second-root calls. This kills the naive statement `93% fewer isqrt calls -> 93% faster`.

## 4. Gap-only large-integer benchmark

A deterministic synthetic benchmark injected about 3% exact squares and otherwise used random integers of a fixed gap bit length. The table then becomes useful because `isqrt` cost grows while one small-modulus reduction remains cheap.

Selected median speedups in this runtime:

| gap bits | 4032 speedup | 20160 speedup |
|---:|---:|---:|
| 64 | 0.92x | 0.93x |
| 72 | 2.01x | 2.06x |
| 128 | 2.13x | 2.21x |
| 256 | 2.95x | 3.32x |
| 512 | 3.32x | 3.63x |
| 1024 | 4.31x | 4.33x |
| 2048 | 4.88x | 5.85x |
| 4096 | 6.16x | 7.29x |

The observed crossover between 64 and 72 bits is an implementation/runtime fact only, not a portable threshold theorem.

## 5. Full ceiling-gap pipeline benchmark

The factoring bridge must first compute

`x = ceil(sqrt(target))`

before it even knows

`gap = x^2 - target`.

Therefore the table saves only the *second* square-root test; it does not remove the first root computation. A separate end-to-end synthetic benchmark included that first `isqrt` and again injected about 3% exact square gaps.

Selected median whole-pipeline speedups:

| target bits | 4032 speedup | 20160 speedup |
|---:|---:|---:|
| 128 | 1.16x | 1.22x |
| 256 | 1.30x | 1.31x |
| 512 | 1.42x | 1.39x |
| 1024 | 1.28x | 1.30x |
| 2048 | 1.31x | 1.30x |
| 4096 | 1.25x | 1.23x |

This is the more relevant engineering result for the current multiplier-Fermat/BRC bridge: the table is a credible constant-factor optimization, not an order-of-magnitude algorithmic improvement.

For an RSA-sized target, the completion gap is roughly half the target bit length in the worst local basin-width sense, so the second-root filter can still be materially useful. But the first-root computation remains in the critical path unless a later BRC recurrence/transport rule avoids recomputing it per multiplier.

## 6. Decision

Keep both static tables:

- `4032` remains the compact default: 504 raw bytes and strong rejection;
- `20160` is the optional strong table: 2520 raw bytes and fewer survivors.

Do **not** claim speedup solely from rejection percentage. Runtime benefit depends on integer size and implementation. For small gaps, direct `isqrt` is faster in Python; for larger gaps, the static lookup saves time; for the full current factor-bridge pipeline, observed gains are around 1.2–1.4x in the tested big-integer range.

## 7. Next useful optimization target

The dominant unresolved cost is the repeated computation of `ceil(sqrt(mN))` across a multiplier scan. The next BRC-specific question is therefore not a larger residue table; it is whether the exact multiplier-basin `(root,remainder,phase)` transport can update adjacent or structured multipliers without a fresh full integer-root computation. A success there would compose with the static table and attack the actual end-to-end bottleneck.

Artifacts:

- `src/enterprise_math/brc_square_gap_tables.py`
- `src/enterprise_math/brc_square_gap_prefilter.py`
- `tests/test_brc_square_gap_prefilter.py`
- `experiments/brc_square_residue_static_table_benchmark.py`
- `research_artifacts/brc_square_residue_static_table_benchmark_20260906.csv`
