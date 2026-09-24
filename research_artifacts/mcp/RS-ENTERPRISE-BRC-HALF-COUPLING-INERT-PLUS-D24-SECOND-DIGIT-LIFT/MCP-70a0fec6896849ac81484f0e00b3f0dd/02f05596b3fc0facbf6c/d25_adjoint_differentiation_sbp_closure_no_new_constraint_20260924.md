# D25 LIFT — differentiating the finite adjoint closes the requested first-jet summation by parts but yields no new constraint

Status: PROVED_STRICT_NO_NEW_CONSTRAINT_UNIT / LIFT_NOT_YET_CLOSED / NOT_A_RESULT / UNREVIEWED
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
Publication: TP2-B6F4FC938FF94941C1B7
Date: 2026-09-24

## 0. Consumed frontier

Consume the durable finite-Gauss boundary checkpoint and the newly durable finite discrete-adjoint checkpoint. In the latter, for p=6m+1, N=p-1,

    b_j=(j-m)(j-2m),

    k^2 lambda_k-b_k lambda_{k+1}=2^{-k},
    lambda_p=2^{-p},

and, writing c_j=[z^j]F_0 and d_j=[z^j]F_1,

    S_m=sum_{j=0}^{2m} lambda_{j+1}[2(3j-4m)d_j+4c_j]

satisfies F_2(1/2)=S_m-2 modulo p. The exact current Source next action is to compose this adjoint with the first-jet equation and perform finite summation by parts. This unit performs that requested composition and identifies its exact information boundary.

## 1. Parameter-dependent adjoint

Keep the full deformation coefficient

    b_j(a)=(j-m+a)(j-2m+2a).

Then at a=0,

    b'_j=3j-4m,
    b''_j=4.

Define the backward adjoint for the whole parameter family by

    lambda_p(a)=2^{-p},

    k^2 lambda_k(a)-b_k(a)lambda_{k+1}(a)=2^{-k},

for k=N,...,1. Every k is a p-unit, so lambda_k and its parameter derivatives are p-integral. Write lambda'_k and lambda''_k for the first two derivatives at a=0. Differentiation gives the exact adjoint-jet recurrences

    BOXED:
    k^2 lambda'_k-b_k lambda'_{k+1}=b'_k lambda_{k+1},       (A1)

    BOXED:
    k^2 lambda''_k-b_k lambda''_{k+1}
      =2b'_k lambda'_{k+1}+b''_k lambda_{k+1}.                (A2)

No fitted dual object has been introduced: these are derivatives of the already-durable evaluation adjoint.

## 2. First summation by parts removes the F_1 coefficient vector

The first parameter jet obeys

    k^2 d_k-b_{k-1}d_{k-1}=b'_{k-1}c_{k-1}.                 (F1)

Moreover c_j=0 for j>m, d_j=0 for j>2m, d_0=0, and the two zero-factor ports give b_m=b_{2m}=0. Put

    A_m=sum_{j=0}^{2m} b'_j lambda_{j+1}d_j.

Using (A1), d_0=0, and summing by parts over j=1,...,2m, the terminal term vanishes because b_{2m}=0. The remaining bracket is exactly (F1). Therefore

    BOXED:
    A_m=sum_{j=0}^{m} b'_j c_j lambda'_{j+1}.                (S1)

Consequently the complete interior second-jet source functional becomes

    BOXED:
    S_m=sum_{j=0}^{m} c_j
      [2b'_j lambda'_{j+1}+b''_j lambda_{j+1}].              (S2)

Thus the requested first-jet summation by parts is exact: the d_j/F_1 coefficient vector disappears, and only the order-0 source plus the differentiated adjoint remains.

## 3. Second summation by parts exposes an adjoint-closure identity

For j>=1, substitute (A2) into (S2). The order-0 coefficients satisfy

    j^2c_j=b_{j-1}c_{j-1}.

Summing from j=1 to m telescopes completely; the upper boundary vanishes because b_m=0. Restoring the j=0 source term gives

    S_m
      =b_0 lambda''_1+2b'_0 lambda'_1+b''_0 lambda_1
      =BOXED: [d^2/da^2 (b_0(a)lambda_1(a))]_{a=0}.          (S3)

This is the exact endpoint produced by the requested finite summation by parts.

## 4. Why (S3) is not a new LIFT constraint

For the full finite Gauss polynomial F(a,z), the same adjoint identity with nonzero constant coefficient c_0(a)=1 gives exactly

    F(a,1/2)
      =1+b_0(a)lambda_1(a)
       -2^{-p}b_N(a)c_N(a).                                 (G)

The terminal coefficient c_N(a) has a double zero at a=0. Hence the first two parameter orders of the last term are zero and its second derivative is exactly the already-proved terminal source

    [d^2/da^2(-2^{-p}b_N(a)c_N(a))]_{a=0}
      =B_m(1/2)=-2 (mod p).

Differentiating (G) twice and using (S3) therefore yields

    BOXED:
    F_2(1/2)=S_m-2 (mod p),                                (C)

which is precisely the durable adjoint checkpoint identity. Thus the requested operation closes algebraically, but it is a self-dual differentiation of the same finite Green identity; it does not create an independent endpoint equation and cannot by itself determine the live LIFT scalar.

This is a useful no-new-constraint result rather than a failure: repeated differentiation/summation-by-parts of the same L_a/adjoint pair is now proved to return the already-known second-jet endpoint. Continuing that loop cannot eliminate the remaining first-neglected p-adic product coordinate or compare it with R_p.

## 5. BRC information audit and exact next information need

Population: the finite Gauss parameter-jet ports together with the backward evaluation adjoint and the terminal k=p source.

Observer: the divided second p-adic digit after accepted UR.

Safe compression proved here: the F_1 coefficient vector in S_m may be replaced by the labelled adjoint-derivative carrier (c_j,lambda_j,lambda'_j), and that carrier further telescopes to the single endpoint derivative (S3).

Information boundary: the telescope is generated entirely by differentiating the same operator/adjoint identity. It therefore preserves, but cannot independently determine, the p-adic lift coordinate [a_parent Psi-1]/p that remains in

    LIFT <=> [a_parent Psi-1]/p
              +Psi_x/(36q)-q(S_m-2)/12-R_p = 0 (mod p).

The next proof-level step must introduce an independent source relation for that retained p-adic lift coordinate (or an equivalent Frobenius/creative-microscoping repair scalar) and couple it to the adjoint endpoint. Merely differentiating the finite adjoint again is do-not-repeat.

BRC_REUSE_RESOLUTION=COMPOSE_APPLIED.

## 6. Deterministic regression

The companion checker reconstructs c,d,F_2 and lambda,lambda',lambda'' modulo p directly from their recurrences. For every target prime p<5000 (166 total) it verifies with zero failures:

1. the first summation-by-parts equality (S1);
2. the reduced source equality (S2);
3. the endpoint telescope (S3);
4. the already-durable terminal relation F_2(1/2)=S_m-2.

The finite scan is falsification/regression only. The all-prime proof is the exact telescoping in Sections 1-4.

## 7. Narrow next action

Do not repeat parameter differentiation of the same finite adjoint. Keep S_m or equivalently the endpoint derivative (S3) as an already-controlled second-jet coordinate, and attack the genuinely independent p-adic lift coordinate [a_parent Psi-1]/p. The highest-information route is to compose the durable degree-p supersingular/Frobenius repair coordinate with the exact finite-Gauss parent bridge, or derive an equivalent source-level p-adic deformation whose first neglected digit is that product coordinate. Any proposed bridge must remain regular on the known singular first-order chart and must preserve the terminal -2 source. LIFT/JT2 remains open.
