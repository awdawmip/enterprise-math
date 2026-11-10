# D25 — Complete four-grade p^4 certificate for the original W216 truncation

Date 2026-11-10 (+08:00); AUTHOR_SIDE_EXACT_ALGEBRAIC_PROOF / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3.

## Statement

For every prime p=6m+1>3 let A_k=binom(2k,k)^2 binom(3k,k)/216^k and W_p=sum_{k=0}^{p-1}(6k+1)A_k. All rational expressions below lie in Z_(p). Put H_n^(r)=sum_{j=1}^n 1/j^r and D_{n,k}^(r)=H_n^(r)-H_{n-k}^(r). The native original index and weight are kept throughout.

Grade 0, 0<=k<=2m: B_k=(-1)^k 2^(-k) binom(2m,k)binom(3m,k)binom(4m,k). Define

 alpha_k=D_(2m,k)^(1)/3 + D_(3m,k)^(1)/2 + 2D_(4m,k)^(1)/3,
 beta_k=D_(2m,k)^(2)/9 + D_(3m,k)^(2)/4 + 4D_(4m,k)^(2)/9,
 gamma_k=D_(2m,k)^(3)/27 + D_(3m,k)^(3)/8 + 8D_(4m,k)^(3)/27.

**New grade-0 third p-adic jet:**

 A_k = B_k * [1-p alpha_k + p^2(alpha_k^2-beta_k)/2
               +p^3(-alpha_k^3+3alpha_k beta_k-2gamma_k)/6] (mod p^4).   (J0-3)

Grade 1, 2m<k<=3m: use the previously constructed positive p-unit
 T_k=(2m)!(k-2m-1)!(3m)!(4m)!/[(3m-k)!(4m-k)!(k!)^3 2^k].
Put
 gamma1_k=[H_(k-2m-1)^(1)-H_(2m)^(1)]/3
          -D_(3m,k)^(1)/2 -2D_(4m,k)^(1)/3,
 delta1_k=[H_(k-2m-1)^(2)+H_(2m)^(2)]/9
          +D_(3m,k)^(2)/4+4D_(4m,k)^(2)/9.

**New grade-1 second p-adic jet:**

 A_k = (p/3) T_k * [1+p gamma1_k+p^2(gamma1_k^2-delta1_k)/2] (mod p^4).   (J1-2)

These are exact congruences for every stated prime and index. At the same precision the already-proved grade-1/grade-2 first-jet reflection gives, for k_j=2m+1+j (0<=j<m), L_j=A_(k_j)/p (mod p^2), C_p=L_0*(A_(p-k_0)/p^2) (mod p^2), E_j=sum_{r<j} e_r where
 e_r=-3/k_r +2/(2k_r+1)+3/(3k_r+1)+3/(3k_r+2) (mod p),

 A_(p-k_j)/p^2 = C_p*(k_0/k_j)^3*(1+pE_j)*L_j^(-1) (mod p^2).           (J2-1)

For grade 3, consume the new exact original inverse-reflection theorem:

 W_(3,p)/p^3 = sum_{h=1}^{2m}(6h-1)/(18h^3 A_h) (mod p).                (G3)

Assemble W_p (mod p^4) by taking the original signed weighted sum of J0-3 and J1-2, then p^2 times J2-1 with the original weight 6(p-k_j)+1, then p^3 times G3. This is a **complete explicit finite certificate** for the original W216 fourth digit, without dropping any valuation layer, cutoff, weight, or carry.

## Proof

Write exactly (1/3)_k=(-2m+p/3)_k, (1/2)_k=(-3m+p/2)_k, (2/3)_k=(-4m+2p/3)_k, retaining the 2^(-k) prefactor. For grade 0 each zero-order factor is a p-unit. For a unit product of factors (1+p a_j), let S_r=sum a_j^r. Its cubic expansion is
  1+p S_1 +p^2(S_1^2-S_2)/2 +p^3(S_1^3-3S_1S_2+2S_3)/6.
Here S_1=-alpha, S_2=beta, S_3=-gamma; (J0-3) follows coefficientwise.

For grade 1 remove the unique zero-order factor p/3 (the j=2m factor of (1/3)_k) before expanding. The retained nonzero factors have first logarithmic sum gamma1, and square-sum delta1; the quadratic product expansion yields (J1-2). Factorials in T_k, all harmonic denominators and 2,3,6 are p-units. Grades 2 and 3 have valuations exactly 2 and 3 respectively, so the already proved J2-1 and G3 possess precisely the missing p-adic accuracy. The disjoint four-grade partition then proves the assembled congruence term-by-term; no unproved cancellation is used.

## Executed exact checker

Independent original integer binomial coefficients are compared with (J0-3) and (J1-2) coefficient-by-coefficient; grade 2 uses the existing signed reflected first jet and grade 3 the new full inverse sum. The final assembled W (mod p^4) is compared to an independent direct sum of all p original terms. Standard library modular arithmetic, no floating point. All 80 primes p<=1000 with p=1 (mod6) PASS.

Selected original W_p modulo p^4: p=13:19786, p=19:82327, p=373:11832087049. At p=373, W_(3,p)/p^3=278 and (W_p-p)/p^3=228 modulo p. This is a finite observation, not a uniform fourth-digit supercongruence or a native original H0/B0 benchmark.

## Next frontier

The missing grade precision at p^4 is now closed algebraically for the original W216 scalar. The remaining substantive proof question is to identify a signed finite WZ/Jacobi telescoper that makes the complete four-grade expression cancel in the appropriate fixed original Delta_p-R_p/216-2304 interface. Prove the preserved bridge before asserting any implication for native LIFT. The highest native required H0/B0 divided-power [X]U mod139129, rank, Frobenius direction/eta, odd kappa and Delta-R, independent replication remain NOT_RUN/PENDING_OWNER (Issue #1559). The current GitHub author note is not a Source checkpoint, role-bound CLAIM, accepted Result or Driver review.
