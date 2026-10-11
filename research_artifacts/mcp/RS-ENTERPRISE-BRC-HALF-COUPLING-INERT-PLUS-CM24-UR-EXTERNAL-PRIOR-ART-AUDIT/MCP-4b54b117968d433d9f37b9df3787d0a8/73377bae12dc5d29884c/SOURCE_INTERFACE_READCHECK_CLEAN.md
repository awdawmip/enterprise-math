# Fixed Betina–Lecouturier v3: oriented first-normal interface gate

**Overall: NORM_ONLY_WITH_GAP for this Task interface.** The fixed paper supplies a marked full-level-3 coordinate, raw theta/period objects, cusp and graph conventions, and a residual diagonal pairing formula. It does **not** expressly identify a separately calibrated, norm-before first-normal scalar with the Task's $G_p$, or prescribe the Task's rational hypergeometric lift $z_{\mathrm{Task}}=1/2\pmod{p^2}$. This is a bounded source-interface finding, not a claim that the paper is false, that its raw objects do not exist, or that no future bridge can exist.

This is a directed, shared-context local readcheck, not a formal independent DR. Only the existing frozen v3 TeX and PDF were read. No remote read/write, provider query, registration, claim, open, native mutation, or Source/GK mutation was made. The preceding 14-unit marked coordinate normalization is taken as a condition and is not rederived here. No multiplier $c$ is selected by matching the desired answer.

This file is a formatting revision of **SOURCE_INTERFACE_READCHECK.md**. The original frozen report is preserved unchanged. Formula delimiters and escaped control characters are repaired; the mathematical assessment and scope are unchanged.

## Exact frozen intake and locators

Both complete files matched the previously saved bytes:

| Source | Bytes | SHA-256 |
| --- | ---: | --- |
| Original v3 TeX, 705 lines | 63224 | 81835e700f2cec78a89cd9e4b81b155f7b086035521f2efe2cdba19d75a0242b |
| Original v3 PDF, 22 pages | 258570 | 03117b4ce827afdbd61c21464c9a40b693f330a79e687590d6f4ec26ad1705fe |

Primary reference: Betina–Lecouturier, *On the p-adic periods of the modular curve X(Γ₀(p)∩Γ(2))*, arXiv:1611.01044v3. The stored original files, rather than a new external response, are the evidence for this gate. PDF pp. 20–21 agree with TeX 620–662 on the complete $N=3$ appendix; TeX 664–705 contains only references and the document end. Hashes and exact numbered locator extracts are in **FIXED_SOURCE_FULL_DIGEST_AND_LOCATORS.json**.

## What is explicit, and what the requested interface still needs

Here $K_{\mathrm{fld}}/\mathbf{Q}_p$ denotes the unramified quadratic field, $k=\mathbf{F}_{p^2}$; it is distinct from the congruence subgroup also called $K$ in Appendix 7.2. The Task's hypergeometric coordinate is denoted $z_{\mathrm{Task}}$, to distinguish it from the paper's upper-half-plane and Schottky coordinates $z$.

The source's eta formula, with its upper-half-plane variable $z$, is exactly:

$$
H(z)=\left(\frac{\eta\left(\frac{z}{3(1-z)}\right)}{\eta\left(\frac{3z}{1-z}\right)}\right)^3.
$$

It does not substitute the algebraic-base variable $z_{\mathrm{Task}}$ for that source variable.

| Object | Field / quotient | Normal datum and lift | Classification for this interface |
| --- | --- | --- | --- |
| $K_{\mathrm{fld}},k$ | Unramified quadratic field and its residue field; no quotient in their definition | Introduction fixes the base field; it does not select a Task lift | EXPLICIT, TeX 103, 111 |
| Full-level-3 $H$ | Rational base coordinate defined over $\mathbf{Z}[1/3]$, with its characteristic-zero eta expression | The source's formula above fixes the coordinate, not a mod-$p^2$ lift at $z_{\mathrm{Task}}=1/2$ | EXPLICIT, TeX 622–635; PDF p. 20 |
| Marked algebraic $a_i=P'_H(H_i)^{-1}$ | $k^\times$, before taking a field norm | Once the already fixed $H$-marking and distinct supersingular $H_i$'s are retained, $a_i=\prod_{j\ne i}(H_i-H_j)^{-1}$ is a well-defined oriented algebraic factor | CONDITIONAL on that frozen marked-root input, not an absent object; the paper does not name it a Task first-normal scalar |
| Residual diagonal period $\bar{\Phi}(e_i,e_i)/p$ | $K_{\mathrm{fld}}^\times/U_1(K_{\mathrm{fld}})$, unit residue in $k^\times$ after dividing by $p$ | The stated $N=3$ analogue, obtained by $\lambda\to H$, gives $a_i^{p+1}=N_{k/\mathbf{F}_p}(a_i)$ | NORM_ONLY_WITH_GAP, Theorem 1.1 TeX 132–148 plus 662; PDF p. 3 and p. 21 |
| Raw $\theta(a,b;z)$ and augmentation-group $\Phi(\alpha,\beta)$ | Actual $K_{\mathrm{fld}}^\times$-valued meromorphic objects/period ratios, before principal-unit reduction | Independently defined on the Schottky half-plane. They are not merely zero-order or norm symbols | Their existence is EXPLICIT, TeX 294–335; selecting an $N=3$ Task scalar from them remains CONDITIONAL |
| Extension $\Phi(e_i,e_j)$ | Raw $K_{\mathrm{fld}}^\times$ in the main $N=2$ construction; residual $N=3$ analogue asserted | The main extension uses a cusp limit with $\lambda'\circ\tau$ and theta ratios. Appendix 7.2 does not print a separate $N=3$ limit and an equality to $G_p$ | CONDITIONAL for the Task interface; TeX 337–380, 662 |
| $c',c$, graph/annulus orientation | Cusp sections / oriented edges, not a mod-$p^2$ supersingular lift | The appendix fixes $c'$ above cusp $[1]_{\Gamma(3)}$ and $[\infty]_{\Gamma_0(p)}$, and $c=w_p(c')$. Main graph edges point out of $v_{c'}$ | Cusp choices EXPLICIT, TeX 633; main orientation EXPLICIT, TeX 249–276. Transport to a Task normal orientation remains CONDITIONAL |
| $N=3$ $\mu,\nu$ | Raw modular unit and powered theta product, before reducing their values | $\mu=u((z+2)/3)^3/u(z)$, $u=(\Delta(pz)/\Delta(z))^{1/d}$, $\nu=(\prod\theta)^{24/d}$. Their proportionality is asserted; no standalone proportionality constant is listed | Objects EXPLICIT, TeX 638–662; their role as a norm-before Task scalar is CONDITIONAL |
| Cusp Fourier/sign normalization | Complex cusp expansion and $p$-adic residual limit | $N=2$ prints a negative leading coefficient and its cancellation under $p-1$. $N=3$ says a Fourier computation gives the analogue; it does not print a Task first-normal Fourier coefficient/sign at $z_{\mathrm{Task}}=1/2$ | CONDITIONAL for the Task normal/lift, TeX 514–516, 564, 602–610, 635–662 |
| Task rational lift $z_{\mathrm{Task}}=1/2\pmod{p^2}$ | A specific algebraic-base lift in $\mathbf{Z}_p/p^2$, distinct from any cusp label | No such prescription or scalar evaluation is supplied in the fixed paper. The appendix's $[1/2]$ is a rational cusp, with exponential local parameter | CONDITIONAL / not supplied by this source; TeX 625, 654 versus 294–317, 372–379 |

The marked factor $a_i$ is available: it must not be discarded merely because the usable period formula takes its norm. Equally, the implication $\bar{\Phi}(e_i,e_i)/p=N(a_i)$ does not give $\Phi(e_i,e_i)/p=a_i$, nor identify either one with $G_p$.

## Norm, principal units, orientation and signs are different operations

The source explicitly puts the displayed main theorem in $K^\times/U_1(K)$ (TeX 134); its proof warns that mixed $k^\times$ and $K^\times$ expressions are understood in that quotient (427). For an unramified field, quotienting by $U_1=1+p\mathcal{O}_K$ retains the valuation and the nonzero unit residue. In particular, if a diagonal period has valuation 1, its class after division by $p$ retains its first nonzero residue. For odd $p$, $-1\notin U_1$: this quotient alone does not erase every sign or every first-normal datum. It does discard higher principal-unit digits of an already chosen multiplicative representative.

Separately, for $a\in k^\times$, the operation appearing in the formula is $a^{p+1}=a\,a^p=N_{k/\mathbf{F}_p}(a)$. This map is not injective: its kernel has order $p+1$, and $N(-a)=N(a)$. Even if $a\in\mathbf{F}_p^\times$, it gives $a^2$, not $a$. These are local algebraic facts about this output interface. They do not rule out recovery after supplying an independently fixed orientation/calibration or more information from the raw period object.

Thus the precise gap is an **unprovided identification and calibration**, not a denial of the source's raw theta pairing, its graph orientation, or the explicitly definable $a_i$. The raw objects may support a future bridge; this fixed source does not state that bridge for the Task.

## The actual Fourier and cusp evidence

The main $N=2$ definition at TeX 372–380 takes $z,z'$ in the Schottky half-plane near chosen cusp lifts, related by $\tau(z)=w_p(\tau(z'))$. It is a cusp limit, not an instruction to evaluate a Gauss/hypergeometric base variable at the rational number $1/2$.

$N=2$ TeX 514–516 explicitly uses $\lambda'\sim-1/(16q_c)$, $\mu\sim p^{-12/d}q_c^{-6(p-1)/d}$, and the residual expression

$$
\bigl((-1/16)^{p-1}p\bigr)^{12/d}=p^{12/d}.
$$

The negative Fourier leading term is real source evidence, but the displayed conclusion involves an even exponent and principal-unit reduction. It is not an independently retained sign for a norm-before CM24 scalar.

$N=3$ fixes $c',c$ (633), $H$'s base pole and exponential local parameter (635), the maps $\pi_i$ (636), $\mu$'s divisor and annular degree $24/d$ (640), $\mu\circ w_p=p^{-12/d}\mu^{-1}$ (641), and $\nu$'s $24/d$ power (660). At 662 it asserts the analogue with $\lambda$ replaced by $H$. These are positive geometric and normalization data, but no independent Task-lift choice or unpowered first-normal scalar evaluation is then added: references immediately start at 664.

The source also distinguishes a base simple pole (635) from a claimed double pole of the pullback on the higher curve at $c'$ (642). This readcheck does not decide their ramification reconciliation, use either to choose a multiplier, or declare the paper false.

The literal $1/2$ entries in the $N=3$ section occur in the cusp list and the cusp-parameter table. In the latter the parameter is $e^{-i\pi/[3p(2z-1)]}$, an exponential local parameter at a cusp, rather than a ring-theoretic lift $z_{\mathrm{Task}}=1/2\pmod{p^2}$. The two hits of the raw text pattern $p^2$ are actually the involution expressions $w_p^2=1$ and $w_p^2=\alpha_g$ (447, 462). The full-file literal diagnostics are only support for locating these uses; the conclusion follows from reading their contexts, not from search silence.

## Bounded gate result and handoff

Completed: identify the actual source objects, field and quotient; retain the marked factor $a_i$; separate norm loss from principal-unit precision; locate the real Fourier/sign/cusp conventions; exclude the cusp $[1/2]$ as a false Task lift witness. No additional source or mathematical branch was opened.

For an EXPLICIT Task interface, a continuation must produce an independently defined oriented local scalar, specify its field and normal parameter/gauge, prescribe the exact rational Task lift and its chosen full-level branch, and prove the normalized equality to $G_p$ before applying the norm. A scalar chosen afterward to force that equality does not fill this gate. No concrete witness of those fields is supplied by the fixed v3 $N=3$ appendix. The verdict remains **NORM_ONLY_WITH_GAP** for this one bounded source interface; global possibility, parent mathematical completion and other active research are unchanged.
