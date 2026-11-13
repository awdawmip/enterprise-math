# R472 signed BRC exact continuation

Date 2026-11-02; Draft PR #1708; follows R471 commit c8128da3cf4308afb6a9da3594cfd4c9ce8921cc.
Scientific frozen source: R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f; original E/O/R source Git blob 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff.
This directory includes the three scripts actually executed plus JSON sign/identity/crosscheck evidence. Reuse the identical kernel and optional exact C accelerator already published in:
research_notes/r468_signed_brc_right_edge_209_216_20261102_emr3/

From the repository checkout:
1. Copy R462_VERIFY_FROZEN_KERNEL.py and R468_EXACT_KERNEL.py from the R468 directory into this directory; optionally copy R468_GMP_ACCELERATOR.c and compile it with gcc -O3 -shared -fPIC R468_GMP_ACCELERATOR.c -o R468_GMP_ACCELERATOR.so -lgmp.
2. Run python R472_CERTIFY.py 241 248 (or each s separately), python R472_ROW_VERIFY.py, python R472_INDEPENDENT_ROW.py.
3. Compare per-s polynomial stream SHA256 in R472_EVIDENCE.json; confirm row stream hashes from both independent programs.
The original commands were run separately for s=241,...,248 on 2026-11-02 using exact integer arithmetic. Full local execution produced 19,576 positive polynomial coefficients, eight Desnanot-Jacobi identities, 160 raw/Catalan crosschecks, and 3,204 exact row sign checks with 64 further crosschecks.

Scientific scope: signed BRC auxiliary scalar; conditional PF3 through r=271 depends on old author-side R447/R450. Source publication is a Draft PR handoff, not formal task CLAIM, independent review or native mathematical admission.
