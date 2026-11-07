# Next BRC N4 / S23 research unit (portable)

Input: PROOF.md in this directory, the exact six-row mixing M, six latent cells AU0 AU1 AV BU0 BU1 BV, the lawful eleven-control behavioral S23 chart, and ancestor PR #1762 commit 24287b48d496fcf2eb01777c9e6ee3f90047a36d. Do not rerun the completed deterministic encoder proof.

Current result: for a deterministic common 5-state encoder and arbitrary policy-aware decoder, exact worst-case error = 1/40. With finite m labels, the error is >=1/40 and approaches this value with the explicit eleven-coordinate quantization. For arbitrary randomized 5-state E, supported bounds on the full-policy-visible error remain [1/47,1/40]. The original finite-label behavioral problems R_(4,10) and R_(6,10) remain [1/2,2/3]. These are separate minimax questions.

Next exact question: Is there a stochastic 6-by-5 row-stochastic encoder E, not equivalent to a deterministic merge, and cell-dependent time-3 decoder probabilities g_x in the range of E, that can achieve r<1/40 simultaneously for all six legal indicator policies H_x? Formulate the 6 indicator constraints ||M(e_x-E d_x)||_infinity <= r with 0<=d_x<=1 and row sums of E equal to one. Either construct a rational feasible witness r<1/40 (then test all eleven-control policies), or prove a certified infeasibility bound >=1/40 valid for every E. A numerical nonconvex solver alone is exploration, not proof.

Secondary: investigate exact asymptotic floor for deterministic k=4; audit the S23 third-stage information set and separate S2 legality; retain the obligation for a future-operation-preserving embedding into native P000 X6 and independent time. Preserve author / reviewer independence and record a real native owner/CLAIM only after a verified native authorization receipt.

Reproduce: `python3 VERIFY.py`. Expected `PASS_BRC_N4_S23_DETERMINISTIC_K5_EXACT_FLOOR_20261101`; exact checks include 4096 strategy tables and 24576 prepared-law TV calculations. The analytic theorem has larger universal coverage than the enumerated checks. Status: AUTHOR_ANALYTIC_PROOF / FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED.
