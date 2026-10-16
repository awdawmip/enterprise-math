# One Parity lower mixed coefficient: centered negative, original-variable positive

Status: `FROZEN_JOINT_AUTHOR_PAPER_CANDIDATE / UNREVIEWED`.

Authors: EM-DVR-BFF6DC and EM-DVR-F73673. This is one bounded derived coefficient application of the existing Parity P1 interface. It is not a new generic method, a third version of the completed top-face/tail result, a new Tool or Task, or an execution of any computational branch. The scientific-program count is zero. Both authors contributed to this proof and cannot independently review it. A genuinely different whole-paper reviewer is required after the entire manuscript and context have been frozen.

## 1. The specified polynomial and the one selected question

Retain the original finite-algebra model: m is an integer, n=m-1, r0=mS, L=ma, r=r0+L, with physical parameters S>=0 and a>0. The original normalized secant Gram matrix is H(L). For a second gap c the source defect is

T(c)=tr(H(L+mc)^(-1)H(L))-n.

Write W=m^2, beta=(W+1)/2, x=mr=W(S+a), and G_W(x)=product_(k=1)^W(x+k). Fix the SAME COMMON normalization as the original c1 paper:

P(c)=(x+Wc+beta)G_W(x)T(c)/c,   P1=[c]P(c).

The original source proves polynomiality of this specified P and P1. We do not replace P by an arbitrarily gcd-reduced numerator. Its exact c1 identity is

P1=(W/2)(x+beta)G_W(x)[tr(K^2)+Wq_W(x)],
K=H^(-1)H', q_W=2ell/(x+beta)-h2,
ell=sum_(k=1)^W1/(x+k)-1/(x+beta),
h2=sum_(k=1)^W1/(x+k)^2-1/(x+beta)^2.

The prime in K differentiates L while holding r0 fixed. It does not differentiate at fixed first-gap ratio. The original inverse-free curvature formula and its actual secant frame supply this identity; the present proof evaluates one further polynomial coefficient, rather than introducing a new inverse-elimination mechanism.

Set h=beta/W, D=W-1, p=W-3, and Q_m(sigma,a)=P1(sigma-h,a). The completed top-face result already gives total degree D. The selected first free centered lower mixed coefficient, and its original-variable counterpart, are

C_m=[sigma^(W-4) a]Q_m(sigma,a),
C_m^S=[S^(W-4) a]P1(S,a).

Both have total degree D-2. All conclusions below concern integer m>=7. Old complete m=2,...,6 coefficient results are not counted again; the stable-degree trace table below must not be continued into an absent low-dimensional polynomial space.

**Theorem proposed for whole-paper review.** Let K_pref=m^(2W)/2. Then

C_m=K_pref (m^4-1)/(432m) P_m <0,
P_m=-27m^6-7m^5+228m^4-83m^3-429m^2+252m+72,                  (1)

C_m^S=K_pref (m^4-1)/(432m) U_m >0,
U_m=81m^8+21m^7-387m^6-91m^5+453m^4-62m^3+21m^2+378m-144.

This is one coefficient read in two specified bases, not two discoveries. The negative centered coefficient rules out a centered coefficientwise-positive-remainder shortcut. The positive original-variable coefficient quantifies the exact compensating contribution of the previously known top layer. Neither sign determines all lower coefficients, the sign of P1 on the physical domain, positivity of T(c), a numerical tail threshold, or the all-M Goal.

The proof does not assume the parked global-reflection working as an independently accepted theorem. The centered metric and scalar germs below establish the parity needed for this P1 calculation directly. The native Heartbeat-X6 spatial basis and original observer contracts remain fixed; sigma, the residue variable u, and the auxiliary finite-dimensional polynomial carrier are separately typed algebraic parameters. No continuum geometry, physical extra dimension, or propagation law is inferred from them. Static coefficient extraction needs no new physical-time coordinate.

## 2. The common second-germ readout, including all normalizations

Put r=m(S+a), rho=r+beta/m=m(sigma+a), L=ma, lambda=L/rho=a/(sigma+a). Use V=Q[u]_(degree<=m-2). In the fixed monomial evaluation frame the centered metric is

Q_rho[j,k]=(n!/m) sum_(i=0)^n (-1)^i binom(n,i) xi_i^(j+k)
              / product_(h=0)^n(rho+xi_i+eta_h),

xi_i=(i-n/2)/m, eta_h=h-n/2, 0<=j,k<=m-2.

With C_rho=diag(rho^(j-m+1/2)), write Q_rho=C_rho A_rho C_rho. For d=j+k,

A_rho=M+rho^(-2)T+O(rho^(-4)),
M_jk=kappa binom(-m,n-d),
T_jk=kappa delta [binom(-m,n+2-d)+W binom(-m-2,n-d)],
kappa=(-1)^n(n!)^2/m^m, delta=(m^2-1)/(24m).              (2)

Negative lower binomial indices mean zero. The centered finite-difference generating function is (-1)^n(2sinh(z/(2m)))^n. Its moments below n vanish, its odd excess moments vanish, and mu_(n+2)/mu_n=delta. The reciprocal Beta product has its order-two correction sum eta_h^2/2=W delta. This gives both terms in T. The exact node reflection gives Q_(-rho)[j,k]=(-1)^(j+k+1)Q_rho[j,k]; after the integer scaling A_jk=rho^(2m-1-j-k)Q_jk, A is even. Thus no missing order-one or order-three germ term is being assumed. This is a finite analytic paper expansion, with no generated coefficient artifact or program.

Let J=d/du, D_alpha=diag(j-m+1/2), Z_lambda=D_alpha+gamma_lambda(J), and use the M-adjoint star. The finite frame polynomial from the earlier V2 proof has

gamma_lambda(J)=J/2+lambda J^2/12+O(lambda^3).

At lambda=0 set

Z=(u+1/2)J-(m-1/2)I, R=Z+Z*, U=J^2, B=M^(-1)T.

The logarithmic derivative is differentiated at fixed original r0, before the centered scaling. Here is the exact frame step, retained from the actual secant model. In the fixed centered polynomial frame write Hbar=F_L(J)^T Q_rho F_L(J), where F_L(J)=sum L^k J^k/(k+1)! is the finite derivative-average polynomial and Gamma_L=F_L' F_L^(-1). The original secant frame differs by a matrix depending on r0 but not L, so this is a legitimate constant congruence for the required derivative. Direct differentiation gives F_L Kbar F_L^(-1)=Gamma_L+Q_rho^(-1)Gamma_L^T Q_rho+Q_rho^(-1)Q_rho'. The exact identity C_rho J C_rho^(-1)=J/rho then makes rho K similar to Z_lambda+A_rho^(-1)Z_lambda^T A_rho+rho A_rho^(-1)A_rho'. The inverse F_L(J)^(-1) used to construct Gamma_L is a terminating polynomial because F_L-I is nilpotent. No inverse of Gamma_L is used. Substitution lambda=L/rho takes place only after this derivative, so no derivative at fixed lambda is substituted. Inserting the analytic even germ and its derivative gives the expansion of this similar representative:

Khat_rho=R_lambda+rho^(-2)([Z_lambda*,B]-2B)+O(rho^(-4)),
tr(Khat_rho^2)=rho^2 tr(K^2).

The -2B is the differentiated second germ; dropping the moving frame or this term changes the question. Put g=(W^2-1)/24. The centered scalar block has

G_W(x)=(m rho)^W[1-Wg/(m rho)^2+O(rho^(-4))],
q_W(x)=(W-1)/(m rho)^2-2Wg/(m rho)^4+O(rho^(-6)).

Here q=2ell/(x+beta)-h2 with the original ell=sum1/(x+k)-1/(x+beta) and h2=sum1/(x+k)^2-1/(x+beta)^2. Inserting the original exact P1 formula yields the total-degree p layer

(m^(2W)/2)(sigma+a)^p F(lambda),
F(lambda)=2tr(R_lambda([Z_lambda*,B]-2B))
             -g[tr(R_lambda^2)+W+1].                       (3)

Consequently the selected coefficient is exactly

C_m=(m^(2W)/2)[pF(0)+F'(0)].                              (4)

The factor 1/2 and the term W+1 are retained. At m=2, the common readout, without the stable-degree trace table below, reduces to the already covered scalar polynomial 6144(sigma+a)^3-160(sigma+a). This is a normalization check only.

## 3. Replace the remaining inverse by a codimension-one residue projection

The factor kappa in M cancels from adjoints and compression. Use

L(f)=[u^(m-1)] f(u)(1+u)^(-m), <f,g>=L(fg).

Thus the original M is the Gram matrix up to kappa. The full degree<=m-1 carrier is nondegenerate: in its monomial Gram matrix entries with i+j>m-1 are zero and those with i+j=m-1 are one. Its complement to V is spanned by

q(u)=(1+u)^m-u^m,

because L(vq) is the coefficient of u^(m-1) in v, L(q^2)=m, and q has top coefficient m. In particular V is nondegenerate. This is a reuse of the existing codimension-one residue carrier, not a new positivity assertion about M.

For a rational multiplier f possessing a Laurent expansion at zero define its compression B_f on V by <v,B_f w>=L(vfw). The operators needed below are determined by this equality, not by a scientific inverse computation. Let

S v=(v-v(0))/u, e_j v=[u^j]v, a v=v(-1), a'v=v'(-1), tau=(-1)^(m-1).

S is nilpotent. Define vectors b,d,c in V by their coefficients, 0<=j<=m-2:

b_j=-binom(m,j+1)+binom(m,j)/m,
d_j=-binom(m,j+2)+m binom(m,j+1)-binom(m,j),
c_j=(-1)^j-tau binom(m,j)/m.                              (5)

Polynomial division followed by removal of the q component gives

B_(1/u)=S+b e_0,
A:=B_(1/u^2)=S^2+d e_0+b e_1,
B_(1/(1+u))=S/(1+S)+c a.                                (6)

These identities can also be checked directly by multiplying by (1+u)^(-m) and taking coefficient u^(m-1). For a general polynomial v, split off its constant and linear coefficients to get the second identity from the defining equations for d and b. All inverses 1/(1+S) are the terminating nilpotent geometric series.

Residue integration by parts gives

R=(m/2)(B_(1/u)-B_(1/(1+u)))
 =(m/2)(N+b e_0-c a), N=S^2/(1+S).                       (7)

Indeed the logarithmic derivative of the residue weight u^(-m)(1+u)^(-m) is -m/u-m/(1+u); inserting Z=(u+1/2)J-(m-1/2) gives precisely m/[2u(1+u)]. No positive-real-spectrum claim about the actual finite-rho form is involved.

The involution I v(u)=v(-1-u) is an isometry of this residue form: residues at zero and minus one sum to zero and the residue at infinity vanishes at the declared degree cutoff. It conjugates A to A_plus=B_(1/(1+u)^2). Z,U,R and every commutator used below commute with I. Since B=delta(A+W A_plus), in a trace against any such commuting operator we may replace B by t A, where

t=delta(W+1)=(m^4-1)/(24m).                              (8)

This is **only a trace-level replacement**; B=tA is not asserted as a matrix identity, and parity-off-diagonal blocks are not asserted self-adjoint for an unrelated positive inner product.

## 4. The six finite trace identities and an explicit verification route

For the declared m>=7 range, (5)-(7) give

tr R^2 = (3m^3-m^2)/2-m+1,
tr(RU) = -m(m-1)(m-3)(m+1)/3,
tr(AR) = -2m^2+m+1,
tr(A[Z,R]) = -(m^2-2m-4)/4,
tr(AU) = (m-1)(m^2-2m-2),
tr(A[U,R]) = m^3-2m^2-3m+2.                             (9)

Here is a coefficient/endpoint verification certificate for all six equalities. It avoids leaving a named unknown trace in the conclusion. The required endpoints from (5), by the binomial theorem and its first two derivatives, are

b_0=-m+1/m, b_1=-(m-2)(m+1)/2,
b_2=-(m-1)(m-3)(m+1)/6,
b_3=-(m-1)(m-2)(m-4)(m+1)/24,
b_4=-(m-1)(m-2)(m-3)(m+1)(m-5)/120,
d_0=(m-1)(m+2)/2, d_1=m(m^2-4)/3,
d_2=m(m-1)(m-3)(m+2)/8,
d_3=m(m-1)(m-2)(m+2)(m-4)/30,
b(-1)=-1+tau/m, b'(-1)=-1-tau, b''(-1)=-2+(m-1)tau,
d(-1)=1-tau, d'(-1)=2+m tau, d''(-1)=6-m(m-1)tau,
c_0=-b(-1), c_1=-1-tau,
c(-1)=-b_0, c'(-1)=b_1, c''(-1)=-2b_2.                (10)

In particular (10)'s b_4 and d_3 are actual present coefficients in our range. Do not extend them past a lower-dimensional truncation by polynomial continuation.

For any f in V the following four evaluations are sufficient:

e_0 A f=f_2+d_0 f_0+b_0 f_1,
e_1 A f=f_3+d_1 f_0+b_1 f_1,
a A f=f(-1)-tau f_0+(tau/m)f_1,
a' A f=f'(-1)+2f(-1)+m tau f_0-tau f_1.                 (11)

Use tr(v ell)=ell(v). Since N is strictly degree-lowering, its powers have trace zero. Directly expanding (7) and substituting (10) gives

tr R^2/(m/2)^2=4[b(-1)-b_0+b_1]+2b_0^2+2b(-1)^2,
tr(RU)=2m b_2,
tr(AR)/(m/2)=2b_2+2b_0+d_1-d_0-b_1+b_0(d_0+b_1)+2,
tr(AU)=2d_2+6b_3.                                      (12)

For the two commutator traces, [Z,S]=-S-S^2/2 gives

L_Z=[Z,N]=-2S^2-sum_(k>=3) ((k+1)/2)(-1)^k S^k,
[Z,R]/(m/2)=L_Z+((u+1/2)b')e_0-(b/2)e_1
                         -((u+1/2)c')a-(c/2)a'.

Taking traces with A and using (10)-(11) reduces the answer to

tr(A[Z,R])/(m/2)
 =1+m/2-d_1-d_2/2+b_2+b_3/2+b_1(m^2-2)/2
   +b_0(1+b_1+b_2-d_1/2)+1/(2m)
 =-(m^2-2m-4)/(2m).                                    (13)

Similarly [S^2,U]=4S^3J-6S^4, e_0 U=2e_2 and e_1 U=6e_3 imply

[A,U]=4S^3J-6S^4+2d e_2-(Ud)e_0+6b e_3-(Ub)e_1.

Thus tr(A[U,R])=tr(R[A,U]); the very same endpoint evaluations give

tr(A[U,R])/(m/2)
 =4(b_4-d_3)+2m^2 b_2+2d_1+2b_0(-d_2+3b_3)-2m-2+2/m
 =2(m^3-2m^2-3m+2)/m.                                  (14)

Equations (10)-(14) prove (9) by ordinary rational polynomial substitution. They are displayed so the most cancellation-heavy part is independently checkable, rather than justified by an inaccessible computed table.

As a hand-only normalization crosscheck in an old covered case, m=5 has b=(-24/5,-9,-8,-3), d=(14,35,35,14), c=(4/5,-2,-1,-3). With r=2R/5, the rows are (-28/5,4/5,1/5,-1/5), (-7,-2,2,-1), (-7,-1,1,-1), (0,-3,3,-3). Direct multiplication gives (rA-Ar)_(2,0)=28 and (rA-Ar)_(3,1)=-26/5; hence tr A[U,R]=(5/2)[2*28+6*(-26/5)]=62, as in (9). This check is not a scientific program, a new finite certificate, or evidence for transferring the formula to m=2 or 3.

## 5. Derivative traces, exact coefficient, and sign

Keep the star for the fixed limiting M. Since Z'_0=U/12, R'_0=(U+U*)/12, cyclicity and adjoint invariance of the trace give

C_0:=2tr(R([Z*,B]-2B))
    =2t tr(A[Z,R])-4t tr(AR),
C_1:=d/dlambda [2tr(R_lambda([Z_lambda*,B]-2B))]_(0)
    =(t/3)[tr(A[U,R])-4tr(AU)],
(d/dlambda tr R_lambda^2)_(0)=tr(RU)/3.                  (15)

For the middle equality, first obtain (t/3)tr(A[U,Z*])-(2t/3)tr(AU), and then use [U,Z]=2U. This is a **trace identity**, not an assertion that the two derivative commutator matrices are equal. The trace-level reflection replacement (8) applies to all terms because Z,U,R commute with the involution.

Substituting (9),

C_0=t(15m^2-6m-4)/2,
C_1=t(-3m^3+10m^2-3m-6)/3.

With g=mt, equations (3) and (15) become

F(0)=(t/2)(-3m^4-m^3+17m^2-10m-4),
F'(0)=(t/9)(m^5-3m^4-10m^3+33m^2-9m-18).

Using p=m^2-3 in (4) now gives (1). Its sign needs no parameter scan: for integer m>=3,

-27m^6+228m^4=m^4(228-27m^2)<0,
-7m^5-83m^3<0,
-429m^2+252m+72<0.

The last inequality follows already at m=1 and decreases thereafter. We use this elementary sign observation only in the proved trace-table range m>=7, not as a low-dimensional extension of (1).

## 6. Translate the same readout back to the original S variable

The exact centered metric germ is even in rho^(-1), and the centered contiguous scalar product is even in x+beta apart from its known leading power. Therefore Q_m has homogeneous degrees D,D-2,D-4,... only. This follows directly from the analytic germs used in Section 2 and polynomiality: on every scaling direction in an open parameter set the omitted odd powers have zero coefficients, so the corresponding polynomial homogeneous components vanish. We do not use an unreviewed assertion about the full P(c) reflection for this step.

Keep K_pref=m^(2W)/2. The previously proved top face has the DIFFERENT prefactor m^2 K_pref:

H_D(sigma,a)=m^2 K_pref (sigma+a)^D B_top(lambda),
B_top(lambda)=tr(R_lambda^2)+W-1, lambda=a/(sigma+a).

The extra m^2 follows either directly from the original P1 identity or from the already frozen V2 top formula m^(2W+2)/2. It must not be dropped when the D and D-2 layers are combined.

Let H_1=[sigma^(W-2)a]H_D. From the trace table and its derivative,

B_top(0)=m(3m-2)(m+1)/2,
B_top'(0)=tr(RU)/3=-m(m-1)(m-3)(m+1)/9.

Thus

H_1/K_pref=m^2[(W-1)B_top(0)+B_top'(0)]
          =m^3(m^2-1)(27m^2+7m-12)/18.                 (16)

There is no unknown lower coefficient in the translation. Indeed P1(S,a)=Q_m(S+h,a). Translation leaves the exponent of a unchanged. To contribute to S^(W-4)a, the only possible higher centered monomial is sigma^(W-2)a from degree D; degree D-1 is absent, and degrees below D-2 cannot gain degree. Consequently

C_m^S=C_m+h^2 binom(W-2,2)H_1.                       (17)

Insert h=(W+1)/(2W), (16), and the exact C_m. Collection with the COMMON factor K_pref(m^4-1)/(432m) gives

U_m=P_m+3(m^2+1)(m^2-2)(m^2-3)(27m^2+7m-12).

For an explicit hand-checkable collection route,

(m^2+1)(m^2-2)(m^2-3)=m^6-4m^4+m^2+6.

Multiplying this displayed polynomial by 3(27m^2+7m-12) and adding the displayed P_m gives precisely the U_m in the theorem. No symbolic program or coefficient artifact is an input to this equality.

For m>=7, the negative terms in U_m admit the conservative grouping

81m^8-387m^6-91m^5-62m^3-144
 >=m^6(81m^2-684)>0,

and the remaining 21m^7+453m^4+21m^2+378m are positive. This proves C_m^S>0 in the declared range. The same sign comparison is not a license to substitute the stable-degree formulas at smaller m.

This resolves the raw-S compensation for exactly the selected mixed coefficient. A negative centered coefficient is therefore not a negative raw coefficient or a physical trace counterexample. No coefficient after an unspecified nonconstant gcd cancellation is covered.

## 7. Actual inputs, contribution history, and stopping boundary

The two load-bearing immutable source bodies are:

- Original c1 paper: Source ac9f1c0ffcfbb7ad5564721442480ad8e2236b83, path research_notes/owner_goal_20261016/p11_independent_native_driver/parity_all_m_c1_curvature_author/PARITY_ALL_M_C1_FACE_INVERSE_FREE_CURVATURE_OBSERVER_AUTHOR.md, 13131B, SHA256 1b0a3105eadb9e3dc59f12183b5dcc7a0bc28417e1707031d363d8f1c6902908, Git blob 9dc967073ac9316d5b899f6275e0147a168fc04e.
- V2 top face and exact rescaled frame: Source 65a880f63fce7488f5c3af126fa42e18a6a90a1f, path research_notes/owner_goal_20261016/p11_independent_native_driver/parity_all_m_c1_uniform_sum_tail_addendum_v2_author/PARITY_ALL_M_C1_POSITIVE_TOP_HOMOGENEOUS_FACE_AND_UNIFORM_SUM_TAIL_AUTHOR_V2.md, 16649B, SHA256 7fdb2a56835e9d8f6d7ef078121712769840d1bdc55e6864db26a5d4db97dce8, Git blob c94088a17f4a09dd2d16171162c09ed13807a8bf.

Both authors personally consumed these original source bodies in their exact old scopes. Their earlier genuine reviews are not votes on this new lower-layer theorem. The old eleven-input all-m source gate remains the provenance locator for the original model and reuse. No new external primary theorem is imported without proof here; nilpotent frame identities, finite residue compression, and the endpoint cancellations used for this particular coefficient are displayed.

BFF6DC selected and coordinated the lower-layer question with F73673. Both authors declared having independently reached the same centered second metric germ and coefficient readout before their complete new constructions were exchanged. This records their disclosed chronology, not external cognitive attestation. F73673 supplied the finite residue-compression/exact-trace elimination and the original raw-S compensation calculation. BFF6DC supplied a separate positive-Gram/Pearson norm argument for this same C_m for m>=40, then fully checked the exact trace proof and caught the missing top-prefactor m^2 in the first raw appendix. F73673 accepted the correction, and both hand-collected the corrected raw polynomial. These are joint proof and correction contributions inside one unit; neither author may act as its genuinely independent reviewer.

The original BFF 9531B bound working, F736 13869B exact centered working, and F736 4537B raw appendix remain unchanged. The last of these contains the now identified prefactor error and is not a current mathematical premise. Its new corrected successor and the detailed self-check record are separately pinned in the context. The original >=40 bound is retained as contribution history and an internal crosscheck, not a second theorem or an extra assertion requiring independent acceptance here. The earlier draft that stated only >=40 remains an unfrozen historical draft.

The 7500B global-reflection working and its 4687B application appendix remain UNREVIEWED/parked. BFF's prior complete read and direction assessment of them are disclosed. Their body was first read by BFF after his V2 freeze; they were not inputs to that earlier theorem. They help explain the selected direction but are not used as accepted premises in the proof above.

Root supplies line direction and control coordination, not an additional mathematical vote. 7CDA51 has predeclared zero construction or repair contribution to this new rho^(-2)/T/readout/Student/Pearson/sign scope; all old Parity/CM24/CONTROL exposure remains NONBLIND. No unfrozen working was sent to that future peer. The next mathematical gate is a genuinely nonauthor whole-paper review of the exact frozen paper, typed interface, context, and precise existing inputs.

All arithmetic and derivations in this manuscript were done on paper. Tools only read/save existing text and handle hashes, byte counts and custody. Scientific programs, imports, AST/compile, samples, solvers, parameter scans, matrix evaluation, generated coefficient expansions, and new scientific invocations all remain zero. Old m7 preparation exhaustion/NO_START, fixed233 STOP, core98 holds, previous Source history, Task records and budgets are unchanged. No Native vote, shared Tool registration, new Task, Foundation promotion, Working Truth or Goal closure is created by this paper.

The unresolved frontier remains substantial: other raw mixed coefficients, other lower layers, full coefficientwise P1 positivity, physical P1/whole-trace sign and the all-M objective are not settled. No automatic successor or manufactured V3 is implied by this one result.
