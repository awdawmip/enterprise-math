# Nondecisive mathematical review: exact conditional CRT repair bits

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: both the exact feasible-fiber formula and sharp total-mass bound
follow from the stated old six-cell reconstruction interface. No unresolved
mathematical defect was found. This is not formal Driver admission.

Reviewed file: `nt/crt_repair_bits.md`.
SHA256: `022633656b11b01c644aeae1970b5c25ecb23599bdfd4eacefd53b61b273d213`.
The old source's linear reconstruction and one-statistic result remain
attributed to EM-CRTJC-5F30D8A2, source member SHA256
`74627303f208933fc9632d51c5f5810a098d010f9682410b2ec9045de7d3cfe4`.
This review checks the new counting/coding consequence of that interface.

The four t-dependent entries are nonnegative exactly when
max(0,e-gamma_4)<=t<=min(e,gamma_1). The two constant entries yield the
other two inequalities; total-row/column equality then enforces the second
row total. Thus every integer in the interval corresponds to exactly one
payload. Empty intervals or inconsistent totals are rejected, not encoded
as a valid zero-bit fiber.

Different t are separated by the already available half-open prefix at
h=3: only the cell at k=1 is counted. Hence a code must have at least
C=U-L+1 messages even with nonlinear decoding. The offset t-L attains
ceil(log2 C) fixed-length bits, with the C=1 and unused-codeword conventions
handled correctly.

For the mass-M maximum, w=U-L is bounded independently by gamma_1 and
gamma_4. Therefore 2w<=gamma_1+gamma_4<=M. The proposed family
((0,t,k-t),(r,k-t,t)), k=floor(M/2), r=M-2k, has constant row/column/carry
data and supplies all k+1 values. This proves sharpness for every integer
M>=0, including M=0,1. No erroneous conversion from one rational statistic
to one bit is made.

Validation grade: independent paper reasoning. I did not rerun the author's
18,564-payload enumeration and do not count that author execution as my
independent verification. It is supplemental finite evidence, whereas the
general-M inequality and explicit family provide the proof. No kernel was
used and no old CRT/Hart experiment was rerun.

Reuse resolution: COMPOSE_APPLIED, existing exact CRT observer plus T4
finite-fiber coding. This is a bounded enriched-multiplicity counting
corollary, not a new CRT tool family. Baseline, support and obtaining t are
paid separately; this is neither total storage nor factoring runtime nor
the unweighted QRWheelIndex lower bound. All-prefix preservation is confined
to the exact declared six-cell language.

Shared control/source context is disclosed; reviewer did not author this
construction and is not a clean-blind reviewer. The conditional arithmetic
descriptor does not redefine native X6 geometry. No formal Task or parent
objective is closed by this review.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
