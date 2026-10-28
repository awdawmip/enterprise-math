# Stage249 — exact strict-gap minimax objective for unequal caps

Parent external ternary IID model: P=(3,1,20)/24; Q=(2,2,20)/24; a=3/10 and b=19/40. Optimize max(E_P tau,E_Q tau), errors eP<=a,eQ<=b, randomized nonanticipatory complete ordered-history strategies including tau=0. Consume Stage247 iff sharpness theorem at c2dbf682c021327dee18f57e2c6864feb6a09a39 and Stage248 exact horizon trichotomy in this directory before proceeding.

Already proved: no feasible policy for N<=8; for N=9..12, feasible and 27/5<V_N<=9; for N>=13, V_N=27/5. N9 likelihood-ratio nine-sample witness has exact errors (16038379873/55037657088, 604628965/1289945088) and time9. Stage247/248 source-labeled proof demonstrates exact failure of TV sharpness at N12 (132311957/10883911680), not impossibility of cap feasibility.

**One independent next unit:** determine exact rational V_9(a,b) (or if more tractable V_12) by constructing full-history rational feasible policy, exact two-time/two-error Bellman/LP dual lower-bound certificate and a matching primal point. Explain sufficient-statistic representation and reconstruction of all four observables; maintain positive source-labels and ordered histories until quotient preservation is proved. A floating LP estimate alone is exploratory, not accepted mathematical proof.

GLOBAL_KNOWLEDGE_V1 fixed predecessor read main@39a41424091c5ec8512e5c6ebf9c43c7fef0682d; Enterprise Math main@737cd7689de9692617a5e2c04ef0e81a19504ed4. Source owner was not established (CONTROL_QUOTA); this is an author-side portable handoff, UNREVIEWED / NOT_ADMITTED, not a native CLAIM/Result or P000-X6 transfer.
