# PREFIX-861 — Balanced two-read BRC observers by shared-gcd transition labels and CRT

Date: 2026-11-17. Author verification: mathematical proof plus exact integer checks; NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Predecessors: PREFIX-850 (projective binary transition labels), PREFIX-859 (arbitrary two-read collision criterion), PREFIX-860 (offset obstruction).
Frozen scientific source: f42f2906d77f24085c123f3ccfe9667d41caa96d. This is an auxiliary provenance-preserving binary-source BRC observer, not an assertion about native X6 Cell/Link/Port event permission.

## Exact observer model

Let p>=1, N=2^p, x in {0,1}^p and U(x)=sum_{i=0}^{p-1} 2^i x_i in [0,N). One update is a no-op or a flip of one named source bit, hence its *signed* integer increment is in
E_p={0} union {+2^i,-2^i:0<=i<p}.
The initial x is unknown; after observing a normalized residue of U_before mod q1 and U_after mod q2, the decoder must return the **complete terminal named state** x_after. It need not identify the old state or which path occurred.

If the physical BRC readouts are c_t(S+U) mod q_t, assume S and the positive integer c_t are known and gcd(c_t,q_t)=1, so the observations normalize exactly. For the power-of-two heartbeat multipliers used in PREFIX-859, this holds for all the odd moduli below.

## Theorem 861-A — shared-gcd synchronization

Let g>=3, a,b>=1, q1=ga, q2=gb, and gcd(a,b)=1. Assume distinct elements of E_p have distinct residues modulo g, and
lcm(q1,q2)=gab >=N.

Then the ordered two-read observer (q1,q2) uniquely recovers every terminal x, for every legal unknown initial x and every legal one-bit/no-op update.

**Proof.** Normalize both observations and write them r1=u mod q1, r2=v mod q2. Since g divides both moduli, their difference gives
r2-r1 = (v-u) mod g.
The actual signed increment delta=v-u belongs to E_p. Its residues are injective by hypothesis, so delta is uniquely recovered. Then v satisfies simultaneously
v = r1+delta (mod q1), v = r2 (mod q2).
The congruences are consistent for the observed history; generalized CRT determines v modulo lcm(q1,q2)=gab. Since 0<=v<N<=gab, exactly one permitted terminal integer exists. Its binary expansion recovers all p named sources. QED.

This is a constructive decoder: look up the unique delta in E_p from (r2-r1) mod g, solve the two compatible congruences by integer CRT, then select v in [0,N).

## Theorem 861-B — projective order exactly characterizes safe transition labels

For any odd g>1, residues of E_p modulo g are pairwise distinct **if and only if**
h(g):=min{d>=1: 2^d is +1 or -1 modulo g} >= p.

**Proof.** Oddness of g distinguishes 0 from every signed power, and distinguishes +2^i from -2^i for the same i. For i>j, a collision of signed powers occurs iff 2^{i-j} is +1 or -1 modulo g. The exponent difference lies in 1,...,p-1. This is equivalent to h(g)<p. QED.

For g=3^s, h(g)=3^{s-1}, by the 3-adic valuation of 2^{2n}-1 and the odd-power negative branch (alternatively by induction on s). Thus a uniform choice is
g(p)=3^{1+ceil(log_3 p)} < 9p.
Here ceil(log_3 p) means the exact least nonnegative integer k with 3^k>=p, not a floating-point computation.

## Corollary 861-C — balanced ports for every number of named sources

Choose g=g(p), let a be the **least positive odd integer** with
g a(a+2) >= 2^p,
and set (q1,q2)=(g a,g(a+2)).
The two moduli are odd, gcd(q1,q2)=g, and the observer is terminal-state lossless.

If B(p) is the larger raw port width, then
B(p)=ceil(log_2(q2+1)) (q2 odd)
and
q2 < sqrt(g 2^p)+4g < 3 sqrt(p 2^p)+36p.
Consequently
B(p) <= p/2 +(1/2)log_2 p + O(1).
All p are covered; for p>=11 both moduli are strictly less than 2^p, so each individual read is noninjective.

**Proof of bound.** Let X=N/g. Since a is the first positive odd with a(a+2)>=X, it lies below sqrt(X+1)+1, including a=1. Thus a+2<sqrt(X+1)+3<sqrt(X)+4, proving the first bound. g<9p implies the second. For p>=11, g<9p<=N/16, so q2<N/4+N/4=N/2<N (using the first bound). QED.

## Corollary 861-D — asymptotically half-width single ports

For any two-read protocol capable of recovering all N terminal states, q1*q2>=N: choose one legal history for each terminal and note that distinct terminals require different residue pairs. Hence its maximal raw width B satisfies B>=ceil(p/2).

Combining this lower bound with the explicit construction proves that the optimal peak width for terminal-state recovery in the (noninjective for p>=11) odd-modulus setting obeys
p/2 <= B_opt(p) <= p/2 + (1/2)log_2 p+O(1).
The relative peak width tends to one half of the full p-bit named state representation. This is a bound, not an exact finite-p optimum, and total communication remains approximately p+log_2 p bits.

## Exact checks and results

The accompanying standard-library Python program generates g and consecutive odd factors for p=1,...,18; verifies h(g)>=p, that all 2p+1 increments differ modulo g, gcd(q1,q2)=g, and lcm>=N. For p=1,...,12, it also directly enumerates every N(p+1) no-op/single-bit-flip trajectory and checks that equal observed residue pairs always have equal terminal integer. Integer arithmetic is exact; output: ALL_EXACT_ASSERTIONS_PASSED.

Sample records (p,g,q1,q2,maximum bits):
(8,27,81,135,8); (9,27,135,189,8); (10,81,243,405,9);
(11,81,405,567,10); (12,81,567,729,10); (16,81,2349,2511,12).
The construction is deliberately general, and may be worse at small p than the individually optimized PREFIX-859 table.

## Preserved information, boundaries and next question

All p named source bits remain the terminal scientific state. The CRT residue pair is an observation/decoding interface with a declared two-heartbeat horizon; it is not a license to discard the named state or ordered source provenance for future operations. Source history and signed flip type can remain different even if terminal U is identical. The two-read terminal observer does not establish an indefinitely lossless sliding-window observer nor a native X6 time-event embedding.

Next mathematical problem: tighten the analytic gap between ceil(p/2) and p/2+(1/2)log_2 p+O(1) for exact odd two-read peak width, and classify choices of g,a,b achieving smaller finite-p widths without losing the transition-residue uniqueness property.
