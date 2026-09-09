# JT2 UR-Sun: exact parity elimination and one ordinary-Legendre norm/jet residue

Status: **EXACT REDUCED OBSTRUCTION RETURN / UNIFORM UR VANISHING OPEN / DRIVER REVIEW REQUIRED**.

Task: RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT  
Publication: TP2-22F5729C777040ECA121  
Researcher: EM-JT2-EF9380  
Claim: ur-sun-ef9380-20260910-201847  
Execution: ER-D9A31C2F856C87718DC2  
Branch: research/ur-sun-ef9380-20260910-201847  
Actual branch/source base: 52775e4f53b4a34210341f7ac07f7c6c2d3834df

## Result and its exact strength

The adjacent generalized-Legendre values and their differentiated recurrence can be eliminated with all parity defects retained. The advertised defect balance then becomes an identity; it does not evaluate the central divided value. A further finite, degree-sensitive Wronskian argument eliminates the generalized polynomial and the higher ordinary index from the remaining condition.

Write f=P_n and define the exact polynomial primitive
\[
I_n(x)=\int_0^x P_n(v)^2\,dv.
\]
On the task's frozen CM and exchanged-port scope, the following is proved uniformly:
\[
\boxed{
9P_n(t)P_n'(t)-p\bigl(2I_n(t)+3t\bigr)
\equiv 3\bigl(3B(t)P_n'(t)+pt\bigr)\pmod{p^2}.}
\tag{EQUIV}
\]
Thus the exact additional congruence still required is
\[
\boxed{
9P_n(t)P_n'(t)\equiv p\bigl(2I_n(t)+3t\bigr)\pmod{p^2}.}
\tag{NORM-JET}
\]
Its left-minus-right polynomial has degree at most 2n+1<p, compared with p-2 for the original barycentric product. At t it is one base-field scalar after a justified division by pt. It uses only P_n, its first jet, and a p-integral polynomial primitive of P_n^2; A, B, C, P_{2n} and their reflection defects have disappeared from the terminal certificate.

The vanishing in NORM-JET is **not proved here**. This is the taskbook's additional-identity return branch, not a proof or refutation of UR. The proved smallness is a single necessary-and-sufficient scalar certificate and the displayed strict degree reduction. No logical independence from the full fixed-polynomial system, no globally minimal new axiom, and no separating model are claimed. In particular, no perturbation violating barycentric lift, degree, endpoints or exact polynomial realizability is used.

## Frozen scope and legal divisions

Let p>3 be prime, p=3n+1=6m+1, and work in
\[
R=\mathbb Z_{(p)},\qquad \mathcal A=R[t]/(2t^2-1),\qquad n=2m.
\]
The exchanged branch is t^p=-t in \(\mathcal A/p\mathcal A\). Indeed,
\(t^{p-1}=2^{-(p-1)/2}\equiv(2/p)\), so among p=1 modulo 6 this is precisely p=13,19 modulo 24. No additional prime class is introduced. Both t and 2 are units; t^{-1}=2t.

Consume the frozen CM0, SIMPLE, coordinate bridge and barycentric lift:
\[
f(t)\in p\mathcal A,\quad d:=f'(t)\not\equiv0\pmod p,
\quad Q_m'(1/2)=d/(2t),
\]
\[
3B(x)\equiv P_{2n}(x)+2P_n(x)\pmod{p^2},
\qquad B(x)=P_{p-1}(-1/3,x).
\tag{BL}
\]
The nonzero d is a unit in the residue field. All k! denominators below have k<p. Coefficient reduction in the defining finite sum gives B=P_n modulo p, so B(t) is divisible by p as well. Define the exact integral values
\[
\lambda=B(t)/p,\qquad u=P_n(t)/p.
\]
These divisions follow from CM0 before reduction. This return does not assume the stronger valuation v_p(B(t))=1; that would follow from UR and SIMPLE, and is not available in advance.

## Sun source and exact truncation boundary

The primary source actually read in this authorized execution is Zhi-Hong Sun, [arXiv:1101.5386v5](https://arxiv.org/html/1101.5386v5), version dated 1 February 2012: definition (1.1), Lemma 2.1, Theorem 2.1, Corollary 2.1 and Theorem 2.2. Its rational p-integral convention matches R. We use the exact finite recurrence, not an untruncated analytic function.

Put N=p-1, z=(x-1)/2 and
\[
c_k(a)=\binom ak\binom{a+k}k,
\qquad c=c_N(-1/3),\qquad
A=P_N(2/3,x),\ C=P_N(-4/3,x).
\]
The exact specialized recurrence is
\[
2A-xB-C=-2c z^p.
\tag{S-EXACT}
\]
The two p-divisible factors in c, with all other factors units, give
\[
c\in p^2R,\qquad c/p^2\equiv1\pmod p.
\tag{TOP}
\]
For example, in the source's parameter notation the residue is n and the displacement (-1/3-n)/p is -1/3. The leading quotient is
\(\{(-1/3)(2/3)\}/\{n(n+1)\}=1\) modulo p. Consequently S-EXACT gives the task's p^3 recurrence
\[
2A-xB-C\equiv-2p^2z^p\pmod{p^3}.
\]
Differentiation is performed in R[x], before evaluation:
\[
2A'-xB'-B-C'=-pc z^{p-1}\in p^3R[x].
\tag{S-DERIV}
\]
This proves the requested modulo-p^2 derivative recurrence, with a stronger p^3 divisibility and an explicit boundary term.

## Exact adjacent-value elimination, retaining defects

Two finite contiguous identities follow directly from the same coefficients. For general parameter a and cutoff N, writing F=P_N(a,x),
\[
(x^2-1)F'-a\bigl(xF-P_N(a-1,x)\bigr)
=2(N-a)c_N(a)z^{N+1},
\]
\[
(x^2-1)F'-(a+1)\bigl(P_N(a+1,x)-xF\bigr)
=2(N+a+1)c_N(a)z^{N+1}.
\]
For completeness, use
\(c_k(a-1)/c_k(a)=(a-k)/(a+k)\),
\(c_k(a+1)/c_k(a)=(a+k+1)/(a-k+1)\), and
\(k^2c_k(a)=(a-k+1)(a+k)c_{k-1}(a)\).
All coefficients through z^N cancel; the displayed z^{N+1} coefficients remain. These are exact rational identities before modular reduction; no potentially nonunit ratio is inverted modulo p.

With D=x^2-1 and a=-1/3 they become
\[
\boxed{2A=2xB+3DB'-(6p-2)c z^p,}
\tag{A-ELIM}
\]
\[
\boxed{C=xB+3DB'-(6p-4)c z^p.}
\tag{C-ELIM}
\]
Subtracting them recovers S-EXACT. Differentiating these exact identities and then subtracting recovers S-DERIV, including its -pc z^{p-1} boundary. Thus the differentiated recurrence is used with actual adjacent-value elimination; no scalar UR conclusion is substituted for that calculation.

Since n is even, the residues n+1,n,n-1 give odd/even/odd reflection signs. Sun's modulo-p^2 reflection therefore makes the following exact polynomial quotients integral:
\[
\alpha(x)=\frac{A(x)+A(-x)}{p^2},\quad
\beta(x)=\frac{B(x)-B(-x)}{p^2},\quad
\gamma(x)=\frac{C(x)+C(-x)}{p^2}.
\tag{DEF}
\]
The task's port coordinates are their values at t. The jet is
\[
\beta_x(t):=\beta'(t)
=\frac{B'(t)+B'(-t)}{p^2}.
\]
The plus sign in this derivative is essential. We do not use the symbol eta for this jet; the older LIFT source's eta is a different divided carry.

Apply A-ELIM and C-ELIM at x and -x, add, and divide by the certified p^2 factor. Because
\[
z(x)^p+z(-x)^p=-1\quad\text{in }\mathbb F_p[x],
\]
TOP gives the coefficientwise identities
\[
\boxed{2\bar\alpha=2x\bar\beta+3D\bar\beta'-2,\qquad
\bar\gamma=x\bar\beta+3D\bar\beta'-4.}
\tag{DEF-ELIM}
\]
In particular, at t,
\[
2\alpha(t)\equiv2t\beta(t)-\tfrac32\beta_x(t)-2,
\quad
\gamma(t)\equiv t\beta(t)-\tfrac32\beta_x(t)-4\pmod p.
\]
Thus
\[
2\alpha(t)-t\beta(t)-\gamma(t)\equiv2\pmod p.
\tag{BALANCE}
\]
The balance in fact holds polynomially before the CM specialization; its derivation does not require the exchanged-port relation. Differentiating the polynomial balance, or subtracting S-DERIV at the two ports before division, yields
\[
2\bar\alpha'-\bar\beta-x\bar\beta'-\bar\gamma'=0.
\]
Substituting DEF-ELIM makes this an identity as well. None of these steps sets alpha, beta, gamma or beta_x to zero. The signed ports and the derivatives are retained until their actual cancellation is proved. What the linear elimination leaves unevaluated is the first even digit lambda, rather than an independently free alpha or gamma.

## A complete finite reduction of the surviving value

The next reduction uses the frozen full polynomial realization and BL, including their degree and endpoint data. Define
\[
\mathcal H(x)=\frac{P_{2n}(x)-P_n(x)}{3p}\in R[x].
\tag{H}
\]
Its integrality follows coefficientwise from BL reduced modulo p and B=P_n modulo p. It is exactly even, has degree at most 2n, and satisfies \(\mathcal H(1)=0\). BL gives
\[
B=f+p\mathcal H\pmod{p^2},\qquad
\lambda\equiv u+\mathcal H(t)\pmod p.
\tag{H-BRIDGE}
\]
Only this established p-divisibility is divided out.

Let
\[
V(x)=(1-x^2)\bigl(f(x)\mathcal H'(x)-f'(x)\mathcal H(x)\bigr).
\]
The ordinary Legendre equations give the exact rational identity
\[
V'(x)=-\frac n3 P_n(x)P_{2n}(x).
\tag{LAGRANGE}
\]
Indeed, the corresponding numerator before division by 3p differentiates to
\([n(n+1)-2n(2n+1)]P_nP_{2n}=-npP_nP_{2n}\).
Modulo p, n=-1/3 and P_{2n}=P_n, so
\[
\bar V'=\bar f^2/9.
\]

The primitive I_n is in R[x]: its denominators are at most 2n+1<p, hence are p-units. Moreover,
\[
\deg V\le n+2n+1=3n+1=p,\quad V\text{ is odd},\quad V(1)=0.
\tag{DEGREE-ENDPOINT}
\]
In characteristic p, a polynomial of degree at most p with derivative zero is a constant plus a multiple of x^p. Oddness eliminates the constant, but **does not eliminate x^p**. Hence
\[
\bar V=\bar I_n/9+\kappa x^p.
\]
The classical finite Legendre norm is
\[
I_n(1)=\int_0^1P_n(x)^2dx=\frac1{2n+1}.
\tag{NORM}
\]
One exact proof uses Rodrigues' formula and n integrations by parts on [-1,1]: all boundary terms vanish, the remaining derivative is the leading coefficient times n!, and the elementary beta integral of (1-x^2)^n gives 2/(2n+1). P_n^2 is even, giving NORM. All rational coefficients and denominators used here are p-integral at the present degrees.

DEGREE-ENDPOINT now fixes
\[
\kappa=-\frac1{9(2n+1)}=-\frac13\pmod p,
\]
because 2n+1=(2p+1)/3. Therefore the precise Frobenius-bearing identity is
\[
\boxed{\bar V(x)=\bar I_n(x)/9-x^p/3.}
\tag{FROB-NORM}
\]
It is proved using the actual degree, fixed Legendre coefficients and endpoint. There is no free-jet model or missing endpoint normalization here.

Only now evaluate at the labeled CM port. CM0, 1-t^2=1/2, and t^p=-t give
\[
-\tfrac12 d\mathcal H(t)
\equiv I_n(t)/9+t/3\pmod p,
\]
and hence
\[
\mathcal H(t)d\equiv-\tfrac29I_n(t)-\tfrac23t\pmod p.
\tag{H-VALUE}
\]
Together with H-BRIDGE this gives
\[
3\lambda d\equiv3u d-\tfrac23I_n(t)-2t\pmod p.
\tag{DIVIDED-ELIM}
\]
Multiplying by 3p proves EQUIV. The term -2t comes from the retained x^p term and the exchanged port; discarding it would change the terminal certificate.

## The exact residual and the next falsifiable identity

Define
\[
\varepsilon_p=
9\frac{P_n(t)}p\frac{P_n'(t)}t
-2\frac{I_n(t)}t-3\pmod p.
\tag{RESIDUAL}
\]
This is a base-field scalar: P_n is even, P_n' and I_n are odd, and division by t removes their common odd type. The division by p uses CM0; division by t uses t^{-1}=2t. EQUIV proves
\[
\boxed{\varepsilon_p=0
\iff3B(t)P_n'(t)\equiv-pt\pmod{p^2}.}
\]
Every object in RESIDUAL is the specified exact polynomial. Its value is not declared freely variable. The identity is necessary and sufficient on the full frozen scope, but its all-prime vanishing has not been established by this return.

Equivalently, write P_n(x)=Q_m(x^2), and put
\[
N_m=\sum_{r=0}^{2m}
\frac{[y^r]Q_m(y)^2}{(2r+1)2^r}.
\]
All 2r+1 satisfy 2r+1<=4m+1=2n+1<p. Then I_n(t)/t=N_m exactly, and the additional identity becomes
\[
\boxed{
18\,\frac{Q_m(1/2)}p Q_m'(1/2)
\equiv 2N_m+3\pmod p.}
\tag{HALF-NORM-JET}
\]
This is the precise proposed next target. It needs one divided ordinary-Legendre value, one ordinary first jet, and one polynomial norm readout. It requires neither a generalized adjacent parameter nor the retired harmonic blocks. No claim that arbitrary formulations require an extra axiom is made: the full defining coefficients already fix the number, and proving its value is the remaining arithmetic task.

## Conditional ordinary-Legendre and original UR bridges

If NORM-JET, equivalently epsilon_p=0, is proved, EQUIV gives the requested 3B(t)d=-pt modulo p^2. Multiplying BL by d immediately gives
\[
\bigl(P_{2n}(t)+2P_n(t)\bigr)P_n'(t)
\equiv-pt\pmod{p^2}.
\]
This is the requested barycentric deduction; it is conditional here only because the final scalar is open.

The recovered original normalization is retained explicitly. Let
\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{(k!)^2}z^k,
\quad g_{\rm raw}=F_p(1/2),\quad G_{\rm div}=g_{\rm raw}/p.
\]
The original terminating-jet source uses G_p for G_div, whereas earlier reflected/Clausen sources used G_p for g_raw. The already checked CM two-port packet gives
\[
G_{\rm div}\equiv\lambda\pmod p,
\qquad Q_m'(1/2)=d/(2t).
\]
The division of g_raw by p is supplied by its inherited CM0 and is confirmed by the retained two-port bridge; no scalar is renamed to force the result. Therefore
\[
3\lambda d=-t
\iff G_{\rm div}\bigl(-6Q_m'(1/2)\bigr)=1\pmod p.
\]
More precisely,
\[
\varepsilon_p\equiv
3\Bigl[1-G_{\rm div}\bigl(-6Q_m'(1/2)\bigr)\Bigr]\pmod p.
\]
Thus this return identifies the original UR obstruction exactly. The older LIFT carry eta_carry=(-6t*lambda*B'(t)-1)/p is not formed here, since its integrality requires UR first. QTF3 remains closed and the separate LIFT/audit/integration obligations are not asserted solved.

## Six-output disposition

| Task output | Delivered strength |
|---|---|
| 1. Uniform slope-value target | Equivalent uniformly to NORM-JET/epsilon_p=0; its vanishing is open. |
| 2. Explicit p^2 parity coordinates and balance | Proved coefficientwise using DEF, TOP and DEF-ELIM; both port labels retained. |
| 3. Differentiated recurrence and adjacent-value elimination | Proved exactly through A-ELIM/C-ELIM and S-DERIV; no parity defect silently discarded. |
| 4. Ordinary-Legendre deduction | Proved as the stated conditional implication via BL. |
| 5. Original UR bridge | Exact conditional equivalence with the source-qualified G_div, legal p divisions and coordinate bridge. |
| 6. Additional congruence/jet obstruction | One explicit base-field norm/jet scalar with proved equivalence and smaller polynomial degree; all-prime vanishing and full-system logical independence are not claimed. |

## Verification, method and source boundaries

The uniform proofs are the exact coefficient calculations, differentiated recurrence, Lagrange identity, finite degree bound, norm and endpoint normalization above. The task-specific exact rational checker additionally evaluated **p=13 and p=19 only** to check the new formulas, the sign of the derivative-invisible x^p term, and their new scalar transcription. It passed. At those two primes the residual is zero; that observation is not the uniform proof. No old 77-prime scan, CM0/SIMPLE proof, accepted QTF3 proof, prior peer check or retired harmonic-block decomposition was replayed.

Current toolbox coverage and explicit reuse resolutions are preserved in the artifact directory. T0/BRC is applied as typed signed coefficient/port/provenance preservation. T6's declared future-observer boundary is applied before quotienting; its use does not assert logical independence or a new minimal quotient theorem. The existing finite integer precision functions precision_detail, project_precision and recompose_precision were actually executed for the two example quotient witnesses. Positive weighted BRC, root/factorization facades and unrelated lexical matches are not used. No new general-purpose tool, Working Truth, Foundation claim or Lean proof is created.

This researcher is SOURCE_EXPOSED and is the same actual earlier advisory reviewer and QTF3 executor. This new UR derivation is not an independent combined-certificate audit. The original author's and reviewer's source identities remain separate. Startup evidence was durably published at 5ea38607c755a47a914037d8eb93f475a91de7db after actual new CLAIM 5608211099 and successful current runtime authorization. The source runtime is the complete 52775e4f snapshot with the explicitly approved, narrowly verified unchanged authority/code scope against 0a3de47e; it is not represented as a complete 0a3de47e local tree.

Source and exact readback bindings, the six-output map, two-example checker and precision/method receipts accompany this return. Recommended next control action: restore the same line Driver EM-DVR-57CCCE for ordinary review of this formal Result and the NORM-JET frontier. This return is frozen research evidence awaiting Driver review; it does not mark UR or the parent proved.

Researcher-ID: EM-JT2-EF9380 / RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT
