# R5 — Complete exact four-arc classification: non-diagonal couplings need at least five edges

Date: 2026-11-11 (Asia/Shanghai). This strengthens the earlier PR #2011 diagonal 4/5/6 constructions and the companion non-diagonal 5/6 theorem in this PR. Scientific pins **unchanged**: GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`, EM \`86149263e38c22292c9def1e0f69092efa1be77e\`.

## Theorem

In the frozen seven-likelihood-ratio P/Q–BRC **auxiliary Blackwell observer**, with the original **30 allowed arcs**, **five physical affine equalities**, **26 physical capacity inequalities**, and **21 Blackwell marginal/martingale equations**:

> Every physically lawful nonnegative coupling supported on at most **four positive arcs** is **diagonal** (every positive arc has \(i=j\)).

Equivalently, any feasible coupling containing a **positive non-diagonal** arc must have **at least five positive arcs**. This is a global statement over the model's entire physical feasible set, not an assertion about a particular seven-edge face or one interpolation path.

The previously verified exact diagonal four-edge example (PR #2011) attains global minimum support four. The companion construction of this PR attains five with positive non-diagonal arcs \((1,3),(5,3)\), so the five-edge non-diagonal threshold is **sharp**.

## Complete finite proof: 27,405 sets / 1,045 exact rational separation certificates

The allowed arc set, as in the frozen original operator, is

\[
D=\{(i,j):j\in\{0,1,2,3,5,6\},\quad 0\leq i\leq6,\quad j\in\{0,6\}\Rightarrow i=j\},
\]

of size 30. The seven distinct likelihood ratios are

\[
(r_0,\ldots,r_6)=(1/10,1/2,3/4,1,5/4,3/2,19/10).
\]

There are \(\binom{30}{4}=27,405\) four-arc subsets.

**Step 1 (exact moment filter).** For each source column \(j\), its Blackwell martingale row is

\[
\sum_{i:(i,j)\in S}(r_i-r_j)e_{ij}=0,\qquad e_{ij}\ge0.
\]

A positive off-diagonal arc at source \(j\) must be accompanied by at least one arc to a strictly smaller ratio and one arc to a strictly larger ratio (diagonal arcs have zero moment). For any candidate set \(S\) that fails this necessary sign condition, its **positive support** cannot equal \(S\). The attached checker identifies 26,345 four-arc sets with a non-diagonal arc failing that condition. Another 15 sets contain diagonals only. The remaining **1,045** sets are exactly all non-diagonal four-arc sets that pass the necessary sign condition: 405 with two off-diagonal arcs, 324 with three, and 316 with four.

**Step 2 (exact Farkas certificates for every remaining set).** Fix such a set \(S\) of four arcs. Let \(p\in\mathbb R^{18}\) consist of 14 original source/target physical variables and four arc weights, constrained by the **original** affine relations:

\[
A_{\mathrm{eq}}p=b_{\mathrm{eq}}
\]

with 5 physical rows and 21 original Blackwell rows; and

\[
A_{\mathrm{ub}}p\le b_{\mathrm{ub}}
\]

with the 26 original capacity inequalities plus four arc-weight nonnegativity inequalities. No artificial bounds on the physical parameters are introduced.

For each of the 1,045 cases, the executable checker constructs exact rational vectors \(y\in\mathbb Q^{26}\), \(z\in\mathbb Q^{30}_{\ge0}\) such that

\[
\boxed{
A_{\mathrm{eq}}^\mathsf Ty+A_{\mathrm{ub}}^\mathsf Tz=0,\qquad
b_{\mathrm{eq}}^\mathsf Ty+b_{\mathrm{ub}}^\mathsf Tz=-1.
}
\]

These are complete Farkas infeasibility certificates. Indeed, multiplying a hypothetical feasible \(p\) gives

\[
0=y^\mathsf TA_{\mathrm{eq}}p+z^\mathsf TA_{\mathrm{ub}}p
\le y^\mathsf Tb_{\mathrm{eq}}+z^\mathsf Tb_{\mathrm{ub}}=-1,
\]

a contradiction. Every equality, sign constraint, and the \(-1\) normalization is checked in **exact SymPy rationals**.

The numerical SciPy/HiGHS solver is used solely to *discover a sparse candidate dual support*. The proposed support is re-solved with exact rationals; only exactly verified certificates count as proved. The checker raises an error if any one of the 1,045 certificate reconstructions, exact equalities, signs, or coverage counts fails. Thus no floating-point infeasibility status is used in the theorem.

**Step 3 (supports of size below four).** Any hypothetical positive non-diagonal support with \(k<4\) can be padded with \(4-k\) additional **zero-weight diagonal** arcs from the original six diagonal arcs. Its exact non-diagonal moment balance is unchanged, so the resulting four-arc set lies among the 1,045 checked cases; the same Farkas contradiction applies. This completes the theorem for support size \(\le4\).

## Reproducible evidence

The standalone \`VERIFY_NONDIA_4_NO_GO.py\` contains the full exact frozen mass, clock, physical capacity, 21-row coupling and 30-arc definitions, the complete \`itertools.combinations(D,4)\` enumeration and a checked rational Farkas certificate for each remaining support. It records a SHA256 digest of the ordered reconstructed sparse rational certificate stream for trace comparison, not as a substitute for certificate checking.

Actual local execution of this verifier produced:

\`\`\`text
TOTAL_ALLOWED_ARCS 30
FOUR_SUPPORT_SUBSETS 27405
DIAGONAL_ONLY 15
MOMENT_EXCLUDED_EXACT 26345
EXACT_RATIONAL_FARKAS_CERTIFICATES 1045
OFFDIAGONAL_2_3_4_COUNTS 405 324 316
MAX_NONZERO_CERTIFICATE_TERMS 19
CERTIFICATE_TRACE_SHA256 abc45fa6ea76aafe693bffde837a0e89cfb3e2693088c9e311612369b696cdb3
PASS_GLOBAL_NO_NONDIAGONAL_SUPPORT_OF_SIZE_AT_MOST_FOUR_IN_FROZEN_R5
\`\`\`

\`EXACT_OUTPUT_4_NO_GO.txt\` is the unedited program stdout. Certificate trace digests may depend on the solver's chosen equivalent sparse dual supports; the **mathematical validation criterion is the exact Farkas equalities, nonnegativity, and exhaustive coverage**.

## Scientific meaning and next action

The global sharp threshold is now established: **4-edge physically lawful couplings may exist, but every one is diagonal; positive non-diagonal branches first become possible at five edges.** The companion two-parameter construction realizes 5/6 non-diagonal strata with minimality from target support occupancy.

A further useful step is to classify *all* feasible non-diagonal five-arc support patterns, determine which have unique transfers, and compare their port-resolved structure with the old E7 family. The status remains an **author-side mathematical proof with an executed exact rational finite checker**; independent review and formal Source Result admission remain separate.