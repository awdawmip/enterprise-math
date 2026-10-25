# R4-EC15 — Uniform BRC source-survival asymptotics through the intermediate scale

2026-10-25. Author-side exact analytic proof manuscript, NOT a native Result, independently reviewed theorem, or Heartbeat/X6 theorem.

## Frozen authority and provenance

GLOBAL_KNOWLEDGE_V1 canonical main \`2487ec77b812748d78d30bf68b3fa407d47a6f70\` (bootstrap, manual, project TASK router, P000 ACTIVE_LOCKED, ACTIVE worldview); P000 original Git blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` matches its startup projection. Enterprise Math source baseline main \`0cafeda058bb248cfa19bddf02ffeb0f405aff4e\` (portable research, activity and native X6 contracts); actual mathematical parent R4-EC14 at \`14dc1e409d0076941200500f53b4bca533471962\`. Locally declared author EMR4-LOCAL-20261025-EC15; registered project research activity RA-EMR4-20261025-1437-EC15UNIFORM. Native task inventory returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. An active Owner, formal CLAIM, source-native research identity and Driver reviewer are NOT verified.

The object is the precise auxiliary positive-mass ordered binary affine BRC, not the native six-dimensional Heartbeat world, native residual transport, physical time, or a theorem about the minimum number of fixed-transition BRC control states. Word length n is an abstract combinatorial parameter.

## 1. Exact carrier and grade source observer

Original paths are ordered input bits. Fine control q in {0,1,2}, clean-source r=0 (no 00, last bit not 0), r=1 (no 00, last bit 0), dirty source r=2, and affine orientation e=+/-1. Initial state (q,r,e,t)=(0,0,+1,0), t=e*k. Edges, displayed as (q', eta, b):

|q|bit 0|bit 1|
|---|---|---|
|0|(2,-1,-1)|(2,+1,-1)|
|1|(0,-1,-1)|(0,+1,-1)|
|2|(1,+1,+1)|(2,+1,-1)|

Let e'=eta*e, t'=t+e'*b and update r by actual occurrence of 00. On every edge, t'-t=e(1-2*bit). Hence j=(n-t)/2 is the number of negative grade increments. The grade-increment string is triangularly bijective to the original bit word; there are exactly binom(n,j) total paths at grade j. Define C[n,j] as the number that never contained 00. Thus R(n,j)=C[n,j]/binom(n,j) is the specifically declared **grade-conditioned provenance observer**, not a full future-input-preserving state quotient.

The eight clean fine states have the exact rational generating function inherited from EC13, recertified for this study by a symbolic eight-state matrix identity:

\[
F(x,u)=\sum_{n\ge0}\sum_{j=0}^n C[n,j]x^nu^j
=\frac{N(x,u)}{\Delta(x,u)},\quad
N=(1-ux^2)(1-ux^3),\quad
\Delta=1-(1+u)x+2u^2x^4-u^3x^6. \tag{1}
\]

The portable code verifies a polynomial vector H with
\((I-xM)H=(1+ux^2)\Delta v\) and \(\mathbf1^T H=(1+ux^2)N\). The exact integer recurrence implied by (1) is
\(C[n,j]=C[n-1,j]+C[n-1,j-1]-2C[n-4,j-2]+C[n-6,j-3]+[x^nu^j]N\),
with negative indices zero.

## 2. Main theorem — uniform, with a second term

There exist absolute positive constants \(\alpha_0,J_0,K\), depending only on the explicit fixed rational function (1), such that for every pair of integers \(n\ge1\), \(J_0\le j<n\) and \(0<\alpha=j/n\le\alpha_0\), we have \(C[n,j]>0\) and

\[
\boxed{\left|\log R(n,j)+2\frac{j^2}{n}+3\frac{j^3}{n^2}\right|
\le K\left(\frac{j^4}{n^3}+\frac{j^2}{n^2}+\frac1j\right).} \tag{2}
\]

These are **common constants over the entire moving-saddle range**, not sequence-specific big-O constants. This analytic theorem establishes existence of constants but does not supply optimized numerical values of \(K\) or \(\alpha_0\).

Consequently, for every \(\sqrt n\ll j\ll n\),

\[
\boxed{\log R(n,j)=-2j^2/n-3j^3/n^2+o(j^3/n^2)
=-(2+o(1))j^2/n.} \tag{3}
\]

In addition, for every \(j\to\infty,\ j=o(n)\) (including \(j/\sqrt n\to c\)),

\[
\log R(n,j)=-n I(j/n)+O((j/n)^2+1/j), \tag{4}
\]

where \(I\) is the exact rate defined in Section 3. Thus \(j/\sqrt n\to c\) gives \(R(n,j)\to e^{-2c^2}\), an independent uniform bridge to EC13. The exact endpoint \(j=0\) has \(R(n,0)=1\); fixed j is outside the asserted moving-saddle theorem.

## 3. Proof

**(a) Isolated pole and uniform analytic amplitude.** At u=0, \(F(x,0)=1/(1-x)\). Choose a fixed circle \(|x|=3/2\). Rouché's theorem, uniformly on this circle for all sufficiently small complex \(|u|\), gives exactly one simple zero \(\rho(u)\) of \(\Delta(\cdot,u)\) inside, analytically continuing \(\rho(0)=1\). All other poles lie outside. Set \(\lambda(u)=1/\rho(u)\) and take \(f(u)=\log\lambda(u)\) analytic at zero. Rational residue calculus, with \(A(u)=-N(\rho(u),u)/[\rho(u)\partial_x\Delta(\rho(u),u)]\), yields

\[
C_n(u):=\sum_j C[n,j]u^j=A(u)\lambda(u)^n+E_n(u),\quad
|E_n(u)|\le K_0(3/2)^{-n},\quad A(0)=\lambda(0)=1. \tag{5}
\]

This bound holds uniformly on a single disk \(|u|\le u_0\) because the pole-subtracted rational function is uniformly bounded on the fixed x-circle. It avoids invoking a fixed-density asymptotic beyond its uniformity scope.

**(b) Exact analytic expansions.** The pole obeys

\[
\lambda^6-(1+u)\lambda^5+2u^2\lambda^2-u^3=0.
\]

The unique root with \(\lambda(0)=1\) satisfies
\[
\lambda=1+u-2u^2+7u^3-29u^4+135u^5+O(u^6),\quad
f=u-\tfrac52u^2+\tfrac{28}3u^3-\tfrac{161}4u^4+O(u^5).
\]

Write \(D=u\,d/du\), \(g(u)=Df(u)=u-5u^2+28u^3-161u^4+O(u^5)\),
and \(\sigma^2(u)=Dg(u)=u-10u^2+84u^3-644u^4+O(u^5)\).
The positive saddle solving \(g(u_\alpha)=\alpha\) is unique and analytic for small positive \(\alpha\), because \(g'(0)=1\):
\[
u_\alpha=\alpha+5\alpha^2+22\alpha^3+86\alpha^4+O(\alpha^5),\quad
\sigma^2(u_\alpha)=\alpha(1+O(\alpha))>0. \tag{6}
\]

**(c) Fourier control uniform as \(\alpha\downarrow0\).** Since \(f(z)=\sum_{r\ge1}c_r z^r\) has real coefficients and \(c_1=1\), reduce the common disk so that \(\sum_{r\ge2}r^2|c_r|u^r\le u/2\). Use \(1-\cos(r\theta)\le r^2(1-\cos\theta)\) to obtain the global angular contraction

\[
\Re[f(ue^{i\theta})-f(u)]\le-\tfrac u2(1-\cos\theta),\quad |\theta|\le\pi. \tag{7}
\]

The exponential damping strength is \(nu\asymp j\to\infty\), even when u tends to zero. Fourier coefficient extraction from (5), with \(u=u_\alpha\), has stationary phase at \(\theta=0\). On \(|\theta|\le j^{-2/5}\),
\[
f(ue^{i\theta})=f(u)+i\alpha\theta-\tfrac12\sigma^2(u)\theta^2+O(u|\theta|^3),
\quad A(ue^{i\theta})=A(u)+O(u|\theta|).
\]
Set \(s=\sqrt{n\sigma^2(u)}\theta\). The terms linear in the imaginary cubic expansion and linear in the imaginary amplitude are odd and integrate to zero on the symmetric arc; fourth-order, squared-cubic and cross terms give a relative \(O((nu)^{-1})=O(1/j)\). On the complementary arc (7) gives \(\exp(-c j^{1/5})\) suppression; \(E_n\) in (5) is exponentially smaller. Gaussian integration therefore proves the **uniform relative** local coefficient estimate

\[
\boxed{C[n,j]=\frac{A(u_\alpha)\lambda(u_\alpha)^n u_\alpha^{-j}}
{\sqrt{2\pi n\sigma^2(u_\alpha)}}[1+O(1/j)].} \tag{8}
\]

All constants come from one fixed analytic disk, and can be selected independently of n,j in the stated range. Positivity follows by increasing \(J_0\) until the relative error is less than one-half.

**(d) Binomial Gaussian cancellation.** Uniform Stirling gives
\[
\binom nj=\frac{\exp(nH(\alpha))}{\sqrt{2\pi n\alpha(1-\alpha)}}[1+O(1/j)],
\quad H(\alpha)=-\alpha\log\alpha-(1-\alpha)\log(1-\alpha).
\]
Set
\[
I(\alpha)=H(\alpha)-f(u_\alpha)+\alpha\log u_\alpha,\qquad
B(\alpha)=\log A(u_\alpha)+\frac12\log\frac{\alpha(1-\alpha)}{\sigma^2(u_\alpha)}.
\]
Taking the logarithm of the coefficient ratio yields
\[
\log R(n,j)=-nI(\alpha)+B(\alpha)+O(1/j). \tag{9}
\]
The exact residue satisfies \(A(u)=1-2u+12u^2-65u^3+O(u^4)\); substituting (6) proves a cancellation invisible to an \(O(\log n)\) estimate:
\[
B(\alpha)=3\alpha^2+12\alpha^3+O(\alpha^4). \tag{10}
\]

**(e) Two and three rate coefficients from the envelope identity.**
Differentiate \(I\): the derivative of the moving saddle cancels by \(g(u_\alpha)=\alpha\), leaving
\[
I'(\alpha)=H'(\alpha)+\log u_\alpha
=\log[(1-\alpha)u_\alpha/\alpha].
\]
Using (6), the logarithm is \(4\alpha+9\alpha^2+(52/3)\alpha^3+O(\alpha^4)\). Since \(I(0)=0\),
\[
\boxed{I(\alpha)=2\alpha^2+3\alpha^3+\tfrac{13}3\alpha^4+O(\alpha^5).} \tag{11}
\]
Equations (9)–(11) imply (2), with a single K on a small fixed \(\alpha\)-interval and all sufficiently large j. For \(\sqrt n\ll j\ll n\), divide the three error terms in (2) by \(j^3/n^2\); their ratios are respectively \(j/n\to0\), \(1/j\to0\), and \(n^2/j^4\to0\). This proves (3). Equation (9) also proves (4). QED.

## 4. Finite evidence and honest boundary

An authored stand-alone SymPy program verifies the 8-state transfer polynomial identity, formal \(\lambda\)-series, saddle inversion, rate coefficients 2, 3, 13/3 and residue series. An exact integer six-row recurrence was run to n=3000, j<=400; 402 selected coefficients agree with an independent eight-clean-state count through n=150. Exhaustive binary-word enumeration covers all lengths 0–12, 8191 total words. The earlier EC14 independent symbolic checker was re-executed successfully. Exact coefficient tests confirm the *model/implementation*; they are not the universal proof, whose analytic steps are written above. All computations are author-side and do not constitute independent Driver review.

Scientific boundary: the compressed grade observer deliberately forgets full endpoint, orientation and future word labels. It cannot answer source equivalence after arbitrary specified future input. The strict six-vs-seven fixed-transition positive BRC realization, native R193 source/time ports and native X6 alignment remain OPEN.

R4-EC16: analyze the complementary boundary \(k=n-j\to\infty,\ k=o(n)\), where the EC14 spectral duality alone does not imply equality of finite-depth coefficients; also derive explicit numerical analytic constants for (2).

Method resolution: EC13/EC14 fine-state BRC law REUSE_APPLIED and EC14 exact symbolic source REUSE_EXECUTED. Status: author mathematical proof and finite exact checks; source publication as this manuscript is storage only, not native admission.
