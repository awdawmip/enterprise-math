# Distinct-reader cross-check: full Parity trace uniform in every second gap

Reviewer: EM-DIRECT-099801.
Activity: RA-BALANCE-FORMAL-20261028-099801.
Date: 2026-10-28 (Asia/Shanghai).
Finding: LOCAL_NONAUTHOR_PAPER_CHECK_NO_MUSTFIX_FOUND on the stated complete
normalization and inherited metric/small-relative-gap interfaces.
This is a research review contribution, not a Driver verdict, formal Task
acceptance, Working Truth, Foundation promotion, or parent closure.

## 1. Exact scope of this independent reading

The complete frozen object reviewed is
`analysis/PARITY_FULL_TRACE_ALL_SECOND_GAPS_SUM_TAIL_AUTHOR.md`, SHA256
cf9fc55ac4a4a193cc4d5c9e8355fde02dae577f0241344b05d48961dea771a0.
I did not participate in its construction or supply proof suggestions before
the freeze. I inherited the owner's shared control/source context and the
task summary; this is distinct-author, source-exposed review, not clean-blind.

For the actual dependencies used in the new argument I read the complete
`analysis/PARITY_FULL_TRACE_BOUNDED_RELATIVE_GAP_TAIL_AUTHOR.md`, SHA256
129cad117292b1e90f3f0f8eb6c2791c2e5a050adff386c9e4a0b4c6e0d55c5e,
and the original centered-metric source in the saved full connector response
`analysis/parity_c1_v2_source_actual.json`, source blob
c94088a17f4a09dd2d16171162c09ed13807a8bf at
1a553d4d28a105230ecebd5a555dc8adbab8ee28. The latter's finite-difference metric
and centered parity Gram arguments are the concrete dependency relevant here.

I did not repeat the unchanged first-round small-cone proof or its old review.
The exact small-nu factor and its finite rational bound are consumed through
the explicitly identified bounded-relative-gap theorem. That consumption is
an inherited premise, not a claim that its earlier review has reviewed this
new unbounded-nu conclusion.

All forms here are external real algebraic auxiliaries. The native basis
remains Heartbeat World's signed six-axis Cell torsor, with no native plane;
the positive auxiliary reference form is not a native probability/positivity
axiom. No native spatial reduction or physical conclusion is used.

## 2. Exact common reference forms and trace orientation

The common input-center identity in the preceding paper gives exactly

    A*=E_lambda^T M(epsilon) E_lambda,
    B*=D_v E_lambda'^T M(epsilon/v) E_lambda' D_v.

Its input transformation is the same at the two endpoints. The output centers
may differ, but they are not substituted for two independent input changes.
This is essential for preserving the original relative trace. The scaling
indices j=0,...,m-2 give
2 sum_j(j-m+1/2)=-(m^2-1), so the limiting determinant ratio is
v^(m^2-1), with the exponent in the stated lower bound m+1.

For Sigma equal to +I on even degrees and -I on odd degrees, the inherited
limiting Gram proof gives P=Sigma M0>0 and P Sigma=Sigma P. The even-polynomial
E operators and diagonal D_v commute with Sigma; hence both positive forms
P_A and P_B commute with it. Their positive square roots and inverses do as
well. None of this requires P_A and P_B to commute with one another.

With C=P_B^(-1/2)P_A^(1/2), cyclicity of trace indeed gives

    T=tr[(Sigma+R_B)^(-1) C (Sigma+R_A) C^T].

The order of C and C^T is correct even when the two positive forms do not
commute. Since C commutes with Sigma,

    T0=tr(Sigma C Sigma C^T)=tr(CC^T)=||C||_F^2>0.

Equivalently the two limiting signed forms are simultaneously definite with
the same sign on each parity block. Their generalized eigenvalues are all
positive, so AM-GM with the determinant ratio gives
T0>=n v^(m+1) for every finite v>=1. This limiting statement is not being
incorrectly extended to definite finite-epsilon signed forms.

## 3. The effective metric bound is independent of both gap ratios

The displayed centered metric is consistent with the earlier factorization:
factoring the r powers from the basis (theta+r/2)^j gives the common factor
epsilon^(-n) and numerator (epsilon theta+1/2)^(j+k). There is no missing
lambda or nu in that metric.

For W=QM, the finite-difference cancellation removes all negative epsilon
powers. One can see the divisibility without a new computation: Q(0)=1,
the metric is analytic by the original finite-difference proof, and its
cleared numerator is a rational polynomial. Thus the numerator is divisible
by epsilon^n in the polynomial ring. W is polynomial, W(0)=M0, and
(W-M0 Q)/epsilon is again a symmetric polynomial matrix.

For 0<=epsilon<=1 the coefficientwise majorant E gives
|M(epsilon)-M0|<=epsilon E because every Q factor is at least one. The
operator bound uses real symmetry correctly:

    ||P^(-1/2) Delta P^(-1/2)||_2
    <= ||P^(-1)||_2 ||Delta||_2
    <= ||P^(-1)||_infinity ||Delta||_infinity.

Both P^(-1) and Delta are symmetric, so their spectral norms are bounded by
their maximum absolute row sums. The rational matrix P has a rational
inverse. Consequently k_m and Rpert_m=max(1,5k_m) are finite computable
rational quantities. Their definition does not claim evaluated numerical
values, reasonable cost, or a uniform bound in m.

At the later endpoint epsilon/v<=epsilon for v>=1, hence the same eta works.
Congruence of -eta P<=Delta<=eta P yields the normalized symmetric errors
R_A,R_B of norm at most eta in their respective positive reference metrics.
No condition number depending on v is introduced. Cross-parity error blocks
are retained in these R matrices; the proof does not project them away.

## 4. Independent derivation of the relative trace perturbation estimate

I checked the key estimate directly, including arbitrary cross-parity errors.
Let S=Sigma, let A=R_A and B=R_B, and suppose ||A||,||B||<=eta<1. Then

    ||(S+B)^(-1)|| <= 1/(1-eta),
    H=(S+B)^(-1)-S,
    ||H|| <= eta/(1-eta).

These follow by factoring S+B=S(I+SB), using S^2=I and ||S||=1. They do not
assume either signed matrix is positive definite.

An equivalent two-term expansion to the author's three-term expansion is

    T-T0 = tr[H C S C^T]
           + tr[(S+B)^(-1) C A C^T].

For arbitrary matrices in this finite real setting,
||C X C^T||_*<=||X||_2 ||C||_F^2. Trace duality therefore bounds these two
terms by eta/(1-eta)||C||_F^2 each. Thus

    |T-T0| <= 2eta/(1-eta) T0.

This proves the author's exact constant without a hidden dimension factor or
a growing additive error constant. Commutation with S is needed to identify
T0 with ||C||_F^2, not to erase A or B cross-parity parts. The argument uses
their full norms and is valid when those parts are nonzero.

At eta<=1/5 the relative error is at most one half. Consequently
T>=T0/2>=n v^(m+1)/2 uniformly for every lambda in [0,1] and every nu>=0.
In particular B* is invertible in this range by the same Neumann argument.

## 5. Quantifiers and the small/large ratio join

The relative estimate alone does not control a gap tending to zero because
Gap=T-n. The author correctly treats that region separately.

For nu>=1, v^(m+1)>=2^3=8, since m>=2. The comparison

    n v^(m+1)/2-n >= n(v^(m+1)-1)/4

requires only v^(m+1)>=3, so it holds throughout that region. For 0<nu<=1,
the exact small-nu factor in the C=1 bounded-relative-gap theorem supplies
the stronger coefficient n/2 instead of n/4. Its threshold depends on m but
not on lambda or the particular positive nu in that interval.

Taking the maximum of those two finite rational thresholds therefore yields
one R_m for every fixed m, independent of a,c,S. The substitution
r=m(S+a), nu=c/(S+a), lambda=a/(S+a) respects S>=0 and a>0: lambda lies in
(0,1], while the extra lambda=0 boundary is used only to obtain a uniform
bound. Since S+a>0, all displayed divisions are legal. The case S=0 is
included when a satisfies the total-scale threshold. There is no positive
lower bound on c, and no upper bound on c/(S+a).

Finally Bernoulli's inequality gives
((1+nu)^(m+1)-1)>= (m+1)nu, so the second stated lower bound
(m^2-1)c/[4(S+a)] has the correct factors and is strictly positive.
The overlap nu=1 leaves no uncovered interval.

## Outcome and preserved limits

No must-fix mathematical gap was found in the new relative-perturbation
argument, the effective threshold construction, or the two-region join at
the identified inherited inputs. The paper supports its stated whole-trace
tail for each fixed m and all positive second gaps.

This is a paper review only. No matrix/parameter scan, scientific program,
symbolic solver, m7/P11 certificate, Lean kernel or numerical experiment was
run. Hash checking binds the frozen text; it is not mathematical evidence.
No historical-novelty claim is reviewed here.

The compact total-scale region, a threshold uniform in m, coefficientwise
P1/higher-face positivity, and the complete mother objective remain open.
The earlier small-cone and bounded-relative tail domains are nested proof
history, not additional independent discoveries to count after this stronger
frontier is integrated. Recommended harvest is RESULT_ONLY_COMPOSE with the
same-signature positive reference forms, full cross-parity norm bounds and
the exact small-nu input retained as load-bearing conditions.

Researcher-ID: EM-DIRECT-099801 / TASK_RESEARCH
