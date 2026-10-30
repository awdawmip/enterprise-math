# D25 SECOND-DIGIT-LIFT — Uniform CM/Deuring proof of the A216 Hasse-zero antecedent (2026-10-30)

**Status:** AUTHOR-SIDE / PROVED USING CLASSICAL CM–DEURING–HASSE–GAUSS THEOREMS / EXACT FINITE-FIELD REGRESSION EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

**Research lane:** chatgpt-research-onhour-enterprise-math-20260923 (not maintenance). **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7; **mother:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; **immutable scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3.

## Theorem: the previously open CM/Hasse antecedent is true for all frozen primes

Let p≥13 be prime, p≡13 or 19 (mod24), m=(p−1)/6, and
\[
P_m(z)=\sum_{k=0}^m\binom{m}{k}\binom{2m}{k}z^k.
\]
Then, for **every** such prime,
\[
\boxed{P_m(1/2)\equiv0\pmod p.}\tag{1}
\]
The proof combines established external arithmetic-geometry results with an explicit original A216 finite polynomial interface. This is not a proof of the outstanding p³ SECOND-DIGIT-LIFT.

### 1. Explicit CM model and good reduction

In K=Q(√2), put t=(2−√2)/4 and a=(1−t)/27. Then t(1−t)=1/8. The elliptic curve
\[
E_t:\quad y^2+xy+ay=x^3
\]
has
\[
\Delta=a^3(1-27a)=t(1-t)^3/27^3\ne0,\qquad
j(E_t)=27\frac{(1+8t)^3}{t(1-t)^3}
=2417472-1707264\sqrt2.
\]
The identity
\[
j^2-4834944j+14670139392=0
\]
is verified exactly. This is the classical Hilbert class polynomial of discriminant −24, so E_t has CM by an order in Q(√−6). Since t and 1−t are p-adic units for p>3, E_t has good reduction at all primes under consideration.

### 2. Deuring inert-prime reduction

For p≡13,19 (mod24), the Legendre symbols satisfy
\[
\left(\frac{-3}{p}\right)=1,\quad
\left(\frac{2}{p}\right)=-1,\quad
\left(\frac{-6}{p}\right)=-1.
\]
Thus every such p is unramified and inert in Q(√−6). Deuring's classical theorem implies that the good reduction of the CM curve E_t at any prime of K above p is supersingular; the residue field may be F_(p²), with no need to falsely identify a native H0/B0 Frobenius.

### 3. Exact Hasse coefficient

Complete the square with Y=2y+x+a:
\[
Y^2=4x^3+(x+a)^2,\qquad (p-1)/2=3m.
\]
By the usual Hasse coefficient criterion, supersingularity implies
\[
H_p(t):=[x^{p-1}]\bigl(4x^3+(x+a)^2\bigr)^{3m}=0
\quad\text{in }\mathbb F_{p^2}.
\]
Coefficient extraction, with k the number of cubic factors, yields
\[
H_p(t)=\sum_{k=0}^{2m}\binom{3m}{k}\binom{6m-2k}{k}
\left(\frac{4(1-t)}{27}\right)^k.\tag{2}
\]

### 4. Reduce the Hasse polynomial without discarding original ports

For 0≤k≤2m, all factorial denominators are p-units and
\[
\binom{3m}{k}\equiv(-1)^k4^{-k}\binom{2k}{k},\qquad
\binom{6m-2k}{k}\equiv(-1)^k\binom{3k}{k}\pmod p.
\]
Moreover
\[
\binom{2m}{k}\binom{4m}{k}
\equiv27^{-k}\binom{2k}{k}\binom{3k}{k}\pmod p.
\]
Define R_m(u)=\sum_{k=0}^{2m}\binom{2m}{k}\binom{4m}{k}u^k. Thus
\[
\boxed{H_p(t)\equiv R_m(1-t)\pmod p.}\tag{3}
\]

### 5. Legendre symmetry

Since −4m≡2m+1 (mod p),
\[
R_m(u)\equiv{}_2F_1(-2m,2m+1;1;u)
=L_{2m}(1-2u)\pmod p,
\]
where L_n is the ordinary Legendre polynomial. Its degree 2m is even, hence
\[
\boxed{R_m(1-u)=R_m(u)\quad\text{in }\mathbb F_p[u].}\tag{4}
\]

### 6. Classical finite Gauss quadratic transformation

At a=−m, b=−2m and c=a+b+1/2=1/2−3m=1−p/2, the exact terminating Gauss identity gives
\[
{}_2F_1(-m,-2m;c;4u(1-u))
={}_2F_1(-2m,-4m;c;u).
\]
The relevant c-rising factorials are p-units through k≤m and k≤2m, respectively. Reducing mod p (where c≡1) yields the finite polynomial identity
\[
\boxed{P_m(4u(1-u))\equiv R_m(u)\quad\text{in }\mathbb F_p[u].}\tag{5}
\]
Because 4t(1−t)=1/2, combining (2)–(5) with supersingularity proves
\[
0=H_p(t)=R_m(1-t)=R_m(t)=P_m(1/2)
\]
in F_(p²). The last term is actually in F_p. **This discharges the all-prime target antecedent, without assuming the desired congruence.** QED.

## Consequences and exact proof strength

Reuse the already derived finite Clausen identity
\[
F_p(z)={}_3F_2(\tfrac12,\tfrac13,\tfrac23;1,1;z)_{p-1}
\equiv P_m(z)^2\pmod p
\]
and the original A216 coefficients
\(a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n\),
with complete n-labelled source moments \(S_{j,p}=\sum_{n=0}^{p-1}n^ja_n\).

The new theorem removes the previously conditional root assumption **for all p≡13,19 mod24**:
\[
\boxed{S_{0,p}\equiv S_{1,p}\equiv0,\quad
S_{2,p}\equiv\tfrac12[P_m'(1/2)]^2\not\equiv0\pmod p.}
\]
The derivative is nonzero by the previously proved Gauss differential-equation root-simplicity lemma. Consequently the Sun (2015) **conditional** S_0 mod p → S_0 mod p² theorem now has a proved antecedent in both target classes, subject to its actual published remaining hypotheses. Together with accepted D24 A_p=S_0+6S_1≡p mod p², the first-moment residue is S_1≡p/6 mod p².

**Still open:** the original second digit
\[
\boxed{U_p+6V_p\equiv0\pmod p},
\qquad
U_p=S_{0,p}/p^2,\quad V_p=(S_{1,p}-p/6)/p^2,
\]
in the p-local ring. Neither Hasse-zero nor p² vanishing proves that joint p³ cancellation.

**BRC/tool reuse:** COMPOSE_APPLIED the earlier exact finite Clausen square, original weighted A216 source jets and known Gauss/Legendre/Deuring/Hasse laws. The preserved carrier has indexed rational coefficients, prime valuation and moment orders 0,1,2, and signed 6n+1 operation. Its S_2≠0 despite S_0=S_1=0 is a proven information-loss witness against the coarser observer. This CM curve is an **external auxiliary**, not the native six-dimensional P000 cell geometry, H0/B0 Frobenius, or the native experiment.

## Executed exact certificate

Python standard-library integer/Fraction/F_p[√2] checker: d25_a216_cm_hasse_antecedent_guard_20261030.py. It verifies exact Hilbert polynomial at j, the full Gauss quadratic polynomial transformation, entire coefficient reduction from Hasse, Legendre reflection, and both target classes' Hasse zero in F_(p²), plus source P_m root in F_p.

**115/115 primes p≡1 mod6, 7≤p<1500 passed; 60/60 frozen-class primes passed.** Original fixed witnesses (p,m,P_m(1/2),P'_m(1/2)): (13,2,0,1), (19,3,0,2), (373,62,0,215). Executed checker SHA256: 3ab817039aa13c297f44017fbfc594d11f62b81612ffe0b7bdaeb7e557e73720. The unbounded theorem rests on the six steps and cited established theorems, **not** on 115 samples. Independent Driver review/formal proof checker **NOT EXECUTED**.

### Sources

* Classical Hilbert polynomial H_−24: https://www2.math.ethz.ch/EMIS/journals/NYJM/j/2019/25-49p.pdf (2019, explicit polynomial); exact singular value: https://www.kaynet.or.jp/~kay/misc/jtau6.html .
* Classical Deuring criterion: Chris Blake, Bull. London Math. Soc. 46 (2014), https://doi.org/10.1112/blms/bdu079 .
* Hasse coefficient criterion: Christophe Debry, https://arxiv.org/abs/1303.5002 .
* Gauss quadratic transformations: NIST DLMF §15.8(iii), https://dlmf.nist.gov/15.8 .
* Sun transfer with separate antecedent/hypotheses: https://arxiv.org/abs/1503.03418 .
* Prior Clausen and moment proof: research_notes/portable_direct/20261030_onhour_d25_A216_clausen_double_root_second_moment.md at 154ab052d3f249639c7af245ed7d9899e9efd99a.

## Exact continuation and native scope

**Mother:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Immutable scientific frontier c47e13e4aba0e006366f989d6334d443f6333ae3; preserve accepted D24 UR, previous regular middle tail and finite Clausen. **Not to redo:** those and the now-proved all-prime CM antecedent.

**Next research action:** attack the original source-faithful *joint p³ digit* U_p+6V_p directly: combine the CM modular input at the next p-adic order with the previously constructed two-zone second jet and regular signed middle tail. Retain the two residue classes' character signs, exact denominators and all source labels. No axiom standing in for LIFT, no native-benchmark substitution.

**Native benchmark remains pending** under issue #1559: at p=373, original H0/B0 divided-power [X]U modulo 139129, genuine module rank/semilinear Frobenius/eta, odd Green/Hesse signs, κ and Δ−R, independent reproduction. The latest Site credential is static read-only (research_authority_granted=false; write_relay_enabled=false); own checkpoint-list read returned ACCESS_DENIED. Exact Source session/claim/run/request/ownership are **unknown**. No fresh dispatch, CLAIM, freeze or Result; no bypass or reuse of maintenance conversation. Author-side proof/evidence are durable only; Source registration/admission remain PENDING.
