# D25: signed two-coset, order-two k-recurrence and exact finite-boundary transfer

**2026-11-05 / TASK_RESEARCH / AUTHOR-SIDE PROVED DERIVATION + 8-PRIME EXECUTED CHECK / UNREVIEWED / NOT_ADMITTED.**
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`; research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (never the maintenance conversation).

## Inputs and theorem

Consume the previously authored *unreviewed* finite CM-cusp transport `research_notes/portable_direct/20261105_onhour_d25_cusp_integral_terminating_transport.md` @ `568aa5423a0546f5f4cc6dc74a00b102150cb5ab`. In `R=Z[1/6]`, it supplies `t(s)=s³U(s)`, `N(s)`, `U(0)=32/729`, `N(0)=1`, and

```
U(s)=32/729 +(56/6561)s² -(416/531441)s³ +...
N(s)=1 +(1/27)s² -(1/243)s³ +...
T[n,k]=9^k (3/2)^n [s^(2n)] N(s)t(s)^k .
```

Put `x=s²`, and uniquely write `t(s)=A(x)+sB(x)` and `N(s)t(s)^k=E_k(x)+sO_k(x)`. The **exact two-channel transition** is

```
(E_(k+1),O_(k+1))^tr
   = [[A,xB],[B,A]] (E_k,O_k)^tr .
```

Its characteristic determinant is `D=A²-xB²=t(s)t(-s)=-x³U(s)U(-s)`. Therefore the even coefficient carrier has the exact, **second-order scalar k-recurrence**

```
E_(k+2)=2A E_(k+1)-D E_k,
E_0=N_even,  E_1=A N_even+xB N_odd .
```

No loss of the odd-by-odd signed interaction occurs: it is carried by `D` and the initial state. For each prime `p>3`, all coefficients lie in `Z_p`.

Define the original 2304 coefficient `b_k=(4k)!/[2304^k(k!)⁴]`, its rational ratio `r_k=(4k+1)(4k+2)(4k+3)(4k+4)/[2304(k+1)⁴]`, and `F_k(x)=b_k9^kE_k(3x/2)`. Let `A_*=A(3x/2)` and `D_*=D(3x/2)`. Then, **as a rational formal series identity**,

```
F_(k+2) = 18 r_(k+1) A_* F_(k+1)
           - 81 r_k r_(k+1) D_* F_k.             (1)
```

In the original finite range `0<=k<=K-2`, `K=floor(2(p-1)/3)`, all denominator factors in `r_k,r_(k+1)` are p-units. Equation (1) is a p-integral across-k recurrence for the *signed original model-labelled* kernel `f_(n,k)=[x^n]F_k=b_kT[n,k]`; no illegal division by a possibly p-divisible `b_k` is made.

## Theorem: exact finite-prefix boundary recurrence

Set `Z_k(L)=sum_(n=0..L)f_(n,k)` and `S_k(L)=sum_(n=0..L)(6n+1)f_(n,k)`. Expand `A_*=sum a_j x^j` and `D_*=sum d_j x^j`. Coefficient convolution with the weight identity `6(m+j)+1=(6m+1)+6j` proves, for every integer `L>=0`,

```
S_(k+2)(L)
 = 18r_(k+1) sum_(j=0..L)a_j[S_(k+1)(L-j)+6j Z_(k+1)(L-j)]
 - 81r_k r_(k+1)sum_(j=0..L)d_j[S_k(L-j)+6j Z_k(L-j)].    (2)
```

The corresponding `Z` recurrence omits the `6jZ` terms. This retains every signed finite cutoff; it does not replace a truncated sum by an infinite analytic period. In particular, with `h=(p-1)/2` and the same `K`, the earlier exact source residual is

`E_p=sum_(k=0..K)[S_k(p-1)-(8k+1)b_k 1_(k<=h)]`.

The previously established 2304 full-vs-half theorem then supplies `W_p-V_p=E_p (mod p³)`. The open mother target is to prove `E_p=0 (mod p³)` for all p≡13 or 19 mod24. Equation (2) is the first direct, explicitly finite-boundary k-recurrence for this particular cusp kernel; its k-summation still requires a telescoping argument.

## Sharp rational edge and typed BRC no-go

For `d=2n-3k`, the source series give `T[n,k]=0` for `d<0` or `d=1`; for `d=0,2,3` they give respectively

```
9^k(3/2)^n U0^k,
9^k(3/2)^n U0^k(1/27+7k/36),
-9^k(3/2)^n U0^k(3+13k)/729.
```

Consequently the exact *first nonzero* entries, for every integer m>=0, are

`T[3m,2m]=(128/243)^m` and
`T[3m+3,2m+1]=-8(8+13m)/2187 * (128/243)^m`.

Already `T[3,1]=-64/2187`. Projecting away odd s powers before multiplying `N(s)t(s)` would instead yield `-52/2187`; the omitted **odd × odd** contribution is `-4/729`, nonzero modulo every p>3. This exact counterexample concerns premature one-step parity deletion, while the proved two-channel and scalar order-two approaches preserve all declared future operations.

## Executed independent arithmetic and next science

The local full checker `d25_signed_two_channel_transfer_20261105.py` uses the earlier published project checker solely for the common U/N polynomial primitives; it independently checks the matrix recurrence, the scalar k-recurrence, the weighted recurrence (1), finite-prefix equation (2) at L=h,p-1, raw integer-binomial coefficients, and rational edge certificates. **Eight primes p=5,7,11,13,19,23,31,37; 0 assertion failures**, modulo p³; see adjacent `20261105_onhour_d25_signed_two_coset_execution.json`.

The previously published two-block original witnesses are reproduced exactly: at p=13, modulus 2197, `(e_0,low,high)=(646,741,1456)`; at p=19, modulus 6859, `(3081,950,5909)`. The two nonzero signed blocks cancel. The BRC carrier retains `(model,prime,n,k,parity-even,parity-odd,weight,valuation,finite-cutoff,carry)`; either the two channels or the exact order-two determinant repair preserves the next multiplication/readout.

**Next exact action:** seek a k-telescoping multiplier or summation functional of (2), prove the full signed boundary at h,K is divisible by p³ for the two frozen prime classes, and check it first at p13/19. Native original-class p373 H0/B0 divided-power `[X]U mod 139129`, rank, semilinear Frobenius, eta, kappa, signed observer and independent replication remain a separate pending execution with support Issue #1559. This author-side publication is neither a Source CLAIM/run/checkpoint nor an admitted Result.
