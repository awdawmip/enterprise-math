# D25 LIFT — adjoint endpoint normalization collapses the reflected correction to one low-branch scalar

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier and provenance
Consume the durable symmetric-mass checkpoint. Thus the live boundary correction C_m is already known to be observer-equivalent to the original 3F2-kernel prefix transform, and the reflected y_r chain is not to be reopened as an independent population. A noncanonical Driver note had separately pointed to a finite adjoint endpoint form; this Researcher unit rederives that algebra under the current task authority and adds the exact terminal normalization needed to remove the reflected chain from the final scalar. No Driver evidence is promoted to Source authority by citation alone.

Work in F_p with p=6m+1, p congruent 13 or 19 mod 24. Keep

a_j = binom(m,j) binom(2m,j) 2^{-j}, 0<=j<=m,
y_1=1/10,
2r^2 y_r=(r+m+1)(r+2m+1)y_{r+1},

and
C_m=sum_{1<=r<=j<=m}(6(j-r)+1)a_j y_r.

## 1. Reverse the finite triangle
Define the exact tail functional

f_r := sum_{j=r}^m (6(j-r)+1)a_j,  1<=r<=m.

Then, by reversing the finite labelled triangle with no quotient of multiplicity or orientation,

C_m = sum_{r=1}^m y_r f_r.                                      (E1)

For linear-time evaluation the f_r satisfy the exact second-difference relation

BOXED:
f_r-2f_{r+1}+f_{r+2}=a_r+5a_{r+1},

with f_m=a_m and f_{m+1}=0. Thus f can be generated backwards without reconstructing the two-dimensional boundary.

## 2. Finite adjoint accumulator
Set u_0=0 and define, for 1<=r<=m,

BOXED:
2r^2 u_r = f_r + (r+m)(r+2m)u_{r-1}.                    (E2)

All denominators are p-units because r<p. Substitute (E2) into (E1):

C_m=sum_r y_r[2r^2u_r-(r+m)(r+2m)u_{r-1}].

The reflected recurrence shifted by one index is

(r+m)(r+2m)y_r=2(r-1)^2y_{r-1}  (r>=2).

Hence the finite sum telescopes exactly. The lower endpoint vanishes because u_0=0, and the only survivor is

BOXED:
C_m = 2m^2 y_m u_m  (mod p).                             (E3)

This is an all-target finite algebraic identity, not a finite-prime inference.

## 3. Exact terminal normalization
Iterating the reflected recurrence from y_1=1/10 gives

y_m = 2^{m-1}(m-1)!^2 (m+1)!(2m+1) / [10(3m)!].          (E4)

Therefore

2m^2y_m = 2^m(m!)^3 (m+1)(2m+1) / [10(3m)!].

Because p=6m+1=0 in F_p,

(m+1)(2m+1)/10 = (5/6)(2/3)/10 = 1/18.

Also

a_m = binom(2m,m)/2^m,

a_m binom(3m,m) = (3m)!/[2^m(m!)^3].

Since 3m<p, every factorial denominator here is a p-unit. Consequently

BOXED:
2m^2y_m = 1/[18 a_m binom(3m,m)]  (mod p).               (E5)

Combining (E3) and (E5) yields the one-scalar low-branch certificate

BOXED:
C_m = u_m/[18 a_m binom(3m,m)]  (mod p).                 (E6)

No y_r coordinate remains in the observer after the proved endpoint multiplier is retained.

## 4. Sharpened surviving LIFT certificate
Consume the already-proved Clausen box-defect identity

W_p = S_p^2 + 12S_pD_p - 2p^2 C_m  (mod p^3).

Then (E6) gives the exact equivalent form

BOXED:
W_p = S_p^2 + 12S_pD_p
      - p^2 u_m/[9 a_m binom(3m,m)]  (mod p^3).           (E7)

Thus the entire reflected truncation defect has been compressed to one typed scalar u_m generated solely from the low Gauss branch a_j plus an explicit terminal normalization. LIFT is still open: the remaining all-target task is to identify this scalar compensation with the second p-adic digits of S_p,D_p (or to derive an equivalent direct WZ/contiguous endpoint identity).

## 5. BRC information audit
Observer: C_m mod p together with the surviving W_p mod p^3 certificate.
Preserved: low index j/r, low Gauss coefficients a_j, orientation of the original low/high boundary through the exact f_r reindexing, the finite adjoint transport, and the terminal normalization port a_m binom(3m,m).
Safe elimination: the explicit reflected y_r chain disappears only after the finite adjoint telescope and exact endpoint multiplier (E5).
Forbidden elimination: replacing the endpoint multiplier by an unsigned mass, discarding a_m/binom(3m,m), or interpreting this scalar reduction as the final p^3 proof.
BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 6. Independent exact regression
A companion integer-modular checker verifies, for every target prime p<5000 (166 total, 83 in each residue class):
- the backward f_r recurrence against its defining finite tail sum;
- the adjoint telescope C_m=2m^2y_m u_m;
- the terminal normalization 2m^2y_m=[18a_m binom(3m,m)]^{-1};
- equality of the one-scalar certificate with the previously proved original-kernel prefix transform.
Failures: 0. The scan is regression/falsification only; Sections 1--4 carry the all-target proof.

## 7. Narrow next action
Do not reopen the reflected boundary chain. Equate the two exact low-branch descriptions of C_m,

u_m/[18a_m binom(3m,m)]
 = sum_{s=1}^m a_s P_s/(12s^2t_s),

and seek a direct creative-telescoping/contiguous certificate for u_m or the weighted prefixes P_s that matches the second p-adic digits of S_p,D_p. The exact hard target remains W_p congruent p mod p^3 for every p congruent 13 or 19 mod 24.
