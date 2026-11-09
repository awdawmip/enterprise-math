# Next research unit — S23/AV first-increment equality and plateau 413

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Current author proof: this directory's PROOF.md, VERIFY_FIRST_DEVIATION.py, RUN_EVIDENCE.txt.
Previous exact Bayes-risk partition theorem: 540863cb933fe4c5b76523c08f5379fe04b66d8f.
Status: author-side proven mathematical argument, independent project review pending; no shared Task CLAIM.

The all-index first-deviation question is answered:
for irrational theta, e_m=min_{d<=m}||d theta|| and q(m) the next strictly better return,
R(m,L)=L e_m exactly through L=q(m)-m, and first fails at L=q(m)-m+1.

## Smallest new open question

The observed first increment in all ten certified frozen S23/AV cases equals ||q(m)theta||. Determine whether this is true for every irrational theta and m. Begin with the old P_m cell adjacent to t_0 and use three-gap/continued-fraction structure to decide whether its maximal refined subgap is necessarily the one split by t_{q(m)}. If false, construct an exact rationally enclosed irrational-rotation counterexample, preserving m, q(m), original gap partition, and exact first increment.

Second independent option: geometric coverage certificate for S23/AV plateau 413, using frozen critical-cell checker and its original covering obligations. The return-time theorem is about auxiliary observer forecasting and is not by itself a plateau covering witness.

Implementation follow-up: a certified incremental partition-refinement algorithm could compute all R(m,L), L<=Lmax, without repeated sorting; compare full precision/cut construction/update/verification costs.
