# R5: primitive-43 pole-depth separation at the first seven cancellation thresholds

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_EXACT_FINITE_FIELD_CERTIFIED / FINITE_THRESHOLD_THEOREM / NOT_REVIEWED**. Independent portable continuation; no formal Task CLAIM/RUN/Result/Review or P000 promotion.

Frozen scientific input: \`awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`. Corrected five-event scalar observer, prices 214,...,314, multiplicities nonnegative, observer failure threshold \`m\` as in the pinned input. This note studies the **next degree of the coefficient quasipolynomial**, not a native X6 heartbeat observer.

## Theorem (new finite-threshold depth distinction)

Write \`F_m(q)=R_m(q)/D(q)\`, where \`D(q)=prod_{p=214}^{314}(1-q^p)\` and \`R_m(q)\` is the exact integer-polynomial numerator for the union of the five failure events. Let \`zeta\` be a primitive complex 43rd root of unity. For each of the **seven individual integer thresholds**
\[
m\in\{37,38,39,40,41,42,43\},
\]
one has
\[
\boxed{ R_m(\zeta)=0,\qquad (\zeta\,dR_m/dq)(\zeta)\ne0. }
\]
The first equation is the exact all-threshold primitive-43 cancellation theorem at \`enterprise-math@c9329abecc9963667647a2774b351a33c0456b0a\`; the second is **new**, established by the finite-field characteristic-zero witness below.

Among the 101 denominator prices, precisely 215, 258 and 301 are divisible by 43. Therefore \`D\` has a zero of order exactly 3 at every primitive 43rd root, while \`R_m\` at each of these seven thresholds has a zero of order exactly 1. Accordingly \`F_m\` has a **pole of order exactly 2** at every primitive 43rd root.

If \`M_m^{(r)}\` denotes the least common coefficient period of terms of degree at least \`r\` in the quasipolynomial in the total price \`N\`, then for these seven thresholds
\[
\boxed{43\nmid M_m^{(2)},\qquad v_{43}(M_m^{(1)})=1.}
\]
This is a genuine observer-resolution distinction: 43 disappears from the degree-\(\ge2\) period when terms \`O_m(N)\` are discarded, but remains visible in the linear-in-\`N\` coefficient. The \`43\nmid M_m^{(2)}\` part uses the pinned exact root-43 argument (including exclusion of higher 43-multiple orders); \`43\mid M_m^{(1)}\` follows from the new surviving order-2 pole. The exponent is exactly one because the universal denominator period is a divisor of \`L=229746052653717600\`, whose 43-adic valuation is one.

**Scope:** the seven thresholds above are proved, not every \`m\equiv37,...,42,0\pmod{43}\`. The existing eight-regime minimal period theorem concerns \`M_m^{(2)}\` and remains at its prior author-derived/NOT_REVIEWED status; this note does not change or repin it.

## Exact independent finite-field certificate

The supplied \`VERIFY_D43_FIRSTJET.py\` computes with dual numbers over four finite fields:
\[
 \mathbb F_p[\varepsilon]/(\varepsilon^2),\qquad
 q\mapsto z(1+\varepsilon),\qquad q^a\mapsto z^a(1+a\varepsilon).
\]
The \(\varepsilon\)-coefficient is precisely the **Euler** derivative \(\dot R_m(z)=zR'_m(z)\), not an unscaled ordinary derivative.

Each pair \`(p,z)\` below has \`p\` prime and \`z\ne1\`, \`z^43=1\` in \`\mathbb F_p\`. As 43 is prime, \`z\` has exact order 43.

| \`m\` | \`p=1033,z=995\` | \`p=1291,z=341\` | \`p=1549,z=104\` | \`p=1721,z=1393\` |
|---:|---:|---:|---:|---:|
| 37 | 842 | 126 | 832 | 836 |
| 38 | 963 | 20 | 57 | 458 |
| 39 | 265 | 1099 | 528 | 883 |
| 40 | 140 | 114 | 646 | 1561 |
| 41 | 538 | 195 | 938 | 947 |
| 42 | 589 | 418 | 366 | 1531 |
| 43 | 393 | 417 | 627 | 1532 |

All 28 zero-order values \`R_m(z)\` are zero modulo \`p\`; all 28 Euler first jets shown above are **nonzero**. Even one prime would be sufficient to establish the nonvanishing in characteristic zero. Indeed, if the integer polynomial \`\dot R_m(q)\` vanished at one complex primitive 43rd root, divisibility by \`\Phi_{43}(q)\` in \`\mathbb Z[q]\` would force vanishing on reduction at *every* primitive 43rd root of unity over \`\mathbb F_p\`, contradicting the witness.

### Complete calculation, with the overlap retained

Write \`A_m\` for the union of E0,E1,E2, and \`B_m,C_m\` for the two disjoint one-block events E3,E4. Since the variable supports of \`A,B,C\` are pairwise disjoint,
\[
R_m=1-(1-A_m)(1-B_m)(1-C_m).
\]
For the first three events, with \`x=a214,y=a215,j=a219+a220+a221\` and shared load \`u=a216+a217+a218\`,
\[
\min(s_0,s_1,s_2)=u+x+y+j-\max(x,y,j).
\]
Decompose the remaining triple by all six descending-coordinate orders, breaking ties by ascending price labels. For each permutation \`(a,b,c)\` of \`(214,215,r)\`, \`r\in\{219,220,221\}\`, let \`delta1=[a>b]\`, \`delta2=[b>c]\`. Then the corresponding cone series is exactly
\[
\frac{a_*^{\delta_1}(a_*b_*t)^{\delta_2}}
{(1-a_*)(1-a_*b_*t)(1-a_*b_*c_*t^2)}
\]
before multiplication by the common numerator. The code algebraically cancels the \`1-a_*\` factor of \`D_U\` **before** specializing at the order-43 root, crucial because \`q^{215}=1\` there. The three equal-count weights are expanded by the exact Lagrange coefficients
\[
\beta_r(q)=\prod_{r'\ne r,\;r'\in\{219,220,221\}}(1-q^{r'-r})^{-1}.
\]
The remaining series factors are \`(1-t)^-1\`, \`\prod_{v=216}^{218}(1-q^v t)^-1\`, \`(1-q^{a+b}t)^-1\`, and \`(1-q^{a+b+c}t^2)^-1\`. This is the exact joint six-cone rational identity, expanded only through \`t^42\`.

For the two separate blocks, the implementation uses the **correct total-item threshold numerator**
\[
\sum_{m\ge1}B_m(q)t^{m-1}
=\frac{D_{223..290}(q)}{(1-t)\prod_{p=223}^{290}(1-q^p t)},\quad
\sum_{m\ge1}C_m(q)t^{m-1}
=\frac{D_{296..312}(q)}{(1-t)\prod_{p=296}^{312}(1-q^p t)}.
\]
It does **not** use the previously invalid replacement \`\prod_p(1-q^{mp})\`. The test also checks \`\dot C_{37}(z)=-43\cdot301\pmod p\`, an independently derived exact S4 plateau identity, and compares the cone answer with **direct seven-mask inclusion/exclusion** at m=1,2,3 for all four primes. All those tests passed.

Rational series and the six-cone identity are algebraic identities over the localized rational function ring, with the only inverses at primitive order 43 coming from \`1-z^{r'-r}\` (nonzero). Thus the finite-field computation represents the exact reduction of the **integer-polynomial** numerator and its Euler derivative. No floating-point or probabilistic evaluation is involved.

## Validation and source pins

- \`python3 VERIFY_D43_FIRSTJET.py\`: \`ALL CHECKS PASS: 28/28 first jets nonzero; literal overlap m=1,2,3 checked at four primes\`.
- \`RESULTS.txt\`: complete 28-value finite-field output.
- Original scalar model pinned: \`enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`.
- All-threshold characteristic-zero \`R_m(zeta43)=0\` on the seven residue classes: \`enterprise-math@c9329abecc9963667647a2774b351a33c0456b0a:research_notes/portable_direct/r5_root43_allthreshold_phase_20261122/RESEARCH.md\`.
- New six-cone proof and corrected S4 transfer: \`enterprise-math@f696e325a2829f80c9a7d1c225e1a0c8219698a3:research_notes/portable_direct/r5_independent_pole_envelope_20261123/RESEARCH.md\`.
- This is exact modular nonvanishing evidence and an author-side mathematical derivation; no independent Driver review, native CLAIM or P000 modification.

## Next discriminating question

Determine the primitive-43 Euler-jet sequence \`\dot R_{r+43h}(\zeta43)\` for \`r=37,...,43\`, \`h\ge0\`. Its algebraic/quasipolynomial evolution could either extend this degree-1 survival to entire infinite residue classes or expose explicit higher-threshold jet cancellations. Keep the higher-degree \`M_m^{(2)}\` classification, native X6 state and any BRC readout distinct until a source- and observer-preserving transfer is proved.
