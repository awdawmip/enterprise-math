# R5: All four-observer linear supports coincide, though eight flow corners retain history

Date 2026-11-07 (Asia/Shanghai). Scientific pins unchanged: GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. Inherits the seven-key, four-stage P/Q-BRC LR observer from PR #1767, predecessor 9f8c0f04b4a571b4a279d8c217d19f69562043a9. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Theorem: complete linear-support equality

Let K_F and K_L be respectively the FULL_HIST and seedless LR four-observer attainable images W=(e_P,e_Q,T_P,T_Q), allowing randomized declarations at each of seven stopping likelihood-ratio keys. For **every real** alpha,beta,rho,sigma,

\[
\max_{W\in K_F}(\alpha e_P+\beta e_Q+\rho T_P+\sigma T_Q)
=\max_{W\in K_L}(\alpha e_P+\beta e_Q+\rho T_P+\sigma T_Q).
\]

Consequently, in four-dimensional real space,

\[
\boxed{\operatorname{conv}(K_F)=\operatorname{conv}(K_L)}.
\]

Conv denotes the closed convex hull. The stronger nonconvex image-equality mother target remains open. This theorem covers all four-coordinate linear normals, rather than the earlier restricted symmetric/asymmetric time sections.

## Exact frozen model

Flow variables x=(g,a,b,u,v,w,z) obey 0<=a,b<=g<=1 and

- 0<=u<=c0=13a/40+b/80;
- 0<=w<=c2=3a/40+21b/80;
- 0<=z<=a/10;
- 0<=v-z<=9b/40.

At the seven ordered stopping LR keys r=(1/10,1/2,3/4,1,5/4,3/2,19/10), the Q masses M_j(x), as well as T_P(x),T_Q(x), are precisely those in VERIFY.py (the predecessor's frozen rational affine formulas). All masses are nonnegative; their zeroth and LR first moments are both one. For each declaration d_j in [0,1], e_Q=sum_j M_j*d_j and 1-e_P=sum_j r_j*M_j*d_j.

Seedless LR imposes 9*b*z=4*a*(v-z). Every legal seedless flow, including a=0 or b=0, has the representation z=theta*a/10, v-z=theta*9b/40, u=eta*c0, w=omega*c2 for theta,eta,omega in [0,1]. FULL_HIST permits independent theta_A,theta_B in the first two equations.

## Finite corner lemma

The base (g,a,b) polytope has five vertices: (0,0,0), (1,0,0), (1,1,0), (1,0,1), (1,1,1). Every affine function of x is multi-affine after the parameterization: affine jointly in (g,a,b) with fraction parameters fixed, and affine separately in each theta,eta,omega. Thus its maximum is reached by base vertices and fraction parameters 0 or 1. FULL_HIST uses five base vertices and four independent binary parameters (eta,omega,theta_A,theta_B); seedless LR uses three (eta,omega,theta).

Exact deduplication yields 34 FULL and 26 seedless corner candidates. The eight full-only corners all have g=a=b=1, u,w each in {0,27/80}, and either (v,z)=(9/40,0) or (1/10,1/10). Their exact historical residual 9bz-4a(v-z) equals -9/10 or +9/10.

## Eight simultaneous convex-order certificates

Set H_lambda(x)=sum_j max(0,1-(1+lambda)*r_j)*M_j(x). For **each** full-only corner x, VERIFY.py lists one fixed convex mixture of seedless corners y_k with nonnegative rational weights t_k. It checks: sum t_k=1, both times sum t_k*T_P(y_k)=T_P(x) and sum t_k*T_Q(y_k)=T_Q(x), and sum t_k*H_lambda(y_k)>=H_lambda(x) at the exact knots

\[
\lambda\in\{-1,-9/19,-1/3,-1/5,0,1/3,1,9\}.
\]

All calculations use Fraction, no floating-point. The lexicographic seedless corner ordering is generated in VERIFY.py, so sparse index-weight witnesses are fully reproducible. On each interval between knots, the hinge functions are affine in lambda. For lambda<-1 the score equals -lambda for all x by the moment identities; for lambda>9 it is zero. Therefore **each fixed mixture dominates every real H_lambda simultaneously**. Eight verified certificates require at most four positive weights each.

## From hinges to all four-dimensional normals

Maximizing alpha*e_P+beta*e_Q+rho*T_P+sigma*T_Q over independent declaration probabilities yields exactly

\[
\alpha+\rho T_P+\sigma T_Q+\sum_j\max(0,\beta-\alpha r_j)M_j.
\]

If alpha,beta>0, the last term is beta*H_(alpha/beta-1). If alpha,beta<0, using both moments, the optimized expression equals beta+rho*T_P+sigma*T_Q+(-beta)*H_(alpha/beta-1). If alpha>=0,beta<=0 the optimized expression is alpha+rho*T_P+sigma*T_Q; if alpha<=0,beta>=0 it is beta+rho*T_P+sigma*T_Q. These formulas also settle zero coefficients.

For any fixed normal the declaration-optimized expression is affine in x, so FULL attains its maximum among the 34 corners. The 26 seedless corners are already seedless feasible; each of the eight remaining corners is dominated by the weighted average of seedless corner scores with exactly matching two times. That weighted average cannot exceed the largest seedless score. Since seedless is contained in FULL, both maxima coincide for the given arbitrary normal. Compactness and finite-dimensional separation imply equality of the closed convex hulls.

The result does not require the witness mixture itself to be implemented as one seedless process. Such a realization is precisely a different, nonconvex image question. There is also no claim that this internal LR observer realizes native X6 dynamics.

## Reproduction and scientific meaning

Run: python3 VERIFY.py. EXACT_OUTPUT.txt is stdout from the Fraction execution. The script verifies 34/26 corner counts, all 34 stopping-mass normalizations and LR moments, nonnegative masses and time bounds, 26 seedless bilinear equations, and eight times/weights/hinge certificate bundles at all eight knots. The proof of all-real scope is by the multi-affine extreme-corner lemma plus piecewise-affine interpolation. The certificate was discovered using exploratory linear optimization, but the published verification requires only the Python standard library.

**New research frontier:** unrestricted four-dimensional linear support optimization is now completely solved: both models have identical support functions. Search for a true distinction, if any, through a nonconvex fiber witness or a direct seedless lifting theorem, not by further scanning linear hyperplanes. See NEXT_UNIT.md.

Native Enterprise Math owner/CLAIM and independent mathematical review remain unconfirmed while the Site service returns BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; a portable PR commit is author-side evidence, not a native Result or admission.
