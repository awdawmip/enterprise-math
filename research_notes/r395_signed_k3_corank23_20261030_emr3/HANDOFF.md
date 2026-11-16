# R395 portable research handoff (2026-10-30)

Status: AUTHOR_SIDE_EXACT / LOCAL_REPLAY_PASS / DRIVER_UNREVIEWED / NOT_ADMITTED. No source CLAIM, task Owner determination, native result freeze or review is asserted.

## Completed

From the exact signed twelve-branch R346 K/J kernels with only K3[t²]=-8(1+theta), derived the 47 polynomial Newton coefficients c0..c46 at corank r=23, and all 45 T1..T45. The finite PF2 set is exactly (-1,eta23], where eta23 is the sole T23 zero in (1865664/10^6,1865665/10^6), approximately 1.8656642740441771. An additional T23 zero is certified in (1869934/10^6,1869935/10^6), but c23<0 there; the local Turán re-entry does not reinstate PF2. Top coefficient c46=343059613650*(30-16theta)^46.

## Reproduction

In this folder execute `python r395_symbolic.py` then `python r395_certify.py`; both compute using exact integer/Fraction arithmetic, with SymPy only in the symbolic top coefficient identity check. The first script re-evaluates seven exact rational theta samples directly from K/J (`r395_exact.py`). The second prints R395_EXACT_PASS, checks complete sign and negative-witness coverings, and writes exact `R395_EVIDENCE.json`.

Inputs `r395_exact.py`, `r395_symbolic.py`, `r395_certify.py` contain no secrets. `R395_POLYNOMIALS.json`, `R395_EVIDENCE.json` and SHA256SUMS are complete reproducible results. The source R346 K/J blob was read via connected GitHub and matches the functions carried forward; R394 immutable predecessor e32bacd7fec48a880e1e3fc3d764fbe56ceee9b5. The independent Driver has not reviewed this work.

## Authority and source pins

GLOBAL_KNOWLEDGE_V1 fixed snapshot `main@7b33f8066e9993e7c941959a9d738ed405248eb8`; Enterprise Math fixed snapshot `main@7e2d83461e50e1a098816be5561bcd2c9d22d540`. P000 and ACTIVE worldview unchanged. Gateway is v0.6.11 and reports research_authority_granted=false. Task list query returned CONTROL_QUOTA; current owner not verified. This author-side portable record is not a canonical task/Result/Review/admission.

## Next precise unit

1) Derive 49 c_j and 47 T_j for r=24 from K/J and determine complete eta24 interval with rational certificate; avoid redoing r=23. 2) Search for uniform even/odd crossing location recurrence or counterexample, preserving all signed branch identities. 3) Request independent Driver mathematical review after the corresponding formal Source results can be legitimately published.
