# D25 — exact p² valuation bands of the **original** finite Gauss overflow

Date: 2026-11-10. TASK_RESEARCH author-side. Status: **EXACT ALGEBRAIC LEMMA / FIVE EXECUTED CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical research lane `chatgpt-research-onhour-enterprise-math-20260923`; maintenance `chatgpt-hourly-enterprise-math-20260921` excluded. Source-native durable frontier `b58330b74576153cdadde5d80a3d92df3a819a0e` is not replaced.

## 1. Exact coefficient bands (new all-prime algebraic proposition)

Fix a prime `p ≡ 13 (mod 24)`, and set `a=(5p-1)/8`, `b=(7p-3)/8`, `q=(p-1)/4`. In `Z_(p)`, put

`f_k=(1/8)_k(3/8)_k/(k!)²`, `d_k=4^k f_k`, for `0≤k<p`.

Then the following **coefficientwise congruence modulo p²** is proved, with `H_0=0`:

1. For `0≤k≤a`,
```
d_k = 4^k C(a,k) C(b,k) *
      {1 - (p/8) [5(H_a-H_{a-k})+7(H_b-H_{b-k})]}   (mod p²).
```
2. For `a<k≤b`,
```
d_k/p = (5/8) * 4^k * (-1)^(a+k) * a! * (k-a-1)! * b!
        / ((b-k)!*(k!)²)  (mod p).
```
3. For `b<k<p`, `d_k=0 (mod p²)`.

All denominators in these displayed formulas are p-units. These are exact claims about the originally frozen coefficient model, not surrogate coefficients.

**Proof.** In the relevant prime class `(1/8)=-a+5p/8` and `(3/8)=-b+7p/8` exactly. For `k≤a`, expand the two finite products to first order in p; each factor contributes `-5p/(8(a-i))` or `-7p/(8(b-i))`. Multiplying gives the first expression. For `a<k≤b`, the first rising factorial has exactly one factor divisible by p, at `i=a`: its quotient by p is `(5/8)(-1)^a a!(k-a-1)!` modulo p; the other rising factorial reduces to `(-1)^k b!/(b-k)!`. For `k>b`, both factorials have a p-factor, giving p² divisibility. This proves all three bands without a scan or extra conjecture.

## 2. Original overflow support and new two-port exact certificate

Keep the **original** finite Gauss-transform overflow as in the preceding author result `20261110_onhour_d25_CM_overflow_scalar_trace_reflection.md`:

```
e_(p+r) = sum_{k=ceil((p+r)/2)}^{p-1}
          d_k * (-1)^(p+r-k) * C(k,p+r-k), 0≤r≤p-2.
E_p(x) = sum_{r=0}^{p-2} e_(p+r)*x^r.
```

Each term of degree `p+r` comes from a factor `x^k(1-x)^k` of degree `≤2k`. Therefore, uniformly over the specified primes,

```
e_(p+r) = 0 (mod p)  for r>q,
e_(p+r) = 0 (mod p²) for r>3q.
```

More explicitly, if `d_k^0` denotes the first (unperturbed) term above for `k≤a`, and `d_k^1=d_k-d_k^0` consists of the harmonic first jet for `k≤a` and the one-zero-factor term for `a<k≤b`, then

```
e_(p+r) = E_r^0 + E_r^1 (mod p²),
E_r^i = sum_{k=ceil((p+r)/2)}^b d_k^i (-1)^(p+r-k) C(k,p+r-k),
E_r^0 = 0 for r>q,    E_r^1 = 0 for r>3q.
```

With the exact CM auxiliary `s=(3-2sqrt(2))/6`, conjugate `1-s`, and `T_r=s^r+(1-s)^r` (so `T_0=2`, `T_1=1`, `T_r=T_(r-1)-T_(r-2)/36`), the earlier scalar target now has **two coefficient-valuation ports**:

```
L_p = sum_{r=0}^q e_(p+r)*T_r  (mod p²),
M_p = sum_{r=q+1}^{3q} e_(p+r)*T_r (mod p²),
S_p = L_p + M_p (mod p²).
```

Here `M_p` is **termwise p-divisible**, whereas `L_p` need not be termwise p-divisible. The previously obtained CM zero `E_p(s)=0 (mod p)` implies `L_p=0 (mod p)`, since its complementary band vanishes mod p. This last conclusion **uses that declared prior author-side hypothesis**. Under it, the remaining all-prime scalar goal is exactly

```
(L_p/p) + (M_p/p) = 48*g_p  (mod p),
```

where `g_p` is the pre-existing **sigma-odd** observer `G_p(s)=p*g_p*sqrt(2) (mod p²)`. These quotients are taken in `Z_(p)` before reduction. The new lemma gives a polynomial-degree cutoff for the signed overflow and separates unit-origin and one-p-factor contributions without erasing the odd observer or original coefficient provenance.

## 3. Executed arithmetic (independent recurrence vs factorial/first-jet)

The attached standalone Python checker uses exact integer modular inverses. For each displayed prime it checks **all** p original `d_k` against the independently evaluated first-jet formulas and **all** `p-1` original overflow coefficients against an independent convolution of the two finite bands, as well as both vanishing ranges and the scalar trace. All checks passed:

| p | a | b | q | L_p/p mod p | M_p/p mod p | S_p mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 8 | 11 | 3 | 4 | 10 | 13 |
| 37 | 23 | 32 | 9 | 32 | 6 | 37 |
| 61 | 38 | 53 | 15 | 57 | 20 | 976 |
| 109 | 68 | 95 | 27 | 14 | 40 | 5886 |
| 373 | 233 | 326 | 93 | 142 | 156 | 111154 |

At p=373 the newly resolved source decomposition reads `S_373/p = 142+156=298 (mod 373)`, in agreement with the previously recorded original scalar `S_373=111154 (mod 139129)` and `2u_373=298`. Neither trace port may be omitted in the fourth-digit calculation. In particular, the second port contributes 156 mod 373, a concrete information-loss witness against a unit-only reduction.

## 4. BRC/observer interface and obligations

**BRC resolution: COMPOSE_APPLIED** (signed graded provenance carrier, not a positive-mass replacement). Population is the finite original overflow coefficients `e_(p+r)`; branch labels are `r≤q`, `q<r≤3q`, `r>3q`; observed output is the sigma-even trace `S_p (mod p²)` with a retained sigma-odd repair `g_p` and the original k/j signs. Valuation lower bounds and endpoint degree prove exactly which port may be compressed; separate digit/carry data are preserved.

**Next direct mathematical action:** derive a telescoping identity for the now-explicit harmonic-low-band and one-zero-factor-middle-band traces, proving `L_p/p + M_p/p=48g_p` for all target primes, ideally with a signed WZ/Jacobi certificate. This remains OPEN. The parent AF4 and original native H0/B0 p373 `[X]U mod 139129`, rank, semilinear Frobenius/eta, κ and Delta−R are separately OPEN, and support Issue #1559 is PENDING_OWNER. No native benchmark run, Source CLAIM/run/checkpoint, mathematical admission or independent review is represented by this file.

Original science pin, authorship and source separation are preserved. Prior dependency: `research_notes/portable_direct/20261110_onhour_d25_CM_overflow_scalar_trace_reflection.md` (author-side; not independently reviewed). Authored in the present Research lane; current authorized GitHub publication does not grant Source execution authority.
