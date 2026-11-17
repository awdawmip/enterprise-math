# R762DJ — 精确模面积游走、Fourier 谱与 BRC 初始记忆成本

2026-11-17 · Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS · publication TP2-8B7E13C5904A2D6F1142 · researcher EM-X6-3050F6 · author verification PASS · independent review NOT_REVIEWED.

## 固定的科学输入、类型及条件

Frozen taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. P000 V5: @a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Scientific inputs and native P000 remain unchanged (six signed spatial axes, distinct time, native PERP_E = 120°, primitive stable balance arity 3).

Reuse V17 signed native Cell path, R762DD open-path area cocycle, and R762DI exact paired-triad six-step path spectrum in Draft PR #2654@c70993410d204fa9468f9755465d2002dfe36f6d. The block is a **candidate composite native path**, not an authenticated TRIADIC_CLOSURE_E force event. No direct identification of a three-step closed force event with a Cell return.

Choose three distinct native axes and a fixed sign vector epsilon. Each block consists of three signed coordinate steps in arbitrary order u, then the three opposite steps in arbitrary order w. Choose u,w independently and uniformly among the six permutations. These 36 named paths are full six-step Cell returns. Their three pair-area coordinates are

    A(u,w) = D_epsilon (s(u)+s(w)), 
    S={s(u)}={+++ , ++- , -++ , --+ , +-- , ---},

where s(u) gives the order orientation of the three unordered axis pairs and D_epsilon has diagonal entries epsilon_i epsilon_j. Their other 12 X6 area coordinates vanish. For a concatenation of k≥1 independent such six-step paired blocks, v=0 for each block; the cocycle A(HK)=A(H)+A(K)+v(H)∧v(K) makes the area **exactly additive**. Define X_k = cumulative A mod q, with starting X_0=0. This defines a **conditional candidate N-BRC random walk**; it is not a claimed physical probability law. Full area trajectories (X_1,...,X_k), final marginals X_k and original named paths are different observation languages.

## Theorem A — q=3: exact distributions, mixing and minimal seeds

For every integer k≥1 the 27 endpoint states x∈F_3^3 split into the following four exact classes:

| R(x) | States | Exact Pr(X_k=x) |
|--:|--:|--|
| 14 | 1 | (4^k+14)/(27·4^k) |
| 2 | 12 | (4^k+2)/(27·4^k) |
| -4 | 8 | (4^k-4)/(27·4^k) |
| -1 | 6 | (4^k-1)/(27·4^k) |

At k=1, eight states have zero weight and the R762DI support has 19 states; at k≥2 all 27 have positive mass. For the uniform distribution U_27,

    TV(Law(X_k),U_27) = 38/(27·4^k).

If all random choice must be represented by equally weighted initial deterministic seeds, with no later random input, then the minimum seed count for only the final endpoint is

    M_3(k) = 9·4^k.

If the entire time-indexed area trajectory (X_1,...,X_k) must be preserved, the minimum is instead

    J_3(k) = 36^k.

### Proof

Multiplying pair-area coordinates by D_epsilon is an invertible change of labels modulo 3, so take epsilon positive. Let omega be a primitive cube root of unity and let t∈F_3^3. For one paired block the Fourier transform equals

    μhat(t)=[F(t)/6]^2, F(t)=Σ_{s∈S} omega^(t·s).

The set S comprises all eight sign triples except the two vectors ±(1,-1,1), so

    F(t) = Π_{j=1}^3 (omega^t_j + omega^(-t_j))
           - (omega^(t·c)+omega^(-t·c)), c=(1,-1,1).

Since omega^a+omega^(-a)=2 for a=0 mod3 and -1 otherwise, all F(t) are exact integers. The complete 27-character finite table has F-value histogram: 6 occurs once (t=0), -3 occurs eight times, 0 occurs twelve times, and 3 occurs six times. Thus μhat(0)=1, μhat(t)=1/4 at fourteen nontrivial characters, and μhat(t)=0 at the other twelve.

For k≥1, invert the kth power of μhat:

    27 Pr(X_k=x)=1+4^(-k) R(x),
    R(x)=Σ_{t≠0,F(t)≠0} omega^(-t·x).

The full finite 27-vector integer character table yields the four R-values and their multiplicities listed above (also reconstructed by the companion verifier). They may be calculated without complex numbers: if n_0(x) counts the fourteen active characters with t·x=0 mod3, then R(x)=(3 n_0(x)-14)/2. The total variation formula follows by summing |R|: 14+12·2+8·4+6·1=76 and dividing by 54·4^k.

There are N=36^k equal named original paths. Exact final-state path counts are N Pr(X_k=x)=3^(2k-3)(4^k+R(x)), with the right side evaluated as integer also for k=1. When k=1, some states have count 1, so the gcd of all nonzero counts is 1. For k≥2, the gcd of the four integer brackets is exactly 3: their pairwise differences have gcd 3, and 4^k-1 is odd and divisible by 3. Thus the path-count gcd is 3^(2k-2) (including k=1). An equal-seed deterministic representation of rational outcome weights c_x/N exists on M seeds precisely when N divides M c_x for all x; the minimum is N/gcd_x c_x. Therefore M_3(k)=36^k/3^(2k-2)=9·4^k.

The trajectory increments are recovered uniquely by X_j-X_(j-1). A single block's mod-3 area spectrum includes an outcome with exactly one named path, so the k-fold joint increment count table contains an entry 1; its gcd is 1. Therefore J_3(k)=36^k. □

## Theorem B — q=4: exact reachable subgroup, mixing and minimal seeds

All pair-area entries A_i are even. Hence modulo 4, the reachable subgroup is 2(Z/4Z)^3 of size 8. Let Y_k=A_total/2 mod2 ∈ F_2^3 encode it losslessly. Then for every k≥1,

    Pr(Y_k=y) = (1+3·9^(-k))/8  for y=000 or y=111,
                 (1-9^(-k))/8   for the other six states.

In particular,

    TV(Law(Y_k),U_8)=3/(4·9^k),
    M_4(k)=2·9^k  (final mod-4 area),
    J_4(k)=18^k   (complete mod-4 area trajectory).

### Proof

The R762DI one-block count spectrum on F_2^3 is 6 at each of 000 and 111, and 4 at each other state (36 named paths). Its Fourier transform at a∈F_2^3 equals 1 at a=000, 1/9 at the three vectors with Hamming weight 2, and 0 at the four odd-weight vectors. Fourier inversion after k steps gives the two-class probabilities, and total variation follows by direct summation.

The two types of final-state path count are

    c_high = 4^k(9^k+3)/8,
    c_low  = 4^k(9^k-1)/8.

Both are integers for k≥1 and gcd(c_high,c_low)=2^(2k-1), because gcd(9^k+3,9^k-1)=gcd(4,9^k-1)=4. Therefore M_4(k)=36^k/2^(2k-1)=2·9^k.

For a joint k-block trajectory, the named-path count of each increment is either 4 or 6. The gcd of all products is 2^k: every product contains that factor, and all-4 and all-6 increment sequences already force the gcd to divide gcd(4^k,6^k)=2^k. Therefore J_4(k)=36^k/2^k=18^k. □

## Evidence, interpretation and next boundary

The companion R762DJ_VERIFY.py program independently constructs all 36 single-block signed X6 paths, recomputes area from the ordered pair wedge sum, checks eight global sign assignments for q=3 and q=4, builds exact integer convolutions at k=1,...,8, checks all 27/8 predicted endpoint state counts, character histograms, integer count gcds, and seed-cost and variation-distance formulas. No floating-point inference or Monte Carlo is used. The JSON evidence is R762DJ_EVIDENCE.json. Author check PASS; independent review NOT_REVIEWED. The finite tests validate the implementation over its declared range; the two theorems follow by the exact algebra and complete finite character classifications given above.

The same named-path population can mix to a uniform **endpoint** while preserving exponentially more **trajectory/provenance** information. The improvement M_3(k)=9·4^k versus J_3(k)=36^k and M_4(k)=2·9^k versus J_4(k)=18^k is strictly observer-scoped. Positive BRC weights do not encode signed force cancellation.

Unfinished mother-task question: determine the authentic, source-pinned native signed Cell/Link/Port TRIADIC_CLOSURE_E licensing predicate and V17/V29/V39 transport. If it licenses these paired six-step blocks and their composition, test whether legal future operations can read only the final area, intermediate area, named microbranches, or a larger residual state. Do not promote this candidate walk into primitive balance without an independently licensed event mapping.