# D25/LIFT — third Jacobi parameter jet: endpoint cancellation and second-digit defect

Date: 2026-10-25. TASK_RESEARCH portable author proof; UNREVIEWED / NOT_ADMITTED / NO_NEW_NATIVE_CHECKPOINT. Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; Research logical lane chatgpt-research-hourly-enterprise-math-20260923. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**. Native CM/Frobenius experiment NOT_RUN.

## Question and new result

The established *second* Jacobi parameter-jet endpoint forcing is nonzero mod p and has already been lifted to mod p³; see prior notes 20261025_hourly_d25_terminal_jacobi_jet_universal_forcing.md and 20261025_hourly_d25_terminal_jet_p3_harmonic_fermat.md. This unit studies the **distinct third derivative** and computes its first nonvanishing cutoff digit; it does not re-credit the earlier second-jet result.

Let p=6m+1>=7 be prime, N=p-1=6m. Define

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\quad
\Phi(x,z)=\sum_{n=0}^{N}b_n(x)z^n,\quad
F_j(z)=\left.\partial_x^j\Phi(x,z)\right|_{x=m}\quad(0\le j\le3).
\]

Let theta=z d/dz, L_m=theta²-z(theta-m)(theta-2m), w_N=b_N''(m)/2 and t_N=b_N'''(m)/6. Write H_k=sum_(j=1)^k 1/j and H_k^(2)=sum_(j=1)^k 1/j², in the p-local rationals.

**Theorem A (exact rational third-jet equation):**

\[
\boxed{\mathcal L_mF_3+3z(3\theta-4m)F_2-12zF_1=K_{3,p}z^p},
\quad
\boxed{K_{3,p}=-6(20m^2t_N-14mw_N)}.
\]

Furthermore

\[
\boxed{t_N=w_N\Lambda_m},\qquad
\Lambda_m=H_m-H_{5m-1}+2H_{2m}-2H_{4m-1}.
\]

**Theorem B (third-port cancellation and first surviving digit):**
With S_p=H_(m+1)^(2)+2H_(2m+1)^(2) modulo p,

\[
\boxed{K_{3,p}\equiv0\pmod p},\qquad
\boxed{K_{3,p}\equiv p\left(12S_p-\frac{1782}{25}\right)\pmod{p^2}}.
\]

For the genuine point observer at z=1/2,

\[
\boxed{K_{3,p}2^{-p}\equiv
p\left(6S_p-\frac{891}{25}\right)\pmod{p^2}.}
\]

For p=13, K_(3,13)=104 modulo 169 and the point readout is 52; p=19 gives 266 and 133 modulo 361. Thus a zero first-digit forcing does not permit deleting the boundary branch at higher precision.

## Proof

The exact coefficient relation (n+1)² b_(n+1)(x)=(n-x)(n-2x)b_n(x) gives, for a(x)=(N-x)(N-2x),

\[
\mathcal L_x\Phi(x,z)=-a(x)b_N(x)z^p.
\]

At x=m, the two numerator Pochhammer factors have distinct simple zeros at indices m and 2m, so b_N(m)=b_N'(m)=0, and

\[
w_N=\frac{2(-1)^m m!(2m)!(5m-1)!(4m-1)!}{((6m)!)^2}.
\]

After removing exactly those two factors, the logarithmic derivative of the remaining product is

\[
\frac{t_N}{w_N}
=-\sum_{\substack{0\le j<N\\j\ne m}}\frac1{j-m}
-2\sum_{\substack{0\le j<N\\j\ne 2m}}\frac1{j-2m}
=\Lambda_m.
\]

Since L'_m=z(3theta-4m), L''_m=-4z, L'''_m=0, a(m)=20m², a'(m)=-14m, the third x-derivative of the exact cutoff differential equation is precisely Theorem A.

For every prime p>=7, H_(p-1)=0 mod p²: pair j with p-j and use 1/j+1/(p-j)=-p/j² mod p², together with the vanishing finite-field sum of inverse squares. For 0<=k<p, this also gives

\[
H_{p-1-k}\equiv H_k+pH_k^{(2)}\pmod{p^2}.
\]

Apply it to k=m+1 and 2m+1. The exact index complements are p-1-(m+1)=5m-1 and p-1-(2m+1)=4m-1. Consequently

\[
\Lambda_m\equiv-\frac1{m+1}-\frac2{2m+1}-pS_p
\equiv-\frac{21}{5}+p\left(\frac{87}{50}-S_p\right)\pmod{p^2}.
\]

Using m=(p-1)/6 and expanding only denominators invertible mod p yields

\[
20m^2\Lambda_m-14m
\equiv p\left(\frac{33}{10}-\frac59 S_p\right)\pmod{p^2}.
\]

The prior independently proved factorial/Wilson source identity supplies w_N=18/5 mod p. Substitution into K_(3,p) produces
-6(18/5)p(33/10-5S_p/9)=p(12S_p-1782/25) modulo p². Because K_(3,p) is divisible by p, the z=1/2 readout to mod p² needs only 2^(-p)=1/2 mod p; unlike the separate second-jet p³ computation it needs no Fermat quotient at this digit. The polynomial z^p remains distinct from its point evaluation. QED.

## BRC applicability and evidence

BRC resolution: COMPOSE_APPLIED on source labels (rank n, parameter-jet order, two zero-factor indices, valuation precision, signed coefficient, cutoff port). Third-jet endpoint cancellation at mod p is an exact scoped observation; K3/p is its future-relevant residual. The second-jet port and signed reflected Clausen corner are different sources. No Boolean/positive-mass collapse or native X6 geometric inference is claimed.

Companion exact checker: 20261025_hourly_d25_third_jacobi_jet_forcing_check.py. Full degree-p polynomial equation was checked over Q with rational Taylor recurrence at p=7,13,19,31,37,43. Separate modular Taylor recurrence was crosschecked against factorial and harmonic formulas modulo p² for all 35 primes p=1 mod6 in 7..373 and p=1327,19963: 37/37 PASS. These are author checks, not independent review, formal verification, mathematical admission or native CM experiment.

## Source frontier and next executable question

Consumed/not re-credited: accepted first-digit inertness, second-Jacobi-jet forcing and its p³ harmonic lift, the exact Jacobi original-source translation, the p³/p⁴ reflected Clausen corner, and the earlier self-Green pairing's failure to supply independent cross-source information. **Next:** seek a genuinely cross-source signed Jacobi/Clausen Green or discrete telescoping identity for B_01,p+A_2 H_0/72-T_jet,p, retaining the third-jet K3/p port when a higher precision observer is used. First derive the cross-source bilinear boundary and test it for a non-tautological source relation; do not reuse the self-pairing as an independent identity.

Mother D25/LIFT/JT2 remains OPEN; same-original-class CM H_0/B_0, [X]U mod p², Frobenius normalization and kappa bridge are missing. This artifact is PORTABLE_ONLY and **not predecessor native completed research**. Fresh direct continuation read this turn returned INVALID_ARGUMENT / CONTROL_QUOTA, not NO_DISPATCH; no winning CLAIM/OPEN/current Source checkpoint. Preserve prior durable native frontier, contribution history and frozen scientific Source pin. Responsible maintenance/support path: enterprise-math Issue #1558. Existing research scheduler and notification settings untouched.
