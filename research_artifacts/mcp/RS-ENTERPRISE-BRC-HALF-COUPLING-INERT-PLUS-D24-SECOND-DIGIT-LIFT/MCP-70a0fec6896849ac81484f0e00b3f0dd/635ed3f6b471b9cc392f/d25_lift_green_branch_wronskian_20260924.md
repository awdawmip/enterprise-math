# D25 LIFT — reflected boundary as a Gauss Green branch and exact finite Wronskian

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed durable frontier

Do not reopen D24 UR/JT0, the global parameter jet, shell/I1/I2/I0, or the Clausen box-defect reduction. Consume the authenticated checkpoint whose live certificate is

    W_p == S_p^2 + 12 S_p D_p - 2 p^2 C_m  (mod p^3),

for p=6m+1 in the target classes, with

    C_m = sum_{1<=r<=j<=m} (6(j-r)+1) x_j y_r  (mod p),
    y_1 = 1/10,
    y_{r+1}/y_r = 36 r^2 / ((6r+5)(3r+2)).

The only new question here is whether the reflected boundary is an arbitrary auxiliary chain or part of the same finite Gauss operator as the low half-series.

## 1. Low branch and its finite Gauss operator

Work in F_p and put

    a_j := x_j (mod p),  0<=j<=m.

Because p=6m+1,

    a_j = (-m)_j (-2m)_j / (j!)^2 * 2^{-j}
        = binom(m,j) binom(2m,j) 2^{-j}.

Hence

    2(j+1)^2 a_{j+1} = (m-j)(2m-j)a_j.                 (1)

Define

    A(z)=sum_{j=0}^m a_j z^j,
    theta=z d/dz,
    L_m = 2 theta^2 - z(m-theta)(2m-theta).

Then coefficientwise (1) is exactly

    L_m A = 0.                                           (2)

This keeps the low-index provenance; no total-only quotient is used.

## 2. The reflected high boundary is the negative-index Green branch

The checkpoint recurrence for y_r simplifies in F_p because

    6r+5 = 6(r+m+1),
    3r+2 = 3(r+2m+1).

Therefore

    y_{r+1}/y_r = 2r^2/((r+m+1)(r+2m+1)),               (3)

or equivalently

    2r^2 y_r = (r+m+1)(r+2m+1)y_{r+1}.                  (4)

Introduce the negative Laurent branch

    G(z)=sum_{r>=1} y_r z^{-r}.

For every negative power z^{-r}, equation (4) is exactly the vanishing coefficient condition for L_m G. The only unmatched coefficient is the splice at z^0, coming from r=1:

    L_m G = -(m+1)(2m+1)y_1.                            (5)

Since m=-1/6 in F_p and y_1=1/10,

    (m+1)(2m+1)y_1 = (5/6)(2/3)(1/10)=1/18.

Thus the reflected high-p^2 boundary is not arbitrary data but the unique normalized negative-index branch with a one-point source defect:

    BOXED:  L_m G = -1/18.                               (G)

The source defect is precisely the missing n=0 splice between the positive polynomial branch A and the negative reflected branch G. This is a provenance-preserving BRC interpretation: the high boundary is retained as an oriented companion branch, not erased as an O(p^2) tail.

## 3. C_m as an exact positive-Laurent projection

Let

    H(z)=A(z)G(z)=sum_{h in Z} h_h z^h.

Because deg A=m, for 0<=h<=m-1,

    h_h = sum_{r=1}^{m-h} a_{h+r} y_r.                  (6)

Reindex j=h+r in the checkpoint boundary sum. Then, exactly in F_p,

    C_m
      = sum_{h=0}^{m-1} (6h+1) h_h
      = [(6 theta+1) [A(z)G(z)]_{>=0}]_{z=1}.            (7)

Here [ ]_{>=0} means nonnegative Laurent projection. This is a safe quotient only for the declared observer C_m mod p: (6) is a bijective reindexing of the original labelled low/high pairs, so no multiplicity or boundary provenance is lost.

## 4. Exact inhomogeneous Wronskian identity

In ordinary derivatives,

    L_m f = z^2(2-z) f'' + [2z+(3m-1)z^2] f' - 2m^2 z f.

Let

    W(z)=A(z)G'(z)-A'(z)G(z).

Using L_m A=0 and L_m G=-1/18, and the integrating factor

    mu(z)=z/(2-z)^{3m},

we obtain the exact finite Green/Wronskian law

    BOXED:
    d/dz { z (A G' - A' G)/(2-z)^{3m} }
      = - A(z) / [18 z (2-z)^{3m+1}].                   (W)

This is an all-target algebraic identity in the same Gauss operator. It exposes the compensation sought by the current continuation: the low value/derivative branch and the reflected boundary are coupled by one constant source defect.

## 5. What this does and does not prove

Proved here: (G), (7), and (W), for every target prime p=6m+1 for which the consumed D25 boundary chain is defined. These are algebraic consequences of the authenticated checkpoint and do not use the finite scan as proof.

Not proved: the final second-digit congruence W_p == p (mod p^3). To close LIFT one still must connect the positive-part observable in (7), equivalently the Green/Wronskian source term, to the p-adic second digits of the full truncated S_p and D_p.

A separate exact regression over all 166 target primes p<5000 checks the low recurrence, the converted Green recurrence, the source -1/18, and equality of the original double-sum C_m with (7); zero failures. This remains falsification only.

BRC_REUSE_RESOLUTION = COMPOSE_APPLIED.
Observer = C_m mod p plus the surviving W_p mod p^3 certificate.
Preserved = low index j, reflected high index r, orientation, valuation provenance, and the splice-source defect.
Forbidden compression = setting G or C_m to zero, unsigned mass replacement, or treating the finite regression as an all-prime proof.

## 6. Narrow next action

Exploit (W) together with the positive-part operator in (7) to derive a finite residue/constant-term identity at z=1 (or an equivalent contiguous telescoper) that expresses C_m directly in terms of the second p-adic digits of S_p and D_p. The exact target remains

    S_p^2 + 12 S_p D_p - 2p^2 C_m == p  (mod p^3).

Do not reopen the completed D24 first digit or the earlier D25 jet/shell reductions.
