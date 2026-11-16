# R468 author-side exact research

Result: s=209–216, 16 full positive-coefficient polynomials, 17,016 strictly positive integer coefficients, 8 Desnanot–Jacobi identities and 160 raw/Catalan crosschecks, each fixed s covers all integers k≥floor((s+2)/2). Conditional PF₃ collage extends odd r through 239; independent finite r=233,235,237,239 yields 2,820 strict integer signs, 64 raw/alternating checks.

Read R468_PROOF.zh-CN.md before interpreting the claims. This is not a canonically admitted Result and still depends on R447/R450 for the combined PF₃ corollary.

R468_EXACT_KERNEL.py imports R462_VERIFY_FROZEN_KERNEL.py (frozen R462 mathematical kernel, copied unchanged from R466). Run python R468_EXACT_KERNEL.py; python R468_CERTIFY.py 209 216; python R468_ROW_VERIFY.py.

For performance, optional: gcc -O3 -shared -fPIC R468_GMP_ACCELERATOR.c -o R468_GMP_ACCELERATOR.so -lgmp. No compiled binary is committed; pure Python fallback uses exact arbitrary-precision multiplication. R468_EVIDENCE_ALL.json and R468_ROW_EVIDENCE.json preserve completed numbers and exact stream hashes; run scripts regenerate per-s evidence. The full run-log and local SHA256 manifest are in the downloadable local ZIP supplied in the ChatGPT run, not in this PR.

Source pins: current normative global main 5cef4755fe796ca26a3014112791967d8d5ad6cc; Enterprise Math current main 3c5f59dd53d611b617195753254f2a8791073557; frozen science R462 18783e01e3646c72b7aab3b16d3f565e83e6446f; prior frontier R467 9c555bc4e8b5bc071e9fc48794350230a676fa4d.
