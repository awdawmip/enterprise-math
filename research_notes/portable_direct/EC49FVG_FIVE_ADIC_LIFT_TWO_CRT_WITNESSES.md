# EC49FVG — exact 5-adic lifting at the previously unresolved unit-one shell

2026-11-21 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FRACTION_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED**.

## Scope and immutable scientific dependency

Portable continuation of EC49FVF (Draft PR #2878, scientific commit `51a7526eeaeef7b05dc4f12a47657bbb8db5c02e`) in the **derived rational Bernoulli hit-observer model**, retaining frozen BRC16943 input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Behavioral protocols are current; scientific input pins are unchanged. P000 V5, the account ACTIVE worldview, and the native X6 space/time interpretation remain unchanged. This result concerns exact rational prime valuations and a derived logarithmic readout, not native X6 physical dynamics. Full composite-minimax transfer remains conditional on FUQ/FUR endpoint-reduction author claims.

Put
\[
 \beta=\frac3{637},\quad \gamma=\frac{141024}{1653649},\quad
 u=\frac{4822040484}{8132285009},
\]
\[
 T_0=(1-x)(1-\beta x),\quad T_E=(1-x)(1+\gamma x),
\quad a=1-T_0=\frac{x(640-3x)}{637},
\quad b=1-uT_E,
\]
\[
 R=\frac{T_0}{uT_E},\quad S=\frac{bR}{a},\quad
 t(x)=\frac{\log R}{\log S},\qquad 0<x<1.
\]
The frozen model has \(0<a<b<1\) and \(1<R<S\). If for rational \(x\) one had \(t(x)=h/k\in\mathbb Q\), \(0<h<k\), then \(R^k=S^h\), so \(k v_p(R)=h v_p(S)\) for every prime \(p\). In particular, \(v_p(R)=0\) and \(v_p(S)\ne0\) certifies irrationality. Logarithms are only the derived observable; the certificates below use exact rational arithmetic.

## Theorem 1: complete 5-adic classification of the unit-one sub-shell

Let \(x=m/d\in(0,1)\) be reduced, \(5\nmid d\), and suppose \(v_5(m)=1\) and \(x/5\equiv1\pmod5\) in \(\mathbb Z_5\), equivalently \(x\equiv5\pmod{25}\). Then
\[
 v_5(R)=0,\qquad
\begin{array}{c|ccc}
 x\bmod125 & v_5(a) & v_5(b) & v_5(S)\\ \hline
 5 & \ge4&3&\le-1\\
 30,55,80 &3&3&0\\
 105 &3&\ge4&\ge1
\end{array}
\]
Consequently all reduced rational widths satisfying
\[
\boxed{5\nmid d,\quad x\equiv5\ \text{or}\ 105\pmod{125}}
\]
have irrational threshold phase \(t(x)\). These are two certified classes inside the previously unresolved \(x\equiv5\pmod{25}\) shell. For residues 30,55,80, the 5-adic *single-prime valuation* is neutral; no rational-phase existence is asserted.

### Proof

Write \(x=5y\), \(y\in\mathbb Z_5^\times\), \(y\equiv1\pmod5\). Exact identities give
\[
 a=25\frac{y(128-3y)}{637},\qquad b=25F(y),\qquad
 F(y)=\delta-\kappa y+u\gamma y^2,
\]
where \(\delta=(1-u)/25\), \(\kappa=u(\gamma-1)/5\). Here
\[
 v_5(1-u)=2,\ v_5(\gamma-1)=3,\
 \delta\equiv9\pmod{25},\
 \kappa\equiv0\pmod{25},\
 u\gamma\equiv1\pmod{25}.
\]
Thus \(F(y)\equiv9+y^2\pmod{25}\). Write \(y=1+5z\), \(z\in\mathbb Z_5\), to obtain
\[
 F(y)\equiv10(1+z)\pmod{25},\qquad
 128-3y=5(25-3z).
\]
Since \(637\) and \(y\) are 5-adic units,
\[
 v_5(a)=3+v_5(25-3z),\qquad
 v_5(b)=2+v_5(F(y)).
\]
For \(z\equiv0\pmod5\), \(v_5(a)\ge4\) and \(F(y)\equiv10\pmod{25}\), so \(v_5(b)=3\). For \(z\equiv4\pmod5\), \(v_5(a)=3\), \(F(y)\equiv0\pmod{25}\), and \(v_5(b)\ge4\). For \(z\equiv1,2,3\pmod5\), both valuations equal 3. These correspond to \(x\equiv5,105,30/55/80\pmod{125}\), respectively. Since \(x\equiv0\pmod5\), \(T_0\) and \(uT_E\) are 5-adic units, so \(v_5(R)=0\). Also \(v_5(S)=v_5(b)-v_5(a)\), proving the table and the irrationality claim. **QED.**

## Theorem 2: opposite-signed CRT residuals invisible to seven historical coordinates

Take pairwise coprime moduli
\[
 (4,3^7,7^5,13^3,125,29^2,673^2,416677^2)
\]
and residues \((2,3^6,1814,157,r,23,295,168371)\), \(r\in\{5,105\}\). Write \(m_r\in[0,N)\) for the CRT solution and set \(x_r=m_r/(N+1)\), where \(N\) is the product of the moduli. Exact integer computations give
\[
 N+1=2670325640808048587895583372456501,
\]
\[
 m_5=1112833620046482137532485425206630,\quad
 m_{105}=2180963876369701572690718774189230.
\]
Both are reduced fractions in \((0,1)\). For **both**, the vectors \((v_p(R),v_p(S))\) are
\[
 p=2:(-2,-4),\quad 3:(-6,-12),\quad 7:(-2,-4),\quad
 13:(-1,-2),\quad29:(0,0),\quad673:(0,0),\quad416677:(0,0).
\]
All seven historical coordinates are compatible with rational-phase candidate \(t=1/2\), but
\[
 p=5:\quad(v_5(R),v_5(S))=
 \begin{cases}(0,-1)&x_5,\\(0,1)&x_{105}.\end{cases}
\]
Both contradict every rational \(t\in(0,1)\). The examples expose opposite-signed 5-adic residuals behind the same coarse *seven-prime valuation observer*; they do not claim that every representation using seven primes is inadequate. The CRT construction and all eight valuation pairs are reproduced by the companion script. **QED.**

## Reproducible verification and scope

Companion Python 3 script uses only \`fractions.Fraction\`, modular inverses, exact rational valuations, and integer CRT. It enumerates all reduced \(0<m<d\le400\) with \(5\nmid d\), \(v_5(m)=1\), \(x\equiv5\pmod{25}\), checking all five residues. Counts for \(x\equiv5,30,55,80,105\pmod{125}\) are **326, 324, 325, 326, 319**, respectively. Both 34-digit CRT witnesses and all eight valuation coordinates check exactly; local Python returned \`ALL PASS\`. Infinite-family claims rely on the algebraic proof above. No independent referee, Lean checker, full composite-minimax transfer, or physical-model verification was performed.

## Next discriminating unit

For \(x\equiv30,55,80\pmod{125}\), the 5-adic valuation \(v_5(S)=0\) stays neutral on these entire residue shells; simply refining precision of that single valuation will not resolve them. Investigate additional independent primes or appropriately typed higher-information derived observations, preserving the residual/provenance distinction; seek finite sufficient prime-coordinate criteria for bounded rational-width families. Activity Source association and mathematical review remain distinct from file publication.
