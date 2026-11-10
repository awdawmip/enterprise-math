# R5: Exact lawful nine-edge Blackwell minimum and four-dimensional local sheet

Date: 2026-11-10 Asia/Shanghai. Author-side rational proof and local verification. Frozen scientific sources unchanged: GK a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Predecessor [PR #1966](https://github.com/awdawmip/enterprise-math/pull/1966), exact head d2d5eeea6bb6ac95dcca34d3218eeeffe56ad889.

## Theorem

In the original frozen seven-likelihood-ratio P/Q–BRC auxiliary Blackwell transport model, an explicitly rational lawful source/target pair has **minimum positive transport support exactly nine**. In the chosen eight-dimensional auxiliary physical parameter family, a nonempty relatively open **four-dimensional affine sheet** around this point has minimum support nine and the same locally unique nine-edge support.

This result concerns the statistical transport observer. P000 native six-dimensional space, independent time and frozen model are unchanged.

## Exact parameter and transport construction

Reuse the predecessor's exact rational physical centre, z11 parameter, 15-row transport matrix C, right-hand-side Jacobian T, full 21-row model, 30 allowed edges, 11-column rank-11 matrix M11 and the **ordered** five basis vectors of the kernel K of its physical annihilator G. The predecessor checker prints all these objects and the original 11 positive weights.

Define the unique 11-by-5 matrix W from M11 W = T K. Write

\[
a=(1/100,\;1/100,\;-1/100,\;-1/100,\;0),
\quad
\tau=\frac{32588385367342445179133179624463329}{10293597568004590105855689746100000000},
\]

\[
z_9=z_{11}+K(a+\tau e_4).
\]

Here e4 is the **fifth** coordinate vector of the five-dimensional auxiliary tangent parameter, numbered from zero. The value of tau is the exact solution of the equation making transport edge (0,1) have zero mass. At this point source-column 1 has zero mass and edge (2,1) vanishes as well.

The remaining strictly positive nine edges are

\[
E_9=\{(0,0),(2,2),(3,3),(4,3),(4,5),
(5,5),(6,5),(6,6),(0,3)\}.
\]

All nine exact weights are printed in the program output. Five original physical equalities, all 26 inequalities and the **complete 21 original Blackwell equations** hold exactly. The only zero physical capacity slack indices are 4,6,15,19,23; the other 21 slacks are positive.

## Exact lower bound and uniqueness certificate

The predecessor contains eight complete, explicit dual vectors y_e associated with

\[
F_8=\{(0,0),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6)\}.
\]

The new checker revalidates for **each** e in F8 and **all 30 columns** f,

\[
y_e^\mathsf{T}C_f\leq {\bf 1}_{f=e},
\qquad y_e^\mathsf{T}q(z_9)>0.
\]

Every nonnegative feasible transport therefore contains all eight named edges. The rank-eight forced-edge matrix C_F8 has a seven-row exact left annihilator L8, and L8 q(z9) is nonzero. The eight forced edges alone cannot reproduce q(z9); hence at least nine are needed. The explicit positive nine-edge solution attains the bound.

For additional completeness, the exact checker exhausts **all 22 remaining one-extra-arc candidates**, finding that only (0,3) satisfies rank([L8 C_f | L8 q]) = rank(L8 C_f). Thus this is the unique nine-edge support at the new point.

## Four-dimensional local stratum

The nine-column matrix has rank nine. Its exact left-nullspace basis N9 obeys rank(N9 T)=4. Therefore the affine eight-parameter locus whose observations lie in the nine-edge column span has dimension 8-4=4.

All five vanishing physical slacks have **identically zero derivatives along this four-dimensional kernel**; the 21 other physical slacks and all nine transport masses are positive at the centre. An open relative neighborhood of this four-dimensional sheet stays physically legal and supports the nine positive edges. The eight strict forcing dual bounds persist there, while all other 21 singleton quotient spans remain excluded by finite closedness and the exact centre exclusions. Therefore the minimum nine and its support are locally stable.

## Reproduction and provenance

The code file VERIFY_9.py embeds the [immutable predecessor checker](https://github.com/awdawmip/enterprise-math/blob/d2d5eeea6bb6ac95dcca34d3218eeeffe56ad889/research_notes/brc_r5_exact_11edge_5d_20261110_t1450/VERIFY_11.py) and appends the new tests. It is self-contained with Python 3 and SymPy:

    python research_notes/brc_r5_exact_nine_edge_20261110_t1543/VERIFY_9.py

The nine-edge proof was independently **executed locally** using Python Fraction/SymPy in a separate reconstruction of the same frozen exact matrices. EXACT_OUTPUT_9.txt records the actual resulting certificate lines. The combined published code was assembled from the exact immutable predecessor blob plus the new extension; the separate local output is not presented as a byte-identical execution of the combined file.

A bounded floating-point LP was used **only to discover** a candidate. The rational tau and all final physical feasibility, 21 equations, eight dual inequalities, 22 exact singleton exclusions and four-dimensional rank are validated in exact arithmetic.

Research status: independently reproducible **author-side** mathematics; the formal R5 owner/CLAIM, native Result admission and independent mathematical review are pending. Canonical dispatch instead selected RS-X6-TRIADIC-CLOSURE-DYNAMICS; R5 direct lookup returned NO_CURRENT_IMMUTABLE_PUBLICATION. No shared task owner or protected worldview was changed.

## Next mathematical question

Determine whether a legal eight-edge support arises on the newly identified four-dimensional sheet or its adjacent physical boundary. A candidate requires full original-21-equation verification, and a minimum-eight result requires new strict forcing or exact exhaustive quotient certificates. Continue classifying the intervening 7–10-edge strata between the global three-edge family and the 11–15-edge constructions.
