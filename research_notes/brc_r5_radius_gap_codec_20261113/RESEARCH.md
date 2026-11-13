# R5 — Radius-local checkpoint gaps give a 56-byte lossless center cache

Date: 2026-11-13. Status: author mathematical proof and local exact verification; shared Task CLAIM, formal Result, and independent review not established.

## Immutable scientific source

The original frozen R5 auxiliary certificate-query input remains at scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`: 28 rational coordinates, 15 labeled operations, 1,065 certificates, 953 distinct activation thresholds, 954 complete-threshold boundaries, and a 2,520-byte original certificate seed. This result changes only the **optional derivative checkpoint-center cache**, not the pinned seed, original certificate identities, or activation semantics.

Exact predecessor: [R5 bounded-radius K-median DP](../brc_r5_bounded_dp_sidecar_20261113/RESEARCH.md), research commit `1c2a16314b189302cadde3ebc665d2218637c043`, file `research_notes/brc_r5_bounded_dp_sidecar_20261113/SIDECAR_BASE64.txt`. Predecessor full sidecar is 1,382 bytes, SHA-256 `94341ccf1aa09eb0eb42c045201b36dc9589008209fe77f446d8a4b93cee68b6`, containing K=213 uint16 boundary indices and a 954-byte nearest-center directory. This exact artifact, not a fabricated reconstruction, is the byte-level regression oracle.

## Theorem — bounded coverage implies bounded checkpoint-index gaps

Let `x_0 < ... < x_W` be **strictly increasing integer** cumulative event counts, and `S={s_0<...<s_{K-1}} subset {0,...,W}` be a collection of checkpoint boundary indices such that
`max_{0<=b<=W} min_{s in S} |x_b-x_s| <= R`, with integer R>=0.

Then:
1. `0 <= s_0 <= R` and `0 <= W-s_{K-1} <= R`;
2. every adjacent index gap `1 <= s_{j+1}-s_j <= 2R+1`.

**Proof.** Strictly increasing integer coordinates imply `x_b-x_a>=b-a` for `b>=a`. Boundary 0 has nearest checkpoint s_0, thus `s_0 <= x_{s_0}-x_0 <= R`; the last-boundary bound is symmetric. Suppose two consecutive checkpoints p<q have q-p>=2R+2. The boundary b=p+R+1 lies strictly between them. The event distance from b to p is >=R+1, and the distance from b to q is also >=R+1. All other checkpoints lie still farther in event-coordinate order, so b is uncovered. Contradiction. These are exact bounds, with no probabilistic premise. QED.

The strict-increment hypothesis holds for complete **distinct** activation walls: each wall group activates at least one certificate, so `x_{b+1}-x_b>=1`. Tied certificates contribute multiplicity inside an event group and do not invalidate the premise. The theorem does not require uniform wall gaps.

## Two lossless center encodings

Given K and R as parameters, store `s_0` in `ceil(log2(R+1))` bits, and each of the K-1 gaps in `ceil(log2(2R+1))` bits, encoding the integer gap minus one. For R=2, K=213 this requires `2+212*3=638` bits = **80 payload bytes**, plus a two-byte count = **82 bytes**. Every radius-2-covering center set in this declared domain fits.

The *actual immutable R5 checkpoint list* has `s_0=1`, `s_{212}=952`; its 212 gaps consist of 16 gaps of 3, 77 gaps of 4, and 119 gaps of 5. With this fixture-specific alphabet `{3,4,5}`, each gap occupies only two bits. `2+212*2=426` bits = **54 payload bytes**, plus the two-byte count = **56 bytes**. Its SHA-256 is `bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326`. The code explicitly checks the alphabet and original SHA; these are fixture-specific conditions, not universal lower bounds.

The previous 954-byte direct-address nearest-center directory is not independent information: for independently regenerated `x_b=E(b)`, let `y_j=x_{s_j}`. The exact tie-to-left directory is
`d(b)=# {j in {0,...,K-2}: 2*x_b > y_j+y_{j+1}}`.
It is rebuilt in **O(W+K)** by a monotone sweep, retaining the same bitmap selection and signed-event correction formula as the predecessor. Loading must recover E from the original pinned science, check that all centers cover at radius 2, and verify J=1070 when reattesting the predecessor's realized optimum. The compressed center bytes alone do not independently certify that DP's global-optimality proof.

## Exact tests executed locally

The Python-standard-library verifier `VERIFY_R5_GAP_CODEC.py`, executed 2026-11-13, read the exact **1,382-byte predecessor** from Base64, verified its published SHA-256, decoded every one of 213 centers, encoded/decoded both 82-byte general and 56-byte fixture formats, and reconstructed **all 426 original center-index bytes byte for byte**.

Independent finite tests enumerated all increasing event sequences of 2 through 7 boundaries with each increment in {1,2,3} and all nonempty center subsets: **110,880** cases; every computed monotone directory matched a brute-force tie-to-left nearest-center oracle (**754,317 entries**). Among these, **30,608** radius-2-covering cases also satisfied the universal gap lemma and encoded/decoded in the general format. Three malformed bitstream samples were rejected.

Local 21-round median microbenchmark (1000 decodes per round) was **0.030452 ms** per 56-byte decode and **0.031162 ms** per 82-byte decode. This measures only codec decode, not original scientific input reconstruction, directory generation, checkpoint bitmap construction, output serialization, process peak memory, or cross-platform latency.

The persisted *optional cache* shrinks from 1,382 to **56 bytes** (95.95% less); original seed plus optional cache becomes **2,576 bytes** rather than 3,902 bytes (33.98% less). Runtime-derived E, bitmap objects and other query indexes are separate memory costs.

## Files and recovery

- `VERIFY_R5_GAP_CODEC.py`: standard-library local test script, with its prior 1,382-byte predecessor regression fixture in `PREVIOUS_SIDECAR_BASE64.txt` when executed outside the stacked checkout.
- `R5_CENTERS_56B.hex`: byte-exact compact center payload; read as hexadecimal bytes.
- `EXACT_OUTPUT.json`: exact observed counts, SHA-256, restricted benchmark and scope.

Follow-on: run the 56-byte decoder and O(W+K) reconstructed directory against the original frozen corpus E on an independent checkout, measure seed-decode and full process RSS/queries, and compare at identical total memory. The existing parent Draft PR remains separate from mathematical admission, CLAIM and review.

