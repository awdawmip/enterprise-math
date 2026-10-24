# D25/LIFT — exact same-prime third-digit five-port transport and four resonance modes

2026-10-24 | TASK_RESEARCH author-side exact algebra + executed modular checks | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Not an admitted Source Result, native benchmark, formal checkpoint, Lean proof or independent review.

Parent `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; task publication `TP2-B6F4FC938FF94941C1B7`. Frozen **scientific** Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged. This author's ordinary Research logical lane is `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance lane. Inherit (without re-crediting) full exact WZ from commit `c7fb90fd7ec451a954b553b963dd85d4ec99fc96` and earlier same-prime plateau from `6fceb814b36be8245eb0038e6cb0ac38de46e42f`.

## 1. Preserve the exact original five WZ sources

As in the frozen original source, for `r,n>=0` set
```
A_r = (6r)! / [3^(6r)*((2r)!)^3]
R_(r,0)=1
R_(r,n+1)/R_(r,n) =
   (4r+2n+1)(3n+1)(3n+2) / [36(n+1)(2r+n+1)(4r+n+1)]
T_(r,n)=A_r*(6n+12r+1)*R_(r,n)
S_r=sum_(n=0)^(4r) T_(r,n).
```
The previously proved exact rational full-summand WZ identity yields `S_(k+1)-S_k = E_0+E_1+E_2+E_3+E_4`, where `N=4k+1`, `E_0=T_(k,N)g(k,N)` is the **old-rank WZ boundary**, and `E_j=T_(k+1,4k+j)`, `j=1,...,4`, are the **four new-rank tails**. The original `g` and all coefficients remain unchanged.

## 2. Theorem — exact p³ five-port transport, including resonance

Take **any prime** `p=6m+1`, `m>=2`, and `ceil(m/2)<=k<=m-1`. Put `L=6m-8k`, `Q(k)=360k²+274k+49` and `M=p²`. For `0<=t<2p` define the p-free factorial (mod M)
```
U_p(t) = product_(1<=a<=t, p∤a) a.
```
It is explicitly computable **to the second normalized digit**:
```
U_p(t) = t!                              (t<p)
       = (p-1)!*(t-p)!*(1+p*H_(t-p))      (p<=t<2p; mod p²),
H_s=sum_(a=1)^s 1/a (mod p²).
```
The factor `(p-1)!` is kept modulo `p²`; replacing it by `-1` at this precision would lose the Wilson quotient.

Define one completely explicit modular unit
```
V_p(r,n) =
  [(6r)!*U_p(4r+2n)*U_p(3n)] /
  [3^(6r)*(2r)!*216^n*(n!)²*((2r+n)!)²*U_p(4r+n)] (mod p²).
```
All denominator factors are invertible modulo `p²` for the five indicated ports. Write `B=V_p(k,N)*2(3k+1)Q(k)/[3(2k+1)] (mod p²)`. Then **every one of the five separately labeled original terms is p-integral**, with the following universal third-digit certificate:
```
E_0/p = B * (8k+3)^(-1)                  if L<=0
      = B                               if L=2 (8k+3=p)
      = p*B*(8k+3)^(-1)                 if L>=4

I_j = 1 if L<=j+3 else 0
E_j/p = p^(1-I_j)*V_p(k+1,4k+j)*(36k+6j+13)
        (mod p²), j=1,...,4.
```
The `L=2` clause **cancels the actual p denominator before inversion**; no inverse of p is taken. `Q(k)` is retained in full, including possible vanishing mod p (no unjustified claim of exact valuation one). Consequently
```
(S_(k+1)-S_k)/p = sum_(i=0)^4 E_i/p      (mod p²).             (T)
```
This is at the original required modulus `p³` for **fixed p**, and is not the real-analysis tail bound or an induction between different primes.

### Proof

Multiplication of the unchanged original three-factor recursion gives, in `Q`,
```
A_r*R_(r,n) =
 (6r)!*(4r+2n)!*(3n)! /
 [3^(6r)*(2r)!*216^n*(n!)²*((2r+n)!)²*(4r+n)!].             (F)
```
At the old port `(r,n)=(k,4k+1)` and all four new ports `(r,n)=(k+1,4k+j)`, both numerator factorials `(4r+2n)!` and `(3n)!` contain **exactly one p each** (their arguments are `[p,2p)`). All other factorial arguments lie below p except `4r+n`, whose factorial contains one p iff `4r+n>=p`. Every factorial argument is less than `2p`. Therefore
```
A_r*R_(r,n) = p^(2-[4r+n>=p])*V_p(r,n) (mod p³).
```
The original quartic WZ coefficient factors **exactly**, without a congruence approximation:
```
(6N+12k+1)*g(k,N) =
  2*(3k+1)*(360k²+274k+49) / [3*(2k+1)*(8k+3)].
```
The old factorial denominator contains p iff `8k+1>=p` (`L<=0`); the separate WZ denominator contains p iff `8k+3=p` (`L=2`). Both effects cannot happen together. For the jth new tail, `4(k+1)+4k+j=8k+j+4`, so its factorial denominator contains p iff `j+3>=L`. Each new linear factor `36k+6j+13` is p-unit: it lies strictly between `3p` and `6p`, is `1 mod 6`, and none of `4p,5p` is. Finally the explicit p-free factorial formula follows from `(p-1)! prod_(a=1)^(t-p)(p+a)` and first-order expansion modulo `p²`. Substitute into the exact five-tail WZ recurrence to obtain every readout and (T). **These steps are an all-primes proof, not a finite-sample inference.**

## 3. Theorem — four prime-class boundary modes

Let `k* = floor((3m-4)/4)+1` be the **first** rank beyond the earlier proved mod-`p²` plateau. Write `m=4a+b`, `b=0,1,2,3`; then `k*=3a+(0,0,1,2)_b`, so `L(k*)=(0,6,4,2)_b`. Thus:

| p mod 24 | first L | first-digit-eligible original WZ ports |
| --- | ---: | --- |
| 1 | 0 | old boundary with factorial-p denominator; all four new tails |
| 7 | 6 | new tails j=3 and 4 only |
| **13** | **4** | **four new tails only**; old boundary is at least p² |
| **19** | **2** | **resonant old boundary plus four new tails** |

These are **support/valuation classifications**, not assertions that individual residues or their signed sum are nonzero. In particular the target prime classes `p≡13,19 (mod 24)` require different boundary evidence. For all `L>=8` each original port has valuation at least two, exactly respecting the inherited plateau. For each later rank, L decreases by eight and the same unmodified formula applies.

## 4. Full upper-half reduction at the frozen target modulus

Let `ell=ceil(m/2)` and `d_(p,k)=sum_i(E_i/p) mod p²` from the theorem. Then
```
S_m = S_ell + p*sum_(k=ell)^(m-1) d_(p,k) (mod p³).         (H)
```
Hence the original fixed-class hard target is **equivalent**, without any extra divisibility assumption on the seed, to
```
S_ell + p*sum_(k=ell)^(m-1) d_(p,k)
    = p*(4/3)^(p-1) (mod p³).
```
The formula replaces the upper-half original hypergeometric recurrence by explicit factorial-Wilson-harmonic local ports at the required precision; the lower seed remains nontrivial and is **not assumed divisible by p**. It does not establish the final congruence by itself.

## 5. Executed exact checks and provenance

The accompanying Python checker independently reconstructs **both** (a) the factorial `U_p(t)` including harmonic corrections modulo p² and (b) the original three-factor R recurrence, original unsimplified quartic WZ `g`, stripped individual p-valuations and actual full `S_(k+1)-S_k` modulo p³. For every prime `p<=1000`, `p=6m+1`, `m>=2`, **3027/3027 fixed-prime rank transitions** passed all **five separate** normalized-`p²` readouts and their full signed sum. The 79 first plateau exits were classified as `(14,20,22,23)` in the four `m mod4` classes. This is author exact computational verification, **not** an infinite proof, native benchmark or independent review.

For `p=211,m=35,k*=26,L=2`, the five readouts `(E_0,...,E_4)/p mod 44521` are `(37325,26960,2188,10171,3019)`; their sum is `35142`. The full late ranks `k=26..34` sum to `8440 mod 44521`; total upper-half `k=18..34` sums to `28274 mod 44521`. At `p=37,m=6,k*=4,L=4`, the five readouts are `(185,294,1060,245,1269) mod 1369`; sum `315`, whose first digit is `19 mod37`, matching the earlier sharpness example.

**Checker:** `research_notes/portable_direct/20261024_onhour_d25_same_prime_five_tail_p3_four_resonance_modes_check.py`. Mathematical proof status: author proof over all stated primes, with independent in-turn integer computations as checks; Source admission remains pending.

**BRC/Enterprise coordinates:** `COMPOSE_APPLIED/REUSE_APPLIED`. The typed observer keeps integer prime p, rank k, five provenance-labeled terms, valuations and p-adic unit jets; it only takes their total under the explicitly proven modulo-p³ future finite-sum observer. This is scalar number-theoretic evidence, **not a native X6 dynamics claim**. P000 `ACTIVE_LOCKED`, six-axis space + separately typed time, and joint-relation observer preservation remain unchanged.

**Next smallest hard unit:** evaluate `S_ell mod p³` in both prescribed prime classes through the Source-fixed same-class CM/divided-power normalization, or establish a genuine whole-expression WZ cancellation in (H). The unchanged **native benchmark** remains an independent obligation. Do not repeat accepted frozen D24 UR, original exact WZ, earlier LOW/HIGH jets or the completed p/p² plateau.

**Control/source truth:** Gateway 0.6.11 current Sites identity is read-only for Research (`research_authority_granted=false`, `executor_binding_configured=false`). Prior exact continuation `em-r-onhour-t11-continuation-read-20261024` has no retrievable new result (`CONTROL_REQUEST_NOT_FOUND`); existing recovery support issue `awdawmip/enterprise-math#1539` remains open. No lawful new Researcher session, winning CLAIM, open/run, native checkpoint, Result or reviewer acceptance is asserted. Three older neutral UR staging sources remain independent and are not promoted.
