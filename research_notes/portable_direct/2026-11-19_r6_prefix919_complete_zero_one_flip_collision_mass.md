# PREFIX-919 — Complete zero-or-one-step named XOR collision mass

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6.
Status: AUTHOR_PROVED / EXACT_INTEGER_COMPUTED / SMALL_OBSERVER_EXHAUSTIVE / INDEPENDENT_CONGRUENCE_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Direct dependency: [PREFIX-918](2026-11-19_r6_prefix918_complete_named_two_flip_collision_mass.md), with its validated fixed-observer two-flip count. This is an auxiliary two-port observer representation retaining named XOR source identity, not an X6-native physical dynamics claim.

## 1. Exhaustive type partition

Let `p>=2`, `N=2^p`, and odd integers `a,b>1`. For each `0<=x<N`, define one zero-step trajectory `Z_x=(x,x)` and, for each named source bit `0<=i<p`, the trajectory `F_x^i=(x,x XOR 2^i)`. The observation is `Phi_(a,b)(u,v)=(u mod a,v mod b)`. Trajectories retain their type, state and source label; different labels are not collapsed.

Let `M_00` count unordered distinct pairs of zero steps, `M_01` count pairs with exactly one zero step and one flip, and `T_p(a,b)` count pairs of two flips as in PREFIX-918. The exact number of all unordered distinct colliding named trajectories is
```text
C_p(a,b) = M_00(p,a,b) + M_01(p,a,b) + T_p(a,b).
```
This partition is exhaustive and pairwise disjoint by trajectory types.

**Theorem 919-A (zero-zero mass).** Put `d=lcm(a,b)`, `q=floor((N-1)/d)`. Then
```text
M_00 = q*N - d*q*(q+1)/2.
```
Proof: distinct zero steps with ordered starting states `x<y` collide iff `d|y-x`. For each positive difference `md<N` there are exactly `N-md` choices. Summing `m=1,...,q` proves the formula.

**Theorem 919-B (complete mixed-type mass).** For each `1<=k<=floor((N-1)/a)`, write `A=ka`, `L=N-A`. For `0<=i<p`, write `H=2^i`, `r=A mod (2H)` and `tau_i(A)=min(r,2H-r)`. Then
```text
M_01(p,a,b)
 = sum_{1<=k,ka<N} sum_{i=0}^{p-1}
     [ 1[b | A+2^i]*(L-tau_i(A))
       + 1[b | A-2^i]*(L+tau_i(A)) ].
```
All terms are nonnegative integers. The two divisibility indicators cannot simultaneously hold for odd `b>1`.

**Proof.** A zero/flip pair cannot start at the same state: otherwise its terminal difference is `+/-2^i`, not divisible by odd `b>1`. For distinct starts choose uniquely the smaller start `x`, larger start `y=x+A`, and source bit `i`. Equality of first-port residues uniquely forces `A=ka>0`. There are two disjoint orientations.

If the larger-start trajectory is the flip, its terminal gap is `A+s*2^i`; for `s=+1`, the bit at `y` must be zero, and for `s=-1` it must be one. If the smaller-start trajectory is the flip, its terminal gap is `A-s_small*2^i`; matching the same indicator `b|A+s*2^i` forces `s_small=-s`. These correspond to opposite bit values at the small and large starting states.

Define `G_i(z)=floor(z/(2H))*H+max(0,z mod (2H)-H)` for `0<=z<=N`, the exact number of bit-`i` ones among integers in `[0,z)`. Since `N` is a multiple of `2H`, bitwise complementation within `[0,N)` implies
```text
G_i(N-A) = N/2 - A + G_i(A),
G_i(N)-G_i(A)= N/2-G_i(A).
```
For `s=+1`, the large-flip orientation contributes `L-(N/2-G_i(A))`; the small-flip orientation contributes `G_i(N-A)`. Their sum is `L+2G_i(A)-A=L-tau_i(A)`, since `A-2G_i(A)=min(r,2H-r)`. For `s=-1`, complementary bit values give `L+tau_i(A)`. Each pair uniquely identifies `(k,i,s,orientation,x)`, proving that the displayed sum neither omits nor duplicates any mixed-type pair. QED.

**Corollary 919-C (coprime-only mixed collisions).** If `gcd(a,b)>1`, then `M_01(p,a,b)=0`. Indeed any nonzero mixed pair would require `b|ka +/- 2^i`, forcing `gcd(a,b)|2^i`; an odd gcd greater than 1 cannot divide a power of two.

**Corollary 919-C2 (strict-19-bit zero-step dichotomy).** In the strict-19-bit p=32 domain, coprime moduli satisfy `ab>2^36>N`, hence `M_00=0`; noncoprime moduli satisfy `M_01=0` by Corollary C. Thus all collisions involving at least one zero step are entirely mixed-type in the coprime case and entirely zero-zero in the noncoprime case. This is an exact statement about labeled trajectory-pair types, not a bound on the two-flip category.

**Corollary 919-D (64-fiber bound in strict-19-bit domain).** If `2^18<a,b<2^19` are odd and `p=32`, then `K=floor((2^32-1)/a)<=16383<b`. For coprime `a,b`, each `(i,s)` determines at most one eligible `k`, namely
```text
k = (-s*2^i*a^{-1}) mod b,  1 <= k <= K.
```
Thus the exact mixed mass needs checking at most `2p=64` congruence fibers for a specified observer, independent of the state population `2^32`. The formula remains valid for noncoprime and unrestricted odd moduli with the direct scan.

**Corollary 919-E (time reversal).** `M_01(p,a,b)=M_01(p,b,a)`. The involution reversing each named trajectory maps `Z_x` to itself and `F_x^i` to `F_{x XOR 2^i}^i`; swapping the observation ports gives a bijection between colliding mixed-type pairs.

## 2. Exact 32-bit observer result

For the same frozen auxiliary observer `(p,a,b)=(32,321651,440665)` as PREFIX-918:
```text
M_00 = 0                 (lcm(a,b)=141740337915 > 2^32)
M_01 = 59,007,025,662
T_32 = 422,370,153,289 (reused, unchanged PREFIX-918)
C_32 = 481,377,178,951.
```
Exactly 17 of the at-most-64 coprime congruence fibers have positive mixed mass. All 17 are on the `A-2^i` branch. The full `k,i,s,mass` table is stored in `PREFIX919_R6_ZERO_ONE_FLIP_RESULTS.json`; the checker reproduces it rather than embedding the table in a proof assumption.

## 3. Independent verification and exact scope

The Python 3 checker `PREFIX919_R6_ZERO_ONE_FLIP_CHECK.py` performs (i) the direct `k,i` mass scan, (ii) separately coded modular-inverse-first enumeration, and (iii) time-reversed observer recomputation. All yield `59,007,025,662` at the frozen example, with identical 17 positive fibers in the first two methods.

For every `2<=p<=8` and every ordered odd `3<=a,b<=min(15,2^p-1)`, the checker explicitly enumerates the complete `Z_x,F_x^i` trajectory multiset, groups exact observation fibers, and verifies `M_00`, `M_01`, modular-inverse recount and time-reversal identity. **255 complete small-observer cases passed** (176 coprime, 79 noncoprime). The locally executed checker used Python integer arithmetic and no probabilistic or floating-point operations.

PREFIX-918's `T_32` has its own separately documented C++17/Python checks, reused here rather than rerun. The current combined count is an exact arithmetic consequence of both disjoint, explicitly specified models and their author proofs. Neither code execution nor file hashes substitute for independent mathematical review or formal admission.

## 4. Next scientific frontier

Derive distributional bounds and characterize zero mixed mass for coprime strict-19-bit observer pairs; study collisions in the full named trajectory observation multigraph using the exact type partition, retaining provenance multiplicities. For the separate global mother problem, continue searching for injective observer pairs or a universal collision guarantee to settle `B_fix,odd(32) in {19,20}`. The model remains an auxiliary two-port readout, with no native two-dimensional plane or native X6 dynamics inferred.

GitHub Source publication of this note and its code/JSON is independent of current shared X6 Task CLAIM; research activity/Source ledger linkage must be reported separately.
