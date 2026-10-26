# D25/LIFT — Diagonal Hasse cancellation and nonzero genuine finite-face Ward flux

Date: 2026-10-27. Research lane: \`chatgpt-research-hourly-enterprise-math-20260923\` (not the maintenance lane). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen **scientific** Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged.

**Evidence classification:** \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY\`. This is exact auxiliary corrected-Clausen mathematics, not a source-native authorized checkpoint, original CM/Frobenius experiment, independently reviewed WZ closure, or parent completion.

## Inputs, question and typed carrier

Consume (without recredit) the exact two-parameter master with four authentic finite-face origins, \`20261026_hourly_d25_bivariate_master_ward_r13.md\`, its individual \(J_n^{ab}+E_n^{ab}\) coefficient source, the third-digit six-channel decomposition \`20261026_hourly_d25_third_digit_dual_ward_resonant_face_r11.md\`, and the one-coordinate left face \`20261026_hourly_d25_left_face_harmonic_factor_r14.md\`. The smallest open question is whether the genuine \(k-1,k-2\) cross-Hasse source couplings yield a **new cancellation** on the six-channel diagonal, while keeping finite cutoff boundaries, upper/infinity and ordered high-high sources distinct.

For integer \(m\ge1\), let \(p=6m+1\), \(L=1-2m\), \(N=2m-1\). Let \(\epsilon\) be a **Hasse deformation parameter**, distinct from the fixed geometric rank weight \(2^n\). Define the rational germs
\[
 f_r(\epsilon)=\frac{(-m-\epsilon)_r(-2m-2\epsilon)_r}
 {(1-p/2-3\epsilon)_r\,r!},\qquad 0\le r<p.
\]
For each \(1\le \ell\le2m\), the high index \(p-\ell\) belongs to \([4m+1,6m]\). Its two numerator Pochhammer factors each contain exactly one zero at \(\epsilon=0\); its denominator is nonzero. Hence \(f_{p-\ell}(\epsilon)=\epsilon^2 g_{p-\ell}(\epsilon)\), \(g_{p-\ell}\) regular, with no artificial subtraction. For target primes \(p=6m+1\ge7\), all germ Taylor coefficients and displayed transfer denominators lie in \(\mathbb Z_{(p)}\).

On the actual **ordered finite pairs** \(1\le j,\ell\le2m\), \(n=\ell-j\), put
\[
 \widehat M_n^h(\epsilon)=\epsilon^{-2}
  \sum_{\ell-j=n}j^h f_j(\epsilon)f_{p-\ell}(\epsilon),
 \quad h=0,1,\qquad
 \widehat Y_n=\widehat M_n^1-\frac{p-n}{2}\widehat M_n^0.
\]
Outside \(L\le n\le N\), all moments vanish, in particular \(\widehat Y_{N+1}=0\). For \(k=0,1,2\), the coefficient \([\epsilon^k]\widehat M_n^h\) is the genuine ordered sum of respectively \((0,2)\); \((1,2)+(0,3)\); \((2,2)+(1,3)+(0,4)\). No multiplicities are silently reweighted.

## Theorem 1: exact all-Hasse diagonal cancellation of second-neighbor coupling

Use the inherited **proved** bivariate master identity, with \(C_n=(p-n)(p/2-n)\), \(B_n=-18m^2+9mn-n^2\), and its actual finite face \(\mathcal E_n(t,s)\). On the diagonal \(t=s=\epsilon\), the \(2(t^2-s^2)\) term vanishes **exactly**; the master becomes
\[
\begin{split}
 &(p-2n-6\epsilon)\mathcal M_n^1+
 [-C_n+3\epsilon(p-n)]\mathcal M_n^0\\
 &=(6m-2n-6\epsilon)\mathcal M_{n+1}^1+
 [B_n+(18m-3n)\epsilon]\mathcal M_{n+1}^0+
 \mathcal E_n(\epsilon,\epsilon).
\end{split}
\]
The two polynomial mass coefficients vanish upon centering, because
\[
 (p-2n-6\epsilon)\frac{p-n}{2}-C_n+
 3\epsilon(p-n)=0,
\]
\[
 (6m-2n-6\epsilon)\frac{p-n-1}{2}
 +B_n+(18m-3n)\epsilon=0.
\]
Define \(\widehat E_n=\epsilon^{-2}\mathcal E_n(\epsilon,\epsilon)\), regular because each finite-face term contains an actual high-index \(f_r\) divisible by \(\epsilon^2\). We obtain the **exact rational germ identity**
\[
\boxed{(p-2n-6\epsilon)\widehat Y_n
 -(p-2n-1-6\epsilon)\widehat Y_{n+1}=\widehat E_n.}\tag{1}
\]
This is a genuine source-family WZ/Green telescoping relation: all *interior* summed \(J\) terms have been absorbed as a uniform parameter shift \(p\mapsto p-6\epsilon\); **neither of the two true cutoff origins in each \(\widehat E_n\) is discarded**. The identity is not a proof that those finite faces vanish or that the original scalar \(Q_p\) equals its lower-triangle endpoint.

For reproducibility, the two finite-face populations remain explicitly
\[
\mathcal E_n(\epsilon,\epsilon)=\begin{cases}
 2(m+\epsilon)^2 f_{p-n-1}(\epsilon)
 -(6m^2-8m\epsilon+2\epsilon^2)
 f_{2m-n}(\epsilon)f_{4m}(\epsilon),&n\ge0,\\
 (20m^2-14m\epsilon+2\epsilon^2)
 f_{-n}(\epsilon)f_{p-1}(\epsilon)
 +(2m\epsilon-2\epsilon^2)
 f_{2m}(\epsilon)f_{p-(2m+n+1)}(\epsilon),&n<0.
\end{cases}\tag{2}
\]
Equivalently, if \(Y_{n,k}=[\epsilon^k]\widehat Y_n\), \(E_{n,k}=[\epsilon^k]\widehat E_n\), \(Y_{n,-1}=0\), coefficient extraction yields for **every** \(k\ge0\):
\[
\boxed{(p-2n)Y_{n,k}-(p-2n-1)Y_{n+1,k}
 =6(Y_{n,k-1}-Y_{n+1,k-1})+E_{n,k}.}\tag{3}
\]
In the authentic individually-labelled recurrence this reads
\[
\boxed{\sum_{\substack{a+b=k+2\\a\ge0,\ b\ge2}}J_n^{ab}
 =6(Y_{n,k-1}-Y_{n+1,k-1}).}\tag{4}
\]
For the third digit, \(+2M_{n+1}^{02,0}\) from \((2,2)\) **cancels** \(-2M_{n+1}^{02,0}\) from \((0,4)\), rather than being assumed negligible. This is cross-Hasse cancellation under the **declared diagonal observer**, not separate channel-wise vanishing.

## Theorem 2: full genuine finite-face Green flux has a universal nonzero rank-jet

Let \(q(\epsilon)=p-6\epsilon\). Set
\[
 D_n(\epsilon)=\frac{1}{q-2n-1}
   \prod_{r=n+1}^{N}\frac{q-2r}{q-2r-1},
 \quad
 P(\epsilon)=\prod_{r=L}^{N}\frac{q-2r}{q-2r-1}.
\]
All denominators have \(p\)-unit constant term. Forward iteration of (1), with the *actual* empty terminal rank \(\widehat Y_{N+1}=0\), gives the exact source-labelled **finite-face flux identity**
\[
\boxed{\mathfrak F_p(\epsilon):=\sum_{n=L}^{N}
D_n(\epsilon)\widehat E_n(\epsilon)
=P(\epsilon)\widehat Y_L(\epsilon).}\tag{5}
\]
The sole nonunit factor in the numerator of \(P\) is the factor \(q-0=p-6\epsilon\) at \(r=0\), so
\[
 P(\epsilon)=(p-6\epsilon)U_p(\epsilon),
 \qquad U_p(\epsilon)\in\mathbb Z_{(p)}[[\epsilon]]^\times.
\]
The actual extreme cell is \((j,\ell)=(2m,1)\); hence
\[
 \widehat Y_L(\epsilon)
 =-2m\,\epsilon^{-2}f_{2m}(\epsilon)f_{p-1}(\epsilon)
 =a_p\epsilon+O(\epsilon^2),
 \quad
 a_p=-2m\,u_{1,2m}u_{2,p-1}\in\mathbb Z_{(p)}^\times.
\]
Consequently \([\epsilon^0]\mathfrak F_p=0\) **exactly**, and
\[
 [\epsilon^1]\mathfrak F_p=p\,U_p(0)a_p,\qquad
 \boxed{[\epsilon^2]\mathfrak F_p\equiv
 -6\,U_p(0)a_p\ne0\pmod p.}\tag{6}
\]
Both factors on the right are proved units (also \(6\in\mathbb Z_{(p)}^\times\)). An explicit residue is
\[
 U_p(0)=\frac1{p-1}\prod_{\substack{L\le r\le N\\r\ne0}}
 \frac{p-2r}{p-2r-1}
 \equiv-\prod_{j=1}^{N}\frac{4j^2}{4j^2-1}\pmod p.
\]
Thus **for every target prime** the genuinely labelled *full-rank finite-face* flux has a nonzero second Hasse jet modulo \(p\). This is a constructive obstruction to declaring that **this particular all-rank diagonal flux vanishes identically**. It is **not** an obstruction to additional cancellation after adjoining the different geometric \(2^n\) observer, positive/infinity \(Z^+\), high-high \(H_p\), or the original CM/Frobenius source. No unsupported promotion from \(\widehat Y\) to the original normalized \(Q_p\) is made.

## Executed finite and exact checks

Companion \`20261027_hourly_d25_diagonal_hasse_ward_flux_r15_check.py\` independently computes Taylor jets through degree four from the original Pochhammer recurrence modulo \(p^3\), all **genuine** ordered finite-channel moments, all six **separate** \(J_n^{ab}\) expressions, and both authentic finite-face terms. Across 23 primes (\(p\equiv1\bmod6\) in \([7,211]\), plus \(p=733\)): **11,742** exact modular assertions for (3)/(4) all pass. A second, source-side computation of the products \(D_n(\epsilon)\) and \(\sum D_n E_n\), independently of the left boundary, confirms **23** nonzero jet-flux certificates.

| Prime | \(U_p(0)\bmod p\) | \(a_p\bmod p\) | \([\epsilon^2]\mathfrak F_p\bmod p\) |
|---:|---:|---:|---:|
| 13 | 5 | 9 | **3** |
| 733 | 663 | 610 | **383** |

The general statements follow from the exact rational-germ proof, **not** by extrapolating the finite tests. A separate author scratch computation also checked 72 exact rational rank equations for \(m=1,2,3,4\) at two nonzero rational parameter values; this is not a substitute for the proof. No external runtime or independent native original-class experiment is asserted.

## BRC / Enterprise-coordinate usage and next precise frontier

**BRC COMPOSE_APPLIED.** Carrier = ordered \((j,\ell)\) provenance, Hasse order, signed difference rank, \(p\)-local valuations and two true finite cutoff source origins. Diagonal composition is a proven, restricted observer port; it is *not* an arbitrary erasure of six Hasse labels. The nonzero coefficient (6) is a retained residual. These are external auxiliary hypergeometric ranks, **not** P000 native X6 spatial axes; P000 and the ACTIVE finite-resolution/residual-faithful worldview remain unchanged.

Next smallest unfinished unit: apply the now-proved diagonal shift law at the **fixed original geometric base \(2\)** to the lower \(n\le0\) observer and the independently oriented positive/infinity observer, with the third-digit finite left-face factor from r14 and ordered high-high \(H_p\) still separated. Determine whether the complete original six-channel signed Clausen scalar admits further cancellation; if not, record a source-tagged nonzero residual on that exact observer. Original-class same-class \(H_0/B_0\), \([X]U\bmod p^2\), normalized semilinear Frobenius \(\eta\), \(\kappa\), \(\Delta_p-R_p\), native experiments and independent Driver review remain OPEN. No prior native Source checkpoint, claim, session, staging, or frozen scientific pin is modified by this portable note.