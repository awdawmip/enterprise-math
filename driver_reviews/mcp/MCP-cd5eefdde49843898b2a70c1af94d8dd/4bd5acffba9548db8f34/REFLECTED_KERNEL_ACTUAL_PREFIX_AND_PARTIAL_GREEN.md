# Independent reflected reciprocal kernel and actual prefix/CM source

Status: ONE FOCUSED LOCAL ALGEBRA UNIT / FINITE REFLECTION, ACTUAL CUTOFF
AND PARTIAL GREEN LEMMAS PROVED / ORIGINAL SCALAR COMPARISON OPEN.
Prepared 2026-10-12 UTC. Only this independent-check directory is written.
No prime, scalar fit, old-checker execution, Source write or native
operational completion occurs. The old reciprocal CM sum exchange and
boundary reduction are consumed as proved inputs. Their old rational
ansatz obstruction is not repeated or re-searched.

## 1. The literal finite reciprocal normalization

Retain p=6m+1 in the frozen classes, N=3m, and exactly
h_0=h_N=g=binom(3m,m), sum h=1. Here g is the unit V(1), not the different
p-adic memo's scalar f_p(1/2). Define the fixed coefficients

    a_i=(1/6)_i(1/3)_i/[(1/2)_i i!],
    t_r=2^(-r)(1/2)_r/r!,
    D_r=2^(r-1)(r-1)!^2/[18(2/3)_r(5/6)_r],
    H_r=rD_r t_r=(1/2)_r(r-1)!/[36(2/3)_r(5/6)_r], 1<=r<=N.

The identical D formula through N is the already proved integral
extension used by the fixed C constructor. It does not enlarge the
OLD-R observer's original cutoff r<=m. Every displayed H_r,D_r,t_r is
a unit: their factorial/Pochhammer factors avoid p on the stated range.
Their actual ratio and first endpoint are

    H_(r+1)/H_r=r(r+1/2)/[(r+2/3)(r+5/6)], 1<=r<N,
    H_1=1/40.                                             (1)

Set the fixed connected homogeneous coefficients

    e_j=(2/3)_j(5/6)_j/[(3/2)_j j!], 0<=j<N.

There is no e_N: its denominator first vanishes there.
The finite reflected sequence H_(N-j)/H_N has ratio

    H_(N-j-1)/H_(N-j)
           =(j+2/3)(j+5/6)/[(j+1)(j+3/2)], 0<=j<=N-2.

This follows from (1) and N=-1/2 as a coefficient reduction; all actual
indices remain in 1,...,N. The initial value is 1, so unit-divisor
propagation proves the finite normalization and its last endpoint:

    BOX: H_(N-j)=H_N e_j, 0<=j<N,
         H_N e_(N-1)=H_1=1/40,
         D_r=H_N e_(N-r)/(r t_r), 1<=r<=N.                (2)

H_N is the literal product above, not a scalar chosen from a target.
This is a finite-field reflection statement, not a characteristic-zero
termination substitution.

## 2. The actual fixed-C coefficient dictionary and all boundaries

Consume the connected inverse for the independently fixed Cbar(z)=C(1-z).
Its summand is
(r-1)!(3/2)_(r-1)/[9(2/3)_r(5/6)_r]=8H_r. Therefore

    BOX: cbar_j=-8e_j sum_(r=j+1)^N H_r
              =-8H_N e_j sum_(s=0)^(N-j-1)e_s, 0<=j<N.  (3)

At j=N-1 this uses only H_N,e_(N-1),e_0 and gives
cbar_(N-1)=-8H_1=-1/5, exactly the genuine top reverse row. The separate
cbar_N=0 convention uses no e_N. All lower and upper coefficient
endpoints are explicit.

Let E_(r-1)(z)=sum_(j=0)^(r-1)e_j z^j, 1<=r<=N. Swapping the finite
sums in (3), without adding any new observer, gives

    Cbar(z)=-8sum_(r=1)^N H_r E_(r-1)(z),
    C_*=C(1/2)=-8H_N sum_(r=1)^N e_(N-r)E_(r-1)(1/2).    (4)

The same value is the quadratic triangle
-8H_N sum_(j=0)^(N-1)e_j2^(-j)sum_(s=0)^(N-j-1)e_s.
Thus the whole carrier keeps its complete finite coefficient triangle.

## 3. The unchanged M_R has an exact reflected cutoff

Keep the original OLD-R triangle and the genuine previous residual:

    Htri_k=sum_(r=1)^k[1+6(k-r)]D_r,
    W_k=t_k Htri_k, W_0=0,
    Z_k=W_k-W_(k-1), 1<=k<=m,
    S_k=sum_(i=0)^k a_i,
    M_R=sum_(k=1)^m S_(k-1)Z_k,
    sum_(i=0)^m a_i=1/g.

The fixed identity a_i t_i=2^(-i)v_i, with
v_i=(1/6)_i(1/3)_i/(i!)^2, preserves the literal old constructor
OLD-R=2sum_(i=1)^m a_i W_i. No OLD-R value is assigned from the residual.

Finite prefix summation by parts gives

    M_R=W_m/g-sum_(i=1)^m a_i W_i.

This is used only to expose the actual summand weights; it is not claimed
as a new scalar evaluation. Define independently from these same terms

    Q_r=(t_m/g)[1+6(m-r)]
                    -sum_(i=r)^m a_i t_i[1+6(i-r)], 1<=r<=m.

Direct finite expansion then proves the new reflected prefix dictionary

    BOX: M_R=sum_(r=1)^m D_r Q_r
       =H_N sum_(s=2m)^(N-1)
                    e_s Q_(N-s)/[(N-s)t_(N-s)].          (5)

The cutoff is literal: r=m maps to s=2m and r=1 maps to s=N-1.
At the last original r=m, Q_m=t_m(1/g-a_m)=t_m S_(m-1), retaining
the actual last Z diagonal. Every r t_r divisor is a unit. There is no
terminal Z_(m+1), r=0 or e_N term.

By contrast, the full C sum (4) uses r=1,...,N. Its complementary
r=m+1,...,N range maps exactly to s=0,...,2m-1. It cannot be removed
merely because OLD-R stops at m.

## 4. Two new partial Green resolvents with their actual endpoint choices

For the original coordinate put
K_(r-1)(w)=sum_(j=0)^(r-1)d_j w^j, with the fixed
d_j=(2/3)_j(5/6)_j/(j!)^2. Its truncated adjoint source is

    D_G*(D_r K_(r-1))=-2^(r-1)w^(r-1)/18.                 (6)

All lower rows cancel by the d ratio. The source coefficient follows
from D_r (r-1+2/3)(r-1+5/6)d_(r-1)=2^(r-1)/18, including r=N.
The original Gauss concomitant vanishes at w=0 and at CM0 equals
D_r K_(r-1)(1/2)V'(1/2)/4. Its degree is at most m+r<=4m<p, so its
zero-at-zero primitive is unique and all denominators i+r are units.
Integrating the exact source therefore proves the individual resolvent

    BOX: D_r K_(r-1)(1/2)V'(1/2)
               =(1/9)sum_(i=0)^m v_i2^(-i)/(i+r), 1<=r<=N. (7)

For the connected coordinate, use the actual E_(r-1) from (4). Direct
finite coefficient calculation, with no e_r at the top, gives

    (r-1+2/3)(r-1+5/6)e_(r-1)=1/(72H_r),
    D_A*(H_r E_(r-1))=-z^(r-1)/72.                       (8)

The first formula follows from
(3/2)_(r-1)=2(1/2)_r and is legal even at r=N; it never introduces the
undefined e_N. The connected concomitant vanishes at z=1, and its CM
value is H_r E_(r-1)(1/2)A'(1/2)/4. Integrating from 1/2 to 1, with
the same degree bound m+r<p, gives the distinct endpoint resolvent

    BOX: H_r E_(r-1)(1/2)A'(1/2)
         =-(1/18)sum_(i=0)^m a_i[1-2^(-(i+r))]/(i+r),
                                                        1<=r<=N. (9)

The minus sign comes from the upper normalization at 1. In both (7)
and (9), r=1 and r=N are actual legal truncations, and no derivative
or C value is inverted. Full summation is consistent with the already
proved old/connected tau dictionary; that full dictionary is not
reclaimed as a new result.

## 5. A genuine common-kernel comparison retaining the complementary tail

Use the original fixed CM boundary tau=-C_*V'(1/2)/4 and (4). It gives

    tau=2H_N V'(1/2)sum_(r=1)^N e_(N-r)E_(r-1)(1/2).

Combine this actual boundary with the unchanged M_R in (5), and define
the independently determined complete source

    T_kernel=sum_(r=1)^m e_(N-r)
                  [Q_r/(r t_r)-6V'(1/2)E_(r-1)(1/2)]
           -6V'(1/2)sum_(r=m+1)^N e_(N-r)E_(r-1)(1/2).

Then the genuine simultaneous source identity is

    BOX: M_R-3tau=H_N T_kernel.                           (10)

Its signs and factor 6 come from the original -C_*V'/4 boundary, not
from selecting a discrepancy. Both the original r<=m cutoff and the
complement r>m are explicit. Formula (9) can contract each CM term
individually: since V'=-gA', it equals the independent resolvent
(g/3)sum_i a_i[1-2^(-(i+r))]/(i+r) after the factor 6H_Ne_(N-r).
That operation retains the complete r range and takes no C inverse.

Thus the preceding exact comparison has the successor formulation

    g(B_H+B_O)+2H_N T_kernel=kappa+T_m+2W_m/g.             (OPEN) (11)

Here B_H,B_O,T_m,kappa and W_m retain their previous independent
constructors. In particular the known odd-moment 16^m term, the cubic
x^p tail and the finite-log complement remain in their own preserved
dictionaries. Equation (11) is an exact reformulation, not a proof of
zero, and no independent nonzero scalar residual is established.

## 6. Independent checking and scope

The new checker passed 38 exact checks: literal D/t/H product and
reflection ratio; first/top normalizations; actual connected inverse
weight; both partial-adjoint source coefficients; their CM integral
scales; generic finite-array verification of the genuine M_R/Q_r
coefficient swap; reflected C coefficient triangles and CM sum exchange;
cutoff endpoints; and common-source signs. These are rational coefficient
and abstract finite-array checks, with zero prime instances and no old
checker reuse. The finite proofs above supply all modular unit ranges.

This unit proves a shared finite reflected kernel for the actual old
prefix source and the fixed C boundary, plus legal partial Green
contractions. It does not evaluate their remaining coupled source,
enlarge the previously ruled-out rational ansatz, or promote the scalar
comparison, LIFT, weighted p^3, period normalization or full native X6.
All parent objectives remain OPEN.
