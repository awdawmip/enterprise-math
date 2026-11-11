# R729 — Named-S3 BRC fiber rational laws and exact observer-rank contrast

Date: 2026-11-12 (Asia/Shanghai). Author-side scientific continuation by Researcher-ID \`EM-X6-03F93F\`, RA \`RA-D8CCA602C77A202AAA753A0A\`. Parent task \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen scientific pin \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Exact predecessor R728: \`69579fbe3fa934b25554bafb80e16545013c9964\`. R725: \`a9ba60cab51fc98e4b39f73e5d0eda7f49c51bb3\`.

## 1. Carrier, paths, and observations

Within P000's **six native spatial axes** select five accessible labels \`01234\` for a *derived combinatorial carrier* (not a distinct five-dimensional native world). Vertices are all ten unordered triples. A directed arc replaces exactly one label. The R725/R728 two 15-arc sharp representative masks, in the original lexicographic 60-arc ordering, are \`A=211733226574\`, \`B=5363347296468\`.

Root at active triad \`012\` with ordered frame \`012\`. Each arc replaces the departing axis by the entering one **in the same slot**, giving an ordered final frame in \`{012,021,102,120,201,210}\`. Positive source-distinct histories retain path ordering and multiplicity. Require cyclic nonbacktracking, including the first/last seam. Let \`a_m^{X}(h)\` denote the number of rooted legal histories of length \`m\` on \`X=A,B\` with final frame \`h\`. Set counts at lengths 0,1,2 to zero and

\[
F_{X,h}(x)=\sum_{m\ge1}a_m^{X}(h)x^m\in\mathbf Z[[x]].
\]

The six exact individual generating functions, with *unreduced common denominators*, are provided **in full** as ascending-order integer coefficient arrays \`rational_numerators[h]\` / \`common_denominator\` in the adjacent \`R729_NAMED_S3_FIBER_RESULTS.json\`. The accompanying complete standalone Node.js verifier generates those arrays by exact \`BigInt\` operations.

## 2. All-length rationality with exact integer certificate

Use R728's candidate character denominator factors, written in ascending coefficient order:

\[
\begin{aligned}
D_{0,A}&=1-3x^3-7x^4-8x^5-4x^6,\\
D_{s,A}&=1+x^3+x^4-2x^5,\\
D_{2,A}&=1-2x^3+2x^5+2x^6-x^7-3x^8-x^9+3x^{10}+2x^{11},\\
D_{0,B}&=1-3x^3-7x^4-8x^5-5x^6-x^7,\\
D_{s,B}&=1+x^3+x^4-2x^5-x^6+x^7,\\
D_{2,B}&=1-2x^3+2x^5+3x^6-x^7-3x^8-2x^9+2x^{10}+4x^{11}+2x^{12}-x^{13}-x^{14}.
\end{aligned}
\]

Define \`Q_X=D_{0,X}D_{s,X}D_{2,X}^2\`. Degrees: \`deg Q_A=33\` and \`deg Q_B=42\`.

Let \`L_X\` be the 90×90 nonnegative integer operator on (current directed arc, current ordered-frame permutation) with transitions along adjacent arcs that do not immediately reverse, applying the V17 slot replacement permutation. For a root first arc \`f\`, its initial basis vector is \`v_f\`. For each final named state \`h\`, let \`w_{f,h}\` select states whose last arc enters \`012\`, whose incoming tail differs from the head of \`f\`, and whose terminal frame is \`h\`. This last criterion enforces cyclic nonbacktracking at the seam. Then the exact path count is

\[
a_m^{X}(h)=\sum_{f:\,\operatorname{tail}(f)=012} w_{f,h}^{\mathsf T}L_X^{m-1}v_f,\qquad m\ge1.
\]

For \`Q_X(x)=\sum_{j=0}^{d}q_jx^j\`, put \`R_X(t)=t^dQ_X(1/t)\`. The standalone verifier explicitly checks every one of the 90 input basis vectors, i.e. **all 8100 integer entries**, obtaining the exact matrix-polynomial identities

\[
\boxed{L_A^5R_A(L_A)=0_{90\times90}},\qquad
\boxed{L_B^3R_B(L_B)=0_{90\times90}}.
\]

The shift is sharp for these polynomials: \`L_A^4R_A(L_A)\` has 144 nonzero entries and \`L_B^2R_B(L_B)\` has 120 nonzero entries. These are exact integer results.

For any such count sequence, the coefficient of \`x^m\` in \`Q_X F_{X,h}\` is \`\sum_{j=0}^{d} q_j a_{m-j}^{X}(h)\`. For \`m\ge d+\ell+1\`, this equals a matrix coefficient of \`L_X^{m-d-1}R_X(L_X)\`, and vanishes by the checked operator identity, where \`(\ell_A,\ell_B)=(5,3)\`.

Next compute the finite initial counts through \`d+\ell\`, obtaining zero numerator coefficients in degrees \`d+1,\ldots,d+\ell\` for **each of the six h values**. Hence

\[
\boxed{F_{X,h}(x)=P_{X,h}(x)/Q_X(x),\qquad\deg P_{X,h}\le\deg Q_X}
\]

holds for **all integer lengths**. The exact P arrays are fully serialized in the JSON; the verifier additionally cross-checks subsequent coefficients through length 82. Unlike a numeric fit, the proof rests on a finite exhaustively checked operator identity plus finite initial data.

## 3. New named-slot contrast laws

Exact polynomial cancellation of the numerator arrays produces

\[
\boxed{F_{A,120}=F_{A,201}}\quad\text{(all lengths)},
\]

\[
\boxed{F_{B,201}-F_{B,120}=\frac{x^5(x+2)}{D_{2,B}}},
\qquad
\boxed{F_{A,102}-F_{A,210}=\frac{x^3}{D_{2,A}}}.
\]

All are formal generating-function identities over the integers. In particular, type A has *equal counts* for the two named three-cycles at every length, whereas type B has a nontrivial named three-cycle contrast. This is a BRC source-count distinction and makes no claim of physical chirality.

A compact, concrete witness is **length 8**. Both networks have exactly the same coarse conjugacy-class totals, \`identity=15\`, \`all transpositions=50\`, \`both three-cycles=32\`, \`total=97\`, but their ordered six named-count tuples differ:

| Carrier | 012 | 021 | 102 | 120 | 201 | 210 |
|---|---:|---:|---:|---:|---:|---:|
| A | 15 | 16 | 16 | 16 | 16 | 18 |
| B | 15 | 16 | 18 | 14 | 18 | 16 |

This demonstrates exact loss of future-relevant named-slot information when six counts are replaced by their three class aggregates.

## 4. Exact linear observer rank

Treat the six infinite named-count sequences \`m↦a_m^{X}(h)\`, \`m\ge3\`, as elements of the rational vector space of sequences, and restrict any reconstruction coefficients to be **fixed across lengths**.

For A, the all-length relation \`F_{120}=F_{201}\` implies dimension at most five. The 5×5 integer submatrix with row names \`(012,021,102,120,210)\` and columns \`m=(3,4,5,6,7)\` has **determinant -2**. Therefore its dimension is exactly five.

For B, the full 6×6 integer submatrix with row names \`(012,021,102,120,201,210)\` and columns \`m=(3,4,5,6,7,8)\` has **determinant -7**. Therefore its dimension is six.

\[
\boxed{\operatorname{rank}_{\mathbf Q}\{a^{A}(h)\}_h=5,\quad
       \operatorname{rank}_{\mathbf Q}\{a^{B}(h)\}_h=6}.
\]

These are observer-specific *constant-coefficient sequence-span ranks*, not a general Markov-state minimization, information-bit requirement or native physics result.

## 5. Reproduction and evidence scope

Run \`node R729_NAMED_S3_FIBER_VERIFY.js > R729_NAMED_S3_FIBER_RESULTS.json\` with a Node.js version supporting \`BigInt\`. No external packages. The program independently reconstructs all 60 candidate arcs, selects both 15-arc networks, checks the entire 90-state polynomial identities, computes counts and all twelve numerator arrays by exact integers, and verifies the contrast polynomial identities and Bareiss rank determinants. It also independently enumerates actual ordered-string-frame histories for lengths 3–7 and compares all six named counts with its 90-state DP. The result is \`status=PASS\` and the exact operator, rank and count evidence is serialized.

Historical context: R728, R725 and frozen P000; the present author ran an independent Python exact-integer prototype as a local cross-check and reproduced the same 8100-entry operator certificates, minors and length-8 named counts before the JavaScript GitHub publication. Neither method claims formal Source Result nor independent review.

### Open scientific unit

Map a selected optimal 15-arc network and its root-closed histories into **actual** V29 Link/Port inventory, signed native-axis directions, Cell identities, per-port event ledger and ordered event times. Construct typed execution witnesses where legal; retain sharply identified obstructions otherwise. Recompute the six named series on the actual executable transition relation and test the observer-rank distinction under V29. Also compute the subdominant named-character spectral radii and certified asymptotic convergence constants.

P000, the six-axis ontology, the original frozen scientific pin and independent review/promotion gates remain unchanged.
