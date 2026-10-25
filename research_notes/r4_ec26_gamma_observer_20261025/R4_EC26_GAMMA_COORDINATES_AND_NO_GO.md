# R4-EC26 — Exact gamma observer of the auxiliary BRC clean-source kernel

**Date:** 2026-10-25. **Status:** author-side algebraic proof plus exact finite checks; not a native Result, independent Driver review, or Foundation acceptance.

## Source and model boundary

- GLOBAL_KNOWLEDGE_V1: canonical \`main@7515b2608fd59fd51900b266efac05b023e79057\`; both universal entry files, P000 startup and original matching blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`, ACTIVE worldview and scoped research policies read at this snapshot.
- Enterprise Math: canonical \`main@5112b02283d53205fc96651c61b204ee41bf28da\`; current \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, TASK research entry, P000 companion, native X6/time, and joint-observer preservation contracts read at this separate pinned snapshot.
- Scientific predecessor: EC25 author-side result at \`3aaedf6d604ed9b57a6f462d29d4f5801e923bd3\`. This study changes the route from sequential higher Newton orders to a uniform all-grade auxiliary observer.
- Connected GitHub principal: \`awdawmip\`. Native task/Owner lookup returned \`CONTROL_QUOTA\`; direct service-issued session start returned \`STATIC_READONLY_SCOPE_DENIED\` with \`operation_sent=false\`. Active Owner and CLAIM were not established. This is independently scoped *author-side* mathematical analysis, not another task's execution.
- **Carrier:** existing positive-weight ordered binary affine auxiliary BRC, with exact clean-provenance counts. \`E[n,j]\` is a finite nonnegative count; the gamma coordinates below are a *signed change of basis*, not signed BRC branch weights. There is no native six-dimensional X6 embedding, update law, heartbeat-time inference, physical calibration or claim of transfer from this auxiliary object.

## Definitions

Write the verified auxiliary symmetric kernel
\[
E(x,u)=\sum_{n\ge0}E_n(u)x^n
=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6}.
\tag{1}
\]
Its coefficients satisfy \(E_n(u)=u^nE_n(u^{-1})\); the following theorem gives a self-contained second proof of this palindromicity. Define unique coordinates
\[
E_n(u)=\sum_{k=0}^{\lfloor n/2\rfloor}
\gamma_{n,k}u^k(1+u)^{n-2k}
\quad(n\ge0).
\tag{2}
\]
This is the **gamma-basis observer**; it is invertible on palindromic polynomials but is not coefficientwise positivity preserving.

## Theorem A — universal exact gamma transform

For formal variables \(y,v\), put
\[
\Gamma(y,v)=\sum_{n,k\ge0}\gamma_{n,k}y^nv^k.
\]
Then the following exact identity of formal power series holds:
\[
\boxed{\Gamma(y,v)=
\frac{1-vy^2}{1-y+2v^2y^4-v^3y^6}.}
\tag{A}
\]

**Proof.** Substitute \(x=y/(1+u)\) in (1), and denote \(v=u/(1+u)^2\). After multiplying \(E_n(u)\) by \((1+u)^{-n}\), the numerator becomes \(1-vy^2\) and the denominator becomes \(1-y+2v^2y^4-v^3y^6\). Expanding the result as a formal series in \(y\) proves (A). Every monomial contributing \(v^k\) has \(y\)-degree at least \(2k\), so \(\deg_v[y^n]\Gamma\le\lfloor n/2\rfloor\). Re-substitution yields (2), proving existence and palindromicity; triangularity of its basis proves uniqueness. \(\square\)

## Theorem B — finite closed binomial formula for every depth and grade

Let \(\binom Nm=0\) when \(N<m\) for nonnegative \(N,m\). Then for all \(0\le k\le\lfloor n/2\rfloor\),
\[
\boxed{
\begin{aligned}
\gamma_{n,k}
=\sum_{a,b\ge0}(-2)^a\binom{a+b}{a}
\bigg[
 &{\bf1}_{2a+3b=k}\binom{n-3a-5b}{a+b}\\
-&{\bf1}_{2a+3b=k-1}\binom{n-2-3a-5b}{a+b}
\bigg].
\end{aligned}}
\tag{B}
\]
Only finitely many pairs contribute to a fixed \(k\); each binomial term is interpreted as zero unless its top is at least its lower argument. Formula (B) additionally has a canonical polynomial extension in the variable \(n\) using falling-factorial binomials.

**Proof.** Expand (A) formally as
\[
\Gamma=\sum_{a,b\ge0}(-2)^a\binom{a+b}{a}
\frac{v^{2a+3b}y^{4a+6b}(1-vy^2)}
{(1-y)^{a+b+1}}.
\tag{3}
\]
Here the factor \((-2)^a\) comes from choosing \(a\) copies of the positive \(2v^2y^4\) denominator term with the alternating geometric sign, while \(b\) copies of the negative \(v^3y^6\) term cancel their geometric signs. Apply \([y^q](1-y)^{-m-1}=\binom{q+m}{m}\) to the two numerator terms, obtaining (B). \(\square\)

## Theorem C — all-grade obstruction to gamma positivity, boundary roots and eventual signs

(i) For **every** \(n\ge2\), \(\gamma_{n,1}=-1\); for every \(n\ge4\),
\[
\boxed{\gamma_{n,2}=-2(n-3).}
\tag{C1}
\]
In particular, even the nonnegative palindromic clean-source polynomial \(E_2(u)=1+u+u^2\) is not gamma-positive. Hence a proof of E-unimodality **cannot rely on global gamma-positivity of this exact family**. The claim says nothing negative about the original path counts.

(ii) For fixed \(k\), the right-hand side of (B), interpreted with polynomial binomial coefficients, is a polynomial \(G_k(n)\). For \(k=0\), \(G_0=1\); for \(k=1\), \(G_1=-1\). For \(m\ge1\),
\[
\deg G_{2m}=m,\qquad [n^m]G_{2m}=\frac{(-2)^m}{m!},
\tag{C2}
\]
and
\[
\deg G_{2m+1}=m,\qquad [n^m]G_{2m+1}
=\frac{(m+2)(-2)^{m-1}}{m!}.
\tag{C3}
\]
Therefore for each fixed \(k\), the gamma coordinate has an **eventually fixed, explicitly known sign**, with infinitely many grades whose eventual sign is negative (for instance \(k\equiv2\pmod4\), and odd \(k\equiv1\pmod4\) with \(k\ge5\)).

(iii) For every \(k\ge2\), put \(L=\lfloor(k+1)/3\rfloor\). The following is an **exact divisibility statement over \(\mathbb Q[n]\)**:
\[
\boxed{
\prod_{\ell=1}^{L}(n-2k+\ell)\ \mid\ G_k(n).
}
\tag{C4}
\]
These roots are *polynomial-extension roots* outside \(n\ge2k\), not extra physical path-count statements.

**Proof.** The \(k=1\) term in (B) is solely the shifted numerator contribution \(a=b=0\), giving \(-1\); the \(k=2\) term is solely \(a=1,b=0\), giving \(-2(n-3)\). For (ii), the degree of a summand is \(a+b\). In the even case \(k=2m\), the unique degree-\(m\) term is \(a=m,b=0\) in the first sum; all other terms have lower degree. In the odd case \(k=2m+1\), the only degree-\(m\) terms are \(a=m-1,b=1\) in the first sum and \(a=m,b=0\) in the subtracted sum. Their combined leading coefficient equals \(\{m(-2)^{m-1}-(-2)^m\}/m!=(m+2)(-2)^{m-1}/m!\). The respective leading coefficients are nonzero, proving exact degrees and eventual signs.

For (iii), every contributing pair has \(a+b\ge L\): if \(2a+3b=k\) or \(k-1\), then \(3(a+b)\ge k-1\). Evaluate the polynomial version of each binomial summand at \(n=2k-\ell\), \(1\le\ell\le L\). In either the unshifted or shifted contribution the binomial top becomes \(a+b-\ell\), lying between \(0\) and \(a+b-1\). Its falling-factorial binomial is therefore exactly zero. Thus \(G_k\) has the \(L\) distinct listed roots, proving (C4). \(\square\)

## Exact finite evidence and reproducibility

An independently implemented exact \(E_n(u)\) recurrence from (1) was compared with the gamma recurrence from (A), with the inverse basis reconstruction (2), and with the separate finite sum (B). The standard-library-only complete verifier \`EC26_verify.py\` generated \`EC26_report.json\`:
- \(0\le n\le110\): 6,216 reconstructed exact polynomial coefficients and 6,216 palindromic coefficients matched.
- 3,136 exact \((n,k)\) comparisons with the finite binomial sum (B).
- Grades \(2\le k\le36\): 222 exact polynomial-extension root checks and 35 exact leading-coefficient/degree checks using forward differences.
- Exact examples: \(E_{10}=[1,9,23,23,25,26,25,23,23,9,1]\), \(\gamma_{10}=[1,-1,-14,15,21,-8]\), and \(\gamma_{16,8}=-2\).

These checks are **finite regression evidence**, not the proof of (A)–(C). The proof is formal algebra over \(\mathbb Q\) and does not require floating-point arithmetic. No native X6 dynamics or independent formal mathematics review was performed.

## BRC observer audit and next unit

**REUSE_APPLIED:** the existing exact positive BRC provenance kernel (1) and EC20–EC25 symbolic coefficient interface. The new gamma observer is information-preserving for each complete palindromic polynomial because (2) is an invertible triangular basis. However it is **not positivity-preserving**: negative gamma values cannot be treated as signed branch cancellation or negative original source masses.

**New eliminated shortcut:** global gamma positivity and any unimodality argument requiring it. This obstruction holds uniformly in \(n\), not merely for one exceptional shallow depth.

**R4-EC27:** seek an alternative exact, provenance-compatible decomposition of the *first differences* \(E[n,j]-E[n,j-1]\) with nonnegative certificates over \(n\ge10,\,1\le j\le\lfloor n/2\rfloor\), or produce a certified counterexample. Retain the EC19 finite-width theorem and EC18 parabolic wedge without rerunning them. Treat the near-center six offsets and low-order Newton coefficients as open. The native X6 mapping, time semantics, service-issued execution/CLAIM and independent Driver assessment remain separate obligations.
