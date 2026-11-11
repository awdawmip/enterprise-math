# D25/LIFT: fourth-digit harmonic decomposition with a retained carry

Date 2026-11-11. Status: AUTHOR_PROVED / EXACT_167_PRIME_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED. Portable author-side continuation of the third-digit source note at commit ce1b5ac8e4ac050501acb5b5c6043d7a39c35d7b.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Source continuation h40-20261111-1243-exact-continuation read SUCCEEDED at a34388855bee7ed2873033f15b679aa69874caea, execution_authorized=false. Native experiment, CLAIM and Result remain separate.

## Theorem (all primes p>=5; Z_(p) arithmetic)

Uniquely write p=6m+1+4epsilon, epsilon=0 or 1. Let alpha=-(1+4epsilon)/6 and beta=-(1+epsilon)/3. For k=0,...,m put t_k=binom(alpha,k)binom(beta,k)/2^k. For 0<=j<k put u_j=1/(6j+1+4epsilon), v_j=1/(3j+1+epsilon), and H_{r,k}=sum_{j<k}(u_j^r+v_j^r) for r=1,2,3.

Define e_{2,k}=(H_{1,k}^2-H_{2,k})/2 and e_{3,k}=(H_{1,k}^3-3H_{1,k}H_{2,k}+2H_{3,k})/6.

Let K(X)=sum_{k=0}^m binom(m,k)binom(2m+epsilon,k)X^k, with two distinct ports A=K(1/2) and B=(1-6epsilon)K(1/2)+6K'(1/2). For P=A use rho_P(k)=1; for P=B use rho_P(k)=1-6epsilon+12k. Preserve four source-labelled observations:

S_P = sum_k rho_P(k)t_k,
E_P = sum_k rho_P(k)t_k H_{1,k},
J_P = sum_k rho_P(k)t_k e_{2,k},
L_P = sum_k rho_P(k)t_k e_{3,k}.

Then for both ports simultaneously,

**P = S_P - p E_P + p^2 J_P - p^3 L_P (mod p^4).**

If P=0 (mod p^2), then S_P/p and C_P=(S_P/p-E_P)/p lie in Z_(p), and

**P/p^2 = C_P + J_P - p L_P (mod p^2).**

Write C_P=c_0+p c_1 mod p^2, J_P=j_0+p j_1 mod p^2, and L_P=l_0 mod p, all digits chosen in 0,...,p-1. The third and fourth digits of P are

**d_2=(c_0+j_0) mod p** and
**d_3=(c_1+j_1+floor((c_0+j_0)/p)-l_0) mod p**.

The explicit addition carry records an observer-dependent source term not recoverable by separately reducing and then simply adding the fourth digits.

## Proof

The exact rational equalities m=alpha+p/6 and 2m+epsilon=beta+p/3 imply, term-by-term,

binom(m,k)binom(2m+epsilon,k)/2^k =
t_k product_{j<k}(1-pu_j)(1-pv_j).

All denominators are p-units since j<m and p>=5. The first three elementary symmetric sums in the 2k factors u_j,v_j are respectively H_1, (H_1^2-H_2)/2, and (H_1^3-3H_1H_2+2H_3)/6. Expand the product through p^3 and sum with rho_P. Reductions modulo p and p^2 when P=0 mod p^2 establish the two divisibilities. Division by p^2 and canonical base-p digit collection establish the last two formulae.

This is a concrete order-four extraction from the previously identified arbitrary-order product, preserving the carry and the new third elementary-symmetric port. It does not alter the unresolved universal Legendre-selector or the native LIFT source map.

## Exact checks

Two integer paths independently compute (i) binom(m,k)binom(2m+epsilon,k)/2^k and (ii) rational-alpha/beta t_k and H_1/H_2/H_3, all modulo p^4. Every prime 5<=p<=1000 (166 primes), plus prime p=101419, passed both-port comparison (167 primes). A separate exact Fraction comparison of the untruncated finite product passed for both epsilon branches and all m<=7.

| p | port | c0 | j0 | d2 | c1 | j1 | add carry | l0 | d3 | P mod p^4 |
| ---: | :---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 149 | B | 13 | 5 | 18 | 1 | 28 | 0 | 94 | 84 | 278267334 |
| 211 | A | 22 | 152 | 174 | 69 | 77 | 0 | 9 | 137 | 1294715201 |
| 101419 | A | 35425 | 38207 | 73632 | 98148 | 26053 | 0 | 55136 | 69065 | 72047771727655493387 |

The original complete verified native frontier remains unchanged; this is author mathematical evidence. If the genuine UR V2 bundle is located, verify exactly 94687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 before claiming restoration. Next useful scientific unit: prove the native H0/B0 semilinear and observer map to these source-labelled coefficients, or solve the all-prime (-6/p) zero-port selector.