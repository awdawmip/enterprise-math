# R42 exact verification evidence

Date: 2026-11-10. Freeze: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Author-side finite exact test, independent mathematical review pending.

Reproduction: download this folder and run with Python 3 standard library:
python VERIFY_R42.py
This regenerates full CERTIFICATE_R42.json and BENCHMARK_R42.json in the current directory. REFERENCE_R41.py is the byte-identical predecessor source fetched from Enterprise Math R41 immutable commit ffcb92863514817ee99cb9a59875b454421b76e1 (original blob 300b2e29d717015093ffbe5897626d000b39fea3).

Expected terminal marker: PASS_R42_CERTIFIED_RECURRENCE_8_FAMILIES_AND_COARSE_REJECTION.

| instance | m | J | N | suffix probes | certified labels covered by suffix | fallback owners | fallback exact scalar floors | independent Euclidean count queries | SHA256 of labelled source JSON |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| frozen S23 | 128 | 1000000000128 | 1000000000 | 164 | 128 | 0 | 0 | 3960 | 5b97af4166df200fa720773b542d2e3c84164a89d567c60fc5543ed4d1f71ae7 |
| sqrt2−1 | 16 | 1000000000 | 100000000 | 17 | 16 | 0 | 0 | 443 | cec34b73958b739a18dcf94ca0a64646c124eb82b86594f78d2cfb58698b2034 |
| sqrt2−1 | 257 | 1000000000 | 100000000 | 392 | 257 | 0 | 0 | 7109 | 77fc21c79c5fdcc0bfa89986ab6dccfff3e3fdb6caf998988cc9eee1617a78c2 |
| near 1/3 | 21 | 1000000000 | 100000000 | 84 | 3 | 18 | 2402 | 581 | 5d5a8b8230cd4e9c9e34c1d5308173dae2e6e98ed696a0414a1df4bd2b1ba66e |
| mixed near 1/3 | 257 | 1000000000 | 100000000 | 869 | 257 | 0 | 0 | 7109 | 30e859da5c45a8dedb79e710899cac42dff7b201ebd823c4fc95577621ab8408 |
| short | 16 | 320 | 120 | 17 | 16 | 0 | 0 | 127 | 33693746c67c8d8b553b2ba7dfa38fb2fb1e134e3854ec6f6dda69061c8adbae |
| historical coincidence | 16 | 16 | 16 | 16 | 16 | 0 | 0 | 80 | 21ad2815c65317c6d19f27343914b2ceb38b8fc624b470baaf4e9c956260d4f5 |
| negative source indices | 16 | -30 | 80 | 28 | 16 | 0 | 0 | 120 | ecbd18f8573104dcdc14cf3ddb27ad45d413bb306e9ea01e11b91d4ca849dd9c |

For each instance, the code compared **every** last-source label against R41 and a separate exact Euclidean Floor Sum rank/select implementation. For short/historical/negative windows it also compared with direct finite reconstruction. One coarse enclosure [2/5,21/50] was rejected for insufficient certification. The S23 full labelled vector has the exact last-source age set {1,...,106} union {143,...,164} from the frozen predecessor.

Under frozen S23: 1 large source-stream initial product/remainder, 163 integer modular updates, 328 integer boundary margin checks, 128 historical precomputation products, 0 source-stream Fraction multiplications, 0 R40 fallback floors.

Three-run Python local elapsed-time medians, R42/R41, in milliseconds: frozen S23 0.213 / 163.753; sqrt2 m16 0.030 / 3.137; sqrt2 m257 0.409 / 903.922; near-third m21 1.287 / 24.279; mixed m257 0.696 / 1944.350; short m16 0.035 / 3.550. These are environment-specific Python implementation comparisons; see PROOF.md for the abstract bit-cost domain.

Local deterministic certificate SHA256 (full regenerated 8-case JSON): dcbb2a778a47a7e57c01a1f600caf9146d36d3081cc08e0b242ca0b6ca184b68. Local executable VERIFY_R42.py SHA256: 7308d54fde6281fa551b2a3ffe868a14ce9a87eb3d7ac15cbd951c36200da23c.

Checkpoint: source-owner subroutine R42 verified on declared cases; direct end-to-end 298-run compiler replay using R42 is the next unit.
