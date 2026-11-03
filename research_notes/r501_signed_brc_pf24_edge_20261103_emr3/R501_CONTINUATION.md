# R501 -> 下一研究单元

Date: 2026-11-03. Status: author-side exact certificate; independent Driver review and native Result pending.
Scientific pin: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Predecessor: R500@0e54475ed4443f6c6f0da06ed70a43b5d02f12cf.

VERIFIED LOCAL RESULT: For signed BRC s=3, r=2k+1, D_24(k)>0 for integers 1<=k<=18 and D_24(k)<0 for all k>=19. The entire integer half-line is covered by an exact 145-point polynomial identity (degree<=144) and the 48 strictly negative Newton coefficients of S(19+u). The finite boundary S(1..18) is strictly positive. 20 direct Bareiss checks and 500 signed/ballot H crosschecks.

REPRODUCE: node R501_VERIFY.js > R501_EVIDENCE.json. Code and full certificate in this folder. Native control_attempt session_start returned STATIC_READONLY_SCOPE_DENIED operation_sent=false; control_tasks returned CONTROL_QUOTA; do not infer a current owner or a formal Task Result.

NEXT SCIENTIFIC UNIT: rank m=25 complete integer sign profile, using 50 Newton coefficients, identity at 151 distinct positive integer values and independent integer determinant cross-checks; if a tail shift is not sign-definite, test rational root isolation or Bernstein intervals. In parallel, factor exact rational rank generating-function denominator for selected k=2,6,19 and compare threshold patterns. Reuse R452/R462 EOR source and preserve signed branch information.
