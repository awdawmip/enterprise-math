# R685 — Native time and hidden complete-frame memory (2026-11-10)

Task: RS-X6-NATIVE-TIME-DYNAMICS; publication TP2-91D4A7C2F63805BE21A3. Frozen R462 science pin: 18783e01e3646c72b7aab3b16d3f565e83e6446f. Source model: R684@ddd775c737dc2f1e11b2992356981d59ff74becd; earlier repeat-PASS kernel R683@1ca5b1c159efff92e6a72edc5822852d6d28453f.

Complete proof: R685_PROOF.zh-CN.md; runnable Python script: R685_VERIFY.py; exact certificate: R685_EVIDENCE.json. Run python3 R685_VERIFY.py. Expected final line R685_HIDDEN_FRAME_FIBRE_T227_EXACT_PASS. Integer/Fraction 120 canonical starts (six R679 biases x 20 triads), 0..256 event steps. Initial u=(-2,-4,-3,10), S=F=035 yields first branch t=212, first same-field-different-frame collision t=227. At t=227: (u,M01,M12,M20,S)=((4,4,-17,10),75,83,69,025), frame=250 with weight 1/4, frame=025 with weight 1/2. Remaining 1/4 at ((3,3,-15,10),75,82,70,034,304). All 119 other starts show no collision through t256.

Theorem: V17 single-step frame transport is bijective, so two unequal complete frames remain unequal along any common future triad sequence. The R684 (u,M,S) Markov quotient remains exact for observers that do not read F; for the complete-frame observer a frame fibre is required. Event time and any purely t-derived periodic clock cannot reconstruct F on the t227 witness.

BRC interface: positive rational labeled branches and exact observer quotients; retained information is full ordered-frame residual. Reuse status COMPOSE_APPLIED. Native X6/port/Cell/Link coupling and actual V39 j are distinct future questions.

This is an author-side research deliverable. No CLAIM, formal Result, Driver acceptance, or canonical Foundation promotion is asserted by publication. Recover from these four immutable files and the current Source task packet; do not repin scientific inputs.