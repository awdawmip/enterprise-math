# PREFIX-616-R2 — Exact positive-realization number is eight, versus signed-linear rank seven

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT PROOF / EXECUTED NATIVE-48-PHASE CHECKER / INDEPENDENT REVIEW PENDING.

Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Current behavioral norms were read separately. Parent scientific dependencies are PREFIX-613, PREFIX-614 and PREFIX-615 (commits 4d276201aec4e8c0dc578d15ac0e0df66c23b47f and d183f7e45d89eed5c74e032172891afa58421402). No P000/worldview modification.

## Problem and exact typed scope

Consider the original typed positive-branch-sum 48-phase native X6 STAR matrix Q(g), with axis weights (1,1,1,1,0,0), g >= 0. The original 96 ports and 576 tagged actions specify upstream provenance. Set d=e4+e11+e14+e32 using original zero-based phase indices; let the first two chronological gates be a,b >= 0. For any later nonnegative gate word q1,...,qt, scalar increment lambda > 0, and original phase-3 **sum** observer h=e3^T, define

    X_t(a,b,q,lambda) = h Q(q_t)...Q(q_1)Q(b)Q(a)(lambda d),    t>=0.

All transition products use the native BRC-derived Q and its exact phase-sum quotient. We ask for the smallest number of states in a *time-homogeneous nonnegative linear realization* of this complete family. Such a realization uses, for every gate g >= 0, a nonnegative real matrix M(g), an initial nonnegative state dependent on (a,b,lambda), and a fixed nonnegative output row, and must agree at every finite future gate word. Its state dimension counts observer-carrier coordinates, not native spatial axes, and does not assert preservation of 96-port tagged-path histories.

PREFIX-614 established that the unrestricted real linear minimum is exactly **seven**, by explicit seven-dimensional reachability and seven-dimensional future observability. PREFIX-615 established the exact simultaneous decomposition

    T(g) ~ diag( 2, R, B(g) ),
    R = [[0,-4],[1,0]],
    B(g) = [[0,0,0,4(g+3)],
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0]],

with initial block coordinates (1, 1, 0, 3+b, 3+a, 1, 1/2), and output row (2,-2,4, 1,0,0,0), scaled by lambda.

## Theorem 616.1 — Seven nonnegative states are impossible for the declared family

For every real gate g,

    tr(T(g)^2) = 2^2 + tr(R^2) + tr(B(g)^2)
               = 4 + (-8) + 0 = -4.

Indeed R^2=-4I2 and B(g) is a weighted directed four-cycle, whose square has zero diagonal.

For every nonnegative real square matrix M, independently of its size,

    tr(M^2) = sum_{i,j} M[i,j] M[j,i] >= 0.

Assume a seven-state nonnegative realization exists for all a,b and all gate words. Because the family has linear Hankel/reachability-observability rank seven (the exact PREFIX-614 certificates), it is also a **minimal** real linear realization. Uniqueness up to an invertible simultaneous change of basis of minimal linear representations of a word-series family forces its gate-0 matrix to be similar to T(0). Trace of the square is similarity-invariant, hence tr(M(0)^2)=-4, contradicting nonnegativity. Thus any nonnegative linear realization of this family needs **at least eight** coordinates.

The minimum-realization uniqueness assertion is specifically for a representation of the *same complete input/output word family*, not for one isolated finite gate program. It follows directly from the usual reachable-state equivalence: map each reachable state word in one representation to the same word in the other; observability makes the map well-defined and invertible, and it intertwines all transition letters. Using 0/1 gate letters suffices since D=Q(1)-Q(0), so the seven independent reachability/observability word-row certificates of PREFIX-614 apply to permitted nonnegative gates.

## Theorem 616.2 — Constructive eight-state nonnegative realization

Let P be the positive four-cycle

    P = [[0,0,0,1],
         [1,0,0,0],
         [0,1,0,0],
         [0,0,1,0]].

Define C=2P, and retain B(g) above. For each g>=0 let

    M8(g)=diag(C,B(g)),

with the nonnegative initial state and nonnegative output row

    u8(a,b,lambda)=lambda*(0,0,4,4, 3+b,3+a,1,1/2)^T,
    h8=(1,0,0,0, 1,0,0,0).

Each M8(g) has exactly eight positive entries (four in C and four in B(g)), and C^4=16 I4. For the baseline first block,

    e0^T C^t (0,0,4,4)^T
       = 16^floor(t/4)*[0,8,16,0]_[t mod 4].

The second block gives, by the positive four-cycle, exactly the gate-dependent term from PREFIX-615:

    e0^T B(q_t)...B(q_1) (3+b,3+a,1,1/2)^T
       = w_[(-t) mod 4] *
         product_{1<=s<=t, s mod4=t mod4} 4(q_s+3),

with w=(3+b,3+a,1,1/2), empty product 1. Adding the two outputs is the exact PREFIX-615 formula for X_t. Therefore h8 M8(q_t)...M8(q_1)u8=X_t for every t>=0 and all declared parameters.

Combining Theorems 616.1 and 616.2:

    MINIMUM NONNEGATIVE LINEAR OBSERVER-STATE COUNT = 8
    MINIMUM UNRESTRICTED REAL LINEAR OBSERVER-STATE COUNT = 7.

The *one-coordinate positive-realization gap* is exact for this specific original BRC phase-3 observer and four-sparse input family. It is not an assertion about reconstructing all 48 phase coordinates with a nonnegative eight-state map, nor about retained tagged-path provenance. The four-cycle C supplies the additional -2 eigenmode missing from the signed 1+2 block's positive representation; the seven-dimensional signed block, taken alone, has an impossible negative trace-square for a positive transition.

## Exact independent reconstruction and validation

The standalone checker PREFIX616_R2_positive_eight_state_checker.py reconstructs all 48 STAR phases, all directed native transitions Q(g), the seven-dimensional E/T0/T1 matrices, their exact seven-dimensional reachability and future-observability determinants, the PREFIX-615 symbolic conjugacy, tr(T(g)^2)=-4, C^4=16I, and the eight-state positive output. It computes the original 48-dimensional Q(b)Q(a)d vector and then iterates each future gate, while separately iterating the seven-state and eight-state models.

Executed 36 distinct (initial two gates / later gate word / increment scale) cases, including zero gates, nonnegative integer and rational gates; checked 444 exact scalar phase-3 outputs and 21,312 exact full48-vs-seven-state coordinate equalities. All assertions passed. The all-length statement follows from the displayed algebraic similarity and four-cycle identities; finite runs are implementation checks, not the universal proof.

Verification assumptions: SymPy exact integers/rationals, source-code STAR/phase generator defined within the checker, original phase sum observer, chronological gate order as stated. No floating-point tolerance, native physical timing inference, or forbidden classical trigonometric approximation was used.

## Research value and next discriminating unit

The gap separates *algebraically minimal* observer coordinates from *nonnegative branch-mass compatible* observer coordinates; only one extra register is necessary in this exact family. The eight-state construction additionally admits a subtraction-free evolution for nonnegative inputs and positive gate programs.

Next: characterize positive-realization dimensions for **other original phase observers** and **complete 48-phase recovery**, checking exact observer maps and future operations one scope at a time. A selected 96-port, provenance-sensitive observer needs its own typed source-to-readout definition before transferring a quotient. Compare native-input preparation, bit lengths, 8-state streaming updates and output reconstruction against 7-state and original 48-phase implementations. Retain reviewer-independent checking and formal Native Result handling on their actual authority route.

Status: independent Driver review, canonical Native Result and Foundation promotion have not occurred for this author-side result.
