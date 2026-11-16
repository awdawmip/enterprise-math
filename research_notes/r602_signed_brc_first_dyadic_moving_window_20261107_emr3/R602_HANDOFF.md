# R602 handoff — exact first dyadic moving window and full-disk error certificate

2026-11-07 · AUTHOR_SIDE_PROOF / DRIVER_UNREVIEWED / NOT_ADMITTED.

Frozen science: R462 signed BRC twelve-branch @18783e01e3646c72b7aab3b16d3f565e83e6446f. Auxiliary scalar observations only; P000 native X6 and joint-composite observer directions remain separate and unchanged.

New exact finite witness: k=2^42=4398046511104, c=1/64, L=64, X=113/8. With rho_k=c(log k)^2, 13<rho_k<14; k=2^41 has rho<13. This is the first dyadic exponent at which the moving window crosses 13.

Using R590 exact Catalan coefficient product, low-degree bound E=S+B with B=3(L+1)/(2(2k-L)), and the factorial tail after j=64, proved sup_(|z|<=113/8)|F_k-F|<=U<1/6720. Complete rational expression for U is in R602_PROOF.zh-CN.md; exact runtime certificate in R602_VERIFY.py and R602_EVIDENCE.txt.

By R600/R601 author-side uniform local Rouché lemma: for every F-zero |zeta|<=14 there is one simple matched F_k-zero with displacement <1/20; in particular the R593 first nonreal conjugate F-pair inside radius 13 is matched in the growing window. No converse all-roots coverage without good-circle count.

Current unfinished scientific unit: find a rigorously certified good circle for this k within (13,14), or an explicit count N_Fk(14) via R591 contour technique, and refine a much smaller k via sharper low-degree coefficient envelope. Then assess matched-set and omitted-tail contributions to V_k. Review R600/R601 load-bearing global zero geometry independently before mathematical admission.

Source: R590 proof directory research_notes/r590_signed_brc_moving_disk_20261107_emr3; R600 @468d87978cb4b4ba2ebb1530b0e3a004ff5e648b; R601 @03810fd313161818d66298f92dd6f5860e1ee21c. Native gateway attempt on this run returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; no native session, verified owner or formal CLAIM. Author-side Draft PR persistence is not a native Result/Review.
