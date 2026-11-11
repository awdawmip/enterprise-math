# D25/LIFT: a universal Lucas q² carry jet for two labeled Clausen ports

**2026-11-11; H40 TASK_RESEARCH author portable proof.** Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. Frozen scientific Source: c47e13e4aba0e006366f989d6334d443f6333ae3. Continues the H40 mod-q prime-power shadow at 5ac5c2ad28a3c5b23b90ebfef90e6c1b406b9d66. **AUTHOR-PROVED; finite integer checked; UNREVIEWED, NOT_ADMITTED; no native CLAIM, checkpoint or H0/B0 experiment.**

## Theorem I: every binomial coefficient has an exact q² digit/borrow jet

Let q>=5 be prime, 0<=k<=n, n=qM+a, k=qK+b, 0<=a,b<q. Put H_j=sum_{i=1}^j 1/i (mod q) for j<q. Define labeled L in Z/q² and R in F_q:

* If b<=a, L=binom(M,K)binom(a,b), R=L[M H_a-K H_b-(M-K)H_{a-b}] (mod q).
* If b>a, set c=b-a. Then L=0, R=(M-K)binom(M,K)(-1)^(c-1)a!(c-1)!/b! (mod q); necessarily M>K.

In both cases binom(n,k)=L+qR (mod q²). All divisions shown are by units mod q.

**Proof.** Since (1+x)^q=1+x^q+q E(x), where E(x)=sum_{i=1}^{q-1}(binom(q,i)/q)x^i, expansion of (1+x)^(qM) modulo q² has correction qM E(x)(1+x^q)^(M-1), which contains no term with degree divisible by q. Therefore binom(qM,qK)=binom(M,K) mod q². If b<=a, divide binom(qM+a,qK+b) by binom(qM,qK): its exact ratio equals
binom(a,b) * prod_{i=1}^a(1+qM/i) / [prod_{j=1}^b(1+qK/j) prod_{h=1}^{a-b}(1+q(M-K)/h)].
Expand the unit factors to first order in q: the bracket is 1+q[M H_a-K H_b-(M-K)H_{a-b}]. If b>a, the exact ratio is
[prod_{i=1}^a(qM+i)/prod_{j=1}^b(qK+j)] prod_{h=0}^{c-1}(q(M-K)-h).
The h=0 factor contributes exactly one q; reducing every other factor modulo q gives the announced R. QED.

## Theorem II: exact provenance-preserving reconstruction of both finite Clausen ports modulo q²

For any m>=0 and epsilon in {0,1}, define F(X)=sum_{k=0}^m binom(m,k)binom(2m+epsilon,k)X^k and A=F(1/2), B=(1-6epsilon)F(1/2)+6F'(1/2). Apply Theorem I to (m,k) and (2m+epsilon,k), obtaining L1,R1 and L2,R2. Write k=qK+b; w_e(b)=1-6epsilon+12b; y=2^-1 mod q². Then:

A = sum_k y^k [L1 L2+q(L1 R2+R1 L2)] (mod q²).

B = sum_k y^k [w_e(b)L1 L2+q{w_e(b)(L1 R2+R1 L2)+12K L1 L2}] (mod q²).

**Proof.** Multiply the two binomial jets; q²R1R2 vanishes modulo q². Differentiate each monomial at X=1/2: the corresponding B-weight is 1-6epsilon+12k=w_e(b)+12qK. QED.

Keep four exact contributor types: neither factor borrowed, only first borrowed, only second borrowed, or both borrowed. The double-borrow type vanishes *at this precision*, not under all future operators. The three explicit joint coordinates are the Lucas core L1L2, first-order binomial jet q(L1R2+R1L2), and derivative weight carry 12qK L1L2. This is a BRC observer statement for the declared mod-q² readout only.

Apply to N=q^r with epsilon_N=0 for N=1 mod6 and 1 for N=5 mod6, m_N=(N-1-4epsilon_N)/6. This **strictly upgrades the earlier mod-q shadow to a mod-q² formula** without claiming a closed factorization into the base ports.

## Discriminating exact cases

The direct binomial algorithm and the digit-jet algorithm agree at:

* N=49 (q=7): (A_N,B_N)=(46,0) mod49, whereas base (A_7,B_7)=(2,14) mod49. Naively lifting the old mod-q formula to q² gives (A_7²,A_7 B_7)=(4,28), **wrong by (42,21) modulo 49**.
* N=169 (q=13): (A_N,B_N)=(13,39) mod169, whereas base (A_13,B_13)=(91,6) mod169. A_13²=0 but A_169=13 (mod169). Both higher ports vanish mod13 and both have q-adic order exactly 1.
* N=289 (q=17): (A_N,B_N)=(272,221) mod289, including a nonzero single-borrow contribution (0,119).
* N=841 (q=29): (A_N,B_N)=(485,0) mod841, with one-borrow contribution (638,290).

These counterexamples concern **the naive q² lift of the earlier correct mod-q formula**, not the mod-q theorem itself.

## Validation and next work

Exact independent computation checked all 0<=k<=n<=120 for every prime 5<=q<=37: **73,810 binomial comparisons including 30,173 borrow cases**, all matching. It also checked every prime-power input q<=997 with m_N<=600 from the preceding H40 family: **188 exact two-port comparisons**, including 22 exponents r>=2; all matched. Full integer certificate, independent Python verifier and an expanded manuscript are included in the user-delivered portable ZIP. No numerical approximation is used.

Next mathematical unit: q³ carry composition, where the double-borrow channel q²R1R2, higher harmonic jets and weight carry interact, and whether those terms control exact q-adic valuations of the supersingular higher-port pair. The original D25/LIFT hard target remains original-class H0/B0 divided powers, [X]U mod p², semilinear Frobenius normalization eta, and the bridge to kappa and Delta_p-R_p. UR V2 94,687-byte four-file original and expected SHA-256=4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 still need actual-byte provenance; previously completed UR mathematics need not be redone.
