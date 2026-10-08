# D25: the exact E3 period gauge and its ordinary CM scalar

Status: AUTHOR_PROOF_V1 / SOURCE_BOUND_ORDINARY_CLASS / LIFT_OPEN, 2026-10-08. Author EM-ENTERPRISE-B078A6, session MCP-bb6f343045854a798ca781ee73de2e39, RA-8C8E44B2AA373F98BC5952A3, winning claim MCP-3d6d72356bcdfef82ab4cfc4, ER-7C265B422DC8E829AD44, authorized run RUN-252e05a5823d9e33ff848863 generation 1. Same existing Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7; no release or Task/parent closure.

## 1. Precisely separated inputs and conclusion

The fixed source is Chisholm–Deines–Long–Nebe–Swisher, Mathematics 1 (2013), DOI 10.3390/math1010009, PDF SHA256 3adacbce06377f7690237de150f5a48a0411d004703f5219f28c5691db6989e2. Its statements used here are:

* Printed p.11, equation (2.1): at the stated CM value, the normalized Ramanujan series has unique algebraic parameters a and delta. This uniqueness is used as a source theorem, not newly proved by a transcendence argument here.
* Section 3.4, p.18, equation (3.10): the periods on the same nonzero cycle of the holomorphic CM eigenclass and the other CM eigenclass have product an algebraic multiple of pi.
* Remark 7, pp.19–20, identifies the hypergeometric Picard–Fuchs solutions of the E3 family. We verify the actual invariant differential and its exact period factor below rather than infer a gauge from the name of that equation.
* The proof on p.27 explicitly assumes the normalized ordinary companion class nu=omega+c partial_lambda omega. This is the class normalization considered here, with algebraic c. We do not replace it by an arbitrary class on the same line or assume a divided-power representative normalization.
* The ordinary analytic Clausen identity, p.27 preceding Lemma 18, relates F(1/3,2/3;1;t)^2 to S(lambda) below. This use involves convergent complex periods, not the finite-prime Clausen truncation or accepted UR proof.

The independent numerical constant in the Ramanujan identity is pinned to Jesus Guillera, *A method for proving Ramanujan series for 1/pi*, arXiv:1807.07394v4 (16 August 2018), https://arxiv.org/pdf/1807.07394v4. PDF 146983 bytes, SHA256 8957b8ec11ee566a22f66e95f0036b9a288a95473b1902d87bbc6678762c0e83. Formula (1), p.1 defines its a+bn convention. Table 3, p.10, positive-z first row gives level 3, degree 2, z=1/2, a_G=1/(3 sqrt(3)), b_G=6/(3 sqrt(3)); hence in the 2013 normalized convention a=b_G/a_G=6 and delta=1/a_G=3 sqrt(3). The author visually checked the original table image. This is a cited analytic formula, not a new proof of the Ramanujan identity; no finite product congruence is used to obtain 6.

**Conclusion with these explicit source inputs.** For the original untwisted E3 invariant differential and lambda=1/2, the ordinary normalized anti-CM class assumed on p.27 has

    c_CM=6 exactly; in any permitted p-adic embedding, c_CM=6 mod p^2.

This conclusion concerns the scalar in that fixed ordinary Gauss–Manin basis. It does not identify an actual divided-power companion representative or kappa, and it does not identify any differently normalized scalar introduced to force a raw coefficient product. The exact new work is the period-gauge certificate and the scalar-identification argument in Sections 2–4, conditional only on the listed source CM/uniqueness statements.

## 2. Direct Picard–Fuchs certificate for the actual differential

Over Q(t) take exactly

    E_t: y^2+xy+(t/27)y=x^3,
    D=2y+x+t/27,       P=D^2=4x^3+(x+t/27)^2,
    omega=dx/D.

We use fixed x to compute the connection; the accepted fixed-x/fixed-xi bridge remains an input and is not re-proved. The parameter derivatives of the displayed representative give

    partial_t omega = -(x+t/27) dx/(27 P^(3/2)),
    partial_t^2 omega = [-P+3(x+t/27)^2] dx/(729 P^(5/2)).

Define

    L_t=t(1-t)partial_t^2+(1-2t)partial_t-2/9,
    R=x(-2t^2+108tx+9t+11664x^3+3888x^2+243x)/6561.

Then the exact rational-function identity on E_t is

    L_t omega = d_x(R/D^3).                                    (1)

Indeed, after multiplying by D^5/dx, its right-hand numerator is

    R_x P-(3/2)R P_x,

and its left-hand numerator is

    t(1-t)[-P+3(x+t/27)^2]/729
      -(1-2t)(x+t/27)P/27 -(2/9)P^2.

Expanding these explicit polynomials gives equality in Q[t,x]. This is a finite exact certificate, not an empirical fit of period coefficients. The rational function R/D^3 is single-valued on the elliptic curve, so its differential has zero integral on every closed cycle avoiding its poles. Thus every transported period of this specific omega obeys L_t p=0.

## 3. Cycle initial value fixes the gauge

Fix a small radius 0<r<1/4. For sufficiently small complex t, the two roots of P near x=0 are inside |x|=r and its third root near -1/4 is outside. There is a branch of D on an annular neighborhood of this circle that tends to x sqrt(1+4x) as t tends to zero, with sqrt(1+4x) taking value 1 at x=0. The even number of enclosed branch points makes the lifted contour closed. Choose its orientation by the positive x-circle and call this cycle C_t.

On this fixed contour the integrand and its parameter derivatives are holomorphic in t, so

    p(t)=integral_(C_t) omega

is analytic near t=0. At the limit,

    p(0)=integral_(|x|=r) dx/[x sqrt(1+4x)]=2 pi i,             (2)

by the residue at x=0. Although the central curve is singular, only the contour away from its node is used in this limit. The nonzero period also proves that the chosen cycle is nontrivial on nearby smooth fibers.

An analytic solution q(t)=sum q_n t^n of L_t q=0 satisfies

    (n+1)^2 q_(n+1)=(n+1/3)(n+2/3)q_n.

Consequently its initial value determines it uniquely, and (1)–(2) prove

    p(t)=2 pi i F(1/3,2/3;1;t).                               (3)

The factor 2 pi i is constant in t. In particular there is no hidden nonconstant algebraic gauge multiplying this hypergeometric period of omega. Continue this cycle along the real interval from small positive t to

    t0=(1-1/sqrt(2))/2=(2-sqrt(2))/4,

which encounters neither singular fiber t=0,1. This is precisely the square-root branch used in the inherited D25 model, not (1-sqrt(2))/2.

Put lambda=4t(1-t) and f(lambda)=F(1/3,2/3;1;t(lambda)), with t(0)=0. The change of variables gives exactly

    L_t f(lambda)=4{lambda(1-lambda)f''+(1-3lambda/2)f'-f/18}.

The analytic initial value is f(0)=1. Equivalently f=F(1/6,1/3;1;lambda), and ordinary Clausen gives

    f(lambda)^2=S(lambda)
      =sum(k>=0) (1/2)_k(1/3)_k(2/3)_k lambda^k/(k!)^3.        (4)

All functions in (3)–(4) are analytic at lambda=1/2 on the stated branch; no truncation or p-adic congruence enters.

## 4. The normalized ordinary CM coefficient

At a CM lambda0 on this branch, let the source's normalized other eigenclass be

    nu=omega+c_CM partial_lambda omega.

The coefficient is algebraic by the assumed source CM construction. Gauss–Manin differentiation of periods on a transported cycle and (3) imply

    integral_C nu =2 pi i (f+c_CM f'),
    (integral_C omega)(integral_C nu)
       =-4 pi^2 {S+(c_CM/2)S'} at lambda0.                    (5)

The CM period-product statement makes the left-hand side an algebraic multiple of pi. Therefore

    S(lambda0)+(c_CM/2)S'(lambda0)=delta'/pi,

for an algebraic delta'. Expressing this as the normalized Ramanujan series (2.1) gives the coefficient

    a'=c_CM/(2lambda0).

The source's uniqueness of its algebraic pair a,delta now forces a'=a, and hence

    c_CM=2lambda0 a.                                          (6)

For lambda0=1/2 and the independently cited Table 3 datum a=6, equation (6) yields c_CM=6. This uses the infinite analytic CM period normalization; it does not define c_CM by any desired finite congruence. The formal invariant differential in xi=-x/y has leading coefficient 1 independently of t; its fixed-xi parameter derivative has leading coefficient 0. Thus the candidate representative omega+6 partial_lambda omega in that frame also has leading coefficient 1, consistently with the source's ordinary normalization. An exact-form choice remains a separate question.

## 5. What this does not transport to D25 automatically

The earlier finite-coefficient distinction is retained. The accepted interface writes alpha=H_(3,p-1)/p, beta=F_p/p, C_p=beta-alpha and proves

    6 alpha J_p^(xi)=1-6 C_p J_p^F mod p.

Neither (3) nor (6) makes C_p vanish: the exact complex period solves a differential equation, whereas the local formal coefficient H and a truncated hypergeometric sum are different arithmetic objects one layer deeper. This note gives no new all-prime value of 6 alpha J; the old finite witness remains only a finite witness.

If c_p in a later argument denotes precisely the coefficient of this normalized ordinary CM class in the fixed basis, its value is now source-bound to 6. If c_p instead denotes a rescaled companion chosen so that c_p alpha J=1 mod p, equality with c_CM has not been proved and cannot be imposed by renaming the scalars. In particular, the expression (6 alphaHat J-1)/p may only be reduced modulo p after its numerator's p-divisibility is justified in the intended actual model. This note does not assert that divisibility.

An actual D_p class, its Frobenius action/identification, its comparison section to the desired ordinary representative, and the same-class primitive difference needed for kappa are still required. Integral ordinary primitive corrections change the differential coefficient b(p-1) only by a multiple of p; they cannot silently repair a first-digit discrepancy. The literal eigenlift obstruction and the conditional Katz comparison boundary remain in force with their exact limited hypotheses. No accepted UR theorem is retracted, no raw product is identified with the target through p^3, and no actual kappa or LIFT/JT2 value is obtained here.

## 6. Actual validation and continuation

Executed check_e3_period_gauge.py with SymPy 1.14.0. Its output e3_period_gauge_checks.json records: the full Q[t,x] numerator residual is 0; all three exact change-of-variable coefficient residuals are 0; seven analytic-recurrence index checks passed; zero failures; zero prime tests. The analytic contour argument and source-bound scalar deduction are proved above, not delegated to numerical testing. No old raw-H/alphaHat scan, fixed-x bridge, or finite congruence proof was rerun.

Source exposure: inherited D25 frontier and prior proofs; fixed 2013 original; Katz extraction and earlier bounded units; direct original Guillera Table 3 and equation (1). An exact-formula web search located a 2026 note, arXiv:2604.03327v1 Lemma 2, which points to Guillera Table 3; that note was a locator only, not a new D25 proof input. The historical Ramanujan paper transcription was also inspected while locating the constant but did not supply this table entry. Driver authorized the E3/PF normalization question and independent review, without supplying this certificate or scalar argument. This is author work awaiting its own independent audit.

Completed: exact E3 invariant-differential PF certificate, constant period gauge, and source-bound identification of the normalized ordinary CM coefficient c_CM=6 (hence modulo p^2). Still open: actual full companion/lift comparison and kappa, the admissible raw coefficient product observer, endpoint bridge, LIFT/JT2 and parent. Next step: independently audit this new ordinary-class conclusion, then specify which actual comparison/representative model can consistently connect it to the D25 first and second coefficient digits; do not obtain that connection by forcing the target product. user_requested_stop=false. This is external elliptic algebra, not a native X6 propagation claim.
