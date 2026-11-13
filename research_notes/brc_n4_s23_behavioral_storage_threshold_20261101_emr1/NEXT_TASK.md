# Next discriminating research unit

The new author-side theorem: in the fixed six-latent-cell BRC N4 S23 stopping-time observer, every policy-independent common source encoder with k<=5 has worst-case error at least 1/47, **even with unlimited information about the policy at decoding**. Six lawful deterministic time-three indicator policies witness the obstruction. With the earlier author-side k>=6 eleven-control quantization upper bound (PR #1762), exactly six common source states are necessary and sufficient for vanishing error as policy-label capacity grows. This is UNREVIEWED / NOT_ADMITTED, and the witness model is not an X6 dynamics theorem.

Immediate mathematical questions:

1. Sharpen the universal 1/47 lower bound for k=4 and k=5 by exploiting row-stochasticity and nonnegativity of the encoder, rather than only its linear rank; seek an exact optimal value for full-policy-visible reconstruction or a stronger dual certificate. Is 1/47 attainable?
2. Keep the original finite ten-label S23 behavioral minimax target R_(4,10) and R_(6,10) open in [1/2,2/3]. The new 1/47 floor does not tighten that interval, although it rules out vanishing k=4 error as m grows.
3. Independently audit whether each of six third-stage indicator policies is allowed by the original S23 information set and P/Q law-independence. S2 needs a separate causal embedding proof.
4. For any native P000 transfer, construct explicit six-axis Cell/time source embedding and show that joint relations and all declared future-operation observers are preserved. Six statistical latent sources cannot be identified with the six native spatial axes without such a bridge.

Reproduction: python3 VERIFY.py; expected marker PASS_BRC_N4_S23_BEH_STORAGE_K_LT6_OBSTRUCTION_20261101. Checks use exact rational arithmetic and finite enumeration; the continuum encoder conclusion is proved by rank-nullspace duality in PROOF.md. Scientific source pins and actual native access limits are in SOURCES.md.
