# A nonhomogeneous Hesse carrier repairs the second divided digit

Status: PREPARED_PROOF / CANDIDATE_FROZEN / NEW_EXACT_REGRESSION_PENDING.
No own native session/claim/open or new arithmetic execution is asserted here.
The proof is a shared, nonblind synthesis by the current investigator, Root's
direction, and the parameter-jet preparer; the accompanying preparation audit
is bounded and is not final mathematical acceptance. Original frozen preparation
texts, including a separately documented harmless operator-wording erratum,
remain unchanged. Formal identity and execution evidence will be added in a
new final artifact after the authorized run, rather than rewriting this draft.

## 1. The finite arithmetic question and its answer

Let p=6m+1≥7 be prime, with

    a_n=(1/6)_n(1/3)_n/(n!)²,
    b_n=(1/3)_n(2/3)_n/(n!)²,
    f_p(w)=sum[n=0..p-1]a_nw^n,
    L_p(x)=sum[n=0..p-1]b_nx^n,
    q(x)=4x(1-x).

Unit16 proves f_p(q)=L_p modulo p² coefficientwise and demonstrates that
the same uncorrected polynomial comparison fails modulo p³. This draft
identifies the lost digit by a universal nonhomogeneous Hesse equation.

Define I_p(x)=sum[j=0..p-2]i_jx^j over F_p by the INDEPENDENT recurrence

    i_0=0,
    (j+1)²i_(j+1)=(j+1/3)(j+2/3)i_j-2/9,
    0≤j≤p-3.                                                (I)

No coefficient of I_p reads a finite Gauss or Hesse value. Every denominator
is a unit, including at numerator-factor entries j=2m,4m. At the exact
x_±=(2±s)/4, s²=2, and the inherited target classes p mod24 in {13,19},
the claim is

    g_p/p = L_p(x_±)/p + p*σ(x_±)*I_p(x_±) modulo p²,       (CM3)

where g_p=f_p(1/2), σ(s)=-s, and only the correction factor is evaluated
over F_p. The first term uses the exact algebraic lift through p³. CM0
divisibility is inherited from the existing chain, not reproved here.

The full polynomial comparison uses one independently computed boundary
scalar B_p, defined in section 4, and

    H_p(x)=L_p(x) modulo p,
    J_p(x)=I_p(x)+B_p H_p(x),
    f_p(q(x))=L_p(x)+p²x^pJ_p(x) modulo p³.                  (POLY3)

The scalar is required for polynomial and derivative observers. It disappears
from the CM value observer by H_p(x_±)=0. This is the concrete simplification:
the corrected target value requires only the fixed zero-seed recurrence (I),
not a boundary beta sum, parameter jet, period scale or fitted constant.

## 2. Exact finite cutoff residuals and universal forcing

Use D_G=w(1-w)∂²+(1-3w/2)∂-1/18 and
D_H=x(1-x)∂²+(1-2x)∂-2/9. The characteristic-zero quadratic identity,
already proved in unit16 by ODE uniqueness, has operator relation

    D_H(F∘q)=4(D_G F)∘q.

The finite coefficient recurrences imply the exact residual identities

    D_G f_p=-(p-5/6)(p-2/3)a_(p-1) w^(p-1),
    D_H L_p=-(p-2/3)(p-1/3)b_(p-1) x^(p-1).                (R)

There is no infinite-tail integrality assertion in (R): each expression is
an exact finite polynomial calculation. Unit16's valuation cutoffs give
v_p(a_(p-1))=v_p(b_(p-1))=2. For n>2m, removing the factors p/6 and p/3
gives the explicit residue

    a_n/p²=(-1)^(3m) m!(2m)!(n-1-m)!(n-1-2m)!
             /[18(n!)²] modulo p.                          (A)

For n>4m, removing p/3 and 2p/3 gives

    b_n/p²=2(2m)!(4m)!(n-1-2m)!(n-1-4m)!
             /[9(n!)²] modulo p.                          (B)

All factorial arguments are <p. Wilson's theorem at n=p-1, retaining the
sign in (A), yields

    a_(p-1)/p²=1/10,  b_(p-1)/p²=1 modulo p.               (W)

Explicitly m!(5m-1)!=(-1)^m*6/5,
(2m)!(4m-1)!=3/2, and (4m)!(2m-1)!=3. The factor (-1)^(3m)
in (A) cancels the first Wilson sign. Thus the two divided residual constants
in (R) are 1/18 and 2/9, respectively. Denominator 10 is a unit, since p≥7.

For proof purposes alone set E=(f_p(q)-L_p)/p² modulo p. Unit16 makes this
integral. More precisely its characteristic-zero identity shows all finite
coefficients of degree <p are EXACTLY equal over Q, so E=x^p K with
deg K≤p-2. Using (R), (W), and 4^(p-1)=1 modulo p gives

    D_H E=(2/9)x^(p-1)[1-(1-x)^(p-1)].

Over F_p, ∂x^p=0, so D_H(x^pK)=x^pD_HK. Also
(1-x)^(p-1)=sum[r=0..p-1]x^r modulo p. Therefore

    D_H K=-(2/9)sum[j=0..p-2]x^j.                          (FORCE)

The apparent division by x cancels exactly in the polynomial numerator.
This forcing is universal, independent of a CM point or the sought digit.
It is a structural identification of the finite truncation defect, not merely
a new name for an evaluated difference quotient.

## 3. Homogeneous ambiguity, its value cancellation, and derivative boundary

The coefficients of a polynomial solution of (FORCE) satisfy (I), with its
initial coefficient free. The first p-2 recurrence denominators (j+1)² are
units, so fixing the initial value determines every coefficient through p-2.
There is an additional terminal equation at degree p-2; the actual K and
the homogeneous H_p satisfy it. It is not a second free coefficient.

The homogeneous normalized solution is precisely

    H_p=sum[n=0..2m](b_n modulo p)x^n,
    H_p(0)=1.

The numerator factor at j=2m kills its next coefficient; the second factor
entry at j=4m creates no new freedom. The unit denominator at both entries
is essential. It follows that K=I_p+K(0)H_p as full polynomials over F_p.
Once the independent scalar B_p=K(0) is proved in section 4, (POLY3) follows.

For the exact branches q(x_±)=1/2 in O=Z_(p)[s]/(s²-2), the algebra is
finite étale since p∤8. Unit16 yields H_p(x_±)=g_p modulo p. Inherited CM0
on the two target classes makes this zero. Consequently K(x_±)=I_p(x_±)
without evaluating K(0). Evaluating (POLY3) at the exact lift and dividing
by p gives

    g_p/p=L_p(x_±)/p+p*x_±^p I_p(x_±) modulo p².

Only x_±^p modulo p is needed in the correction; because 2 is a nonsquare
on the target classes it equals σ(x_±) modulo p. This proves (CM3). It does
not replace the exact x_± in the first term by a residue point, Teichmüller
representative or literal p-power lift.

The complete polynomial correction has differentiated observer

    q'(x_±)f'_p(1/2)=L'_p(x_±)+p²x_±^pJ'_p(x_±) modulo p³. (DER3)

Differentiating x^p contributes p³ and vanishes at this precision. Replacing
J by I in (DER3) omits B_pH'_p. Inherited SIMPLE makes H'_p(x_±) a unit;
when B_p≠0, this omission changes the derivative. Thus the boundary scalar
may be dropped only for the CM value observer at the declared precision.
It remains part of the complete state for future derivative/period operations.
This observer-specific cancellation never identifies source a_i or an
unpowered raw period with a coordinate derivative.

## 4. An explicit harmonic boundary for the uniform polynomial

Define q_2=(2^(p-1)-1)/p and, for 0≤k<m,

    S_2=sum 1/(6k+2),
    T_r=sum 1/(6k+r)², r=2,3,6,
    B_p=(2/9)[(-3S_2-q_2)/p+q_2²/2
                   -3T_6+12T_3+(33/2)T_2] modulo p.         (HB)

The first division is legitimate, as shown below. S_2 and q_2 require
precision p²; all T_r require only precision p. Their denominators lie
between 2 and p-1. This independent definition reads no Task value.

Let a_p,b_p be the index-p coefficients of the infinite characteristic-zero
series, used only for boundary extraction. The full quadratic identity gives

    [x^p](f_p(q)-L_p)=b_p-4^p a_p.                          (BOUND)

Both index-p coefficients are p-units after EXACT cancellation of the two
numerator p factors against (p!)². By adjacent coefficient ratios and (W),
a_p=1/18, b_p=4^p a_p=2/9 modulo p. Their exact unit ratio is

    R=b_p/(4^p a_p)
      =2^(1-p) product[j=0..p-1,j≠4m](3j+2)
                   /product[j=0..p-1,j≠m](6j+1).

Every numerator/denominator unit is uniquely r+pκ_B(r) or r+pκ_A(r),
for r=1,...,p-1, with κ_B(r)=(2-r) mod3 in {0,1,2} and
κ_A(r)=(1-r) mod6 in {0,...,5}. These are actual factors, not a
congruence substituted beyond its precision. Put

    V_1=sum(κ_B-κ_A)/r,
    V_2=sum(κ_B²-κ_A²)/r².

The integral product expansion through p³ is

    R=1+p(V_1-q_2)
      +p²[(V_1²-V_2)/2-q_2V_1+q_2²] modulo p³.

Unit16 and (BOUND) imply R-1 is divisible by p², hence V_1-q_2 is
divisible by p. Pair r with p-r using representatives r=6k+2,6k+3,6k+6.
The six carry differences in residues 1,2,3,4,5,0 are
1,-5,-2,-2,-2,1; their square differences are 1,-25,-12,-8,-4,3.
Since 1/(p-r)=-1/r-p/r² modulo p², pairing gives

    V_1=-3S_2+p[-T_6+2T_3+2T_2] modulo p²,
    V_2=4T_6-20T_3-29T_2 modulo p.

In particular -3S_2-q_2 is divisible by p. Substitution, and multiplication
by the unit 4^p a_p=2/9, give exactly

    (b_p-4^p a_p)/p²=B_p modulo p.

By (BOUND) this is K(0). It proves (HB) and completes the uniform (POLY3).
The supplementary terminating parameter family
A(t)=1/6-t/6, B(t)=1/3+t/6, C(t)=1/3-t/3, D(t)=2/3+t/3
explains the corresponding integral jets. At t=p the two sides terminate
exactly; that independent preparation is retained, but no jet computation
is required for (CM3).

## 5. Evidence, scope and next consumption

The author candidate definitions and checker were frozen before new execution.
The planned six-prime regression checks full coefficients, harmonic versus
factorial boundary, both factor entries and terminal equation, exact two
branches, target second digits, derivative transport, and the old omitted-
correction negative. Zero-seed polynomial/derivative failures are separate
negative checks of scope. The theorem proof is the algebra above, not the
finite passes. A decisive nonauthor review of the final exact bytes is pending.

The correction is computable with O(p) field operations. No improved
asymptotic complexity is claimed. The information gain is the universal
forcing and the removal of one independently unknown boundary coordinate
from the CM value observer, while retaining that coordinate for derivatives.
The CM correction can now be consumed in a later structural LIFT comparison
without needing a raw modular-period calibration first.

Reuse unchanged Source integer precision projection/detail/recomposition
functions for canonical residue division. New arithmetic code is a task-local
checker, not a new general toolbox family or a method-novelty claim. Preserve
the unit16 exact proof/checker evidence and all earlier completed units.

The declared object population is the complete finite coefficients, cutoff
layers, exact lifts, conjugation, signed values, derivatives and coordinate
Jacobians, plus inherited h/omega^r full-level marks. Allowed observers here
are finite polynomial evaluation/differentiation, reduction and canonical
division at stated precisions. The seed cancellation certificate covers only
the target divided value through p²; derivatives and other points retain
the full boundary. Heartbeat World native X6/time and joint-preservation
remain unchanged. These are external arithmetic readouts, with no newly
claimed native embedding or full-X6 propagation.

UR, the parent LIFT certificate, independent raw period normalization,
external duplication/novelty status, Working Truth and Foundation remain
unchanged and unproved by this Task. No provider query, old 77-prime replay,
new arbitrary root choice or mathematical parent closure follows.
