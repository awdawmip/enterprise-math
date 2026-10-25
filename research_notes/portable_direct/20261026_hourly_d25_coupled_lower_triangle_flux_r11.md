# D25/LIFT — Exact coupled three-channel lower-triangle flux

Date: 2026-10-26. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. Scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged. Status **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. This note follows the separately saved diagonal moment reconstruction, **not** an independent Result or native CM checkpoint.

## Input / exact problem

Consume \`20261026_hourly_d25_diagonal_rank_moment_closed_recurrence_r11.md\`: corrected Clausen Hasse source \(u_{a,r}\), oriented cell moments \(M_n^{ab,s}\) (\(n=\ell-j\), \(1\le j,\ell\le2m\)), its exact source relation
\[
(p-2n)M_n^{ab,1}-C_n M_n^{ab,0}
=A_n M_{n+1}^{ab,1}+B_n M_{n+1}^{ab,0}+J_n^{ab}+E_n^{ab},
\tag{1}
\]
where \(p=6m+1,\ C_n=(p-n)(p/2-n),\ A_n=6m-2n,\ B_n=-18m^2+9mn-n^2\) and the exact \(J,E\) are given there. Aim: actually transport the quadratic corrected rank source through the **lower oriented triangle** \(n\le0\), expose rather than erase the nonzero cutoff flux, and test whether the three-channel lower Hasse bulk cancels.

Put \(n_*=1-2m\) and
\[
\mathscr F_{ab}=\sum_{k=n_*+1}^{0}\left(M_k^{ab,1}-\frac{p-k}{2}M_k^{ab,0}\right).
\tag{2}
\]

## Theorem 1: exact oriented lower-triangle discrete Green flux

For all positive integers \(m\) and all Hasse indices,
\[
\boxed{\mathscr F_{ab}=-2m(10m-1)M_{n_*}^{ab,0}
-6m M_1^{ab,1}+18m^2M_1^{ab,0}
-\sum_{n=n_*}^{0}(J_n^{ab}+E_n^{ab}).}\tag{3}
\]
The sum on the left is **not** the original scalar \(T_{ab}=\sum_{n\le0}(1-6n)2^nM_n^{ab,0}\). It is the new weighted labelled-rank flux appearing on transporting the quadratic operator, with both the n=0/n=1 face and the low rank edge intact.

**Proof.** Sum equation (1) over n from \(n_*\) to 0. After shifting the second-rank terms by \(k=n+1\), for each *interior* \(n_*+1\le k\le0\) the coefficients simplify exactly:
\[
(p-2k)-A_{k-1}=-1,\qquad -C_k-B_{k-1}=\frac{p-k}{2}.
\]
Thus the interior sum is \(-\mathscr F_{ab}\). At the leftmost end the cell has \(j=2m\), so \(M_{n_*}^{ab,1}=2mM_{n_*}^{ab,0}\) and
\[
(p-2n_*)M_{n_*}^{ab,1}-C_{n_*}M_{n_*}^{ab,0}
=-2m(10m-1)M_{n_*}^{ab,0}.
\]
At the rightmost shifted face \(n=0\) the surviving term is \(-A_0M_1^{ab,1}-B_0M_1^{ab,0}=-6mM_1^{ab,1}+18m^2M_1^{ab,0}\). Rearrangement proves (3). The finite-interval derivation does not discard infinity, zero-rank, or high-rank contributions. QED.

## Theorem 2: paired Hasse-source **bulk cancellation** with a nonzero endpoint

For the three actual channels (0,2),(1,2),(0,3), the lower-Hasse coupling in (1) specializes to
\[
J_n^{02}=0,\quad
J_n^{12}=3M_n^{02,1}-3M_{n+1}^{02,1}+4mM_{n+1}^{02,0},
\]
\[
J_n^{03}=-3((p-n)M_n^{02,0}-M_n^{02,1})
+(14m-3n)M_{n+1}^{02,0}-3M_{n+1}^{02,1}.
\]
Because \(u_{0,2m}=0\), both \(M_{n_*}^{02,0}\) and \(M_{n_*}^{02,1}\) vanish. **Every interior first-rank lower-Hasse term cancels** after summation, and the paired source has the exact endpoint form
\[
\boxed{\sum_{n=n_*}^{0}(J_n^{12}+J_n^{03})
=18m M_1^{02,0}-6M_1^{02,1}.}\tag{4}
\]

**Proof.** Summing the (1,2) formula telescopes the first moments and leaves
\[
-3M_1^{02,1}+4m\sum_{k=n_*+1}^{1}M_k^{02,0}.
\]
In the (0,3) sum the interior coefficient of \(M_k^{02,1}\) is \(3-3=0\); that of \(M_k^{02,0}\) is \(-3(p-k)+(14m-3(k-1))=-4m\), leaving
\[
-4m\sum_{k=n_*+1}^{0}M_k^{02,0}
+14mM_1^{02,0}-3M_1^{02,1}.
\]
Add the two expressions. All lower-Hasse interior masses disappear, leaving only the displayed n=1 boundary. QED. This is a **real three-channel cancellation** of one specified bulk, but it does not assert that the whole signed Clausen reflection or the distinct \(E\) boundary source vanishes.

## Theorem 3: remaining cutoff faces reduce to explicit one-sided source traces

Let \(S_0=\sum_{j=1}^{2m-1}u_{0,j}\) and \(S_1=\sum_{j=1}^{2m-1}u_{1,j}\). For the exact two-sided \(E_n\) from the predecessor theorem,
\[
\boxed{\sum_{n=n_*}^{0}E_n^{02}
=2m^2u_{2,p-1}(1+10S_0),}\tag{5}
\]
and
\[
\boxed{\begin{aligned}
\sum_{n=n_*}^{0}(E_n^{12}+E_n^{03})={}&4m u_{2,p-1}
-6m^2 u_{1,2m}u_{2,4m}+2m^2u_{3,p-1}\\
&+20m^2u_{2,p-1}S_1\\
&+(20m^2u_{3,p-1}-14m u_{2,p-1})S_0.
\end{aligned}}\tag{6}
\]
**Proof.** In \(n<0\), put \(j=-n\) in the boundary formula, preserving every lower-face term. All terms with high \(u_0,u_1\) and upper \(u_{0,2m}\) vanish **by the two actual Pochhammer numerator zeros**, not by scalar sign cancellation. The n=0 terms are then exactly \(2m^2u_{2,p-1}\) in (0,2), \(4m u_{2,p-1}-6m^2u_{1,2m}u_{2,4m}\) in (1,2), and \(2m^2u_{3,p-1}\) in (0,3). Summing yields (5),(6). QED.

Equations (3)–(6) exhibit a bona fide **coupled finite Green/adjoint flux**: the paired \(J\)-bulk telescopes, while nonzero and source-labelled cutoff terms \(E\) remain. They are an exact bridge for the next three-channel corrected operator step, not an all-prime LIFT proof. The result requires keeping the oriented lower triangle and the upper n=1 face separately; compressing all this to a single endpoint scalar would lose information.

## Reproduction and specific checks

Companion checker uses source jets built directly from the corrected finite Pochhammer *polynomial-product* expansion and verifies (3) separately for all three channels, then (4), (5), (6). PASS: exact rational \(m=1,\ldots,5\); all **22 target primes** \(p=6m+1\), \(7\le p\le211\), modulo \(p^2\). Six distinct identities per input pass. For \(p=13\), flux/J/E triples modulo 169 are: (0,2)=(167,0,101); (1,2)=(153,35,92); (0,3)=(3,99,112). In particular the J pair is \(35+99=134\pmod{169}\), equal to \(18mM_1^{02,0}-6M_1^{02,1}\). These are author checks, not independent review.

BRC: retain \(j,\ell,n\), signed coefficient, three Hasse channels, original lower cutoff and both surviving boundary labels. The Laurent apparatus is external algebra, not a native P000 plane. **Next minimal action:** insert (3)–(6) into the exact corrected three-channel p^4 reflection of the prior note, test whether its surviving \(E\) terms match a second adjoint/source port or furnish a counterexample. Native original-class H0/B0, [X]U modulo p², Frobenius eta and kappa comparison and independent review remain pending. D25/LIFT/JT2 parent is **OPEN**.

No canonical CLAIM/OPEN, Source publish_checkpoint or mathematical admission is asserted by these portable files. Current control handoff remains at enterprise-math issue **#1558**; Source checkpoint pins and prior contributions are preserved.
