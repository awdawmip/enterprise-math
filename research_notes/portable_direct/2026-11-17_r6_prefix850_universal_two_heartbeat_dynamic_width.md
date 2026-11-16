# PREFIX-850 — Two-heartbeat modular recovery: universal constructions and a sharp eight-source improvement

**Date:** 2026-11-17. **Status:** AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / INDEPENDENT_EXACT_LOCAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific input:** f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
**Scientific predecessors:** PREFIX-840--849, particularly PREFIX-848's ordered-pair automaton and PREFIX-849's five-source four-heartbeat law.
**Type:** auxiliary Q-only, named positive-weight BRC scalar observer; this result does not claim an X6 Cell/Link/Port native event implementation.

## 1. Precise model

There are p **named** sources, each with weight 1 or 2. Let x=(x_0,...,x_{p-1}) in {0,1}^p, and let U(x)=sum_i 2^i x_i, with N=2^p possible named configurations. Between consecutive heartbeat times, either no bit changes or exactly one named bit flips. The choice of bit is hidden. A predetermined, state-independent, possibly periodic sequence of positive integers m_t produces

\[
Y_t=2^{\lfloor t/2\rfloor}(S+U(x_t))\bmod m_t,
\]

where S is a known fixed integer. The decoder knows S, times and moduli, but has **no known old state** and must determine x_t from only the last w observations, for every legal infinite trajectory and all t>=w. B_p(w) is the least B for which each modulus is <=2^B. For late times any modulus <=2^B has effective modulus equal to its odd part; an odd modulus is unaffected by the gain.

Define Hamming closed neighborhood A(x)={x,x xor 2^0,...,x xor 2^{p-1}} as packed integers. For any word (q,r) of odd moduli, the complete two-observation ambiguity relation consists of endpoints u,v reached from a pair x,y with x≡y (mod q), u in A(x), v in A(y), and u≡v (mod r). The word is **good** precisely if all resulting endpoint pairs are diagonal. A predetermined infinite two-window schedule works exactly when the directed graph with one vertex per modulus and edges for good words has a directed cycle. This is the exact PREFIX-848 criterion.

## 2. Universal one-heartbeat optimum

For every p>=1,

\[
\boxed{B_p(1)=p+1.}
\]

For late times every bounded modulus has effective odd part <=2^B. When B<=p, the effective odd modulus is at most 2^p-1 and cannot distinguish all 2^p states at a single heartbeat. Conversely the constant odd modulus 2^p+1 (which occupies p+1 bits) is injective on U=0,...,2^p-1 at all times.

## 3. First universal construction: p bits in two heartbeats for every p>=6

Let H=2^{p-1}, Q=2H-1, and q=H-7. The following preassigned periodic modulus schedule is good:

\[
\boxed{m_{2j+1}=H-7,\qquad m_{2j+2}=2H-1\quad(j\ge0),\qquad p\ge6.}
\]

Both moduli are odd and <=2^p, so

\[
\boxed{B_p(2)\le p\quad(p\ge6).}
\]

**Proof, complete for all p>=6.** Put A=A(0)={0,1,2,4,...,H} and D=A(2H-1)={2H-1,2H-2,2H-3,...,2H-1-H}, with the subtractions in D taken only at powers of two. Modulo q=H-7, the residues of A are precisely {0,1,2,4,...,H/2,7}. The residues of D are {13,6,12,11,9,5} together with {H+6-2^j:4<=j<=p-2}. The latter lie between H/2+6 and H-10; the six small residues are not powers of two, 0, or 7. Hence A and D have disjoint residues modulo q.

For the word (q,Q), the only non-diagonal pair of integers in [0,2H-1] congruent modulo Q is {0,2H-1}. Its possible predecessor pair must lie in A x D (up to orientation), whose q residues are disjoint. Thus (q,Q) is good.

For (Q,q), the first reading has either a diagonal pair (x,x) or the extreme pair {0,2H-1}. The extreme pair cannot lead to q-equal endpoints by the disjoint-residue fact. From a diagonal pair (x,x), two possible successors differ by a signed sum of at most two powers of two from {1,2,...,H}. Its nonzero absolute value is at most H+H/2, which is below 2q for H>=32. If it were divisible by q, it would therefore equal q. But q=H-7 is odd and is neither 1 nor 2^i+1 nor 2^i-1: the latter congruence is 7 (mod 8) for i>=3, while q≡1 (mod 8), and q-1=H-8 is not a power of two for H>=32. Consequently no such non-diagonal pair is q-equal. So (Q,q) is good too. Both cyclic two-windows are good, proving the claim. QED.

## 4. Stronger universal construction: p-1 bits in two heartbeats for every p>=8

Let d=2^{p-5} (so d>=8), N=32d, and define

\[
\boxed{q=7d+1,\qquad r=12d-1,\qquad m_t=q,r,q,r,\ldots.}
\]

Both are odd and <=N/2=16d; thus their ports use at most p-1 bits. We prove **both** (q,r) and (r,q) good:

\[
\boxed{B_p(2)\le p-1\qquad(p\ge8).}
\]

A key necessary condition for any ambiguous non-diagonal final pair is the following elementary arithmetic statement. If the first reading is modulo q and the second is modulo r, let d_1=U(y_1)-U(x_1)=u q, with |u|<=4, and d_2=U(y_2)-U(x_2)=v r, with 1<=|v|<=2. (These ranges follow exactly from 0<=U<N.) Since each trajectory flips at most one bit,

\[
d_2-d_1=v(12d-1)-u(7d+1)=(12v-7u)d-(u+v)
\]

must be expressible as a sum of at most two **signed powers of two** whose exponents are 0,...,p-1. We establish that none of the 9x4=36 possible integer differences has such a representation. The same statement for (r,q) follows by reversing the temporal difference, with the same 36 pairs (and opposite signs).

**Arithmetic separation lemma.** For every h>=3, d=2^h, every integer -4<=u<=4 and v in {-2,-1,1,2}, the integer

\[
D=(12v-7u)2^h-(u+v)
\]

is not a signed sum of at most two powers of two of exponents 0,...,h+4.

*Proof.* At h=3 and h=4 this is a finite exact enumeration of 36 differences against the complete signed two-power spectrum; the attached executable checker enumerates all possibilities, with no floating-point arithmetic. For h>=5 write k=12v-7u and s=u+v. Here |s|<=6 and k≠0 (the equality 12v=7u would force 7|v, impossible for 1<=|v|<=2). If both signed powers have exponent >=h, divisibility by 2^h requires s=0. Then u=-v and k=19v in {±19,±38}; neither is a signed sum of at most two powers of two. If exactly one exponent is >=h, reduction modulo 2^h and |s|<=6 forces the lower power to have magnitude |s| in {1,2,4}; the coefficient k must be a signed single power of two. But k=19v-7s for |v|=1 or 2, s in {±1,±2,±4}, never has power-of-two absolute value (finite list of possible absolute values: 5,9,10,12,24,26,31,33,45,47,52,66). Finally, if both exponents are <h and distinct, their sum in magnitude is at most 3*2^{h-2}=3d/4, whereas |kd-s|>=d-6>3d/4 for d>=32. If their exponents coincide, the result is zero or a single power of two, already excluded by k≠0 or the previous cases (the only possible magnitude d would demand k=±1 and s=0, whereas s=0 implies k=19v). This proves the lemma. QED.

If two legal trajectories had identical observations at both times but distinct final states, their difference would satisfy the forbidden representation in the lemma. Thus both cyclic words are good; the claimed schedule recovers the **named current state exactly** from the last two scalar reports at every heartbeat. QED.

**Important accounting:** the source itself may update between readings. The decoder must retain two readings plus the public schedule, i.e. two ports of <=p-1 bits each; this theorem optimizes **maximum per-heartbeat port width**, not total transmitted bits or memory.

## 5. New sharp small-capacity classifications

The exact ordered-pair recurrence over all 2^p named states, the actual Hamming-neighborhood relation and every odd effective modulus gives:

| p | one-heartbeat B_p(1) | optimal two-heartbeat B_p(2) | two-heartbeat witness |
|---|---:|---:|---|
| 5 | 6 (PREFIX-849) | 6 (PREFIX-849) | (33,33) |
| 6 | 7 | **6** | (25,63) |
| 7 | 8 | **7** | (57,127) |
| 8 | 9 | **7** | (57,95) |

For the matching lower bounds: at p=6 and B=5, all 16²=256 possible late odd pairs were checked; none is good. At p=7 and B=6, all 32²=1024 pairs were checked; the **single** good edge is (33,55), which cannot form a directed cycle, ruling out a perpetual two-window schedule. At p=8 and B=6, all 32²=1024 pairs were checked and none is good. At the next width the counts of good pairs are respectively 22, 334 and 69; witnesses above are verified in **both** cyclic orientations. Each finite lower bound is therefore exact in the specified observer model.

The new p=8 result **saves two bits per heartbeat versus the optimal one-heartbeat port**. The p=6 and p=7 two-heartbeat laws save one bit.

## 6. Exact verification, scope, and next questions

The attached Python exact-integer checker independently constructs full ordered-pair ambiguity relations, exhaustively enumerates all odd effective two-words at p=6,7,8 in the stated ranges, detects graph cycles, verifies both constructions for p=6,...,10, and checks all 36 arithmetic differences for every p=8,...,24. It returned ALL_EXACT_ASSERTIONS_PASSED. The h>=5 proof is symbolic; finite verification checks its boundary cases h=3,4 and additional regressions. All source-weight names remain separate bit positions, and actual trajectories may choose different single-bit changes.

Prior literature is **not claimed** for these exact new constructions; prior provenance is the project-specific PREFIX-848/849 observer formalism. Results are auxiliary BRC modular-channel theorems. No equivalence with an admissible native X6 Cell/Link/Port event is assumed.

**Next scientific problems:** (a) determine whether p>=9 admits a third saved bit or a p-dependent saving growing with p under two observations; (b) derive asymptotic optimal two-port bit-width bounds rather than just explicit constructions; (c) study robust recovery under one erased or corrupted heartbeat; (d) test actual native event source/port licensing without replacing P000.

**Authority:** independently authored research evidence. No shared X6 CLAIM, Result, Review, Working Truth or Foundation promotion is asserted.
