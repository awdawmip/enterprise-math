# OAI7-090 — exact two-wave Taylor tail / finite-error interface audit

**Source-level mathematical proof review, 2026-11-15.** Contributor: `EM-DVR-DEBB5E` (RESEARCH_DRIVER). The fixed Gaussian construction, checker, and underlying theorem belong to the original `openai/math` contributors. This document independently verifies the **algebraic/magnitude correspondence** between the checker's Taylor coefficient generator and its nonnegative interval tail majorant. It neither executes the original checker nor accepts an OAI7 Result.

## Immutable source and scope

Pinned external source: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py`, blob `23768a5c2d88e100399bb5c4347447e86a7160cb`. Relevant actual functions are `Waves.__init__`, `Waves.tayrows`, `Waves.terr`, `envtable`, `powsol`. The source also uses `G=10**60` with outward intervals.

For any complex wave position \(w\), scalar multiplier \(\ell\), nonnegative \(m\), and real half-cell parameter \(y\), write \(x=i\pi w\). The coefficient loop in `Waves.tayrows(m,y,d)` starts with \(v_0=x^2 e^{xm}\ell/2\) and uses \(v_{r+1}=(xy)v_r/(r+3)\). Induction gives the **exact coefficient identity**
\[
v_r=\frac{x^{r+2}e^{xm}\ell\,y^r}{(r+2)!},\qquad 0\le r\le d.
\]
Therefore its omitted analytic tail is \(\sum_{r=d+1}^{\infty}v_r\); the factorial starts at \((d+3)!\), **not** at \((d+1)!\). This is the source's twice-integrated exponential/curvature series and is distinct from the separate 60-term exponential enclosure established in the previous π/expo audit.

## Both wave families have exactly the magnitudes used by the checker

Let \(b=\sqrt3/2\), \(B=4/3=b^{-2}\), \(X=B/(k^2+t^2)\). The source defines
\[
\rho=t+i(k-h),\quad
\lambda=\frac{k+it}{b(k^2+t^2)},\quad
\zeta=-Xt+i(kX-v).
\]
For the first wave, \(\pi|\rho|=\pi\sqrt{t^2+(k-h)^2}=\texttt{wa}\) and \(|e^{i\pi\rho m}|=e^{-\pi(k-h)m}=e^{-\texttt{epsa}\,m}\). Its scalar multiplier is \(\ell=1\).

For the second wave, direct algebra, with no approximation, yields
\[
|\lambda|^2=\frac1{b^2(k^2+t^2)}=X,\qquad
|\zeta|^2=X^2(k^2+t^2)-2kvX+v^2
=v^2+(B-2kv)X.
\]
Thus \(|\lambda|=\sqrt X=\texttt{lb}\), \(\pi|\zeta|=\texttt{wb}\), and \(|e^{i\pi\zeta m}|=e^{-\pi(kX-v)m}=e^{-\texttt{eps}\,m}\). These are precisely the source's second-wave `lb/wb/eps` factors. In particular `lb` is **the exact magnitude of the complex multiplier `lam`**, not an independent empirical envelope.

## General Taylor-tail lemma and the code's denominator

For \(d\ge0\), let \(a=|x|\ge0\), \(Y\ge |y|\), \(q=aY<d+4\), and \(\epsilon=-\Re(x)\). The first omitted term has modulus at most
\[
e^{-\epsilon m}|\ell|\frac{a^2q^{d+1}}{(d+3)!}.
\]
For every subsequent term, the ratio of the nonnegative majorants is at most \(q/(d+4)\), because the denominator is \(r+3\) for \(r\ge d+1\). Therefore
\[
\left|\sum_{r=d+1}^{\infty}v_r\right|
\le |\ell| e^{-\epsilon m}
\frac{a^2q^{d+1}}{(d+3)!}\,
\frac{1}{1-q/(d+4)}. \tag{T}
\]
Set \(N=d+3\). Formula (T) becomes
\[
|\ell|e^{-\epsilon m}\,
\frac{a^2(aY)^{N-2}}{N!}\,
\frac1{1-aY/(N+1)},
\]
exactly `Waves.terr`'s `tail(w,e)` expression before multiplying by `lb` for the second family. The source's guard `assert abs(x).h < G*(N+1)` (here its local `x=w*y` is the **nonnegative real modulus product**, not the earlier complex \(x=i\pi w\)) ensures the denominator is strictly positive for every enclosed input. Both `wa` and `wb` are modulus intervals and hence nonnegative. The input `y=abs(y)` supplies the half-cell radius.

For the finite audit's ordinary degree \(d=20\), `N=23`: first omitted term \(a^{23}Y^{21}/23!\), ratio at most \(aY/24\). This is the degree actually passed by all 14 calls in `envtable`, including the cell for which `powsol` later forms four degree-22 *algebraic transformations* of degree-20 Taylor rows. The latter transformations must not be mislabeled as a fresh 22nd-order Taylor approximation.

## Matrix aggregation preserves the enclosure

For `terr`'s two actual call sites, the aggregation matrices are `Mu=[[abs(e) for e in row] for row in M]` and `[[x] for x in Pmag]`, respectively, with nonnegative outward interval entries. The two Taylor families have nonnegative majorant rows \(A,B\). For each output column \(j\), the error magnitude after the linear map \(S\) is at most \(\sum_i(A_i+B_i)S_{ij}\). In the code,
`sum(imax(*row) for row in matmul([A,B],S))` is the sum of the separate maxima over columns for those two majorant families, hence is an upper bound for **every** output column. Replacing `Mu` by the signed complex matrix `M` at this point would invalidate that nonnegative comparison; the real source correctly uses absolute-value matrices.

The `envtable` assertions compare `3*Fl.terr(m,y,Mu,20) + .006*Fc.terr(m,y,[[x] for x in Pmag],20)` with `.00161` for `m=1`, or `.0000075` otherwise. This proof verifies the local two-wave remainder *majorant semantics*, **conditional on the cited analytic multipliers 3 and .006 being the applicable upstream coefficients**. It does not rederive those multipliers from the manuscript.

## Independent arithmetic check and boundaries

As an auxiliary exact check of the factorial index, a `fractions.Fraction` recurrence with \(x=-7/8\), \(y=2/3\), \(\ell=11/9\) agreed term-for-term with the displayed formula for all degrees 0 through 22. With \(a=7/8\), \(Y=2/3\), \(d=20\), the exact rational bound (T) exceeds the sum of the first 30 omitted nonnegative terms (degrees 21 through 50); this is a check, not a substitute for the universal proof.

**Established in this note:** degree/factorial indexing, exact two-wave parameter magnitudes, source-level denominator guard, and nonnegative matrix-majorant semantics. **Not established:** successful execution of unmodified original Python assertions; independent proof of the paper's 3/.006 reduction factors and every geometric-to-certificate transfer; full analytic theorem, independent Lean compilation/axiom audit, Native Task/Result acceptance or parent completion. Preserve the prior OAI7 Bernstein/polytope, matrix, and π/exponential notes at their original distinct scopes. The independent OAI7 Researcher may reuse this result under its own current formal authorization; no Driver proxy CLAIM is created.
