# PREFIX-1012 — One-Green reconstruction of all signed X6 BRC rooted Link loops

**Date:** 2026-11-22 (+08). **Status:** AUTHOR_EXACT_FORMAL_SERIES_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.

**Frozen input:** awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5). **Direct predecessor:** PREFIX-1011 at bdde3b30c3b6bd6b1e680c9d9671f711b9bfc0b6.

## Exact typed model

Use the native signed six-axis X6 Cell torsor with a chart-relative chosen anchor Cell 0; twelve named signed directions; initial incoming-neighbour port \(h=-e_1\); each native step \(d\) sends \((x,h)\to(x+d,-d)\) with the Stage46 **candidate** BRC signed integer weight \(w(h,d)=1-6\mathbf1_{h=d}\). Delete both directed crossings of Link \(\{0,e_1\}\), without renormalizing. \(L_k\) is the sum of signed weights of all permitted \(2k\)-step paths returning to Cell 0, summed across terminal incoming ports. This is a signed observer, **not** squared probability, positive mass, physical time or a change to P000.

As in PREFIX-1010/1011, work coefficientwise over \(\mathbb Q[[z]]\) in the Laurent ring:
\[
S(X)=\sum_{i=1}^6(X_i+X_i^{-1}),\quad D(X,z)=1-zS(X)+36z^2,\quad
G_j(z)=[X_1^jX_2^0\cdots X_6^0]D(X,z)^{-1}\quad(j=0,1,2).
\]
Let \(F=G_0,\ J=G_2,\ B=F-J,\ A(z)=1+36z^2\), and \(f_m=[z^{2m}]F\) with \(f_{-1}=0\).

## Theorem 1012.1 — G2 from G0 with a unique formal derivative law

For the entire formal series,
\[
\boxed{\frac{d}{dz}\bigl[z(G_0-G_2)\bigr]
=\frac{(1-36z^2)((1+36z^2)G_0-1)}{12z^2}.}\tag{1012.1}
\]
The right side is regular as a formal series since \(A F-1\) is divisible by \(z^2\). If \(B=\sum_{m\ge0}b_mz^{2m}\), then
\[
\boxed{b_0=1,\qquad b_m=\frac{f_{m+1}-1296f_{m-1}}{12(2m+1)}\quad(m\ge1).}\tag{1012.2}
\]
Thus \(G_2\) is reconstructed with no independently supplied second Green series; to obtain coefficients through \(z^{2K}\), one must read \(F\) through \(z^{2K+2}\).

**Proof.** Let \(g_j(u)=\sum_{a\ge0}u^a/[a!(a+j)!]\). Direct formal differentiation yields \(g_1=g_0'\), \(g_2=g_0''\), and \(u g_0''+g_0'=g_0\); equivalently, \(u g_2=g_0-g_1\). Let \(W_{r,j}\) count unweighted **named** six-axis signed words of length \(r\) with displacement \(j e_1\). These count coefficients in the already-proved exact BRC Laurent resolvent; they are not used as a substitute dynamical law. Separating the six positive and negative axis counts,
\[
W_{2m,0}=(2m)![u^m]g_0^6,\qquad
W_{2m,2}=(2m)![u^{m-1}]g_2g_0^5.
\]
Consequently,
\[
\begin{aligned}
W_{2m,2}&=(2m)![u^m](g_0-g_1)g_0^5\\
&=W_{2m,0}-\frac{(2m)!(m+1)}6[u^{m+1}]g_0^6\\
&=\boxed{W_{2m,0}-\frac{W_{2m+2,0}}{12(2m+1)}}.
\end{aligned}\tag{1012.3}
\]
At \(m=0\), both sides give zero: \(W_{0,2}=0\), \(W_{0,0}=1\), \(W_{2,0}=12\).

The exact native BRC resolvent derived in PREFIX-1010 states
\[
G_j(z)=A(z)^{-1}\sum_{r\ge0}W_{r,j}\bigl(z/A(z)\bigr)^r.\tag{1012.4}
\]
Set \(t=z/A\) and \(H(t)=\sum_{m\ge0}W_{2m,0}t^{2m}\). By (1012.3)–(1012.4),
\[
A(F-J)=\sum_{m\ge0}\frac{W_{2m+2,0}}{12(2m+1)}t^{2m},\qquad
\frac d{dt}[t A(F-J)]=\frac{H(t)-1}{12t^2}.
\]
Since \(tA(F-J)=z(F-J)\), \(H(t)=AF\), and \(dt/dz=(1-36z^2)/A^2\), the formal chain rule proves (1012.1). Also \(f_0=1,\ f_1=W_{2,0}-36=-24\). Coefficient comparison yields \(b_0=(f_1+36)/12=1\) and (1012.2) for \(m\ge1\). Differentiation determines a formal series \(zB\) uniquely from its derivative and its zero constant term. QED.

## Theorem 1012.2 — One ordinary A6 collision sequence determines every signed L_k

Write
\[
A_6(r)=\sum_{a_1+\cdots+a_6=r}\left(\frac{r!}{a_1!\cdots a_6!}\right)^2.
\]
Then \(W_{2r,0}=\binom{2r}{r}A_6(r)\), and the single Green input has the explicit exact coefficient formula
\[
\boxed{f_m=\sum_{r=0}^m(-36)^{m-r}\binom{m+r}{m-r}\binom{2r}{r}A_6(r).}\tag{1012.5}
\]
Define
\[
\begin{aligned}
U&=(1+36z^2)F-1,& R&=[1+(1-36z^2)F]/2,\\
P_+&=1+(1-6z)(zF+U/12),&
P_-&=1-(1+6z)(zF-U/12).
\end{aligned}
\]
Substituting \(J=F-B\) into the existing PREFIX-1011 signed rank-two BRC Link identity gives the complete all-grade formula
\[
\boxed{\mathcal L(z)=\sum_{k\ge0}L_kz^{2k}
=\frac{R(1-6z^2B)}{P_+P_-},\quad B\text{ from (1012.1) or (1012.2)}.}\tag{1012.6}
\]
Both denominators have unit constant terms, so all inverses exist formally. Equations (1012.2), (1012.5), (1012.6) compute any \(L_K\) from \(A_6(0),\ldots,A_6(K+1)\) alone. With fixed six-axis dimension a direct convolution implementation uses \(O(K^2)\) scalar arithmetic operations and \(O(K)\) coefficient storage, excluding large-integer bit complexity. **This is an observer-specific exact factorization**, not a proof of a rational-algebraic formula \(G_2=R(z,G_0)\), not a minimality theorem, and not permission to discard port, branch or provenance information needed by future observers.

## Actual exact verification

Executed locally with standard-library Python, exact factorial, binomial and fractions arithmetic:
- Six-axis word formula reconstructed \(G_0\) through \(z^{82}\); (1012.2) reconstructed \(B\) through \(z^{80}\).
- Independent displaced-word formula (1012.3) constructed \(G_2\) and agreed with \(G_0-B\) at every even degree \(0,\ldots,80\).
- Formal rank-two BRC formula (1012.6) produced integer \(L_0,\ldots,L_{40}\), with all odd coefficients through \(z^{80}\) zero.
- Reproduced all thirteen historical \(L_0,\ldots,L_{12}\) from PREFIX-1010.
- Separately ran the named twelve-direction, joint Cell-and-port signed BRC dynamic program with both forbidden Link crossings excluded, using only unreachable-return pruning; checked all \(L_0,\ldots,L_7\) exactly.

New integer coefficients (complete \(0\ldots40\) certificate and checker are alongside this note):

| k | Exact signed L_k |
|---:|---:|
|33|80304278237724943991300690540234070211919150130|
|34|-3268305998576990065330374494768021977521838246080|
|35|33133080815160949053797839196218026132598153650530|
|36|2655065628616619687578452575032196892085887967492540|
|37|-136393513872007237895768591150972217126007981835115920|
|38|3319281370806969872593595250241351922360739582214604600|
|39|-67626836932042223512044628760364453525936258210436185310|
|40|1455851491692302715943705657153082246427276017875760197900|

## Provenance and remaining problem

PREFIX-1010 and PREFIX-1011 are mathematical prerequisites; the present theorem is an **author proof and exact check**, not independent Review, accepted Foundation, formal Result, or a physical calibration. Frozen P000 and current ACTIVE worldview are unchanged. The mother question \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\) remains open. Historical \(EM\text{-}DIRECT\text{-}FBEA5D\) and \(RA\text{-}3FB2D033BE6048D8712FF056\) are provenance only; no current formal CLAIM or live identity is inferred.

**Next:** build a two-path endpoint-and-terminal-port Gram/collision formula for the *squared* first interior layer Link-masked probability. Seek either a separately certified quotient or the smallest fiber counterexample demonstrating that this one-scalar **signed-total** reduction fails for squared probability. A purely algebraic (no formal integration) expression for \(G_2\) remains an open stronger reduction.