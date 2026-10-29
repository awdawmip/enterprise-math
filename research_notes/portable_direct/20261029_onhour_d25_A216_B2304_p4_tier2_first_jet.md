# D25 / SECOND-DIGIT-LIFT — Original A216/B2304 valuation-two first jets through p^4

2026-10-29 Asia/Hong_Kong. Classification: AUTHOR-SIDE / ALGEBRAIC THEOREM PROVED / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Task publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3; unchanged.
Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923.
This note grants no native session/claim/run/Result and does not adopt any maintenance conversation identity.

## Retain both actual signed streams (BRC carrier)

For a prime p>=5 and integers 0<=n<p, take the distinct original rational coefficients

\[
a_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},\qquad
b_n=\frac{(4n)!}{(n!)^4 2304^n},
\]

\[
A_p=\sum_{n=0}^{p-1}(6n+1)a_n,\qquad
B_p=\sum_{n=0}^{p-1}(8n+1)b_n.
\]

The retained BRC carrier is two separately labelled exact-weight streams, recording index, valuation, signed weight, and first harmonic jet in the ring Z/p^4. The derived joint observer is A_p-2B_p+p chi_p, where chi_p=(-3/p). This is an auxiliary p-adic scalar observer, not native H0/B0 or a substitute for original Green/Hesse measurements.

The *valuation-three* top source reflection, including its signed gap D_p, was proved and published separately in the 2026-10-29 author note at commit 64f29780c682ae896aff65d617e314c85ece6b96. This unit establishes the previously missing *valuation-two* first jets at full fourth-digit precision. The full p^4 bridge remains a candidate, not a theorem.

## Factorial block lemma (proved)

Let H_j=sum_{i=1}^j i^{-1} in F_p, H_0=0; define W_p=((p-1)!+1)/p mod p and q_p(c)=(c^(p-1)-1)/p mod p for p∤c. All factorial indices below lie in 0,...,p-1, so every displayed division is by a p-unit.

For each k=1,2 and 0<=s<p, the identity of p-adic units modulo p^2 is

\[
\frac{(kp+s)!}{p^k}\equiv k!((p-1)!)^k s!(1+kpH_s)\pmod{p^2}. \tag{F1}
\]

To prove it, remove the k explicit multiples p,2p,...,kp. Each of k completed unit blocks is (p-1)! times a product of (1+jp/i), i=1,...,p-1; because H_(p-1)=0 mod p, each block correction is 1 mod p^2. The final unit block is s!(1+kpH_s) mod p^2. Wilson's theorem gives (p-1)!=-1+pW_p mod p^2. Reflecting the terminal factorial gives, for 0<=r<p,

\[
(p-1-r)!\equiv\frac{(-1)^{r+1}}{r!}
[1+p(H_r-W_p)]\pmod{p^2}. \tag{F2}
\]

Also c^{-(p-1)}=1-pq_p(c) mod p^2 for p∤c.

## Theorem A — original A216 valuation-two source, modulo p^4

Let ceil(p/2)<=n<2p/3, r=p-1-n, t_2=2r+1, t_3=3r+2-p, s_2=2n-p and s_3=3n-p. All r,t_2,t_3,s_2,s_3 are in [0,p-1]. Set

\[
C_{A,r}=216^r\frac{(r!)^5}{t_2!t_3!},\qquad
\Xi_{A,r}=H_{t_2}+H_{t_3}+H_{s_2}+H_{s_3}
-5H_r+W_p-q_p(216)\pmod p.
\]

Then v_p(a_n)=2 and the original signed weighted coefficient satisfies

\[
\boxed{\frac{(6n+1)a_n}{p^2}\equiv C_{A,r}
\left[(6r+5)+p\big((6r+5)\Xi_{A,r}-6\big)\right]\pmod{p^2}.} \tag{A2}
\]

Proof: 2n=p+s_2 and 3n=p+s_3. Apply (F1) with k=1 to both factorials and divide the two-unit-block result by (n!)^5. Apply (F2) to s_2!, s_3! and n!, then substitute 216^{-n}=216^r(1-pq_p(216)) mod p^2. Reflection parity makes the unweighted normalized coefficient negative. Finally 6n+1=6p-(6r+5) reverses that sign. Collect the harmonic terms; the Wilson-quotient coefficient is exactly +1, yielding Xi_A. Every step is an equality of rational p-adic units modulo p^2, so multiplication by p^2 yields the stated fourth-digit congruence.

## Theorem B — original B2304 valuation-two source, modulo p^4

Let ceil(p/2)<=n<3p/4, r=p-1-n, t=4r+3-p and s=4n-2p. All r,t,s lie in [0,p-1]. Put

\[
C_{B,r}=2\cdot2304^r\frac{(r!)^4}{t!},\qquad
\Xi_{B,r}=H_t+2H_s-4H_r+W_p-q_p(2304)\pmod p.
\]

Then v_p(b_n)=2 and

\[
\boxed{\frac{(8n+1)b_n}{p^2}\equiv C_{B,r}
\left[(8r+7)+p\big((8r+7)\Xi_{B,r}-8\big)\right]\pmod{p^2}.} \tag{B2}
\]

Proof: 4n=2p+s. Apply (F1) with k=2, reflect s! and (n!)^4 with (F2), and use 2304^{-n}=2304^r(1-pq_p(2304)) mod p^2. Since t is even for odd p, the normalized unweighted reflected coefficient has a negative leading sign. The original weight 8n+1=8p-(8r+7) reverses that sign. The full-block, reflection and denominator terms sum to Xi_B above. This is not the previously known valuation-three reflected B top.

## Exact, source-preserving reduction of the p^4 bridge

Let A_p^(j) and B_p^(j) denote the original index sets where v_p(a_n)=j and v_p(b_n)=j. For n<p these are exactly j=floor(2n/p)+floor(3n/p) and j=floor(4n/p). Define

\[
Q_p=(A_p^{(2)}-2B_p^{(2)})/p^2\bmod p^2,
\qquad
D_p=(A_p^{(3)}-2B_p^{(3)})/p^3\bmod p.
\]

The two new proved expressions (A2) and (B2) give the entire Q_p. The previously proved top reflection gives D_p. Denote the untouched valuation-zero and valuation-one signed stream by

\[
C_p^{(01)}
=A_p^{(0)}+A_p^{(1)}
-2(B_p^{(0)}+B_p^{(1)})+p\chi_p.
\]

Without assuming any supercongruence, exact source decomposition gives

\[
\boxed{A_p-2B_p+p\chi_p
\equiv C_p^{(01)}+p^2Q_p+p^3D_p\pmod{p^4}.} \tag{PORT}
\]

The next **smallest unfinished theorem** is the character-sensitive valuation-zero/one cancellation

\[
C_p^{(01)}\stackrel{?}{\equiv}-p^2Q_p-p^3D_p
\pmod{p^4}\qquad(p>3),
\]

or the weaker original frozen target A_p-B_p=0 mod p^3 on p≡13,19 mod 24, using the independently proved Guo–Zudilin B_p theorem. The PORT identity is proved algebra; the cancellation above remains a conjecture.

## Independent exact-integer execution

The reproducible program d25_a216_b2304_p4_tier2_reflection_portable_20261029.py performs per-term evaluation of (A2) and (B2) in Z/p^2 and independently generates **original** coefficients by two different recurrences modulo p^4. It additionally checks untransformed binomial sums, term by term, at p=5,7,11,13,19,31,373.

Executed result: PASS 237 primes 5<=p<1500; **68,767 separately weighted valuation-two terms** matched and the aggregated A/B tier-two sums matched.

| p | A^(2)/p^2 mod p^2 | B^(2)/p^2 mod p^2 | Q_p mod p^2 | D_p mod p (prior) | observed C^(01)/p^2 mod p^2 |
|---:|---:|---:|---:|---:|---:|
| 13 | 75 | 39 | 166 | 6 | 94 |
| 19 | 161 | 114 | 294 | 10 | 238 |
| 373 | 68898 | 87282 | **33463** | **40** | **90746** |

At p=373 the finite original bridge residual cancels: 90746+33463+373*40=139129=373^2. This is an exact finite certificate, not an all-prime proof.

## Durable continuation / authority

High valid author-side frontier: new A/B valuation-two p^4 jet and the prior A/B valuation-three top; no need to repeat either. Frozen Source pin, signed original coefficients, two residue classes and P000 unchanged. Native H0/B0 support issue #1559 still requests an actually authorized fixed-p373 divided-power evaluator, [X]U modulo 139129, actual module rank, semilinear Frobenius direction/eta, odd signed Green/Hesse, kappa and independently validated readouts. The Site on this run reported research_authority_granted=false and write_relay_enabled=false; em_checkpoint_list returned ACCESS_DENIED. Those are client-scoped observations. No original native experiment, Researcher CLAIM, formal Source checkpoint, Result or Driver acceptance is asserted. Next formal continuation must recover native request/session ownership from Source, with the Researcher conversation ID above, on an authorized execution path.
