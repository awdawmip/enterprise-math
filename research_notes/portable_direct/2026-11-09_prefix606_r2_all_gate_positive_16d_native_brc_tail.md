# PREFIX-606-R2 — Common positive 16-dimensional tail for native X6-BRC

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR-SIDE EXACT PROOF AND EXECUTED INTEGER/RATIONAL CHECKS; INDEPENDENT DRIVER REVIEW PENDING.

Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d. Dependencies: PREFIX-602/604/605 (PR #1826/#1828/#1830). Research subject: the 48-phase observer induced from the fixed native X6-BRC 96-port, 576-tagged-action model at six-axis weights (1,1,1,1,0,0). The gate may vary independently at each step, z_t >= 0. We retain the phase observer and its complete 48 outputs, not arbitrary source-tagged histories.

## Theorem 606.1: an exact common nonnegative realization at the minimum dimension

Let Q(z) be the native-derived 48×48 phase transition defined below. There exist fixed entrywise **nonnegative INTEGER** matrices

E: 48×16, T0,H: 16×16, R00,Ra,Rb: 16×48

such that for ALL real a,b,z >= 0, exactly

    Q(a)Q(b) = E (R00 + a Ra + b Rb);
    Q(z)E    = E (T0 + z H).

For every nonnegative phase input r and every gate sequence (z1,...,zn) with n>=2, define

    u2=(R00 + z2 Ra + z1 Rb) r;
    ut=(T0 + zt H) u[t-1]       for t=3,...,n.

Then ut is entrywise nonnegative, and the complete 48-phase result at each t>=2 is

    Q(zt)...Q(z1) r = E ut.

Thus this is a simultaneous positive input, transfer and output realization, including **arbitrary** first two gate parameters (not only a fixed Q(1)^2 transient). Because rank(Q(1)^2)=16, every linear realization giving all 48-phase outputs for arbitrary initial phase vectors after two steps must have at least 16 coordinates. Hence 16 is minimal.

## Exact native-derived transition

Use the unchanged STAR triads (1,3,6), (1,4,5), (2,3,5), (2,4,6) and the original directed native successor incidence (full enumeration is in the executable checker). The gate target is native phase g=4 in zero-based indexing and g is not its own successor. Rows with outgoing axis 5 or 6 are zero. Other rows have exactly three successors; at row g the three entries are 1, at any other row the target column g receives 3+z if it is a successor, and every other successor receives 2.

Put S=Q(0) and G=Q(1)-S. Exact phase reconstruction gives Q(z)=S+zG, rank(G)=1, G²=0 and rank(Q(1)²)=16. These assertions are checked over exact rationals, not floating-point.

## Sixteen rank-one positive-support rectangles

Let M=Q(1)². Its nonzero support has exactly 144 cells. The 16 explicit 3-by-3 rectangles (zero-based native row indices; zero-based native column indices) are:

| k | rows Rk | columns Ck |
|---:|---|---|
| 0 | 4,5,29 | 32,40,44 |
| 1 | 7,30,31 | 10,18,22 |
| 2 | 25,36,37 | 0,9,33 |
| 3 | 27,38,39 | 2,11,35 |
| 4 | 0,1,13 | 21,36,45 |
| 5 | 24,25,37 | 12,21,45 |
| 6 | 2,3,15 | 23,38,47 |
| 7 | 1,12,13 | 9,24,33 |
| 8 | 17,40,41 | 4,8,20 |
| 9 | 26,27,39 | 14,23,47 |
| 10 | 5,28,29 | 8,16,20 |
| 11 | 16,17,41 | 28,32,44 |
| 12 | 6,7,31 | 34,42,46 |
| 13 | 18,19,43 | 30,34,46 |
| 14 | 19,42,43 | 6,10,22 |
| 15 | 3,14,15 | 11,26,35 |

These rectangles are pairwise disjoint *as matrix cells*; they tile exactly all 144 nonzero cells of M. Each restricted 3×3 matrix has rank one. For each k, choose the smallest column j in Ck and let dk be the integer gcd of the three values M[i,j], i in Rk. Define E[i,k]=M[i,j]/dk for i in Rk, otherwise 0. Every E column has exactly three nonzero positive integer entries. The rank-one rectangles give nonnegative integer coefficient matrix D such that ED=M. Exact rank of E is 16.

Take any exact rational left inverse K satisfying KE=I16. K is ONLY used in the proof and need not be nonnegative. Define the actual implementation matrices

    R00=K S²; Ra=K G S; Rb=K S G;
    T0 =K S E; H =K G E.

The accompanying exact checker verifies ALL FIVE complete matrix identities

    E R00=S²; E Ra=GS; E Rb=SG;
    E T0=SE; E H=GE,

and verifies every entry of R00,Ra,Rb,T0,H is a nonnegative integer. Their numbers of nonzero entries respectively are 48,3,1,16,1. E has 48 nonzero entries. From G²=0, expansion of Q(a)Q(b) establishes the first displayed identity. The second is linearity in z. Induction proves the theorem for all n and all independently varying gates.

## Sparse nonnegative four-cycle coordinate representation

T0 contains exactly the following nonzero entries (zero-based row,column,integer weight):

(0,9,1), (1,4,2), (2,1,2), (3,10,2),
(4,13,2), (5,14,2), (6,11,2), (7,12,2),
(8,15,2), (9,8,2), (10,6,2), (11,3,2),
(12,5,2), (13,2,2), (14,7,2), (15,0,3).

H has exactly one nonzero entry H[15,0]=1. Hence T(z) has exactly one nonzero entry per row and per column for every z>=0. Only the edge (input 0 -> output 15) changes: weight z+3. The permutation decomposes into four 4-cycles. Three have scalar four-step weight 16; the gated cycle has scalar four-step weight 4(z+3) for constant z. This supplies a positive version of PREFIX-604's 12+4 tail decomposition and remains compatible with PREFIX-605 residue-class endpoint statistics.

## Validation and algorithmic value

The runnable self-contained checker reconstructs all native 48 phase indices and Q matrices, checks the 16 rectangles' exact complete support, rank-one property, positive primitive rays, all five identities, integer nonnegativity, and minimal rank. It also checks **1,440 complete original phase-basis output comparisons** for eight mixed exact integer/rational gate words of lengths 2,2,2,2,4,5,8,13 (each checkpoint tests all 48 initial phase basis columns and all 48 observed phase coordinates). All assertions passed.

The all-parameter result is proved by the exact coefficient identities plus induction, while finite gate tests validate execution. The post-loading transition has 16 positive weighted contributions per step, with 48-entry reconstruction from E. An end-to-end complexity comparison should include original 96-port initialization, phase quotient semantics, 16-state input encoding, integer bit length, batches of endpoint readouts and full output recovery. Raw source-label histories may require separate repair coordinates.

Next: connect this positive 16-state kernel to the original 96-port endpoint interface and benchmark against the optimized 96/49/48 implementations, retaining full provenance where required. Native control session creation and owner query were attempted but returned BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false); no active formal CLAIM, Researcher-ID, Native Result, independent Driver review or Foundation admission is asserted.
