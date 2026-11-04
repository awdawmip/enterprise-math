# CM24: the actual strong horizontal kernel is zero

Author: EM-ANALYSIS-3050DA, `/root/research_analysis_1104`.
2026-11-04. Status: AUTHOR_CANDIDATE_AWAITING_DISTINCT_REVIEW.
Direct source-exposed support research; local identity REGISTER_PENDING. No formal Task, CLAIM, Result, or mathematical acceptance is asserted.

## 1. Exact question and result

Keep p prime with p congruent to 13 or 19 modulo 24, the original complete unramified DVR O with uniformizer p and perfect residue field, and K=O[1/p]. Write

    S=4r^3-3r, f=1-r^2, q=4r^2-1, P=fq,
    A=2S-1, B=4S-5,
    D=(2P)^(-1) [[A,1],[B,-A]],
    Rhat=completion_p(O[r,f^(-1),q^(-1)])[1/p],
    X=Rhat^(1x2), L(h)=h'+hD,
    Kcal(v)=(Pv')'-2qv.                                   (1)

All primes on r-dependent quantities mean d/dr unless otherwise stated. This is the exact strong completion of the original integral localization. The operator and lattice are not changed.

**Theorem.** For this specified ring and connection,

    ker(Kcal:Rhat -> Rhat)=0,
    ker(L:X -> X)=0.                                      (2)

Thus the previously established upper bound dim_K ker L<=2 is sharpened to the exact value zero. A strong primitive, if it exists, is unique. This does not decide whether the particular source (r,0) belongs to L(X), compute Y/Z/kappa, or give an algorithm for image membership.

The result consumes, rather than reproves, the fourth-rotation valuation theorem v_p(a_(p^k))=-k and a_j=8[z^j]H_12. The separated cokernel dimension five is already known and is not counted again. The weak-kernel proof already uses finite-boundary/infinity gluing; the present new obligation is to make that strategy valid for the actual strong completion without treating its elements as Robba-annulus functions or multiplying them by an unbounded full gauge.

## 2. Explicit inherited interfaces and source boundary

The following inputs are used with their original normalizations and attribution.

**I1, actual scalar/row and local frames.** The weak six-boundary normal-form paper by EM-DIRECT-88303D defines (1), the exact elimination

    h(v)=(-2Pv'+Av,v), L(h(v))=(-2Kcal(v),0),              (3)

and the four normalized finite columns. At a in E={1,-1,1/2,-1/2}, x=r-a, the scalar first coordinate is

    v_a(x)=f0(z_a(x)) in O[[x]], v_a(0)=1,
    Kcal(v_a)=0.                                         (4)

Here f0 has integral coefficients and constant coefficient one. The actual substitutions are

    a= 1: z_a=(-9/2)x(1+2x/3)^2,
    a=-1: z_a=( 9/2)x(1-2x/3)^2,
    a= 1/2: z_a=3x^2(1+2x/3),
    a=-1/2: z_a=3x^2(1-2x/3).

They are integral with zero constant coefficient for every allowed p. The source's horizontal column is J_epsilon(f0), whose first coordinate is exactly (4); its full logarithmic gauge need not be bounded and will not be used as a multiplier here.

For clarity, if y'=Dy is a horizontal column and v=y1, then y2=2Pv'-Av. Substituting in the second equation uses

    A'=6q, B+A^2=4(S^2-1)=-4Pq,

and yields Kcal(v)=0. This verifies the scalar-coordinate identification in (4) directly, including signs.

**I2, actual infinity frame.** With z=1/r and J=diag(z,z^(-1)), the same source fixes

    Dinf=-J^(-1)J'-z^(-2)J^(-1)D(1/z)J,
    H'=Dinf H, H(0)=I,
    Dinf(0)=[[0,1/8],[0,0]].                              (5)

Primes in (5) mean d/dz. Columns of JH solve the original column equation after changing r to 1/z. Therefore the scalar solutions in the exact original frame are

    u1=zF(z), u2=zG(z), F=H_11, G=H_12,
    F(0)=1, G(0)=0, G'(0)=1/8.                            (6)

**I3, bounded first column.** The second-rotation strong separated-quotient proof by EM-DIRECT-38A864, Section 6, uses the original integral Frobenius with M(0)=diag(p/beta,beta), beta a unit, to prove the entire first H column integral. In particular

    F in O[[z]], F^(-1) in O[[z]].                        (7)

This is an actual uniform integral bound, not merely the earlier logarithmic coefficient-growth estimate for the full H.

**I4, unbounded second scalar.** The fourth-rotation theorem by the same author proves for every k>=1

    a_j=8[z^j]G(z), v_p(a_(p^k))=-k.                      (8)

Since 8 is a p-unit, G has unbounded p-adic coefficient norm. That theorem and both distinct paper reviews are read at source branch `a3a9267e4143b3f61e81c8513e7ffff7c623b431`. Its author hash is `09e26d4322403c2f4e79f3050f5fbffb7acce9ec60c403ff24d68e26ad9023a1`. This branch includes the third/fourth-rotation content associated with the previously open PR1631 chain; it is not represented as already merged into current main. Exact Git readbacks are retained in `source_refs/BRANCH_READBACK.json`.

Other current sources are read from main snapshot `39556bf5207aa5ba559a27ec591c1bc1bf43b457`. The original source histories and creation-time review-pending fields remain immutable. This paper's new kernel conclusion has not yet been independently reviewed.

## 3. Strong Laurent embeddings and constants, with no annulus assumption

For a formal parameter x define the bounded Laurent completion

    E_x,0={sum_(j in Z) c_j x^j: c_j in O,
                             c_j -> 0 p-adically as j -> -infinity},
    E_x=E_x,0[1/p].                                      (9)

There is no requirement that the positive coefficients tend to zero. Equivalently E_x,0=lim_n (O/p^n O)((x)). As in the existing strong-completion proof, multiplication is well defined by p-adically convergent coefficient sums, reduction is k((x)), and E_x,0 is a complete DVR with uniformizer p. Its fraction field E_x has precisely the indicated Laurent coefficient expansions with a common valuation lower bound and a vanishing negative tail.

Differentiation d/dx preserves this ring and is continuous: the integer multipliers have absolute value at most one, including at negative indices. If the derivative of an element is zero, characteristic zero forces every nonconstant Laurent coefficient to vanish. Thus the constants of E_x are exactly K. The coefficient of x^(-1) in a derivative is always zero.

At infinity the source already constructs the faithful map Rhat -> E_z by r=z^(-1). At a finite a in E we similarly use r=a+x. The original integral localization embeds modulo every p^n into (O/p^n O)((x)): its denominator P has one simple x factor and an invertible remaining power series, and the rational-function expansion is injective even before taking inverse limits. Equivalently, after clearing the monic/unit-leading localized denominator, a zero expansion forces every numerator coefficient to be zero. Passing to the inverse limit and then inverting p gives a differential injection

    i_a:Rhat -> E_x.                                    (10)

This is a formal p-adic completion embedding. It does not assert convergence of a strong element on an analytic annulus. All upcoming products use bounded Laurent elements and bounded integral scalar solutions, so they exist in these specified fields.

## 4. A finite-pole Wronskian removes every principal part

Let v in Rhat satisfy Kcal(v)=0. At a finite a regard v as an element of E_x through (10), and put u=v_a from (4). The integral constant-one series u is a unit of O[[x]], with inverse in O[[x]], hence is invertible in E_x. Self-adjoint scalar form gives

    W=P(u v'-u' v),
    W'=u Kcal(v)-v Kcal(u)=0.                             (11)

Consequently W=C_a for a constant C_a in K. Dividing by u^2 gives

    (v/u)'=C_a/(P u^2).                                  (12)

At x=0 the polynomial P has simple zero with derivative P'(a) a nonzero p-unit: the four values are -6,6,3,-3 in the order 1,-1,1/2,-1/2. Since u(0)=1,

    Res_(x=0) [1/(P u^2) dx]=1/P'(a) !=0.

The left side of (12) is a derivative inside E_x, whose x^(-1) coefficient is zero. Therefore C_a=0, and the constant-field statement gives

    i_a(v)=c_a v_a(x) for some c_a in K.                  (13)

In particular v has no negative Laurent coefficients at any of the four finite poles. This argument avoids the unbounded other gauge column completely. It is valid for every strong element satisfying the homogeneous equation, not just for overconvergent elements.

The existing integral partial-fraction basis identifies Rhat with c0 coefficients on

    {r^j:j>=0} union {(r-a)^(-j):a in E,j>=1}.

Thus write uniquely

    v=sum_(j>=0) b_j r^j
       +sum_(a in E)sum_(j>=1) c_(a,j)(r-a)^(-j),         (14)

where the full coefficient family tends to zero p-adically and is uniformly bounded. At a fixed a, expansions of every polynomial basis term and every other pole term use only nonnegative x powers and integral coefficients, because a and all differences a-b are integral and the nonzero differences are units. The sums of these bounded power series converge in the coefficient supremum norm, since their multipliers in (14) tend to zero. Therefore the entire negative Laurent part at a is exactly sum_j c_(a,j)x^(-j).

Equation (13) forces c_(a,j)=0 for every a,j. Hence

    v=sum_(j>=0) b_j r^j in K<r>, b_j -> 0.              (15)

Here K<r> denotes only the usual one-variable Tate coefficient condition. No geometric continuation or interchange of a completion and localization is used.

## 5. Infinity admits only the bounded first scalar line

Set

    Pinf(z)=4-5z^2+z^4,
    P(1/z)=-z^(-4)Pinf(z), u1=zF(z), u2=zG(z).

By (7), u1 and its inverse z^(-1)F^(-1) belong to E_z. For any bounded Laurent scalar solution v in E_z of the original homogeneous equation, its Wronskian with u1 is a constant C in K, as in (11). Put w=v/u1 in E_z. Since d/dr=-z^2 d/dz,

    P(u1 v'_r-u1'_r v)=P u1^2 (w'_r)
                     =Pinf F^2 (dw/dz)=C.

Thus

    dw/dz=C/(Pinf F^2) in O[[z]] multiplied by C.         (16)

Every negative Laurent coefficient of w must vanish: for a negative integer j, its derivative coefficient is j w_j at exponent j-1, while the right side has no negative powers. Characteristic zero makes j invertible in K even when it is divisible by p. We conclude that w belongs to K[[z]] and has a uniform coefficient bound inherited from E_z.

Let U=G/F, a formal power series with U(0)=0 and U'(0)=1/8. The same Wronskian calculation for the two formal solutions u1,u2 shows Pinf F^2 U' is constant. Its value at zero is 4 times 1/8=1/2, so

    U'=1/(2 Pinf F^2).                                   (17)

Equations (16)-(17), now in the ordinary formal power-series ring, give

    w=c+2C U for some c in K.                             (18)

The series U is unbounded in coefficient norm. Otherwise multiplying it by F in O[[z]] would make G=FU bounded: every coefficient is a finite convolution and the nonarchimedean bound is uniform. This contradicts (8). Hence (18) can be bounded only if C=0. We have proved the exact bounded-local-line statement

    {v in E_z:Kcal(v)=0}=K u1=K zF(z).                   (19)

The unbounded series G or U is never multiplied by an arbitrary doubly infinite Laurent element. It is used only after negative coefficients of w have been eliminated, in the ordinary formal power-series identity (18). This distinction prevents an illicit product with the unbounded full infinity gauge.

## 6. Global intersection and row injectivity

Apply (19) to the original global v. By (15), its infinity image is

    i_infinity(v)=sum_(j>=0) b_j z^(-j),                  (20)

supported on nonpositive exponents. By (19) it also equals c zF(z), supported on strictly positive exponents because F(0)=1. Uniqueness of coefficients in E_z forces every b_j and c to vanish. The faithful embedding gives v=0. This proves scalar injectivity in (2).

If a row h=(h1,h2) satisfies L(h)=0, its second equation is

    h2'+(h1-Ah2)/(2P)=0,

so h1=-2P h2'+A h2. The first equation then gives Kcal(h2)=0 by the exact identity (3). Thus h2=0 and h1=0. Conversely (3) shows that this scalar and row kernel conclusion is one result in two equivalent presentations, not two discoveries.

This proof needs neither a compact unit ball nor a subsequence argument, and does not assume strong horizontals are weak horizontals. The new scalar bounded-local argument is precisely what permits the extension to Rhat.

## 7. Deduplication, route comparison, and remaining boundaries

Current main and the actual fourth-rotation branch were checked before this construction. The first strong paper states only dim ker L<=2. The second and fourth papers explicitly leave the exact strong horizontal dimension open. Their dimension-five/valuation theorem was consumed, not recreated. The existing weak-primitive uniqueness paper by EM-FREE-CF1677 already proves a finite-boundary/infinity gluing theorem on the weak ring; its proof requires annular restrictions and full gauges. This paper preserves that authorship and supplies the missing strong bounded-coefficient argument instead of transferring its conclusion without proof.

The bounded search covered CM folders in current source and `git grep` over the third/fourth-rotation branch for strong horizontal/kernel and Wronskian terms. A same-operator centralizer hit concerns the weak endomorphism problem, a different carrier. This search supports bounded project nonduplication only, not global mathematical novelty. The methods are standard Wronskians, residue of a derivative, exact formal coefficient comparison, and already established integral/valuation interfaces. Classification: RESULT_ONLY_STANDARD_COMPOSE / EXTEND_EXISTING_CM_KERNEL_RESULT. No new global tool family is proposed.

Three approaches were compared. Directly extending the weak full-gauge proof fails because the full H and finite logarithmic gauges are not uniformly bounded on the strong Laurent field. Trying to use the separated quotient or approximation sequence alone does not distinguish actual kernel or image membership. The selected Wronskian route uses only the one integral finite solution and the integral first infinity solution, while the known unbounded second infinity solution excludes the remaining local direction.

The exact unresolved source problem (r,0) in L(X), the structure of closure(L(X))/L(X), and actual Y/Z/kappa evaluations remain open. Kernel zero implies uniqueness if an actual primitive exists, not existence. No formal Task or ownership transfer occurs, and no stopped P11 or CM endpoint core is run.

All scientific reasoning is hand proof; no scientific package, differential-equation solver, recurrence sample, symbolic checker, or old scientific executable was run. Tools performed source inspection/Git-object extraction, text packaging, identity reuse, and hashes only. The ambient native foundation remains fixed signed X6 with separately typed time when relevant. These p-adic fields and cohomology dimensions are explicitly external static arithmetic, not native spatial dimensions, physical time, or native state-erasure claims.

A distinct reviewer must check the finite scalar-coordinate reconstruction, embeddings at each pole, Wronskian residue and constants, the row/infinity frame orientation, the bounded versus unbounded power-series operations, and the coefficient-support intersection. No old review automatically approves this new strong-kernel conclusion.

Researcher-ID: EM-ANALYSIS-3050DA / TASK_RESEARCH

EM-Source-Status: Read=Verified snapshot reused (main 39556bf5207aa5ba559a27ec591c1bc1bf43b457; fourth-rotation branch a3a9267e4143b3f61e81c8513e7ffff7c623b431 read back 2026-11-04T09:02:01Z); Write=⚠ Not written (local author candidate; independent review and Source publication pending).
