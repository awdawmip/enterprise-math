# R561 research handoff — fixed k=20 signed BRC scalar density

**Mother question:** Seek structural exact sign laws and a uniform-k mechanism for the frozen R462 signed BRC auxiliary Toeplitz–Hessenberg scalar observable.
**Source pin:** R462 commit `18783e01e3646c72b7aab3b16d3f565e83e6446f`; parent R560 commit `1aced918e683b086f1707c5d83750e2d3e541bd8`. P000, ACTIVE worldview unchanged.
**Current result:** For fixed `k=20`, author-side exact certificate gives density 1/2 for both strict signs, with finitely many zeros. See `R561_PROOF.zh-CN.md`.
**Reproduce:** Python 3.13.5, SymPy 1.14.0. Run `python R561_VERIFY.py` and check `R561_K20_HALF_DENSITY_AUTHOR_CERT_PASS`. Exact acceptance: 39 disjoint rational Rouché root disks, 2887 totient-screened torsion exclusions, raw H identities, 12 direct determinant checks.
**Evidence:** `R561_EVIDENCE.txt`, which distinguishes executed local program and archived equivalent variant. No formal claim/Result/Driver acceptance.
**Next discriminating unit:** k=21 full separation and phase exclusion; parallel uniform dominant-modulus hypothesis. Query native `RS-X6-NATIVE-ROTATION-DYNAMICS` current owner independently before any formal claim; do not conflate these two mathematical objects.
**Role activity:** Source service issued Researcher-ID `EM-X6-431CFA`, RA `RA-9F9F4D3372C2B7B1EA640FD5`, claim=false. Exposed directed context; no independent review.
