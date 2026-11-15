# Next research unit — certified integer-budget mixed allocation

Mother objective: source-aware frozen BRC S23 T/B trial optimization as one research route in the open ten-label decoder minimax mother problem (recorded [1/2,2/3]).

Already established and not to rerun: for F=C_T/(2-s)-C_B <=0, pure B sampling is optimal at every integer budget. For rational s with F>0 and cT=P/Q reduced, K=LP+1 and (m,n)=(LQ,1) beats both pure allocations whenever LP F>C_B. Exact witness at s=1/2,v=1/21,K=75001,m=50000,n=1: strict gain over pure B >1/1600, strict gain over pure T >0. PROOF.md/VERIFY.py/RUN_EVIDENCE.txt contain reusable exact certificate. Preceding global-uniqueness lemma is author proof, awaiting independent review.

Immediate next question: can a significantly smaller K admit strict mixed-vs-pure advantage, and can the globally best admissible (m,n) be certified? For K=6..100 and explicit rational s mesh above s_c, enumerate all m,n with m(2-s)+n<=K. For EACH allocation optimize one SHARED t in max_t[m f_T(t)+n f_B(t)] with certified interval/transcendental bounds, rather than summing separately optimized Cs. Give finite exhaustive coverage and exact error certificates, or an analytic minimum-budget proof. Test whether optimum uses n>1. Retain source labels and full cost including unused capacity.

Native research CLAIM/Result/Driver review is pending actual Source permission/owner resolution; do not invent session identity, task ownership, or admission.
