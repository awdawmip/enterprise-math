# D25 — exact non-scalar de Rham first-jet bridge for the external 216/2304 CM elliptic fibers

Date: 2026-11-03. Classification: AUTHOR-DERIVED / EXACT ALGEBRA PROVED IN EXTERNAL ELLIPTIC DE RHAM / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This is NOT a native H0/B0 experiment or a formal Source checkpoint.

Frozen TASK_RESEARCH: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research lane chatgpt-research-onhour-enterprise-math-20260923; NOT the maintenance lane. Continue the immutable author-side frontier 74831cbeb2e571faa301f7b5bcff2dbd2c54687b. The original mother target Delta_p-R_p=0 (mod p), equivalently ORIGINAL weighted W216=p (mod p^3) for p=13,19 (mod24), remains OPEN.

## Local question with distinguishing outcome

The earlier exact E3/E4 quadratic twist and differential gauge phi*omega4=u^-1 omega3 did not give a valid original-weighted 216/2304 p-adic transport: the bare scalar candidate W216=(u^(p²-1))^-1 S2304 (mod p³) fails on all p=13 mod24 at first digit and at p=19 on the second digit. Does the *external elliptic cohomology* contain a missing derivative/second-kind coordinate? The answer below is a rigorous algebraic YES for a specified fiberwise first-jet map, with a precise limitation: it is not a comparison of the finite, truncated, original p-adic hypergeometric observations.

## Named geometric inputs

Let s=sqrt(2), d=3s, u²=d, t3=(2-s)/4, t4=(3-2s)/6. For lambda=-4t(t-1), lambda3=1/2 and lambda4=1/9. The external elliptic families are

    E3 : y3²+x3*y3+(t/27)*y3=x3³,
    E4 : y4²=x4³+x4²+(t/4)*x4.

Complete the first square Y3=y3+(x3+t/27)/2, Y4=y4. Write

    f3(x,t)=x³+(x+t/27)²/4;
    f4(x,t)=x³+x²+(t/4)x.

At the specified t3,t4 the exact prior quadratic-twist isomorphism phi is

    x4=d*(x3+1/12)-1/3, Y4=u³*Y3.

Use the two classes omega_i=dx_i/(2Y_i) and eta_i=x_i*omega_i in each external elliptic H^1_dR; the second is a differential of the second kind. Pullback is exactly

    phi*omega4=u^-1 omega3,
    phi*eta4=u eta3+(d/12-1/3)u^-1 omega3.             (1)

The fixed x-chart and named fiber and parameter of each class are retained. These objects are auxiliary algebraic elliptic curves, not the native P000 six-axis space.

## Theorem 1 — complete Gauss-Manin reduction certificates

For Y²=f(x,t), let theta_lambda=lambda d/dlambda=[t(t-1)/(2t-1)]d/dt. The polynomial identity

    -f_t=2(a+b*x)f+4P'(x)f-2P(x)f'(x)                  (2)

implies nabla_(d/dt)[omega]=a[omega]+b[eta] in H^1_dR: differentiate omega=dx/(2Y) holding x fixed, then subtract the exact differential d(P/Y). For the two families, the following expressions satisfy (2) IDENTICALLY over Q(t)[x]:

    E3: a3=-1/[3(t-1)], b3=-3/[t(t-1)],
        P3=1/[108(t-1)] + [(9-4t)/(12t(t-1))]x
           + [3/(t(t-1))]x².

    E4: a4=-1/[4(t-1)], b4=-1/[2t(t-1)],
        P4=[(2-t)/(4t(t-1))]x+[1/(2t(t-1))]x².

At the two *different* lambda parameters the exact coefficients are

    nabla_(theta3)omega3=(s-1)/6 omega3+3s eta3,
    nabla_(theta4)omega4=(3s-4)/32 omega4+(3s/8)eta4. (3)

The two parameter derivatives are first evaluated within their own families; only their resulting cohomology classes on the two isomorphic fibers are compared. This is NOT an assertion that the varying E3/E4 families, or their original parameter derivatives, are globally the same.

## Theorem 2 — NON-SCALAR fiberwise first-jet port

Combine (1),(3), eliminate eta3, and use u²=d=3s:

    ( phi*omega4                 )         ( 1  0 ) ( omega3                )
    ( phi*nabla_theta4(omega4) ) = u^-1 * ( A  B ) ( nabla_theta3(omega3) ),

    A=(s-2)/32,  B=d/8=3s/8.                           (4)

The lower-left entry A is genuinely NONZERO; for all good p>3, A and B are units in Fp[s]/(s²-2). Indeed A=0 would give s=2 and hence characteristic 2. The matrix determinant is u^-2 B=B/d=1/8, another p-unit. The first-jet port therefore retains an independent derivative/second-kind coordinate in the explicitly named bases. A raw scalar twist coefficient is not the same operation as this first-jet mapping.

## Theorem 3 — scalarization only after a named symmetric-square observer

In Sym² H^1_dR (odot denotes symmetric tensor product, NEVER wedge product), define

    Q3=omega3 odot omega3 +12 omega3 odot nabla_theta3(omega3);
    Q4=omega4 odot omega4 +16 omega4 odot nabla_theta4(omega4).

Because 1+16A=s/2, 16B=2d, and u²=d=3s, exact substitution in (4) gives

    phi*Q4=(1/6) Q3.                                   (5)

This is an exact external elliptic COHOMOLOGY symmetric-square identity with coefficients reflecting the formal 6k+1 and 8k+1 weighted differentiation of 3F2 square-type series. It is emphatically NOT W216=6 S2304 (mod p³): in the original finite weighted truncations both values equal p modulo p² on the target classes, so W216-6 S2304=-5p (mod p²) for p>5. An original-period comparison must provide its own normalized cycle and integral coefficient map, with p13/p19 orientation, p-adic lifts, and the existing nonzero p² cutoff boundaries.

The symmetric tensor loses the sign of u because u^-2=d^-1. The external quadratic-twist Frobenius sign is not itself the sign of the original 216 weighted finite readout, nor is it native H0/B0 semilinear Frobenius. This source/observer distinction explains why a formal first-jet result cannot promote a failed scalar hypothesis to the original D25 theorem.

## Executed certificate, BRC preservation and next step

The accompanying Python 3 / SymPy 1.14.0 checker symbolically verifies BOTH full polynomial identities (2), every CM coefficient in (3), the matrix (4), and symmetric-tensor factor (5). Independent exact Fp² coordinate arithmetic checks A, B and q=p² twist signs at p=13,19,37,43,109,373. Every assertion passed. The script's JSON is supplied independently. Symbolic algebra supplies the proof of the declared rational polynomial identities; six-prime tests are regression evidence and not a universal p-adic proof.

BRC classification: COMPOSE_APPLIED, external source labels E3/E4 separately retained; original x,t,lambda and CM fiber tags retained; omega/eta basis, tangent-direction operator, u square-root extension, signs, p-unit checks, and symmetric-tensor readout explicitly typed. The p-adic finite truncation and native original class have NOT been replaced or collapsed.

NEXT EXACT SCIENTIFIC ACTION: derive a genuine p-adically integral comparison identifying the **original finite weighted 216 and 2304 coefficient solutions** with the external period/first-jet classes, including compatible cycles, 13/19 orientation, exact weight, Frobenius lift, and the signed nonzero second-digit truncation. State one explicit candidate and test on original p13, p19, p373. An independent finite WZ/Gauss-Clausen three-source route remains OPEN.

NATIVE OBLIGATION UNCHANGED: enterprise-math#1559 original same-class p373 H0/B0 divided-power [X]U mod139129, rank, genuine semilinear Frobenius/eta, odd Green-Hesse/kappa, independent replay NOT_EXECUTED/PENDING_OWNER. This paper's external de Rham proof does not satisfy it.

Current Sites gateway 0.6.11: research_authority_granted=false, executor_binding_configured=false; exact continuation CONTROL_QUOTA; historical ordinary-Chat request remains FAILED UPSTREAM_CODE_REVIEW_REQUIRED at kimi-query-bridge#6633 (native lookup CONTROL_REQUEST_NOT_FOUND). No new native session, CLAIM, run, Source checkpoint, Result, review, admission or maintenance identity. No scheduler changes.

Source families: Chisholm–Deines–Long–Nebe–Swisher, p-Adic Analogues of Ramanujan Type Formulas for 1/pi (2013), DOI 10.3390/math1010009; published separate 2304 series theorem Guo–Zudilin, A q-microscope for supercongruences (2019), arXiv:1803.01830.
