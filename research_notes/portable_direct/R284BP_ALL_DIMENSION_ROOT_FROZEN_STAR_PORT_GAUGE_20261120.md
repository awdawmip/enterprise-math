# R284BP — All-dimension root-frozen star-Port gauge and exact identifiability

Date: 2026-11-20 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Model: auxiliary signed determinant Port observer, not asserted to implement X6-native dynamics or BRC positive-mass arithmetic. Mathematical source frontier: R284BO @ a6cce9ae0bd967ff7f8bd3e16be71f5787963824, which establishes the n=3, arbitrary-H frozen-diagonal classification. This note extends **the root-frozen part** to every n>=3. A frozen leaf in n>=4 remains open.

## Exact observer and fibre theorem

Let n>=3, H>=2, C in {1,...,H}^{n x n}. Write C in blocks

    C = [ a  b^T ]
        [ v   A  ]

where a is a scalar, b,v have n-1 positive integer entries, and A is an (n-1)x(n-1) strictly positive integer matrix. Put m=n-1; for leaf controls x=(d_1,...,d_m), set B(x)=diag(x)-A and g_A,v(x)=adj(B(x))v. With a fixed integer root control d_0=t and free independent leaf-diagonal and directed star controls z=(z_1,...,z_m),

    F_C(x,z) = det(diag(t,x)-C-sum_{i=1}^m z_i E_{0i})
             = (t-a) det B(x) - (b+z)^T g_A,v(x).                    (1)

**BP1 (complete root-frozen constant-fibre classification).**
For any two rational matrices C,C' with nonzero components of v, the difference F_C-F_C' is independent of every x_i and z_i if and only if there is a rational column vector alpha such that

    a' = a;       v' = v;
    A' = A + v alpha^T;
    b' = b - (t-a) alpha.                                          (2)

In that case F_C=F_C' exactly, with zero constant difference. In particular, for n>=3 there are NO distinct positive rational matrices whose frozen-root responses differ by a nonzero constant.

This characterizes the observer's exact algebraic gauge orbit. It does NOT say that collapsing a gauge orbit preserves subsequent operations outside the declared frozen-root observer family.

**BP2 (sharp integer-alphabet boundary, all n>=3).**
For C in {1,...,H}^{n x n}, some distinct C,C' have F_C=F_C' identically if and only if

    1-H(H-1) <= t <= H^2.                                         (3)

Outside this interval every distinct pair has a nonconstant response difference.

**BP3 (arbitrary finite adversarial circular noise).**
Let the one observation be an element of F_p displayed on a real circle of circumference p with any prescribed error bound rho>=0. There exists a prime p and a fixed, nonadaptive assignment of all 2m free controls such that every one of the H^{n^2} candidates is uniquely decodable under every circular error of radius <=rho if and only if

    t is an integer outside [1-H(H-1), H^2].                      (4)

Consequently, the least nonnegative allowable frozen root setting is H^2+1, independently of n and of any finite rho. This is an existence and finite-table decoding result; no efficient parameter search, minimal modulus, polynomial-time decoding, physical sensor or BRC realization is claimed.

## Proof

1. The adjugate vector g=adj(diag(x)-A)v is multi-affine in the m independent variables x_i. For each k, its coefficient of the monomial product_{r != k} x_r is v_k. Thus equality g=g' implies v=v'. For k != l, compare the coefficients of product_{r != k,l} x_r in component g_k. These coefficients are A_{kl} v_l - A_{ll} v_k. Equality therefore yields

    (A'_{kl}-A_{kl}) v_l = (A'_{ll}-A_{ll}) v_k.

As all v_l are nonzero, setting alpha_l=(A'_{ll}-A_{ll})/v_l gives A'=A+v alpha^T. Conversely, by the matrix-determinant lemma, for B'=B-v alpha^T,

    det B' = det B - alpha^T adj(B)v,
    adj(B')v = adj(B)v.                                           (5)

The second identity holds on the open set where B is invertible by Sherman–Morrison, hence identically as a polynomial, including singular x.

2. If F_C-F_C' is independent of z, their z coefficients imply g=g', so step 1 applies. The coefficient of the full product x_1...x_m in (1) is t-a, since g has degree at most m-1. Hence a=a'. Substituting (5) into (1) gives

    F_C' - F_C = -[(t-a)alpha + b' - b]^T g.                       (6)

The m degree-(m-1) monomials product_{r != k} x_r in the components of g are distinct and have coefficients v_k !=0. Since m-1>=1, the right side of (6) can be constant only if every coordinate of its bracket vanishes. Thus b'=b-(t-a)alpha and the difference is exactly zero. The converse follows from (5) and (1). This proves BP1, including the n>=3 boundary.

3. For C,C' with alphabet {1,...,H}, if they are distinct in one gauge orbit then alpha_l !=0 for some l. The integer (A'_{ll}-A_{ll})=v_l alpha_l is nonzero, so |alpha_l|>=1/v_l>=1/H. Meanwhile b_l-b'_l=(t-a)alpha_l is an integer with magnitude <=H-1. It follows that |t-a|<=H(H-1). As a belongs to [1,H], t lies in (3).

Conversely, the length-H intervals [Hq+1,Hq+H] for integers q=-(H-1),...,H-1 tile exactly the interval (3). Write t=a+Hq with 1<=a<=H and |q|<=H-1. For any n>=3, construct C with v=(H,...,H)^T, A the all-ones m x m matrix, a as above, b_1=1+max(q,0), and all other b entries 1. Take alpha=(1/H,0,...,0)^T. Define A'=A+v alpha^T (the first column becomes all 2) and b'=b-Hq alpha (so b'_1=1+max(-q,0)); keep v and a unchanged. Both matrices lie in the alphabet, are distinct, and are exactly equivalent by BP1. This proves BP2.

4. For t outside (3), every difference polynomial Q=F_C-F_C' is nonconstant by BP1–BP2. Fix rho>=0, put M=floor(2rho), and N=H^{n^2}. For every unordered candidate pair and every integer k in [-M,M], Q-k is nonzero over Z. Choose a prime p larger than 2M+1 and larger than the absolute values of all nonzero coefficients of this finite polynomial family. Every Q-k remains a nonzero polynomial over F_p of total degree <=m. If independent controls are drawn uniformly from F_p, Schwartz–Zippel plus the union bound gives

    P(any collision at circular difference in [-M,M])
       <= m(2M+1) binom(N,2)/p.

Choosing a prime p>4m(2M+1)binom(N,2) makes this probability <1/4. Some single setting then gives pairwise circular integer distance >=M+1>2rho. The closed error balls are disjoint; table lookup or nearest residue recovers C. In (3), BP2 supplies exact indistinguishability for any controls and any rho. This proves BP3.

## Exact finite evidence

A companion standard-library Python checker evaluates (1) by integer determinants for each binary diagonal x in {0,1}^m and records all g components and F(x,0). Because the polynomials are multi-affine in x, these evaluation tables determine all coefficients exactly; z is handled by its explicit linear coefficients g. It enumerates all 512 matrices at n=3,H=2 for t=-2,-1,0,4,5 and all 65,536 matrices at n=4,H=2 for t=-2,0,5, detecting distinct symbolic response signatures, plus seven explicit rank-one witnesses with larger n or H.

Verified unique signature counts:
- n=3, H=2: t=-2:512; t=-1:497; t=0:482; t=4:497; t=5:512.
- n=4, H=2: t=-2:65536; t=0:64094; t=5:65536.

All seven gauge witnesses satisfy exact identity of their full polynomial signatures. These are finite checks of the proofs, not substitutes for the universal algebraic argument. The checker and evidence preserve the candidate order, evaluation convention and tested ranges. Review status remains NOT_REVIEWED.

## Information/observer fidelity and next questions

The rank-one transformation is an **exact fibre** of the declared root-frozen Port observer. It cannot be silently quotiented when the experiment later varies d_0, switches to a different Port geometry, exposes native X6 relations or tracks provenance. This is an application of the project's observer/future-operation preservation discipline, not an assertion that a signed determinant implements a native heartbeat event.

Next: classify the leaf-frozen n>=4 fibres (which may have nonzero constant separation), sharpen the least p and control magnitude for n>=4 with root t=H^2+1, and explore a decoder exploiting the rank-one gauge quotient rather than an H^{n^2} lookup table.

Author provenance: continuation of R284BO in the historical R1 portable research line EM-DIRECT-E6B1DD; no claim to current authenticated execution session or CLAIM, formal Source Result, independent review or Working Truth admission.
