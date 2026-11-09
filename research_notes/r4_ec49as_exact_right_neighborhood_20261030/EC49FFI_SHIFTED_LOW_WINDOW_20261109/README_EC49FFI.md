# EC49FFI — Shifted low-observer interval theorem and exact native-prefix nonmonotonicity

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Mode: author-side TASK_RESEARCH, independent Driver review pending. P000 and protected ACTIVE worldview unchanged.

## Carrier and precise objective

Use the original six-axis signed native word expansion, original nine-state BRC DFA and full complete-key triple K=(x,y,z). A key is count-admissible if z>=1, x>=2z and y>=0. For fixed terminal horizon H=x+y-1, EC49FFD/EC49FFF show the low signature quartet {1,2,4,8} can each be realized with separate legal ordered words at h exactly when the standard representative K_H exists with h+1<=H<=2h-1. The representative is K_H=(2+floor((H-1)/2), H-1-floor((H-1)/2),1). All components of K_H are strictly positive.

The first problem requires the quartet at every integer window A<=h<=U for arbitrary 2<=A<=U. Minimize lexicographically (number of distinct complete keys, sum of native signed microstep lengths of one word per chosen key). As established in EC49FFC, each word of K=(x,y,z) has length 2(H+z). This secondary length measure is a cache selection surrogate; the ordered-prefix union is evaluated separately in the second problem.

## Theorem 1 — shifted dyadic interval cover, no finite horizon cutoff

Let A,U be any integers 2<=A<=U and define

k = min{j>=1: 2^j(A-1)>=U},
H_i=1+ceil(U/2^(k-i)), i=1,...,k,
n=U-1, q=floor(n/2^k), and s_2(n)=popcount(n).

Then the lexicographically minimum cache-key count and one-word-per-key native length sum are

(k, L), where
L = sum_{i=1}^k 2(H_i+1)
  = 4(n-q)+6k-2(s_2(n)-s_2(q)).

The k distinct standard keys K_(H_i) attain the optimum. In particular A=2 recovers EC49FFH and k=ceil(log2 U).

### Proof

At fixed H, standard-key dominance retains all low signature accessibility and has z=1, so its native length is no larger than that of any original key with the same H. Redundant keys can be deleted and distinct remaining horizons ordered H_1<...<H_m. Their low windows are intervals [ceil((H_i+1)/2),H_i-1] with both endpoints increasing. Every horizon in a minimal cover must contribute to covering [A,U]; hence H_1<=2A-1, H_m>=U+1 and consecutive horizons satisfy H_(i+1)<=2H_i-1 (otherwise there is a gap).

Iterating from H_1 gives H_i<=2^i(A-1)+1 and therefore U<=2^m(A-1). Thus m>=k. For m=k, iterating the adjacency inequality backwards from H_k>=U+1 gives H_i>=1+ceil(U/2^(k-i)). The proposed horizons are strictly increasing, start in [A+1,2A-1], end at U+1 and obey adjacency, so they form a feasible k-key cover and are componentwise minimal. Every original key has word length 2(H+z)>=2(H+1). Hence the proposed keys minimize the stated pair globally.

For the closed form, use ceil(U/2^j)=floor((U-1)/2^j)+1, and the finite binary identity
sum_{j=0}^{k-1} floor(n/2^j)=2(n-q)-s_2(n)+s_2(q), q=floor(n/2^k).
Substitution into L=4k+2 sum_{j=0}^{k-1} ceil(U/2^j) yields the formula.

The jump law is also exact: if k(A,U+1)=k(A,U), then
L(A,U+1)-L(A,U)=2[1+min(k-1,v_2(U))].
At the cardinality jump U=2^k(A-1), the increment is 2(A+k+2).
These are formulas in integer arithmetic.

Examples:
A=3,U=9: k=3, horizons (4,6,10), L=46.
A=5,U=9: k=2, horizons (6,10), L=36.
A=5,U=16: k=2, horizons (9,17), L=56.
A=5,U=17: k=3, horizons (6,10,18), L=74.

## Theorem 2 — exact finite native-prefix cost is not horizon-monotone

For a single observation window h, require the four distinct low final signatures {1,2,4,8}, selecting exactly one original six-operation word for each signature and using a single admissible complete BRC key K shared by all four. The cost is the number of distinct nonempty ordered, signed native-six-axis microstep prefixes across the four selected words.

Exhausting every count-admissible complete key and every admissible original ordered word for h=2,3,4,5 gives:

h | admissible full keys | globally minimum prefix edges
2 | 1 | 28
3 | 3 | 34
4 | 7 | 32
5 | 13 | 36

There are 24 key/window configurations in this finite domain. The exact bitset checker enumerates every legal four-word selection for each configuration (3,389,185 selections in total), without MILP, floating point or probabilistic sampling.

In particular the optimum drops from 34 edges at h=3 to 32 edges at h=4, despite the growth of the required observation word length. This is a concrete observer-and-path-order effect, not a monotone length surrogate.

An optimal h=3 certificate uses K=(3,2,1):
signature 1: deg; 2: egd; 4: ceg; 8: egc; native prefix union 34.
An optimal h=4 certificate uses K=(4,2,1):
signature 1: gefd; 2: fegd; 4: fegc; 8: gefc; native prefix union 32.

For every candidate, the checker recomputes the original nine-state automaton state, native six-axis displacement (2,0,0,0,0,0), three positive native step counts (x,y,z), signed microstep length and every ordered prefix. Exhaustion supplies the lower bound; the recorded witnesses supply the upper bound.

## Reproducibility and scope

Run: python3 VERIFY_EC49FFI.py
Uses Python standard library only, original operation expansion and DFA constants copied from EC49FFH's immutable original verifier. Independently evaluates 120 interval-subset DPs (2<=A<=U<=16), tests the jump law on 1,547 integer cases, and exhausts the 3,389,185 original prefix combinations for h=2..5. The compact result table is EXACT_REPORT_EC49FFI.json.

Provenance: EC49FFC 2dd856c416f111d90d523dcb10cde952248ec814; EC49FFD df0dbc54707a6926db858631e5a03fea189dccde; EC49FFF 58cdba9c360bc180028183cff711405d2e2f37c0; EC49FFH 6f6e4032b699358781898a1ba0acab2f8f0db97b. Global main read 27934d979d2b83995d872efc9f690ccef3f536a6; EM main read 08a0afb765518b5766b393d14c7ff54e32f1246d. Frozen science remains fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

Status: AUTHOR_ANALYTIC_THEOREM / EXACT_INTEGER_DP_120_PASS / EXACT_NATIVE_PREFIX_ENUM_3389185_PASS / NOT_ADMITTED. No Result/Review/Claim is created by this author-side note.

Next: seek direct original-prefix improvements for new 22-path quota masks beyond EC49FEO/EC49FEU, using the interval theorem as a cache prefilter. For h>=6 or multiple independent windows, reuse native prefix packing/dual certificates with bounded exact solvers, and test nonstandard full keys rather than inferring prefix-optimality from one-word length. Parent target remains <=5 full keys and <=93 native prefix edges.
