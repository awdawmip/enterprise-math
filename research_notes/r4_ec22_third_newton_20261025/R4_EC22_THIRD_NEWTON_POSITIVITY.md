# R4-EC22 — All-grade positivity of the third-highest Newton coefficient

Date: 2026-10-25 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT PROOF; NOT INDEPENDENTLY REVIEWED OR ADMITTED.

## Verified source scope

- GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@91f205cff7fae11596003fc2275ae44b383f3aa4. Read its two normative entry files, TASK_RESEARCH routing, P000, ACTIVE worldview, math policy and BRC route. P000 status ACTIVE_LOCKED; original P000 Git blob SHA-1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches the startup projection.
- Enterprise Math Source: awdawmip/enterprise-math main@0c67928445a0d75177b4f982f145ed756b12b6d5; read AGENTS.md, portable research and ordinary ChatGPT protocols, X6 contract and joint-observer preservation.
- Prior exact author-side result: R4-EC21, immutable commit 437a512174bc1518f9a99834b82062a87baaf53b.
- Scope: the positive ordered binary affine auxiliary BRC clean-source kernel. This derivation uses the source-defined formal BRC generating function, **not** a native P000 X6 evolution, phase calculation, physical heartbeat, or any attribution of native residuals. No pi/trigonometry or ordinary matrix exponential was used.
- Real connector identity: GitHub awdawmip. Native task query reported CONTROL_QUOTA; service-issued researcher session creation reported STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Active owner/CLAIM was not verified. No other owner's task or authority is claimed.

## Statement

Let

\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6},\qquad
f_j(n)=[x^nu^j]E-[x^nu^{j-1}]E.
\]

Use the exact Newton transform from EC20/21, for \(j\ge d\ge0\):

\[
q_d(j)=\Delta^{j-d}f_j(2j+6)=[z^jt^d]\mathcal H(z,t),\qquad
\mathcal H(z,t)=
\frac{(1+t)^6(1-tz)(1-t(1+t)^2z)}
{1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3}.
\]

**Theorem.** For every integer \(c\ge2\), \(r\in\{0,1,2\}\), set \(d=3c+r\). The polynomial \(w\mapsto q_d(d+w)\) has exact degree \(c\), and

\[
\boxed{[w^{c-2}]q_{3c+r}(3c+r+w)=G_r(c)/(c-2)!>0.}
\]

For \(v=c-2\ge0\), the three *explicit* all-grade positivity certificates are

\[
\begin{aligned}
360G_0(v+2)={}&32v^6+1056v^5+12080v^4+57840v^3+
114653v^2+98499v+52920,\\
1260G_1(v+2)={}&32v^7+1344v^6+20804v^5+148680v^4+
515543v^3+905436v^2+932571v+451080,\\
1260G_2(v+2)={}&8v^8+416v^7+8344v^6+82544v^5+
434707v^4+1276814v^3+2251556v^2+2356701v+960120.
\end{aligned}
\]

All displayed coefficients are positive integers, so positivity holds for arbitrary grades, not just those tested numerically. With the first two coefficients proved in EC21, the three highest monomial coefficients of every \(q_d(d+w)\) for \(d\ge6\) are positive. This does not settle all Newton coefficient signs or global source-kernel unimodality.

## Full formal-coefficient proof

Write \(y=1-z\), and put

\[
\begin{aligned}
N_0(t)&=(1+t)^6(1-t)(1-t(1+t)^2),\\
N_1(t)&=(1+t)^6\{t[1-t(1+t)^2]+t(1+t)^2(1-t)\},\\
N_2(t)&=t^2(1+t)^8,\\
Q_0(t)&=1-2t,\quad Q_1(t)=2t-t^2,\quad Q_2(t)=t^2.
\end{aligned}
\]

An exact formal power-series decomposition is

\[
\mathcal H(1-y,t)=
\sum_{k\ge0}\frac{(1-y)^{3k}t^{3k}(N_0+yN_1+y^2N_2)}
{y^{k+1}(Q_0+yQ_1+y^2Q_2)^{k+1}}. \tag{1}
\]

For \(d=3c+r\) only \(k\le c\) contributes to coefficient \(t^d\). Write the Laurent singular terms of \(h_d(z)=[t^d]\mathcal H(z,t)\) as

\[
h_d(1-y)=A_dy^{-c-1}+B_dy^{-c}+C_dy^{-c+1}+O(y^{-c+2}).
\]

To get those three coefficients, only \(k=c,c-1,c-2\) in (1) are relevant. For \(\langle m;F\rangle=[t^m]F(t)\), exact multiplication through order \(y^2\) yields

\[
A_d=\langle r;N_0/Q_0^{c+1}\rangle,
\]

\[
B_d=\left\langle r;
\frac{N_1-3cN_0}{Q_0^{c+1}}
-\frac{(c+1)N_0Q_1}{Q_0^{c+2}}\right\rangle
+\langle r+3;N_0/Q_0^c\rangle,
\]

and

\[
\begin{aligned}
C_d={}&\Big\langle r;
\frac{N_2-3cN_1+\frac{3c(3c-1)}2N_0}{Q_0^{c+1}}
-\frac{(c+1)(N_1-3cN_0)Q_1}{Q_0^{c+2}}
-\frac{(c+1)N_0Q_2}{Q_0^{c+2}}
+\frac{(c+1)(c+2)N_0Q_1^2}{2Q_0^{c+3}}\Big\rangle\\
&+\Big\langle r+3;
\frac{N_1-3(c-1)N_0}{Q_0^c}
-\frac{cN_0Q_1}{Q_0^{c+1}}\Big\rangle
+\langle r+6;N_0/Q_0^{c-1}\rangle. \tag{2}
\end{aligned}
\]

Every bracket is a finite exact extraction using
\([t^m](1-2t)^{-p}=2^m(p)_m/m!\).

The EC21 degree bound, \(h_d=P_d/(1-z)^{c+1}\) with \(\deg P_d\le d+c-1\), shows that the polynomial part of the Laurent expansion has support only in degrees \(z^j\) with \(j\le d-2\). Hence for all \(j=d+w\ge d\) the first three pole terms give exactly the three highest powers of \(w\):

\[
q_d(d+w)=A_d\binom{d+w+c}{c}
+B_d\binom{d+w+c-1}{c-1}
+C_d\binom{d+w+c-2}{c-2}
+\text{degree-}\le c-3\text{ terms}.
\]

For \(c=2\) there are no residual terms in \(w\). The elementary-symmetric identity

\[
\frac{e_2(d+1,\dots,d+c)}{c(c-1)}
=\frac{d^2+d(c+1)}2+\frac{(c+1)(3c+2)}{24}
\]

thus gives

\[
\boxed{
G_r(c)=A_d\!\left(\frac{d^2+d(c+1)}2+
\frac{(c+1)(3c+2)}{24}\right)
+B_d(d+c/2)+C_d,\quad d=3c+r.}\tag{3}
\]

Substitute the coefficient-extraction identities (2) into (3), apply the rising-factorial formula, and set \(c=v+2\). Direct *symbolic* polynomial equality produces the three explicit all-positive polynomials in the theorem. Therefore the result is valid for every integer \(c\ge2\), independently of finite computation. QED.

## Exact verification and limits

The companion exact Python/SymPy verifier symbolically derives (2)--(3), checks zero difference against all three positive-coefficient polynomials, checks each coefficient is positive, and separately constructs the independent integer recurrence for \(P_d\). It tests the highest three coefficients after exact polynomial interpolation in \(w\) for \(c=2,\ldots,14\) and \(r=0,1,2\): **39/39 PASS**. At \(c=2\), the three third coefficients are \(147,358,762\). The finite checks are regression evidence; the all-grade proof uses exact formal algebra and coefficient identities.

No independent Driver, official Result, source-issued CLAIM, native X6 run, or full observer/native correspondence certificate was obtained. The result does not justify interpreting auxiliary clean-path counts as physical residuals.

## Next exact question

Derive the fourth-highest coefficient \([w^{c-3}]q_{3c+r}(3c+r+w)\) for \(c\ge3\), via the third-order Laurent term, and seek a positive shift \(c=3+v\) or an exact negative counterexample. The stronger uniform nonnegativity of all Newton differences and the six near-center inequalities \(f_j(2j+s)\ge0\) (\(s=0,\ldots,5\)) remain open, as do native X6 transfer and independent project admission.
