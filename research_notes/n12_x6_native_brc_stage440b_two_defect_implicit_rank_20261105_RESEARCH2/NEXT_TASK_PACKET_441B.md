# Stage441-B — extend double-source quotient beyond one defect per source

Parent: Stage440-B PR #1736 and its exact rank/population formula. Frozen science: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

Mother problem: minimal future-sufficient BRC/X6 static ordered histories under bounded independent POP/APPEND. Stage440-B solved equal-length, one interior B defect in each source, K=L-2, 1<=b<=a<=L-4, one APPEND each. It obtained q=(d+1)(s+1)+s² and direct no-codebook rank/unrank.

Next discriminating test: choose two interior nonadjacent B defects in EACH source of equal length, preserve both complete directed J histograms and a fixed K. Compare POP budgets (1,1) and (2,1), APPEND (1,1). Try a finite-state DP on (position, defect counts in each source, previous defect flags, current K, exposed suffix/crossed labels), counting support and exact original multiplicity by R class. Check against brute enumeration of the same full-O fiber and all twelve APPEND labels on small domains. Deliver an exact population and implicit rank/unrank theorem or a strict missing-state example with raw ordered paths and distinguishing operation trace. Include input conversion O(L), DP states, arithmetic bit sizes, class label, within-class reconstruction, evidence and unresolved cases.

Publication: reuse this existing Draft PR branch; preserve stage/source scope and review/claim authority.