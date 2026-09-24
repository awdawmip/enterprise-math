# D24 second-digit LIFT: terminating p-shift decomposition of I0

Status: PROVED_DERIVATION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

Let p=6m+1, n=2m=(p-1)/3 and

t_k=(6k+1)(1/2)_k(1/3)_k(2/3)_k/(k!)^3 2^k.

The live lower shell is S_0=sum_{k=0}^n t_k modulo p^3. The key exact rewrite is

1/3 = -n + p/3.

For 0<=k<=n define the terminating base port

u_k=(6k+1)(1/2)_k(-n)_k(2/3)_k/(k!)^3 2^k,

A_k=H_n-H_{n-k}=sum_{j=n-k+1}^n 1/j,
B_k=H_n^(2)-H_{n-k}^(2)=sum_{j=n-k+1}^n 1/j^2.

All denominators are p-units. Expanding the finite product (-n+p/3)_k around (-n)_k gives, term by term and uniformly for k<=n,

(-n+p/3)_k/(-n)_k
≡ 1-(p/3)A_k+(p^2/18)(A_k^2-B_k) (mod p^3).

Hence the entire I0 shell has the exact terminating deformation

boxed:
S_0 ≡ U_0-(p/3)U_1+(p^2/18)U_2 (mod p^3),

where
U_0=sum_{k=0}^n u_k,
U_1=sum_{k=0}^n u_k A_k,
U_2=sum_{k=0}^n u_k(A_k^2-B_k).

This is not an asymptotic expansion: every omitted term contains p^3 because the deformation parameter is exactly p/3 and the finite-product denominators are p-units.

## Special source port k=m

The task requires preservation of the unique weight source 6m+1=p. Write

v_m=(1/2)_m(-n)_m(2/3)_m/(m!)^3 2^m,
so u_m=p v_m. Its contribution to the p^3 observer is therefore

boxed:
p v_m-(p^2/3)v_m A_m (mod p^3).

The quadratic derivative port at k=m is automatically p^3-invisible, but the source itself and its first deformation derivative are not. Thus the special k=m provenance can be separated without deleting it.

If hats denote sums with k=m removed, then

S_0 ≡ 
  Uhat_0
 +p(v_m-Uhat_1/3)
 +p^2(Uhat_2/18-v_m A_m/3)
 (mod p^3).

## Combination with the already-persisted upper shells

The preceding units proved

S_1/p ≡ b_1(Q_m+pJ_m) (mod p^2),
S_2/p^2 ≡ (4/9)(6/p)K_m (mod p),
S_3≡0 (mod p^3).

Therefore the full third-digit observer has the exact source-preserving normal form

boxed:
W_p ≡
 Uhat_0
 +p[ v_m-Uhat_1/3+b_1 Q_m ]
 +p^2[ Uhat_2/18-v_m A_m/3+b_1 J_m+(4/9)(6/p)K_m ]
 (mod p^3),

with the understanding that b_1 Q_m is retained modulo p^2, while b_1 J_m is needed only modulo p.

LIFT remains the assertion that this expression is congruent to p modulo p^3. This is a strict structural reduction of the original p-term weighted 3F2 observer into: a terminating negative-integer base family, its first two explicit deformation ports, the singled-out k=m source, the I1 seed/derivative carrier, and the I2 boundary 5F4 carrier. No shell or signed residual is declared zero without proof.

## BRC audit

Population: I0 ports k=0..n with source index, terminating base value, and deformation provenance.

Compression: replacing (1/3)_k by the exact finite Taylor carrier at -n retains all information visible modulo p^3.

Special port: k=m is not absorbed into a total; its p-weight and first derivative are explicit.

Future operations: the new carrier supports a terminating hypergeometric identity / creative-microscoping search without reopening UR/JT0.

## Regression

An exact checker independently reconstructs t_k modulo p^3 and verifies the termwise deformation, summed identity, and isolated k=m formula for every target prime p<5000. All 166 targets pass, 83 in each residue class.

Executed checker SHA-256: 8bee68e37b8c51a25f2ff0fb048b04830beb3661d6f7ad6db9536fabdc19f84b.

Finite regression is falsification only; the all-prime derivation is the finite-product expansion above.

## Next exact unit

Do not enlarge the scan. The remaining scientific bottleneck is now a terminating identity/contiguous relation for the combined carrier. First test whether Uhat_0 and Uhat_1 admit an exact telescoper under k->n-k or a terminating 3F2/4F3 evaluation whose first two parameter derivatives generate the compensation -b_1 J_m-(4/9)(6/p)K_m. Preserve the isolated k=m source throughout.
