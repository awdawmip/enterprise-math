# D25 author-side proof: finite-field Legendre and the mod-p² Clausen moment

2026-10-25; **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Research lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance lane. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, taskbook blob `53a3ef039325534e3715add837f0eee332289984`.

Prior accepted first-digit science and author-side exact cutoff identity are **inputs**, not reproved here; previous author-side Clausen/corner record `cefbad99f03e3b79e0cfc9de624481ed2010ae40`. **Notation collision corrected:** previous author note called its 2F1 sum `R_p`, but the *frozen D25 Taskbook* uses `R_p` for the LIFT target. Here the 2F1 moment is `M_p`, its first moment `N_p`; the taskbook's `R_p` remains unchanged.

## Newly proved modular Legendre identity and derivative unit

For prime p=6m+1≥7 define
```
r_n = (1/6)_n (1/3)_n / (2^n (n!)²)
    = product_{i=0}^{n-1} (6i+1)(3i+1)/(36(i+1)²)
M_p(z) = sum_{n=0}^{p-1} r_n z^n,  M_p=M_p(1),  N_p=M'_p(1)
b_n = binom(m,n)binom(2m,n) / 2^n,   B_m(z) = sum_{n=0}^m b_n z^n.
```
All denominators are p-units. For n>m, r_n=0 mod p. For 0≤n≤m, r_n=b_n mod p. **Polynomial theorem in Fp[z]:**
```
M_p(z) = B_m(z) = P_{2m}(sqrt(1-z/2))   mod p.                 (1)
```
The square root is formal: P_{2m} is even, so the RHS is an ordinary polynomial in z of degree m. Proof: let x=z/2, s²=1−x, Y(x)=P_{2m}(s). Its Legendre ODE becomes
```
x(1-x)Y'' + (1−3x/2)Y' + [m(2m+1)/2]Y = 0.
```
Since 6m+1=p, modulo p this is the Gauss polynomial equation with a=−m, b=−2m, c=1. The unique degree≤m solution with Y(0)=1 has coefficient recurrence
```
(n+1)² a_{n+1} = (m−n)(2m−n) a_n
```
and is Σ binom(m,n)binom(2m,n)x^n; every n+1≤m is invertible. This proves (1) without an illicit infinite truncation.

At s²=1/2 in Fp², differentiating (1) and using (1−s²)P'_k=k(P_{k−1}−sP_k) proves
```
M_p = P_{2m}(s),
N_p = −P'_{2m}(s)/(4s) = m P_{2m}(s) − m P_{2m−1}(s)/s mod p.       (2)
```
Both values actually lie in Fp, by Legendre parity. **Nondegeneracy theorem:** M_p=0 mod p implies N_p≠0 mod p. Otherwise P_{2m}(s)=P_{2m−1}(s)=0; their three-term recurrence can be run backwards (indices< p are units), forcing P_0(s)=0, impossible.

## Newly proved faithful p² lift, with the nonzero middle rank preserved

For 0≤n≤m the following identity holds **exactly in Q**:
```
r_n = b_n ∏_{i=0}^{n−1}(1−p/[6(m−i)])(1−p/[3(2m−i)]).
```
Write e_{m,n}=−(H_m−H_{m−n})/6−(H_{2m}−H_{2m−n})/3, so r_n=b_n(1+p e_{m,n}) mod p².

The middle band m<n≤2m has valuation exactly one. Define h_n=r_n/p mod p by
```
h_{m+1}=b_m*(3m+1)/(36(m+1)²),
h_{n+1}=h_n*(6n+1)(3n+1)/(36(n+1)²), m+1≤n<2m.
```
All these denominators are units. The n>2m band has valuation≥2 and is discarded **only under the modulo-p² observer**. The exact all-prime reduction is
```
M_p = B_m(1) + p*(Σ_{n=0}^m b_n e_{m,n} + Σ_{n=m+1}^{2m} h_n) mod p².  (3)
```
If the independent still-open condition B_m(1)=0 mod p holds, U_p=M_p/p is p-integral and
```
U_p = B_m(1)/p + Σ b_n e_{m,n} + Σ h_n mod p.                 (4)
```
The taskbook accepts W_p=p mod p²; the previous author-side exact Clausen identity gives W_p=M_p(M_p+12N_p)−Q_p with Q_p in p²Zp. Hence, **conditionally on the Legendre zero**, (2)–(4) imply
```
12 U_p N_p = 1 mod p,
−12m U_p P_{2m−1}(s)/s = 1 mod p.                           (5)
```
This uses the accepted first digit; it does not independently prove it.

## Exact checks and remaining hard target

The separate local exact-modular checker `d25_legendre_unit_root_check_20261025.py` recomputed the original r_n to n=p−1, the finite binomial deformation, all middle h_n and an independent Legendre recurrence in Fp[s]/(s²−1/2). It checked (1)–(4) for **all 94 primes p≡1(mod6), p≤1200, plus p=19963** (95 total); 53 target-class primes showed finite-sample B_m=0, N_p≠0 and 12U_p N_p=1. Finite verification is not an all-prime proof of root vanishing.

Examples `(p, N_p, U_p, low-jet, middle-h)`: (13,7,11,3,1), (19,1,8,6,15), (211,42,193,183,10), (19963,6798,11730,15493,13537), all residues modulo p. At p=7, B_m=2 mod7 and U_p is correctly **undefined** as a p-integral quotient. Local full proof SHA256 `93f6dc077b7281ff42dde6f79e26f9c10e2c624a06292ed62fffbbc186111d4f`, checker SHA256 `0affbc9b29e36555ee549f39c48b875efd4ca7c56c0ceafc67056c7ee94138ba`.

**BRC/carrier audit:** rank n, valuation bands [0,m], [m+1,2m], [2m+1,p−1], and derivative observer N_p are retained. Legendre compression is faithful at mod-p zeroth/first moments only; (3) repairs the lost first p-adic digit. This is an applied provenance-preserving valuation composition, not a native X6/physical claim.

**Still OPEN:** universal zero B_m=0 at p≡13,19(mod24), then joint p³ evaluation of M_p(M_p+12N_p)−p²T_p and the exact frozen Delta_p−R_p target. Specifically next prove a finite-field Jacobi/CM or Frobenius identity at P_{(p−1)/3}(1/sqrt2), then an exact p-adic Wronskian/Green cancellation retaining T_p. Native benchmark NOT_EXECUTED. No formal Source-native session/CLAIM/run/checkpoint/Result/review established. Last source continuation read: CONTROL_QUOTA on gateway 0.6.11; support #1539. This GitHub file is **neutral author-side preservation**, not mathematics admission. Frozen source pin and schedule/notification behavior unchanged.
