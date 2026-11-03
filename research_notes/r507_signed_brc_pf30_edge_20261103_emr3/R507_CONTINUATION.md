# R507 continuation — exact signed BRC right-edge rank 30

- Source pin: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; predecessor R506@41e6c0e78a8ad36b587b69b1a557ae12b0e5cb96.
- Theorem (conditional on frozen R452/R462 polynomial premise): D_30(k)>0 for k=1..5 and k=7..37; D_30(k)<0 for k=6 and every integer k>=38. Here r=2k+1 and s=3.
- Reproducible certificate: degree f_30<=180; G_30=[k(k+1)(2k+1)(2k+3)]^30(k+2), degree 121; 60 Newton coefficients; 181 exact polynomial identity points; 60 strictly negative shifted Newton coefficients from k=38; all 37 initial integer signs. JS exact check: 20 direct Bareiss and 600 original signed-BRC/ballot checks. Independent SymPy original matrix check: 12 points.
- Files: R507_PROOF.zh-CN.md, R507_VERIFY.js, R507_EVIDENCE.json, R507_INDEPENDENT.py, R507_CONTINUATION.md.
- Status: author-side exact computer-assisted certificate; unreviewed; not formally admitted. GitHub author identity awdawmip, but native Researcher session denied STATIC_READONLY_SCOPE_DENIED, current owners list denied CONTROL_QUOTA; no invented CLAIM/Result/Driver authority.
- Next: s=3, m=31 using 62 Newton differences and 187 interpolation-identity points; compare the fixed-k order generating functions at k=6,7,37,38. Native X6 transfer is separate.
- P000 / ACTIVE worldview and frozen scientific inputs unchanged.
