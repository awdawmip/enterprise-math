# R45 — exact execution evidence

Date: 2026-11-10. Researcher-ID: EM-DIRECT-8D941E / TASK_RESEARCH. Research-Activity-ID: RA-3FE8F89994D035EA414A978F (native Source registration verified). Frozen pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Extended local execution using Python stdlib Fraction and integer arithmetic:

```
PASS_R45 128 389 3
PASS_R45 8 120 7
PASS_R45 16 128 5
PASS_R45 7 100 7
EVIDENCE_SHA256 460605f646a5f234e2d1621e8e45119519b01d9e9b0b32ce7c4109b6f83b1689
FROZEN_S23_STAGES [(128, 164, 'left', 67), (164, 225, 'right', 0), (225, 389, 'right', 0)]
PASS_R45_COMPILER S23 262 3 (-7551, 28800)
PASS_R45_COMPILER S23_low 262 3 (-7551, 28800)
PASS_R45_COMPILER S23_high 262 3 (-7551, 28800)
PASS_R45_COMPILER S23_short 113 8 (89, -336)
PASS_R45_COMPILER sqrt2_rational_bound 113 6 (193, -464)
PASS_R45_COMPILER sqrt3_rational_bound 94 8 (211, -287)
PASS_R45_FROZEN_R32_261_UPDATE_CHECK
COMPILER_SHA256 7d68018c190c556b990d48c283c6387791d35a474fadfd103683ebcdc2e98e8d
```

Each of 262 S23 risk levels (including R_128) was independently reconstructed from phase-sorted elementary gaps for theta midpoint, lower rational endpoint and upper rational endpoint; all coefficient pairs agreed. Generation performed **zero full-gap-maxima boundary queries**; independent verification used full geometry. Exact stage reset: at s=164 the new extinct rank is 67, at s=225 it is 0, although the old rank at either boundary equals 128.

Standalone independently executable `VERIFY_R45_COMPACT.py` is published alongside this record. The complete executed local `VERIFY_R45.py`, `EXACT_CERTIFICATE.json`, `COMPILER_CERTIFICATE.json`, `PROOF.md` and next-task note are archived in `R45_RESEARCH_BUNDLE.zip` in the originating research conversation. The independently archived frozen R32 TSV was loaded from R42's prior bundle only as a regression oracle, never as generation input. Project acceptance and independent math review remain pending.
