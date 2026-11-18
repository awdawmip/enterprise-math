# EC49FDA — eight-slot dual-carrier BRC prefix optimization

Input frozen pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Consume EC49FCZ exact 128-case certificate; reuse EC49FCS frozen_model.py and EC49FCY labelled trie solver.

Local question: for the A/B branch families EC49FCZ and selected (H4:r,H6:s,H7:t) signature triples, additionally free one distinct H6 or H7 slot (now 8 mutable paths) without changing the original 24-slot observer, fixed cache keys, or prefix semantics. For each exact instance compute the full-language minimum and preserve the first improving witness if below 158; otherwise store a reproducible exact certificate. Test both extra-H6 and extra-H7 variants at a bounded initial sample, measure actual state counts and memory before extending.

Scientific target: explicit improvement from 158 if present, or a more informative exact boundary for coordinated substitutions; continue toward the nine-window 93-edge objective. Owner and native Source claims must follow actual control authority; author-side preservation is separately permitted.
