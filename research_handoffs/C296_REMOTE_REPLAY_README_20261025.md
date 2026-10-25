# C296 replay and scope — 2026-10-25

Scientific object: the C195/H168 79-node **positive-rational auxiliary**; target `Q=2^128`. The frozen mathematical base is the C295 author commit `014e5b8444ee1b4ace1175566075cd12951e168e`, inherited into this research branch without copying or rewriting its original inputs. GLOBAL_KNOWLEDGE_V1 is pinned to `45aa95910fe2809e438d5b3cb8d2e37e8e5a1a1f` and Enterprise Math canonical control to `5ea0d75fdb6f1b110a3fb6f3c67a2589d6e81c42`.

From `research_handoffs/` run:
```bash
python C296_VERIFY_128_256_OUTWARD.py
python C296_INDEPENDENT_FULL_FRACTION_REMOTE.py
```

Both use only Python standard library and inherited C275/C288/C295 files. The first verifies both C295 and C296 SHA-bound integer arrays, all 500 endpoint signs using integer outward rounding at P=320/448, and strict margins >2^-142 / >2^-268. The second independently expands original 79 positive rational branches with `Fraction`, certifying all 250 256-bit endpoint signs and that each exact result lies in the proved P448 interval. Locally, both programs ran successfully; **no GitHub-run/CI result is claimed**.

Extended author manuscript, complete JSON K256 records, exact candidate-generation script and hardware-scoped resource logs reside in the accompanying ZIP for this research iteration. It includes SHA256 manifest and isolated re-execution. Floating-point secant proposes candidates only; proof uses exact directed integer intervals.

Research status: `AUTHOR_EXACT_FINITE_UNREVIEWED`. Native control `CONTROL_QUOTA` and `STATIC_READONLY_SCOPE_DENIED (operation_sent=false)` prevented owner verification and session/CLAIM. This author GitHub storage is not a Source Result, Driver acceptance or canonical main merge. Native GF(2)-BRC, ports, phase, provenance and X6 bridge remain open. Next task C297: prove uniform precision-dependent enclosure error bounds and genuine bit complexity.
