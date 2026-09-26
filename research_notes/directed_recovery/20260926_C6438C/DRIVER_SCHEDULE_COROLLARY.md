# Native-word resource bounds for the driver's truncation schedule

Status: AUTHOR_SYMBOLIC_COROLLARY / SHARED_CONTEXT / UNREVIEWED /
NOT_ADMITTED. This is a bounded mathematical connection between the driver's
schedule and the already derived four-square constructor. No target observer,
native word, Shor trajectory, ideal reference, or TV experiment was executed
for this document. No frozen source or artifact was modified.

Researcher EM-DIRECT-C6438C; activity RA-CAAAC604CB513AEA8BBC1DFC.
The earlier compiler/construction package is recorded at Source
`8d4e9c12f7492316b825e96423bc0ee36ccdee22`; the general constructor and direct-word
integration increment is recorded at Source
`9348fc6abdf45becbd12a8019d93f72d576b9fab`.
These are dependency Sources supplied by the parent, not a claim that this
new document has already been published or read back. The scientific Control
Source remains `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`; executable primitive
Source remains `0852cad130c1d877174d235687cf60c19f318c58`. Global control uses the
parent-verified canonical snapshot 8446003, whose three entry files were read
for this review chain.

## 1. Inherited constructive input

For every integer phase index m>=3 and explicit positive rational delta,
`new_word_compiler/CONSTRUCTIVE_FOUR_SQUARE_FRONTIER.md` supplies a complete
61-mode native word W_m. Choose

    B = min{b integer : b>=2 and 2^b > 128/delta^2},
    S = 2^B,                h = B+4.

Its strict, replayable full-carrier certificate gives

    ||W_m-U_m||_op <= ||W_m-U_m||_F < delta,
    E_upper < 84/S < delta^2.

The same proof bounds the finite word resources by

    indexed length <= 10B+124,
    canonical 62-letter length <= 150B+7480,
    H4 count <= 2B.                                      (1)

The canonical letters remain H4 on coordinates 0,1,2,3, a sign on coordinate
0, and the 60 adjacent swaps. Routing introduces no additional H4 or new
primitive coefficient. The exact m2 quarter-turn has no H4 denominator and
needs no approximate compilation. All completion/residual directions remain
part of the same carrier.

Every H4 entry has denominator 2; signs and swaps are integral. Consequently
the entries of W_m have a common denominator dividing 2^(2B). Orthogonality
implies that their integer numerators, when expressed over that denominator,
have magnitude at most 2^(2B). Thus an entry's numerator needs at most 2B+1
binary digits plus a sign. These are bounds on the exact native word, not
numerical rounding or an alteration of the frozen target32/vector64 bank.

## 2. The proposed K(t), delta(t) schedule has explicit finite resources

Let t>=2 be even and set

    K = ceil(2 log2 t),          delta = t^(-2).          (2)

Keep m2 exact, compile m=3,...,K at tolerance delta, and replace m>K by the
identity on the complete 61-mode carrier. This is an explicitly different
truncation schedule, with its own error proof below. Identity replacement
does not project out, reset, or renormalize any residual mode.

We have 2<=K<=t. One purely integer proof of the upper bound is t^2<=2^t
for all even t>=2. It holds at t=2; if it holds at an even t, then
(t+2)^2<=4t^2<=2^(t+2). Taking logarithms gives 2log2t<=t, hence K<=t.
There are exactly K-2 potentially approximate phase types; this number is
zero when t=2.

For every retained phase the same B is sufficient, and

    B = floor(log2(128 t^4))+1
      <= 8+4log2t,             h <= 12+4log2t,
    128 t^4 < S <= 256 t^4.                              (3)

The strict threshold is why equality at a power of two advances to the next
B. The bound in (3) is on B itself, not on 2^B. In particular (1) gives

    indexed length <= 204+40log2t,
    canonical length <= 8680+600log2t,
    H4 count <= 16+8log2t.                               (4)

At any streaming round, a history-dependent feedback word uses at most one
copy of each retained phase type (or its inverse), plus the integral exact
quarter-turn. Hence its common denominator divides 2^J, where

    J <= 2B(K-2) = O((log t)^2).                         (5)

It is again an orthogonal full-carrier matrix, so its entry numerators over
that denominator have at most J+1 magnitude bits. The estimate is independent
of the selected history and work-register modular order.

For completeness, define the total retained approximate occurrence count

    L(t,K) = sum_(m=3..K)(t-m+1)
           = (K-2)(2t-K-1)/2.

An unnormalized complete history, started at an integral basis state and
implemented with the inherited two H4 control/spectator operations per round,
has a common denominator exponent bounded by

    2t + 2B L(t,K) <= 2t+2Bt(K-2).                       (6)

Modular permutations add no denominator. Projection to a recorded branch
does not add one either, and no square-root normalization is performed.
The state norm is at most one, so every retained scalar numerator over this
common denominator is bounded in magnitude by the denominator. This controls
exact amplitude bit size; it does not bound the number of work labels or
histories that must be stored or processed. In particular, it is not a
polynomial-time factoring claim.

The construction's integer deficit, here denoted D_def to distinguish it
from the cutoff K, satisfies 0<=D_def<5S=O(t^4). The implemented pair search
examines at most (R+1)(R+2)/2=O(D_def+1) pairs, where R=floor(sqrt(D_def)).
Its square table observes the integer comparisons defining R without
evaluating a numerical square root. Across O(log t) phase types this gives
O(t^4 log t) pair-observer steps for a completing run with adequate budgets.
This is a count of these arithmetic observations; it does not include
repeated cursor replay, or establish a total wall-clock/bit-complexity bound.

## 3. A pi-free full-carrier tail bound

Use the inherited positive algebraic branch

    q_2=1,
    q_(m-1) q_m^2 + 2q_m - q_(m-1)=0.

For m>=3 the defining equation gives 2q_m<q_(m-1), because both q values
are positive. Thus, by induction,

    0<q_m<2^(2-m).

For U_m=[[c,s],[-s,c]] direct-sum I_59, with
c=(1-q_m^2)/(1+q_m^2) and s=2q_m/(1+q_m^2), direct symbolic algebra yields

    ||U_m-I||_op^2 = (c-1)^2+s^2
                  = 4q_m^2/(1+q_m^2).

Consequently

    ||U_m-I||_op < 2q_m < 2^(3-m).                       (7)

This argument requires no value of pi and no trigonometric or square-root
evaluator in an executor. It is an inequality between exact proof objects.

Phase m occurs t-m+1 times. Telescoping the complete orthogonal products
and then applying the inherited terminal-instrument contraction gives

    TV(P_actual,P_ideal)
      <= E_local+E_tail,
    E_local <= t(K-2)delta,
    E_tail < 8t*2^(-K)        if K<t,
    E_tail = 0               if K=t.                    (8)

The tail estimate follows by extending the positive geometric sum in (7)
to infinity. It holds on the entire carrier, including arbitrary residual
input. For the standard prepared Shor input the ideal control marginal is
the standard ideal law; no such law is numerically executed here.

Substituting (2), and using 2^K>=t^2, gives the sufficient bound

    TV <= min(1,(K+6)/t) = O(log t/t).                    (9)

Thus the original driver's asymptotic schedule now has explicit native word,
denominator and amplitude-bit bounds. Equation (9) is a symbolic upper bound,
not an observed TV value or a claim that every term in it is sharp.

This convergence alone does not prove a positive uniform CF success rate.
The inherited ideal guarantee at default width t=2n is at least
1/(8n)=1/(4t), not a constant. Subtracting the much larger sufficient error
bound in (9) gives no positive guarantee. This failure of that estimate is
not proof that the actual CF algorithm fails; a stronger accuracy schedule
is needed to derive the desired quantitative success bound.

## 4. A finite schedule for any requested rational epsilon

Let epsilon>0 be rational. Select the first integer K in {2,...,t} for which

    16t <= epsilon*2^K;                                  (10)

if no such integer exists, set K=t. Set

    M = max(1,K-2),       delta = epsilon/(2tM).          (11)

These are exact finite integer/rational decisions. They need no logarithm
evaluator. Compile m=3,...,K using (1) with this delta, keep m2 exact, and
use full-carrier identity for higher indices.

If K<t, (10) and (8) give E_tail<=epsilon/2. If K=t the tail is zero,
regardless of whether (10) was ever satisfied. At all K,

    E_local <= t(K-2)delta <= epsilon/2.

Therefore the single-terminal distribution satisfies

    TV(P_actual,P_ideal) <= min(1,epsilon).               (12)

The general constructor terminates at each retained m and positive rational
delta when provided sufficient finite resources. Its B is the least integer
at least two with 2^B>128/delta^2; the same word and denominator bounds apply.
Equations (10)-(12) are valid also for K=2: there are no approximate words,
and their budget allocation is vacuous. They also cover small widths at
which the safe choice is to retain every phase.

## 5. Recovering the factor-success budget

Take n=ceil(log2 N), t=2n and

    epsilon = 1/(8t) = 1/(16n).                          (13)

For a node with at least two distinct odd prime factors, after the existing
exact even/perfect-power/prime preprocessing, the inherited original-CF/gcd
theorem gives ideal attempt success at least 1/(4t). The uniform bound (12)
therefore gives actual success at least

    1/(4t)-1/(8t) = 1/(8t) = 1/(16n).                   (14)

As in `new_word_compiler/STRONG_SHOR_COMPILATION_THEOREM.md`, the stochastic
statement requires fresh conditionally uniform legal bases and readouts.
The order remains a proof quantity, never a compiler or executor input.
At most 8t*s=16n*s attempts make retry failure at most 2^(-s); recursive
splits require the existing per-node allocation and product/prime/partial
ledger. Random-source interruption and compilation interruption remain
explicit incomplete outcomes, not prime certificates or discarded failures.

For (13), cutoff (10) is equivalently the first 2^K>=128t^2, or K=t if
none exists. At sufficiently large t it retains only O(log t) phase types;
delta=1/[16t^2 max(1,K-2)]. Thus B=O(log t+log log t), and per-feedback
denominator exponent remains O((log t)^2). This is a constructive resource
bound for the phase layer, not a change in the remaining simulator costs.

Single-terminal TV in (12) is not whole-retry-transcript TV. A requested
transcript error requires its own sum of conditional per-attempt budgets.
The retry-failure bound is a separate probability statement.

## 6. Implemented evidence and the remaining scheduling optimization

The general single-phase four-square constructor and its strict full-column
verifier have actual bounded execution evidence. The frozen fair full-bank
compiler and its streaming/full-factorization interfaces also have actual
bounded evidence. The direct new words have separately been imported into
the complete circuit and streaming instrument at the stated t4 fixtures.
None of those facts is relabelled here as execution of (2) or (10)-(11).

The nonuniform truncated-bank automatic allocator described in this corollary
has not yet been implemented or executed. Integrating it would avoid compiling
provably unnecessary high-index phases and would use the existing direct
constructor for the retained ones. It is an optimization/explicit composition
of established finite components; the already implemented full-bank fair
compiler remains the general finite-termination baseline.

The independently constructed words for different m have not been proved
to share a common native root or to commute with each other. In particular,
the Stage89/90 W4-power merging identities, or scheduling optimizations that
require such commutation, cannot be imported automatically into this word
family. No commutator experiment was performed here. The norm telescoping
argument and the inherited step-by-step full-carrier streaming schedule do
not require these additional identities: they preserve the specified order
of actual factors and retain the original controlled-label dependencies.

This document closes the mathematical word-resource question for the stated
schedules under the inherited native-linear and exact quadratic-observer
contract. It neither reports a TV measurement nor establishes independent
admission, physical Born-law derivation, efficient classical factoring, or
zero-error equality with every ideal phase.

Global-Knowledge-Sync: main@8446003 / GLOBAL_KNOWLEDGE_V1
