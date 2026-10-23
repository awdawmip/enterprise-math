# D25/LIFT — Joint reflected J-jet obeys two exact seam-forced polynomial differential equations

**2026-10-23; TASK_RESEARCH portable mathematical evidence.** Classification: **AUTHOR-PROVED EXACT POLYNOMIAL IDENTITIES / FRACTION AUTHOR SELF-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. No original native benchmark, formal Source checkpoint, CLAIM/run, Result/freeze, independent review, or completion of LOW/EP/LIFT is claimed.

**Provenance and frozen scope.** Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`, isolated from control maintenance. Parent Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; Task publication \`TP2-B6F4FC938FF94941C1B7\`; frozen Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. Consume prior exact J head/tail parameter derivative, not repeat: \`research_notes/portable_direct/20261023_onhour_d25_J2_head_tail_single_parameter_4F3.md\` @ immutable commit \`d20a2d935c4d0f05ab220148b2276f8a0e3293c7\`. Earlier BC mirror/curvature, LOW/Beta, B11 and finite 611-prime endpoint are prior evidence, not new acceptance. Verified global control snapshot \`GLOBAL_KNOWLEDGE_V1 main@61cfa2a580230863c0d02b5f818381adbb3cb11b\`; P000 ACTIVE_LOCKED, canonical blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`. This note is rational arithmetic with no P000/X6 native physical implication.

## 1. A single coefficient carrier for both finite 4F3 blocks

Let m≥1 be an integer, N=3m, and H_0=0, H_a=∑_{j=1}^{a}1/j. For 1≤r≤N define

\[
d_r=\begin{cases}m-r,&r\le m,\\r-m-1,&r>m,\end{cases}\quad
J^\circ_r=\tfrac12(H_{r-1}-H_m)
+\tfrac23(H_{2m}-H_{d_r})
+\tfrac13(H_{4m}-H_{3m-r}).
\]

Retain the original branch selector \(c_r=1\) for \(r\le m\), \(c_r=1/3\) for \(m<r\le3m\), and signed Beta branch weight

\[
\beta_r=\frac{(-1)^m m!(r-1)!}{2^{m+r}(m+r)!}.
\]

The preceding proof constructed two finite truncated 4F3-like parameter polynomials \(\Phi_H(t,z)\) and \(\Phi_T(t,z)\) with head/tail derivatives equal to the appropriate \(J_r^\circ\), and exact full reflected second-digit scalar \(J_m^{(2)}\). Their *unified* finite polynomial is

\[
\Psi_m(t,z)=\Phi_H(t,z)+(2z)^m\Phi_T(t,z).
\]

Define the two rational-coefficient polynomials of degree N−1

\[
\boxed{F_0(z)=\Psi_m(0,z)=\sum_{r=1}^{N}u_{r-1}z^{r-1},\qquad
F_1(z)=\partial_t\Psi_m(0,z)=\sum_{r=1}^{N}u_{r-1}J^\circ_r z^{r-1},}
\tag{F}
\]

with explicitly *tagged* rational coefficients

\[
\boxed{u_{r-1}=2^{r-1}c_r\beta_r
=\frac{(-1)^m m!}{2^{m+1}}\,c_r\,\frac{(r-1)!}{(m+r)!}.}
\tag{U}
\]

The factor \((2z)^m\) is required: the tail starts at monomial degree m, not zero. Using the already proved reflected Beta integral,

\[
\boxed{J_m^{(2)}=
\bigl[(3z\partial_z+2)F_1(z)+F_0(z)\bigr]_{z=1/2}.}
\tag{J}
\]

This maintains the entire \(r>m\) tail and both its one-third multiplicity and harmonic correction. It is **not** a replacement of finite sums by nonterminating hypergeometric functions.

There is also a literal finite-integral observer for the zero jet, obtained term-by-term from \(\beta_r=\int_0^{1/2}x^{r-1}(x-\frac12)^m dx\):

\[
F_0(z)=\int_0^{1/2}(x-\tfrac12)^m\,
\frac{3-2(2zx)^m-(2zx)^{3m}}{3(1-2zx)}\,dx.
\tag{BETA}
\]

The apparent denominator \(1-2zx\) cancels as a *finite polynomial* before evaluation; it is not a pole prescription. In particular \(F_0(1/2)=\int_0^{1/2}(B_m(x)/x)P_1(x)dx\), the existing LOW/Beta first-digit adjoint port.

## 2. First new theorem: zero jet has only THREE forcing impulses

Let the rational polynomial differential operator be

\[
\mathcal L_m F:=z(1-z)F'(z)+(m+1-z)F(z).
\tag{L}
\]

From (U) the coefficient ratio is

\[
\frac{u_r}{u_{r-1}}=
\begin{cases}
\frac{r}{m+r+1},&1\le r\le3m-1,\ r\ne m,\\
\frac{m}{3(2m+1)},&r=m.
\end{cases}
\tag{R}
\]

Thus every ordinary interior coefficient cancels, leaving **only** the initial, branch seam and terminal inputs:

\[
\boxed{
\mathcal L_mF_0(z)
=(m+1)u_0-\frac{2m}{3}u_{m-1}z^m
-3m\,u_{3m-1}z^{3m}.}
\tag{BASE-ODE}
\]

This is an exact identity in \(\mathbb Q[z]\) for every m≥1, **not** a congruence conditional on p=6m+1 being prime. It transforms the former 3m-term Beta carrier into an explicitly forced first-order differential equation, with branch provenance retained in the \(z^m\) seam source and \(z^{3m}\) finite-cutoff source. It does not claim a corresponding native X6 update law.

## 3. Second new theorem: the first J-jet has RATIONAL interior forcing

A direct telescoping of the inherited reflected harmonic expression proves, for 1≤r<3m,

\[
\boxed{
J^\circ_{r+1}-J^\circ_r=
\begin{cases}
\displaystyle\frac1{2r}+\frac2{3(m-r)}+\frac1{3(3m-r)},&r<m,\\[5pt]
\displaystyle\frac{2}{3m},&r=m,\\[5pt]
\displaystyle\frac1{2r}-\frac2{3(r-m)}+\frac1{3(3m-r)},&m<r<3m.
\end{cases}}
\tag{DELTA-J}
\]

In particular \(r=m\) is a **separate exact finite seam**; neither singular-side expression can be substituted there. Put \(\Delta_r\) equal to the relevant right side of (DELTA-J). Then

\[
\boxed{\begin{aligned}
\mathcal L_m F_1(z)={}&
(m+1)u_0J^\circ_1\\
&+\sum_{r=1}^{m-1}r u_{r-1}\Delta_r z^r\\
&+\left[-\frac{2m}{3}u_{m-1}J^\circ_m
+\frac29u_{m-1}\right]z^m\\
&+\sum_{r=m+1}^{3m-1}r u_{r-1}\Delta_r z^r\\
&-3m\,u_{3m-1}J^\circ_{3m}z^{3m}.
\end{aligned}}
\tag{JET-ODE}
\]

**Proof of both ODEs.** For any polynomial \(F(z)=\sum_{k=0}^{N-1}f_kz^k\), the coefficient of z^r in \(\mathcal L_mF\), for \(1\le r<N\), is \((m+r+1)f_r-rf_{r-1}\), while the constant and terminal \(z^N\) coefficients are respectively \((m+1)f_0\) and \(-Nf_{N-1}\). Insert \(f_k=u_k\); (R) zeroes every interior coefficient except \(r=m\), where \((2m+1)u_m-mu_{m-1}=-2m\,u_{m-1}/3\). This proves BASE-ODE.

Next insert \(f_k=u_k J^\circ_{k+1}\). At \(r\ne m\), (R) gives \(r u_{r-1}(J^\circ_{r+1}-J^\circ_r)=r u_{r-1}\Delta_r\). At the seam, \((2m+1)u_m=m u_{m-1}/3\), and (DELTA-J) gives

\[
(m/3)u_{m-1}J^\circ_{m+1}-m u_{m-1}J^\circ_m
=-\frac{2m}{3}u_{m-1}J^\circ_m+\frac29u_{m-1}.
\]

The remaining two coefficients are the endpoint terms in JET-ODE. The harmonic difference (DELTA-J) itself follows from \(H_a-H_{a-1}=1/a\) on the two original piecewise d_r branches; across r=m calculate directly. Thus both proofs hold for every m≥1 and do not depend on finite testing.

**Information retained and mathematical significance.** The undifferentiated complete reflected beta tail becomes a three-forcing scalar ODE; the first harmonic derivative becomes the same operator with explicit *rational* forcing in the interior, except the declared harmonic head/seam/terminal factors. This is a concrete holonomic interface to match the existing low second-order binomial jet and contiguous-Dixon B11; it is not yet that matching theorem. Taking the positive magnitude of signed weights would lose the cancellation, so retain \(u_r\), r labels and p-adic precision before any quotient.

## 4. Exact executable finite witness (author cross-check only)

Using standard Python 3 \`Fraction\`, factorials and independent direct harmonic evaluation, tested m=1,...,30. For each m constructed the full coefficients \(F_0,F_1\), applied \(\mathcal L_m\) *coefficientwise*, and compared against the independent BASE-ODE and JET-ODE right sides for all \(3m+1\) coefficients. Also individually checked DELTA-J at every admissible r. The actual execution returned:

    PASS exact F0/F1 sparse-seam+terminal differential certificates; m=1..30 all coefficients
    m=2 F0 forcing: [(0,1/8),(2,-1/72),(6,-1/672)]; F1 seam = -2983/181440
    m=3 F0 forcing: [(0,-1/16),(3,1/480),(9,1/10560)]; F1 seam = 26167/7983360
    m=5 F0 forcing: [(0,-1/64),(5,1/24192),(15,1/2976768)]; F1 seam = 1402972763/16895152834560

This is a finite falsification/implementation cross-check, not an all-m theorem substitute, independent review, a Source native benchmark, or formal admission. The all-m proof is the coefficient argument above. The operator and coefficients are rational with all ordinary factorial denominators bounded below the original p=6m+1 target (when p is prime); no hidden divided-p quotient is introduced.

## 5. Next precise unfinished science unit and recovery contract

The true unproved problem is still the **JOINT LOW second-digit** certificate with its already established divided-first-digit and curvature-mirror corrections:

\[
\mathscr D_m^{\mathrm{joint}}=
\frac{\mathcal A_m\Theta_m-1}{p}
+\mathcal A_m\bigl(2^{-m}C_m-2V_m+\mathsf M_m^\sharp+J_m^{(2)}\bigr)-\chi_p
\pmod p.
\]

This is a **routing/display** of the previously defined joint components; use the precise existing mirror-conservation and LOW/Beta contract before any assertion that these terms cancel. An apparent cancellation between \(J_m^{(2)}\) and curvature \(I_m/3\) alone is false at p=13 and 19 (witnesses in the preceding J-note). The next exact action is to apply (BASE-ODE) and (JET-ODE) to the genuinely weighted low second-jet Beta kernel, preserving the \(-pC_m\) first-digit division term; derive a shared finite contiguity/telescoping identity at z=1/2 or isolate a single explicit nonzero joint defect. Do **not** infer original EP/LIFT closure from the holonomic form. Original native benchmark object/conditions, scientific acceptance, external review remain open.

**Persisted Source/recovery debt:** own Research lane control issues #6186 (local recovery-status ACTIVE projection, not certified source ownership), #6187 (exact D25 continuation PREREQUISITE_NOT_SUCCEEDED), #6188 (original dispatch FAILED / TimeoutExpired) have been read and not replayed. #1539 remains the real Source-session registration support path. Current direct Site client has \`research_authority_granted=false\`; no current valid Researcher CLAIM/run is established. A GitHub mathematical author note grants no Source activity registration, role-bound checkpoint, Result, freeze, review, native benchmark, or ownership. Maintain \`REGISTER_PENDING / SYNC_DEBT\`, unchanged frozen Source pin and original research schedule/notification controls.
