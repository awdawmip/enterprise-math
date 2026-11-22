# PREFIX-1015 — Strict all-length negative-port Gram dominance as an exact sum of squares

2026-11-22 (+08). Status: **AUTHOR_EXACT_LAURENT_PROOF / EXACT_INTEGER_CHECKED_N5_TO_N14 / NOT_REVIEWED**. Continuation of PREFIX-1014, within the frozen **candidate** signed BRC model. This is an observer-specific model-internal theorem, not Foundation promotion.

## Frozen input and observer

Science input: P000 V5 at \`enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`; native signed six-axis Cell steps, original chart-relative anchor and incoming-neighbour ports; integer signed BRC weight \`w(h,d)=1-6[h=d]\`, terminal incoming port \`-d\`; the two orientations of the Link \`{0,e1}\` are blocked. Initial packet \`(chosen Cell 0,h=-e1)\`; grade \`k=1\` contains exactly one negative native-axis step. Same-cell AND same-terminal-port amplitudes interfere before taking squares, without renormalization.

Exact predecessor: [PREFIX-1014](https://github.com/awdawmip/enterprise-math/blob/599f5d5306abae0101769432d6ff8da77517bf3e/research_notes/portable_direct/2026-11-22_r6_prefix1014_four_port_gram_orbits.md). Its full Laurent amplitude identity, rather than a historical numerical fit, is used below.

All Laurent polynomials are in \`Z[z_1^{±1},...,z_6^{±1}]\`. Let \`S=z_1+...+z_6\`, \`T=S-z_1\`, and \`V_j=S-6z_j\`; define \`f^*(z)=f(z^{-1})\` for integer-coefficient Laurent polynomials and \`||f||_2^2=CT(f f^*)=sum_x ([z^x]f)^2\`. Its torus/Haar form is an exact integer coefficient identity. Write \`A_j=V_j V_j^*\` and \`D=A_1-A_2\`.

From the previously proved PREFIX-1014 negative-port identity
\`N^L_{n,j}=z_j^{-1} S^{n-3}(S-6z_j)(S-z_1)\`,
the per-port squared numerator is, for every integer \`n>=5\`,
\`Q^-_{n,j}=||S^{n-3}T V_j||_2^2\`. Here \`j=1\` is the distinguished negative-direction terminal-port class, and each fixed \`j>=2\` has the same mass by S5 symmetry.

## Theorem (strict negative-port dominance, every length)

For every integer \`n>=5\`, in the frozen X6 model,

\`Q^-_{n,1}-Q^-_{n,j} = (1/12)|| S^{n-3} ( |S-6z_1|^2-|S-6z_j|^2 ) ||_2^2 > 0\` for every \`j=2,...,6\`.

All absolute-square symbols denote Laurent products \`f f^*\`, not unsigned replacements of the original BRC amplitudes. The equality is an *exact certified terminal-observer identity*; in particular the contrast has a uniform strict sign for all lengths, not only the predecessor's checked finite range.

**Proof.** By axes 2–6 symmetry it suffices to compare \`j=2\`. Let \`C=SS^*\`, \`A=V_1V_1^*\`, \`B=V_2V_2^*\`, \`D=A-B\`, and let \`L(F)=CT[S^{n-3}(S^*)^{n-3}F]\`. This linear functional is invariant under the exchange \`z_1 <-> z_2\`. The elementary Laurent identity
\`6TT^*=5C+A-30\` follows by expanding \`T=S-z_1\` and \`V_1=S-6z_1\`.

Thus
\`6(Q^-_{n,1}-Q^-_{n,2})= L[(5C-30)(A-B)] + L[A(A-B)]\`.
The first term vanishes since \`C\` and \`L\` are exchange symmetric while \`A-B\` is antisymmetric. Exchanging 1 and 2 gives
\`L[A(A-B)]=L[B(B-A)]=(1/2)L[(A-B)^2]\`.
Consequently
\`Q^-_{n,1}-Q^-_{n,2}=(1/12)L[D^2]=(1/12)||S^{n-3}D||_2^2\`.

The Laurent polynomial is not zero: direct expansion gives
\`D=6(z_1-z_2)sum_{i=3}^{6}(z_i/(z_1z_2)-z_i^{-1})\`, with a nonzero distinct monomial coefficient; the Laurent polynomial ring has no zero divisors, so \`S^{n-3}D!=0\`. Its sum of squared integer coefficients is strictly positive. QED.

The positive integer contrast, divided by \`36^n\`, is the contrast of the normalized per-port squared masses \`P^-_{n,1}-P^-_{n,*}\`.

## General exchange-symmetric Gram lemma

Let \`d>=2\`, \`S=sum_{i=1}^d z_i\`, \`T=S-z_1\`, \`V_i=S-dz_i\`, and \`A=|V_1|^2, B=|V_2|^2\`. Let \`L\` be any linear Laurent constant-term functional that is invariant under the exchange 1↔2 and for which \`L(F F^*)>=0\` (e.g. \`L(F)=CT(WF)\` with a nonnegative exchange-symmetric torus weight \`W\`). Then
\`L[|T|^2(A-B)]=(1/(2d))L[(A-B)^2]>=0\`.

Proof: expand \`d|T|^2=(d-1)|S|^2+A-d(d-1)\`, cancel the exchange-antisymmetric term, and symmetrize \`L[A(A-B)]\` as above. For \`d=2\`, \`A=B\` identically. For \`d>=3\` and a weight positive almost everywhere, the inequality is strict; the explicitly factored \`A-B\` is then nonzero. This lemma is a purely algebraic Gram observation and does not change the frozen six-axis model.

## Verification, exact scope and reproducibility

The independent local checker \`PREFIX1015_R6_NEGATIVE_PORT_SOS_CHECK.py\` uses native BRC-derived Laurent terminal packets and integer coefficient convolution. It verifies \`6TT^*=5SS^*+A-30\` symbolically and the exact equality \`12(Q^-_{n,1}-Q^-_{n,2})=||S^{n-3}D||_2^2\` for every \`n=5,...,14\`. The four independently checked PREFIX-1014 native BRC terminal-port values at n=5..8 match.

| n | distinguished Q⁻ | each other Q⁻ | strict difference | SOS norm |
|---:|---:|---:|---:|---:|
| 5 | 16,560 | 12,384 | 4,176 | 50,112 |
| 6 | 246,870 | 191,574 | 55,296 | 663,552 |
| 7 | 4,299,380 | 3,455,060 | 844,320 | 10,131,840 |
| 8 | 83,992,020 | 69,575,892 | 14,416,128 | 172,993,536 |

These finite checks support the implementation; the all-length statement follows from the exact Laurent/symmetry proof. The checker performs terminal Gram postprocessing and does not claim a new independent native BRC trajectory, Result, Review or a physical-time interpretation.

**Next scientific question:** determine the sign of \`Q^+_{n,1}-Q^+_{n,*}\` for all n, or construct an exact counterexample, using the existing \`B^+_{n,j}\` Laurent packets and their common eleven marked-collision signatures. Explore whether the present SOS structure admits an exact \`A_6\`-shift expression. The mother question \`B_fix,odd(32) in {19,20}\` stays open.

**Provenance / control:** Existing historical R6 provenance \`EM-DIRECT-FBEA5D\` / Activity \`RA-3FB2D033BE6048D8712FF056\`. Original SID \`MCP-45ad6d29cd534c1aad25595a72e3c532\` still open, but current formal execution authorization not granted in the observed recovery. This mathematical Source publication is independent of a CLAIM/PROGRESS and is not itself an Activity association.
