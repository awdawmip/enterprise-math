# C307 — Pointwise-optimal heterogeneous modular Newton observations

Date: 2026-10-26. Status: AUTHOR_PROOF / EXACT_FINITE_CHECKS / NOT_SOURCE_ADMITTED. Subject: integer-polynomial content arithmetic, with a conditional application to the C195/H168 79-positive-rational-branch auxiliary scalar model. This is not a native GF(2)-BRC/X6 dynamics theorem.

## Exact provenance

Canonical account knowledge: awdawmip/chatgpt-global-knowledge main@3f5265ba9cb837a6d9b3ba272de8106f751e8d34. Source-control routing: awdawmip/enterprise-math main@f67a9840c8e8b0d9420366d8049e689f8f1abf1b. Read current GLOBAL_KNOWLEDGE_V1 bootstrap/manual, P000 startup projection and blob (matching canonical SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview, TASK route and current portable-research protocol. Mathematical predecessor: C306 author commit d204fa8d28b88722c92ba54a36f8b76aa4fc7aad, with complete frozen user-supplied C306 portable package and its C305 exact gcd witnesses. C293 frozen records SHA256: 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89.

C306 proved a smallest uniform modulus. C307 asks for optimal per-node moduli with the same consecutive integer sample nodes and universal polynomial class.

## C307 theorem: coordinatewise minimal observation moduli

Let s >= 1, d >= 0, T be an integer. Let P(t) be any integer polynomial of degree at most d. Define content(0)=0 and G(P)=gcd(s,content(P)). Set

\[
h=\prod_{p\mid s}p^{v_p(d!)},\qquad M=s h,
\]
\[
\boxed{N_j=\frac{M}{\gcd(M,\binom dj)}
=\prod_{p\mid s}p^{v_p(s)+v_p(j!)+v_p((d-j)!)}},\quad 0\le j\le d. \tag{1}
\]

Here the product is mathematical notation; neither computing h nor N_j requires prime factorization.

**Sufficiency.** The data P(T+j) mod N_j for j=0,...,d determine G(P) exactly.

**Individual sharpness.** If arbitrary positive moduli L_0,...,L_d yield a residue vector that determines G(P) for every integer polynomial of degree <=d, then N_j divides L_j for each j. Thus (N_j) is the unique smallest fixed nonadaptive modulus schedule in the componentwise divisibility ordering. This lower bound does not extend to adaptive queries, other node sets, coefficient access or a restricted model family.

### Proof of the formula

For p dividing s, v_p(M)=v_p(s)+v_p(d!). The p-adic valuation of binomial(d,j) is v_p(d!)-v_p(j!)-v_p((d-j)!), between 0 and v_p(d!). The integer M has no prime divisors outside s. Dividing M by gcd(M,binomial(d,j)) gives (1). In particular N_0=N_d=M, N_j=N_(d-j), and N_j divides M.

### Proof of sufficiency

For 0<=k<=d define the falling-factorial polynomial

\[
e_k(t)=\prod_{i=0}^{k-1}(t-T-i),\quad e_0(t)=1.
\]

The e_k are monic integer polynomials of pairwise distinct degrees k, hence they form an integral unitriangular basis of integer polynomials of degree <=d. Write P=\sum_{k=0}^d B_k e_k with B_k integers. Consequently content(P)=gcd(B_0,...,B_d) up to sign. Newton's finite-difference identity is

\[
\Delta^kP(T)=\sum_{j=0}^k(-1)^{k-j}\binom kjP(T+j)=k!B_k. \tag{2}
\]

Choose nonnegative representatives r_j=P(T+j) mod N_j. For each prime p|s put a=v_p(s). The valuation of the error contributed by one replacement P(T+j)->r_j in the kth difference satisfies, for j<=k<=d,

\[
\begin{aligned}
v_p(\binom kj N_j)
 &=v_p(k!)-v_p(j!)-v_p((k-j)!)\\
 &\quad+a+v_p(j!)+v_p((d-j)!)\\
 &=a+v_p(k!)+v_p((d-j)!)-v_p((k-j)!)\\
 &\ge a+v_p(k!).
\end{aligned}\tag{3}
\]

Thus the difference of the representative residues is congruent to k!B_k modulo s a_k, where a_k=gcd(k!,h) is precisely the s-supported part of k! and b_k=k!/a_k is coprime to s. Define

\[
\delta_k=\left(\sum_{j=0}^k(-1)^{k-j}\binom kjr_j\right)\bmod(s a_k).
\]

Because the true difference is a_k b_k B_k, delta_k is divisible by a_k as an integer. Let

\[
\beta_k=(\delta_k/a_k)b_k^{-1}\bmod s.
\]

Then beta_k=B_k mod s, so

\[
\boxed{G(P)=\gcd(s,\beta_0,\ldots,\beta_d).}\tag{4}
\]

For s=1 the answer is trivially 1; d=0 and the zero polynomial are also covered. All operations are exact integer arithmetic. This proves sufficiency.

### Proof of individual sharpness

Fix j and suppose a proposed universally sufficient L_j satisfies v_p(L_j)<v_p(s)+v_p(j!(d-j)!) for some prime p|s. Form the monic degree-d polynomial

\[
q_j(t)=\prod_{0\le i\le d,\ i\ne j}(t-T-i).
\]

It vanishes at all sampled nodes except j, and |q_j(T+j)|=j!(d-j)!. Let c=L_j/gcd(L_j,j!(d-j)!), let P_0=0 and P_1=cq_j. Their residues match under the entire proposed schedule: at all other nodes both are zero, and at node j the value of P_1 is divisible by L_j. But content(P_1)=|c| because q_j is monic, and

\[
v_p(c)=\max(0,v_p(L_j)-v_p(j!(d-j)!))<v_p(s).
\]

Hence G(P_1) differs from G(P_0)=s, contradicting sufficiency. Thus every proposed L_j contains the required p-power for each p|s, and N_j divides L_j. For s=1 all N_j=1. This proves the sharpness claim.

## Exact factorization-free algorithm

Compute f=d!, then repeatedly extract gcd(u,s) from u=f to obtain h; let M=sh. Compute N_j=M/gcd(M,binomial(d,j)) for all nodes. Evaluate the actual P(T+j) only modulo N_j, yielding r_j. Successively compute finite differences on these representatives, reducing intermediate differences modulo M to bound integer size. At layer k reduce the first difference modulo s*gcd(k!,h), exactly divide by a_k, multiply by the modular inverse of b_k=k!/a_k modulo s, and accumulate gcd(s,beta_k). The difference phase uses d(d+1)/2 modular subtractions and O(d log M) bits of working row storage. Observation precision is coordinatewise optimal but this fact does not prove an equal saving of runtime or peak memory.

Example: s=10,d=4 gives C306 common M=80 but the C307 schedule is (80,20,40,20,80).

## Exact verification and honest coverage

The general theorem is proved above by hand, not Lean-admitted. A separate bounded checker examined 3,630 exact integer polynomial cases (d=0..9, s=1..121; fixed random seed 30720261026, signed coefficients/starts, zero polynomial included); every G matched its direct coefficient oracle. It constructed 11,660 explicit omitted-prime-power indistinguishability witnesses. These tests check implementation and are not the universal proof.

On all 125 frozen auxiliary-model paths, a separate exact schedule audit recomputed the underlying factorized denominator parameters and their s,d values from the frozen C293 input, verifying 44,038 pointwise N_j formulae, consistency with all 125 C306 uniform moduli and prior exact-gcd witnesses. Results: 43,788 node moduli smaller than C306; 250 endpoint nodes equal to M; median per-node width saving 57 bits, maximum 121 bits; total of all individual bit-width savings 2,479,184 bits. That sum is not a runtime or memory reduction claim. The schedule audit did not re-evaluate all 44,038 reduced-numerator residues. Separate direct end-to-end varied-modulus circuit checks completed for paths 0, 28 and 63, with the reconstructed gcd identical to the C305 exact author oracle. Other interrupted batch logs show additional completed per-path comparisons but not an all-125 finished numerical rerun.

The scientific implication for the other paths follows from the proven universal theorem plus C306's previously computed exact residues and gcds; it inherits C300/C305/C306 author-level input and cancellation assumptions. There is no newly independent exhaustive review of all 125 circuit evaluations.

## BRC, role and next work

This is integer-polynomial content recovery for a declared scalar observable, not a proof that scalar compression preserves joint signed/phase BRC state, branch provenance, ports, future operations or the native six-axis X6 Cell system. The original 79 branch inputs remain frozen; P000 and ACTIVE worldview are unchanged.

Connected GitHub identity was awdawmip with push permission. The canonical native control attempts em_control_tasks and em_control_dispatch returned CONTROL_QUOTA; em_session_start(RESEARCHER) returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Live active Owner could not be verified. No Source-native CLAIM, formal Result, Driver review, canonical admission or main merge is asserted. This branch is an author-level research checkpoint only.

C308 next: derive a correct streaming mixed-precision finite-difference recurrence with explicit per-layer p-adic precision invariants and compare exact bit-operation/peak-memory costs on the frozen 79-branch circuit. Seek independent review of the upstream C300-C306 cancellation/content chain and a future-safe typed BRC observer morphism before any native-world transfer.
