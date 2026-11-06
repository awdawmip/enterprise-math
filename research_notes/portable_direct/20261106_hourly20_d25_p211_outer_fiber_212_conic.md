# D25: full p=211 two-source collision fiber (212 points)

Date: 2026-11-06. Status: AUTHOR-DERIVED EXACT FINITE-FIELD RESULT; independently executed local arithmetic; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3. Related pre-existing exact jet data and source: 20261106_hourly20_d25_outer_source_exception_p211_p3.md and d25_p211_second_digit_certificate_20261106.py. Logical Research lane is configured as chatgpt-research-hourly-enterprise-math-20260923; this is not independently authenticated platform identity.

## Theorem and domain

For p=211, m=35, s=(70,105,140), define the three labelled factors and the signed weighted observer

$$ U_j(\mathbf{x})=(-1/2)^j\prod_{i=1}^3\binom{s_i+x_i}{j},\quad
\mathcal W(\mathbf v)=\sum_{j=0}^{210}(6j+1)U_j(211\mathbf v)\pmod{211^3}. $$

Take v*=(-1/3,-1/2,-2/3) and perturb v* by (x,0,y), for x,y in F_211. The observable is well-defined on residue classes (the outer first-jet values vanish mod 211). For all 211^2 pairs,

$$\boxed{\mathcal W(\mathbf v_*+(x,0,y))-\mathcal W(\mathbf v_*)\equiv211^2Q(x,y)\pmod{211^3}},$$

$$\boxed{Q(x,y)=11x^2+29xy+91y^2+165x+141y\pmod{211}}.$$

The zero fiber Q=0 contains EXACTLY 212 ordered shifts, including 211 nonzero shifts. Exactly 209 shifts have both outer coordinates nonzero.

## Proof: second-order Taylor and signed-source jets

The previous exact source-jet recurrence supplies

$$A=(28696,10279,42622)\pmod{211^2},\quad T=A\bmod211=(0,151,0),$$

$$H=\begin{pmatrix}22&170&29\\170&4&71\\29&71&182\end{pmatrix}\pmod{211}.$$

For every delta=(x,0,y), the finite polynomial Taylor formula is valid modulo p^3 because all factorial denominators j! for j<p are p-adic units:

$$\mathcal W(v_*+\delta)-\mathcal W(v_*)\equiv p A\cdot\delta+p^2\left(v_*^TH\delta+\frac12\delta^TH\delta\right)\pmod{p^3}.$$

Since A_1=211*136 and A_3=211*202, the linear coefficients after division by p^2 are respectively 136+29=165 and 202+150=352=141 mod 211. The quadratic coefficients are H_11/2=11, H_13=29, H_33/2=91. This establishes Q for EVERY pair, not merely tested pairs.

## Proof: 212-point classification

The discriminant of the homogeneous quadratic part equals 29^2-4*11*91=-3163=2 mod211. Since 211=3 mod8, the value 2 is a quadratic nonresidue. The unique center of Q is (205,108), giving

$$Q(x,y)=11(x-205)^2+29(x-205)(y-108)+91(y-108)^2+156.$$

Thus Q=0 is an anisotropic nondegenerate binary quadratic form taking the NONZERO value 55 mod211. Any such form is a nonzero scalar times the norm from F_(211^2) to F_211. The norm map is surjective, with multiplicative kernel of cardinality 211+1, so every nonzero value has exactly 212 preimages. The axis solutions are precisely (0,0), (0,17), and (196,0). Hence 209 zeros have both x and y nonzero.

## Source information lost: explicit collision

The pair (x,y)=(1,53) lies on Q=0. Direct full 211-term integer-modular computation gives both weighted sums equal to 211 mod211^3. Yet the first LABELLED coefficient changes:

$$\left(U_1(211(v_*+(1,0,53)))-U_1(211v_*)\right)/211
\equiv35+53\cdot123=13\ne0\pmod{211}.$$

Therefore even two digits of a signed WEIGHTED SCALAR cannot uniquely identify this one source coefficient. This is a BRC observer-fiber statement for the stated population, labelled sources, perturbation operation and p-adic precision. It is not a conclusion about authentic native H0/B0, Frobenius, eta/kappa or the frozen LIFT theorem.

## Verification and continuation

A standalone Python finite-modular recurrence was actually run on the following exact finite domain: all 44,521 pairs were evaluated for the polynomial Q; all 212 zero pairs were independently checked using the original full 211-term rational weighted sum mod211^3; additionally eight nonzero pairs checked the Q formula. Observed PASS: 212 zeros, 211 nontrivial zeros, 209 with both variables nonzero; sample (1,53) weighted 211=211 and local j=1 difference/p=13. Companion script: d25_p211_outer_fiber_conic_20261106.py. No native experiment or independent review is asserted.

Next science: derive conditions for outer-source conic degeneration/nondegeneration in other p=13,19 mod24 cases; retain source labels before reducing observer fibers. Universal T1+T3=0 remains an open symbolic-proof question; compensation Theta and original p373 H0/B0 plus Frobenius remain open. Mother goal remains Delta_p-R_p=0 mod p for p=13,19 mod24.

Native control: earlier D25 checkpoint remains the highest reported Source frontier; no new authorized Source write established. Original pending read requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 were reconciled this run to QUEUED following EVENT_COLLECTION_IO, not treated as final. Preserve old session/staging and owner history; support #1558 handles lawful successor transition. No new CLAIM, OPEN, checkpoint, review or freeze claimed.
