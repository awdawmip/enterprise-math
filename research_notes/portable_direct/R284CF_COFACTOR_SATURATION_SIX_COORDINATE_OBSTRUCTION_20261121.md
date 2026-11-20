# R284CF — A six-coordinate saturation theorem for the frozen 34-bit Port observer

Date: 2026-11-21 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**.

Portable, non-CLAIM research continuation of R284CE; frozen scientific model from R284BZ and R284CD retained. This note studies the precise information lost by the *continuous interval relaxation* used to bound a discrete determinant observer. It does not change P000, a shared Task, or another owner's lease.

## Exact observer and question

Let each entry of the unknown matrix \(C\) initially belong to \(\{1,2\}\), and define
\[
M(C)=\operatorname{diag}(1120832,6,13,1651128)-C
 -390139E_{01}-394465E_{02}-1497639E_{03},
\quad p=17179869143,\quad F(C)=\det M(C)\bmod p.
\]
Indices are zero-based. For a partial assignment \(J\subseteq\{0,\ldots,3\}^2\), relax each *unfixed* entry to the real interval \([1,2]\). Denote the resulting rectangular connected domain by \(Q_J\). The **single-interval relaxation** is
\[
I_J=[\min_{C\in Q_J}\det M(C),\max_{C\in Q_J}\det M(C)].
\]
Its circular projection is \(I_J\bmod p\). This relaxation deliberately forgets the binary fibers within the interval; no statement about the set of actual discrete codewords follows from interval saturation alone.

## Theorem (sharp six-coordinate saturation threshold)

Let
\[
S=\{C_{10},C_{11},C_{12},C_{20},C_{21},C_{22}\}.
\]
Then:

1. **Universal five-coordinate obstruction.** For **every** choice of at most five fixed entries anywhere in the 16 matrix positions, and **every** assignment of the fixed entries to 1 or 2, the unwrapped determinant range has length at least
\[
L=2494802255689>145p>p.
\]
Consequently \(I_J\bmod p\) is the entire circle. Such a real-interval pruning oracle rejects no modular observation, even with measurement error zero.

2. **Six-coordinate sufficiency.** Fix exactly the six entries in \(S\). For all 64 binary assignments, the determinant interval is the arc of R284CE, with exact width between
\[
307592214\quad\text{and}\quad450181375,
\]
strictly below \(p/2\). Thus the circular interval is a proper arc and carries useful pruning information.

3. **Uniqueness at the minimal coordinate count.** Among all six-element coordinate sets from the 16 matrix entries, \(S\) is the unique set whose continuous single-interval projection can be a proper subset of the modulus circle. Any different six-set leaves a member of \(S\) free and is saturated for every assignment. The minimal number of fixed *raw matrix entries* for this particular relaxation is exactly six.

These quantifiers concern raw-coordinate fixing, the fixed 34-bit observer and real-interval pruning. Nonlinear modular tests, correlations, signed/branch-aware carriers or other codes may distinguish candidates much earlier.

## Exact cofactor lemma

Write \(H_{ij}(C)=\operatorname{cof}_{ij}(M(C))\). The determinant is affine in \(C_{ij}\), with
\[
\det M(C_{ij}=1)-\det M(C_{ij}=2)=H_{ij}(C),
\]
and the right side is independent of \(C_{ij}\). Each \(H_{ij}\) is the signed determinant of a 3-by-3 matrix. As a function of its nine remaining input entries, it is multi-affine; its minimum over the nine-dimensional real cube is therefore attained at one of the \(2^9=512\) binary vertices. Exact integer enumeration gives:

| Free coordinate | Minimum cofactor | Maximum cofactor |
|---|---:|---:|
| \(C_{10}\) | 7,737,204,318,762 | 9,032,740,246,754 |
| \(C_{11}\) | 19,054,272,660,842 | 21,556,277,470,645 |
| \(C_{12}\) | 2,494,802,255,689 | 4,989,621,589,776 |
| \(C_{20}\) | 3,249,430,052,052 | 4,544,941,207,681 |
| \(C_{21}\) | 2,501,945,035,417 | 5,003,907,149,232 |
| \(C_{22}\) | 6,114,158,305,212 | 8,608,990,448,094 |

All six cofactor minima exceed \(p\). These are exact global bounds over the full real cube, using only nine relevant variables for each cofactor.

**Proof of the theorem.** If at most five coordinates are fixed, the pigeonhole principle leaves some \(C_{ij}\in S\) free. Choose arbitrary allowed values for every other unfixed coordinate. Varying just this coordinate continuously from 1 to 2 produces an interval of determinant values of length \(H_{ij}\ge L>p\). The image of the connected full cube under the continuous scalar determinant is an interval containing it, so the interval projects surjectively to the circle of circumference \(p\). This proves (1). R284CE's strict M-matrix monotonicity shows that, after \(S\) is fixed, the endpoints are obtained by putting the remaining ten entries all equal to 2 and all equal to 1. The companion checker evaluates all 64 exact endpoint widths, yielding the bounds in (2). Any six-set different from \(S\) leaves at least one of these six coordinates free; apply (1)'s argument without the at-most-five restriction to prove (3). QED.

## Reproducibility and provenance

- The companion standalone standard-library Python script enumerates **3,072 exact signed-minor values**, using \(6\cdot2^9\) 3-by-3 determinant evaluations, and checks all six lower/upper cofactor bounds. Multi-affinity promotes these finite extrema to the full real nine-cubes.
- The same script checks all 64 six-coordinate group widths and independently regenerates the **65,536 binary codewords**, verifying the original frozen codeword SHA-256 \`b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4\`, uniqueness and exact circular minimum gap 59. Arithmetic is signed unbounded integer throughout.
- The finite checker supports the stated cofactor extremum and frozen-code identities; the universal quantifier over arbitrary partial assignments follows from the mathematical argument above, not by enumerating all coordinate subsets.
- Prior frozen results: R284BZ (34-bit gap-59 encoding), R284CD (coordinate arc frontier), R284CE (M-matrix endpoint and indexless arc construction). The present result is an additional obstruction lemma, not independent admission or review.

Scientific artifacts:
- \`research_notes/portable_direct/R284CF_cofactor_saturation_checker.py\`
- \`research_notes/portable_direct/R284CF_cofactor_saturation_verification.json\`

## Consequence and next research unit

The R284CE zero-persisted-arc decoder **cannot** prune a five-or-fewer-coordinate prefix using only one unwrapped monotone determinant interval reduced modulo \(p\): that relaxation is already the entire circle. An adaptive decoder must retain modular fiber/branch information (for example unions of discrete-residue intervals, cofactor-conditioned congruence classes or typed BRC residual carriers) if it wants to inspect fewer than all 64 coarse keys before the sixth critical coordinate is resolved. This is a concrete observer-fidelity boundary, not a native P000/X6 theorem.

Next experiment: construct a **discrete-fiber-preserving modular pruning bound** for partially assigned critical coordinates, compare its exact coverage and worst-case search against the 64-group baseline, and account for representation plus preprocessing costs. A separate open problem is a 33-bit-or-smaller code retaining gap 59.

Activity semantic linkage: pending verification of this runtime's own Researcher/Activity authorization; existing historical contribution identity is provenance, not a transferred live capability. Formal CLAIM not established. Independent Review: NOT_REVIEWED.
