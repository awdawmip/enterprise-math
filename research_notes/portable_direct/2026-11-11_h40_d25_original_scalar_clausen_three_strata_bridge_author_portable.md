# D25/LIFT: exact original-scalar g/h bridge from the finite Clausen pair, including both cutoff tails

Date: 2026-11-11. Classification: AUTHOR-PROVED / EXACT-INTEGER-VERIFIED / UNREVIEWED / NOT_ADMITTED. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. This is author-side portable evidence, **not** a Source CLAIM, native H0/B0 divided-power representative, Frobenius identification, accepted LIFT Result or proof of Delta_p=R_p.

## Exact original-scalar connection

Let p=6m+1 be prime, p>=7. Work in Z_(p). Put

 b_k = ((1/6)_k(1/3)_k/(k!)^2) 2^{-k}, 0<=k<p;
 g_p=sum_{k=0}^{p-1} b_k,  h_p=sum_{k=0}^{p-1} (12k+1)b_k.

These are the original scalar quantities from the frozen parent, with G_p=g_p/p when p divides g_p. Define the auxiliary finite Clausen polynomial

 F_m(X)=sum_{k=0}^m binom(m,k)binom(2m,k) X^k;
 A=F_m(1/2), B=F_m(1/2)+6F_m'(1/2).

The equality (1/6)=-m+p/6, (1/3)=-2m+p/3 gives an exact product identity for EVERY original index k:

 b_k=2^{-k}(k!)^{-2} prod_{j=0}^{k-1}(j-m+p/6)(j-2m+p/3).

There are three p-adic cutoff sectors, determined by the exact zeros j=m and j=2m at p=0.

## Three sector formulas, all explicit

For 0<=k<=m, put
 T_k=binom(m,k)binom(2m,k)2^{-k},
 L_k=sum_{j<k}(1/[6(j-m)]+1/[3(j-2m)]),
 M_k=sum_{j<k}(1/[36(j-m)^2]+1/[9(j-2m)^2]),
 J_k=(L_k^2-M_k)/2.
Then b_k = T_k(1+pL_k+p^2 J_k) (mod p^3).

For m<k<=2m, put
 U_k=((-1)^{m+k} m! (k-m-1)! (2m)!)/[6(2m-k)!(k!)^2 2^k],
 V_k=sum_{0<=j<k,j!=m}1/[6(j-m)]+sum_{j<k}1/[3(j-2m)].
Then b_k=p U_k(1+pV_k) (mod p^3).

For 2m<k<p, put
 Z_k=((-1)^m m!(k-m-1)!(2m)!(k-2m-1)!)/[18(k!)^2 2^k].
Then b_k=p^2 Z_k (mod p^3).

All displayed denominators are p-adic units. The ranges cover each k once. The corresponding weighted h_p congruence is obtained termwise by multiplying by (12k+1).

Define the source-separated correction coordinates

 C=sum_{k<=m}T_k L_k + sum_{m<k<=2m} U_k,
 D=sum_{k<=m}T_k J_k + sum_{m<k<=2m}U_k V_k + sum_{2m<k<p}Z_k,
 E=sum_{k<=m}(12k+1)T_k L_k + sum_{m<k<=2m}(12k+1)U_k.

**Universal exact congruences** (p=6m+1, p>=7):

 g_p = A+pC+p^2 D (mod p^3),
 h_p = B+pE (mod p^2).

In particular A=g_p (mod p), B=h_p (mod p), making the existing auxiliary Clausen two-port calculations legitimate *first-digit* readouts of the original scalar; the second digit requires the displayed corrections and cutoff tails.

For p in {13,19} mod 24 the accepted CM0 input implies p|A and thus p|g_p; the accepted UR says (g_p/p) h_p = 1 (mod p). Set
 Ghat=A/p+C+pD (mod p^2), Hhat=B+pE (mod p^2).
Then the original LIFT observer is reconstructed without erasing its source tags:

 **Delta_p = ((Ghat*Hhat-1)/p) (mod p)**.

The quotient is well-defined because UR establishes a numerator divisible by p. Thus LIFT is equivalently this *explicit* scalar expression = R_p (mod p) when the original R_p has been authenticated at the frozen interface. The expression is a genuine exact bridge, but we do not classify it as a strict lower-complexity solution or a proof of the still-open target.

## Proof

Split the exact product identity at its two integer zeros. Before the first zero, expand prod(1+p a_i) to order p^2, giving 1+p sum a_i+p^2((sum a_i)^2-sum a_i^2)/2. Between the zeros, factor p/6 out of the first Pochhammer product and expand the remaining unit product to first order; factorial identities give U_k. After both zeros, factor (p/6)(p/3)=p^2/18; the remaining unit products reduce to the factorial expression Z_k modulo p. Because all j<k<p and all nonzero j-m, j-2m in the designated ranges have abs value <p, every denominator is p-prime. Sum by source sector; for h keep only terms through p. For the divided g/p observer retain all three g sectors through p^2. QED.

## Information-loss witness at the actual second-digit observer

At p=13, m=2, exact independent computation gives
 A mod 13^3 = 1105; B mod 13^2 = 6;
 C mod 13^2=56, D mod13=8, E mod13=11;
 g mod13^3=988, h mod13^2=149,
 G=g/13 mod169=76, Delta=((G*h-1)/13) mod13=0.

Here the three summands of D are **(0,0,8) mod13**: the entire p^2 correction in g comes from indices k>2m. Dropping that distant cutoff sector leaves first-digit UR unchanged but would give **Delta=4 mod13**, an incorrect second-digit readout.

At p=19, m=3, the corresponding coordinates are
 (C mod361,D mod19,E mod19)=(306,12,10);
 g mod6859=1596, h mod361=50, G mod361=84, Delta mod19=12.
The three D components are (3,18,10) mod19. Dropping the final sector changes Delta from 12 to 6 mod19. These are exact witnesses for retaining the late original-class source, not an appeal to generic information loss.

## Verification, limits and next frontier

An independent modular implementation uses the original one-step recurrence b_(k+1)/b_k=(6k+1)(3k+1)/[36(k+1)^2] and separately evaluates the three factorial/harmonic sectors. All **204,946 termwise comparisons** for all **178 primes p=1 mod6, 7<=p<=2500** passed modulo p^3; the g mod p^3 and h mod p^2 sums also matched. Among them **94 target primes** (48 p=13 mod24, 46 p=19 mod24) had integral g/p, verified UR and exact split-observer Delta consistency. The bounded verification is not a universal proof; universality follows from the preceding product argument.

The remaining required scientific step is an exact Source-authenticated R_p and original-class H0/B0 divided-power/[X]U/Frobenius interface at the frozen pin, followed by comparison with the explicit Delta reconstruction. Native CM experiment is NOT_RUN; no CLAIM, Result, independent review or canonical Task checkpoint is asserted. UR V2 original four-file bundle still requires original bytes (94687, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) for its provenance writer only; its mathematics is not re-proved here.
