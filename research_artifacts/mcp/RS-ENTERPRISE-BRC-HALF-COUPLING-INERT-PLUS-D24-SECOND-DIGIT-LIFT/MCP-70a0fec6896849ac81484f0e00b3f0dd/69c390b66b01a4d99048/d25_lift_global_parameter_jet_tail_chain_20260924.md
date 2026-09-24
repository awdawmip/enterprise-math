# D24 second-digit LIFT: one global parameter jet and its two valuation-jump tail chain

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

## 0. Consumed frontier

Keep the accepted D24 UR/JT0 parent and the already-published D25 observer/shell/I1/I0 checkpoints. In particular, LIFT is equivalent to

    W_p == p (mod p^3)

for every p == 13 or 19 (mod 24), and the previous source-faithful normal form has:
- the low shell I0 through U0,U1,U2 with the fixed k=m source retained;
- I1 through the live seed/derivative carrier b1,Q_m,J_m;
- I2 through the signed boundary carrier (4/9)(6/p)K_m;
- I3 pointwise invisible modulo p^3.

The immediately preceding unpublished unit also proves that I0 is one second-order parameter jet F_n(epsilon), and rules out naive exact antisymmetric k <-> n-k cancellation. This note does not redo those results. It compresses I0,I1,I2 and the p^3-invisible I3 into one finite polynomial jet and proves where the old shells reappear as valuation jumps.

## 1. One finite polynomial produces the whole W_p

Let

    p = 6m+1,
    n = 2m = (p-1)/3,

and put

    c_k = (6k+1)(1/2)_k(2/3)_k / ((k!)^3 2^k).

Define the finite polynomial

    P_n(epsilon) = sum_{k=0}^{p-1} c_k (-n+epsilon)_k.

Because

    -n + p/3 = 1/3,

the original weighted terminating carrier is exactly

    boxed:  W_p = P_n(p/3).

For k<p every denominator occurring in c_k and in the epsilon-polynomial is a p-adic unit. Hence P_n has p-integral Taylor coefficients and, modulo p^3,

    boxed:
    W_p == P_n(0) + (p/3)P_n'(0) + (p^2/18)P_n''(0)  (mod p^3).       (GJ)

Thus the p^3 observer sees one second-order finite parameter jet, not three independent shell mechanisms.

## 2. Low ports reproduce the existing I0 jet

For 0<=k<=n, the existing notation is

    u_k = c_k (-n)_k,
    A_k = H_n-H_{n-k},
    B_k = H_n^(2)-H_{n-k}^(2).

Termwise differentiation gives

    d/depsilon (-n+epsilon)_k |0 = -(-n)_k A_k,

    d^2/depsilon^2 (-n+epsilon)_k |0
      = (-n)_k (A_k^2-B_k).

Therefore the low coordinates of the global jet are exactly

    P_low(0)=U0,
    P_low'(0)=-U1,
    P_low''(0)=U2.

The fixed port k=m remains an explicitly tagged source inside these sums. Embedding it in P_n does not license deleting its provenance; the prior checkpoint's isolated k=m formula remains valid.

## 3. Every tail port has a common zero and a canonical derivative carrier

Write k=n+r with 1<=r<=4m. There is the exact factorization

    (-n+epsilon)_{n+r}
      = epsilon (-n+epsilon)_n (1+epsilon)_{r-1}.

Since n=2m is even,

    d/depsilon (-n+epsilon)_{n+r} |0
      = n!(r-1)!,

and

    d^2/depsilon^2 (-n+epsilon)_{n+r} |0
      = 2 n!(r-1)! (H_{r-1}-H_n).

Define the single tail chain

    boxed:
    d_r = c_{n+r} n!(r-1)!.

Then

    boxed:
    P_n'(0) = -U1 + sum_{r=1}^{4m} d_r,                              (D1)

    boxed:
    P_n''(0) = U2
               + 2 sum_{r=1}^{4m} d_r (H_{r-1}-H_n).                 (D2)

No shell assumption has entered: I1/I2/I3 are now valuation strata of d_r.

## 4. The shell boundaries are exactly two valuation jumps

Because n+r<p, the factorial denominators and n!, (r-1)! are p-units. In the tail range the weighted factor 6(n+r)+1 is also a p-unit.

The only p-factors of c_{n+r} before k=p are:
- one factor from (1/2)_k when k>=3m+1;
- one additional factor from (2/3)_k when k>=4m+1.

Consequently

    boxed:
    v_p(d_r) =
      0,  1<=r<=m,
      1,  m<r<=2m,
      2,  2m<r<=4m.                                                   (V)

This reproduces the old I1/I2/I3 stratification without taking the shells as primitive objects.

The tail chain has the exact rational recurrence

    boxed:
    d_{r+1}/d_r =
      3r (p+3r+1)(2p+6r+1)(2p+6r+5)
      -------------------------------------------------
      4 (p+3r+2)^3 (2p+6r-1).                                       (R)

Its first valuation jump is visible directly at r=m, where

    2p+6m+1 = 3p.

Its second valuation jump is visible at r=2m, where

    p+6m+1 = 2p.

Thus the two former shell boundaries are exact source-labelled jump edges of one recurrence.

## 5. The p^3 observer safely deletes only valuation-forced terms

Substituting (D1),(D2) into (GJ), and using (V), gives the smaller exact-equivalent carrier

    boxed:
    W_p ==
      U0 - (p/3)U1 + (p^2/18)U2
      + (p/3) sum_{r=1}^{2m} d_r
      + (p^2/9) sum_{r=1}^{m} d_r(H_{r-1}-H_n)
      (mod p^3).                                                       (C)

The omitted terms are not guessed cancellations:
- r>2m in the first-derivative tail have v_p(d_r)>=2, so the prefactor p makes them p^3-invisible;
- r>m in the second-derivative tail have v_p(d_r)>=1, so the prefactor p^2 makes them p^3-invisible.

This is a proved observer quotient.

Moreover, evaluating the exact tail factorization at epsilon=p/3 gives

    (1/3)_{n+r}
      = (p/3)n!(r-1)!
        [1 + (p/3)(H_{r-1}-H_n) + O(p^2)].

Hence the old shell carriers are projections of the same d_r chain:

For 1<=r<=m,

    boxed:
    t_{n+r}/p ==
      d_r/3 + p d_r(H_{r-1}-H_n)/9
      (mod p^2).                                                       (I1-id)

For m<r<=2m,

    boxed:
    t_{n+r}/p^2 == (d_r/p)/3 (mod p).                                 (I2-id)

So the previously preserved I1 first-order derivative coordinate and the I2 normalized boundary carrier are not unrelated residuals. They are respectively the unit and one-p-divisible strata of the same first derivative of P_n.

## 6. BRC information audit

Population:
all p ports k=0,...,p-1 of the weighted 3F2 source, with parameter-derivative order 0,1,2 and source index retained.

Carrier before quotient:
the finite polynomial jet (P_n(0),P_n'(0),P_n''(0)) together with the source-labelled low and tail decompositions.

Observer:
mod p^3 for W_p, equivalently the LIFT second digit after the accepted parent reduction.

Safe compression:
I0/I1/I2/I3 are replaced by the low jet plus the single d_r tail chain. Formula (C) is lossless for this observer. Terms are removed only after their exact p-valuations force p^3 invisibility.

Preserved provenance:
the fixed k=m low source remains tagged; r=m and r=2m remain explicit valuation-jump edges; derivative order and p-adic valuation are retained.

Forbidden quotient:
do not discard the first derivative of the unit tail (old I1 derivative information), the first p-divisible tail stratum (old I2 boundary information), or the k=m source before an identity proves their compensation.

BRC_REUSE_RESOLUTION = COMPOSE_APPLIED.

## 7. Deterministic exact regression

The companion checker reconstructs the complete carrier modulo p^3 without floating point. For every target prime p<5000 it verifies:
- formula (C) against the direct W_p sum;
- the exact valuation vector 0^m,1^m,2^(2m) of d_r;
- the cross-multiplied recurrence (R);
- the two jump edges.

Result:

    target primes = 166
    p mod 24 = 13: 83
    p mod 24 = 19: 83
    failures = 0

Checker SHA-256:
20772740f3471bf4b4a6454bb3c384c9ebc1aff7471f47df5fcb5e1882b7b1e1

Finite regression is falsification only. The strict reduction follows from the finite polynomial factorization, Taylor expansion in Z_(p), and exact valuation count.

## 8. New narrow frontier

LIFT is not yet proved. The live certificate has however been strictly reduced again: instead of separately coordinating the I1 seed/derivative carrier and I2 signed boundary carrier against the I0 jet, it is enough to control the single global finite parameter jet P_n and its two valuation-jump tail recurrence.

Next:
derive a terminating contiguous/telescoping relation directly for P_n(epsilon), or for the exact combination in (C), that forces W_p==p (mod p^3); alternatively produce an exact counterexample. The relation must preserve the k=m low source and both jump edges. Do not return to naive antisymmetric k<->n-k pairing, and do not rebuild I1/I2 as independent carriers unless a proof requires their typed projections.
