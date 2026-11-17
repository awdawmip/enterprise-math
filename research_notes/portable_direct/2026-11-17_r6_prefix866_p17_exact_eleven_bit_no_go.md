# PREFIX-866 — Exact eleven-bit no-go and sharp twelve-bit recovery for 17 named sources

Date: 2026-11-17. Role: auxiliary TASK_RESEARCH / named-source BRC observer.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Predecessor: PREFIX-864 exact fiber/divisibility theorem; PREFIX-865 no-op least-common-multiple and forced-coupled-decoder obstruction.
Status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## The exact question and answer

Let `u` range over every p-bit named binary source state (`0<=u<2^p`). A legal ordered heartbeat transition is `(u,u)` or `(u,u xor 2^i)` for some i in [0,p). Both states are initially unknown. Read fixed odd moduli `q1,q2>=3` before and after the heartbeat, obtaining `(u mod q1, v mod q2)`. Demand recovery of the COMPLETE ordered transition, with peak port width `B=max(bit_length(q1),bit_length(q2))`.

**Theorem 866 (sharp):** For p=17, the minimum peak width among ALL fixed ordered odd-modulus two-read complete-transition observers is exactly

`B_fix,odd(17)=12.`

More precisely, EVERY ordered pair of odd moduli `3<=q1,q2<=2047` has an actual transition collision, while `(q1,q2)=(1221,4033)` is injective. Together with PREFIX-864, this completes exact values for p=10 through p=18 inclusive.

## Proof: complete finite exclusion at B=11 with a single old-residue fiber

Put `p=17`, `N=2^17=131072`, `T=N*(p+1)=2359296`, and `M=2^11-1=2047`. Any valid pair (q1,q2) must satisfy the following necessary conditions:

1. Each q is odd in [3,M] and `h(q)>=p`, where `h(q)=min {d>=1:2^d == +1 or -1 (mod q)}`. If `h(q)<p`, the modulus identifies two p-bit states at Hamming distance at most two. For q1 these can be distinct predecessors of the SAME legal successor, colliding for any q2; for q2 reverse the role of predecessor/successor. Concretely, differences `2^d-1` and `2^d+1` correspond to pairs of Hamming distance two, and each pair has a common one-flip neighbor.
2. `q1*q2>=T` by the total number of distinct ordered legal transitions.
3. `lcm(q1,q2)>=N` by the no-op argument of PREFIX-865.
4. In the old-residue-zero fiber, there are `m=ceil(N/q1)` distinct old states `u=0,q1,2q1,...<N`, hence exactly `m*(p+1)` legal ordered transitions. Their second residues must all be distinct, requiring `q2>=m*(p+1)`. Also `T<=q1*M` and `m*(p+1)<=M` follow as preliminary q1 pruning.

The **complete exact certificate** enumerates the 1023 odd candidate values for each port (1,046,529 ordered pairs), constructs the 958 moduli satisfying condition 1, and applies conditions 2–4 to give precisely 441 eligible q1 values and 113,884 eligible ordered pairs.

For EACH of these 113,884 pairs it fully enumerates the **whole zero fiber**, not a statistical sample:

`V_0(q1) = [u] + [u xor 2^i for i=0,...,16]`, for every `u=0,q1,2q1,...<N`.

It then checks whether all `v mod q2` in this multiset are different. **Precisely zero** pairs pass. By PREFIX-864's exact fiber criterion, any collision already inside this single fiber disproves global injectivity. All pruned pairs fail independent necessary conditions. Thus no eleven-bit fixed odd-modulus observer is injective. This finite domain is exhaustively covered by integer loops and has no untested external parameter.

The standalone Python certificate and an independently implemented compiled C++ exact residue checker both yield:

`half_period_safe_moduli=958`;
`eligible_first_moduli=441`;
`eligible_pairs=113884`;
`pairs_surviving_zero_fiber=0`.

The C++ version uses integer timestamp arrays instead of Python residue sets and reproduces the same counts.

## Constructive twelve-bit upper bound

Select `g=37, a=33, b=109` and moduli `q1=g*a=1221, q2=g*b=4033` (both odd, each <=4095). Exact modular powering gives `h(37)=18>=17`, and `gcd(33,109)=1`. Hence `lcm(q1,q2)=37*33*109=133089 >= 131072=N`.

For every transition, `delta=v-u` is one of `{0,+/-1,+/-2,...,+/-2^16}`. Their residues modulo 37 are pairwise distinct because h(37)>=17. From the difference between the two observed residues modulo 37, recover delta exactly. Then generalized CRT on `v == r1+delta (mod q1)`, `v == r2 (mod q2)` determines the unique 0<=v<N, and `u=v-delta`. Thus the complete transition is recovered in twelve-bit ports. Combining the upper construction with the complete B=11 exclusion proves the theorem.

## Evidence, verification and status

Scientific source anchors: PREFIX-864 at `b8b6e11f65662d769d9efd491a9a64123545d516`; PREFIX-865 at `7bcccec60fb2cb573eef95d5ab1ef66d0d337660`; PREFIX-861 at `727d6ca2dee6f707e3dd3cabba600d2c21b12bc8`.

The exact scripts `PREFIX866_R6_P17_ELEVEN_BIT_EXCLUSION_CHECK.py` and `PREFIX866_R6_P17_INDEPENDENT_CXX_CHECK.cpp` each execute the declared finite domain using integer arithmetic. The Python script also checks the constructive CRT parameters; the C++ script independently checks all eleven-bit candidates. Results are recorded in `PREFIX866_R6_P17_ELEVEN_BIT_EXCLUSION_RESULTS.json`. Both ran successfully in this research session. The finite certificate requires no probabilistic assumption, external mathematical library, numerical approximation or prior unseen proof.

This is a self-contained auxiliary named-source observer theorem; it changes neither P000 V5 nor the native X6 Cell/Link/Port interface or shared-task claim authority.

## Continued research question

The new zero-fiber phenomenon suggests asking whether, for larger p and B near counting-optimal, collisions in the old-residue-zero fiber alone always certify certain odd-modulus lower bounds. Examine p=19,20 and derive a structural arithmetic criterion replacing finite enumeration, while keeping fixed-odd complete-transition and other observation models separated.
