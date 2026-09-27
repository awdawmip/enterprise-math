# Aligned-progression shared-context symbolic review

Reviewed the complete `next_design/ALIGNED_PROGRESSION.md`, SHA-256
`782c3af4622e24282cbf5e3cbf564128ff02d7c56d5b25e42cc74b93b9acf49f`,
against its pinned `DIFFERENCE_AUTOCORRELATION.md`, SHA-256
`c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.
**No substantive error found in the stated symbolic scope.** No scientific
execution, host numerical experiment, professional query or source modification
was performed. This is shared-context review, not independent admission.

1. If the progression step is a positive multiple of P, its remainder s is
   constant and its quotient is exactly q0+j(a/P). Substitution into the saved
   finite-interval formula A(d)=(H-q)C(s)+e(s) gives (2) by the integer triangular
   sum. Both definitions coincide at s=U. The length formula enforces d<L,
   hence q<H; it does not extrapolate the autocorrelation outside its domain.
   The stipulated empty-branch return prevents evaluating n-1 or an invalid
   head needlessly. Exact division by two is justified by n(n-1).
2. For U|R with P not dividing R, R/U is odd, so P divides 2R. The original
   indices split disjointly as j=2l and j=2l+1. Their counts are ceil(n/2) and
   floor(n/2), respectively, with heads b and b+R. The upper displacement bound
   is inherited by every surviving term. A singleton has no odd branch.
3. At residue zero, heads 0 and R include displacement zero exactly once;
   positive return magnitudes receive two orientations. At r=R/2 the equal
   heads must both remain. For R>=L either orientation is a singleton or empty,
   but both can survive. Two nonzero surviving magnitudes would have sum
   R<=2L-2, proving the stated threshold R>=2L-1. This is an endpoint-counting
   assertion, not a permission to omit a surviving second head.
4. The R|U cancellation uses a genuine label-preserving involution: toggling
   bit k changes x by plus or minus U, remains in the interval of length L,
   preserves its residue, and reverses its sign. Thus each signed residue
   histogram entry is zero. It does not require constructing the histogram.
   R|U is distinct from U|R; their intersection R=U is consistent with the
   half-aligned formula. The smallest g=1 symbolic cases are consistent with
   the two possible displacement magnitudes and the orientation convention.
5. At most four scalar progression evaluations is correct for the complete
   half-aligned query; at most two suffice when P|R. The broader split into
   P/gcd(P,R) classes is not uniformly small. The note correctly keeps this
   distinction, bit costs, typed integer receipts, source checks and paid
   order/address discovery. Nothing here reduces arbitrary masks, full matrix
   correlation growth or the general Shor problem.

Implementation recommendation within this exact scope: preserve each oriented
head and each parity branch in the receipt even when its length is zero; return
the zero contribution before quotient/coefficient evaluation for that branch.
Keep signed C(s), e(s), progression sums and final K. Typed predicate validation
must distinguish the zero case R|U from the alignment case U|R. Do not infer an
execution-cost improvement from zero moment tables; actual scalar digit costs
still require a separately authorized bounded execution. The current note is
ready to retain as a symbolic design without changing the executed direct unit.
