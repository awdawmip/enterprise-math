# R681 — Author-side durable research handoff

Task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW; publication TP2-47D65B35A7D48082EFBB; frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Prior R680: PR #1921, immutable 151d820a1c776fe4b1401ab0a23b1d0867c13883. No formal CLAIM or independent Driver acceptance is asserted by this file.

Research question: After R680 fixes unique event-by-event V27 active-triad selection, can unordered V23 triad plus full V29 count ledger safely replace V17 full ordered inherited slot frame?

Proved within a precisely declared primitive PASS model: no, a structural ordered-frame residual survives. With baseline u=(3,2,4,-10) and initial triad 145, positive BRC word ACB ends at unordered triad 015 / frame 105, while BCA ends at unordered 015 / frame 015; all completed V29 counts are equal. Common later legal V17 successor 015->012 maps those to frames 102 and 012. Ordered-label inheritance is explicitly part of the observer. This is a concrete extension of R680, not a new P000 axiom.

Complete finite census: six R679 initial biases times 20 initial triads, each with all 16 distinct-PASS words of length <=3: 1920 histories. Summing minimal observable state counts separately across 120 fixed-initial-context machines gives 1141 for (M,unordered triad), 1143 for (M,ordered frame). Exactly one context has a frame-splitting ledger-triad fiber, producing two extra states; no collision at <=2 PASSs in this restricted corpus. The analytic theorem is Markov future-sufficiency of (M,F) with fixed u0, and minimality follows from the declared current observation.

Evidence: R681_PROOF.zh-CN.md (complete statements, proof and boundaries), R681_VERIFY.py (standalone exact-integer enumeration), R681_EVIDENCE.json (counts, histograms and witness). Local execution of the source-equivalent verifier succeeded; exact remote blob readback is required before labeling the branch durable. Publication and formal task completion are different operations.

Open dependencies: the event order is still an external labeled input rather than a source-derived autonomous X6 scheduler; V39 loop current j is not updated; full typed rotation covariance and general future minimum for autonomous many-Cell X6 remain unproved. Next unit: derive permitted PASS/TRANSFER scheduler and V39 current updates; compare (M,F,j,scheduler) future observers for safe quotient and BRC source preservation. No physical calibration.

Researcher role as verified in current native session: EM-X6-5440A9, activity RA-6A1C3418CDA2B529D75E6504; Source registration is independent of formal CLAIM.