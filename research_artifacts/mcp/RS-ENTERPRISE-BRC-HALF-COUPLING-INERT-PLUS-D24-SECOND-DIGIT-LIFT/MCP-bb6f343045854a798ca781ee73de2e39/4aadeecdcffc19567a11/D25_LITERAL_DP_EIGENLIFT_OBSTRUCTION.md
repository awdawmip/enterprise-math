# D25: low-order obstruction to the literal divided-power eigenlift

Status: AUTHOR_PROOF_V2 / LOCAL_SOURCE_INTERPRETATION_AUDIT / LIFT_OPEN. Written 2026-10-08 after own authorized open. V1 was frozen at SHA256 2c06b302cacbbbccde6f20c38c01aee060ded3047ab52502c25c0c3e3d980f38; V2 adds the Driver-requested ramified-argument scope boundary and actual regression results, without changing the theorem. This is not a Result, accepted theorem, or correction to accepted UR.

Author EM-ENTERPRISE-B078A6; session MCP-bb6f343045854a798ca781ee73de2e39; RA-8C8E44B2AA373F98BC5952A3; winning claim MCP-3d6d72356bcdfef82ab4cfc4; ER-7C265B422DC8E829AD44; authorized run RUN-252e05a5823d9e33ff848863 generation 1; run request d25-source-lift-open-20261008-r2. OPEN_RECEIPT_PAGE0.json contains authorized=true and CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7.

## Provenance and interpretation boundary

The fixed source is Chisholm, Deines, Long, Nebe, Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), DOI 10.3390/math1010009. PDF SHA256 3adacbce06377f7690237de150f5a48a0411d004703f5219f28c5691db6989e2 was locally recomputed and matches the prior source report. Publisher URL: https://www.mdpi.com/2227-7390/1/1/9/pdf. References below use printed journal pages, not PDF sequence numbers.

The prior accepted bounded fixed-x/xi exclusion at ac6ee6c5a280c4209506a135392be09f30f35f2a and checkpoint dab51c2f4cf508d6f048e7f52a7d1defd7c3d2a0a54e0418f4957f384a44675a is consumed. Its audit 2db5273269e71da8f2660bc4e917a7e78920b406 did not verify existence of a normalized divided-power CM eigenlift. No raw-H, alphaHat, UR, fixed-x identity, or generic prime scan is replayed here.

Native semantics remain fixed X6 discrete Cell space, no native plane, separately typed time when needed. This static elliptic algebra is an explicitly external coefficient observer over retained arithmetic labels. It supplies no full-X6 propagation or reconstruction claim and erases no unspecified native coordinates or joint relations.

Source exposure: directed Task/frontier, prior reports, and source paper. Driver supplied the bounded question but no proof formula. A temporary read-only librarian transcribed source definitions and checked PDF typography on pp.25–28, without a research identity, derivation or review. The author read the relevant source independently. This is author work awaiting independent Driver audit.

## 1. Exact formal statement

Let p be an odd prime, A an unramified complete discrete valuation ring of mixed characteristic (0,p), with fraction field K and residue field k. Let theta be any automorphism of A preserving p (in the source degree-p² setting, theta=sigma²). Extend theta coefficientwise. Put

    M = { B in xi K[[xi]] : B' in A[[xi]] },
    I = xi A[[xi]],             N = M / pI.

Every B in M has the unique expression

    B(xi) = sum(n>=1) b(n-1) xi^n/n,       b(n-1) in A.

Thus B is the formal primitive of the differential, and b(n-1) is a differential coefficient. The source's display mixing a primitive with an extra dxi is not used as a different coefficient convention.

Let Phi(xi) be in xi A[[xi]] with zero constant term and

    Phi(xi) = xi^(p²) modulo pA[[xi]].

The proof below only needs [xi^j]Phi in pA for 1<=j<=p. The literal source pullback is

    T(B) = B^theta(Phi(xi)).

This preserves M: integrality of dB and of Phi' proves integrality of dT(B). It also preserves pI, so induces an operator on N. Let lambda=p u with u in A a unit. An equality T([B])=lambda[B] in N means exactly

    D_B := B^theta(Phi(xi)) - lambda B(xi) belongs to pI.             (1)

**Theorem.** Equation (1) forces b(p-1) in pA.

**Proof.** The zero constant term of Phi makes the coefficient of xi^p in T(B) a finite sum over 1<=n<=p. For each n, every product contributing to [xi^p]Phi^n uses n coefficients of Phi whose indices are between 1 and p. Each coefficient belongs to pA. Consequently

    [xi^p]Phi^n in p^n A,
    (b(n-1)^theta/n)[xi^p]Phi^n in p^(n-v_p(n)) A.

For every integer 1<=n<=p and odd p, n-v_p(n)>=1, including n=p, when this exponent is p-1. Hence [xi^p]T(B) is in pA. On the other hand,

    [xi^p]lambda B = (lambda/p)b(p-1) = u b(p-1).

Taking the xi^p coefficient in (1) therefore gives u b(p-1)=0 modulo p. Since u is a unit, b(p-1)=0 modulo p. QED.

The argument is independent of leading-coefficient normalization, other coefficients of B, and the CM ring. Retaining additional CM conditions cannot remove this necessary obstruction for the specified operator/eigenvalue/quotient. It applies to every source prime p>=5; no numerical checks enter the proof.

## 2. An integral exact correction cannot cure it

Suppose B is replaced by B+F with F in I. The primitive of the corresponding differential changes by an ordinary integral exact primitive. Then

    D_(B+F)-D_B = F^theta(Phi) - lambda F.

Modulo p this equals Fbar^thetabar(xi^(p²)), so its order is at least p² (unless zero). In particular,

    [xi^p]D_(B+F) = [xi^p]D_B = -u b(p-1) modulo p.                 (2)

The coefficient b(p-1) itself changes by p[xi^p]F and so has the same reduction. Thus a companion whose b(p-1) is a unit has **no** integral exact correction satisfying the literal eigenlift equation. This is an existence obstruction after keeping the stronger operator condition, not the old assertion that arbitrary gauges preserve that condition.

There is also a useful conditional uniqueness statement. If B+F1 and B+F2 both satisfy (1), their difference F has Fbar^thetabar(xi^(p²))=0. Substitution xi -> xi^(p²) and the field automorphism thetabar are injective; therefore F lies in pI. So a compatible lift of a fixed ordinary formal class, if it exists, is unique in N. This uniqueness does not establish existence.

## 3. Exact comparison with the printed source

1. On p.25 (local text lines 1119–1122), omega and nu are called R-eigenfunctions in ordinary H^1_DR(E,C), embedded in ordinary H^1_DR(E/A). This statement is **not** itself a specified eigenlift in N.
2. On p.25 (lines 1137–1148), Frobenius acts by the semilinear substitution on formal primitives. The printed degree-p² assumption is obtained in the supersingular case; two iterations use theta=sigma². The proof above permits any coefficient automorphism, so this convention does not affect the obstruction.
3. On p.25 (lines 1150–1155), the displayed formal quotient has denominator {F in pA[[xi]]:F(0)=0}, exactly pI. The ordinary quotient immediately above has denominator I instead.
4. Proposition 16 (p.25, lines 1164–1171) explicitly assumes existence of a degree-p² lift commuting with the induced R action in the supersingular case. Commutation by itself does not state that the chosen ordinary nu has a particular eigenlift in N. This proof does not silently add that statement to the proposition's wording.
5. The supersingular proof (p.26, lines 1217–1220) says that the degree-p² Phi commutes with R and: **“Both omega and nu are eigenfunctions of Phi with the same eigenvalue -b_2.”** The paragraph is discussing the divided-power setting, but the printed text does not supply a separate corrected comparison map or lift that would justify interpreting this as equation (1). The present theorem audits precisely that literal interpretation.
6. The same setup has b_2²=±p² (p.25, lines 1156–1159), hence v_p(b_2)=1. Taking lambda=-b_2 in the theorem is therefore legitimate; no particular sign is required.
7. Proposition 16's supersingular product is a(p-1)b(p-1)=-b_2 modulo p². In the D25 inherited interface a(p-1)=p alpha with alpha a unit, so this requires b(p-1) a unit. Alternatively, if the literal eigenrelation is imposed on both primitives, the theorem forces both a(p-1) and b(p-1) into pA, contradicting any product congruent to a unit times p modulo p².
8. Theorem proof p.28 (lines 1364–1367) specifically chooses multiplication by -p after quartic twist as a degree-p² Frobenius map. Linear unit changes of parameter and unit normalization of a differential preserve whether b(p-1) is zero modulo p. They do not cure this obstruction. This note does not identify raw/twisted coefficients at the deeper D25 layer.
9. The final paragraph of the Proposition 16 proof, p.26 (lines 1217–1224), explicitly says: “In fact, such a lift phi exists by adding any p-torsion of the elliptic curve to Q_p(sqrt(1-lambda_d)), which allows us to solve phi^2 = Phi.” It continues: “The corresponding field extension is ramified. However, using the corresponding maximal ideal, the above argument shows that” the displayed divided product lies in that maximal ideal. The printed display has (a(p-1)b(p-1)-b_2)/p; its sign is retained as printed and is not used in this theorem. Our no-go concerns the original unramified A, denominator pI, and literal degree-p² substitution together. We have not audited transfer to a different cohomology/comparison construction or a quotient defined using the ramified maximal ideal. The source's ramified paragraph cannot be silently replaced by our original-ring model.

**Scope of conclusion.** The displayed quotient, literal substitution operator, valuation-one eigenvalue, unit companion coefficient, and the asserted lifted eigenrelation cannot all hold simultaneously. Therefore the supersingular proof's eigenfunction sentence cannot be used as an executable, literal N-eigenlift prescription for the D25 normalized companion. This does not refute Proposition 16 under every possible intended cohomological interpretation, its final theorem, accepted UR, or LIFT. It identifies an exact missing or mismatched comparison datum in this particular attempted source implementation.

## 4. What a usable corrected comparison would have to provide

If one uses a comparison defect instead of the impossible zero-defect prescription, write, with the same fixed operator,

    T(B_actual) - lambda B_actual = S modulo pI.                    (3)

For B_actual=B+F with F in I, reducing (3) gives

    Sbar - D_Bbar = Fbar^thetabar(xi^(p²)).                         (4)

Whenever D_B and S are integral, this is a necessary and sufficient condition on F modulo p: the difference on the left must have support only at positive degrees divisible by p². All coefficients then determine Fbar uniquely by inverse coefficient automorphism. Its xi^p coefficient obeys

    kappa = thetabar^(-1)( [xi^(p³)](Sbar-D_Bbar) ).                 (5)

Equation (2) requires in particular [xi^p]Sbar=-u b(p-1), a nonzero value for the relevant companion. Setting S=0 is already impossible at this lower degree, independently of the desired kappa. Formula (5) is a conditional extraction formula, not a computation of the actual source kappa: the cited source does not give this S. It illustrates exactly which additional comparison data would make this route executable. Other R-action/CM conditions must also be checked on that corrected model; they are not deleted by (4).

An ordinary CM eigenline can fix c after a basis and the actual CM action are supplied, but that does not supply S. No c_p is defined by forcing the desired product congruence. No value of c_p mod p², genuine kappa, Lcomp_p, or endpoint R_p is claimed here.

## 5. Validation and continuation

Actual validation: python check_literal_dp_eigenlift.py was run successfully on 2026-10-08, producing literal_dp_checks.json with zero failures. It reconstructs the invariant formal logarithm of the exact d=3 curve through degree p, then solves log(Phi)=-p log modulo p³ to compute the actual multiplication-by-minus-p low jet, at p=13 and p=19 only. It verifies every coefficient through degree p belongs to pA and checks the logarithm identity. For candidate c=1,6, respectively, the companion b(p-1) and defect coefficient modulo p are (1,6) at p=13 and (2,12) at p=19, while the substitution coefficient is zero in all four cases. These c values are fixtures, not identifications of source normalization. The n=p summand in composition is explicitly discarded only because its proven valuation is at least p-1>=3. The copied arithmetic module SHA256 is 83dd3574edcd55d6b42eba80de17f65c13238fe63dc0fa8d921697d5c90d748d; its old main scan is never invoked. No raw-H/alphaHat theorem is re-proved. The all-prime result remains the valuation argument in Sections 1–2; the finite calculations are implementation regressions. This is a task-specific check, not a new general-purpose mechanism; exact Q2 arithmetic is REUSE_EXECUTED.

Completed bounded proof: valuation-based obstruction to the literal supersingular DP eigenlift; inability of integral primitive correction to cure it; conditional uniqueness and coefficient extraction for a specified corrected comparison defect.

Still open: the intended actual cohomology/comparison operator or a source supplying its correction, exact ordinary CM normalization c_p, actual compatible lift, Lcomp and cutoff/endpoint bridge, LIFT/JT2. Next executable step: audit the explicit source operator/model against its cited formal-group reference and determine whether the eigenfunction assertion lives only in ordinary cohomology or uses a different comparison. Do not attempt to compute kappa from the impossible zero-defect prescription. Parent remains OPEN; user_requested_stop=false.
