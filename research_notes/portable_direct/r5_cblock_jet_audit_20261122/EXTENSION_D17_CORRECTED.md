# R5 order-17 first-jet corrections: 10/10 phases recovered

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_EXACT_CORRECTION / INTEGER_CYCLOTOMIC_CROSSCHECKED / NOT_REVIEWED. Scientific input remains frozen at enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.

## Located dependency and correction

The previous author-side d17 theorem at enterprise-math@6f0635fa79fc610410cdb88f39bf538d2ddac510:research_notes/portable_direct/r5_d23_firstjet_global_20261122/EXTENSION_D17_D19.md used the same incorrect S4 formula as the d23 and six-order sources. In VERIFY_D17_D19.cpp, function cjet(m) assigns the Euler derivative of product_{p=296}^{312}(1-q^{mp}); the original event instead counts the total number of Z items being less than m.

The correct Euler derivative at primitive d=17, where D_Z(q)=product_{p=296}^{312}(1-q^p) has a simple cyclotomic zero, is

\[
\dot C_m(\zeta_{17})
=\dot D_Z(\zeta_{17}) \sum_{j=0}^{m-1}
h_j\bigl(\zeta_{17}^{296},\ldots,\zeta_{17}^{312}\bigr).
\]

The first three overlapping short events retain the exact signed joint incidence; their original computed A_m and dot A_m values are **reused unchanged** from the pinned source CSV. On the ten phases r=13..17 and r=30..34 the previous paper had A_{r+34h}=0 and needed a nonzero first jet. At fixed r, the previous rational six-cone bound gives dot A polynomial degree at most 2 in h; the corrected Cdot along m=r+34h is affine. For all ten phases the second forward difference computed from m=r,r+34,r+68 is zero, so dot R is exactly affine for every h>=0. Corrected canonical coordinate 0 gives:

| r | corrected U | corrected V |
|---:|---:|---:|
| 13 | -13328 | -29087 |
| 14 | -6681 | -10268 |
| 15 | -7565 | -17782 |
| 16 | -12631 | -25262 |
| 17 | -4046 | -6545 |
| 30 | -29087 | -29087 |
| 31 | -10268 | -10268 |
| 32 | -17782 | -17782 |
| 33 | -25262 | -25262 |
| 34 | -6545 | -6545 |

In each row U is nonzero and UV>0; therefore U+hV never vanishes for any nonnegative integer h. The previous 24/34 nonzero zero-order phases are unaffected because they need no S4 Euler derivative. Hence the all-positive-threshold d17 root/first-jet nonvanishing theorem survives with **10/10 corrected derivative witnesses**, conditional on the six-cone pole-degree lemma, without changing its statement.

## Exact reproducibility

The included VERIFY_D17_CORRECTED.py computes the true complete homogeneous sums of the 17 Z-price monomials in Z[q]/(q^17-1), evaluates the actual derivative and subtracts the old substituted derivative, and adds their difference to the pinned author CSV's ten selected coordinate coefficients. It verifies second differences and nonzero same-sign roots, saving D17_CORRECTED_WITNESSES.csv. A local Python standard-library run returned:

    PASS corrected_order17_firstjet=10/10 all same-sign; degree_le_one consistent

The local corrected CSV SHA256 was acc557767413431f3327e8abd42e939fddd076b438c51b4bfd436dd85fe431d7. The calculation is a correction to author A values, not an independent rewrite of the joint-incidence DP.

## Effect on complete R5 frontiers

Across the source-pinned lower-bound orders, the mistaken S4 derivative was load-bearing at d17, d23, and the six-order d25/d27/d31 groups. The repairs recorded in RESEARCH.md, EXTENSION_D31_R59_REPAIRED.md and this note restore all their targeted first-jet nonvanishing arguments. At d19 and d37 previous proofs used nonzero R_m(\zeta_d), not the S4 derivative. At d7/11/13 the S4 denominator has at least two cyclotomic zeros so its first derivative vanishes, unaffected by the substitution. The primitive d29/d32/d43 all-m cancellation claims are separate prior proofs and still require independent audit.

The global eight-regime least-period formula retains author-side **conditional, NOT_REVIEWED** status. No formal Result/Review acceptance or P000/native X6 transfer is asserted. Next action: independently check the underlying six-cone pole-degree bound and the 29/32/43 cancellation arguments in their immutable sources, then consider a lossless BRC/observer transfer.
