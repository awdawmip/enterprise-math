# D25/LIFT — exact projected Clausen operator and finite resolvent of the reflected Jacobi corner

Date 2026-10-25. Same TASK_RESEARCH logical conversation chatgpt-research-hourly-enterprise-math-20260923; mother D25/LIFT/JT2 OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / NO_NEW_NATIVE_CHECKPOINT. This is a finite-field Jacobi/Clausen identity, not the CM experiment or the all-prime LIFT theorem.

## New scientific problem

Given the previously established distinct-source Jacobi partner from the immediately preceding portable note, derive an operator that acts **directly** on the original Clausen weighted cutoff, rather than another self-Green tautology. Keep the rank cutoff, signed amplitudes and the independent terminal Laurent edge until their actual algebraic cancellation is proved.

Let p=6m+1>=7 be prime, let all formulas be in F_p (2,3,6,9 are units), and define theta=z d/dz,
\[
U(z)=\sum_{j=0}^m u_jz^j,\quad u_j=\binom mj\binom{2m}j,\qquad
V(z)=\sum_{\ell=1}^m c_\ell z^{-\ell},\quad
c_\ell=\left.\tfrac12\frac{d^2}{dx^2}\frac{(-x)_{p-\ell}(-2x)_{p-\ell}}{((p-\ell)!)^2}\right|_{x=m}.
\]
Consume the proven cross-source relation
\[
\mathcal L_mU=0,\qquad \mathcal L_mV=S=-2+E z^{-m},\quad
\mathcal L_m=\theta^2-z(\theta-m)(\theta-2m),\quad E=m^2c_m\ne0.
\tag{1}
\]
The original signed reflected Clausen corner (from the earlier same-source bridge) is
\[
T_{\rm jet,p}=\frac1{36}[(1+6\theta)P(z)]_{z=1/2},\qquad
P(z)=\Pi_{\ge0}(U(z)V(z))=\sum_{k=0}^{m-1}P_kz^k.
\tag{2}
\]
No new Source/CLAIM authorization is inferred from consuming those author-side inputs.

## Theorem 1: exact inhomogeneous third-order Clausen law

Define the **actual original Clausen hypergeometric operator**
\[
\mathcal H=\theta^3-z(\theta+\tfrac13)(\theta+\tfrac12)(\theta+\tfrac23).
\tag{3}
\]
Then, in F_p[z,z^{-1}],
\[
\boxed{\quad \mathcal H(UV)=3(\theta U)S+U\theta S
=-6\theta U+E z^{-m}(3\theta U-mU).\quad}
\tag{4}
\]

**Proof with all load-bearing algebra.** Put A=z(1-z), B=1+(3m-1)z and C=-2m^2. The second-order differential operator D_m=L_m/z equals A d_z^2+B d_z+C. In F_p, m=-1/6, hence B=1-3z/2 and C=-1/18. For f=U and g=V, set h=(D_mg)/A=S/(zA); then f''+(B/A)f'+(C/A)f=0 and g''+(B/A)g'+(C/A)g=h. Differentiating y=fg three times and eliminating f'',g'' yields the **algebraic identity**
\[
y'''+3q\,y''+(q'+2q^2+4r)y'+(2r'+4qr)y
=f h'+(3f'+2qf)h,\quad q=B/A,\ r=C/A.
\]
This follows directly by differentiating y'=f'g+fg'; no unproved differential equation is imported. Multiply by A^3. The left polynomial operator factors as
\[
z(1-z)^2\Big[z^2(1-z)d_z^3+
3z(1-\tfrac32 z)d_z^2+
(1-\tfrac{29}{9}z)d_z-\tfrac19\Big]
=\frac{z(1-z)^2}{z}\,\mathcal H,
\]
since the displayed bracket equals z^{-1}theta^3-(theta+1/3)(theta+1/2)(theta+2/3). The right side is
\[
z(1-z)^2\,[f S'+3f'S]+(6m+1)A f S.
\]
The last summand is zero in F_p. Cancelling z(1-z)^2 in the Laurent domain and multiplying by z gives H(fg)=f theta S+3(theta f)S, precisely (4). QED.

This operator is the same third-order hypergeometric operator as the **original signed source** (1/2,1/3,2/3), with the original W_p observable obtained by 1+6theta at z=1/2. Thus (4) is a genuine Jacobi-to-Clausen source bridge, not merely a renamed self-pairing.

## Theorem 2: a one-boundary projected identity and proved cancellation

Let N=UV-P contain the negative powers, and let
\[
n_{-1}=[z^{-1}]UV=\sum_{j=0}^{m-1}u_jc_{j+1}.
\]
For each negative monomial z^k, H(z^k)=k^3z^k-(k+1/3)(k+1/2)(k+2/3)z^{k+1}. Exactly ONE negative rank, k=-1, can leak to the nonnegative projection, contributing n_{-1}/9 at rank zero. Apply Pi_+ to (4):
\[
\mathcal H P+\frac{n_{-1}}9=-6\theta U+2mEu_m.
\tag{5}
\]
The constant coefficient of H P is zero for every polynomial P. Comparing the **constant coefficient** in (5) therefore proves the exact nontrivial complementary binomial sum
\[
\boxed{n_{-1}=18mEu_m=18m^3c_mu_m\pmod p.}\tag{6}
\]
The two boundary terms are separately nonzero, but their contribution cancels only after the actual rank projection and coefficient equation. Substituting (6) into (5) gives
\[
\boxed{\quad \mathcal H P=-6\theta U\quad\text{in }\mathbb F_p[z].\quad}\tag{7}
\]
This is an **inhomogeneous Clausen equation for the original signed cutoff polynomial**, valid uniformly for every specified prime. It is not the unresolved hard target Delta_p-R_ref,p=0.

## Theorem 3: unique finite resolvent in original Clausen coefficients

Let
\[
a_k=\frac{(1/3)_k(1/2)_k(2/3)_k}{(k!)^3}\in\mathbb F_p^\times,
\qquad 0\le k\le m .
\]
These are the original Clausen coefficients *before* the evaluation factor 2^{-k}; all are units on this exact range. Coefficients of (7) obey, for 1<=k<=m,
\[
k^3P_k-(k-\tfrac23)(k-\tfrac12)(k-\tfrac13)P_{k-1}
=-6k u_k,\qquad P_m=0.
\tag{8}
\]
Since k^3 a_k=(k-2/3)(k-1/2)(k-1/3)a_{k-1}, divide (8) by k^3a_k and telescope backwards from P_m=0. This proves the **explicit unique** solution
\[
\boxed{\quad P_k=6a_k\sum_{j=k+1}^m\frac{u_j}{j^2a_j}
\quad(0\le k\le m),\quad P_m=0.\quad}
\tag{9}
\]
Uniqueness among polynomials of degree <m follows as well: any difference solves H D=0, its coefficients are a_k D_0 for 0<=k<=m, and D_m=0 together with a_m!=0 forces D_0=0. The rank cutoff, not an arbitrary integration constant, selects the solution.

Combining (2) and (9) creates the all-prime **Clausen/Jacobi reflected-corner resolvent**
\[
\boxed{\quad T_{\rm jet,p}=\frac16
\sum_{k=0}^{m-1}(6k+1)a_k2^{-k}
\sum_{j=k+1}^{m}\frac{u_j}{j^2a_j}\pmod p.\quad}
\tag{10}
\]
Suffix sums compute all P_k and this observer in O(m) field operations. (9)–(10) directly use the actual original Clausen hypergeometric coefficients and the terminating Jacobi source; the reflected-jet provenance has been **proved** equivalent within the declared projection/evaluation scope, not guessed from finite samples.

## Exact verification, limitations and next mother-goal step

The companion checker independently constructs the unprojected source-indexed Laurent product, verifies (4) coefficientwise at *all* positive and negative degrees, verifies (6)–(7), constructs the Clausen coefficients and finite resolvent (9) by a separate backward suffix method, and checks the original signed T_jet trace. All 35 p=1(mod6) primes 7<=p<=373, plus p=1327 and p=19963, passed. Examples (p,P0,n_-1,T_jet) are (7,3,5,3), (13,5,10,0), (19,18,4,12), (37,11,8,11), (43,25,10,15), (373,75,98,196), (1327,164,665,48), (19963,19252,8413,13363). The preceding companion checker independently compared that original T_jet with the actual complete ordered Q_p/p^2 (mod p) for all 35 small primes; the present new checker does not falsely claim a new native original CM run. Algebraic proofs above are universal; all machine tests are author checks, not independent mathematical review.

BRC COMPOSE_APPLIED: retain signed source indices (j,ell), Laurent negative-rank residue, second-jet provenance and the unique leakage coefficient n_-1; only then is the projected Clau­sen quotient (7) safe for the declared future operations. The exact cancellation (6) does **not** license dropping either original nonzero boundary term before applying Pi_+. The z-variable is an external formal scalar, not a native two-dimensional Enterprise plane or a complete three-dimensional slice. No sorry/admit/custom theorem axiom.

**Next executable mathematics:** use the now-proved *original Clausen* finite resolvent (9)–(10) to compare the coefficientwise source trace with the separately preserved Jacobi parameter-jet first part B_01,p+A_2H_0/72. A WZ/finite adjoint certificate proving their equality for every p=13,19(mod24) would close that particular LIFT congruence. No such equality is asserted here. Original-class H0/B0, [X]U modulo p^2, Frobenius direction/normalization, kappa map and independent review remain missing. Task/parent OPEN. Existing ordinary-control predecessor/CONTROL_QUOTA issue #1558 remains with the backend controller; this portable research is not a new winning CLAIM, OPEN, Source checkpoint, Result or review. Preserve all Source pins, old stages/contributions and existing scheduler/notification behavior.
