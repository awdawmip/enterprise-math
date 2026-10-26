# R1T11 actual execution evidence (Stage164 author)

Executed locally using Python 3 and fractions.Fraction, two independent representations in /mnt/data/verify_stage164.py:
- exact backward Bellman and forward count-suffix recursion on all 680 (n,a,b) states;
- full ordered integer-weight DFS (PN=(3,1,20), QN=(1,1,10)), with independently accumulated terminal eP/eQ/tP/tQ and terminal masses.
- all four corner vectors equal EXACTLY between those computations, with total terminal mass P=Q=1 at every corner; zero mixed vector.
- 680 states, 1238 strictly positive nonminimum Bellman gaps, minimum 141134197/6494515200, tie states R/S exactly; no negative gap.
- R 10 first-hit ordered histories, S 12056; DFS nodes 00=445864,01=409696,10=445624,11=409456.
- left endpoint EXACTLY Stage163 alpha,V; two endpoint Bellman equalities, strict positive tP-tQ; width 17071484375/17158292304297984; right coin saturates S and R stays interior.
- PASS written as rational certificate164.json; actual stdout verify_stage164.log.

Executed separately /mnt/data/scan_stage165.py: exact tangent sensitivity and next-dual-closure scanner; published candidate165_summary.json. Stage165 is DUAL CANDIDATE ONLY, primal unproved.

Note: GitHub PORTABLE_VERIFY_STAGE164.py is a faithful adaptation of Stage163's published verifier, not a byte-identical copy of the independently executed verify_stage164.py. An upload/readback is not a remote Python run. Local code/logs/certificate may be shared as the R1T11 evidence ZIP; the GitHub full mathematical proof is PROOF_STAGE164.md. No native review/CLAIM, and the parent objective remains ongoing.