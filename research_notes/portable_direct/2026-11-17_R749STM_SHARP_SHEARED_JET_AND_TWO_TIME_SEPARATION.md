# R749STM — Sharp sheared two-jet margins and an explicit finite two-time separator

Date: 2026-11-17. Evidence: **AUTHOR_EXACT_NOT_REVIEWED**. Frozen auxiliary scalar model: five distinctly labeled sources of weights (1,1,2,3,6), with four nuisance parameters e,d,E,D in [-2,2], fixed along each observation tail. Source pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Dependencies: R749STK and R749STL, including R749STL@1f17bac7eebc3b51b76868d578f62970a8398e29. This is a scalar observer theorem, with no native X6 event or BRC Port/Cell descent claimed.

## Model

Let C_n count the 5-tuples of nonnegative integers v with v1+v2+2v3+3v4+6v5 <= n-1, and let T_n be the sum of v1 over these 5-tuples. Define

\[
S(n)=18n^4+54n^3-345n^2+2070n-16315,\qquad
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108}.
\]

For residues r=0,...,5, take b=(78,73,74,75,76,77), A=(54027,74412,69363,60588,62019,70092), q=b_r+6k, p=q+6h, with arbitrary integers k>=0 and h>=1. Put x=(6j)^{-1}, F_j=Y_{q+6j}(e,d)-Y_{p+6j}(E,D), and F_j=a_1 x+a_2 x^2+O(x^3). The constant difference is zero.

## Theorem 1: exact universal sheared two-jet identity

For each of all six phases, every k,h and every legal nuisance quadruple, the exact formal Laurent coefficients obey

\[
\boxed{a_1=720(D-d),\qquad
a_2+(q+27)a_1=4320\{e-E-h(D-A_r/34992)\}.} \tag{1}
\]

Thus the sheared coefficient J_2=[a_2+(q+27)a_1]/4320 removes the first-jet contamination without assuming d=D. In particular, the following minimum is **sharp over the full four-dimensional nuisance box**:

\[
\boxed{
\min_{[-2,2]^4}|J_2|=
\begin{cases}
0,&r\in\{0,2,3,4\},\\
\max(0,(41h-1296)/324),&r=1,\\
\max(0,(h-1296)/324),&r=5.
\end{cases}} \tag{2}
\]

Each minimum is attained simultaneously with a_1=0, for every k>=0. The first strictly positive margins are sigma=4/81 at r=1,h=32 and sigma=1/324 at r=5,h=1297.

**Proof.** Rational quasi-polynomials C_r(n),T_r(n) follow from the exact generating functions

\[
\sum_{n\ge1}C_n z^{n-1}=\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{n\ge1}T_n z^{n-1}=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

Divide their polynomial coefficients to extract the Laurent coefficients through order 2 and substitute n=q+1/x. Direct symbolic simplification gives (1) in all six residue phases for symbolic k,h (not a finite scan). The standalone certificate reconstructs the coefficients and verifies both identities. Set alpha=A_r/34992. Since e-E covers [-4,4] independently of D in [-2,2], the minimum of |J_2| is max(0,h dist(alpha,[-2,2])-4). For residues 0,2,3,4, alpha lies in [-2,2] and the rational witness d=D=alpha,e=E=0 attains zero. In residues 1 and 5, respectively, alpha=689/324=2+41/324 and 649/324=2+1/324. Set d=D=2; when h(alpha-2)<=4 choose e=-h(alpha-2)/2,E=h(alpha-2)/2; otherwise choose e=-2,E=2. These witnesses achieve (2) and force a_1=0. QED.

## Theorem 2: explicit finite two-time separation

Fix either (q,p)=(73,265), with r=1,h=32,sigma=4/81, or (q,p)=(77,7859), with r=5,h=1297,sigma=1/324. For x=1/(6j), let f(x)=F_j and f(x/2)=F_{2j}. Define

\[
\widehat a_1=\frac{4f(x/2)-f(x)}x,\quad
\widehat a_2=\frac{2f(x)-4f(x/2)}{x^2},\quad
\widehat J_2=\frac{\widehat a_2+(q+27)\widehat a_1}{4320}.
\tag{3}
\]

**Exact uniform sufficient thresholds:** for all four nuisance parameters, at every integer j>=3,899,747 for (73,265), respectively j>=44,927,677,740 for (77,7859),

\[
\boxed{|\widehat J_2|\ge \sigma/2.} \tag{4}
\]

Hence the two candidate tails are never exactly equal at both matched observation indices j and 2j. For four independently observed absolute readout errors each bounded by eta, the noisy statistic has magnitude strictly greater than sigma/4 provided

\[
\boxed{\eta<\frac{1080\sigma x^2}{12+10(q+27)x},\quad x=(6j)^{-1}.} \tag{5}
\]

At the respective displayed starting indices, (5) becomes eta<5/615927273500052 and eta<1/261597111117468792114240. These are certified sufficient bounds, not optimal precision claims.

**Proof, including the exact finite remainder certificate.** For any fixed phase and q, write U_q(x)=x^5[C_r(q+1/x)+d], V_q(x)=x^6[T_r(q+1/x)+e], S_q(x)=x^4 S(q+1/x)/108, and P_q(x)=((1+qx)^3 V_q(x)-S_q(x)U_q(x))/x^4. Cancellation of the first four coefficients makes P_q a polynomial and gives Y_{q+6j}=P_q/U_q. For the other cutoff use E,D. Exact polynomial division of

\[
F(x)=P_q(x)/U_q(x)-P_p(x)/U_p(x)
\]

yields an **identity**, not an asymptotic assertion:

\[
F(x)=a_1x+a_2x^2+\frac{x^3 Q(x)}{U_q(x)U_p(x)}. \tag{6}
\]

Both denominators have constant coefficient c=1/4320. The executable certificate sets rho=1/(1000p) and, for polynomial coefficients depending on e,d,E,D, uses their monomial coefficient absolute-sum with the factor 2 to the total nuisance degree. It proves for all |x|<=rho and all nuisances in [-2,2] that |U_q-c|<c/2, |U_p-c|<c/2, |Q(x)|<=B_Q. Hence the exact uniform bound |F(x)-a_1x-a_2x^2|<=M|x|^3, where M=4B_Q/c^2, holds on that interval.

Substitution into (3) yields |\widehat a_1-a_1|<=3Mx^2/2, |\widehat a_2-a_2|<=5Mx/2, hence

\[
|\widehat J_2-J_2|\le
Mx\left(\frac52+\frac32(q+27)\rho\right)/4320.
\]

Taking x <= min[rho, sigma/(2M(5/2+3(q+27)rho/2)/4320)] gives error <=sigma/2. The script evaluates the exact rational majorants and takes j=ceil(1/(6x_max)); it proves both tabulated integer thresholds. Each readout error <=eta gives each f error <=2eta; from (3) its effect on \widehat J_2 is <=eta[12/x^2+10(q+27)/x]/4320. Equation (5) makes this <sigma/4. QED.

## Reproduction and scope

Run **R749STM_TWO_TIME_FINITE_SEPARATION_CERT.py** using Python 3 and SymPy. It reconstructs six phase polynomials from the frozen labeled-source generating functions, verifies (1) symbolically for arbitrary k,h, checks independent integer dynamic-programming counts for every 29<=n<=240, constructs polynomial Q and exact rational coefficient norms for both boundary pairs, and writes **R749STM_TWO_TIME_FINITE_SEPARATION_RESULTS.json** with the majorants, positivity checks, precision thresholds and sufficient j values. Author-side execution produced PASS in all checks. Exact arithmetic throughout. Evidence status AUTHOR_EXACT_NOT_REVIEWED; no formal checker or independent research review was performed.

**Next question.** Tighten the deliberately conservative rational majorants to yield practical observation times and noise budgets, extend constructive two-time bounds across arbitrary same-phase gaps and base shifts, and separately test if any source-aware BRC Port/Cell map preserves the relevant scalar residuals under declared native X6 future operations.
