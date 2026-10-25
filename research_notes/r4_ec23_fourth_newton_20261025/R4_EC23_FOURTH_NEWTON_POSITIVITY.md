# R4-EC23 — All-grade positivity of the fourth-highest Newton coefficient

Date 2026-10-25 · Status: AUTHOR-SIDE EXACT SYMBOLIC PROOF AND EXACT-INTEGER REGRESSION; NOT FORMALLY ADMITTED OR INDEPENDENTLY REVIEWED.

## Fixed sources, exact research scope

Global account control read: awdawmip/chatgpt-global-knowledge main@f54ad6814f1be98ffb6f7bc35a6ce332f6b61127. Read both entry files, Enterprise Math router, P000 original and projection, ACTIVE worldview, BRC priority, mathematical research and code policies. The original P000 blob SHA-1 (770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc) matches the startup projection; P000 is ACTIVE_LOCKED.

Enterprise Math source: awdawmip/enterprise-math main@502294bc379ecb2f5e6666c2e60bb6c7334e031e. Read current AGENTS, portable research, native X6/time and joint-observer contracts. Exact author-side predecessor: R4-EC22 third-leading theorem at research-draft/r4-ec22-third-newton-20261025-2033-r4, commit a6cf19e2eb9911366c173c7c2a36252d991e5294; R4-EC21 at 437a512174bc1518f9a99834b82062a87baaf53b.

This theorem concerns the positive ordered binary affine **auxiliary BRC** clean-source kernel. It is not a native P000 six-axis X6 dynamic or a physical time/heartbeat claim. It does not remove or project any native X6 relation. No safe native bridge or prior independent admission is assumed.

GitHub actor: awdawmip. Native task control returned CONTROL_QUOTA; own researcher session creation returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Live owner, official CLAIM and task identity were not obtained. This is an independently marked author-side research continuation, not a formal Result on someone else's claimed task.

## 1. The all-grade theorem

Consider the established clean-source kernel

\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6},
\quad f_j(n)=[x^nu^j]E-[x^nu^{j-1}]E.
\]

Use the verified R4-EC20/21 Newton transformation: for integers \(j\ge d\ge0\),

\[
q_d(j)=\Delta^{j-d}f_j(2j+6)=[z^jt^d]\mathcal H(z,t),
\]

where

\[
\mathcal H(z,t)=
\frac{(1+t)^6(1-tz)(1-t(1+t)^2z)}
{1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3}.
\]

**Theorem.** For every integer \(c\ge3\), \(r\in\{0,1,2\}\), let \(d=3c+r\). Then the polynomial in \(w\), \(q_d(d+w)\), has exact degree \(c\) and

\[
\boxed{[w^{c-3}]q_{3c+r}(3c+r+w)=\frac{J_r(c)}{(c-3)!}>0.}
\]

Writing \(v=c-3\ge0\), we have the following **exact**, integer, positive-polynomial certificates. Each list gives all coefficients, in descending degree including the constant. For \(M_r J_r(v+3)\):

| r | M_r | Polynomial degree | All coefficients from highest degree to constant |
|---|---:|---:|---|
| 0 | 45360 | 9 | 64, 4032, 101472, 1320480, 9724008, 42601608, 116706113, 204088185, 201711258, 79697520 |
| 1 | 113400 | 10 | 32, 2400, 73920, 1219680, 11892426, 72237690, 284870155, 747921945, 1262838717, 1203498135, 483424200 |
| 2 | 1247400 | 11 | 64, 5632, 208120, 4234560, 52587612, 421079736, 2258391575, 8321229290, 20967696299, 34213646907, 32107807305, 12853209600 |

Every integer is strictly positive and every denominator is positive, proving the assertion for **all** grades \(c\ge3\), not simply a finite test range. Together with EC21/22, the four highest monomial coefficients of the Newton difference polynomial are all strictly positive where defined. This does not imply all coefficients are nonnegative.

## 2. Proof from exact formal coefficient extraction

Set \(y=1-z\), and define

\[
\begin{aligned}
N_0(t)&=(1+t)^6(1-t)(1-t(1+t)^2),\\
N_1(t)&=(1+t)^6\{t(1-t(1+t)^2)+t(1+t)^2(1-t)\},\\
N_2(t)&=t^2(1+t)^8;\\
Q_0(t)&=1-2t,\quad Q_1(t)=2t-t^2,\quad Q_2(t)=t^2.
\end{aligned}
\]

Direct algebra yields the formal identity

\[
\mathcal H(1-y,t)
=\sum_{k\ge0}\frac{t^{3k}(1-y)^{3k}
(N_0+yN_1+y^2N_2)}
{y^{k+1}(Q_0+yQ_1+y^2Q_2)^{k+1}}. \tag{1}
\]

The denominator of the original rational function is exactly
\(y(Q_0+yQ_1+y^2Q_2)-(1-y)^3t^3\), so (1) is a formal geometric expansion in \(t\). No convergence or floating-point approximation is used.

Put \(d=3c+r\), \(c\ge3\), \(r\in\{0,1,2\}\), and \(h_d(z)=[t^d]\mathcal H(z,t)\). At the fourth relevant pole order, only \(k=c,c-1,c-2,c-3\) contribute. Define, for \(h=0,1,2,3\),

\[
\boxed{
R_h(c,r)=\sum_{\ell=0}^{h}[t^{r+3\ell}y^{h-\ell}]
\frac{(1-y)^{3(c-\ell)}(N_0+yN_1+y^2N_2)}
{(Q_0+yQ_1+y^2Q_2)^{c-\ell+1}}.} \tag{2}
\]

Then the first four Laurent singular coefficients are exactly

\[
h_d(1-y)=R_0 y^{-c-1}+R_1 y^{-c}
+R_2y^{-c+1}+R_3y^{-c+2}
+O(y^{-c+3}). \tag{3}
\]

To make (2) explicitly evaluable with integer/rational polynomial arithmetic, fix \(\ell,h\), let \(k=c-\ell\) and \(p=k+1\), and enumerate \(a=0,1,2\), \(i,s_1,s_2\ge0\) satisfying \(a+i+s_1+2s_2=h-\ell\). The corresponding summand in \(R_h\) is

\[
\frac{(-1)^{i+s_1+s_2}(3k)_{\underline i}(p)_{s_1+s_2}}
{i!\,s_1!\,s_2!}
[t^{r+3\ell}]N_a(t)Q_1(t)^{s_1}Q_2(t)^{s_2}
(1-2t)^{-p-s_1-s_2}. \tag{4}
\]

Here falling and rising factorials are distinct. The last extraction is finite because

\[
[t^m](1-2t)^{-p}=2^m(p)_m/m!.
\]

In our case \(r+3\ell\le11\). Thus (2)–(4) are **uniform symbolic polynomial formulas in \(c\)**, not extrapolations from finite \(c\).

## 3. Extraction of the fourth monomial coefficient

The previously proved (and independently implemented) recursion for the coefficients \(h_d\) provides

\[
h_d(z)=P_d(z)/(1-z)^{c+1},\quad
P_d\in\mathbf Z[z],\quad
\deg P_d\le d+c-1.
\]

Consequently the polynomial part at \(z=1\) has \(z\)-degree at most \(d-2\), hence cannot contribute to \([z^{d+w}]h_d\) for nonnegative integer \(w\). Pole terms of order \(c-3\) or less are polynomials in \(w\) of degree at most \(c-4\); the fourth-highest monomial coefficient depends **exactly** on \(R_0,\ldots,R_3\).

Let \(e_m\) be the elementary symmetric polynomial of order \(m\), and \(d=3c+r\). Expanding the associated binomial polynomials yields the exact formula

\[
\boxed{
\begin{aligned}
J_r(c)={}&
R_0\frac{e_3(d+1,\dots,d+c)}{c(c-1)(c-2)}
+R_1\frac{e_2(d+1,\dots,d+c-1)}{(c-1)(c-2)}\\
&+R_2\frac{e_1(d+1,\dots,d+c-2)}{c-2}
+R_3. \tag{5}
\end{aligned}}
\]

For \(m\) consecutive numbers \(d+1,\ldots,d+m\), define the power sums

\[
S_1=md+\frac{m(m+1)}2,\quad
S_2=md^2+dm(m+1)+\frac{m(m+1)(2m+1)}6,
\]

\[
S_3=md^3+\frac{3d^2m(m+1)}2+
\frac{dm(m+1)(2m+1)}2+
\left(\frac{m(m+1)}2\right)^2.
\]

Newton's identities give
\(e_1=S_1\), \(e_2=(S_1^2-S_2)/2\),
\(e_3=(S_1^3-3S_1S_2+2S_3)/6\).

Substitute these expressions and (2)–(4) into (5), set \(c=v+3\), expand over \(\mathbf Q[v]\) and cancel. The result consists of **exactly the three numerator coefficient lists in the theorem table**, each divided by its displayed \(M_r\). The attached SymPy program recomputes every intermediate formal coefficient directly and checks the signs by exact arithmetic. No numerical fitting enters the proof. The coefficient lists have no negative or zero element, hence \(J_r(v+3)>0\) for \(v\ge0\). QED.

## 4. Reproduction, limitations and next unit

The standalone file R4_EC23_verify.py derives the pole coefficients from (4), simplifies (5), asserts positivity of the full shifted rational-polynomial coefficients and separately constructs the **integer** recursion for \(P_d\). Exact interpolation of the independently computed \(q_d(d+w)\) for \(3\le c\le14\), \(r=0,1,2\) gave **36/36** matches. For \(c=3\) and \(r=0,1,2\) the fourth coefficients are respectively \(1757,4263,10304\). A local cold-start reexecution regenerated the report byte-identically. The symbolic identities, not finite crosschecks, justify the theorem for arbitrary \(c\).

Missing: genuine active owner and native CLAIM, Research Activity Guard, service-issued Result, independent Driver review, and all native X6 calculations. No native/worldview change, physical inference or Foundation promotion is asserted.

**Next discriminating question (R4-EC24):** derive the fifth-highest coefficient \([w^{c-4}]q_{3c+r}(3c+r+w)\) for \(c\ge4\), looking either for a shifted positive integer polynomial certificate or a fully exact negative counterexample. Separately retain the still-open all-Newton-coefficient positivity question and the near-center inequalities \(f_j(2j+s)\ge0\), \(s=0,\ldots,5\). The fixed-transition six/seven control-state gap and X6/native observer correspondence are independent pending problems.
