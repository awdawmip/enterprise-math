# D25 LIFT — a finite discrete adjoint removes the second-jet z-state while preserving the terminal -2 source

Status: PROVED_STRICT_REDUCTION_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier

Consume the durable D24 UR/JT0 Result, the D25 first-digit-fiber/tangent-torus checkpoint, and the finite-Gauss second-jet boundary-forcing checkpoint. The last of these proves that for p=6m+1, N=p-1=6m,

    F(a,z)=sum_{k=0}^N c_k(a) z^k,
    c_k(a)=(-m+a)_k(-2m+2a)_k/(k!)^2,

with F_r(z)=partial_a^r F(a,z)|_{a=0} and

    L_0 = theta^2-z(theta-m)(theta-2m),

satisfies

    L_0 F_2
      = 2z(3theta-4m)F_1 + 4zF_0 + B_m(z),

where the entire finite-boundary term is supported at z^p and

    B_m(1/2) == -2 (mod p).

The live obstruction was that L_0F_2 at z=1/2 still contains the z-derivative state of F_2. This unit constructs an exact finite Green/adjoint functional that evaluates F_2(1/2) directly from the lower parameter jets F_0,F_1 and the labelled terminal boundary port.

## 1. Coefficient form of the finite operator

Put

    b_k=(k-m)(k-2m).

For any polynomial

    y(z)=sum_{k=0}^{N} y_k z^k

of degree at most N=p-1, let f=L_0 y. Then for 1<=k<=N,

    f_k := [z^k]f
         = k^2 y_k - b_{k-1} y_{k-1},

and because y_p=0 the terminal coefficient is

    f_p := [z^p]f = -b_N y_N.

For the application y=F_2 we have y_0=0.

## 2. Exact backward adjoint weights

Define rational weights lambda_k backwards by

    lambda_p = 2^{-p},

and, for k=N,N-1,...,1,

    BOXED:
    lambda_k
      = (2^{-k}+b_k lambda_{k+1})/k^2.                 (A1)

Since 1<=k<=p-1, every denominator k^2 is a p-adic unit. Hence all lambda_k are p-integral and may be reduced modulo p without ambiguity.

The recurrence is the finite adjoint equation for evaluation at z=1/2:

    BOXED:
    k^2 lambda_k - b_k lambda_{k+1} = 2^{-k}.         (A2)

## 3. Exact discrete Green identity

Assume y_0=0. Then

    sum_{k=1}^{p} lambda_k f_k

equals

    sum_{k=1}^{N} lambda_k k^2 y_k
      - sum_{k=1}^{N} lambda_k b_{k-1} y_{k-1}
      - lambda_p b_N y_N.

Shift the second sum by j=k-1. The coefficient of every y_k, 1<=k<=N, is

    k^2 lambda_k-b_k lambda_{k+1}=2^{-k},

while the y_0 term vanishes because y_0=0. Therefore the identity is exact over Q:

    BOXED:
    y(1/2)=sum_{k=1}^{p} lambda_k [z^k](L_0y).        (A3)

This is a finite telescoping identity, not an asymptotic approximation and not a numerical inversion.

## 4. Apply the adjoint to the complete second parameter jet

Write

    c_j=[z^j]F_0,
    d_j=[z^j]F_1,
    e_j=[z^j]F_2.

For 1<=k<=N, the exact second-jet differential equation gives

    [z^k]L_0F_2
      = 2(3(k-1)-4m)d_{k-1}+4c_{k-1}.                (A4)

The k=p coefficient is exactly the labelled terminal coefficient of B_m(z). Using lambda_p=2^{-p}, its contribution to (A3) is exactly

    lambda_p [z^p]B_m(z)=B_m(1/2),

hence modulo p it is -2.

There is also an exact support reduction at a=0:

- c_j=0 for j>m, because (-m)_j contains its zero factor;
- d_j=0 for j>2m, because after both Pochhammer zero factors have appeared the first parameter derivative of their product also vanishes.

Thus only j<=2m can contribute to the interior adjoint source. Define

    BOXED:
    S_m :=
      sum_{j=0}^{2m} lambda_{j+1}
        [2(3j-4m)d_j+4c_j]             (mod p).       (A5)

Equations (A3)-(A5) and the proved terminal boundary residue give

    BOXED:
    F_2(1/2) == S_m-2                 (mod p).         (A6)

This eliminates the complete order-2 parameter jet from the live observer. The replacement uses only order-0/order-1 source coefficients, deterministic adjoint weights, and the terminal boundary provenance.

## 5. Exact reduction of the frozen LIFT scalar

The finite-Gauss bridge already identifies

    F_0=Phi,
    F_1=-Phi_x,
    F_2=Phi_xx,
    H_0=Psi,
    H_1=-Psi_x,

at z=1/2, and with q=Q'_m(1/2),

    Delta_p
      == [a_parent Psi-1]/p
         + Psi_x/(36q)
         - Phi_xx q/12                  (mod p).

Substituting (A6) gives the lower-derivative certificate

    BOXED:
    Delta_p
      == [a_parent Psi-1]/p
         + Psi_x/(36q)
         - q(S_m-2)/12                  (mod p).       (A7)

Therefore, under the already-frozen UR/SIMPLE inputs,

    BOXED:
    LIFT
    <=>
    [a_parent Psi-1]/p
      + Psi_x/(36q)
      - q(S_m-2)/12
      - R_p
      == 0                              (mod p).       (A8)

This is a strict reduction in derivative complexity: Phi_xx/F_2 and its z-derivative state are gone. No new bridge object is introduced; S_m is an explicit finite functional of the existing F_0/F_1 source jets.

It is not yet a proof of LIFT, because the remaining first-jet scalar (A8) has not yet been shown to vanish uniformly.

## 6. BRC information audit

Population: all finite Gauss ports k=0,...,p together with parameter-derivative order and the terminal truncation port.

Observer: the divided second p-adic digit Delta_p modulo p after the accepted UR first digit.

Preserved state: the coefficient labels j; c_j and d_j separately; the adjoint weight lambda_{j+1}; target prime/residue provenance; and the terminal k=p source. The terminal source is not folded into an unsigned mass.

Safe compression: (A3) proves that, for the evaluation observer y -> y(1/2) on y_0=0, the full second-jet coefficient vector factors exactly through the labelled forcing coefficients of L_0 and the adjoint weights. Equations (A4)-(A6) then factor it further through F_0,F_1 plus the exact terminal boundary source.

Forbidden compression: dropping the k=p terminal term; replacing S_m by an unlabelled total; or treating the p<5000 regression as an all-prime proof. The -2 term is a signed, provenance-bearing source and must remain explicit.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 7. Deterministic falsification/regression

The companion checker independently constructs c_j,d_j,e_j modulo p from the differentiated coefficient recurrence, reconstructs every coefficient of L_0F_2, constructs the backward adjoint weights from (A1), and verifies:

1. every interior coefficient agrees with (A4);
2. the exact finite adjoint identity (A3) evaluates F_2(1/2);
3. the terminal adjoint contribution is -2 modulo p;
4. F_2(1/2)=S_m-2 modulo p.

For every target prime p<5000 with p mod 24 in {13,19}, the checker returns zero failures (166 primes total). This scan is falsification/regression only; the proof is Sections 1-6.

## 8. Narrow next action

Do not reconstruct Phi_xx directly again. The live scalar is now (A8). The next information-gain step is to simplify the explicit first-jet adjoint sum S_m against the already-frozen q, Psi_x and first-neglected product coordinate, ideally by composing (A1) with the first-jet equation

    L_0F_1=z(3theta-4m)F_0.

If the resulting finite summation-by-parts identity collapses (A8) to zero, LIFT closes uniformly. If a nonzero exact endpoint term survives, persist that term as the new smallest certificate.
