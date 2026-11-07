# R401 full exact evidence and reproducibility index

R401 r=29 signed 12-branch K/J→B→D finite observer. Proven parameter classification: PF₂ iff -1<theta<=eta29, eta29 the unique T29 root in (1868683/1000000,1868684/1000000).

**Canonical code for regeneration in this PR:** r401_exact.py (raw Fraction recurrence), r401_symbolic.py (integer polynomial build), r401_certify.py (exact Bernstein sign certificates). Run both latter Python scripts with SymPy. Both write JSON to their own directory: R401_POLYNOMIALS.json and R401_EVIDENCE.json. These are computed research data, not custom axioms.

**Expected exact SHA256:**
- R401_POLYNOMIALS.json: 6375031691ee0a57d88b6c433a89e2afdc08c0bad111818e5fd232a66d73d207
- R401_EVIDENCE.json: 4a47e7a7e54cb538cbf45d1b5c446eaa5d91513c324d803094e4ae82b63aba30
- Local full source/data archive EnterpriseMath_R401_SignedK3_Corank29_ExactResearch.zip: 784ec00500b7f9a1692df5c165cf67387f0d13f8da6a8a4f0d5721ab3554741e

**Verified actual outputs:** R401_SYMBOLIC_PASS (59 C,57 T,812 crosschecks, polynomial dataset signature 63f136dbf1186353725d613b5d2e2f0c08a0f59230a3fb8c6e68d2401c0dc9c2); R401_EXACT_PASS (120 exact sign objects,132 rational leaves,139 Bernstein checks,9500 strictly positive rational controls, max depth12, certificate signature 9d08dbac7ccd9df5ec25dc16f5b7ae27ef7b58387907bb136800aac57fad820f). The root is bracketed by 85 exact bisections; the 13-leaf negative-witness cover handles (b,4] and the 17 exact-positive coefficients of -c0(4+u) handle infinity.

**Remote-storage scope:** GitHub stores all three execution sources, full proof, handoff, and the exact expected digests. The full generated raw JSON data and byte-identical replay logs are retained in the provided local ZIP. Raw JSON is not claimed to be present in the GitHub tree unless actually uploaded. Programmatic reconstruction is source-bound and deterministic under the documented Python/SymPy arithmetic. No hosted Actions run. No formal Source acceptance; no owner takeover. Git Blob SHA verification for all three scripts required upon publication.
