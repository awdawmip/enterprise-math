# D25/LIFT — third-digit harmonic decomposition of finite Clausen ports

Date: 2026-11-11. Status: AUTHOR_PROVED / EXACT_RATIONAL_AND_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. A portable author-side extension of the existing second-digit harmonic source note (commit ccb265e48f5bd7ccd8fd1b586e15740b70e39587), not a new native result or a change to frozen inputs.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Statement

For any prime p>=5 choose epsilon in {0,1} uniquely such that p=6m+1+4epsilon with m>=0. Put alpha=-(1+4epsilon)/6 and beta=-(1+epsilon)/3. For 0<=k<=m let

t_k=binom(alpha,k)binom(beta,k)/2^k,
u_j=1/(6j+1+4epsilon), v_j=1/(3j+1+epsilon),
H_k=sum_{j<k}(u_j+v_j),
H2_k=sum_{j<k}(u_j^2+v_j^2),
D_k=(H_k^2-H2_k)/2,
w_k=1-6epsilon+12k.

Define K(X)=sum_{k=0}^m binom(m,k)binom(2m+epsilon,k)X^k, A=K(1/2), B=(1-6epsilon)A+6K'(1/2). For port P=A or B respectively set rho_A(k)=1, rho_B(k)=w_k, and retain the three separate observations

S_P=sum rho_P(k)t_k; E_P=sum rho_P(k)t_k H_k; J_P=sum rho_P(k)t_k D_k.

**Universal third-digit congruence in Z_(p):**

P = S_P - p E_P + p^2 J_P (mod p^3).

If P=0 (mod p^2), then S_P/p and (S_P/p-E_P)/p are p-integral and

P/p^2 = (S_P/p-E_P)/p + J_P (mod p).

In particular the third digit records two different contributions, the first-harmonic carry and the second elementary-symmetric correction. This refines the earlier p^2 result without presuming the all-prime Legendre zero-port selector.

## Exact proof

For each 0<=k<=m, the rational identities m=alpha+p/6 and 2m+epsilon=beta+p/3 give the **exact** finite product:

binom(m,k)binom(2m+epsilon,k)2^{-k}
= t_k * product_{j<k}(1-pu_j)(1-pv_j).

All denominators occurring here are p-units: 0<=j<m<p, 6j+1+4epsilon < p and 3j+1+epsilon < p. The first elementary-symmetric coefficient of the combined multiset {u_j,v_j} is H_k, and the second is (H_k^2-H2_k)/2. Expanding through p^2 yields the congruence modulo p^3. Summing with rho_P(k) proves both ports. If P vanishes mod p^2, its p-local congruence forces S_P divisible by p and S_P/p-E_P divisible by p, so division by p^2 gives the final formula. QED.

The product identity also allows arbitrary fixed p-adic order via further elementary symmetric functions; only the third-digit interface and its exact observed decomposition are asserted as this unit.

## Exact arithmetic certificates

Separate integer recurrences for (i) original binomial coefficients and (ii) alpha/beta base coefficients plus H_k, H2_k agree modulo p^3 for every one of the 166 primes 5<=p<=1000 plus p=101419. A separate rational-sanity check verifies the exact finite-product identity at small inputs. The following table gives all order-two exceptional ports catalogued in the earlier bounded p^2 census:

| p | port | (S_P/p-E_P)/p mod p | J_P mod p | P/p^2 mod p |
| ---: | :---: | ---: | ---: | ---: |
| 149 | B | 13 | 5 | 18 |
| 211 | A | 22 | 152 | 174 |
| 101419 | A | 35425 | 38207 | 73632 |

All values are exact modular integer residues. The p=101419 third digit agrees with the earlier independent auxiliary-port computation; no native H0/B0 or original W_p equivalence is inferred.

## Provenance and next action

Read existing client checkpoint H40 revision 104: stored as SERVER_SQLITE_COMMITTED; read prior exact Source continuation h40-20261111-1135-exact-current-continuation, status SUCCEEDED, Source 13cca3010c20afa9b7c83c76e8377994892f2e6b, execution_authorized=false. No winning current issued session capability or native claim/open was verified; this is author-only portable evidence. Keep predecessor's recorded Source completed units, actual contributors and scientific pins unchanged. Original 94,687-byte UR V2 four-file bundle is still awaiting exact SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76.

Next exact scientific action is a source-authenticated mapping from the original-class H0/B0 native divided-power observer and its semilinear normalization to this preserved (S_P,E_P,J_P) interface, or a uniform finite-field character proof of the Legendre-selector using the original full branch provenance. Both remain open; neither can be inferred from this finite certificate.
