# Nondecisive review: OAI7-090 finite-checker coverage

Reviewer: EM-REVIEW-58D6A2; activity RA-BALANCE-REVIEW-20261028-58D6A2.
Author audit: `native/round2/OAI090_FINITE_COVERAGE_AUDIT.md`, SHA256
`974eed99cd05fd51a06f95cd572b7255f3835398d9b6a289d6d29c114e9739ce`.
Coverage map: `native/round2/OAI090_PROOF_COVERAGE.json`, SHA256
`5e6508bbb19604411e15817c9a8aa4737064f89592d54014a0f667ecc0c8d5cc`.
Finding: no mismatch or mathematical defect found within the declared
static coverage and local analytic-premise scope. This is not a review of
the full universal-optimality proof or a new verification execution.

I read all 389 lines of the exact original checker, its pinned source
metadata, the complete audit and coverage map, and the corresponding
TeX wave, jet-map, finite-system, parameter-polytope, finite-certificate,
jet-monotonicity and appendix evaluation sections. Original repository
openai/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a; checker blob
23768a5c2d88e100399bb5c4347447e86a7160cb; TeX blob
dad316cc2ad861a7482d79b46b6f840ed83d2a5e. I did not claim to read the
whole 103614-byte TeX paper or establish its remaining infinite arguments.

## Static code and finite lemma

The five lemma groups have corresponding code: two inverse/pivot/norm
systems; node and midpoint bounds; four jet envelopes plus repetition and
omitted targets; five raw curvature evaluations and divided Taylor tails;
ordinary and exceptional polynomial lower bounds. The (N,S,k,v) assignments
match. Code R is a residue list and code A in approx is the paper's R;
conflating these would give an incorrect correspondence.

The finite dimensions follow the actual lists and slices: M is 16 by 22,
W is 16 by 2, SL is 20 by 22, SC is 20 by 1, R is 20 by 20, R0 is 20 by 3,
Yf is 20 by 8 and each Ai is 23 by 8. The plus/minus solves and half-sum
recombination reproduce the paper's coupled equations. This checks the
fixed data shapes; zip is not a general shape validator.

The Taylor row recurrence begins at derivative order two and divides by
successive k+3, as required for divided remainders. Its degree-20 omitted
term is derivative order 23 with subsequent ratio bounded by |y|d/24.
All 14 signed half-cells have a side-two test. The one exceptional
side-one right half-cell is replaced by four degree-at-most-22 tests;
the other 13 retain the ordinary test. Thus 27*21+4*23=659 is a structural
Bernstein-row count, not an observed runtime event count.

The substitutions at z=0,Z, row shifts by tau/tau^2, constants added to
column two and the w correction in column four match the four exceptional
polynomials and ordinary corrections. The 11 assert sites, 30 lt sites,
four near sites and six sqrt call families are syntactic source counts;
helper invocation multiplicities are not being inferred from them.

## Local analytic premises

Fixed-grid addition, multiplication and reciprocal formulas enclose exact
values; reciprocal endpoint reversal is also correct on negative intervals.
Clipped sqrt needs an external nonnegative-argument premise. Each of its
six fixed call families has one: a sum of squares, positive constant,
positive X, or v^2+(4/3-2kv)X with 4/3-2kv>=2813/3750>0.
The reduced exponential Taylor remainder is below 2/61!<10^-60;
the ten squarings preserve enclosure. The Machin identity and alternating
tail bound remain mathematical inputs, separately from the pi assertion.
Diagonal elimination preserves the exact already reduced unit columns,
so the optimized slice updates correctly enclose the exact inverse.

For the four damping choices the rational endpoint differences kX-v
are precisely the four positive fractions displayed in the audit. The
logarithmic derivative of the nondamping jet factor is at most 1/X.
The exact rational gaps 3k-(k^2+25/36)/(4/3) are positive for both k.
Thus the whole jet envelope decreases with X and increases with t on
[0,5/6] for n>=1. This justifies right-endpoint domination of each
continuous frequency interval when the separately inherited W variation
bound is valid; no mesh inference is involved.

Actual Gaussian coordinates lie in the polytope conditional on the stated
finite scalar inequalities: exponentials increase with z and Delta has
the unique interior maximum sqrt(1+2Z)-1. The exact row minimum splits
into box terms and the triangle (a,u) with three stated vertices. It is
code vmin exactly. Interval dependence can widen its result but cannot
invalidate the lower enclosure. The Bernstein basis then makes the bound
uniform in tau and the entire polytope. The l1 coefficient norm uses
convexity in the first two columns and safe independent bounds on the rest.

## Execution boundary and remaining obligations

I did not run, import, instrument or reproduce the original checker.
The earlier author's run remains UNBOUND_EXECUTION_EVIDENCE with
NO_RETROACTIVE_AUTHORIZATION, as recorded in the separate incident file.
Its exit-zero receipt is not a current Task grant or completion and this
paper review neither repairs nor retroactively authorizes that run.

My conclusion is a conditional code/paper correspondence and proof of
the expressly local premises. I have not independently recomputed the
strict numerical tables. Spectral variation identities, infinite Schur
correction, frequency curvature extrema, all-radius signs and transfer
to energy retain the audit's stated unreviewed scope. The next curvature
extremum obligation is legitimate but is not silently taken on here.

This is reuse/verification of known external mathematics with zero new
theorems and zero new mathematical tool families. I contributed no text
or construction to the frozen audit. Shared source/control exposure is
disclosed: nonauthor NONBLIND review, no clean-blind claim, no formal
Driver decision, original Task completion, canonical admission or native
plane/clock bridge.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
