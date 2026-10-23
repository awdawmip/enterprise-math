# D25/LIFT — Third-digit two-seam harmonic certificate with no independent Fermat quotient

2026-10-24 | TASK_RESEARCH | **AUTHOR-DERIVED ALL-TARGET-PRIME p³ CONGRUENCES; EXACT FINITE CHECKS; UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged); current repository control head was separately checked at d24edb655afe259cdf4bf0a65c1d536138081a32. Research-lane logical label specified by the recurring task: chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921 and the onhour Research lane. A label is not a new Source-issued identity, CLAIM or execution credential. Account rules verified main c99ad291db5bec0b509a17257752504f64483274; P000 projection status ACTIVE_LOCKED and canonical blob SHA1 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched.

This is a **new third-digit composition**, not a reproof of the cited authors' already published first-seam and six-block products. Prerequisites (portable author proofs, not independent admissions):
- [Exact upper-to-lower seam transfer](20261024_hourly_d25_two_seam_collapse_mod_p2.md), especially ST-exact.
- [Exact first-seam-to-target normalization](20261024_hourly_d25_T2_Gm_normalization_p2.md).
- [Six-block p² harmonic repair and T2/G third digit](20261024_hourly_d25_sixblock_p2_repair_T2_G_p3.md), especially Q6-2 and TG3.
- [Original terminal-sensitive two-seam endpoint](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md), fixing both actual coefficients and the n=4m boundary.

## Exact question, typed observer, and definitions

For each prime p=6m+1>=7 let R_n be the original hypergeometric sequence from the frozen endpoint, and define

\[
T_2=R_{2m}/p,\qquad T_4=R_{4m}/p,\qquad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2}.
\]

Use p-integral rational harmonics \(H_r=\sum_{j=1}^r j^{-1}\), \(Q_r=\sum_{j=1}^r j^{-2}\); write \(h_1=H_m,\ h_2=H_{2m},\ q_1=Q_m,\ q_2=Q_{2m}\). The original *combined* seam-plus-terminal scalar is

\[
\mathcal C_m
=\underbrace{\frac{(p+2)(4p+1)}{3(2p+1)}}_{\alpha_p}T_2+
\underbrace{\frac{-8p^2+14p-3}{4p-1}}_{\beta_p=3-2p\ {\rm exactly}}T_4.
\]

Original branch labels n=2m and n=4m plus the n=4m+1 terminal remain distinct. We ask for the complete scalar observer mod p³, **one digit finer** than the existing open LIFT's mod-p² divided certificate. The result does not claim native-X6 arithmetic or a physical interpretation.

## Theorem A — standalone upper seam has a simple p³ harmonic normal form

Define
\[
\boxed{L_m=2h_1-\frac{11}{3}h_2,\qquad
M_m=\frac{L_m^2}{2}+\frac{q_1}{3}-\frac{13q_2}{18}-4.}
\]

Then, for **every prime** p=6m+1>=7, in \(\mathbb Z_{(p)}/p^3\),

\[
\boxed{\displaystyle
\frac{T_4}{G_m}\equiv
-\frac13\left(1+pL_m+p^2M_m\right)\pmod{p^3}.}\tag{T4G3}
\]

In particular the third-digit scalar needs neither an independent Fermat quotient q_p(6) nor H_{3m}; it needs only the two lower harmonic boundaries and their quadratic reciprocal observers. The p³ statement uses the actual harmonics as rational p-local numbers, not digit representatives inserted without higher-precision correction.

### Proof, retaining every seam factor

The inherited all-m exact product is
\[
\frac{T_4}{T_2}
=\frac{1}{9\,6^{p-1}}
\left[\prod_{j=2m}^{p-2}\left(1+\frac pj\right)\right]^2.
\tag{ST}
\]
Let \(d=\sum_{j=2m}^{p-2}j^{-1}\), \(e=\sum_{j=2m}^{p-2}j^{-2}\), \(q=q_p(6)=(6^{p-1}-1)/p\). Direct expansion of the *finite* product gives
\[
\frac{T_4}{T_2}\equiv\frac19
\left[1+p(2d-q)+p^2(2d^2-e-2dq+q^2)\right]\pmod{p^3}.
\tag{ST3}
\]
All denominators are p-units.

We require the **second digit** of d and q, not just their mod-p residues. Reciprocal pairing plus \(\sum_{k=1}^{p-1}k^{-2}\equiv0\bmod p\) proves \(H_{p-1}\equiv0\bmod p^2\) for p>=5: for \(1\le k\le(p-1)/2\),
\(1/k+1/(p-k)\equiv-p/k^2\bmod p^2\), and the half sum of inverse squares is zero mod p. Also \(Q_{p-1}\equiv0\bmod p\). Since \(2m=(p-1)/3\),
\[
\begin{split}
d&=H_{p-2}-H_{2m-1}
\equiv -2-h_2-2p\pmod{p^2},\\
e&=Q_{p-2}-Q_{2m-1}\equiv8-q_2\pmod p.
\end{split}\tag{DE}
\]
The prior independently proved six-block identity Q6-2 states, with
\(h=(3h_1+h_2)/6\),
\[
q_p(6)\equiv-h+pz\pmod{p^2},\qquad
z=\frac{h^2}{2}-\frac{3q_1+2q_2}{36}.
\tag{Q6}
\]
Put \(d_0=-2-h_2\), \(a_0=2d_0+h=-4+h_1/2-11h_2/6\). Equations (ST3), (DE), (Q6) give
\[
\frac{T_4}{T_2}\equiv\frac19\{1+pa_0+p^2[
-4-z+2d_0^2-(8-q_2)+2d_0h+h^2]\}\pmod{p^3}.\tag{R}
\]
The inherited TG3 identity is
\[
\frac{T_2}{G_m}\equiv-3(1+pX+p^2Y)\pmod{p^3},\quad
X=4+\frac32h_1-\frac{11}{6}h_2,\quad
Y=8+\frac12X^2+\frac14q_1-\frac{16}{9}q_2.
\tag{TG3}
\]
Multiply (R) with (TG3). The p coefficient is
\(X+a_0=2h_1-11h_2/3=L_m\).
Expanding the p² coefficient
\(Y+Xa_0-4-z+2d_0^2-(8-q_2)+2d_0h+h^2\)
and collecting terms gives exactly
\(\tfrac12L_m^2+q_1/3-13q_2/18-4=M_m\).
This proves (T4G3) for every stated prime, with no unlicensed inversion of p. QED.

## Theorem B — the original **two** seam contributions jointly through p³

Set
\[
\boxed{J_m=\frac{37}{9}+\frac53h_1-\frac{22}{9}h_2,}
\]
\[
\boxed{
K_m=14+\frac{17}{12}h_1^2-\frac{77}{18}h_1h_2+
\frac{121}{36}h_2^2+\frac{109}{18}h_1-\frac{385}{54}h_2+
\frac5{18}q_1-\frac{77}{54}q_2.
}
\]

Then the **original** seam-plus-terminal contribution has the all-target-prime congruence
\[
\boxed{\displaystyle
\frac{\mathcal C_m}{G_m}
\equiv-3(1+pJ_m+p^2K_m)\pmod{p^3}.}\tag{BOTH3}
\]

**Proof.** Use the *actual original coefficients*, not seam replacements:
\[
\alpha_p=\frac23+\frac53p-2p^2+O(p^3),\qquad
\beta_p=3-2p\quad(\text{exactly}).
\]
The expansions make sense p-locally for all p>=7. Substitute (TG3) and (T4G3):
\[
\frac{\mathcal C_m}{G_m}
\equiv-3\alpha_p(1+pX+p^2Y)
-\frac{\beta_p}{3}(1+pL_m+p^2M_m)\pmod{p^3}.
\]
Constant coefficient is -3. The p coefficient is \(-3J_m\); direct collection of the p² coefficient is \(-3K_m\). A denominator-free equivalent declaration of the second coefficient is
\[
108K_m=
153h_1^2-462h_1h_2+363h_2^2+654h_1-770h_2+
30q_1-154q_2+1512.
\]
All rational denominators (2,3,9,12,18,36,54,108) are p-units. The formula follows by finite exact algebra. QED.

**Precision caveat.** (BOTH3) isolates *both* seams one order beyond the currently sought LIFT; the regular forcing sum still has to be computed. It does not imply either \(\mathcal C_m/G_m=-3(1+pJ_m+p^2K_m)\) exactly in Q or that the full \(\mathcal K_p\equiv G_m\pmod{p^2}\) holds. Do not use (BOTH3) to assert a third-digit LIFT without separately resolving the regular forcing sum and the original endpoint's source-specific requirements.

## Reproducible exact author checks and provenance

A Python 3 standard-library Fraction/factorial author check independently rebuilt the **original** factorial forms
\[
R_{2m}=\frac{(8m)!}{216^{2m}((4m)!)^2},\quad
R_{4m}=\frac{((12m)!)^2((2m)!)^2}
{216^{4m}((6m)!)^2((4m)!)^2(8m)!},
\]
formed \(T_2,T_4,G_m,\alpha_p,\beta_p\) as exact rationals, and reduced numerator times the modular inverse of denominator modulo p³ only after exact cancellation. No floating-point approximation. For **all 43 target primes p=6m+1 with 1<=m<80** (up to p=463), both (T4G3) and (BOTH3) returned zero residual modulo p³. Independent direct recurrence multiplication (the original R_{n+1}/R_n, not its factorial result) also matched both factorial inputs exactly for m=1,...,8, including composite p=6m+1.

Selected separate witnesses (p; actual T4/G residue mod p³; actual combined C/G residue mod p³):
- 7: (65, 67)
- 13: (2162, 2116)
- 19: (2438, 4310)
- 31: (20470, 7158)
- 37: (15922, 774)
- 61: (6608, 188975)

These checks are **finite author self-tests**, not a Source-native benchmark, independent review or universal proof. The universal theorem relies on the exact finite-product proofs and the previously stated algebraic lemmas. Source-specific CM/divided-power representative, leading normalization and same-class comparison remain separate and missing.

### BRC / source and observer status

BRC typed composition: REUSE_APPLIED / COMPOSE_APPLIED. Original carrier retains both labeled seams n=2m and n=4m, the upper terminal, exact rational signs/weights, their p-valuation/unit sectors and harmonic second-digit repair. Observer: the \(\mathbb Z_{(p)}/p^3\) scalar of the original combined seam; future operations: combination with the *unchanged* regular forcing sum and exact original endpoint. (ST) is the reconstruction certificate for the upper seam when compressed to this observer. Finite harmonic remainders are not discarded as positive-mass cancellations; the p³ coordinate specifically repairs information that a coarse mod-p projection erases.

**Last durable scientific frontier:** current Source-native checkpoint and immutable pin remain separate from this portable note. This note is author evidence only, UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT; no Claim/open/run/freeze/driver review or platform execution credential is asserted. Current Sites read-only connection reports research_authority_granted=false and the new exact direct continuation request returned CONTROL_QUOTA; the previous successful ordinary-control D25 packet is historical, not a fresh authorization read. Bridge recovery request, if still queued, must be read under its **original request_id** before any new control writes.

**Smallest unfinished mathematical unit:** express the regular forcing sum's p² coefficient via the prior LOW first jet plus both high-sector finite sums, and determine (with exact boundary terms at m,2m,4m) whether the coefficient equals the negative of the newly exposed -3J_m term after the inherited first-digit cancellation. For the original LIFT, continue to target the exact existing regular-sum congruence modulo p² (not a third-digit claim). Supply native Source CM normalization and independently verify the final original benchmark before any formal acceptance. Do not repeat the 43-prime scan as if it were new progress.
