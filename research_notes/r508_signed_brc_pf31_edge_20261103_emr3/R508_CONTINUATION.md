# R508 continuation — exact signed BRC right-edge rank 31

- Date 2026-11-03. Frozen science pin R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Predecessor R507@ff5a7f487092f3f3008479bd16ac8402763df5b0.
- Result conditional on frozen R452/R462 polynomial premise: D_31(k)>0 for integers 1<=k<=14, D_31(k)<0 for every integer k>=15 (s=3,r=2k+1).
- Exact reproducible proof: deg f_31<=186; G_31 positive, degree 125; 62 Newton coefficients; 187 polynomial identity points; 62 strictly negative shifted coefficients at k=15; initial 14 all positive.
- Independent verification: 20 direct 31x31 BigInt Bareiss, 620 signed BRC/ballot checks; 10 SymPy Berkowitz raw-definition determinants. Witness files: R508_VERIFY.js, R508_EVIDENCE.json, R508_INDEPENDENT.py, R508_INDEPENDENT_EVIDENCE.json, R508_PROOF.zh-CN.md.
- Fixed-k all-order rational generating function F_k(z)=1/[1-sum_(e=1)^(2k-1)(-1)^(e-1) H_k(e+2) H_k(2)^(e-1) z^e]; denominator degree 2k-1.
- STATUS: AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE, DRIVER_UNREVIEWED, NOT_ADMITTED. GitHub connected identity awdawmip (admin); native session denied STATIC_READONLY_SCOPE_DENIED, active owner request CONTROL_QUOTA, no invented claim/review.
- NEXT: m=32 classification (64 differences, 193 identity points); compare k=6,7,14,15,37,38 rational generating function poles. Preserve all scientific pins, P000 and ACTIVE worldview.
