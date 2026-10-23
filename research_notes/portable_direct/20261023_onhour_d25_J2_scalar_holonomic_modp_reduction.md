# D25/LIFT — Exact scalar elimination of the high-band first parameter jet modulo p

**2026-10-23 | TASK_RESEARCH | AUTHOR-PROVED / EXACT_RATIONAL_SELF_CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** Research conversation provenance: \`chatgpt-research-onhour-enterprise-math-20260923\` (not maintenance, and not a currently granted Source session). Parent frozen Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\` / \`TP2-B6F4FC938FF94941C1B7\`; original source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, unchanged. No native execution, independent review, Result/freeze, or formal checkpoint implied.

**Immediate, exact dependencies consumed:** \`research_notes/portable_direct/20261023_onhour_d25_J2_head_tail_single_parameter_4F3.md\` @ \`d20a2d935c4d0f05ab220148b2276f8a0e3293c7\`, and \`research_notes/portable_direct/20261023_onhour_d25_J2_seam_forced_holonomic_jet.md\` @ \`41574a32721b72d573c98bf57960b610a6861dbb\`. Those give *exact* finite polynomials \(F_0,F_1\), the original full-tail \(J_m^{(2)}\), and a two-jet forced first-order operator; do not re-prove the B11/WZ or low-endpoint band decomposition. GLOBAL_KNOWLEDGE_V1 read snapshot \`main@61cfa2a580230863c0d02b5f818381adbb3cb11b\`. P000 ACTIVE_LOCKED, no native-X6 implication.

## 1. The new exact one-scalar cancellation

Let \(m\ge1\), set \(p=6m+1\) (not necessarily prime for the **exact** identity), and take the signed rational coefficient polynomials of the prior proof:

\[
F_0(z)=\sum_{r=1}^{3m}u_{r-1}z^{r-1},\qquad
F_1(z)=\sum_{r=1}^{3m}u_{r-1}J_r^\circ z^{r-1},
\]

where \(u_{r-1}=(-1)^m m!\,c_r(r-1)!/[2^{m+1}(m+r)!]\), \(c_r=1\) for \(r\le m\), \(1/3\) for \(r>m\), and \(J_r^\circ\) is the original reflected harmonic correction with piecewise \(d_r\). Let

\[
\mathcal L_mF=z(1-z)F'(z)+(m+1-z)F(z),\quad
R_m(z):=\mathcal L_mF_1(z).
\]

The full Beta reflected second-digit port obeys the already proven exact operator representation

\[
J_m^{(2)}=\left[(3z\partial_z+2)F_1(z)+F_0(z)\right]_{z=1/2}.
\]

But evaluating \(\mathcal L_mF_1\) at \(z=1/2\) gives

\[
R_m(1/2)=\frac14F_1'(1/2)+\left(m+\frac12\right)F_1(1/2).
\]

Eliminate \(F_1'(1/2)\) *exactly*, without a congruence approximation:

\[
\begin{aligned}
J_m^{(2)}
&=\frac32F_1'(1/2)+2F_1(1/2)+F_0(1/2)\\
&=6R_m(1/2)-6\left(m+\frac12\right)F_1(1/2)+2F_1(1/2)+F_0(1/2).
\end{aligned}
\]

Therefore the **new exact rational theorem**, valid for all integers m≥1, is

\[
\boxed{J_m^{(2)}=F_0(1/2)+6R_m(1/2)-(6m+1)F_1(1/2).}
\tag{SCALAR-EXACT}
\]

This coefficient 6m+1 is a genuine *operator matching* feature at z=1/2 and is **exact**, not an artificially inserted target modulus.

## 2. Prime second-digit reduction and a rational seam witness

Now assume p=6m+1 is prime. All denominators of \(u_r,J_r^\circ,F_0,F_1,R_m\) are products of powers 2,3 and integers ≤4m<p (the reflected \(H_{4m}\), beta factorial \((m+r)!\), and rational finite difference denominators). They belong to \(\mathbb Z_{(p)}\). Consequently the *single* \(pF_1(1/2)\) term vanishes modulo p:

\[
\boxed{J_m^{(2)}\equiv F_0(1/2)+6R_m(1/2)\pmod p.}
\tag{SCALAR-MOD-P}
\]

This is precisely the order of precision needed for the p²-weighted reflected high-band term of LOW/EP; it would be **wrong** to assert the same equality modulo p² without retaining the last term of SCALAR-EXACT.

The holonomic differential certificate provides an *explicit* source polynomial for \(R_m\). Define, for \(1\le r<3m\) except the seam \(r=m\),

\[
\Delta_r=\begin{cases}
\frac1{2r}+\frac2{3(m-r)}+\frac1{3(3m-r)},&r<m,\\[3pt]
\frac1{2r}-\frac2{3(r-m)}+\frac1{3(3m-r)},&m<r<3m.
\end{cases}
\]

Then the complete value in SCALAR-MOD-P is a **finite rational nonnested** source plus exactly three harmonic boundary/seam evaluations:

\[
\boxed{\begin{aligned}
R_m(1/2)={}&
(m+1)u_0J_1^\circ\\
&+\sum_{r=1}^{m-1}\frac{r u_{r-1}\Delta_r}{2^r}\\
&+\frac{u_{m-1}}{2^m}
 \left(-\frac{2m}{3}J_m^\circ+\frac29\right)\\
&+\sum_{r=m+1}^{3m-1}\frac{r u_{r-1}\Delta_r}{2^r}\\
&-\frac{3m\,u_{3m-1}J_{3m}^\circ}{2^{3m}}.
\end{aligned}}
\tag{SOURCE}
\]

The surviving three harmonic values are original endpoint quantities, not invented correction constants. In particular
\[
J_m^\circ=-\frac1{2m}+\frac13H_{2m}+\frac13H_{4m},\qquad
J_{3m}^\circ=\tfrac12(H_{3m-1}-H_m)+\frac1{3m}+\tfrac13H_{4m},
\]
and \(J_1^\circ\) is the exact r=1 instance of the inherited formula. The \(1/3\) tail multiplicity and m-seam discontinuity remain explicit.

The **first-digit Beta port** \(F_0(1/2)=\int_0^{1/2}(x-\frac12)^m P_1(x)\,dx/x\) is already available as part of LOW/Beta. Thus all internal high-band harmonic sums needed for \(J_m^{(2)}\bmod p\) have been replaced by the first-digit Beta port, rational finite source and three harmonic endpoint terms. This is a smaller concrete joint-cancellation target, not a proof of its cancellation.

## 3. Executed arithmetic check, not independent admission

An author-side Python Fraction evaluator constructed \(u_r,J_r^\circ\), \(F_0(1/2),F_1(1/2),J_m^{(2)}\) from the raw piecewise harmonic definition, and \(\mathcal L_mF_1(1/2)\) by independently taking its polynomial coefficient formula. It asserted the exact SCALAR-EXACT, then for p=6m+1 prime computed both sides of SCALAR-MOD-P using integer modular inverses. Exact p-unit residues were:

| p | m | original full-tail J2 mod p | reduced F0+6R mod p | F1 mod p |
|---:|---:|---:|---:|---:|
| 7 | 1 | 4 | 4 | 1 |
| 13 | 2 | 5 | 5 | 0 |
| 19 | 3 | 0 | 0 | 6 |
| 31 | 5 | 22 | 22 | 8 |
| 37 | 6 | 18 | 18 | 14 |
| 43 | 7 | 6 | 6 | 21 |
| 61 | 10 | 60 | 60 | 14 |

The nonzero F1 at p=19 and p=31 confirms that SCALAR-EXACT's pF1 term is genuinely present before modular projection. Theorem strength rests on the differential operator proof, not the finite self-check. This is not a native benchmark run or independent Driver review.

## 4. Parent objective: exact remaining joint cancellation

The previous LOW/Beta certificate requires preserving the divided-first-digit \(-p2^{-m}C_m\) term, the pure A/mixed low second jets, reflected BC/mirror curvature, the \(-2V_m\) moment and target Fermat quotient \(\chi_p\). The new SCALAR-MOD-P can be substituted **at precisely the existing \(J_m^{(2)}\bmod p\) port**; no other term is redefined. The next discriminating scientific action is to pair \(\mathsf M_m^\sharp-2V_m\) with \(F_0(1/2)+6R_m(1/2)\), retaining the divided-first-digit and mirror correction, and seek a finite terminating contiguous-Dixon/B11 certificate for the resulting *joint* mod-p scalar. Do not equate \(J_m^{(2)}\) alone with curvature \(I_m/3\); actual p=13,19 counterexamples already refute that shortcut. The original EP/LIFT and native benchmark remain incomplete.

**Recovery/source integrity.** Same Research logical lane; original own control #6186 recovery is not Source ownership, #6187 exact continuation rejected PREREQUISITE_NOT_SUCCEEDED, #6188 original dispatch terminal FAILED/TimeoutExpired; all read, no duplicate requests. Source support #1539 owns registration defect. Direct Sites service version 0.6.11 still reported research_authority_granted=false, so there is no newly authorized own native session/CLAIM/open/checkpoint/freeze or benchmark assertion. GitHub source publication is a neutral author proof note and its verified immutable readback is not mathematical or Source task admission. P000, frozen Source pin, user notification and schedule remain untouched.
