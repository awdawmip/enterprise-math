# Blind square-class compatibility and bounded RR reduction

Status: exact partial reduction with two excluded subfamilies. No degree-six map, completed RR system, period normalization or terminal verdict is claimed. This is not the task's final raw freeze.

Researcher: EM-HODGEH0O-82EF42. Actual claim: `chatgpt-rb-blind-20260908-1943ccc582e1463bbcef0c6ab3c7db1b`. The task remains the canonical RB blind branch-pattern completion task, with unchanged TP2 and ER. This continues the six-file assignment checkpoint, reported published by the owner at `b8c4fb6c8e86080699c67b65b863e1ce791f1263`.

Only the two whitelisted mathematical sources at `c73816d3552b4247861e12e476101e94a4a2ce5a` and our own preceding blind output are used. Their whole-file SHA256 values are fixed by `source_binding.json` (`516400d46ae5dd5a8aa2d25520021ee3a57dc839538746a550ad2a7bfae2a473`). The assignment certificate SHA256 is `a83524c6b9b8cb6e00561c014e7129c614e9b1c46eedcbd9c9e79f2ff5ee89a0`. No catalog, originating map, coefficients, basepoint, twist, period, replay, research journal or targeted external search was opened.

## 1. Scope and field

Use the curve C: t^2=R^3-3R with origin O, and F=(R+2)t, so D is w^2=F. Let B be the reduced divisor consisting of O, the other three two-torsion points, and Pplus/Pminus. Direct divisor calculation gives

div(F)=B-6[O].

The statements about four unramified square classes are geometric: they are over an algebraic closure of the task's coefficient field, or modulo constant square classes after appropriate algebraic extension. They do not prove descent to the original field. Chosen halves of points below are formal algebraic choices, not evaluated roots. Nonzero constant factors are retained explicitly. None of the paper's symbolic quotients is a new native numerical division implementation.

Every retained assignment has an empty special fiber. A target V4 translation can send one such fiber to infinity while keeping the fixed lambda and the differential. The new certificate records the actual V4 label permutation for every one of the 45 or 90 previously retained fixed-parameter assignments. Where there are two empty fibers, the remaining equivalence is resolved by a deterministic representative inside the same V4 orbit. No source-sign or semilinear quotient is added.

Write S_0,S_1,S_lambda for the three finite branch blocks, allowing an empty block. They partition B. The pole divisor of X is 2D_infinity, where D_infinity is an effective divisor of degree three, disjoint from B. The permitted local ramification statement therefore gives

div(X-a)=S_a+2E_a-2D_infinity,

where E_a is effective of degree 3-|S_a|/2. At a branch point in S_a the local multiplicity is exactly one, so E_a cannot include that point. Additional local and exact-pole conditions must be retained when solving the equations below.

## 2. Explicit geometric square-class representatives

For any pair of distinct branch points U,V, choose a point Q with 2Q=U+V. Let ell_UV be their chord and ell_Q the tangent at Q, both interpreted as rational line sections in the standard plane cubic embedding. Their third intersection is the same point -(U+V). Thus

g_UV=ell_UV/ell_Q,

div(g_UV)=[U]+[V]-2[Q].

This includes the vertical-line cases. If one point is O, use its projective chord; if Q=O, the tangent at infinity is the constant rational section 1. No distinct-branch-point assumption is lost. The four possible halves of U+V differ by two-torsion. One chosen half suffices to specify a base representative; changing it permutes the geometric twist labels and may change a nonzero constant factor.

For 4+2+0, let p label the two-point block, q the four-point block and z the empty finite block. Set

G_p=g_pair, G_q=F/g_pair, G_z=1.

Writing div(G_a)=S_a-2B_a, the corresponding integral divisors are

B_p=[Q], B_q=3[O]-[Q], B_z=0.

For 2+2+2, choose base pair representatives for labels 0 and 1 with half-points Q_0,Q_1, and put

G_0=g_pair0, G_1=g_pair1, G_lambda=F/(g_pair0*g_pair1).

Then

B_0=[Q_0], B_1=[Q_1], B_lambda=3[O]-[Q_0]-[Q_1].

In either case, G_0 G_1 G_lambda=F exactly, and the sum of the B_a is exactly 3[O]. The B_a need not be effective. Their degrees, which are what the RR dimensions use, are |S_a|/2.

Let s be the formal generator with s^2=3. The four unramified geometric square classes are represented by

gamma_O=1, gamma_T0=R, gamma_Tplus=R-s, gamma_Tminus=R+s.

Indeed div(gamma_T)=2[T]-2[O], and R(R-s)(R+s)=t^2. Conversely, if a nonzero function has an even divisor, its half-divisor has degree zero and two-torsion divisor class. Removing the appropriate gamma_T leaves a principal half-divisor and hence a square up to a nonzero constant. This proves coverage, rather than merely exhibiting four examples.

All functions with odd support S_a consequently have form

X-a=alpha_a G_a gamma_Ta u_a^2,

with alpha_a nonzero constants and u_a nonzero rational functions over the chosen algebraic field. Set B'_a=B_a+[O]-[T_a], so div(G_a gamma_Ta)=S_a-2B'_a.

## 3. The actual 16-way compatibility restriction

The prescribed source double cover imposes

A X(X-1)(X-lambda)=F H^2,

with nonzero A. Since the base G product is F, this is possible geometrically only when

T_0+T_1+T_lambda=O.

It is also sufficient for the product square-class condition, apart from the explicitly retained constant square factor. Of the 64 triples of two-torsion labels, exactly 16 satisfy this condition. Choose T_0 and T_1 freely and set T_lambda=T_0+T_1. The other 48 geometric twist triples are excluded; constants cannot repair their nontrivial unramified class.

For every allowed triple the product of the three gamma factors has the explicit square root h_T as a formal rational function:

- all three labels O: h_T=1;
- two equal nonzero labels and one O: h_T=that gamma;
- the three distinct nonzero labels: h_T=t.

The integer polynomial checker verifies all 16 identities using only s^2=3 and t^2=R^3-3R. There are 720 or 1440 assignment-plus-geometric-twist components, respectively. These are components of a remaining parameter problem, not 2160 maps or 2160 solvable systems. Arithmetic constant square classes and descent are not counted as solved finite data.

## 4. Minimal RR dimensions and the remaining exact equations

The factorization in section 2 implies

div(u_a)=E_a-D_infinity+B'_a.

Thus u_a belongs to L(D_infinity-B'_a). On a genus-one curve every divisor of positive degree d has h^0=d: by RR, h^0(D)-h^0(-D)=d, and a negative-degree divisor has no nonzero section. Therefore the respective dimensions are exactly

| Branch block size | Degree and dimension of its u space |
| --- | ---: |
| 4 | 1 |
| 2 | 2 |
| 0 | 3 |

Both patterns require a total of six RR section coefficients: (1,2,3), in the label order dictated by the assignment, or (2,2,2). This is a basis-dimension theorem, not an evaluated basis or a solved coefficient system.

The two required function identities are

alpha_0 G_0 gamma_T0 u_0^2 - alpha_1 G_1 gamma_T1 u_1^2 = 1,

alpha_0 G_0 gamma_T0 u_0^2 - alpha_lambda G_lambda gamma_Tlambda u_lambda^2 = lambda.

Both sides lie in L(2D_infinity), which has dimension six. With an actual basis, each identity is six coefficient equations. One must impose the exact degree-six pole divisor, the prescribed simple multiplicity at each S_a, nonzero constants, and the absence of common cancellation; dropping these conditions would admit degenerate lower-degree candidates.

For clarity, the variable D_infinity has not silently been replaced by 3[O]. Write S for its degree-three divisor class parameter, so D_infinity is linearly equivalent to 2[O]+[S]. If d has divisor D_infinity-2[O]-[S], then d is a section of L(2[O]+[S]) and v_a=d*u_a is a section of L(2[O]+[S]-B'_a). The same equations, multiplied by d^2, read

alpha_0 G_0 gamma_T0 v_0^2-alpha_1 G_1 gamma_T1 v_1^2=d^2,

alpha_0 G_0 gamma_T0 v_0^2-alpha_lambda G_lambda gamma_Tlambda v_lambda^2=lambda*d^2.

This supplies an equivalent bounded parameterization: one elliptic class parameter S, three denominator-section coefficients, and the six numerator square-root-section coefficients, together with the constant factors and the fixed geometric twist choice. The exact degree and local saturation conditions still apply. No assumption S=O is made in the full system.

Because the gamma product is h_T^2, choose a nonzero constant eta with eta^2=A*alpha_0*alpha_1*alpha_lambda when such a choice exists over the field being considered. Then H=eta*h_T*u_0*u_1*u_lambda. The independent differential constraint becomes

delta X=beta*h_T*(t+k)*u_0*u_1*u_lambda,

with nonzero beta=c*eta and delta=t*d/dR. In denominator-cleared form one may use the integer derivation 2delta. This equation, descent, basepoint data and the absolute period normalization remain unsolved gates. The square-class product alone does not imply them.

## 5. Exclusion of the R-only ansatz

A nonconstant X in K(R) cannot satisfy the fixed-k ODE. In the basis {1,t} over K(R), its left side F(delta X)^2 is odd in t. The even coefficient of the right side is

K*(R^3-3R+k^2)*X(X-1)(X-lambda),

which is nonzero in the function field for nonzero K and nonconstant X. This contradiction does not exclude any branch assignment merely because its six labels happen to be invariant under source sign. An invariant assignment does not force its map to lie in K(R).

## 6. A genuine RR subfamily exclusion

Assume the 4+2 pattern, a finite empty special fiber at e, and a geometrically trivial square class for X-e. Over the algebraic closure we may write X=e+g^2, absorbing a nonzero constant symbolically. The degree-six condition gives deg(g)=3.

Further suppose the degree-three pole divisor of g is linearly equivalent to 3[O]. This is a restriction on this subfamily only. It yields

g=(a*t+b*R+c)/(d*t+e1*R+f),

with independent numerator and denominator in L(3[O])=<1,R,t>. In the checked polynomial identities e1 is named e; it is a coefficient and is not the special value denoted e above. These two sections have no common zero as sections of this degree-three line bundle, since g has degree exactly three.

Let Q be any of the three allowed points with t=-k. By the frozen reduction, Q is not a double-cover branch point, the two lifts on D are simple zeros of the given differential, and a valid pullback has ramification index two there. Thus X has local degree two at Q if its value is not a target branch value, and local degree four if its value is a target branch value. All possibilities for g must be treated:

- If g(Q)=0, then X=e, so local degree of X is twice that of g; hence g has local degree two.
- If g has a pole at Q, the same statement holds at infinity; g again has local degree two.
- If g(Q) is finite and nonzero, the map z -> e+z^2 is unramified there. An ordinary X value forces local degree two for g. Any remaining target branch value would force local degree four for g, which is impossible for a degree-three map.

Consequently every surviving possibility requires all three Q to be critical points of g. This argument uses local degrees, not the unsafe assertion that a displayed derivative vanishes despite possible denominator cancellation.

Put A1=a*e1-b*d, B1=a*f-c*d and C1=b*f-c*e1. For the numerator N and denominator L, direct integer polynomial differentiation in t^2=R^3-3R gives

(2delta N)*L-N*(2delta L)
= A1*(R^3+3R)+3*B1*(R^2-1)+2*C1*t.

At a finite Q where L is nonzero, criticality makes this numerator vanish. At a pole of order at least two, L vanishes to that order while N is nonzero in the local section frame; the same numerator has positive order and still vanishes. There is no common section zero. The vector field delta is nonvanishing at Q because t=-k is nonzero.

The three distinct R coordinates of Q satisfy R^3-3R-k^2=0. Restricting the displayed numerator to that divisor gives the quadratic

3*B1*R^2+6*A1*R+(A1*k^2-3*B1-2*C1*k).

A quadratic vanishing at three distinct points is zero. Characteristic zero and k!=0 imply B1=A1=C1=0. All two-by-two minors of the numerator/denominator coefficient rows vanish, so the rows are dependent and g is constant. This contradicts deg(g)=3.

The conclusion is exactly this subfamily exclusion. It does not remove any of the 45 or 90 assignment components, nor nontrivial unramified square classes, nor general pole line-bundle classes. No descent to the original field has been inferred.

## 7. Actual checks and remaining frontier

The new checker `check_squareclass_rr.py` reads the frozen assignment JSON and source binding. It does not rerun the historical checker or the preceding assignment search. It records an empty-infinity V4 representative for each component, verifies the 16 formal gamma identities, and checks both the cleared derivative numerator identity and its restriction to the Q divisor by integer polynomial rewriting.

The actual first run produced `squareclass_rr_certificate.json` with SHA256 `e5fd0f12abaf11201de208daaf8c7d526aa077a764d3a522b6f38a0c8b7476e6`, with counts 720 and 1440 and no RR/ODE solution claim. The selected static V2 gate passed for this one new checker. No division, remainder, root, rational-function value or BRC evaluation occurred. Integer formal algebra is the execution boundary; the local-degree and RR arguments above are paper proofs.

Before publication, owner review found that this draft had reversed all four displayed RR differences while leaving their right sides positive. The first checker did not validate these printed signs. The old full publication manifest, paper and execution evidence are preserved as a rejected draft, not a successful mathematical review. The four formulas above now use X-(X-a)=a. A new actual integer-polynomial regression checks this identity for constant and symbolic shifts, its denominator-cleared form, and the failure of the old reversed direction. The revised certificate SHA256 is `d861e5b4d9d5b562c7e2a972c56b30144f2cd41275963f80a3aa80c5f1d3a289`; five focused tests passed. This correction does not change the 16-way compatibility or the independent critical-point exclusion identities.

Remaining work is explicit: solve or exclude the surviving bounded section identities with the ODE and the exact local conditions, without fixing the pole class to O; then establish descent, actual X/Y, basepoint and period data if a map is found. The full six-point-block exclusion remains the earlier cited premise. No task raw freeze, unblinding, full reconstruction, no-go theorem for both patterns, or period verdict is declared by this checkpoint.
