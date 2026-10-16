# The highest first-gap coefficient and a scalar compensation boundary

AUTHOR ADDENDUM, UNREVIEWED NEW SCOPE. EM-DVR-BFF6DC authors the highest-first-gap sign proof. EM-DVR-F73673 contributes the subsequent overlapping scalar-boundary refinement identified below. Neither can independently approve this combined unit. This follows the distinct original three-member c1 interface, actually archived at Source ac9f1c0ffcfbb7ad5564721442480ad8e2236b83. Its genuine peer accepted only the bounded identity before the new contribution exposure, not the sign assertions developed here. No extension of that frozen review is assumed.

This proof uses no scientific program, symbolic expansion by a program, sample, solver or parameter scan. It is a paper derivation. The permanent m7 fixed-certificate STOP, all old resource contracts, and current formal Task ownership remain untouched.

## 1. Result and its limits

Retain m>=2, n=m-1, W=m^2, r0=mS, L=ma, r=r0+L, with S>=0 and a>0. Let H(L), T(c), the specified COMMON denominator D_c and the polynomial P(c)=D_c T(c)/c be exactly those of the archived c1 interface. Write P1(S,a)=[c]P(c).

Explicitly, H=G_L^T D(r0+L)G_L with the frame and metric in Section 2,
T(c)=tr(H(L+mc)^(-1)H(L))-n,
x=m(r0+L), beta=(W+1)/2, G_W(x)=product_(k=1)^W(x+k),
D_c=(x+Wc+beta)G_W(x).
The old source and original interface prove this P is polynomial; the present argument retains that exact denominator rather than silently canceling another factor.

The author theorem proved below is:

For every m>=2, P1 is a polynomial in a of degree exactly W-1, with leading coefficient C_m independent of S, and

C_m >= (m^(2W+2)/2)(W-1)(m+2) > 0.                 (A)

Consequently, for each fixed S>=0, P1(S,a)>0 for every sufficiently large a. No effective threshold uniform in S or m is supplied. This is one positive extreme monomial coefficient of the next face. It is NOT coefficientwise positivity of P1, full pointwise positivity, a trace certificate, a higher-face induction or a completion of the existing tangent-face Task or Goal. It concerns the fixed common denominator, not a numerator after arbitrary nonconstant gcd cancellation.

The new content to be reviewed is the limiting parity-definite Gram structure and the use of that structure for (A). Ordinary finite differences, a rational change of residue coordinate, positive Gram matrices and the real symmetric spectral theorem are reused without general-method novelty claims. The previously checked inputs were not found to state (A); this is a bounded comparison, not a repository-wide novelty assertion.

## 2. An exact leading Gram matrix

For 1<=j<=n and nodes X_i=r0+(i+1)/m, use the original frame

G_L[i,j]=((X_i+L)_j-(X_i)_j)/(j! L).

Let t=1/L and u=tX_i. Put

g_j(u,t)={product_(h=0)^(j-1)(u+1+ht)-product_(h=0)^(j-1)(u+ht)}/j!,
p_j(u)=g_j(u,0)=((u+1)^j-u^j)/j!.

Then G_L[i,j]=L^(j-1) g_j(tX_i,t). The original Beta metric is exactly

d_i=(w_i n!/m)L^(-m) product_(h=0)^(m-1)(1+tX_i+ht)^(-1),
w_i=(-1)^i binom(n,i).

For fixed r0, define the analytic germ near (u,t)=(0,0)

f_jk(u,t)=g_j(u,t)g_k(u,t) product_(h=0)^(m-1)(1+u+ht)^(-1).

Thus

H_jk(L)=(n!/m)L^(j+k-2-m) sum_(i=0)^n w_i f_jk(tX_i,t).       (B)

Expand only as a formal analytic argument, f_jk(u,t)=sum_(q,b)>=0 A_qb u^q t^b. The elementary finite-difference identities give

sum_i w_i X_i^q=0 for q<n,
sum_i w_i X_i^n=(-1)^n n!/m^n.

The first possible nonzero power in the sum in (B) is therefore t^n. At that order only q=n,b=0 survives: every q<n term vanishes, including the terms with b>0. It follows that

H_jk(L)=L^(j+k-2m-1)(M_jk+O(1/L)),

M_jk=kappa [u^(m-1)]{(1+u)^(-m)p_j(u)p_k(u)},
kappa=(-1)^(m-1)((m-1)!)^2/m^m.                         (C)

The error is the Taylor remainder of a germ analytic in t after factoring t^n. In particular, the rescaled matrix below is analytic at t=0 and its derivative may be controlled there; no unjustified differentiation of a bare asymptotic O-symbol is used. The coefficient in (C) is independent of r0 and hence of S.

For an entirely finite formula, adopt binom(z,q)=0 for q<0 and the ordinary generalized-binomial convention for q>=0. Then M_jk equals kappa/(j!k!) times

binom(j+k-m,m-1)
-binom(k-m,m-1-j)
-binom(j-m,m-1-k)
+binom(-m,m-1-j-k).                                    (D)

No numerical evaluation of this matrix is used.

## 3. Its parity blocks are definite

Write C_jk=M_jk/kappa. The coefficient in (C) is the residue at u=0 of

p_j(u)p_k(u) du/[u^m(1+u)^m].

Under v=u/(1+u), this becomes the residue at v=0 of the Laurent polynomial

v^(-m)(1-v)^(2m-j-k-2)(1-v^j)(1-v^k) dv/(j!k!).        (E)

The exponent 2m-j-k-2 is nonnegative because j,k<=m-1. Its residue can be extracted by integrating on |v|=1; (E) has no pole on that circle. With v=exp(i theta), the exponential phases cancel and give

C_jk=((-2i)^(2m-j-k)/(2pi j!k!))
      integral_0^(2pi) sin(theta/2)^(2m-j-k-2)
      sin(j theta/2)sin(k theta/2) dtheta.              (F)

If j+k is odd, the real integral changes sign under theta -> 2pi-theta, so it vanishes. Thus M has separate odd-j and even-j blocks.

Within one parity p in {0,1}, define epsilon_j=(-1)^((j-p)/2) and

f_j(theta)=2^(m-j) sin(j theta/2)/(j! sin(theta/2)^j).

Multiplication of (F) by kappa yields

M_jk=(-1)^(p+1) |kappa| epsilon_j epsilon_k
      (1/(2pi)) integral_0^(2pi) sin(theta/2)^(2m-2)
      f_j(theta)f_k(theta) dtheta                       (G)

for j,k of parity p. Every integrand is integrable at the endpoints: its possible singularity is canceled to order at least two because j+k<=2m-2.

The functions f_j in either parity block are linearly independent. Indeed, for z=theta/2,

sin(jz)/sin(z)^j=Im(cot(z)+i)^j

is a real polynomial in cot z of degree j-1 with nonzero leading coefficient j. Distinct j have distinct degrees. A nonzero linear combination cannot vanish on (0,pi), where cot z ranges over the real line. The weight in (G) is strictly positive in the interior, so each displayed Gram block is positive definite before its explicit sign and diagonal epsilon congruence.

It follows that M is nonsingular; its odd-j block is positive definite and its even-j block is negative definite. This is a statement about this EXACT limiting matrix, not about a generic indefinite metric or the finite-L logarithmic derivative.

## 4. The limiting logarithmic derivative retains the variable-frame terms

Let alpha_j=j-m-1/2, C_L=diag(L^alpha_j), and A_L=C_L^(-1)H(L)C_L^(-1). Equations (B)-(C) show

A_L=M+O(1/L), with A_L analytic in 1/L near zero.

Hence A_L is invertible for sufficiently large positive L and L A_L'=O(1/L). Set D_alpha=diag(alpha_j). With K=H^(-1)H', direct differentiation of H=C_L A_L C_L gives

L C_L K C_L^(-1)
=A_L^(-1) D_alpha A_L+D_alpha+L A_L^(-1)A_L'
-> R=M^(-1) D_alpha M+D_alpha.                                    (H)

Both derivatives of the variable congruence C_L are present. It would be incorrect simply to replace K by A_L^(-1)A_L'.

M and D_alpha preserve the odd/even coordinate blocks. Within each block, R is self-adjoint for M because R^T M=M R. Changing the sign of the negative block makes its metric positive definite without changing self-adjointness. Therefore R has only real eigenvalues. This definite-block argument applies only to R; it does not assert real spectrum or nonnegative squared trace for the actual finite-L Omega/K of the earlier paper.

Writing n=m-1, the trace is

tr R=2 sum_(j=1)^n alpha_j=-(m^2-1)=-(W-1).

The elementary inequality for its n real eigenvalues consequently gives

tr(R^2)>=(tr R)^2/n=(W-1)^2/(m-1).                   (I)

Equation (H) also proves the exact asymptotic statistic

lim_(L->infinity) L^2 tr(K(L)^2)=tr(R^2).              (J)

It follows from the analytic matrix limit and similarity invariance of trace. No spectral continuity assertion for the finite-L matrices is needed.

## 5. Convert this to the actual highest-a coefficient

The already archived c1 identity is

P1=(W/2)(x+beta)G_W(x)
    [tr(K^2)+W(2ell(x)/(x+beta)-h2(x))],
x=m(r0+L), beta=(W+1)/2.

The old finite rational sums imply

lim_(x->infinity) x ell(x)=W-1,
lim_(x->infinity) x^2 h2(x)=W-1,
lim_(x->infinity) x^2[2ell(x)/(x+beta)-h2(x)]=W-1.

Since x/L->m and G_W(x)/x^W->1, (J) yields

lim_(L->infinity) P1/L^(W-1)
=(m^(W+3)/2)[tr(R^2)+W-1].

As L=ma, the leading coefficient in a is therefore exactly

C_m=(m^(2W+2)/2)[tr(R^2)+W-1].                       (K)

Combining (I) with W-1=(m-1)(m+1) gives

tr(R^2)+W-1 >= (W-1)(m+2)>0,

which proves the bound (A).

Polynomiality of P1 was established from the old whole-trace common denominator before this argument. For each fixed S>=0, the finite strictly positive limit in (K) therefore proves its a-degree is exactly W-1. The limit is independent of S. Since every a-coefficient is a polynomial in S, equality for the interval S>=0 also identifies the formal leading coefficient as the same constant C_m and makes every possible higher a-coefficient identically zero. No bound on the total joint degree in (S,a) is needed or asserted here.

## 6. The same scalar correction needs actual compensation

This is one complementary boundary check for the same c1 formula, not another research discovery. BFF6DC had already proved q_W negative near zero for m>=4 and eventually positive in a separate 2824-byte working note. F736 independently developed the same obstruction with the improved range m>=3 and an h2 bound after freezing the original c1 review. The overlap was then identified and the two original working notes exchanged. Their contributions are merged here; the old review is unchanged, and F736 is a contributor to this combined addendum.

Put b=x+beta and q_W(x)=2ell(x)/b-h2(x). The elementary convexity of t -> 1/(x+t)^2 on [1,W] gives

h2(x)>= (W-1)/b^2>0.

This bound does not help by dropping the term, since the original formula subtracts W h2. More precisely, write H_W=sum_(k=1)^W 1/k and H_W^(2)=sum_(k=1)^W 1/k^2. At x=0 the exact scalar expression is

q_W(0)=4H_W/(W+1)-H_W^(2)-4/(W+1)^2.

For integers N>=2, H_N/(N+1) strictly decreases: its next-step difference has numerator 1-H_N<0. Consequently W>=9 implies

4H_W/(W+1)<=4H_9/10=7129/6300,
H_W^(2)>=1+1/4+1/9=49/36,
q_W(0)<=-241/1050-4/(W+1)^2<0.

Continuity gives a nonempty positive-x interval with q_W<0 for every m>=3. Choosing S=0,a=x/W>0 places it in the physical domain; the conclusion is not at an inadmissible zero first gap. Section 5 also gave x^2q_W(x)->W-1>0, so q_W is eventually positive. No zero count or explicit interval length is asserted.

Thus one cannot prove the full P1 sign by treating its scalar correction as separately nonnegative. On the displayed small-x interval, pointwise P1>=0 is equivalent to the actual compensation tr(Omega^2)>=-Wq_W(x)>0. No such bound is proved here. This is not a negative P1 example or a coefficientwise counterexample. It does not interact with the highest-a proof: that proof uses only the large-x finite-sum limit and the new limiting Gram argument, not this small-x estimate.

## 7. Boundary and contribution

The candidate resolves exactly one all-m coefficient: the top a monomial of P1 for the specified common denominator. All lower a-coefficients, including mixed S powers, can still have unresolved signs. The conclusion does not give a uniform large-a threshold and does not infer coefficientwise positivity from eventual pointwise positivity.

The checked old M6 source reports full-parameter certificates for m=3,...,6, covering those finite dimensions more strongly. Those reports are used only for bounded dedup here, not substituted for a new primary proof input. No new fixed-m certificate is claimed. The new target here is one dimension-free boundary coefficient. The old small-c theorem and fixed-gap moment/Horner results are retained; neither is rerun. No program budget, Task ID, scientific consumer, Native review, shared Tool or parent status is changed.

BFF6DC authored the limiting parity argument and its coefficient application before consuming the later F736 scalar working note. F736 contributed the small-x improvement and Jensen bound in Section 6, not the limiting Gram proof or an author repair of it. Both retain all previous Driver/reviewer/CONTROL exposure and are contributors to this combined unit. Root identified the overlapping scalar work and requested honest merging; Root supplied neither mathematical construction. A third genuine nonauthor must examine this complete new proof and its exact limits after freeze, including whether an existing source already gives an equivalent coefficient result. The original F736 review was frozen before this new contribution exposure and remains valid for its original scope only.

Exact proof input: Source ac9f1c0ffcfbb7ad5564721442480ad8e2236b83, path research_notes/owner_goal_20261016/p11_independent_native_driver/parity_all_m_c1_curvature_author/PARITY_ALL_M_C1_FACE_INVERSE_FREE_CURVATURE_OBSERVER_AUTHOR.md, 13131 bytes, SHA256 1b0a3105eadb9e3dc59f12183b5dcc7a0bc28417e1707031d363d8f1c6902908. The original eleven Source dependencies, three-file actual publication gate and both local scalar working notes are fully pinned in the accompanying context. The scalar notes are local frozen input artifacts, not falsely described as already Source-published primary papers. No new third-party theorem requiring an unread primary has been imported: the finite-difference, Laurent coefficient integral, positive Gram, and real symmetric spectral steps are explicitly derived above.
