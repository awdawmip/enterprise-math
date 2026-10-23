# D25/LIFT — JOINT-POLY second-jet -> first-jet holonomic bridge

2026-10-24 | TASK_RESEARCH | AUTHOR-PROVED EXACT FINITE IDENTITIES / FRACTION AUTHOR SELF-CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. **Not** Source registration, CLAIM, run, formal checkpoint, Result, Driver review, native benchmark or global LIFT proof.

**Frozen task and provenance**: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research logical conversation chatgpt-research-onhour-enterprise-math-20260923, separate from control maintenance. Consumes exact prior BIVARIATE-C from research_notes/portable_direct/20261023_onhour_d25_mixed_jet_bivariate_beta_nopole.md and complete high reflected J scalar/holonomic forcing from 20261023_onhour_d25_J2_scalar_holonomic_modp_reduction.md. No reproof of D24, B11/WZ or endpoint finite scan. Verified GLOBAL_KNOWLEDGE_V1 main@0d1a36da02cbd766d83a625e62c9a47076edd4e5; P000 ACTIVE_LOCKED blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. External rational algebra; no native X6 claim.

## Theorem 1: exact second-to-first-jet collapse

Let m>=1 be an integer and put p=6m+1 formally; primality is **not** needed for the following equality. Define

\[
P_m(z)=(1-z/2)^{m-1}=\sum_{j=0}^{m-1}a_jz^j,\quad
a_j=(-1)^j{m-1\choose j}/2^j,\quad
\widehat F_m(z)=-(1-z)P_m(z).
\]
\[
A_n=H_m-H_{m-n},\qquad
\Lambda_n=2(H_{2m}-H_{2m-n})-(H_{2m+n}-H_{2m}),
\quad h_n=\Lambda_n(\Lambda_n-3A_n).
\]
For \(0\le j<m\), let \(d_j=2/(2m-j)-1/(2m+j+1)\), \(e_j=1/(m-j)\).
The prior BIVARIATE-C exact theorem defines a pole-free finite rational polynomial functional
\(\mathcal B_m[G]=\frac1{18}\sum_{n=0}^{m}[z^n]G(z)h_n\).

**New exact identity, every m>=1**:
\[
\boxed{18\mathcal B_m[\widehat F_m]=
\sum_{j=0}^{m-1}a_j\left[
(2d_j-3e_j)\Lambda_j-3d_jA_j+d_j^2-3d_je_j
\right].}\tag{1}
\]
This removes every *quadratic* low harmonic product and the bivariate coefficient/integration loop from the unreduced JOINT low second-jet port, while retaining two linear first-jet families.

**Proof**: As \(\widehat F_m(z)=\sum_{j=0}^{m-1}a_j(z^{j+1}-z^j)\), for any \(h_n\),
\(\sum_{n=0}^{m}[z^n]\widehat F_m\,h_n=\sum_{j=0}^{m-1}a_j(h_{j+1}-h_j)\).
The exact adjacent harmonic differences are \(A_{j+1}-A_j=e_j\) and
\(\Lambda_{j+1}-\Lambda_j=d_j\). Consequently
\[
h_{j+1}-h_j=(\Lambda_j+d_j)(\Lambda_j+d_j-3A_j-3e_j)
-\Lambda_j(\Lambda_j-3A_j)
=(2d_j-3e_j)\Lambda_j-3d_jA_j+d_j^2-3d_je_j.
\]
Substitute into BIVARIATE-C. Finite algebra over Q proves (1) without numerical extrapolation.

## Theorem 2: explicit finite first-jet resolvent and forcing ODE

On polynomials of degree at most m-1 let \(\theta=z\partial_z\) and use **coefficientwise finite resolvents**
\[
\mathsf D=2(2m-\theta)^{-1}-(2m+1+\theta)^{-1},\quad
\mathsf E=(m-\theta)^{-1}.
\]
These simply multiply the \(z^j\) coefficient by \(d_j\) or \(e_j\); all relevant denominators are positive. Set
\[
\mathcal T_m(z)=\sum_{j<m}a_j\Lambda_jz^j,\qquad
\mathcal U_m(z)=\sum_{j<m}a_jA_jz^j.
\]
Then (1) is equivalent to the **exact linear first-jet observer**
\[
\boxed{18\mathcal B_m[\widehat F_m]=
\left[(2\mathsf D-3\mathsf E)\mathcal T_m
-3\mathsf D\mathcal U_m+
(\mathsf D^2-3\mathsf D\mathsf E)P_m\right]_{z=1}.}\tag{2}
\]

Both low jets are genuinely first parameter derivatives: for \(0\le j<m\) let
\[
T_j(t)=\prod_{s=0}^{j-1}(1+t/(2m-s))^2
\prod_{s=1}^{j}(1+t/(2m+s))^{-1},\quad
U_j(t)=\prod_{s=0}^{j-1}(1+t/(m-s)).
\]
Empty products equal 1; \(T'_j(0)=\Lambda_j\), \(U'_j(0)=A_j\), \(T_j(0)=U_j(0)=1\). Hence \(\mathcal T_m,\mathcal U_m\) are first-jet polynomials of two explicitly **terminating rational-product** families. Their neighboring term ratios are rational in j,t.

Define the polynomial first-order operator
\(\mathscr K_m=(2-z)\partial_z+(m-1)\). The **second exact theorem** is
\[
\boxed{\begin{aligned}
\mathscr K_m P_m&=0,\\
\mathscr K_m\mathcal T_m&=-\sum_{j=0}^{m-2}(m-1-j)a_jd_jz^j,\\
\mathscr K_m\mathcal U_m&=-\sum_{j=0}^{m-2}(m-1-j)a_je_jz^j.
\end{aligned}}\tag{3}
\]
**Proof**: \(2(j+1)a_{j+1}=-(m-1-j)a_j\). The \(z^j\) coefficient of \(\mathscr K_m\sum c_jz^j\) is \(2(j+1)c_{j+1}+(m-1-j)c_j\). Substituting \(c_j=a_j,\,a_j\Lambda_j,\,a_jA_j\) and the two adjacent differences gives (3). At the highest coefficient \(j=m-1\), the last factor is zero, so no artificial high-boundary impulse exists. The high-band already-proved \(\mathcal L_mF_1=R_m\), \(\mathcal L_m=z(1-z)\partial_z+(m+1-z)\), remains *distinct* and retains its head/m seam/3m terminal. These are now two low first-jet equations and one high first-jet equation at the same parameter-derivative order, a concrete contiguous/telescoping interface, not yet a matched telescoper.

## The original JOINT-LIFT scalar, unchanged

The earlier exact carrier decomposition is
\(\mathsf X_m=\mathcal B_m[\widehat F_m]-(p/2)\mathcal B_m[zP_m]\).
For prime \(p=6m+1\), the BIVARIATE-C functional and (1)-(3) have only p-unit denominators; thus only **mod p** may we use \(\mathsf X_m\equiv\mathcal B_m[\widehat F_m]\).
Together with the already-proved Q-minus/Q-plus reflection-curvature certificates, the *original* second low moment becomes
\[
\boxed{\mathsf M_m\equiv \mathsf P_m+
\frac1{18}\left[(2\mathsf D-3\mathsf E)\mathcal T_m
-3\mathsf D\mathcal U_m+(\mathsf D^2-3\mathsf D\mathsf E)P_m\right]_{z=1}
+\frac49Q_m^-+\frac5{18}Q_m^+\pmod p.}\tag{4}
\]
Keep the full target:
\[
\mathscr D_m^\beta\equiv
\underbrace{\frac{\mathcal A_m\Theta_m-1}{p}}_{\Delta_m}
+\mathcal A_m[2^{-m}C_m-2V_m^{\rm beta}
+\mathsf M_m+F_0(1/2)+6R_m(1/2)]-\chi_p
\pmod p.\tag{5}
\]
Here \(\chi_p=((4/3)^{p-1}-1)/p\). Do not drop \(\Delta_m\), Fermat quotient, beta V, Q±, pure-A P, or the r>m reflected 1/3 tail/seam/terminal; (5) is still OPEN. Equations (1)-(4) prove only an *equivalent lossless representation* and first-jet order reduction, not the global supercongruence or native experiment.

## Executed exact author-side checks

Companion Python 3 Fraction checker in this same conversation (d25_joint_firstjet_reduction.py) independently evaluates the original \(\mathsf X_m\), low second moment \(\mathsf M_m\), and bivariate polynomial \(\mathcal B_m[\widehat F_m]\); checks the new finite-difference form; and checks every coefficient of (3).

- m=1..40: (1) matches the exact finite-difference construction.
- m=1..9: independent \((1-x)(1-y)\) polynomial division + monomial integration matches (1), with zero boundary remainders.
- m=1..60: every polynomial coefficient in the forcing identities (3) matches exactly.
- 25 primes p=6m+1 with m<=40, from p=7 through p=241: the **original** harmonic \(L_n,M_n\) second moment agrees with (4) modulo p. This is not the native benchmark.

Witnesses: m=2,p=13: \(\mathcal B_m[\widehat F]=47/900\equiv7\bmod13\), original \(\mathsf M_m\equiv7\); m=3,p=19: \(\mathcal B_m[\widehat F]=-742229/114307200\equiv15\bmod19\), original \(\mathsf M_m\equiv18\); m=5,p=31: \(\mathcal B_m[\widehat F]=-488312351/584366983200\equiv29\bmod31\), original \(\mathsf M_m\equiv27\). Nonzero scalar terms cannot be silently discarded. Proof strength is the all-m finite algebra; calculations are author falsification only.

## Continuation checkpoint (portable, not native)

BRC REUSE_APPLIED/COMPOSE_APPLIED: keep the signed binomial a_j/n/r provenance, exact p-adic digit hierarchy, separate head/seam/tail and original source pin. The diagonal resolvents only preserve the declared scalar observer; they are not physical X6 axes or positive-mass conservation. **Next mathematically discriminating unit**: construct an actual *joint* terminating contiguous/WZ-Gosper telescope between low (3), full high \(\mathcal L_mF_1=R_m\), and **all** \(\Delta_m,C_m,-2V_m,\chi_p,\mathsf P_m,Q_m^\pm,F_0\). It must produce the kernel, exact boundary/seam/terminal and all-m proof or a rigorously explicit remaining obstruction; do not expand more stand-alone auxiliary jets or rescan primes. The native benchmark must still be performed under its unchanged exact object/input/verification conditions.

Source session gap: Sites v0.6.11 verified identity research_authority_granted=false, executor_binding_configured=false; no direct recovery_status action exposed for this logical conversation. Previous original bridge requests #6186 (local ACTIVE unverified), #6187 (PREREQUISITE_NOT_SUCCEEDED), #6188 (FAILED/TimeoutExpired) are **not replayed**, not NO_DISPATCH. Existing enterprise-math issue #1539 owns restoration; three historical staging items remain independently sourced, not folded into Result. This file is neutral author mathematical evidence on an authorized GitHub surface, not Source checkpoint/CLAIM/Result/freeze/independent review. Original research schedule, enabled state and notifications unchanged.