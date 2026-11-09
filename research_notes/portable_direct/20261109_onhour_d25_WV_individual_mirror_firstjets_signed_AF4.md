# D25 — individual complementary first jets and signed grade-two mirror at the original AF4 precision

Date: 2026-11-09. TASK_RESEARCH, task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`. **Author-side theorem and exact execution only; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.**

## Original coefficient carriers, provenance and observers

For a prime `p>3`, in the local ring `Z_(p)`, let

```text
A_n = (2n)!(3n)!/((n!)^5 216^n) = binom(2n,n)^2 binom(3n,n)/216^n
C_n = (4n)!/((n!)^4 2304^n) = binom(4n,2n) binom(2n,n)^2/2304^n
W_p = sum_{n=0}^{p-1}(6n+1)A_n
V_p = sum_{n=0}^{p-1}(8n+1)C_n.
```

The original full cutoff and both distinct weight operators remain fixed. Set `H_r=sum_{k=1}^r 1/k` in `F_p` for `0<=r<p`, `Q_p(b)=(b^(p-1)-1)/p mod p` for `b=216,2304`, and `s=p-q`. The complement products are divided by their *actual exact* valuation three; the rational unit reductions are made only afterwards.

## Theorem A: individual first jet of the 216 mirror

For **every** prime `p>3` and integer `p/3<q<p/2`,

```text
  (A_q A_{p-q})/p^3
   ≡ (1/(36q^3)) [1+p J_A(q)]                       (mod p^2),
  J_A(q) ≡ 3/q - Q_p(216)
             + 2H_{2q} + 3H_{3q-p} - 5H_q             (mod p).
```

Here `v_p(A_q)=1`, `v_p(A_{p-q})=2`. All displayed denominators are `p`-units. This is a statement about original coefficients, not a changed representative of an H0/B0 operator.

## Theorem C: individual first jet of the 2304 mirror

For **every** prime `p>3` and integer `p/4<q<p/2`,

```text
  (C_q C_{p-q})/p^3
   ≡ (1/(288q^3)) [1+p J_C(q)]                      (mod p^2),
  J_C(q) ≡ 3/q - Q_p(2304)
             + 4H_{4q-p} - 4H_q                     (mod p).
```

Here `v_p(C_q)=1`, `v_p(C_{p-q})=2`.

## Complete proof, including the p-adic correction

Write `w_p=((p-1)!+1)/p`. For `k=ap+r`, `0<=r<p`, with the small nonnegative `a<p` used here, splitting the ordinary factorial at its multiples of `p` and using `H_{p-1}=0 mod p` gives

```text
  k!/p^a ≡ (-1)^a a! r! [1+ap(H_r-w_p)]       (mod p^2).
```

The complementary-factorial identity, again with actual integer factorials, is

```text
  r!(p-1-r)! ≡ (-1)^(r+1) [1+p(H_r-w_p)]      (mod p^2).
```

For `p/3<q<p/2`, the numerator factorials have quotient/remainder pairs
`2q=0*p+2q`, `3q=1*p+(3q-p)`, `2s=1*p+(p-2q)`, `3s=1*p+(2p-3q)`. The denominator is `(q!s!)^5`. Apply both identities and simplify, without reducing the coefficient to its leading digit:

```text
  A_q A_s/p^3
   ≡ -[(p-2q)(2p-3q)] / [(p-q)^5 216^p]
      *[1+p D_A(q)]                         (mod p^2),
  D_A = H_{2q}+2H_{3q-p}+H_{p-2q}+H_{2p-3q}-5H_q.
```

The Wilson quotient cancels. Under the exact complement reflections
`H_{p-2q}=H_{2q}-1/(2q)` and
`H_{2p-3q}=H_{3q-p}-1/(3q)` modulo `p`.
The rational prefactor expands to
`6/q^3 [1+23p/(6q)]`, and
`216^{-p}≡216^{-1}[1-pQ_p(216)] mod p^2`.
The harmonic reflection contributes `-5/(6q)`; together these yield precisely `3/q` in `J_A`.

For `p/4<q<p/2`, the only numerator quotient/remainder pairs are
`4q=1*p+(4q-p)` and `4s=2*p+(2p-4q)`. The denominator is `(q!s!)^4`. The same factorial identities give

```text
  C_q C_s/p^3
   ≡ -[2(2p-4q)] / [(p-q)^4 2304^p]
      *[1+p D_C(q)]                         (mod p^2),
  D_C = 2H_{4q-p}+2H_{2p-4q}-4H_q.
```

Since `H_{2p-4q}=H_{4q-p}-1/(4q) mod p`,
the prefactor is `8/q^3[1+7p/(2q)]`, and
`2304^{-p}≡2304^{-1}[1-pQ_p(2304)]`.
The harmonic correction `-1/(2q)` again leaves the coefficient `3/q`. This proves both identities for the full stated prime/indicator domains.

On the common interval `p/3<q<p/2`, the quotient also yields

```text
  (A_q A_s)/(C_q C_s)
   ≡ 8[1+p(J_A(q)-J_C(q))]                   (mod p^2),
  J_A-J_C = Q_p(32/3)+2H_{2q}+3H_{3q-p}-4H_{4q-p}-H_q.
```

This **recovers**, rather than recredits, the earlier six-interval ratio first-jet result. Its new utility is the separate individual jets needed to recover *both* signed grade-two tails at fourth-digit precision.

## Corollary: full signed grade-two recovery modulo p^4

For `q` in the respective ranges let `a_q=A_q/p` and `c_q=C_q/p`, units modulo `p^2`, and let `U_A,U_C` denote the right-hand complementary units above. Then

```text
  T2_W ≡ p^2 * sum_{p/3<q<p/2}
                 (1+6(p-q)) U_A(q)/a_q           (mod p^4),
  T2_V ≡ p^2 * sum_{p/4<q<p/2}
                 (1+8(p-q)) U_C(q)/c_q           (mod p^4).
```

The *unreduced* signed factors `1+6(p-q)` and `1+8(p-q)` retain their `+6p` and `+8p` terms, which are invisible at third-digit precision but affect the AF4 fourth digit. This gives the exact grade-two part `T2_W-2T2_V` from grade-one coefficients and the above first-jet observer without any independent high-index factorial computation.

For `p=13,19,373`, exact original-binomial computation gives `T2_W-2T2_V mod p^4` equal to `28054,106134,4655673727`, respectively. At `p=373,q=125`: `J_A=35,J_C=87,U_A=12041,U_C=29993 mod139129`; `J_A-J_C=321 mod373`, matching the previously proved ratio-jet observer.

## Executed finite check and admission scope

The sibling executable checks **all 46 primes** `5<=p<=211` plus `373`, comprising **801 original-A and 1202 original-C** complement pairs. Each pair independently checks normalized products modulo `p^2`, reflected upper coefficient modulo `p^2` and the weighted full grade-two sum modulo `p^4`. On `p=5,7,13,19,37,43,73,373`, all original coefficients are also recomputed through independent exact rational recurrences modulo `p^5`. All checks passed, with no floating point. The universal algebraic proof does not depend on the finite check.

This is a **direct additive AF4 transfer improvement** but not a proof of the universal AF4 cancellation, original frozen LIFT `Delta_p-R_p=0`, or the native H0/B0 benchmark. Retain the unfinished zero/first-grade AF4 cancellation, the original signed source/odd observer, and the frozen LIFT task. The authentic fixed native `p=373 [X]U mod139129` (module rank, Frobenius semilinear direction/eta, kappa, Delta-R, independent rerun) remains `NOT_EXECUTED` and is tracked by existing support issue #1559 with no assigned executor.

## Next discriminating action

Use the now explicitly *low-index* signed grade-two formula with the existing first-grade second jet to construct a finite Abel/WZ boundary relation for the **remaining zero/first-grade** combination, initially at `p=13,19` and independently at `p=373`. Test the exact signed `+6p,+8p` terms; seek a universal proof only after the boundary identity survives those examples. In parallel, the native executor path must supply the existing #1559 raw original-class H0/B0 data, not an auxiliary port.
