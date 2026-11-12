# R5 — exact event-count quotient and single-coordinate compact checkpoint directory

Date: 2026-11-13 (Asia/Shanghai). Author-side result for the frozen R5 auxiliary model. Predecessor: Draft PR #2203, commit `65e8ecf2bdbb6ee1fb8c68a8e7d914b04d44d255`; science remains frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`. No formal CLAIM, Result or independent scientific review is asserted.

## Theorem: complete-wall event-count factorization

Let the M terminal certificates occupy the terminal-preorder positions 0,...,M-1. Their distinct ordered rational activation walls are w_0<...<w_{W-1}. Let e_i be the wall code of certificate i and let pi be any permutation of terminal positions ordered by nondecreasing (e_i,i). Define E(b)=# {i:e_i<b}, for 0<=b<=W, and A_b=sum_{i:e_i<b}2^i. Then

  A_b = sum_{j=0}^{E(b)-1} 2^{pi(j)}.

Proof: by definition the first E(b) elements of the sorted order are exactly the certificates with wall codes <b; their terminal positions are distinct. The representation is independent of the original wall boundary b once the cumulative event position x=E(b) is known. Empty wall groups produce repeated values E(b), with identical bitmaps, and can be quotient-collapsed. Tied certificates are not merged: they contribute distinct set bits and their entire wall group is inserted or removed together at complete-wall boundaries.

For any checkpoint s at a *complete-wall boundary*, store only x_s=E(s) and bitmap A_s. At a query wall rank b, let x=E(b), select any checkpoint and correct its bitmap using sorted event indices j in [min(x,x_s),max(x,x_s)): set bits if x>x_s, clear bits if x<x_s. The corrected bitmap is exactly A_b, hence for any prefix node v with terminal interval [L_v,H_v),

  C_v(r) = popcount((A_b >> L_v) & (2^(H_v-L_v)-1)),
  b = upper_bound(w,r).

This is exact for all finite ordered certificate trees, rational comparisons, repeated walls, arbitrary prefix nodes and arbitrary query order. Event-count checkpoint coordinates are sufficient for this declared activation-count observer and query horizon; this theorem is not a universal quotient for provenance-sensitive operations.

If M<=65535, each x_s fits in an unsigned 16-bit array element. In this specific frozen corpus M=1065, so 213 optimized checkpoints need only 426 raw bytes of coordinate payload, or 522 bytes for the observed Python `array('H')` object. There is **no need** to store the checkpoint wall rank, a second integer coordinate list or an inverse-wall directory. The logically minimal fixed-width coordinate is 11 bits here (213*11 bits = 293 bytes after rounding), but the implementation uses native uint16 for direct indexing.

## Provenance and exact original fixture evidence

The previous minimax construction gives K=239, radius R*=2 and 213 complete-wall checkpoint centers on the same E(b). The new implementation was run in local CPython 3.13.5 against the independently reconstructed frozen 28-coordinate, 15-operation rational fixture, with 1065 valid ordered certificates, 2880 prefix nodes and 953 distinct rational walls. Its baseline and compact bitmap masks were checked identical in order. All 954 complete-wall boundaries x all 2880 prefix nodes (2,747,520 counts) agreed with a separate exact terminal-code prefix-sum oracle; 57,600 original Fraction/Wavelet checks also passed.

Measured Python object space on this interpreter (bytes; only the stated mask/list/array objects, not a full heap or RSS measurement):

| Index variant | Masks | Checkpoint directory | Sum |
| --- | ---: | ---: | ---: |
| Weighted, old Python list bounds+coords | 33,108 | 15,608 | 48,716 |
| Weighted, event-count uint16 array | 33,108 | 522 | **33,630** |
| Uniform B=4 nearest, masks only | 37,516 | 0 (stride arithmetic) | 37,516 |

The event-count quotient reduces the weighted directory's measured object footprint by 15,086 bytes (96.66%), and the weighted compact masks+directory use 3,886 fewer counted bytes than uniform B=4 masks alone. These measurements count exactly their stated components; all variants share frozen walls, event order, prefix intervals and fixture-generation inputs. A separate event-order `uint16` payload would occupy 2130 raw bytes, shared by these event-correction variants.

Seven-run local median query timings in milliseconds (including rational-wall bisect and count, excluding construction/RSS/output serialization):

| Load | Uniform nearest B=4 | Old weighted lists | Compact weighted uint16 |
| --- | ---: | ---: | ---: |
| Root (256) | 0.968 | 0.938 | 1.000 |
| Broad (512) | 1.869 | 1.923 | 1.912 |
| Random (2048) | 7.494 | 7.389 | 7.486 |
| Hotspot (2048) | 7.582 | 7.546 | 7.712 |

The compact representation produces a clear **index-object memory improvement**, without an observed query-speed gain on these local workloads. Corpus rebuild took 1.443 seconds in the same run; this is not a seed-only initialization benchmark. The serialized seed remains 2520 bytes, and no new external-model or P000 claim is made.

## Verification and next problem

Local full executable: `/mnt/data/em_r5_compact_event_directory_20261113/VERIFY_R5_COMPACT_DIRECTORY.py`; local exact output: `EXACT_OUTPUT.json` in the same local folder. This GitHub branch also contains a portable verifier using the stacked original-fixture ancestry, to be executed independently from its actual committed bytes. Pending: reproducible clean checkout execution; separately measure seed-only decode, index allocation/RSS, wall/order construction, output serialization, equal-total-memory workloads and possible event-order compression. Formal R5 task owner/CLAIM, Source Activity, Result and independent review follow the current native control contract, not this author-side file.