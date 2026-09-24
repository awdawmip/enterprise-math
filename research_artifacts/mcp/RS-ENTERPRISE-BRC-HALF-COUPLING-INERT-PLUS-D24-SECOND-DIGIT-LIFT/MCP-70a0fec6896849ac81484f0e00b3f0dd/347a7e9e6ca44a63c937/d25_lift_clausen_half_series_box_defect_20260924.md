# D24 second-digit LIFT: Clausen half-series box defect and reflected p^2 boundary

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED
Date: 2026-09-24
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7

## 0. Consumed frontier

Keep the accepted D24 UR/JT0 parent and the already-published D25 observer/shell/I1/I0/global-jet checkpoints. In particular,

    W_p == p (mod p^3)

is the exact remaining LIFT certificate for every p == 13 or 19 (mod 24), and the immediately preceding durable frontier rewrites W_p as one global finite parameter jet P_n(epsilon) with a source-labelled tail chain d_r and two valuation jumps.

This note does not reopen those units. It changes representation again, using an exact Clausen factorization at the actual evaluation point epsilon=p/3. The result eliminates the epsilon-derivative coordinates entirely and localizes every truncation defect, modulo p^3, to one low/high boundary coupling.

Throughout

    p = 6m+1,
    n = 2m = (p-1)/3.

## 1. Exact binomial and Clausen forms

At epsilon=p/3 the weighted carrier is

    W_p =
      sum_{k=0}^{p-1}
      (6k+1) (1/2)_k (1/3)_k (2/3)_k
      --------------------------------------  2^{-k}.
                       (k!)^3

Equivalently, by duplication/triplication,

    boxed:
    W_p =
      sum_{k=0}^{p-1}
      (6k+1) binom(2k,k)^2 binom(3k,k) / 216^k.          (B)

Define

    f_j = (1/6)_j (1/3)_j / (j!)^2,
    x_j = f_j / 2^j.

Clausen's identity with a=1/6 and b=1/3 is

    _2F_1(1/6,1/3;1;z)^2
      =
    _3F_2(1/2,1/3,2/3;1,1;z).

Therefore coefficientwise, for every k>=0,

    (1/2)_k(1/3)_k(2/3)_k / (k!)^3 * 2^{-k}
      =
    sum_{j+l=k} x_j x_l.                                  (Cl)

This is an exact rational identity, not a congruence.

The same Clausen specialization is part of the classical d=3 Ramanujan/CM mechanism used by Chisholm--Deines--Long--Nebe--Swisher, "p-Adic Analogues of Ramanujan Type Formulas for 1/pi", Mathematics 1 (2013), 9--30, DOI 10.3390/math1010009. Their general theorem supplies the accepted first-digit input at the parent scope; the present p^3 truncation-defect calculation below is a separate finite congruence calculation and does not claim that the 2013 modulo-p^2 result already proves LIFT.

## 2. Full box minus the triangular truncation defect

Put

    S_p = sum_{j=0}^{p-1} x_j,
    D_p = sum_{j=0}^{p-1} j x_j.

By (Cl),

    W_p
      =
    sum_{j,l >= 0, j+l <= p-1}
      (6(j+l)+1) x_j x_l.

If the triangular condition j+l<=p-1 is removed, the full p-by-p box is

    sum_{0<=j,l<p} (6(j+l)+1)x_jx_l
      =
    S_p^2 + 12 S_p D_p.                                   (FB)

Hence exactly

    W_p = S_p^2 + 12 S_p D_p - T_p,

where

    T_p =
      sum_{0<=j,l<p, j+l>=p}
      (6(j+l)+1)x_jx_l.                                   (T)

The only question is which part of T_p remains visible modulo p^3.

## 3. Exact valuation strata of the half-series

For j<p all denominator factors in x_j are p-units. Because p=6m+1:

- (1/6)_j first acquires its unique p-factor at j=m+1, from 6m+1=p;
- (1/3)_j first acquires its unique p-factor at j=2m+1, from 3(2m)+1=p;
- before j=p neither rising factorial acquires another p-factor.

Consequently

    boxed:
    v_p(x_j) =
      0, 0 <= j <= m,
      1, m < j <= 2m,
      2, 2m < j <= p-1.                                  (Vx)

Now inspect a pair (j,l) in the defect region j+l>=p=6m+1.

If both j and l exceed m, then they cannot both lie at most 2m, since j+l<=4m<p. Thus at least one is >2m. The total valuation is then at least 1+2=3, so the pair is invisible modulo p^3.

The only defect pairs of valuation <3 therefore have one index in 1,...,m and the other at least p-j. They have valuation exactly 2. By symmetry,

    T_p
      ==
    2 sum_{j=1}^m sum_{l=p-j}^{p-1}
        (6(j+l)+1)x_jx_l                                  (mod p^3).

Write l=p-r. Then 1<=r<=j<=m. Since x_{p-r} has valuation exactly 2, the coefficient 6(j+p-r)+1 may be reduced modulo p after dividing out p^2. Therefore

    boxed:
    W_p
      ==
    S_p^2 + 12 S_p D_p - 2 p^2 C_m                       (mod p^3),   (CB)

where

    C_m =
      sum_{1<=r<=j<=m}
        (6(j-r)+1) x_j y_r                                (mod p)

and

    y_r := x_{p-r}/p^2                                    (mod p).    (Ydef)

Thus every p^3-visible truncation defect is a low-unit / high-p^2 coupling. The entire middle valuation-1 band is absent from the defect observer because it can enter j+l>=p only together with a valuation-2 port.

## 4. Exact reflection of the high p^2 boundary

The high coefficient in (Ydef) has a p-independent complementary-parameter reflection.

For 1<=r<=m,

    boxed:
    y_r
      ==
      2^(r-1) (r-1)!^2
      -------------------------------                     (mod p).   (Y)
      18 (5/6)_r (2/3)_r

Proof.

Write

    x_{p-r}
      =
    [(1/6)_{p-r}/(p-r)!]
    [(1/3)_{p-r}/(p-r)!]
    2^{-(p-r)}.

For A_r=(1/6)_{p-r}/(p-r)!, use

    (1/6)_{p-r}
      =
    6^{-(p-r)} prod_{i=0}^{p-r-1}(6i+1).

The affine map i -> 6i+1 permutes F_p, with its unique zero at i=m. The product of all nonzero residues is -1 by Wilson. The omitted r indices i=p-r,...,p-1 contribute

    prod_{s=1}^r (1-6s)
      =
    (-1)^r prod_{s=1}^r(6s-1).

Also

    (p-r)! == (-1)^r/(r-1)!                              (mod p)

and 6^{p-r}==6^{1-r} (mod p). Dividing the unique p-factor gives

    A_r/p
      ==
    -(r-1)!/[6(5/6)_r]                                   (mod p).

The same argument for B_r=(1/3)_{p-r}/(p-r)! gives

    B_r/p
      ==
    -(r-1)!/[3(2/3)_r]                                   (mod p).

Finally 2^{-(p-r)}==2^{r-1} (mod p), so multiplying the two normalized factors proves (Y).

In particular the reflected chain is hypergeometric with

    y_1 = 1/10,

    boxed:
    y_{r+1}/y_r
      =
    36 r^2 / [(6r+5)(3r+2)].                             (Ry)

No p-dependent high index remains in this recurrence.

## 5. Linear-time prefix form of the defect

Although C_m is naturally a triangular source-coupling, it need not be evaluated quadratically. Define

    Y_j = sum_{r=1}^j y_r,
    Z_j = sum_{r=1}^j r y_r.

Then

    boxed:
    C_m
      =
    sum_{j=1}^m x_j [(6j+1)Y_j - 6Z_j]                   (mod p).   (CP)

This keeps the same low/high provenance while exposing a one-pass boundary carrier.

Equations (CB), (Y), and (CP) are the strict reduction:

    LIFT
      <=> 
    S_p^2 + 12 S_p D_p - 2p^2 C_m == p                  (mod p^3),

where S_p and D_p are the value and logarithmic z-derivative of one truncated half-series

    _2F_1(1/6,1/3;1;z)

at z=1/2, and C_m is a mod-p complementary-parameter boundary chain. There are no epsilon-derivative coordinates and no independent I1/I2 shell carriers in this representation.

This does not yet prove the final congruence.

## 6. BRC information audit

Population:
all source ports of the weighted terminating 3F2, now lifted through the exact Clausen convolution to ordered half-series pairs (j,l).

Observer:
W_p modulo p^3.

Preserved coordinates:
the two half-series indices, the triangular truncation predicate j+l<p, p-adic valuation, the low/high orientation, and the complementary high-boundary reflection index r=p-l.

Safe quotients:
all defect pairs of valuation >=3 are removed only after (Vx); symmetry is used only after the low/high sectors are disjoint. The high p^2 port is then replaced by its proved normalized reflection (Y), which preserves its source as y_r.

Forbidden quotients:
do not replace C_m by zero, an unsigned mass, or a generic O(p^2) tail. Do not infer the p^3 target from the accepted parent p^2 theorem. Do not use the finite regression below as proof.

BRC_REUSE_RESOLUTION = COMPOSE_APPLIED.

## 7. Deterministic exact regression

The companion checker works entirely with integer modular arithmetic. For every target prime p<5000 it verifies:

1. the exact valuation strata (Vx);
2. every reflected boundary value x_{p-r}/p^2 == y_r (mod p);
3. the Clausen full-box defect formula (CB) against a direct weighted 3F2 recurrence;
4. the already-observed target congruence W_p==p (mod p^3), only as falsification/regression.

Result:

    target primes = 166
    p mod 24 = 13: 83
    p mod 24 = 19: 83
    failures = 0

Checker SHA-256:

    887876101f244e5990f5baa0b3dd8f37afde587a20bffe202a6d8988968e12a0

The proof of the strict reduction is Sections 1--5; the finite scan is not substituted for it.

## 8. New narrow frontier

The previous global-jet problem has been replaced by a half-series boundary problem.

Next, seek an all-target identity for

    S_p^2 + 12 S_p D_p - 2p^2 C_m,

preferably by a finite Wronskian/contiguous relation for the truncated
_2F_1(1/6,1/3;1;z) at z=1/2 together with the complementary chain (Ry).
Equivalently, derive a creative-telescoping certificate that makes the
boundary correction C_m explicit in the second p-adic digit.

Do not return to the disproved naive k<->n-k antisymmetry and do not reopen D24 UR/JT0. The new target is the exact compensation between the half-series value/derivative and the reflected p^2 triangular boundary.
