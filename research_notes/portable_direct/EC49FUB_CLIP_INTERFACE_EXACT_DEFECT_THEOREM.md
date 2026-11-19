# EC49FUB — Sharp clipping-interface stochastic defect and Wasserstein bounds

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.

Direct parent: EC49FUA PR #2815, immutable commit 71564c619d245e007634c9dd80bc8ed4fe052fb1. Frozen native scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab (inherited BRC16943 Bellman input). This result concerns an **external joint-price-prior conditional readout**; native Bellman optimality is inherited as an author claim, not newly computed or reviewed.

## Exact theorem

Take the fee-gap interface m2=1469/64, with U=3/4, L=951/1280, W=U-L=9/1280. The joint price tilt is h_epsilon(a,b)=1-epsilon M_*(a,b)Z_*(a,b), with any finite real epsilon <= E=1048576/18958647. Let mu_minus and mu_plus denote the **weak one-sided limits** of the conditional discount law as m tends to m2 from below and above, respectively. The conditional value at exactly m2 is not uniquely fixed and is not asserted here.

Let nu_epsilon be the atomless probability measure with density proportional to 1-epsilon*m2*z on [L,U]. Then

    mu_minus = nu_epsilon
    mu_plus  = (1-q_epsilon)*nu_epsilon + q_epsilon*delta_U

where the exact top-atom mass is

    q_epsilon = 575*(41217719*epsilon-2359296)
                    / (45529434409*epsilon-2630615040).

This identity gives, for any bounded measurable observer phi,

    E_plus[phi] - E_minus[phi]
       = q_epsilon*(phi(U)-E_nu[phi]).

For nondecreasing phi the difference is nonnegative. For z<U the exact CDF identity is

    F_plus(z) = (1-q_epsilon)*F_minus(z).

For generalized quantiles Q (0<u<1),

    Q_plus(u) = Q_minus(u/(1-q_epsilon)), 0<u<1-q_epsilon;
    Q_plus(u) = U, 1-q_epsilon<=u<1.

Thus clipping introduces a finite observational defect in mass, moments and quantiles even when the continuous fiber itself has no discontinuity.

Using total variation TV=sup_A|mu(A)-nu(A)| and 1-Wasserstein distance W1 measured in the external scalar discount z, exact identities hold:

    TV(mu_plus,mu_minus) = q_epsilon;
    W1(mu_plus,mu_minus)
        = q_epsilon*(U-E_nu[Z]).

Both are strictly **decreasing** in epsilon for every epsilon<=E. The sharp lower bounds over the entire admissible parameter half-line are

    q_epsilon >= 3310244525/8132285009
              = q_E > 0,

    W1(mu_plus,mu_minus) >=
       10133262941675265/6885347826098094592
       = W1(E) > 0.

Equality holds at the admissible endpoint epsilon=E. The opposite (unattained) supremum limits as epsilon tends to minus infinity are

    q_minus_infinity = 23700188425/45529434409,
    W1_minus_infinity = 6782993927235/3712287963972224.

At epsilon=0, q=115/223 and W1=207/114176.

## Exact fiber calculation and proof

The inherited EC49FUA coordinate chart gives continuous mass
A(e)=A0-e*A1, top-clipping mass B(e)=B0-e*B1, and continuous first gap moment J(e)=J0-e*J1, where J(e)=c*integral_L^U (U-z)*(1-e*m2*z) dz and c=16/945. The unclipped clipping fiber has length d=23/3360. Exact integrations give

    A0=1/8400
    A1=133679/65536000
    B0=23/181440
    B1=948007537/428070666240
    J0=3/7168000
    J1=2102139/293601280000.

For atom-prior tilt one must average the uncollapsed **unclipped** price observer P=M_* Z_* across that price fiber. This gives

    mean_P_atom=41217719/2359296 > m2*U,

whereas the continuous observer mean is A1/A0=m2*(L+U)/2 < m2*U. Replacing the entire atom's prior by its clipped boundary value would lose this information and change the theorem.

Both A(E)>0 and B(E)>0. Since their coefficients of -e are positive, they stay positive for every e<=E. Therefore the right-limit conditional measure has weights A/(A+B) and B/(A+B), while the left-limit continuous law is nu. The mixture theorem follows by weak convergence of the inherited phase geometry.

The discrete atom has no counterpart in the left law, so TV=q. Coupling probability 1-q at unchanged continuous Z and transporting probability q of the same continuous Z to U costs q*(U-E_nu Z). The 1-Lipschitz test function f(z)=z attains the same expectation difference, so the coupling is optimal and W1 equals the displayed expression.

Exact differentiation yields

    q'(e)= -581059943674675200
           /(45529434409*e-2630615040)^2 <0.

The exact Wasserstein expression is

    W(e)=1035*(700713*e-40960)*(41217719*e-2359296)
         /(128*(2807259*e-163840)*
                 (45529434409*e-2630615040)).

Its algebraic derivative is

    W'(e) = -198720*P(e)
      /((2807259*e-163840)^2
        *(45529434409*e-2630615040)^2),

where

    P(e)=67100590040566349370337*e^2
         -7863342704812535316480*e
         +230358520503572889600.

Because E<1/18, P'(e)<0 for all e<=1/18, and the exact rational check

    P(1/18)=196581997098329904097/324 >0

implies P(e)>0 for every admissible e. Hence W'(e)<0 over the whole real half-line. Direct substitution and the limit e -> -infinity give the sharp rational constants stated above. This is an all-real analytic argument, not an inference from a finite grid.

## Verification, scope and continuation

The accompanying standard-library Fraction verifier rederives A0,A1,B0,B1,J0,J1 from the original fiber integrals, checks rational-function polynomial identities and derivative coefficients exactly, and checks all endpoint constants and the strict sign of P. Seven finite-parameter regressions are additional checks only. The JSON certificate is the actual recorded local execution output.

This proof does **not** identify m or z as native X6 coordinates, does not build a two-dimensional native plane, does not discard path/price provenance as globally redundant, and does not rerun a BRC Bellman experiment. It works within the inherited pricing observer only. P000 and ACTIVE worldview are unchanged. Source publication is distinct from Activity linkage and from formal Task/CLAIM/Result/Review acceptance.

Next open research unit: recover the frozen native Bellman decision branches for z<11/16, determine the exact next switching boundary, and compare its observable interface against the present externally clipped price-law discontinuity.