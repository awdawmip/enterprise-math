# D25 — Cartier-compatible short-overflow port for both 2304 branches

2026-11-07 · TASK_RESEARCH author-side theorem and executed exact finite-field check · UNREVIEWED / NOT_ADMITTED.

Parent task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Intended hourly20 Research lane `chatgpt-research-hourly-enterprise-math-20260923`, distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`. Source inputs: prior other-lane B3/B5 reflected-prefix formula at `10635cfb1086d1c59ba7ca61a03a6f87c6744a5e`, other-lane Cartier integration-constant proof at `463de60c82ea336e48444919c88e19b34b0b7cf8`, and this lane's Dixon diagonal theorem at `991ef9a186933833a519f4c968c34ae9581091a4`. Sources are mathematical inputs, not imported owner identities.

## Construction

Let \(p\equiv 13,19\pmod{24}\) be prime and let \(p=8k+3\) (B3) or \(p=8k+5\) (B5). In \(\mathbb F_p[z]\), define the degree-\(k\) low Gaussian part

\[
Q(z)=\sum_{i=0}^{k}q_i z^i,\qquad q_i=\binom{k}{i}\binom{3k+1}{i},
\]

and the source-labeled reflected normalized \(p^2\)-tail

\[
R(z)=\sum_{j=0}^{J} r_j z^{p-1-j},\qquad
r_0=\frac{3}{64(k+1)(3k+2)},\quad
\frac{r_{j+1}}{r_j}=\frac{(j+1)^2}{(k+j+2)(3k+j+3)},
\]

where \(J=5k\) for B3 and \(J=5k+2\) for B5. All denominators are nonzero modulo \(p\). Set \(C(z)=1\) for B3, \(C(z)=1-z\) for B5, \(D=z\frac{d}{dz}\), and \(P=\pi_{<p}(CQR)\).

## Theorem 1 — the high projected carry is only degree \(k\)

There is a unique polynomial \(H\in\mathbb F_p[z]\) such that

\[
\boxed{C(z)Q(z)R(z)=P(z)+z^pH(z),\qquad \deg H\le k.}\tag{1}
\]

Its coefficients require **only** the first \(k+1\) reflected indices \(r_0,\ldots,r_k\):

\[
\boxed{
[z^\ell]H=
\sum_{j=0}^{k-\ell-1}q_{j+\ell+1}r_j
-\mathbf 1_{\mathrm{B5}}\sum_{j=0}^{k-\ell}q_{j+\ell}r_j,\quad
0\le\ell\le k.
}\tag{2}
\]

Empty sums are zero. In B3, \(\deg H\le k-1\). Proof: a term \(q_i r_j z^{p-1+i-j}\) crosses the degree-\(p\) cutoff iff \(i-j\ge1\). Its B5 Euler-shift partner \(-q_ir_j z^{p+i-j}\) crosses iff \(i-j\ge0\). Sorting their coefficients by \(\ell=i-j-1\) and \(\ell=i-j\) proves (2), including the boundary \(i=j\).

## Theorem 2 — exact compact observer and Cartier bridge

Let \(x\in\mathbb F_p\setminus\{0,1\}\) satisfy \(Q(x)=0\). The weighted source readout

\[
E_B(x)=2(1+8D)\pi_{<p}(CQR)\big|_{z=x}
\]

has the **exact** finite-field representation

\[
\boxed{
E_B(x)=16C(x)(DQ)(x)R(x)
-2x\left[H(x)+8(DH)(x)\right].
}\tag{3}
\]

Proof: \(D(z^pH)=z^pDH\) in characteristic \(p\), and \(x^p=x\). At \(Q(x)=0\), the constant part of \((1+8D)(CQR)\) vanishes, and \(D(CQR)(x)=C(x)(DQ)(x)R(x)\). Apply \(2(1+8D)\) to (1) and evaluate at \(x\).

Moreover the existing exact Gauss–Cartier Wronskian identity from `463de60...` says

\[
(DQ)(x)R(x)=-\frac{I_B(x)+c_Bx}{(1-x)^r},
\]

where the relevant B-branch integrating exponent is \(r=(p+1)/2\) for B3 and \(r=(p+3)/2\) for B5, and \(I_B,c_B\) are the previously defined non-Cartier primitive and its single integration constant. Substitution in (3) proves the **source-aware bridge**

\[
\boxed{
E_B(x)=
-\frac{16C(x)}{(1-x)^r}\left(I_B(x)+c_Bx\right)
-2x\left(H(x)+8(DH)(x)\right).
}\tag{4}
\]

Thus the exact B3/B5 finite projected observer is reconstructed from a Cartier endpoint port plus the \(H,DH\) boundary pair; \(H\) has degree at most \(k\), instead of carrying the entire high-series product. In B5, the cutoff diagonal cannot be silently dropped: the separately established Dixon evaluation gives \(T_{B,p}=(k!)^2((3k+1)!)^2/192\ne0\).

## Independent exact check

The companion program `d25_b_source_short_overflow_20261107.py` constructs \(Q,R\) by their own finite-field binomial/factorial recurrences. It independently evaluates every surviving term of \(2(1+8D)\pi_{<p}(CQR)\), and compares it with the compact quotient-and-Cartier-compatible expression (3). Executed on **all 94 primes** \(p<2500,\ p\equiv13,19\pmod{24}\), **94/94 PASS**. Representative \(p:(E_B,(DQ)R,H,DH)\) at \(x=1/9\):

- \(13:(0,7,11,1)\)
- \(19:(8,9,10,4)\)
- \(43:(33,11,34,9)\)
- \(67:(46,56,50,28)\)
- \(373:(220,319,57,323)\).

In particular all five values of \((DQ)(1/9)R(1/9)\) match the **independently published** Cartier-port table at `463de60...`, and all five \(E_B\) values match the **independently published** full projected-source table at `10635cf...`. The \(p=373\) arithmetic here is a portable finite-field derivative check, not the original native H0/B0 experiment.

## Next unresolved mathematical unit

The mother objective \(W_p\equiv p\pmod{p^3}\) for both target classes is OPEN. The new equations (3)–(4) are an exact connection between the previously separate projected-prefix and Cartier descriptions. Next use the existing A-stream forced ODE lower injection and the actual Fricke parameter pair \(t_\pm=\pm6\sqrt2\) to derive the **A/B adjoint cancellation**. The new smaller B port is \((I_B+c_Bx,H,DH)\), with explicit B5 Dixon diagonal and with B3's \(C=1\) preserved. Test candidate off-diagonal compensation at \(p=13,19,43,67,373\), without repeating accepted D24 units or native p373 H0/B0 (#1559).

Native Site status remains `CONFIGURED_NOT_LIVE_VERIFIED`; its ordinary-control transport read returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. Prior session/claim/run/uploads and requests remain preserved as UNKNOWN; no new native authority or checkpoint is asserted. Existing control issue: #1558.