# R558 signed BRC k=17 execution evidence

Observed date: 2026-11-05 (Asia/Shanghai).
Python 3.13.5; SymPy 1.14.0.
Scientific input: frozen R462 commit `18783e01e3646c72b7aab3b16d3f565e83e6446f`; exact predecessor R557 `72efdc6f4b9e7e0e071687b6908243e80374ec29`.

Local reproduction used `python R558_VERIFY_COMPACT.py` with the mathematical and verification operations reproduced in adjacent `R558_VERIFY.py`. The local verified script had SHA256 `331fb255e5c18e2f4dc0eee7af144972976406bf7febba389479d30b100dfec7`. This checksum applies to the local script, not independently to the published GitHub byte stream.

Actual stdout:

```text
R558_K17_ROUCHE_PASS 33 disks 528 pairs dominant>27 others<10
R558_K17_PHASE_PASS phi<=1056 q<=2230272 candidates=2063
R558_K17_RECURRENCE_PASS 514 511 0 307 raw_det=12
R558_K17_HALF_DENSITY_AUTHOR_CERT_PASS
```

Validation semantics: `sympy.nroots(n=65)` only discovers candidate centers. Each disk cert, distinctness test, modulus gap, atan/π enclosure, Euler-totient enumeration, rational-angle exclusion, recurrence and determinant equalities is asserted over exact `Fraction` or integer operations. The 12 raw determinant checks use Berkowitz; tested m=1,…,12. The first 1025 scalar signs are finite cross-checks; the infinite density and finite-zero conclusions use Rouché, rational-angle exclusion, Weyl and Skolem–Mahler–Lech as detailed in the proof.

Scope: author-side exact computer-assisted certificate for the frozen **signed BRC auxiliary scalar Toeplitz–Hessenberg model**, k=17. Independent mathematical review and formal TASK Result/Driver acceptance remain open. P000 and ACTIVE worldview were unchanged. No claim of native X6 realization, general-k theorem or physical dynamics.
