# R365 executable handoff (2026-10-28)

Source: original signed BRC K/J in existing research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py on this PR branch. Parent PR #1592 remains Draft. Previous complete ancestor R364 at 04d6dad2d8eb5a885bbaf1dc8e70305c89d70d06.

Frozen global canonical main e531e8ab792fe44637f9d3be0a73ab5c0cf48669; Enterprise Math main bd0dd87b6864ce4994cee0a7d32eaacb0cfa4263.

New finite r345..352: 5584/5584 exact positive Newton, 5568/5568 strict ordinary Turán, 5107 negative + 461 positive ULC, no ties, 64 raw D minor checks; all-decimal SHA256 50bf1a56fabe89d4752ed71634cbb95d6c7c320d61b09aba1c501857650555a7. R364 q344 regression hash exact. R365_reproduce.py executed locally and writes full 5584-line certificate plus per-r digests. Independent R365_scan.py and a complete original decimal output were retained in the attached R365 complete archive. R365_transition_check.py independently checks the r347/r348 first-positive shift using direct binomial sums (no forward_differences).

Structural result: using R364 finite r1..344 and the eight new rows, every r1..352 has a positive strictly log-concave coefficient vector; so PF2. Every r has a negative ULC defect; Newton's inequalities exclude all-real zeros of its coefficient generating polynomial, hence it is not PF∞. A presumed fixed 57-entry ULC-positive tail fails at r348 (58 entries).

Reproduce: run python R365_reproduce.py from the PR branch; original R346 dependency must be accessible at the listed relative path (for an isolated extraction, place it under research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/ adjacent to the script). Compare combined_rows_sha256 to the recorded digest. All-k fixed-r claims require author-side R363 extraction/degree theorem, independently unreviewed. No native X6 observer map or formal Source CLAIM/Result/Driver approval. Keep UNREVIEWED / NOT_ADMITTED.

Next: prove all-r PF₂ or find a sign-preserving BRC counterexample; derive threshold j*(r) transitions (r348 first step); independently audit R363 and native correspondence. No need to recalculate completed r345..352 absent a changed dependency.
