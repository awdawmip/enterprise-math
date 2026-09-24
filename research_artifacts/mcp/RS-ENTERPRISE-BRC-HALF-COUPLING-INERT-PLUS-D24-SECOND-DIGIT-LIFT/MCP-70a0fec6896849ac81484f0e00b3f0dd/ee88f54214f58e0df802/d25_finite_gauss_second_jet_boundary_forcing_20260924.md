# D25 LIFT — finite Gauss second-jet boundary forcing is one universal terminal source

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier

Consume the accepted D24 UR/JT0 parent, the current D25 global parameter-jet/tail-chain checkpoints, and the source-pinned finite Jacobi-jet interface. A later noncanonical Driver intake observed that the entire valuation stratification can be embedded in the finite Gauss deformation. This unit rederives the needed two-variable finite identity under the live Researcher authority and proves a new endpoint fact: the finite hypergeometric differential equation has no truncation forcing at parameter orders 0 or 1, while its order-2 forcing is a single k=p-1 terminal source whose residue at z=1/2 is universally -2 modulo p.

No Driver evidence is promoted merely by citation.

## 1. Exact finite Gauss deformation

Let p=6m+1 and N=6m=p-1. Define

    F(a,z) = sum_{k=0}^N c_k(a) z^k,
    c_k(a) = (-m+a)_k (-2m+2a)_k / (k!)^2,
    H(a,z) = (1+12 theta)F(a,z),
    theta = z d/dz.

At a=p/6 and z=1/2,

    F(p/6,1/2)=g,
    H(p/6,1/2)=h,

because -m+p/6=1/6 and -2m+p/3=1/3. Thus this is an exact deformation of the live weighted source, not a fitted auxiliary family.

Put

    L_a = theta^2 - z (theta-m+a)(theta-2m+2a).

The coefficient recurrence for c_k(a) gives the exact finite identity

    BOXED:
    L_a F(a,z)
      = -(5m+a)(4m+2a)c_N(a) z^p.                 (1)

All interior coefficients cancel. Hence every failure of the infinite Gauss differential equation for the finite p-term carrier is concentrated at the single terminal port k=N=p-1.

## 2. The terminal port has deformation order exactly two

At a=0, the first Pochhammer has exactly one zero factor, at j=m, and the second has exactly one zero factor, at j=2m. Therefore

    c_N(0)=0,
    c_N'(0)=0,

while

    BOXED:
    c_N''(0)
      = 4(-1)^m m!(2m)!(4m-1)!(5m-1)!/(6m)!^2.   (2)

So the finite truncation boundary is invisible to the order-0 and order-1 parameter observers and first appears at order 2. This is the differential-equation version of the residual-faithful valuation jump: the boundary is not discarded, but its exact deformation order is now proved.

Let F_r(z)=partial_a^r F(a,z)|_{a=0}, and L_0=theta^2-z(theta-m)(theta-2m). Since

    partial_a L_a|_0 = -z(3theta-4m),
    partial_a^2 L_a|_0 = -4z,

differentiating (1) yields

    BOXED:
    L_0 F_0 = 0,                                          (3)
    L_0 F_1 = z(3theta-4m)F_0,                            (4)
    L_0 F_2 = 2z(3theta-4m)F_1 + 4zF_0 + B_m(z),          (5)

where the entire boundary forcing is

    BOXED:
    B_m(z)
      = -80(-1)^m m^2 m!(2m)!(4m-1)!(5m-1)!/(6m)!^2 * z^p.   (6)

Equations (3)-(6) are exact rational finite-polynomial identities.

## 3. Universal terminal residue at the D25 observation point

Now reduce at z=1/2 modulo p. Wilson complement gives

    (4m-1)! == 1/(2m+1)!            (mod p),
    (5m-1)! == (-1)^m/(m+1)!        (mod p),
    (6m)!^2 == 1                     (mod p).

Therefore, using 2^{-p}==1/2 (mod p),

    B_m(1/2)
      == -40 m^2/[(2m+1)(m+1)]
      == -2                              (mod p),

because m==-1/6, 2m+1==2/3 and m+1==5/6 modulo p. Hence

    BOXED:
    B_m(1/2) == -2 (mod p)                         (7)

for every prime p=6m+1, in particular both target classes p==13,19 (mod 24). The residue does not depend on the target residue class.

Consume the already-proved CM0 input F_0(1/2)==0 (mod p). Then (5) gives the sharpened second-jet equation

    BOXED:
    [L_0F_2]_{z=1/2}
      == [(3theta-4m)F_1]_{z=1/2} - 2               (mod p).   (8)

If H_1=(1+12theta)F_1, then equivalently

    BOXED:
    [L_0F_2]_{1/2}
      == H_1(1/2)/4 + 5F_1(1/2)/12 - 2              (mod p).   (9)

This is not yet LIFT, because L_0F_2 at one point still contains the z-derivative state of F_2. It is, however, a strict source reduction: the non-homogeneous truncation defect at the complete second parameter jet is one explicit terminal scalar, and that scalar is the constant -2 modulo p.

## 4. Exact bridge back to the frozen parent Jacobi-jet coordinates

Let the frozen parent family be

    Phi_m(x,z)=sum_{k=0}^{6m} (-x)_k(-2x)_k z^k/(k!)^2,
    Psi_m=(1+12theta)Phi_m.

Because F(a,z)=Phi_m(m-a,z) exactly, at z=1/2 we have

    F_0=Phi,
    F_1=-Phi_x,
    F_2=Phi_xx,
    H_0=Psi,
    H_1=-Psi_x.

Thus the full finite-Gauss deformation does not introduce a new unnamed bridge coordinate. If

    A_p := F_0/p + F_1/6,

then exactly

    BOXED: A_p = Phi/p - Phi_x/6 = a_parent.          (10)

Consequently its first-neglected product coordinate is exactly

    BOXED:
    Phi_p^prod := [A_p H_0-1]/p
                 = [a_parent Psi-1]/p.                 (11)

The full-jet product formula therefore becomes

    Delta_p
      == [a_parent Psi-1]/p
         - a_parent Psi_x/6
         + Phi_xx Psi/72                              (mod p),   (12)

which is precisely the second-digit expansion of the frozen parent scalar

    (a_parent+p Phi_xx/72)(Psi-p Psi_x/6).

This proves the requested source-backed identification rather than identifying two similarly named objects by notation. It also shows where the genuinely new information lies: not in another alpha/beta bridge, but in controlling the second-jet transport subject to the universal terminal forcing (7).

Using UR and SIMPLE, write q=Q_m'(1/2), so Psi==-6q and a_parent==-1/(6q) modulo p. Then (12) has the normalized tangent form

    Delta_p
      == [a_parent Psi-1]/p
         + Psi_x/(36q) - Phi_xx q/12                  (mod p).   (13)

The LIFT residue is obtained by subtracting the frozen R_p.

## 5. BRC information audit

Population: all source ports k=0,...,p-1 of the finite Gauss deformation, with parameter derivative order retained.

Observer: the D25 second digit modulo p after the accepted first digit.

Preserved provenance: k=p-1 terminal port; the two zero factors j=m and j=2m; parameter derivative order; z=1/2 evaluation; target residue label; parent Phi/Psi coordinates.

Safe compression: under the differential-equation-defect observer, all interior source ports telescope by the coefficient recurrence and the complete non-homogeneous order-2 truncation source is B_m(1/2)=-2.

Forbidden compression: deleting the terminal port because F_0 and F_1 see no boundary, or replacing the order-2 boundary by an unsigned mass. The fact that the first two deformation orders are homogeneous is exactly why the terminal source must remain tagged at JT2.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 6. Deterministic falsification

The companion checker evaluates the closed factorial expression (6) for every target prime p<5000 and verifies B_m(1/2)==-2 modulo p. It also verifies the two simple zeros and the closed c_N'' formula against an independent jet recurrence for the terminal Pochhammer products. Finite checking is regression/falsification only; Sections 1-4 are the proof.

## 7. Narrow next action

LIFT remains open. Do not rebuild the old shell decomposition and do not search for a separate bridge for Phi_p^prod: equations (10)-(12) identify it exactly with the frozen parent first-neglected product coordinate. The next information-gain step is to pair the forced second-jet equation (8)/(9) with an adjoint/contiguous functional at z=1/2 that eliminates the extra z-derivative state of F_2 while retaining the terminal source -2. If that succeeds, compare the resulting one-scalar endpoint with R_p; otherwise preserve the exact remaining adjoint defect.
