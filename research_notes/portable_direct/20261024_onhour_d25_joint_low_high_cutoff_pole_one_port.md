# D25/LIFT — Fixed-prime joint LOW/HIGH cutoff pole and one necessary Cauchy port

**2026-10-24 | TASK_RESEARCH portable author proof | UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This is an auxiliary *fixed-prime cutoff* method diagnostic, not a theorem or counterexample about the unchanged original LIFT supercongruence. It is not a native benchmark, Source checkpoint, Result, independent review, or native Researcher execution.

**Mother:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Author provenance: the separate ordinary-control Research lane chatgpt-research-onhour-enterprise-math-20260923; **not** maintenance chatgpt-hourly-enterprise-math-20260921, **not** the other researcher lane chatgpt-research-hourly-enterprise-math-20260923.

This paper consumes, without relabeling as new, the original LOW first jet/HIGH two sectors (20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md), fixed LOW boundary (20261024_onhour_d25_p211_fixed_endpoint_sharp_valuation_low_boundary.md), Green adjoint (20261024_onhour_d25_high_impulse_green_two_boundary_certificate.md), and the *other lane's* Source-fixed HIGH cutoff theorem (20261024_hourly_d25_fixed_high_cutoff_shift_universal_pole_82.md, Git commit 21c62ae4afd8ecde26d38a44eb60ce9b421382b): for every prime p=6m+1, \(p(Z_{m+1}-Z_m)\equiv-82\bmod p\). The present combined theorem is explicitly conditional on this as-yet-unreviewed author HIGH theorem and the inherited author first-digit identity. There is no claim of independent Source acceptance.

## 1. Unchanged coefficients, new fixed-p observer

For each integer r≥1, write

\[
b_{r,n}=\frac{(-1)^n}{2^n}\binom rn,\qquad
k_n=\frac{(1-3n)(6n+3)}{(3n+1)(3n+2)},\qquad
A_r=\sum_{n=0}^r b_{r,n}k_n,
\]

\[
\epsilon_j=\frac3{6j+1}-\frac1{3j+2}-\frac2{3j+1},\quad
d_n=\frac2{1-3n}+\frac2{6n+3}-\frac1{3n+2}-\frac2{3n+1},
\]

\[
J_r=\sum_{n=0}^r b_{r,n}k_n\left(d_n+\sum_{j=0}^{n-1}\epsilon_j\right),
\qquad
B_r=\frac{(2r-1)!(2r)!}{(4r)!}.
\]

Here \(Z_r\) is *exactly* the original Source-fixed two-sector HIGH sum with independently labeled \(a_{r,s}k_s^A\) and \(-c_{r,s}k_s^B/24\) branches (not the fitted auxiliary seam pair). Let \(H_t=\sum_{j=1}^t1/j\). For a **fixed prime** \(p=6m+1\), define the auxiliary cutoff expression

\[
\Phi_p(r)=\frac{A_r+(1-2r)B_r}{p}+J_r+
B_r\left(Z_r+\frac{28}{9}+\frac13H_r+\frac29H_{2r}\right). \tag{1}
\]

At the **original rank** r=m this reduces to the previously established finite obstruction \(\mathcal F_m\bmod p\); the LOW divided numerator there is p-integral. The extension r=m+1 holds **p fixed**. It is neither the original task at p nor the different-prime task at p'=6(m+1)+1. It diagnoses whether an uncorrected m-contiguous rational WZ step is lawful.

## 2. Three-port principal-pole theorem

**Theorem A (conditional composition).** For every prime \(p=6m+1\), m≥2 (therefore p≥13), \(\Phi_p(m+1)\) has p-valuation at least -1, and the full combined LOW/HIGH cutoff residue is

\[
\boxed{\mathcal R_m:=
p\,[\Phi_p(m+1)-\Phi_p(m)]
\equiv
\underbrace{A_{m+1}-(2m+1)B_{m+1}}_{\mathrm{divided\ LOW}}
+\underbrace{3b_{m+1,m+1}k_{m+1}}_{\mathrm{new\ LOW\ jet}}
-\underbrace{82B_{m+1}}_{\mathrm{fixed\ HIGH}}
\pmod p.}\tag{2}
\]

**Proof.** Since \(4m+4<p\), the factorial ratio \(B_{m+1}\), binomial sum \(A_{m+1}\) and all harmonic seam denominators up to \(2m+2\) are p-integral. In the full first jet at the *new* rank m+1, the **only** p-denominator is \(6j+1=p\) at j=m within \(\epsilon_m\), and it occurs only in the n=m+1 terminal LOW summand. Hence
\(pJ_{m+1}\equiv3b_{m+1,m+1}k_{m+1}\pmod p\), while \(J_m\) is integral. The inherited fixed HIGH theorem gives \(pZ_{m+1}\equiv-82\pmod p\), while \(Z_m\) is p-integral. The original divided numerator at r=m is p-integral after dividing by p, so multiplying the difference of its terms by p retains only its new rank m+1 numerator. All other scaled terms vanish modulo p; the two original HIGH sectors and terminal remain encoded in the **unchanged** \(Z,B\) objects. QED.

## 3. A single additional LOW Cauchy port controls the full pole

Define the two exact finite rational ports (no analytic-continuation hypothesis):

\[
I_a(r)=\sum_{n=0}^{r}\frac{b_{r,n}}{3n+a}
=\int_0^1x^{a-1}(1-x^3/2)^r\,dx,\quad a=1,2.
\]

Partial fractions give exactly

\[
k_n=-2+\frac2{3n+1}+\frac3{3n+2},\qquad
A_r=-2^{1-r}+2I_1(r)+3I_2(r).\tag{3}
\]

Integrating the derivative of \(x^a(1-x^3/2)^r\) between 0 and 1 proves for every integer r≥1 the exact rational beta-by-parts identity

\[
\boxed{(3r+a)I_a(r)-3r I_a(r-1)=2^{-r}.}\tag{4}
\]

With r=m+1 and 3r≡5/2 modulo p, (4) and (3) yield

\[
\boxed{A_{m+1}\equiv\frac59A_m+\frac{20}{63}I_1(m)
+\frac{46}{63}\,2^{-m}\pmod p.}\tag{5}
\]

For all m≥2 with p=6m+1 prime, exact factorial cancellation yields

\[
\frac{B_{m+1}}{B_m}=
\frac{2m(2m+1)^2(2m+2)}
{(4m+1)(4m+2)(4m+3)(4m+4)}
\equiv-\frac1{14}\pmod p.\tag{6}
\]

The inherited original first digit (not re-proved here) gives
\(A_m\equiv(2m-1)B_m\equiv-4B_m/3\pmod p\);
direct reduction gives \(k_{m+1}\equiv-16/21\pmod p\).
Substituting (5),(6) in (2) proves

\[
\boxed{\mathcal R_m\equiv
\frac{20}{63}I_1(m)+
\frac{46+72(-1)^m}{63\,2^m}+
\frac{976}{189}B_m\pmod p.}\tag{7}
\]

All denominators in (7) are units for p≥13, including the required p≡13,19 mod 24 classes. This is a compact, **one-surviving-LOW-port** exact certificate for the actual Source-fixed joint cutoff Laurent coefficient, **conditional on its explicitly cited author-side HIGH input**. Its proof is algebraic, not a fitted finite-prime coincidence.

**Typed observer/rank.** Writing s=3(m+1), the linear map from formal LOW port coordinates \((I_1(m),I_2(m))\) to the offset-adjusted outputs \((A_m,A_{m+1})\) has determinant

\[
\boxed{-\frac{6s}{(s+1)(s+2)}
\equiv-\frac{20}{21}\ne0\pmod p.}\tag{8}
\]

Hence on the **formal two-port state** the next-cutoff LOW observer cannot factor through A_m alone; I_1(m), or an equivalent contrast, is a necessary retained coordinate unless an additional relation on the actual CM/Hasse family is separately proven. This does **not** assert actual family independence or an X6/CM equivalence.

## 4. Exact obstruction at the first two target primes

At p=13,m=2, the shifted diagnostic cutoff r=3 has
\(A_3=10,\ B_3=11,\ b_{3,3}=8,\ k_3=11\pmod{13}\).
The three ordered terms of (2) reduce to (7,4,8), giving

\[
\boxed{13[\Phi_{13}(3)-\Phi_{13}(2)]\equiv6\not\equiv0\pmod{13}.}\tag{9}
\]

Thus \(\nu_{13}(\Phi_{13}(3))=-1\); an **uncorrected fixed-p cutoff transport is not p-integral**. At p=19,m=3 the sources are (12,8,6), summing to 7≠0 mod19. These are counterexamples **only to that naive auxiliary cutoff-regularity shortcut**; they are not counterexamples to the original LIFT conjecture or its p³ precision.

The small prime p=7,m=1 is **excluded** from this theorem because \(B_{m+1}=B_2\) is not p-integral; treating it would require its own Laurent-port accounting. No different-prime m→m+1 assertion is made.

## 5. Executed exact arithmetic, limits, and next action

The portable standard-library Python checker d25_joint_low_high_cutoff_pole_check.py (delivered separately) was **actually run** using fractions, factorials and modular inversion. It independently rebuilt both HIGH sectors, the complete LOW jet and the harmonic seam; checked (4) exactly for r=1..9; and compared a direct rational evaluation of \(p\Phi_p(m+1)\) with (2) and (7) for p=13,19,31,37,43,61,211. All **7/7** prime cases passed; combined residues respectively **6,7,26,24,18,22,142**. Finite arithmetic is author self-check, **not** an all-prime proof, independent audit, native experiment or Source promotion.

**BRC REUSE_APPLIED / COMPOSE_APPLIED:** carrier = signed original LOW binomial branch ports (I_1,I_2), the first jet, separate source-fixed HIGH-A/HIGH-B branches, seams and cutoff Laurent pole labels. Observer = fixed-p m→m+1 Laurent residue, with exact rational/valuation precision. Equation (8) is a formal observer-factorization obstruction and (7) retains the minimal demonstrated repair port; no positive-mass substitution or hidden third-digit/CM equivalence is inferred.

**Original hard target remains OPEN.** \(\mathcal F_m=0\) for every target prime, same-class CM/divided-power class/semilinearity/map direction, the ordinary \(\omega+6\nabla_\lambda\omega\) leading normalization bridge, and **unchanged native benchmark** remain uncompleted. The next exact mathematical unit is to build a compensated LOW/HIGH finite WZ/contiguous certificate retaining \(I_1(m)\), whose cutoff-pole correction cancels (7), or instead a fixed-rank termination identity that avoids an auxiliary cutoff. Do not confuse auxiliary counterexample (9) with the original conjecture. Prior D24 certified material remains frozen.

**Authority/ownership:** Sites 0.6.11 freshly reported research_authority_granted=false; this lane's exact continuation read returned CONTROL_QUOTA. Neither creates Source ownership. Existing #1539 support, historical request IDs and three separate UR staging uploads remain untouched. No Researcher session/claim/open/run, formal Source checkpoint, freeze, Result, review, native benchmark, scheduling or notification mutation is claimed or performed.
