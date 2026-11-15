# Sources and coverage
- Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
- Immediate predecessor: PR #1765 commit 09af0b3987632f8da6cbab552a24f1b6a6be3daa, directory research_notes/brc_n4_s23_k17_phase_s12_to_s35_20261105_research1. Its proof establishes fT/fB unique-optimizer facts and the inherited Chernoff model.
- Original exact interval arithmetic design: PR #1765 commit 6cea711da98353ce1408ed8d63ec76df9536a50e, VERIFY.py blob 6e445e1c57ff575aa0037bd2b7ceac09d890aa07. This run's VERIFY.py is a standalone copy/adaptation of the arithmetic semantics.
- Normative source check on 2026-11-05: global main e8ba2c13a8e1411e5e9d5f7a8a711a20af64db6e; Enterprise Math main 13a245c2bcb7d4c9a3cde5ca8e796f9965931a00. They are control pins, separate from frozen science.
- Execute: python VERIFY.py (Python stdlib, Fraction/isqrt, exact rational interval certificates). RUN_EVIDENCE.txt records actual execution output. No external statistical sampling or floating-point decision inequalities.
- Status: author-side analytic theorem / exact rational executed; not independently reviewed, no native claim or admitted Result.
