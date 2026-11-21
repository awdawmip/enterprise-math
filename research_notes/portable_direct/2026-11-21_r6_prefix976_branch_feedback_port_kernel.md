# PREFIX-976 — Branch-feedback XOR port kernel and exact same-port return classification

Date: 2026-11-21 · Author route: independent portable auxiliary research, `EM-DIRECT-FBEA5D` / `RA-3FB2D033BE6048D8712FF056` (historical session registration verified; this note does not assert a formal CLAIM).
Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Depends on previously recorded PREFIX-973–975 signed source-mask definitions.

## Precise model
For integer p>=3 and integer residual c in D_p={2^i-s 2^j:0<=i,j<p, s∈{+1,-1}}, define static masks P_c (plus labels) and M_c (minus labels), with bit j set iff the indicated i exists. For x a p-bit integer define S_c^+(x)=P_c & ~x and S_c^-(x)=M_c & x, truncated to p bits, and V_c(x)=S_c^+(x)|S_c^-(x). Port labels encode distinct named sources.

This note defines a separate **positive BRC path observer**, not an asserted native X6 rotation: starting at x and residual c, choose a valid source port j; flip that same source bit, x'=x XOR 2^j; observe a second residual C at a port J. All sources and transitions are labelled. On the odd-input subpopulation restrict j,J to A={1,...,p-1}, so all flips preserve parity.

For any fixed nonnegative integer port kernel K_{jJ} (zero outside A), define
M_fb(c,C,x;K)=sum_{j,J∈A} V_c(x)_j K_{jJ} V_C(x XOR 2^j)_J.
Define M_fr by replacing V_C(x XOR 2^j)_J with V_C(x)_J.

## Theorem 976.1 — exact feedback-correction law
Write D_C=P_C XOR M_C, U=V_c(x), V=V_C(x). Then **for every p,c,C,x and K**
M_fb=M_fr + sum_{j∈A} U_j K_{jj} (D_C)_j [1-2V_j].

Proof: PREFIX-974/975's affine identity gives V_C(x XOR 2^j)=V_C(x) XOR ((P_C XOR M_C)&2^j). Thus only the second-stage port J=j changes; toggling a Boolean bit v changes its numeric indicator by 1-2v. Multiplying by the first valid-port indicator and the kernel proves the formula, with no independence assumption. In particular **K_{jj}=0 for all j gives exact two-step frozen factorization** even under branch-dependent flips. This is an exact horizon-2 result, not a multi-step marginal independence assertion.

With signed ports and nonnegative fixed K^{sigma,tau}_{jJ}, where sigma,tau each belong to {+,-}, the same proof yields:
M_fb^signed=M_fr^signed + sum_{j,sigma,tau} S_c^sigma(x)_j K^{sigma,tau}_{jj} A_C^tau(j) [1-2 S_C^tau(x)_j],
where A_C^+(j)=P_C(j), A_C^-(j)=M_C(j). Distinct labelled signs, including j where P and M overlap, are preserved. The signed statement was separately checked against literal two-stage enumeration.

## Theorem 976.2 — diagonal closed form
For K_{jJ}=[j=J] and any allowed set A,
M_fb(c,C,x;I)=popcount(P_c & M_C & ~x & A)+popcount(M_c & P_C & x & A).

Proof: if x_j=0, first-stage validity can only use the plus sign P_c(j), while after the toggle second-stage validity can only use the minus sign M_C(j). If x_j=1, the reverse holds. Counting the two disjoint classes gives the formula. In particular for C=c, M_fb(c,c,x;I)=popcount(P_c & M_c & A), independent of x.

## Theorem 976.3 — complete same-port return classification
For all p>=3, P_c and M_c share a port j iff c=3*2^j with 0<=j<=p-3. The two named sources are (i=j+2,j,s=+1) and (i=j+1,j,s=-1). Proof: both signs at the same j require 2^u-2^j=2^v+2^j; hence 2^u-2^v=2^{j+1}. Since 2^v(2^{u-v}-1) is a power of two, u=v+1, v=j+1, u=j+2. The converse is immediate.

Consequently, for any odd x, odd-preserving j>=1 and C=c, **there is exactly one same-port two-stage feedback path iff c=3*2^j for some 1<=j<=p-3; otherwise there are zero**. For p=19 the number of such distinct residuals is 16; over the 2^18 odd x values the positive total across these self-residual paths is 16*2^18=4,194,304.

## Exact obstruction
At p=19, x=1, c=C=0 and K diagonal on A={1,...,18}: the frozen same-port observer gives 18, but the feedback observer gives 0. Under K_{jJ}=[j!=J] both give 306. The discrepancy comes entirely from the joint branch/port relation and cannot be repaired by storing only independent marginal masses.

## Exact reproducibility
`PREFIX976_R6_COMPACT_CHECK.py` independently builds all P/M dictionaries from the integer source definition, directly enumerates j-dependent flips and checks the correction and diagonal laws. Exhaustive all-residual odd-x self-return tests p=4..8: 16,312 states. Cross-residual checks: all c,C,x for p=4..6 and deterministic explicitly selected residuals for p=7..8: 428,808 triples. Each triple checks diagonal and a nonzero off-diagonal weight kernel against direct enumeration. A separate local extended verifier checked 18,642 signed-kernel triples; see full local reproduction bundle. p=19 result is analytic and checked against the constructed D_19 dictionary and explicit x=1 example; no exhaustive 2^18*499^2 loop is claimed.

The path observer is a precisely declared auxiliary positive-weight construction in the pinned odd-core XOR study. Its output is neither the original two-core witness count (previously 1,903) nor a native Heartbeat trajectory, and it makes no signed/phase cancellation claim.

## Continuation
Classify the actual *reachable* residual changes under a declared native or task-authorized BRC transition kernel, then compute the minimal future-query source-coordinate support under that kernel. For h>=3 retain a joint path/incidence carrier or prove an exact sufficient-statistic descent; Theorem 976.1 alone covers a single source-selected flip and a second port query. Compare construction, storage, update and source recovery costs before claiming an algorithmic speedup. Preserve the shared X6 owner/CLAIM boundary and prior research provenance. Mother question B_fix,odd(32)∈{19,20} remains open.
