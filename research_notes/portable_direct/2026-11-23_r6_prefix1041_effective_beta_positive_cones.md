# PREFIX-1041 — Effective Bernstein positivity cones from narrow spectral bands

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1040. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_IMPLICATIONS_CHECKED / NOT_INDEPENDENTLY_REVIEWED.

## Scope and pinned inputs

Science remains pinned to \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json\` (P000 V5). The Stage46 signed BRC candidate is \`W=J12-6I12\`, incoming \`-e1\`, blocked bidirectional Link \`{0,e1}\`, exactly one negative outgoing step. Preserve the native X6 Cell–terminal-port–grade joint observer, signs, branch identities, multiplicities and provenance.

This is an auxiliary **six-phase scalar spectral** theorem. It uses the previously derived density \`g\` and its Beta/Hausdorff representation; it neither computes native BRC propagation nor proves the full native observer correspondence. The earlier scalar representation and two critical-point sign certificates are assumed within their original bounds.

Immutable premises:
- PREFIX-1033 \`fec5c00006e3693121ee18f6d0be661506e06410\`: \`g\` continuous on \`[0,36]\`, and the exact Beta identity for normalized Hausdorff differences.
- PREFIX-1037 \`928461a6f8c675b9a7bd38586cf47db9d25835e9\`: the inherited Bessel kernel, absolute tail inequalities and certified critical-point lower bounds.
- PREFIX-1040 \`58e35fe4a131729405107d736198cf555d53cc8a\`: \`g(y)>7/4\` for \`|y-4|<=10^-6\`, and \`g(y)>49/50\` for \`|y-16|<=10^-9\`.

## Result A: a global, explicit uniform bound for the auxiliary density

Under the PREFIX-1037 scalar integral \`g(y)=int_0^infty K(t;y) dt\`, the following uniform bound holds:

\[
\boxed{\|g\|_{L^\infty[0,36]}\le611856.}\tag{A}
\]

The bound is intentionally conservative, but its constant is a *rational/integer certificate*, unlike a compactness-only unknown maximum.

**Proof.** For \`0<y<36\`, set \`r=sqrt(y)\`, \`H=y^2(36-y)^2\`, \`P=y(y-36)(17y-91)\`, \`A=2H'-P\`, \`B=H/r\`, \`C=12(11+y)\`, \`D=r(y-6)\`, \`E=2y\`. The inherited kernel is
\[
K(t;y)=\frac{J_0(t)^6}{5}\left[A\,tJ_0(rt)-B\,t^2J_1(rt)
+C\left(DJ_1(rt)-\frac E tJ_2(rt)\right)\right].
\]
The standard real-argument Bessel integral representations imply \`|J_nu(u)|<=1\` for integer \`nu>=0\`, \`|J_1(u)|<=u/2\`, and \`|J_2(u)|<=u^2/8\` for \`u>=0\`. Reuse the PREFIX-1037 Volterra bound: \`|J_0(t)|^6<=2t^-3\` for \`t>=1\`, and \`|J_1(u)|<=4u^-1/2\` for \`u>=1\`. The latter follows already from \`sqrt(2/pi)e^{3/(4u)}u^-1/2\` and \`e^{3/4}<4\`. The \`J_0^6\` bound likewise follows from \`(2/pi)^3 e^{3/(2t)}t^-3\`, \`pi>3\`, and \`e^{3/2}<19/4\`.

Coefficient bounds on \`[0,36]\`:
\[
|H'|\le2(36)^3,\quad |P|\le36^2(521),\quad
|A|\le861840,\quad C\le564,\quad |D|\le180,\quad E\le72.
\]
Also \`y(36-y)<=324\` and \`r<=6\`. For \`B=r^3(36-r^2)^2\` this gives \`B<=69984\`; if \`r>=1\` it also gives \`B/sqrt(r)<=34992\` using \`sqrt(r)<3\`. If \`0<r<=1\`, then \`B<=1296\`.

The four integral weights obey
\[
\begin{aligned}
\int_0^\infty |J_0(t)|^6\,t|J_0(rt)|dt
&\le\tfrac12+2=\tfrac52,\\
\int_0^\infty |J_0(t)|^6\,|J_1(rt)|dt
&\le1+\int_1^\infty2t^{-3}dt=2,\\
\int_0^\infty |J_0(t)|^6\,\frac{|J_2(rt)|}{t}dt
&\le \frac{r^2}{16}+\int_1^\infty2t^{-4}dt
\le\tfrac94+\tfrac23=\tfrac{35}{12}.
\end{aligned}
\]
For the \`B\` term define \`I_B(r)=int_0^infty |J_0(t)|^6 t^2|J_1(rt)|dt\`. If \`r>=1\`,
\[
I_B(r)\le\tfrac13+\frac{16}{\sqrt r},
\quad
B I_B(r)\le\frac{69984}{3}+16(34992)=583200.
\]
If \`0<r<=1\`, split the tail at \`t=1/r\`. On \`[1,1/r]\`, \`|J_1(rt)|<=rt/2\` contributes at most \`1\`; on \`[1/r,\infty)\`, \`|J_1(rt)|<=4(rt)^{-1/2}\` contributes \`16\`. Thus \`I_B(r)<18\` and \`B I_B(r)<=1296(18)<583200\`.

Summing absolute contributions to \`g=\int K\`,
\[
|g(y)|\le\frac1{5}\left[
861840\cdot\tfrac52
+583200
+564\cdot180\cdot2
+564\cdot72\cdot\tfrac{35}{12}\right]
=430920+116640+40608+23688=611856.
\]
The continuity inherited from PREFIX-1033 extends (A) to \`y=0,36\`. QED under the cited kernel and Bessel premises.

## Result B: explicit all-order, nonzero-width positivity cones

For nonnegative integers \`m,k\`, let \`N=m+k\`, \`n=N+1\`, \`j=m+1\`, \`s=j/n\`. With the PREFIX-1033 normalization,
\[
D_{m,k}:=\frac{(N+1)\binom Nm\,E_{m,k}}{36^{N+1}}
=\mathbb E[g(36T)],\qquad
T\sim{\rm Beta}(j,n-j+1).
\tag{B}
\]

For either center \`c in {4,16}\`, take the certified band radius \`\delta_c\`, positive lower bound \`\gamma_c\`, and output threshold \`\eta_c\` below.

| c | delta_c | gamma_c (strict local lower bound) | eta_c (new D lower bound) | n_c |
|---|---|---|---|---|
| 4 | 1/1000000 | 7/4 | 5/3 | 46,656,000,000,000,000 |
| 16 | 1/1000000000 | 49/50 | 9/10 | 46,656,000,000,000,000,000,000 |

**Theorem.** For *every* \`m,k>=0\` satisfying
\[
\boxed{n=m+k+1\ge n_c,\qquad
\left|\frac{m+1}{m+k+1}-\frac c{36}\right|
\le\frac{\delta_c}{72},}
\tag{C}
\]
the corresponding normalized Hausdorff difference is **strictly bounded**:
\[
\boxed{D_{m,k}>\eta_c>0,\qquad E_{m,k}>0.}\tag{D}
\]
These are two explicit, nonzero-width cones of integer pairs, not simply two asymptotic sequences. For every \`n>=n_c\` each cone contains at least one \`j\` (choose the integer nearest \`n c/36\`).

**Proof.** The distribution \`Beta(j,n-j+1)\` is exactly the law of the \`j\`-th order statistic among \`n\` independent Uniform(0,1) samples. For \`s=j/n\` and \`h>0\` within the unit interval, binomial tail identities and Hoeffding's bound give
\[
\Pr(|T-s|\ge h)\le 2e^{-2nh^2}.\tag{E}
\]
Indeed, \`T<=s-h\` is the binomial upper-tail event \`Bin(n,s-h)>=j\`, a deviation \`nh\`. Similarly \`T>=s+h\` is \`Bin(n,s+h)<=j-1\`, a deviation at least \`nh\`.

Set \`h=\delta_c/72\`. Condition (C) and \`|T-s|<h\` imply \`|36T-c|<=\delta_c\`, hence the inherited band bounds yield \`g(36T)>\gamma_c\`. Everywhere else (A) gives \`g(36T)>=-611856\`. Thus, with \`p=\Pr(|T-s|\ge h)\`,
\[
D_{m,k}>\gamma_c-(\gamma_c+611856)p.
\]
For \`n>=n_c=9(72/\delta_c)^2\`, \`2nh^2>=18\`, hence \`p<=2e^{-18}<2^{-23}\`. The last strict inequality follows from \`e^3>16\` (already the sum of Taylor terms \`0<=r<=4\` exceeds \`16\`) and \`e^{18}>16^6=2^{24}\`.

Exact rational comparisons give
\[
\frac74-\frac{7/4+611856}{2^{23}}>\frac53,\qquad
\frac{49}{50}-\frac{49/50+611856}{2^{23}}>\frac9{10}.
\]
Together with (B), they establish (D). For nonemptiness at all stated \`n\`, rounding \`ns_c\` to the nearest \`j\` gives \`|j/n-s_c|<=1/(2n)<=\delta_c/72\`; the bounds are far inside \`0<j<n\`. QED.

Example certified rays (exact integer pairs at \`n=n_c\`):
- \`c=4\`: \`(m,k)=(5183999999999999,41472000000000000)\`, \`D_{m,k}>5/3\`.
- \`c=16\`: \`(m,k)=(20735999999999999999999,25920000000000000000000)\`, \`D_{m,k}>9/10\`.

## Evidence, interpretation and next question

Companion \`PREFIX1041_R6_BETA_CONE_EXACT_CHECK.py\` checks the global-bound arithmetic, the Taylor inequality, both \`n_c\` values, valid sample indices, and the two positive margins using only Python standard-library integer/Fraction operations. Local execution: \`EXACT_RATIONAL_IMPLICATIONS_PASSED\`.

This yields **effective, uniform in all eligible integer pairs, eventually positive finite-order Hausdorff differences** conditional on the previously derived signed-density representation. The thresholds are very large because the local band radii and the global absolute bound are intentionally coarse; no evaluation of moments at those huge indices was attempted or needed. This note does not establish full \`g>=0\` or every Hausdorff difference, and retains \`NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION\`.

Highest-useful next scientific units: (i) exploit the one-sided cusp plus resonant-mode cancellation to obtain much wider lower-bounded bands; (ii) certify the remaining compact spectral intervals directly, or exhibit an interval negative witness; (iii) separately verify the signed X6 Cell–port–grade observation map and original typed BRC interface. Mother problem \`B_fix,odd(32) in {19,20}\` remains open. Existing historical attribution \`EM-DIRECT-FBEA5D/RA-3FB2D033BE6048D8712FF056\` is source provenance, not current execution identity. No formal CLAIM, PROGRESS, Result or independent review is claimed.
