# R43 exact verification — 2026-11-10

Command: `python VERIFY_R43.py` using exact Python Fraction and integer residues, frozen R42 reference files `VERIFY_R42.py` and `REFERENCE_R41.py` from PR #1983; scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The accompanying local R43 research bundle includes source, JSON certificates, and literal stdout.

| Case | Verified window vectors | Single-label expiry repairs |
| --- | ---: | ---: |
| S23 trillion, m128, K32 | 33 | 0 |
| sqrt2-1 m16 K64 | 65 | 0 |
| sqrt2-1 m257 K12 | 13 | 0 |
| sqrt3-1 m32 K32 | 33 | 0 |
| near 1/3 m21 K12 | 13 | 0 |
| mixed near 1/3 m257 K8 | 9 | 0 |
| short m16 N5 K80 | 81 | 78 |
| short m16 N16 K80 | 81 | 30 |
| short m16 N120 K80 | 81 | 0 |
| negative J m16 N12 K60 | 61 | 30 |
| historical endpoint m16 N16 K20 | 21 | 15 |

**PASS_R43_ROLLING_LABELLED_LAST_SOURCE_11_CASES**. Totals: **491 complete last-source vectors / 17,447 labelled values**. For ten cases all vectors compared against independent Euclidean Floor Sum; the mixed 257 case compares against an independently restarted R42; short-window cases also have literal brute-force checks. S23 terminal source ages: H0=164, terminal max age=138, no expiry during 32 shifts. All comparisons use exact rational/integer mathematics.

Scope: source-selection subroutine for auxiliary observer. This run did not rerun S23's full 298-segment affine risk compiler; its R42 two-path validation remains a separate prior result. Independent mathematical review pending.
