# R749SSY — Sharp one-read phase-class recovery at cutoff 501

**Date:** 2026-11-17. **Evidence level:** AUTHOR_EXACT_NOT_REVIEWED; reproducible exact symbolic author certificate (nine polynomial guards, 54 positive coefficients, and an exact rational sharpness witness). Independent mathematical review is pending. **Mode:** independent portable research; not a native X6/Task/Result/Review claim.

**Frozen scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Reused exact predecessors:** R749SST (all-phase quasipolynomial generating functions and limiting phase values), R749SSV (sharp six-phase bounds), R749SSX (eight-read finite-range exact identification). Prior review statuses are unchanged.

## Definition

Keep five *distinct labeled* sources with weights \(w=(1,1,2,3,6)\). For an integer \(q\ge6\), let
\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^{5}:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
Let \(S(q)=18q^4+54q^3-345q^2+2070q-16315\). The auxiliary scalar readout is
\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},
\qquad(e,d)\in[-2,2]^2.
\]
For \(r=q\bmod6\), the four distinct limiting values define these **limit classes**:

| Class | Residues | \(L_r\) |
|---|---|---|
| 0 | 1, 5 | \(-295/36\) |
| 1 | 2, 4 | \(-25/36\) |
| 2 | 3 | \(185/36\) |
| 3 | 0 | \(455/36\) |

## Theorem 1 — One-read phase-class recovery with uniform absolute noise

For **all integers \(q\ge501\)** and **all real \(e,d\in[-2,2]\)**, a single measured value \(z=Y_q(e,d)+\eta\) with \(|\eta|\le1/100\) identifies the asymptotic phase class through these fixed rational thresholds:
\[
\begin{array}{c|c}
z<-2& \{1,5\}\\
-2<z<1203/250& \{2,4\}\\
1203/250<z<11&\{3\}\\
z>11&\{0\}.
\end{array}
\]
Every true value \(Y_q(e,d)\) is separated from the *relevant threshold boundaries* by strictly more than \(1/100\), so none of the equal-threshold ambiguities occurs with the stated noise.

The conclusion is about the **four limit classes**, not the exact cutoff \(q\) and not a distinction between the two residues within either class \(\{1,5\}\) or \(\{2,4\}\).

## Theorem 2 — The integer threshold 501 is sharp

Among integer lower bounds \(N\), the bound **\(q\ge501\)** is the smallest domain on which a *single exact scalar readout* always separates different limit classes.

Indeed, let \(y=483/100\). Two distinct candidates in different phase classes satisfy the identical reading:
\[
\begin{aligned}
(q,e,d)&=(500,\;2,\;-27938674640336/14145809615083),\\
(p,E,D)&=(501,\;-2,\;56906884259978/28518301075091).
\end{aligned}
\]
Both \(d\) and \(D\) lie in \([-2,2]\), and the exact integer counts are
\[
(C_{500},T_{500})=(7677066992,643545647661),\quad
(C_{501},T_{501})=(7753232942,651222714653).
\]
Direct substitution gives **\(Y_{500}(2,d)=Y_{501}(-2,D)=483/100\)**. This refutes uniform one-read limit-class discrimination for any \(N\le500\); Theorem 1 proves it for \(N=501\).

## Complete all-cutoff exact proof of Theorem 1

The five-labeled-source generating functions are
\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
Multiplying by \((1-z^6)^6\) and \((1-z^6)^7\) respectively yields polynomial numerators
\[
z(1+z+\cdots+z^5)^3(1+z^2+z^4)(1+z^3)
\]
and
\[
z^2(1+z+\cdots+z^5)^4(1+z^2+z^4)(1+z^3)
\]
of degrees 23 and 29. Coefficients of \(z^{6n+r}\) in such numerator divided by \((1-z^6)^m\) are sums of binomial polynomials \(\binom{n-j+m-1}{m-1}\), \(j\le3\) or \(j\le4\). Each early coefficient with \(n<j\) vanishes also in the polynomial extension. Consequently, for each residue \(r\), \(C_{6+r+6k}\) and \(T_{6+r+6k}\) are *exactly* rational polynomials of degrees 5 and 6 for every integer \(k\ge0\). Six and seven direct integer source counts uniquely determine them for the whole infinite residue track.

On the allowed parameter square the readout is strictly increasing in \(e\) and strictly decreasing in \(d\), since \(C_q+d>0\) and \(T_q+e>0\):
\[
\partial_eY_q=\frac{q^3}{C_q+d}>0,\qquad
\partial_dY_q=-\frac{q^3(T_q+e)}{(C_q+d)^2}<0.
\]
Thus \(Y_q(-2,2)\) and \(Y_q(2,-2)\) are the global minimum and maximum for every cutoff.

Set the boundaries \(\theta=(-2,1203/250,11)\) and margin \(\epsilon=1/100\).
A residue class on the **lower** side of \(\theta_i\) requires
\(Y_q(2,-2)<\theta_i-\epsilon\);
one on the **upper** side requires
\(Y_q(-2,2)>\theta_i+\epsilon\).
Only adjacent class boundaries are needed.

For each residue \(r\), let \(n_r=501+(r-501\bmod6)\) and write \(q=n_r+6k\), \(k\ge0\). Insert the exact rational phase polynomials \(C_r(k),T_r(k)\). For the specified corner \((e,d)\), shifted boundary \(b\), and sign \(\sigma=\pm1\), form
\[
P_{r,i}(k)=\sigma\bigl[108q^3(T_r(k)+e)
 -(S(q)+108b)(C_r(k)+d)\bigr].
\]
Take \((e,d)=(2,-2), b=\theta_i-\epsilon,\sigma=-1\) on a lower class, and
\((e,d)=(-2,2),b=\theta_i+\epsilon,\sigma=+1\) on an upper class.
Because \(108(C_r(k)+d)>0\), the desired inequality is equivalent to \(P_{r,i}(k)>0\).

The companion Python/SymPy certificate reconstructs each \(C_r,T_r\) from the labeled integer recurrences, checks surplus interpolation samples, expands the **nine** needed \(P_{r,i}\) over the rationals, and asserts that **all 54 coefficients (degree five per guard) are strictly positive**. The smallest coefficient across every guard equals **\(38502/625>0\)**:

| \(r\) | First \(q\) | Guard(s) | Minimum coefficient(s) |
|---|---:|---|---|
| 0 | 504 | above 11 | \(39582/125\) |
| 1 | 505 | below -2 | \(150282/125\) |
| 2 | 506 | above -2; below 1203/250 | \(31482/125;\;667818/625\) |
| 3 | 501 | above 1203/250; below 11 | \(38502/625;\;142182/125\) |
| 4 | 502 | above -2; below 1203/250 | \(31482/125;\;667818/625\) |
| 5 | 503 | below -2 | \(150282/125\) |

Positive coefficients yield each guard for *every* integer \(k\ge0\); monotonicity extends them to *all* real calibration errors in the specified square. This proves the theorem without a finite cutoff grid or an error-parameter grid.

## Validation, significance and next unit

Run the sibling script **R749SSY_SHARP_PHASE_CLASS_CERT.py** with Python 3 and SymPy. Actual local author run returned **PASS: 9/9 polynomial guards, 54/54 positive rational coefficients, global minimum \(38502/625\), and both exact equal-reading witness states**. Machine JSON records every guard and the rational witness. Evidence level remains AUTHOR_EXACT_NOT_REVIEWED.

The sharp \(q\ge501\) one-read limit-class result improves the looser sufficient \(q\ge953\) bound derived from the symmetric phase envelopes. R749SSX still separately supplies all-pairs eight-read identification for \(6\le p,q\le1000\); R749SST supplies global eleven-read identification. Exact identification and global uniform absolute noise stability are different scientific questions.

The auxiliary six-phase scalar observer retains *labeled* source counts and shared per-candidate errors. It is not directly a native P000 six-axis Cell/Link/Port transition or a physical-time increment; transferring it into native BRC/Enterprise coordinates requires an explicit fiber-, provenance- and future-operation-preserving typed carrier.

**Next open question:** Can two or more readings disambiguate the residues within \(\{1,5\}\) and \(\{2,4\}\) over unbounded cutoffs, and can the finite R749SSX eight-read determinant certificate be upgraded to all distinct \(p,q\ge6\)?
