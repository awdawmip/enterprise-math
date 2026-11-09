# R29: independently regenerable exact certificate

Parameter enclosure is (262204504569236716045286 / 10^24, 262204504569236716045287 / 10^24), m=128. Each source's historical arc is preserved. This is the auxiliary circle model.

| q | p | j | c | H_min | K | K_neighbor | K_owner | positive events |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 14298 | 3749 | 25339 | 6644 | 164 | 9 | 9 | 252 | 1280 |
| 154021 | 40385 | 168319 | 44134 | 164 | 2 | 2 | 2291 | 384 |
| 6318118 | 1656639 | 10899111 | 2857796 | 164 | 5 | 5 | 171406 | 768 |

For each pair, [j-164,j) covers all m=128 historical arcs; [j-163,j) misses precisely phase-order arc rank 127, source 61; [j-128,j) misses 36 arcs. The 128 last-source labels are exactly [j-164,j-98] and [j-61,j-1], each listed integer included. To regenerate the entire 128-label mapping, run VERIFY_R29.py, which performs exact per-arc binary searches and asserts the complete set. It performs whole-window phase-order certification using two Euclidean floor sums, not q direct comparisons.

For each integer k in [0,K], the 128 source-index events lie at q+t+1+kq, with the two blocks n-(j+kq)=[q-163,q-97] and [q-60,q]. They have height min(|q theta-p|, |(c+kp)-(j+kq)theta|), choosing the sign so the latter is the positive opposite-neighbor error. Detailed formulas are in PROOF.md.

Original full-run artifacts retained as downloadable conversation files:
- local PROOF.md SHA-256 01477cbd481864bf31020b1eaa50e8138d51fa458a0a1068bd6a75e710b0e46c
- local VERIFY_R29.py SHA-256 c14f78ddb11b7657ad518dde0dc018fc4f2cdb474bebfc1dc9f1bd8c259c07eb
- local CERTIFICATE_R29.json SHA-256 9daa73b7142c559a56454db23312097b39b2a6e1907eca5a1348f8986b1176fe
- local RUN_EVIDENCE.txt SHA-256 2008eaea4b9d607eccb7650ff1553f23c0e18197a122b6a00f66b86f5d010342

These local hashes identify the extended local run. The GitHub verifier is a shorter, separately published executable reproducer, not claimed byte-identical to that extended local script. Native proof admission and independent review are pending.