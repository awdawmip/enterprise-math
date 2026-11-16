# R413 research handoff | 2026-10-30

Source: R413_PROOF.zh-CN.md; r413_verify.py; r413_independent_verify.py; R413_EVIDENCE.json (all in this folder). The R413 contribution is a whole-integer-corank exact positive-coefficient certificate for fixed s=26 and all r>=27, in the original signed 12-branch BRC **auxiliary combinatorial object**, conditional on the R404 Catalan kernel and R407 normalization. No native X6 mapping is asserted.

Reproduce with Python 3+SymPy: `python r413_verify.py && python r413_independent_verify.py`; outputs `R413_EXACT_PASS 2 53 53 94 282` and `R413_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks`. Evidence SHA256 for original producer JSON: `c5198c0b067e5aac9a91f105c1b9f16d9070696556258b95462512b27754cde7`. Both parity polynomials have positive integer coefficients: 26+27 for each numerator and denominator. The full coefficient vectors are in the JSON.

Input provenance: R412 immutable commit `84b736bead9564d65774aab3f03f9af1cc188d9e`, global control snapshot `00ef24faf2998a3c14cb3f10e8f618725eafc667`, EM project snapshot `1d6845f8f03cbd6d6647a57d5ad25877f0d06a7e`. The result is author-side, not Source-admitted; independent Driver and upstream R403/R404 derivation reviews remain open. GitHub actor must not be confused with authenticated native research session.

Next self-contained research question: prove/refute `D_(r,27)>0` for all integers `r>=28` using exact parity-shift polynomial certificates, or construct a uniform positivity argument without fixed s/k bounds. Previously finished bands are inputs, not work to recompute. In current combined coverage, open corner starts at `(r,s)=(156,27)` (`s>=27, r-s>=129`). Preserve signed branch provenance and P000/ACTIVE worldview; do not claim original X6 dynamical theorem or formal activity/CLAIM/Result/Review by this proof alone.

Publication and activity metadata: this PR branch file is an immutable research frontier once committed/read back; any actual activity record/checkpoint, native Owner status and independent review must be checked separately through the live authorized contract.
