# D24 second-digit LIFT: first-order p-shift transport of the I1 shell

Status: PROVED_DERIVATION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

## 0. Input from the preceding shell unit

Let p=6m+1, p≡13 or 19 (mod 24), and

t_k=(6k+1) binom(2k,k)^2 binom(3k,k)/216^k.

The p^3 observer has exact shells I0=[0,2m], I1=[2m+1,3m], I2=[3m+1,4m], I3=[4m+1,6m]. I3 is pointwise zero mod p^3 and I2 has already been transported to a fixed-parameter truncated 5F4. This note resolves the p-dependent shape of I1 one p-adic order deeper.

## 1. Normalize the I1 shell

For 1<=r<=m set

b_r = t_{2m+r}/p  (mod p^2).

Because every I1 term has exactly one structural p from binom(3k,k), this is a legal integral observer.

The exact term ratio is

t_{k+1}/t_k = (6k+7)/(6k+1) * (2k+1)(3k+1)(3k+2)/(36(k+1)^3).

Put k=2m+r=(p-1)/3+r. Then the exact ratio between consecutive normalized I1 ports is

R_r(p) = 1/4 * (2p+6r+5)(2p+6r+1)(p+3r)(p+3r+1) / ((2p+6r-1)(p+3r+2)^3).

For 1<=r<m every denominator is a p-adic unit.

## 2. First-order p-shift is explicit

Define

R_r^(0) = (6r+5)(6r+1)(3r)(3r+1) / (4(6r-1)(3r+2)^3),

and

D_r = 2/(6r+5) + 2/(6r+1) +1/(3r) +1/(3r+1) -2/(6r-1) -3/(3r+2).

Expanding each affine factor to first order gives the exact mod-p^2 transport law

boxed: b_{r+1} ≡ b_r R_r^(0) (1+p D_r) (mod p^2).

No analytic logarithm is used: D_r is the rational first-order coefficient from multiplying unit factors modulo p^2.

## 3. Fixed-parameter hypergeometric carrier plus one derivative port

Set q_0=1, H_0=0 and for s>=1

q_s = product_{r=1}^s R_r^(0),
H_s = sum_{r=1}^s D_r.

Then

boxed: b_{s+1} ≡ b_1 q_s (1+p H_s) (mod p^2).

The q_s sequence is fixed-parameter hypergeometric:

q_s = (1)_s^2 (7/6)_s (11/6)_s (4/3)_s / ((5/6)_s (5/3)_s^3) * (1/2)^s / s!.

With Q_m=sum_{s=0}^{m-1}q_s and J_m=sum_{s=0}^{m-1}q_s H_s, the entire I1 shell satisfies

boxed: S_1/p ≡ b_1 (Q_m + p J_m) (mod p^2),

where S_1=sum_{k=2m+1}^{3m}t_k and b_1=t_{(p+2)/3}/p mod p^2. Thus all p-dependent high-index transition geometry has been reduced to one exact seed b_1; the remaining carrier is a fixed-parameter 5F4 sequence plus its explicit first-order derivative/harmonic port H_s.

For reference, the seed has the elementary mod-p reduction

b_1 ≡ -10 (2n)!/(n!^5 216^n) (mod p),

where n=(p+2)/3. The mod-p^2 correction of b_1 remains a live scalar port.

## 4. BRC information audit

Population: individual I1 ports indexed by r, each carrying exactly one structural p.

Compression: the p-dependent high-index recurrence is replaced by (b_1,q_s,H_s). This is lossless for S_1/p modulo p^2 because the transport law is exact to first p-adic order.

Preserved residual: H_s is retained. Dropping H_s would preserve only the coarser digit and would destroy precisely the second-digit information needed by E_p.

Not claimed: this does not evaluate b_1,Q_m,J_m in closed form and does not yet prove E_p=0. It isolates derivative/Frobenius-sensitive content rather than declaring it cancelled.

## 5. Deterministic regression

The exact checker independently reconstructs t_k modulo p^3, forms b_r, verifies every first-order transition, verifies the summed form, and checks the initial seed reduction. It was executed over all 166 target primes p<5000: 83 in each residue class, all checks PASS.

Executed checker SHA-256: a56a3c4e0ba426b0093d91568571cb82ad2cec09a8d469e5bb41c818bb5ef227.

Finite regression is falsification only. The all-prime derivation is the exact term-ratio expansion and factorial calculation above.

## 6. Next exact unit

The unresolved object is now concentrated in I0 together with the single I1 seed b_1 and the explicit pair (Q_m,J_m). Next derive a reflection or terminating p-shift identity for I0 modulo p^3, taking special care of k=m where 6k+1=p. The goal is to expose whether the I0 correction naturally supplies the negative of the I1 derivative port plus the already-known I2 5F4 boundary term. Do not collapse the k=m source or the H_s derivative coordinate before this comparison.
