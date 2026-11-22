# R5 independent source audit: the S4 block Euler-jet numerator was miscomputed

Date: 2026-11-22 (Asia/Shanghai). Scope: frozen five-event scalar observer, \`awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`. Status: **EXACT_COUNTEREXAMPLE_TO_AN_INTERMEDIATE_FORMULA / PARTIALLY_REPAIRED_CYCLOTOMIC_WITNESSES / NOT_REVIEWED**. This is an independent portable audit, not a formal Result/Review or native X6 claim. Historical source/Activity identities are preserved; the prior files are not overwritten.

## Proven source defect and correct formula

For the fourth indexed event E4, support Z={296,...,312}, define D_Z(q)=∏_{p∈Z}(1−q^p). The event requires the **total number of Z items** to be <m. Its exact signed union-numerator component is

\[
C_m(q)=D_Z(q)\sum_{j=0}^{m-1}h_j\bigl((q^p)_{p\in Z}\bigr),
\]

where h_j is the complete homogeneous symmetric polynomial. The published helper implementations instead use

\[
\widetilde C_m(q)=\prod_{p\in Z}(1-q^{mp}).
\]

These polynomials are *not* identical. At m=2,
\[
C_2=D_Z(1+\sum_{p\in Z}q^p),\quad
\widetilde C_2=D_Z\prod_{p\in Z}(1+q^p);
\]
the second multiplier contains nonzero pair and higher-degree terms. This provides an exact counterexample to the intermediate identity used for S4. It does not by itself disprove the target least-period formula.

The defect is visible in the immutable source code:
- \`@6f0635fa79fc610410cdb88f39bf538d2ddac510:research_notes/portable_direct/r5_d23_firstjet_global_20261122/VERIFY_D23_JET.cpp\`, function \`cjet\`: multiplies factors with exponent \`p*m\`.
- \`@12d34b310988f62ecb34ce9b2fe8f56e99b30a12:research_notes/portable_direct/r5_triple_allphase_global_20261122/VERIFY_REMAINING6.cpp\`, function \`C\`: the same substituted factors.
- These exact substituted polynomials also appear in the associated research notes.

For primitive d-th roots zeta where D_Z(zeta)=0, the **correct** Euler derivative is

\[
\dot C_m(\zeta)=\dot D_Z(\zeta)\sum_{j=0}^{m-1} h_j\bigl((\zeta^p)_{p\in Z}\bigr).
\]

In particular, at d=23,25,27,31 the Z block has exactly one price divisible by d; its Euler jet generally differs from the archived substitution. At d=7,11,13 the Z block has at least two prices divisible by d, so both the true and substituted first jets vanish.

## Exact correction of the original six-order certificates

The bundled original 228-row compressed witness is a byte-for-byte copy of the original immutable evidence at \`@12d34b31\`; decoded CSV SHA256 \`fa987223acdeec3c310ef5e11122a924c290e0e3139e07e817a23b678eb997a2\`. The accompanying verifier recomputes the actual S4 first jet in the exact cyclic integer ring \(\mathbb Z[q]/(q^d-1)\) by the unbounded-multiplicity recurrence for each h_j, performs the author's same cyclotomic-coordinate reduction, and replaces **only** the wrong C contribution in each pre-existing coordinate. No floating point or new assumed ROOT certificates enter.

Original chosen-coordinate same-sign test after this correction:

| d | tested phases | still same-sign | previously selected coordinate fails sign criterion |
|---|---:|---:|---|
| 7 | 14 | 14 | none |
| 11 | 22 | 22 | none |
| 13 | 26 | 26 | none |
| 25 | 50 | 50 | none |
| 27 | 54 | 52 | r=4,5 |
| 31 | 62 | 59 | r=1,4,59 |
| **Total** | **228** | **223** | **5** |

The corrected selected coordinate for four failures is nevertheless a rigorously nonzero integer-valued **linear** polynomial on h>=0:
- d27 r4: \`6021 - 21870*h\`
- d27 r5: \`8775 - 33534*h\`
- d31 r1: \`1302 - 12493*h\`
- d31 r4: \`744 - 12493*h\`.

Each zero would require a positive noninteger value of h strictly between 0 and 1, hence is excluded. Thus **227/228** of the original selected-coordinate phase arguments can be recovered from their corrected original coefficients, using a nonintegral-root test in four cases rather than the old same-sign test.

At **d31, r59**, the original selected coordinate index 1 corrects identically to \`0\` (U=V=W=X=0), so that certificate is invalid. A different coordinate or a new exact polynomial must be verified before reasserting the all-m d31 nonvanishing dependency. A direct independent integer joint-incidence DP at m=59 gives A_m(zeta31)=0 and \`dot A_m\` in cyclotomic basis with coordinates 2..6 equal to \`[-6727,-53816,-47089,-40362,-6727]\` (others zero); correct \`dot C_m\` has only coordinate 0 nonzero \`-19220\`. Hence the full first jet at m=59 **is nonzero**, but this finite result alone does not prove its nonvanishing for all m=59+62h.

## Primitive 23 repair

The original d23 paper correctly separated the first 41 nonzero zero-order phases from five phases r=42,...,46 needing a nonzero first jet, but evaluated the latter using the wrong C substitution. Replacing C by its exact total-multiplicity numerator changes the **canonical coordinate zero** in those five phases to:

| r | corrected coefficient at h=0 | corrected slope, m=r+46h |
|---|---:|---:|
| 42 | -37881 | -37881 |
| 43 | -38180 | -38180 |
| 44 | 115 | 115 |
| 45 | -62192 | -62192 |
| 46 | -9430 | -9430 |

If the previously established rational t-pole multiplicity bound at d23 is valid, this coordinate is a degree-at-most-one function of h and exactly equals \`(h+1)*U_r\` for every h>=0, with U_r!=0. Thus the d23 first-jet nonvanishing conclusion survives the correction, though its formerly published numerical witness table must be superseded.

## Validation and effect on the latest frontier

- Exact original 228-row SHA256 checked; all 228 corrected by the included standard-library verifier. Local run: \`223\` same-sign, five sign failures at the exact (d,r) pairs listed. Four repaired by integer-root exclusion; one incomplete.
- Independent C++17 joint-incidence group-ring check at d31,m59 found the nonzero finite first jet above. Separate finite-field DP checks of the same phase at m=59,121,183 over primes 311,373,683,1489,1613 produced zero-order (0,0,0) and first-jet modular values of the form \`(u,2u,3u)\`, supporting—but not proving in characteristic zero—the candidate exact identity at that phase.
- The previously reported global eight-regime formula and 91-class all-threshold period theorem remain **author-side conditional claims with a reopened d31 r59 load-bearing proof dependency**. No numerical counterexample to their ultimate least-period values has been established by this audit. The d29/d32/d43 root classifications and unchanged unaffected jet orders are not rejected on this basis.
- The prior files' hashes and authorship remain unchanged. This audit supersedes the specific S4 formula, its derivative values and affected certificates, not unrelated facts.

## Precise next scientific action

Construct the full corrected characteristic-zero d31,r59 Euler-jet polynomial (or a more economical exact nonzero certificate valid for all h>=0); then recompute and replace all affected primitive-order witness tables with correct S4 semantics, check any other affected source claims, and independently assess the six-cone pole multiplicities. Keep the original frozen scientific input, prior attribution, and P000/ACTIVE worldview unchanged. Project authority: independent portable research source only; formal CLAIM/RUN/Review require live authorization.
