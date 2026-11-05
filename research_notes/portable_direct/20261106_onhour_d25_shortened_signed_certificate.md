# D25 / SECOND-DIGIT-LIFT — p-adically shortened signed finite certificate

**2026-11-06 · TASK_RESEARCH · AUTHOR-SIDE EXACT DERIVATION / 12-PRIME INTEGER CHECK · UNREVIEWED / NOT_ADMITTED.**

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (never the maintenance lane).

Consume the **existing unreviewed author-side** exact triangular cusp transport
`20261105_onhour_d25_cusp_integral_terminating_transport.md` and signed two-coset recurrence `20261105_onhour_d25_signed_two_coset_weighted_k_recurrence.md`, retaining even/odd interaction. They give
`a_n = sum_{k<=floor(2n/3)} T[n,k]*b_k` with
`T[n,k]=9^k(3/2)^n[s^(2n)] N(s)t(s)^k`,
`t(s)=s^3 U(s)`, `U(0)=32/729`, `N(0)=1`, `U'(0)=N'(0)=0`.

## New theorem 1: shorter exact finite signed residual

For each prime p>3, put
`a_n=(2n)!(3n)!/[216^n(n!)^5]`,
`b_k=(4k)!/[2304^k(k!)^4]`,
`L=floor((2p-1)/3)`, `h=(p-1)/2`,
`K0=floor(2L/3)`,
`K=K0-1` if `2L-3K0=1`, else `K=K0`. In particular `K<=h`.
Then modulo p^3:

```
W_p - V_h = C_p - V_tail;
C_p = sum_{k=0}^K b_k*(sum_{n=0}^L (6n+1)*T[n,k] - (8k+1));
V_tail = sum_{k=K+1}^h (8k+1)*b_k.
```

**Proof.** For 0<=n<p, `v_p(a_n)=floor(2n/p)+floor(3n/p)` since n! is a p-unit. The valuation is >=3 for n>L, so the removed n-rows vanish modulo p^3 **after signed k-summation**. Triangular support gives T[n,k]=0 for 3k>2n. The additional d=1 edge vanishes exactly because U and N have no linear s term, so if 2L-3K0=1, the entire final k-column is zero for n<=L. Substitute the exact rational triangular identity and subtract V_h, preserving its distinct k>K tail. The already sourced 2304 full/half theorem gives `W_p-V_p = C_p-V_tail (mod p^3)`.

The original frozen mother objective for primes p=13,19 mod24 reduces under the previously source-aligned scalar interface to proving `C_p-V_tail=0 (mod p^3)`. This uniform vanishing remains open.

## New theorem 2: exact signed tail first digit

For each K<k<=h when the tail is nonempty, `p<=4k<2p`, so `v_p(b_k)=1`. Wilson gives

```
b_k/p = -(4k-p)!/[2304^k(k!)^4] (mod p),
V_tail/p = -sum_{k=K+1}^h (8k+1)(4k-p)!/[2304^k(k!)^4] (mod p).
```

In the original target primes p=13 and p=19, the **compensating tail is nonzero**:
`p=13: (L,K0,K,h)=(8,5,4,6), C_p=V_tail=1157 mod 2197, V_tail/p=11 mod 13`;
`p=19: (L,K0,K,h)=(12,8,8,9), C_p=V_tail=1862 mod 6859, V_tail/p=3 mod 19`.
For p=67, `(L,K0,K,h)=(44,29,28,33)`, `C_p=V_tail=55945 mod 300763`, `V_tail/p=31 mod67`. These are finite certificates, not a uniform proof of the required cancellation.

## Executed verification and carry preservation

The companion Python checker, derived from the previous exact CM-cusp code and tested independently with a locally executed equivalent, reconstructs all n<=L coefficients from raw binomial data, confirms all higher n-rows vanish mod p^3, tests C_p-V_tail, tests V_p=V_h mod p^3, and verifies each Wilson tail unit. **12 primes 5,7,11,13,17,19,23,31,37,43,61,67; 0 failed assertions.** It uses exact integer ring operations. Transported columns: 9 to 5 at p13, 13 to 9 at p19, 45 to 29 at p67 (representation size, not measured runtime).

BRC observation retains (original model, p, n, k, s-even/s-odd channel, coefficient, valuation, weight, support, signed V_tail) until the final cancellation. Do not replace the native p373 original-class H0/B0 module, [X]U mod139129, rank, semilinear Frobenius eta/kappa or independent replication with this portable certificate; Issue #1559 is OPEN/PENDING_OWNER as observed this run.

**Next science:** Find an explicit finite k-telescoper of C_p whose signed boundary equals V_tail modulo p^3 for p=13,19 mod24; first reject candidates mismatching the nonzero p13/19 compensators. Continue the original native benchmark via an authorized owner. Researcher identity registered by a distinct service session in this run; no CLAIM/open/Result/freeze/admission asserted.
