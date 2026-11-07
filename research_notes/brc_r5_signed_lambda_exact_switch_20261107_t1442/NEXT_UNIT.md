# R5 next unit — asymmetric time perturbations after exact lambda switches

Status: OPEN / AUTHOR-SIDE / UNREVIEWED. Frozen Global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Mother task: FULL_HIST vs seedless LR equality/separation for complete four-observer W=(eP,eQ,TP,TQ).

2026-11-07 frontier: exact signed support maximum at TP=TQ=31/10 for ALL real lambda in [-1/10,1/10], with two transition points -351/17291 and +351/16589. The entire exposed optimizer set at those transitions lies in seedless LR. See RESEARCH.md and executable VERIFY.py in the same directory.

Unfinished discriminating experiment: take (TP,TQ)=(31/10+epsilon,31/10-epsilon) and the reversed pair for epsilon in {1/100,1/50,1/20}. For selected rational lambda in {-1/10,-351/17291,-1/50,0,1/50,351/16589,1/10}, solve the full 7-variable rational LP (with all seven declaration keys). Derive a certifiable rational primal and supporting inequality, then test whether ANY seedless LR realization at the same fixed times and two errors reaches the full-History extremum. The bilinear seedless relation is 9*b*z=4*a*(v-z); replacing it by a fixed-flow condition is not sufficient. Preserve exact risk of false local separation under flow reconfiguration.

Second route: calculate exact nonnegative gap certificates for a neighborhood of non-symmetric time pairs to establish a genuine common support region. When a candidate difference appears, specify the exact four-observer W, not only an unobservable stopped-key mass vector.

Publish evidence on the same Draft PR under existing author scope; formal CLAIM/Result/Review requires current native authority. Do not alter original scientific pins or P000.
