# PREFIX-847 - Single-source update residuals and the last-heartbeat information barrier

**Scientific status:** AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
**Direct predecessor:** PREFIX-846, streaming-window CRT for a *constant* BRC source tuple.
**Model scope:** Q-only positive-integer named-source BRC scalar observer, not a native X6 Cell/Link/Port event.

## The problem and the typed interface

Let p>=1 and W>=2. A named source state is x=(x_0,...,x_{p-1}) with x_i in {0,...,W-1}, corresponding to original positive source weights w_i=x_i+1. Put N=W^p, U(x)=sum_i x_i W^i, and let S be a fixed known integer offset. At heartbeat t>=1 the scalar port transmits

  Y_t(x)=c_t(S+U(x)) mod m_t,
  c_t=a^floor(t/2) b^floor((t-1)/2), with a,b positive integers and C=ab.

We now allow one named-source weight to change between consecutive heartbeats. Define H_1(x) as the radius-one Hamming ball around x: x itself plus all states obtained by replacing one digit with another allowed value. Its size is exactly R=1+p(W-1). First consider a *supplied, correctly known baseline* x just before an update. The recovery question is to identify any y in H_1(x) using the new scalar observation. This supplied baseline is a typed extra input. A receiver carrying only the preceding w modular reports has a different, potentially harder, decoding obligation.

## Theorem 847.1: complete one-update collision criterion

For q>=1 define the finite positive integer set

 D_{p,W} =
 {k W^i: 0<=i<p, 1<=k<=W-1}
 union
 {|k W^i - l W^j|:
       0<=i<j<p, 0<|k|,|l|<=W-1}.

Every listed integer is nonzero. At a fixed heartbeat t let q_t=m_t/gcd(m_t,c_t). The observation Y_t is injective on H_1(x) for **every** baseline x if and only if

  (for all d in D_{p,W}) q_t does not divide d.           (847.1)

The exact port lower bound R<=q_t follows.

**Proof.** Equality of two observed residues is equivalent to
m_t | c_t(U(y)-U(z)), hence to q_t | U(y)-U(z).
If y,z arise from the same baseline by changing the *same* digit, their nonzero difference has the form k W^i, 1<=|k|<=W-1. If they change different digits i,j, their difference has the form kW^i-lW^j with nonzero signed k,l in the prescribed range. Every such difference can be realized: for each signed digit increment choose its baseline digit at an endpoint that admits the increment, independently for coordinates i and j. Distinct-position differences cannot be zero, because equality would imply a nonzero coefficient of magnitude below W is divisible by W. Thus the list describes exactly the universally possible collisions. Condition (847.1) is necessary and sufficient. The Hamming ball has R states, so an injective residue port must have q_t>=R. QED.

This is a scope-exact *update neighborhood* result. It retains named digit positions, including the composite powers W^i and their cross-differences, rather than replacing the joint source relation by a sum-only statistic.

## Theorem 847.2: optimal permanent scalar modulus with a known baseline

Define

 q_* (p,W,C) = min {q>=1: gcd(q,C)=1 and no d in D_{p,W} is divisible by q}.

This minimum exists. A fixed raw modulus q_* recovers every one-coordinate update from a known prior state, at every t>=1. Furthermore, among all bounded-width predetermined sequences of raw moduli m_t that must recover the update after **every sufficiently late heartbeat**, the smallest possible maximum port width is exactly

  B_local(p,W,C)=ceil(log2(q_*(p,W,C))).                    (847.2)

In particular,

  1+p(W-1) <= q_* <= min{q>=N:gcd(q,C)=1}
               <= N+rad(C)-1,                             (847.3)

with rad(1)=1.

**Proof.** gcd(q_*,C)=1 implies gcd(q_*,c_t)=1 for all t; Theorem 847.1 therefore gives injectivity at every t, and a direct decoder simply enumerates H_1(x), finding the unique element with the observed residue. Conversely, suppose every modulus in a predetermined schedule has m_t<=2^B. For sufficiently large t, uniformly over this *finite* set of possible m_t, the gain c_t contains every C-supported prime power occurring in m_t. Therefore q_t=m_t/gcd(m_t,c_t) is the C-coprime part of m_t, and q_t<=2^B. By Theorem 847.1 any universally correct local update decoder requires q_t to be collision-free, hence q_t>=q_*. Thus 2^B>=q_*; the constant modulus achieves equality of the bit-width bound. The interval bound is immediate: any q>=N avoids all nonzero differences (each is at most N-1), and among any rad(C) consecutive integers there is an integer congruent to 1 modulo rad(C). QED.

## Corollary 847.3: last-heartbeat causal barrier for autonomous window decoding

Suppose a receiver must decode the **current last state** from every length-w window of scalar reports, the update law permits a single arbitrary named-coordinate change at the last heartbeat of the window, and the receiver is not otherwise given the update. Then any predetermined port schedule working for all admissible trajectories must satisfy

  B >= B_local(p,W,C),                                    (847.4)

independently of w, even if the receiver is granted the entire pre-update state for free.

**Proof.** Choose any baseline and a trajectory that stays there until the final heartbeat. All earlier reports are identical across the possible last updates. Even giving the decoder the exact baseline only makes the decoding task easier. It must distinguish H_1(x) using the last report alone, so Theorems 847.1-847.2 impose the lower bound at arbitrarily late windows. QED.

A comparison with PREFIX-846 now becomes precise. PREFIX-846's width/latency equality applies to a constant U throughout its observation window. Under source changes, those earlier CRT residues refer to a different U; applying their CRT reconstruction without carrying an update residual produces an incorrect final-state claim. Theorem 847.2 supplies a constructive local repair when the baseline is already known, but does **not** assert that a receiver retaining only w past scalar reports can always obtain that baseline.

## Finite exact certificates and concrete values

The accompanying executable enumerates D_{p,W}, tests every admissible C-coprime modulus from 1 upward to the first collision-free q, and checks the R-state counting lower bound. Its exhaustive domain comprises all 60 cases p=1..5, W=2..5, C in {1,2,6}. For every p<=4,W<=4 it independently enumerates *all* baseline digit tuples, all permitted single-coordinate updates, and every modulus q in 1..N+2, verifying that (847.1) agrees with literal injectivity. It also checks the actual c_t-weighted BRC readout at t=1,2,4,9 for p=3,W=3,a=2,b=3,m=13 and S=5. All arithmetic is exact (bounded JS integer computations plus BigInt for gains).

Representative minimal permanent local moduli:
- p=3, W=3, C=6: q_*=13, four bits, versus N=27 full tuples.
- p=5, W=5, C=6: q_*=59, six bits, versus N=3125 full tuples (twelve bits of unrestricted identity).
- p=4, W=2, C=2: q_*=11, four bits, versus N=16 (four bits).

The saving for p=5,W=5 applies because the receiver has the previous complete named tuple. Its complete information-storage and synchronization costs must be included before claiming end-to-end compression.

## Source boundaries and next research question

The positive-integer BRC scalar observation is an explicitly typed derived observer; underlying named provenance, signed native relations, interaction paths and six-axis X6 state remain outside this quotient until a scope-exact observer/future-operation bridge is proved.

Next exact question: characterize the smallest finite-state decoder that can recover **all** Hamming-one evolving source trajectories from windows alone (without the previous-tuple oracle). A concrete first case is p=2, W=2 and w=2 with a,b fixed: determine whether any sub-full-width schedule is sufficient, and quantify the minimal repair state if it is not. Also test modulo choices with bounded update magnitude, event-time stamps and admissible native Cell/Link/Port input before asserting transfer to X6.

**Reproduction:** `node PREFIX847_R6_DYNAMIC_SOURCE_LOCAL_CHECK.js > PREFIX847_R6_DYNAMIC_SOURCE_LOCAL_RESULTS.json`.
