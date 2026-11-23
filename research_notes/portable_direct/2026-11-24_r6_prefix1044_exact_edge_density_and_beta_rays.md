# PREFIX-1044 — Exact six-phase spectral edge constants and two families of positive Hausdorff rays

**Date:** 2026-11-24 (Asia/Shanghai). **Parent:** PREFIX-1043. **Status:** AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_INTEGER_CROSSCHECK / NOT_REVIEWED.

## Frozen provenance and mathematical scope

The scientific input remains pinned to \`enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\`, P000 V5. Preserve the twelve-direction Stage46 BRC W=J12−6I12, initial incoming −e1, both exclusions of Link {0,e1}, one outgoing negative step and the complete X6 Cell–terminal-port–grade joint observer, including branch, sign, multiplicity, provenance and residual. The following is **only** about the inherited auxiliary six-phase Haar signed scalar observer; its map to the full native BRC state remains NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION.

Inherited SOURCE: PREFIX-1033 (\`fec5c00006e3693121ee18f6d0be661506e06410\`) establishes for Y=|z1+...+z6|² under six independent Haar unit phases, its probability density ρ on [0,36], and the signed continuous contrast density g:
\[
5g=4(H\rho)'-2P\rho+12(11+y)F,\quad H=y^2(36-y)^2,\quad P=y(y-36)(17y-91),
\]
\[
F(y)=\int_y^{36}(6-s)\rho(s)\,ds=\int_0^y(s-6)\rho(s)\,ds.
\]
It also establishes ρ(0)=ρ₀>0, ρ(y)=ρ₀+O(√y), ρ'(y)=O(y^{-1/2}), and a differentiable upper-edge expansion ρ(36−u)=c u^{3/2}+O(u^{5/2}) with c>0. For integers m,k≥0 put n=m+k+1, T∼Beta(m+1,k+1) and
\[
E_{m,k}=\int_0^{36}y^m(36-y)^k g(y)dy,\quad
D_{m,k}=\frac{n\binom{n-1}{m}}{36^n}E_{m,k}=\mathbb E[g(36T)].
\]

## Theorem A — exact upper-edge density

As u↓0,
\[
\boxed{\rho(36-u)=\frac{u^{3/2}}{864\pi^3}+O(u^{5/2})},\qquad
\boxed{g(36-u)=\frac{35}{12\pi^3}u^{5/2}+O(u^{7/2}).}
\]
Both leading constants are strictly positive. This supplies the exact value of c left unspecified in PREFIX-1033.

**Proof.** Remove a common unit-phase rotation by choosing the sixth angle zero. The five relative phases α lie in a torus with normalized volume (2π)^{-5}. The **unique** maximum Y=36 occurs at α=0. Around it,
\[
36-Y(\alpha)=\alpha^{\mathsf T}Q\alpha+O(\|\alpha\|^4),\qquad
Q=6I_5-\boldsymbol1\boldsymbol1^{\mathsf T}.
\]
Its eigenvalues are 1 (once) and 6 (four times), so det Q=6⁴=1296 and √det Q=36. The five-dimensional unit ball has volume V₅=π^{5/2}/Γ(7/2)=8π²/15. Applying the smooth Morse chart and coarea density formula at this isolated nondegenerate maximum yields
\[
\Pr(Y\ge36-u)=\frac{V_5}{(2\pi)^5\sqrt{\det Q}}u^{5/2}+O(u^{7/2})
=\frac{u^{5/2}}{2160\pi^3}+O(u^{7/2}),
\]
\[
\rho(36-u)=\frac{1}{864\pi^3}u^{3/2}+O(u^{5/2}).
\]
The density expansion is **differentiable**: the Morse-chart smooth Jacobian admits radial integration and a differentiated asymptotic, avoiding an unjustified derivative of an arbitrary O-term. Compactness and uniqueness of the maximum prevent another contribution near 36.

Write c=(864π³)^{-1}. Since H(36−u)=1296u²+O(u³) and P(36−u)=−18756u+O(u²), we get
\[
4(H\rho)'=-18144cu^{5/2}+O(u^{7/2}),\qquad
-2P\rho=37512cu^{5/2}+O(u^{7/2}).
\]
Also F(36−u)=∫_{36−u}^{36}(6-s)ρ(s)ds=−12cu^{5/2}+O(u^{7/2}), so
\[
12(11+36-u)F=-6768cu^{5/2}+O(u^{7/2}).
\]
Therefore 5g=(−18144+37512−6768)cu^{5/2}+O(u^{7/2})
=12600cu^{5/2}+O(u^{7/2}), and g=2520cu^{5/2}+O(u^{7/2})=35u^{5/2}/(12π³)+O(u^{7/2}). QED.

**Exact independent moment coefficient.** The same quadratic saddle yields for the six-label collision numbers A₆(r)=E[Y^r]:
\[
\boxed{A_6(r)\sim\frac{27}{4\pi^{5/2}}36^r r^{-5/2}}.
\]
This fills in the unspecified positive leading constant in PREFIX-1017's asymptotic. Equivalently, insert the established edge density into the Laplace integral: (864π³)^{-1}36^{5/2}Γ(5/2)=27/(4π^{5/2}). The finite recurrence crosscheck described below is not used to prove this limit.

## Theorem B — lower-edge coefficient

With ρ₀=ρ(0)>0 as in PREFIX-1032/1033,
\[
\boxed{g(y)=\frac{3024}{5}\rho_0\,y+O(y^{3/2})\quad(y\downarrow0).}
\]
**Proof.** At y↓0, H=1296y²+O(y³), P=3276y+O(y²). The inherited regularity of ρ and its derivative implies 4(Hρ)'=10368ρ₀ y+O(y^{3/2}) and −2Pρ=−6552ρ₀ y+O(y^{3/2}). Moreover F(y)=∫_0^y(s−6)ρ(s)ds=−6ρ₀y+O(y^{3/2}), so 12(11+y)F=−792ρ₀y+O(y^{3/2}). Sum and divide by 5. QED.

## Theorem C — two entire eventual-positive boundary rays

For **each fixed integer k≥0**, as m→∞,
\[
\boxed{D_{m,k}=\frac{22680}{\pi^3}
\frac{\Gamma(k+7/2)}{\Gamma(k+1)}m^{-5/2}
+O_k(m^{-7/2}).}
\]
Consequently for every fixed k there exists M_k with E_{m,k}>0 for all m≥M_k. For the k=0 ray in particular,
\[
\lim_{m\to\infty}m^{5/2}D_{m,0}=\frac{42525}{\pi^{5/2}}>0.
\]
For **each fixed integer m≥0**, as k→∞,
\[
\boxed{D_{m,k}=\frac{108864}{5}\rho_0(m+1)\,k^{-1}
+O_m(k^{-3/2}).}
\]
Consequently for every fixed m there exists K_m with E_{m,k}>0 for all k≥K_m.

**Proof.** Beta fractional moments give for any fixed q>0,
\[
\mathbb E[(1-T)^q]=\frac{\Gamma(k+1+q)\Gamma(m+k+2)}
{\Gamma(k+1)\Gamma(m+k+2+q)},\quad
\mathbb E[T^q]=\frac{\Gamma(m+1+q)\Gamma(m+k+2)}
{\Gamma(m+1)\Gamma(m+k+2+q)}.
\]
Theorem A and global continuity of g yield g(y)=a(36−y)^{5/2}+O((36−y)^{7/2}) **with a finite constant uniformly over [0,36]** (on a compact set away from 36 the quotient by (36−y)^{7/2} is bounded). Here a=35/(12π³). Therefore
\[
D_{m,k}=a36^{5/2}\mathbb E[(1-T)^{5/2}]
+O(\mathbb E[(1-T)^{7/2}])
=\frac{22680}{\pi^3}\frac{\Gamma(k+7/2)}{\Gamma(k+1)}m^{-5/2}
+O_k(m^{-7/2}).
\]
Similarly Theorem B and compactness yield g(y)=b y+O(y^{3/2}) uniformly, with b=3024ρ₀/5. Then
\[
D_{m,k}=36b\,\frac{m+1}{m+k+2}+O(\mathbb E[T^{3/2}])
=\frac{108864}{5}\rho_0(m+1)k^{-1}+O_m(k^{-3/2}).
\]
All Gamma coefficients are positive; E and D have the same sign. QED.

## Validation, meaning and next research unit

Companion \`PREFIX1044_R6_EDGE_COEFFICIENT_CHECK.py\` verifies det Q, all upper-edge/Morse coefficients, the collision asymptotic coefficient, and the k=0 Beta constant symbolically. It also evaluates exact A₆(r) via the all-index recurrence of PREFIX-1035 (through r=200) to provide numerical convergence *crosschecks only*. The proof is the analytic argument above, conditional on the inherited signed-scalar identity; no native BRC execution, independent review or formal acceptance is claimed.

This adds two **unbounded positive families** without needing the very large fixed-ratio thresholds of PREFIX-1043. It does **not** settle full g≥0 on [0,36], the X6–BRC observer equivalence or B_fix,odd(32)∈{19,20}. An efficient next research unit is to obtain explicit edge remainder constants, converting the eventual statements into finite integer thresholds; independently certify remaining interior bands by rigorous spectral enclosures or isolate a negative interval. Preserve authorship and current Task/CLAIM/Activity boundaries.

Provenance: continued historical Researcher-ID EM-DIRECT-780BBE / Activity RA-0ABD84561C86E53067DB0322. This source file does not assert a fresh authenticated execution run or a PROGRESS event.
