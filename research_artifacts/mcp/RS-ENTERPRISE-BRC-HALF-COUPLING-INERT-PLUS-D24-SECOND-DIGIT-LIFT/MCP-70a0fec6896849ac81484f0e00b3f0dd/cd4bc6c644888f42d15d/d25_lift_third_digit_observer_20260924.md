# D24 second-digit LIFT: normalized third-digit observer

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

## Frozen inputs consumed, not reproved

For p = 6m+1 with p ≡ 13 or 19 (mod 24), use the accepted/frozen parent notation

B_k = (1/6)_k (1/3)_k / ((k!)^2 2^k),
g = sum_{k=0}^{p-1} B_k,
h = sum_{k=0}^{p-1} (12k+1) B_k,
G_p = g/p (mod p^2),

and the frozen reflected scalar

R_p = 2 sum_{i=1}^m B_i sum_{r=1}^i (1+6(i-r)) C_r (mod p),

C_r = 2^(r-1)(r-1)!^2 / (18 (5/6)_r (2/3)_r).

The accepted D24 UR/JT0 result gives the first digit W_p ≡ p (mod p^2). The earlier reflected-tail bridge gives T_p ≡ p^2 R_p (mod p^3).

The live D25 discrepancy is

Delta_p = (G_p h - 1)/p (mod p),

and LIFT is Delta_p ≡ R_p (mod p).

## 1. Exact convolution identity

Put

c_n = (1/6)_n(1/3)_n/(n!)^2,

so B_n=c_n 2^{-n}. Then, exactly over Q,

g h
 = sum_{0<=i,j<p} (12j+1) B_i B_j.

Swapping i and j and averaging gives

g h
 = sum_{0<=i,j<p} (6(i+j)+1) B_i B_j.          (1)

For a fixed n=i+j<p, the truncation i,j<p is automatic, so the whole degree-n convolution coefficient is present. Clausen's identity

2F1(1/6,1/3;1;z)^2
 = 3F2(1/2,1/3,2/3;1,1;z)

therefore gives

sum_{i+j=n} B_i B_j
 = (1/2)_n(1/3)_n(2/3)_n/(n!)^3 * 2^{-n}
 = binom(2n,n)^2 binom(3n,n)/216^n.

Define the weighted truncation

W_p = sum_{n=0}^{p-1}
      (6n+1) binom(2n,n)^2 binom(3n,n)/216^n.

The complementary degree-at-least-p finite convolution tail is

T_p = sum_{0<=i,j<p, i+j>=p} (6(i+j)+1) B_i B_j.

Thus (1) splits EXACTLY as

boxed: g h = W_p + T_p.                         (2)

No p-adic approximation has been used in (2).

## 2. Exact normalized discrepancy

Because G_p=g/p,

Delta_p
 = (G_p h - 1)/p
 = (g h - p)/p^2   (mod p).

Insert (2) and the already-frozen tail theorem
T_p ≡ p^2 R_p (mod p^3):

Delta_p
 ≡ (W_p-p)/p^2 + R_p                  (mod p).

Hence

boxed:
Delta_p - R_p ≡ E_p (mod p),
E_p := (W_p-p)/p^2 (mod p).                       (3)

The quotient E_p is well-defined because the accepted D24 first-digit result
W_p ≡ p (mod p^2) has already been terminally reviewed and accepted.

Therefore the live second-digit statement is exactly

boxed:
LIFT  <=>  E_p = 0 in F_p
      <=> W_p ≡ p (mod p^3).                       (4)

This is uniform in both requested residue classes; the algebra above does not
split p ≡ 13 and 19 (mod 24).

## 3. Observer/minimal-state classification

Before (3), the live interface carries G_p mod p^2, h mod p^2, the cutoff-sensitive
Phi_xx/jet data, and the reflected scalar R_p. Those coordinates may NOT be
discarded before the exact product and reflected-tail bridges are consumed.

After (2) and the frozen congruence T_p ≡ p^2 R_p (mod p^3) are applied, all
those coordinates enter the surviving discrepancy only through the single
F_p-valued scalar E_p.

Accordingly the smallest remaining observer reached in this unit is

E_p in F_p,

represented directly by one weighted 3F2 truncation modulo p^3. This is a
strict state-space reduction of the D25 execution interface, but it is NOT yet
an all-prime proof that E_p=0.

The reduction also explains the prior-art boundary: E_p=0 is precisely the
a=1, plus-class p^3 specialization of Zhi-Wei Sun's Conjecture A14(ii) already
identified by the frozen Jacobi-jet return. A conjecture is not imported as a
proof.

## 4. Information-loss audit

1. G_p mod p^2 and h mod p^2 are retained until they are combined into
   (g h-p)/p^2.
2. R_p is retained until the frozen degree-at-least-p tail is subtracted.
3. Phi_xx / derivative / Frobenius provenance is not declared irrelevant
   globally; it is compressed only after the exact accepted bridges have
   carried its contribution into W_p and T_p.
4. No high-precision BRC note is reused merely because it contains more
   p-adic digits; it would need a proof that it preserves E_p.
5. Finite computation below is falsification/regression only.

## 5. Independent deterministic regression

A task-local checker recomputes the three sides independently:

- Delta_p from the B_k recurrence and g,h;
- R_p from the frozen triangular C_r formula;
- E_p from the independent weighted 3F2 recurrence.

For every prime p<5000 with p ≡ 13 or 19 (mod 24):

- 166 primes total;
- 83 in each residue class;
- Delta_p - R_p - E_p failures: 0;
- nonzero E_p values: 0.

The checker SHA-256 is
aee9ef7518c5d012692e768ac4e03db0349340ab564f60c7a6051fc4517f5a0b.

These zero failures do not prove E_p=0 for all target primes.

## 6. Current proof/literature boundary

A fresh targeted audit on 2026-09-24 found:

- Chisholm–Deines–Long–Nebe–Swisher (2013) supplies the Ramanujan-type
  p-adic/CM framework used for the already-closed first digit, not a verified
  theorem here closing this exact weighted 216 modulus-p^3 target.
- Wang–Sun (2022), 'Proof of some conjectural hypergeometric
  supercongruences via curious identities', proves several other z != 1
  truncated supercongruences, but the audited text did not yield this exact
  weighted 216 theorem.
- Mao–Tian (2026) proves recurrences for coefficients of squared/cubic
  hypergeometric functions and a Clausen proof; it does not by itself provide
  the required p-adic third digit.

This is a scoped audit statement, not a claim that no proof exists anywhere.

## 7. Next exact scientific unit

Do not revisit UR/JT0 or merely enlarge the prime scan.

The next unit is to prove or refute E_p=0. Preferred mechanisms:

(a) a terminating p-shift / creative-microscoping certificate for the weighted
    3F2 truncation modulo p^3; or
(b) a Frobenius/CM lift that controls the next digit beyond the accepted
    Chisholm first-digit interface.

Any proposed reduction must preserve the normalized third-digit observer E_p.
