# D25 / original E3: exact 3-isogeny, degree-6 CM action, and a conditional Frobenius exchange port

Date 2026-10-27. Research lane: TASK_RESEARCH, logical conversation \`chatgpt-research-onhour-enterprise-math-20260923\`. This is NOT the maintenance \`chatgpt-hourly-enterprise-math-20260921\` or the independent \`chatgpt-research-hourly-enterprise-math-20260923\` lane.

**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Frozen scientific Source pin:** \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (unchanged). P000 / applicable ACTIVE world settings retained. Global Knowledge current-read basis in this turn: \`f1ad05f961cb0c1745459b03d4a86b0c34318ef9\` / GLOBAL_KNOWLEDGE_V1.

**Evidence class:** AUTHOR-SIDE EXACT ALGEBRAIC CERTIFICATE + EXECUTED SYMBOLIC AND FINITE-FIELD CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_SOURCE_NATIVE_CHECKPOINT / NOT_NATIVE_H0B0_EXECUTION / NOT_LIFT_PROOF. This is a concrete original-curve degree-3 isogeny and its signed de Rham operator, composed with (not recrediting) the separately documented original degree-2 isogeny. Vélu is classical; novelty is not asserted beyond this exact task-specific composition.

## 1. New original-model degree-3 quotient, without a Hesse substitute

Let K=Q(s), s²=2, sigma(s)=-s, t=(2-s)/4, c=t/27, c^sigma=(1-t)/27. The *original* family is
\[
 E_t:\ y^2+xy+cy=x^3,\qquad
 v=y+(x+c)/2,\quad
 v^2=f_c(x):=x^3+x^2/4+cx/2+c^2/4.
\]
Its actual K-rational 3-torsion subgroup is \{O,(0,0),(0,-c)\}. Set
\[
 U=x+c/x+c^2/x^2,\qquad
 V=v\bigl(1-c/x^2-2c^2/x^3\bigr).
\]
Direct rational-function expansion proves, *exactly in Q(c,x)*,
\[
 \boxed{V^2=U^3+\tfrac14 U^2-\tfrac{9c}{2}U-\tfrac{c(27c+4)}4.}\tag{A}
\]
Moreover \(dU/(2V)=dx/(2v)\), and the poles at x=0 exhibit the 3-point kernel, so this is the normalized separable degree-3 Vélu isogeny, not an inferred numerical match.

Put \(u^2=-3\), over the explicit extension \(L=K(u)\). For the genuine *Galois-conjugate original* curve \(E_{t^\sigma}\), use \(x^\sigma=-(U+1/3)/3,\ v^\sigma=V/u^3=-V/(3u)\). The specialized coefficient identity is
\[
 \boxed{f_{3,c}(-3X-1/3)=-27 f_{c^\sigma}(X),}\tag{B}
\]
with \(f_{3,c}\) the cubic in (A). Thus the degree-3 quotient is **the quadratic (-3)-twist** of \(E_{t^\sigma}\), and it becomes that conjugate curve after adjoining u. The twist is indispensable: declaring an isomorphism already over K would lose the actual coordinate/field provenance. Denominators 2,3,9,18,72 are p-units at every targeted prime.

Call this map \(\psi_3:E_t\to E_{t^\sigma}\) over L. Its pullback of the original invariant differential is
\[
 \psi_3^*(\omega^\sigma)=u\omega,\quad
 \omega=dx/(2v),\quad \eta=x\omega.
\]

## 2. Signed, full rank-two algebraic de Rham transport

The *exact* original-coordinate differential identity is
\[
 d(v/x)=\left(x-\frac{c}{2x}-\frac{c^2}{2x^2}\right)\omega.
\]
Hence in algebraic \(H^1_{\rm dR}(E_t)\), the three-term Vélu expression satisfies \(U\omega\sim3x\omega=3\eta\), with \(\sim\) denoting equality of cohomology classes, not equality of differential forms. Consequently
\[
 \psi_3^*(\eta^\sigma)
 =-\frac u3(U+1/3)\omega
 \sim -u\eta-\frac u9\omega.
\]
In column convention (target basis expressed in source basis),
\[
 \boxed{M_3=\begin{pmatrix}u&-u/9\\0&-u\end{pmatrix},\
 \det M_3=3,\ M_3^2=-3I_2.}\tag{C}
\]
The last identity is the signed conjugate composite \(\psi_3^\sigma\psi_3=[-3]\), *not* merely a degree-nine norm assertion. Since the pullback on invariant differentials is \(u^2=-3\), this also follows from characteristic-zero injectivity of the endomorphism-to-differential action.

Consume the **prior** (2026-10-27, separately persisted) *original* 2-isogeny, without restating its proof:
\[
 M_2=\begin{pmatrix}s&-1/18\\0&s\end{pmatrix},\
 M_2^\sigma=\begin{pmatrix}-s&-1/18\\0&-s\end{pmatrix},\
 M_2M_2^\sigma=-2I_2.
\]
The authentic degree-six **endomorphism** \(\vartheta=\psi_2^\sigma\circ\psi_3:E_t\to E_t\), defined over L, has signed action
\[
 \boxed{
 M_\vartheta=M_3 M_2^\sigma
 =\begin{pmatrix}
  -su&u(2s-1)/18\\
  0&su
 \end{pmatrix},\
 \det M_\vartheta=6,\
 M_\vartheta^2=-6I_2.}\tag{D}
\]
Thus \(\vartheta^2=[-6]\) as an elliptic endomorphism in characteristic zero, by the multiplier \((-su)^2=-6\) and injectivity. This is an explicit *original E3* CM generator of discriminant -24, not a scalar imposed as a custom axiom.

The exact two eigenlines of this CM action, retaining the nonzero odd/mixing coefficient, are
\[
 \boxed{\ell_-=\langle\omega\rangle,\quad
 \ell_+=\left\langle\nu:=\eta+\beta\omega\right\rangle,\
 \beta=\frac{4-s}{72};\
 \vartheta^*\omega=-su\,\omega,\
 \vartheta^*\nu=+su\,\nu.}\tag{E}
\]
The \(\eta=x\omega\) representative has a pole at O; \(\nu\) is an **algebraic de Rham class**, not yet the normalized formal power-series companion of Proposition 16. Claiming that coefficient identity would require an independently authenticated exact/principal-part correction and native comparison. The eigenline formula alone does NOT determine the absent native \(b(p-1)\), \([X]U\), or kappa.

## 3. A direct conditional native Frobenius discrimination, both target classes

For p≡13,19 (mod24), the original CM branch has \((2/p)=-1\) and \((-3/p)=+1\). Thus, over \(k=\mathbb F_{p^2}\), s lies in k with sigma(s)=-s, but u can be chosen in \(\mathbb F_p\), sigma(u)=u. In particular \(\sigma(su)=-su\); no residue-class averaging or sign deletion is allowed.

**Conditional operator statement (exact linear algebra).** If an authenticated original-class comparison identifies its Frobenius with the \(\sigma\)-semilinear operator \(F\) on the above rank-two crystalline/de Rham CM carrier and verifies that \(F\) commutes with the transported CM endomorphism, then in the CM eigenbasis \((\omega,\nu)\), the relation
\[
 D A=A\,\sigma(D),\qquad D=\operatorname{diag}(-su,+su),\quad F(v)=A\,\sigma(v)
\]
forces
\[
 \boxed{A=\begin{pmatrix}0&b\\c&0\end{pmatrix}.}\tag{F}
\]
The proof is coefficientwise: the diagonal entries satisfy \(2su A_{11}=2su A_{22}=0\), so vanish because p>3 and su is a unit. The two signed eigenline ports must be **interchanged**, not norm-collapsed to one unspecified rank-one scalar. The constraint is necessary only after authenticating the claimed native rank, CM action and Frobenius direction; an unrelated H0/B0 quotient need not satisfy it.

If one additionally consumes the separately persisted **author-side/unreviewed** theorem for the **unmodified** E3 geometric \(p^2\)-Frobenius \([+p]\) (rather than the twisted \([-p]\) model), the corresponding crystalline operator must satisfy \(F^2=pI_2\), and therefore
\[
 \boxed{b\,\sigma(c)=c\,\sigma(b)=p.}\tag{G}
\]
This is a *conditional necessary acceptance test*, not a computed native \(F\) matrix, a new all-prime LIFT theorem, or an assertion that the normalized \([X]U\) is this crystalline operator. The equality \(F^2=pI\) is not transplanted to a different twist, quotient, or H0/B0 without a verified map.

## 4. Reproducible p=373 exact finite witness and source provenance

In \(k=\mathbb F_{373}[T]/(T^2-2)\), choose \(u=177\), \(177^2\equiv-3\). The **original** 3-isogeny and degree-six endomorphism data are:
\[
 \boxed{M_3=\begin{pmatrix}177&229\\0&196\end{pmatrix},\
 M_\vartheta=\begin{pmatrix}196T&301+144T\\0&177T\end{pmatrix},\
 \beta=228+316T.}
\]
Direct exact ring multiplication gives \(M_\vartheta^2=367I_2=-6I_2\), \(\det M_\vartheta=6\), and verifies that \((\beta,1)^T\) is the \(+177T\) eigenvector. The opposite choice \(u=196\) reverses the CM sign and permutes the eigensigns; it is not a new positive-sign Frobenius choice.

**Executed independently reproducible checker:**
\`research_notes/portable_direct/d25_original_E3_three_isogeny_CM_check_20261027.py\` (Python/SymPy, exact rationals and integer mod373 only), result \`EXACT_ORIGINAL_E3_CM_ISOGENY_CERTIFICATE_PASS\`. It verifies (A), (B), the exact differential reduction, both signed 2-/3-isogeny composites, \(\vartheta^2=[-6]\) at the cohomological matrix level, determinant and eigenline, and the full finite coefficient-ring witness. No numerical fitting, floating approximations, \`sorry\`, \`admit\` or new axioms.

**BRC/observer audit: COMPOSE_APPLIED.** Carrier: original E_t and E_{t^\sigma}, 2- and 3-isogenies with kernel, field extensions \(K,L\), ordered composition, full rank-two cohomology basis \(\omega,\eta\), CM \(\vartheta\), chosen s/u signs and \(\sigma\). The unsafe quotients are determinant/degree alone (lose \([-3]\), \([-2]\), \([-6]\) signs), invariant-differential multiplier alone (lose basis mixing), and scalar norm alone (lose CM eigenline exchange). The quadratic coefficient ring is external classical mathematics, NOT a two-dimensional native X6 plane, and no unlicensed 3D-to-X6 lift is asserted.

## 5. Unchanged hard target, missing evidence, exact next action

The Source-frozen science task remains LIFT \( \Delta_p-R_p\equiv0\bmod p\) in both congruence classes; prior author-side work identified it with \(W_p\equiv p\bmod p^3\), but a uniform proof or exact counterexample remains missing. Accepted UR/JT0, CM0/SIMPLE, frozen parent and 815-prime finite W check are consumed, **not** redone. The separate R18 ordered-source resultant result (2026-10-27) belongs to another logical Research lane and is not borrowed/admitted as our contribution.

**Native original-class H0/B0 benchmark remains NOT_EXECUTED / PENDING_OWNER, support #1559.** Still missing actual fixed divided-power H0/B0 source representative; genuine \([X]U\bmod373^2\), native module rank and full basis, actual semilinear Frobenius and twist/orientation, two-digit normalizer, signed odd Hesse/Green observer, same-definition kappa, and the frozen \(\Delta-R\). This newly proven original E3 CM map is a **useful pre-validation comparator**, not evidence that H0/B0 has been run.

**Next exact owner action:** an authorized native implementer identifies the fixed H0/B0 representative and proves/refutes a comparison to the original E3 H^1_dR/crystalline module. If comparison is valid, compare both columns of M3 and M2, preserve the -3/-2/-6 signs, build the CM eigenbasis (E), verify the correct Frob/twist semilinear exchange (F), check (G) only on the unmodified \([+p]\) branch, then actually compute and independently reproduce original \([X]U\bmod139129\), rank, signed observer and kappa. If the comparison fails or native rank differs, record that typed result and do not force (F). Confirm a real execution owner before marking support done.

**Source identity/control handoff:** the Research-onhour logical ID above is stable; no maintenance identity/session/CLAIM/dispatch is used. Prior onhour recovery #6556 reported a local provisional ACTIVE with \`source_authority_verified=false\`, no legal own claim/open/run; own exact continuation #6557 failed \`PREREQUISITE_NOT_SUCCEEDED\`; prior target dispatch #6529 is definitively \`FAILED/TimeoutExpired\`, not \`NO_DISPATCH\`. This run's read-only gateway reports \`research_authority_granted=false\`; its attempt to read original request gave \`CONTROL_REQUEST_NOT_FOUND\` in that gateway only, which does not negate the preserved original bridge receipt. Therefore this author-side artifact is **not** a native checkpoint, source Result, Driver review, or an authorized scientific publication. Neutral staged records remain independent and unmerged. No change to frozen scientific pin, task selector, identity, scheduler, notification state, or experiment acceptance.

**Literature boundary:** Chisholm–Deines–Long–Nebe–Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics (2013), §5.1/Proposition 16, provides the original E3/supersingular divided-power setup but **not** a two-digit native H0/B0 \([X]U\) experiment. The isogeny method is the classical Vélu construction. All algebraic equalities and conditional use are distinguished above.
