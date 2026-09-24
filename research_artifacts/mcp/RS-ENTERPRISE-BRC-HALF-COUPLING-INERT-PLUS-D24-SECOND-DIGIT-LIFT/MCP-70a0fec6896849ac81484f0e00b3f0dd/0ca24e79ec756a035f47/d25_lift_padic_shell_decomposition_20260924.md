# D24 second-digit LIFT: exact p-adic shell decomposition of the third-digit observer

Status: PROVED_DERIVATION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

## 0. Consumed durable frontier

Use the already-derived exact observer

E_p = (W_p-p)/p^2 (mod p),

where p=6m+1, p≡13 or 19 (mod 24), and

W_p = sum_{k=0}^{p-1} t_k,
t_k = (6k+1) * binom(2k,k)^2 * binom(3k,k) / 216^k.

The live LIFT statement is exactly E_p=0. This note does not reopen UR/JT0 and does not use the finite scan as proof.

## 1. Exact valuation shells

Put

C_k = binom(2k,k)^2 binom(3k,k) / 216^k.

For 0<=k<p, Legendre's formula gives exactly

v_p(C_k)
 = 2 floor(2k/p) + floor(3k/p) - floor(2k/p)
 = floor(2k/p) + floor(3k/p).

Because p=6m+1, this gives four shells:

I0: 0<=k<=2m,      v_p(C_k)=0;
I1: 2m+1<=k<=3m,   v_p(C_k)=1;
I2: 3m+1<=k<=4m,   v_p(C_k)=2;
I3: 4m+1<=k<=6m,   v_p(C_k)=3.

The weight 6k+1 never lowers a valuation. In 0<=k<p it is divisible by p only at k=m, where it raises the valuation by one.

Therefore every I3 term vanishes individually modulo p^3. If

S_j = sum_{k in I_j} t_k,

then

W_p ≡ S_0 + S_1 + S_2 (mod p^3).                    (1)

This is a provenance-preserving deletion: the discarded I3 population is pointwise invisible to the p^3 observer, rather than cancelled only after summation.

## 2. The p^2 boundary shell has a universal low-index recurrence

For 1<=r<=m define

a_r = t_{3m+r}/p^2 (mod p).

The exact hypergeometric term ratio

C_{k+1}/C_k
 = (2k+1)(3k+1)(3k+2) / (36 (k+1)^3)

implies, after k=3m+r and 6m+1=p,

a_{r+1}/a_r
 =
 r(6r-1)(6r+1)(3r+2)
 ---------------------------------
 9(2r+1)^3(3r-1)
 (mod p).                                             (2)

All denominators in (2) are p-units for 1<=r<m.

The initial value is also explicit. At k=3m+1=(p+1)/2,

p^{-1} binom(2k,k) ≡ -1/(k!)^2 (mod p),

binom(3k,k) ≡ (p+3)/2 (mod p),

and 6k+1 ≡ 4 (mod p). Hence

a_1 ≡ 6 / ((k!)^4 216^k) (mod p).

Wilson's theorem gives
((p-1)/2)!^2 ≡ (-1)^((p+1)/2) (mod p),
so k!^4 ≡ 1/16 (mod p). Euler's criterion then yields

a_1
 ≡ 96 * 216^{-(p+1)/2}
 ≡ (4/9) (6/p)
 (mod p),                                             (3)

where (6/p) is the Legendre symbol. In the two task classes,

p≡13 (mod24): (6/p)=-1,
p≡19 (mod24): (6/p)=+1.

Thus the residue-class identity survives explicitly as a signed source coefficient.

## 3. Fixed-parameter truncated 5F4 form

Define q_0=1 and

q_s =
 (1)_s^2 (5/6)_s (7/6)_s (5/3)_s
 ----------------------------------- * (1/2)^s / s!,
 (3/2)_s^3 (2/3)_s

for s>=0. Its ratio is

q_{s+1}/q_s
 =
 (1/2)(s+1)(s+5/6)(s+7/6)(s+5/3)
 ------------------------------------------------
 (s+3/2)^3(s+2/3),

which is exactly (2) after r=s+1. Therefore

a_{s+1} = a_1 q_s (mod p).

Writing

K_m = sum_{s=0}^{m-1} q_s
    = truncated _5F_4(
        1,1,5/6,7/6,5/3;
        3/2,3/2,3/2,2/3;
        1/2
      ) through s=m-1,

we obtain the exact boundary-shell certificate

boxed:
S_2/p^2 ≡ (4/9)(6/p) K_m (mod p).                  (4)

Consequently

boxed:
W_p ≡ S_0 + S_1 + p^2 (4/9)(6/p) K_m (mod p^3).   (5)

The accepted first-digit theorem W_p≡p (mod p^2) and S_2≡0 (mod p^2) show that

S_0+S_1≡p (mod p^2),

so the quotient

E_low,p := (S_0+S_1-p)/p^2 (mod p)

is well-defined. The live observer splits exactly as

boxed:
E_p ≡ E_low,p + (4/9)(6/p)K_m (mod p).             (6)

Thus LIFT is equivalent to the lower-shell identity

E_low,p ≡ -(4/9)(6/p)K_m (mod p).                  (7)

## 4. BRC / information-loss audit

Population:
the weighted k-ports t_k, retaining k, p-adic valuation shell, residue class and source formula.

Allowed quotient:
I3 is removed only because every individual member has valuation >=3. No signed cancellation is used for that deletion.

Preserved repair coordinate:
I2 is not collapsed to its total blindly. Its normalized p^2 residue is first reconstructed by the exact recurrence (2), whose initial coefficient (3) keeps the class-13/class-19 Legendre sign. Only then is it summarized by K_m.

Not erased:
the I0/I1 aggregate still contains the unresolved second-digit information. Equation (6) does not claim it is zero and does not treat K_m as the whole observer.

Scientific gain:
the p^3 observer no longer needs the upper third of the original p-term population; the entire surviving p^2 boundary shell is transported to a fixed-parameter length-m 5F4 object. The next proof search can target the lower-shell quotient E_low,p and its exact compensation with K_m.

## 5. Deterministic regression

The accompanying pure-Python checker:
- generates the t_k recurrence modulo p^3 without large binomial integers;
- checks the four valuation shells;
- checks I3 pointwise vanishing;
- checks (3);
- checks recurrence (2) for every r;
- checks (4)-(5).

For every target prime p<5000:
166 primes total, 83 in each residue class;
all checks pass.

Checker SHA-256:
1749b4a3832eeda2d6210cfe7e45dff1a07d7490cc19396f1d2c0c97dab6f6fd

This regression is not an all-prime proof; the all-prime proof of (1)-(7) is the valuation/factorial/ratio derivation above.

## 6. Next exact unit

Do not enlarge the prime scan and do not reopen the accepted first digit.

The next narrow unit is the I1 shell. It contributes p times a nontrivial unit sequence, so E_low,p needs its first p-adic correction, not only its reduction modulo p. Derive an exact low-index reflection/deformation for S_1 modulo p^3 (equivalently S_1/p modulo p^2), retaining the derivative/harmonic correction generated by the p-shift. The aim is to express E_low,p in a fixed-parameter low-index carrier that can be compared termwise or telescopically with K_m.
