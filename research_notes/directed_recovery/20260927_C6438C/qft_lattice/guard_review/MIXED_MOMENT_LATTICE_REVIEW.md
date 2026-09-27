# Shared-context review of the lattice reduction

Reviewed source: `MIXED_MOMENT_LATTICE_REDUCTION.md`, SHA-256
`d051e709c1e3751ba10a38206265ee90f2ad4bf1114e325888f64be15e259b57`.
Verdict: **no substantive error found in the stated symbolic reductions or
their fixed-parameter complexity consequence**. This is shared-context
mathematical review, not formal independent admission. No scientific arithmetic,
host numerical example, backend invocation or experiment was performed.

## Floor graph and box lift

For integer j in the closed range 0 through n-1, each constraint with width
P-1 (respectively p-1) selects exactly the Euclidean quotient a (respectively
c). Division boundaries therefore have one representative, rather than two.
The inputs make both integer quotients nonnegative. Fractional points in the
relaxation need not have nonnegative a or c, which causes no problem: only
integer fibers are counted. Each real quotient is still bounded because its
affine numerator and positive denominator are bounded.

At an integer base point, u independent intervals of length j, alpha of
length a, and beta of length c contain precisely the required product number
of integer auxiliary tuples. Positive exponent at base zero gives an empty
fiber; exponent zero introduces no coordinate, including the 0^0 convention
appropriate to a monomial. Thus the lift counts the weighted sum without
enumerating its base points. Empty, lower-dimensional and n=1 cases are
allowed; n=0 is correctly removed beforehand.

The six base inequalities plus twice the total degree give at most sixteen
inequalities in at most eight coordinates. Coefficients use only a fixed
number of binary input additions and small constants. The entire description
has polynomial (indeed linear up to fixed conventions) encoding size in the
listed input lengths. The count bound in the source has logarithm O(B), so
there is no exponentially long output hidden in the assertion. The signed
combination of finitely many moments also has polynomial bit length.

## Primary theorem actually checked

I browsed the primary [Barvinok–Woods v1 paper](https://arxiv.org/pdf/math/0211146v1),
specifically Theorem 3.1 on printed page 11, Theorem 2.6 on printed page 9,
and the all-ones evaluation remark on printed page 10. The first supplies a
polynomial-time short generating function for fixed dimension, with a fixed
number of denominator factors. The latter permits specialization at a regular
point even if the displayed fractions individually have poles. A finite
lattice set has a Laurent polynomial regular at all ones, so the required
count follows. The paper refers the complete proof of Theorem 3.1 to BP99;
I have not separately read that earlier proof. This is a theorem-statement
and application check, not an implementation audit of a counting algorithm.
The separate `READING_EVIDENCE.json` was also read: it accurately limits the
root author's reading scope, distinguishes the displayed version from the
retrieval URL, and does not claim a local PDF-byte hash or full-paper review.

The source correctly keeps dimension fixed and does not claim small practical
constants. Its complexity parameter is g plus the supplied modulus bit length,
not log(g): explicitly writing 2^g already takes g+1 bits. No divisibility of
the two moduli is required for this counting reduction. The old degree-three
single-floor evaluator does not thereby acquire a new callable capability.

## Fixed sparse-mask pair reduction

For each bit assignment, a permitted integer pair has the unique integer
z=(x-y-r)/R and unique quotients in the intervals specifying the chosen bits.
Conversely the displayed constraints give precisely that pair and assignment.
The selected-bit intervals are disjoint and cover every residue within their
period, including both endpoints. The inequalities bounding x and y bound z
because R is positive; each quotient is bounded as well. Thus every assignment
defines a bounded rational polytope, not an unbounded counting oracle.

The 4^h assignments partition pairs and the stated sign restores their exact
weights. For h=2, sixteen six-dimensional counts suffice for arbitrary R.
R=1 and R larger than the overlap interval do not alter uniqueness. This pair
formulation uses x-y congruent r, whereas the inherited difference note uses
y-x congruent r. Swapping x and y preserves both the rectangular domain and
w(x)w(y), so the scalar results agree. This equivalence should not be silently
assumed for an unrelated asymmetric matrix weight.
The final source now states this symmetry qualification explicitly.

For fixed h, the number of polytopes, dimensions and sign summands are fixed;
their coefficients and outputs have polynomial length. If h grows, the
displayed construction has 4^h summands and increasing dimension. The note
correctly draws neither a polynomial bound nor a lower bound in that regime.

## Research scope

Both reductions are valid abstract algorithms through an established external
theorem. Neither is an executed actual-typed BRC backend. No lattice count,
resource certificate, practical speedup or native arithmetic mapping has been
demonstrated by writing the inequalities. The intended future implementation
still must pay and certify its primitive operations and output representation.

The supplied R and residue do not include free order finding or target-address
recovery. The scalar Walsh signs do not encode arbitrary chronological matrix
products, and a fast individual coefficient does not by itself bound the
number of Gram queries or implement the full output sampler. The source keeps
these distinctions, original 4^-g scaling and orientation multiplicity intact.
No edit is required to support its stated conclusion.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
