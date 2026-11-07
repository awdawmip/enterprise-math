# R505 scientific continuation — signed BRC auxiliary Toeplitz edge

- **Scientific pin:** R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f` (do not change).
- **Previous verified frontier:** R504 `e2535d803c6b1ab41c28b39d1f6b11914af0e40b` (27th order).
- **Current author-side frontier:** `D_28(k)` has signs `+ (1..5)`, `- (6..12)`, `+ (13..infinity)` for integer `k>=1`, under R452/R462 polynomial prerequisites. Proof and 56-coefficient exact certificate in sibling files.
- **Executed:** `node R505_VERIFY.js > R505_EVIDENCE.json` -> `R505_EXACT_JS_PASS` (169 polynomial checks, 20 direct Bareiss, 580 H/H2); `python R505_INDEPENDENT.py` -> `R505_INDEPENDENT_PASS` (8 independent exact determinants). The computation covers the exact auxiliary scalar model; no native X6 physical-residual claim.
- **Authority:** Connected GitHub identity `awdawmip`, write/admin permission; original Source control: `STATIC_READONLY_SCOPE_DENIED` for session start, `CONTROL_QUOTA` for active owner list. Native Researcher-ID/owner/CLAIM/Result/Driver review unconfirmed; publication only in existing research branch/Draft PR.
- **Next executable unit:** `s=3,m=29`, 58 Newton coefficients, 175 distinct integer identity points, same frozen pin. If the 58 shifted coefficients never become uniformly signed within the bounded search, classify finite-window sign behavior and inspect the fixed-k recurrence generating function instead of expanding the claim.
- **Alternate explanatory unit:** For k=6,12,13,25,26, factor the exact rational generating-function denominator for `sum_m f_m(k) z^m`, then compare its characteristic root/phase structure to observed m=27/28 sign thresholds. Record exact certificates, not numerical intuitions alone.
- **Admission scope:** AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE; DRIVER_UNREVIEWED; NOT_ADMITTED. Preserve P000 and ACTIVE worldview unchanged.
