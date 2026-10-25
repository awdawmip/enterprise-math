# R4-EC21 — All-diagonal pole trichotomy and two positive leading Newton coefficients

2026-10-25 · **Author-side exact derivation, not independently reviewed/admitted**. Scope: positive ordered binary affine *auxiliary BRC* clean-source kernel; not P000-native X6 dynamics or the full word-resolved observer.

## Source and fixed question

GLOBAL_KNOWLEDGE_V1 read: \`awdawmip/chatgpt-global-knowledge main@9f35cf43236aaf491ac0693f2bd3a35c22175e0e\`; EM control/source read: \`awdawmip/enterprise-math main@9713f10774d8c0a64c64fb2bd9888bec5679f40d\`. Prior R4-EC20 theorem: \`972ec96c277b023946d2b60d6bbee75261622c6e\`. Reuse of R4-EC17/19/20 exact kernel and Newton transform: **REUSE_APPLIED / EXTEND_EXISTING_TOOL**, not a new BRC family.

Let

\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6},\quad
f_j(n)=E[n,j]-E[n,j-1],\quad E[n,j]=[x^nu^j]E.
\]

For \(j\ge d\ge0\), R4-EC20 established

\[
q_d(j):=\Delta^{j-d}f_j(2j+6)=[z^jt^d]\mathcal H(z,t),
\quad
\mathcal H=\frac{(1+t)^6(1-tz)(1-t(1+t)^2z)}
{1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3}.
\]

EC20 proved all-grade positivity for \(d\le14\), but not for unrestricted \(d\).

## All-grade theorem

For **every** integer \(d=3c+r\ge0\), where \(c=\lfloor d/3\rfloor\) and \(r\in\{0,1,2\}\), put \(h_d(z)=[t^d]\mathcal H(z,t)\). Then:

1. \(h_d(z)=P_d(z)/(1-z)^{c+1}\) for an integer polynomial \(P_d\). For \(d\ge1\), \(\deg P_d\le d+c-1\); \(P_0=1\).
2. The pole order is **exactly** \(c+1\). Indeed,
\[
A_d:=P_d(1)=
\begin{cases}
1&r=0,\\
2c+6&r=1,\\
2c^2+14c+14&r=2.
\end{cases}
\]
All \(A_d>0\).
3. For **all** \(j\ge d\), \(q_d(j)\) is exactly a polynomial of degree \(c\) in \(w=j-d\), with leading monomial coefficient \(A_d/c!>0\). If \(c\ge1\), the next coefficient, that of \(w^{c-1}\), equals \(F_r(c)/(c-1)!\), where
\[
\begin{aligned}
F_0(c)&=(8c^3+72c^2+91c-87)/6,\\
F_1(c)&=(2c^4+28c^3+85c^2-22c-72)/3,\\
F_2(c)&=(4c^5+80c^4+435c^3+430c^2-619c+195)/15.
\end{aligned}
\]
For all integers \(c\ge1\), **every** \(F_r(c)>0\). For \(c=0\), the polynomial is the positive constant \(A_d\).
4. Consequently each fixed \(d\) has a computable threshold \(W_d\) beyond which \(q_d(d+w)>0\) for integers \(w\ge W_d\). This does **not** establish the uniform statement \(q_d(d+w)>0\) for all \(d,w\ge0\).

## Proof, part I: exact integer-polynomial recurrence

With \(y=1-z\) the denominator factorizes as
\[
Q(z,t)=y(1-2zt-zyt^2)-z^3t^3.
\]
The numerator coefficients are, with out-of-range binomial coefficients defined to be zero,
\[
N_d(z)=\binom6d-\left(\binom6{d-1}+\binom8{d-1}\right)z+\binom8{d-2}z^2.
\]
Coefficient comparison in \(Q\mathcal H=N\) yields
\[
h_d=N_d/y+2zh_{d-1}+zyh_{d-2}+z^3h_{d-3}/y,\qquad h_k=0\ (k<0).
\]
Writing \(c=\lfloor d/3\rfloor\) and multiplying by \(y^{c+1}\) yields
\[
\boxed{P_d=N_d y^c+
2zP_{d-1}y^{c-\lfloor(d-1)/3\rfloor}+
zP_{d-2}y^{c+1-\lfloor(d-2)/3\rfloor}+z^3P_{d-3}},
\]
with negative-index terms omitted. In particular every \(P_d\) is in \(\mathbb Z[z]\).
The base cases \(d=0,1,2,3\) are explicit. Inductively, for \(d\ge4\), the four polynomial degrees are bounded by \(c+2\), \(d+c-1\), \(d+c-1\), \(d+c-2\); thus \(\deg P_d\le d+c-1\).

For \(j\ge d\), the coefficient formula
\[
[z^j]h_d=\sum_{k=0}^{d+c-1}[z^k]P_d\binom{j-k+c}{c}
\]
is a polynomial in \(j\) of degree at most \(c\). The usual binomial-zero convention is compatible with the polynomial falling-factorial expression since \(j-k+c\ge1\), including \(k>j\) for which the binomial is zero. Exact degree will follow from its nonzero leading pole coefficient.

## Proof, part II: exact leading pole

Expand the cubic piece formally as
\[
\mathcal H(z,t)=\sum_{k\ge0}
\frac{z^{3k}t^{3k}N(z,t)}{y^{k+1}(1-2zt-zyt^2)^{k+1}}.
\]
For \(d=3c+r\), the only contribution to pole order \(c+1\) is \(k=c\). Therefore
\[
A_d=[t^r]\frac{N(1,t)}{(1-2t)^{c+1}},\quad
N(1,t)=(1+t)^6(1-t)(1-t(1+t)^2).
\]
The coefficients of \(t^0,t^1,t^2\) of \(N(1,t)\) are \(1,4,2\), respectively. Extraction gives \(A_d=1,\ 2c+6,\ 2c^2+14c+14\), proving the exact pole order and degree.

## Proof, part III: second highest coefficient

For \(c\ge1\), denote the coefficient of \(y^{-c}\) in \(h_d\) by \(B_d\). Only \(k=c\) (first derivative in \(y\)) and \(k=c-1\) (constant term) contribute. Define
\[
N_1(t)=N(1,t),\quad
\dot N_1(t)=(1+t)^6\{t[1-t(1+t)^2]+t(1+t)^2(1-t)\}.
\]
The exact formula is
\[
\begin{aligned}
B_d={}&[t^r]\bigl[
(\dot N_1-3cN_1)(1-2t)^{-c-1}
-(c+1)N_1(2t-t^2)(1-2t)^{-c-2}
\bigr]\\
&+[t^{r+3}]N_1(t)(1-2t)^{-c}.
\end{aligned}
\]
Extracting terms through degree \(r+3\le5\) **with symbolic \(c\)** gives
\[
\begin{aligned}
B_{3c}&=(4c^3+36c^2+35c-45)/3,\\
B_{3c+1}&=(2c^4+28c^3+64c^2-94c-99)/3,\\
B_{3c+2}&=(4c^5+80c^4+330c^3-380c^2-1879c-330)/15.
\end{aligned}
\]
Now \(h_d=A_dy^{-c-1}+B_dy^{-c}+O(y^{-c+1})\). Expanding binomials at \(j=d+w\), the two highest coefficients are
\[
[w^c]q_d(d+w)=A_d/c!,\quad
[w^{c-1}]q_d(d+w)=\frac{A_d(d+(c+1)/2)+B_d}{(c-1)!}.
\]
Simplifying gives the displayed \(F_r(c)\). Set \(v=c-1\ge0\). Then
\[
\begin{aligned}
6F_0(1+v)&=8v^3+96v^2+259v+84,\\
3F_1(1+v)&=2v^4+36v^3+181v^2+240v+21,\\
15F_2(1+v)&=4v^5+100v^4+795v^3+2255v^2+1886v+525.
\end{aligned}
\]
Every coefficient is positive. The theorem follows **for all grades**, independently of any finite sweep. Effective eventual positivity follows by bounding all lower powers by \((\sum_{i<c}|a_i|)w^{c-1}\) for \(w\ge1\) when \(q_d(d+w)=a_cw^c+\sum_{i<c}a_iw^i\), since \(a_c>0\). QED.

## Verification, limits and continuation

A Python **exact-integer** checker constructs \(P_d\) via the displayed recurrence and checked \(d=0,\ldots,120\), including polynomial degrees and both pole formulas. Its independent depth-direction recurrence for \(E[n,j]\) checked 210 exact finite-difference equalities with \(0\le d\le34,\ 0\le w\le5\). The local ZIP evidence was cold-start executed successfully, with byte-identical regenerated report. These checks are distinct from the **symbolic proof** for all \(d\).

Example \(d=14\): coefficient of \(w^4\) is \(102/4!=17/4\), and coefficient of \(w^3\) is \(3801/3!=1267/2\), matching EC20. Example \(d=120\): exact pole order 41, \(A_{120}=1\).

**Open**: signs of all lower monomial coefficients when \(c\ge2\), all-\((d,w)\) positivity, full palindromic-kernel unimodality, and near-center \(f_j(2j+s)\ge0\) for \(s=0,\ldots,5\). Next precise unit: derive/prove the third-leading coefficient for \(d=3c+r\), look for an invariant positive polynomial cone or an exact counterexample. This work confers no CLAIM, formal Result, independent Driver approval or P000 theorem.
