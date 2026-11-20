# X6 R62 — Exact truncated-star moment lattice, sharp Port-count threshold and precision certificate

Date: 2026-11-20 (Asia/Shanghai). Line: RS-X6-NATIVE-TIME-DYNAMICS. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## Scientific source and scope

This note directly continues X6 R61, `research_notes/portable_direct/2026-11-20_x6_r61_repeated_source_star_degree_tomography.md`, read at current GitHub blob `9a595e5b1869a005655fbb6b00ba734669ccaaf5`. Its input is the explicitly conditional positive BRC model of R60–R61, with a known Port set of size p, p by p binary successful-branch incidence S, Port-independent positive weights u,v, independently reset trials, and a cross-trial predicate requiring all A Ports to be identical. The row success-degree histogram c_d is supported in {0,...,D}, with 1<=D<=p and sum_d c_d=p. The normalized t-star observation is m_t = Z_star(t)/(uv)^t = sum_d c_d d^t; m_0=p is a known integer, not a physical zero-trial event.

Frozen P000 scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; native 6D+time, Cell/Link provenance, whole-triad `TRIADIC_CLOSURE_E` and original research admission remain unchanged. This theorem is a discrete counting result for the conditional observer, not a native admission claim. It preserves the full incidence S for all later incidence-sensitive operations; c is only an observer-specific projection.

## R62.1 Complete integer solution from only D-1 nonzero star depths

Suppose m_0,m_1,...,m_{D-1} are known exactly. Define signed first-kind Stirling numbers s(j,t), with s(0,0)=1 and s(j,t)=s(j-1,t-1)-(j-1)s(j-1,t). Define the integer binomial moments

B_j = (1/j!) sum_{t=0}^j s(j,t)m_t = sum_{d=j}^D binom(d,j)c_d,   0<=j<D.

The generating polynomial G(z)=sum_{d=0}^D c_d z^d satisfies

G(z) = sum_{j=0}^{D-1} B_j(z-1)^j + a(z-1)^D,

where a=c_D is an *integer*. Hence the entire exact candidate set is

c_k(a)=c_k(0)+(-1)^(D-k) binom(D,k) a,  0<=k<=D,

c_k(0)=sum_{j=k}^{D-1} (-1)^(j-k)binom(j,k)B_j for k<D, and c_D(0)=0.

The admissible values a are precisely those integers for which a>=0 and all c_k(a)>=0 (the sum is automatically p). This is a contiguous integer interval [L,U] intersected with [0,p]: each constraint is a one-sided linear inequality in a. In particular the first D star observables are sufficient for **a particular measured instance** iff that interval contains exactly one integer, even where a uniform D-1-depth guarantee fails. The formula computes all alternative histograms rather than merely giving a no-go label.

Proof: the falling-factorial/binomial identity gives B_j, and Taylor expansion of G about z=1 has coefficient B_j. Its only unknown coefficient through degree D is B_D=c_D=a. Expansion in z gives the displayed integer family; nonnegativity is both necessary and sufficient. Every nonnegative histogram with sum p and degrees at most D is realized by a p-by-p success table, by filling exactly c_d rows with d ones each; D<=p is the feasibility condition.

## R62.2 Sharp global phase transition for omitting the final moment

For all integers D>=1 and p>=D, the map
(c_0,...,c_D) -> (m_0,...,m_{D-1})

is injective on all nonnegative histograms of total size p **if and only if**

p < 2^(D-1).

Proof: if c and c' have the same first D moments, their difference h lies in the one-dimensional rational kernel of the D by (D+1) Vandermonde matrix (j^t) for 0<=t<D. The exact integer generator of the kernel is

h_j = a (-1)^(D-j) binom(D,j),  0<=j<=D,

because the Dth finite-difference identity annihilates all polynomials of degree <D; the kernel has dimension one and h_D=a belongs to Z. For nonzero a the sum of the positive entries of h and the sum of magnitudes of negative entries are both |a|2^(D-1). Two nonnegative histograms c,c' with total p can therefore differ only if p>=|a|2^(D-1)>=2^(D-1).

Conversely at p>=2^(D-1), take the even- and odd-index binomial histograms c^even_j=binom(D,j) for even j, and c^odd_j=binom(D,j) for odd j, padded in each with p-2^(D-1) degree-zero rows. They give the same m_t for 0<=t<D but different m_D, and are realizable by p by p tables because p>=D. Thus the threshold is both necessary and sufficient. The case D=1 has threshold p>=1 and correctly says that m_0 alone never identifies the degree-0/degree-1 histogram.

This closes the precise converse left open in R61: its bound p>=2^(D-1) is not merely a range supporting witnesses, but the exact first Port-count at which omission of depth D can ever produce histogram ambiguity.

## R62.3 Exact additional measurement precision after an exact prefix

For any two feasible candidates with the same exact prefix m_0,...,m_{D-1}, their final moments obey

m_D(a)-m_D(a') = D!(a-a').

Indeed F_D=sum_{t=0}^D s(D,t)m_t = D! c_D, and s(D,D)=1. Consequently a further measured normalized depth-D moment y_D with certified absolute error <=eta selects at most one candidate for every instance when 2 eta < D!. The bound is uniformly *sharp* on the ambiguous regime p>=max(D,2^(D-1)): the even/odd witnesses differ in depth-D moment by exactly D!, and their midpoint is compatible with both at eta=D!/2. If the exact prefix already has a singleton feasible interval, no depth-D observation is needed.

This is a conditional precision statement: earlier normalized moments and u,v are exact. If earlier measurements are noisy, round-to-integer reconstruction is uniformly valid for |error_t|<1/2 independently for all t=1,...,D-1; thereafter the same interval/candidate classification applies. For D>=2 this 1/2 bound is best possible as a uniform exact-integer-rounding guarantee (histograms with one degree-0 vs degree-1 row have a unit moment gap), but it need not be the optimal joint-noise decision radius for each concrete instance. Raw mass errors scale by (uv)^t, so the required normalization precision must be propagated per depth rather than treated as a common untyped scalar.

## Example and resource interpretation

For D=4,p=8, the two histograms c^even=(1,0,6,0,1) and c^odd=(0,4,0,4,0) have common prefix (m_0,m_1,m_2,m_3)=(8,16,40,112). The complete integer candidate interval is a in {0,1}; the depth-four moments are respectively 352 and 328. Thus a depth-four read accurate to eta<12 distinguishes them, versus the generic <1/2 precision bound needed when every earlier moment is itself rounded separately. If D=4 and p=4,...,7, the first three star depths already identify any feasible histogram (with exact prefix), saving the fourth star observer and its four AB trials. These are observation-target resource savings; they do not collapse the underlying directed Cell/Link incidence network.

## Exact check, scope and next question

Companions: `research_notes/portable_direct/x6_r62_moment_lattice_verify.js`, `research_notes/portable_direct/x6_r62_moment_lattice_results.json`. The Node.js BigInt checker exhausts **17,089** histograms for D=1,...,6 and D<=p<=min(9,D+4), checks the exact candidate interval and reconstructs every histogram, and checks all 10 even/odd finite-difference witnesses for D=1,...,10. All assertions pass. Finite enumeration is author reproduction, not an independent theorem review. The general claims are proved above by polynomial and integer lattice reasoning.

Next: quantify optimum joint error radius when several lower moments are noisy rather than rounded separately; identify minimal-cost non-star Port-equality motifs that recover R60's otherwise invisible Cell/Link incidence residual. For native TRIADIC_CLOSURE_E, first exhibit or refute a trace-preserving whole-triad Cell/Link/Port reset-and-equality map. No autonomous primitive two-force balance is introduced.

Control provenance: historical Researcher EM-X6-214D9C and Activity RA-545183ADD4EF71C3E4698AEE; continuation request r2-20261120-2312-x6-current-cont-observe-v1 returned SUCCEEDED. As of 2026-11-20T15:14:23Z, owner=taskbook/unassigned, execution_authorized=false, typed predecessor continuation required; task Source changed after read admission and protected operations require reauthorization. This portable scientific publication is not a CLAIM, native PROGRESS, review or Foundation promotion. Activity association must use actual current session and permitted CAS path, not provenance labels alone.
