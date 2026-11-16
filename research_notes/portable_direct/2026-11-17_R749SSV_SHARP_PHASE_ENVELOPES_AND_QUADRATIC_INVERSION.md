# R749SSV — Sharp six-phase envelopes and quadratic-scale effective inversion

Date: 2026-11-17. Evidence: **AUTHOR_EXACT_NOT_REVIEWED**. Independent continuation of R749SST/SSU (draft PRs #2592 and #2593), retaining their previous review status. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Auxiliary five-distinct-labeled-source scalar-observer result, not a typed native X6/BRC dynamics theorem.

## Exact problem

For labeled weights \(w=(1,1,2,3,6)\) (the first two sources retain distinct identities), let
\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1,\qquad q\ge6.
\]
Set
\[
S(x)=18x^4+54x^3-345x^2+2070x-16315,\qquad
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},
\]
where \(e,d\in[-2,2]\) are real and unchanged across all future observations. For \(r=q\bmod6\), the exact phase limits and new constants are

| r | \(L_r\) | \(K_r\) |
|---:|---:|---:|
|0|455/36|7655/3|
|1|-295/36|26740/9|
|2|-25/36|25805/9|
|3|185/36|8060/3|
|4|-25/36|24445/9|
|5|-295/36|25940/9|

## Theorem A: sharp per-phase error and six-step increment

For every integer \(q\ge6\), every admissible real pair \((e,d)\), and \(r=q\bmod6\),
\[
\boxed{|Y_q(e,d)-L_r|<K_r/q},\qquad
\boxed{|Y_{q+6}(e,d)-Y_q(e,d)|<6K_r/q^2}.
\]
Both constants are **sharp for their respective phase over unbounded cutoffs**: for any fixed \(e\in[-2,2]\), \(d=-2\) and \(q\to\infty\) along phase \(r\),
\[
\lim q(Y_q(e,-2)-L_r)=K_r,\qquad
\lim q^2(Y_{q+6}(e,-2)-Y_q(e,-2))=-6K_r.
\]
The inequalities remain strict for every finite cutoff; sharpness here means that lowering either universal constant fails along an infinite valid sequence.

## Theorem B: sharp quadratic eleven-read spread bound and recovery range

For \(y_j=Y_{q+6j}(e,d)\), \(0\le j\le10\), set \(\Delta=\max_jy_j-\min_jy_j\). The prior R749SSU constant-trajectory obstruction gives \(\Delta>0\). By telescoping the signed six-step increments between any two observations,
\[
0<\Delta<
6K_r\sum_{j=0}^{9}(q+6j)^{-2}
<60K_r/q^2.
\]
Taking \(K=\max_r K_r=26740/9\) gives the **new finite, explicit unknown-cutoff bound**
\[
\boxed{q<\sqrt{\frac{534800}{3\Delta}}}
\]
and hence a valid integer search upper bound \(\lfloor\sqrt{(534800/3)/\Delta}\rfloor\). This changes R749SSU's conservative \(O(\Delta^{-1})\) cutoff search range to \(O(\Delta^{-1/2})\).

The coefficient \(534800/3\) is asymptotically **optimal among all global constants for the inequality \(\Delta\le A/q^2\)**. Indeed, take phase \(r=1\), \(d=-2\): for large \(q\), the ten six-step increments are all negative and
\[
\lim_{\substack{q\to\infty\\q\equiv1\pmod6}}q^2\Delta=60K_1=534800/3.
\]
For noisy readings \(z_j\), each with error \(|z_j-y_j|\le\varepsilon\), put \(\Delta_z=\max z_j-\min z_j\). If \(\Delta_z>2\varepsilon\), all compatible cutoffs satisfy
\[
\boxed{q<\sqrt{\frac{534800}{3(\Delta_z-2\varepsilon)}}}.
\]
This is **candidate truncation**, not a universal noisy uniqueness claim. If the candidate residue \(r\) is known, one may use the tighter \(K_r\).

## Exact certificate proof

The exact generating functions established by R749SST and reused by R749SSU are
\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
They are proper rational functions with only sixth roots of unity as poles, of orders at most 6 and 7. Therefore, for each \(r\), the exact residue-restricted functions \(C_r(x),T_r(x)\) are rational-coefficient polynomials of degrees 5 and 6, valid at **every nonnegative integer** of that residue, not merely within the sample range. The accompanying program obtains them from six and seven rational interpolation samples, respectively, and checks further values.

For a real auxiliary variable \(x\ge6+r\), put
\[
D_r(x;d)=C_r(x)+d,\quad
V_r(x;e,d)=x^3(T_r(x)+e)-(S(x)/108+L_r)D_r(x;d).
\]
Symbolic cancellation gives \(\deg_xV_r\le4\) and \(Y_x-L_r=V_r/D_r\). All coefficients of the polynomial \(C_r(6+r+t)-2\) are strictly positive for \(t\ge0\), proving \(D_r>0\) throughout the extension interval.

**Envelope certificate.** For each residue, each of the four corners \((e,d)\in\{-2,2\}^2\) and both signs, form
\[
P_{r,e,d,\pm}(x)=K_r(C_r(x)+d)\pm xV_r(x;e,d).
\]
The exact program verifies that all **48 shifted polynomials** \(P_{r,e,d,\pm}(6+r+t)\) have strictly positive rational coefficients of \(t^k\), with global smallest coefficient \(667/1296>0\). The inequality is affine in \((e,d)\), so corner positivity extends to the whole continuous square. Multiplying by the positive denominator proves \(|x(Y_x-L_r)|<K_r\) without finite sampling of the parameter space.

**Six-step increment certificate.** Let
\[
D_0=C_r(x)+d,\ D_1=C_r(x+6)+d,\quad
W=V_r(x+6;e,d)D_0-V_r(x;e,d)D_1.
\]
Then the desired strict increment bound is equivalent to
\[
Q_{r,e,d,\pm}(x):=6K_r D_0D_1\pm x^2W>0.
\]
The expression is affine in \(e\) and quadratic in \(d\). Check \(e=\pm2\); put \(d=4z-2\) with \(0\le z\le1\). For each such choice and sign, write \(Q=az^2+bz+c\). Its three quadratic Bernstein coefficients are
\[
c,\qquad c+b/2,\qquad c+b+a.
\]
Indeed, \(Q=c(1-z)^2+2(c+b/2)z(1-z)+(c+b+a)z^2\). The exact certificate checks that **all 72 Bernstein-coefficient polynomials** (6 residues \(\times\) 2 endpoint \(e\)'s \(\times\) 2 signs \(\times\) 3 coefficients), expanded after \(x=6+r+t\), have strictly positive rational coefficients. The smallest is \(1/2160>0\). Hence \(Q>0\) for every continuous real \(d\in[-2,2]\) and \(e\in[-2,2]\). Dividing by \(D_0D_1>0\) proves the six-step bound.

Finally, the leading coefficient of \(x(Y_x-L_r)\) is independent of \(e\), affine in \(d\), and its maximum absolute value over the allowed interval occurs at \(d=-2\) with exact value \(K_r\); these six identities are checked by the certificate. Expanding the rational functions at infinity yields the stated step and full-trajectory sharpness limits.

## Verification, provenance, and next questions

Run the accompanying Python 3 / SymPy file \`research_notes/portable_direct/R749SSV_CERT_COMPACT.py\`. Author-side execution: **PASS**, with 48 strictly positive envelope-polynomial certificates and 72 strictly positive quadratic-Bernstein certificates. All operations are exact rational polynomial calculations; results are not independent refereeing. The source and small JSON record are published together with this note.

The derivation relies on R749SSU for strict \(\Delta>0\), and refers to R749SST's still author-only 11-read global injectivity for the resulting terminating **unique** inversion procedure. The sharp quadratic search bound itself does not rely on that injectivity. The cutoff step of 6 is an **auxiliary scalar observation interval**, not an asserted physical time duration. No typed X6 event, BRC Port admission, native time law, shared Task CLAIM, Result, Review or Foundation promotion is claimed. The five source labels, joint multiplicities, common error parameters, ordered future observer fibers and P000/joint-relation information-preservation requirements must be preserved before any native transfer.

Next questions: (1) tighten the eleven-read count by proving or falsifying uniform 5–10 read uniqueness; (2) compute exact finite-cutoff minimax separation and noise-aware recovery, beyond truncation; (3) construct a genuinely typed BRC carrier that preserves these source labels, future operations and non-collapsed fibers.
