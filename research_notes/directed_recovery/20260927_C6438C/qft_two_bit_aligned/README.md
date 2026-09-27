# Executed aligned two-bit scalar observer

One declared actual-typed run verified 36 signed residue outputs against 720
ordered pair observations across six finite fixtures. The adapter evaluates
two-bit scalar signs when V=2^ell divides the supplied modulus R. Its production
work was **77,763 digit replays**, exceeding the independent one-pass pair
comparator's **35,531** on these small inputs. The total recorded work across
production, comparator, positive replay, paid input rejection and negative
replay was **255,115 digits**. This is a correctness result with no demonstrated
small-input speed advantage.

The interface is AlignedTwoBitObserver.two_negative(g, ell, k, R, r, stride=1),
with strict integers g>=2, 0<=ell<k<g, R>=1, 0<=r<R and V|R. The signed count
sums (-1)^(bit_ell(x)+bit_k(x)+bit_ell(y)+bit_k(y)) over 0<=x,y<2^g and
y-x congruent r modulo R. The original raw normalization remains 4^-g.
The observer neither discovers R nor computes phase words or full Gram matrices.

The implementation derives the compressed progression data through the actual
typed arithmetic route and calls the frozen direct observer's single-progression
helpers. It retains both orientations, including equal half-modulus heads, and
the original parity sign. Shifted progressions have independently certified
lengths, including the exact empty-overlap A_one(M)=0 boundary. The independent
comparator enumerates pairs once per fixture and fills all residue buckets; it
does not repeat the pair enumeration separately for each residue.

The run rejected twelve invalid inputs: ten before arithmetic and two after
paid nonalignment checks. Two attempts to reuse incomplete observers were also
rejected without changing retained evidence. Twelve certificate negatives
include four early rejections, seven complete fresh failed replays and one paid
partial replay. Incomplete-request reuse rejection is not a resume protocol.
All five cost categories and available failed work remain in the full raw
artifact. One shared native column observation supplied the full-adder kernel;
one core call does not represent the full arithmetic cost.

DESIGN.md is the frozen pre-run design and intentionally retains its original
CODE_ONLY heading. The final summary, execution log, author cost note and
source-specific saved-record review report the subsequent actual run. The
approximately 19.391-second pre-serialization checker duration is not a matched
performance benchmark. Host serialization/bookkeeping is outside the digit
counters. Shared-context review is not formal independent admission.

The next_design structural-shortcut note and its review are unchanged symbolic
successor copies, not implemented routes in this result. They propose a
highest-bit cancellation test, omission of a zero-coefficient shifted sum and
an affine highest-compressed-bit progression formula. The published lattice
unit separately gives a theorem-based polynomial-bit route for fixed two-bit
signs at arbitrary R; its counting backend is not implemented here.

This remains a supplied-modulus scalar component. It does not solve arbitrary
history-dependent matrix correlations, growing signed masks, order/address
acquisition, full sampling or Shor dequantization. The research goal remains
active and P000 is unchanged.

DEPENDENCIES.md gives immutable source-first restoration. The readable evidence
transport restores the complete original gzip, and the delivery ZIP includes
that same original file. CONTINUE.md identifies concrete next work without
treating recorded local paths as research-capability restrictions. Publication
and actual original-byte backup receipts are produced separately after those
actions occur.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
