# R281 portable handoff — author-side (2026-10-25)

## Fixed source snapshots and research target

- Global Knowledge: main@8ce5de60e43a0ff3123f44d79c2d6424b0a44c06. Same snapshot includes mandatory bootstrap/manual/P000 startup/ACTIVE worldview and math/BRC/code policies. Original P000 blob: 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
- Enterprise Math canonical control read: main@9da3be970df5a28268b54d246594b2896bcff468. Portable protocol read.
- Mathematical parents: R279 signed rational generating function at 24f2d7515ac6bb8201d74c5dcdc1d61b6a11b159; R280 local CLT, spectral gap, bounded-mode localization at 66be646553b1b7e8f989bd60dc91124dedfdb5f8. Author-side only; R280 Driver review still outstanding.
- Objective: first signed clean reset Edgeworth correction and asymptotic unique full-effect peak. Carrier retains each original source word, endpoint q0, affine sign and integer shift; formal positive BRC auxiliary model, not P000 physics/time.

## This round's derived theorem

For n large, bounded k≡n mod 2, sigma2=(15+7sqrt5)/10, mu+=-(2+sqrt5), mu-=-(5+sqrt5)/2,

P_n(e,k)=phi^n/[5 sqrt(2*pi*sigma2*n)]*[1+(1+3sqrt5/8-(k-mu_e)^2/(2*sigma2))/n+O_M(n^-2)].

Fourth cumulant: -(3825+1711sqrt5)/50. Both signs have identical second log-amplitude derivative -(119+53sqrt5)/10. Together with the prior fixed-width global maximizer lemma this gives, for **some unspecified integer N**, unique clean maximum (+1,-4) on even n and (-1,-3) on odd n.

Finite exact work: SymPy algebra verified, source-DP through n=400, independent Laurent-GF coefficients through n=150 (21,463 nonzero integers identical), parity throughout. Observed n=81..400 matches predicted unique maximizer, last exception n=80, **not a proof N=81**.

## Published source and verification

Research directory:
research_notes/r281_edgeworth_signed_peaks_20261025_t3/

Files:
- R281_EDGEWORTH_SIGNED_PEAK_AUTHOR_PROOF.zh-CN.md — complete author-side derivation.
- R281_verify_edgeworth.py — executed Python+SymPy symbolic and unbounded integer verifier.
- EXACT_EVIDENCE.json — actual output of the verifier; status PASS.
- HANDOFF.md — this handoff.

GitHub remote code blob 6f94299709f50119a6ee91a262200c6693162062 and evidence blob f1167c096ec968391e1cdc3bee2b40a73b9b0c7e match the original locally executed bytes. The proof was additionally read from remote and is nonempty. Branch storage is not canonical mathematical admission.

Research-Activity-ID RA-EMR3-20261025-1022-R281EDGEWORTH (on EM main). Canonical-format locally allocated Researcher-ID EM-DIRECT-851BF0 (activity record corrected at EM main@0c20646ad4d9fa5345dcdbc28c35fdf52a2bc5d7); session label emr3-20261025-1022-local; no platform-issued Researcher identity. Native em_control_tasks failed CONTROL_QUOTA, native em_session_start denied STATIC_READONLY_SCOPE_DENIED(operation_sent=false). Current active Owner and formal CLAIM remain unverified; no native Source Result or independent Driver review. These restrictions were not circumvented using another storage provider.

## Next smallest unresolved unit

Derive a **rigorous effective bound N** for the two alternating mode comparisons (explicit saddle-point remainder bound or positivity certificate). Once the clean peak is effectively fixed, compare dirty q0/q1/q2 at exactly (+1,-4) for even and (-1,-3) for odd; derive or falsify eventually B_n=Lambda_n. Do not promote R281, R280 or any BRC auxiliary result to P000 native dynamics without a separate fidelity map and review.
