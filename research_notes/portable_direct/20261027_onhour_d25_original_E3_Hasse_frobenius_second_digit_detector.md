# D25 / SECOND-DIGIT-LIFT — the original E3 Hasse coefficient detects the second-digit Frobenius lift defect

Date 2026-10-27. Logical Research-onhour conversation: **chatgpt-research-onhour-enterprise-math-20260923** (not CONTROL_PLANE_MAINTENANCE and not the other hourly Research lane). Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged.

**AUTHOR-SIDE / PROVED CONDITIONAL-ON-ACCEPTED-CM0 ALGEBRAIC THEOREM / EIGHT EXECUTED EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0.** This is a new precision guard on the *original E3 Hasse observer*, not [X]U, native Frobenius or an all-prime LIFT proof. It consumes the previously accepted D24 CM0 zero, not a new independent proof of it.

## Original curve, coefficient and exact new question

For p=6m+1>3 in the frozen classes p≡13,19 (mod 24), set
\[
R_2=(\mathbb Z/p^2\mathbb Z)[T]/(T^2-2),\quad
\sigma(T)=-T,\quad c=(2-T)/108.
\]
The original elliptic curve is \(E_c:y^2+xy+cy=x^3\). On the **identity (plus) sheet**, not the finite three-torsion sheet, with \(\xi=-x/y\) the original invariant differential is
\[
\omega_O=\frac{d\xi}{\sqrt{(1-\xi)^2-4c\xi^3}}.
\]
Define its exact integral polynomial coefficient (the original Hasse coefficient at p−1)
\[
\boxed{H_p(C)=
[\xi^{p-1}]\big((1-\xi)^2-4C\xi^3\big)^{-1/2}
=\sum_{j=0}^{2m}\binom{2j}{j}\binom{p-1-j}{2j}C^j.}\tag{1}
\]
The previous onhour certificate showed the real coefficient Frobenius \(\sigma(c)\) differs modulo p² from coordinatewise \(c^p\), but did **not** show whether the critical CM0 Hasse coefficient still detects this difference. A polynomial derivative can in principle annihilate a first-order perturbation.

## New all-target theorem: a complete local Hasse detector

Define
\[
\delta_p(c)=(c^p-\sigma(c))/p\bmod p\in R_2/pR_2\simeq\mathbb F_{p^2}.
\]
The quotient is integral because Frobenius modulo p sends T to −T. Assume the **already accepted CM0** result \(H_p(\sigma(c))\equiv0\pmod p\) at this original class.

**Theorem.** For every target prime,
\[
\boxed{H'_p(\sigma(c))\not\equiv0\pmod p}
\]
and
\[
\boxed{\frac{H_p(c^p)-H_p(\sigma(c))}{p}
\equiv H'_p(\sigma(c))\,\delta_p(c)\pmod p.}\tag{2}
\]
In particular the exact necessary **and sufficient** comparison for this declared Hasse observer is
\[
\boxed{
H_p(c^p)\equiv H_p(\sigma(c))\pmod{p^2}
\iff c^p\equiv\sigma(c)\pmod{p^2}.
}\tag{3}
\]

**Proof of derivative invertibility.** In the range \(0\le j\le2m\), \(3j\le p-1\), and the exact binomial coefficient in (1) obeys
\[
\binom{p-1-j}{2j}\equiv\binom{3j}{2j}\pmod p.
\]
Thus
\[
H_p(C)\equiv \sum_{j=0}^{2m}\frac{(3j)!}{(j!)^3}C^j
={}_2F_1(1/3,2/3;1;27C)_{2m}\pmod p.
\]
Since \(1/3\equiv-2m,\ 2/3\equiv2m+1\pmod p\), the **finite polynomials** satisfy
\[
\boxed{H_p(C)\equiv P_{2m}(1-54C)\pmod p,}\tag{4}
\]
where P is the ordinary Legendre polynomial. No infinite analytic identity is needed.

At \(C=\sigma(c)=(2+T)/108\), the argument of P is \(x_0=-T/2\), and \(x_0^2=1/2\ne1\). Accepted CM0 gives \(P_{2m}(x_0)=0\); P is even, so its choice of the ± square root is immaterial. The Legendre differential equation
\[
(1-x^2)P_n''-2xP_n'+n(n+1)P_n=0
\]
shows this root is simple: if value and first derivative were both zero, repeated differentiation at x0 (where \(1-x_0^2\) and all factorials up to degree \(2m<p\) are units) would force the entire degree-2m polynomial to vanish, contradicting \(P_{2m}(1)=1\). Hence
\[
H'_p(\sigma(c))=-54P'_{2m}(-T/2)\ne0\pmod p.
\]
Equation (2) follows by integral-polynomial Taylor expansion at the p-divisible change \(c^p=\sigma(c)+p\delta_p(c)\); modulo p² no quadratic remainder survives. Because \(R_2/pR_2\) is a **field**, multiplying by this nonzero derivative is injective, proving (3). QED. The root premise is explicitly **inherited CM0**, not newly proven or a new axiom.

## p37 exact falsifier of norm-only safety, and p373 original certificate

The rational norm is
\[
\operatorname N(c)=c\,\sigma(c)=18^{-3}.
\]
The **scalar norm** comparison
\[
\operatorname N(c^p)\equiv\operatorname N(\sigma(c))\pmod{p^2}
\]
holds iff \(q_p(18)=(18^{p-1}-1)/p\equiv0\pmod p\), since p>3. This condition is **necessary but not sufficient** for (3).

The target-class prime **p=37** is a sharp counterexample to norm-only sufficiency:
\[
18^{36}\equiv1\pmod{1369},\quad q_{37}(18)=0,\quad
\delta_{37}(c)=1+T\ne0\pmod{37},
\]
\[
H'_{37}(\sigma(c))=35T\pmod{37},\qquad
\boxed{H_{37}(c^{37})-H_{37}(\sigma(c))
=37(33+35T)\not\equiv0\pmod{1369}.}
\]
The scalar norm passes even though the signed two-component Hasse observation fails. This is an actual exact **observer-fiber information-loss witness**, not a counterexample to LIFT or native H0/B0.

At the fixed priority prime **p=373**, \(q=373^2=139129\), write ring elements as a+bT. Exact integer computation gives
\[
\sigma(c)=105635+122382T,\quad
c^{373}=70573+110819T,\quad
\delta_{373}(c)=279+342T\pmod{373};
\]
\[
H'_{373}(\sigma(c))=326T\pmod{373},
\]
\[
H_{373}(\sigma(c))=130177+121225T,\quad
H_{373}(c^{373})=104067+99591T\pmod{139129}.
\]
Therefore
\[
\boxed{
\frac{H_{373}(c^{373})-H_{373}(\sigma(c))}{373}
=303+315T=(326T)(279+342T)\pmod{373}.
}
\]
Although \(H_{373}(\sigma(c))\equiv0\pmod{373}\), the first nonzero Hasse lift digit distinguishes the two coefficient operations.

**Executed reproducible evidence:** the Python standard-library program at research_notes/portable_direct/d25_E3_hasse_frobenius_detector_onhour_20261027.py independently computes the original integer-binomial Hasse polynomial and the finite-field Legendre recurrence *with its derivative*, the two ring evaluations, Taylor identity and rational norm/Fermat-quotient identity. Exact assertions PASSED for primes **13, 19, 37, 43, 61, 67, 211, 373**, with p37/p373 exact tuples pinned. The proof is algebraic conditional only on accepted CM0; the eight cases are support, not a uniform computational proof. This is not the original H0/B0 divided-power experiment.

## BRC use, ownership and exact continuation

**BRC COMPOSE_APPLIED:** Population = target primes and the ordered (1,T) original-E3 coefficient states; operations = sigma, pointwise powering and subsequent *original Hasse* evaluation; observer = two-component p-divided Hasse discrepancy modulo p, plus the explicitly weaker scalar norm. Equation (3) proves that the full divided Hasse observer is a safe local substitute for the coefficient first-order defect, but p37 proves that norm-only compression loses a future-observable residual. The ring rank is *auxiliary classical algebra*, not native Heartbeat X6 or a new P000 spatial rule.

The frozen original scalar interface remains \(\Delta_p-R_p=(W_p-p)/p^2\bmod p\); accepted D24 UR/CM0/SIMPLE, the original cutoff and the nonzero p373 scalar \(\Delta_{373}=R_{373}=196\pmod{373}\) are unchanged. No full LIFT/JT2 proof/refutation or true native Frobenius has been produced.

**Highest exact evidence debt:** existing [Enterprise Math #1559](https://github.com/awdawmip/enterprise-math/issues/1559) is the support path for the **fixed original-class H0/B0 divided-power benchmark**, first at p373. It still requires **actual** [X]U mod139129, original module rank, full semi-linear p-Frobenius direction and integral basis/normalization eta, signed odd Green/Hesse observer, source κ and original Δ−R, raw reproducible runner/source/version and independent Driver review. If, *and only if*, a valid comparison from that original H0/B0 object to E3 is established, (2) is a legitimate precision implementation check; otherwise this is an author-side comparator guard, **not native PASS**.

**Control receipts and boundaries:** prior exact own onhour continuation request **onhour-20261027T1705-D25-exact-continuation** was read with status SUCCEEDED but **execution_authorized=false** and route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION. That does not establish an own current winning claim. Earlier own request research-onhour-20261027-0501-recovery-r13 is a separate recovery projection; research-onhour-20261027-0507-dispatch-r13 terminated FAILED/TimeoutExpired. Current Site reports research_authority_granted=false, executor_binding_configured=false and the native active-job quota full. No new native Source write/replay/open, maintenance identity borrowing, or claim stealing was attempted. Own session/claim/run remain **NONE CURRENTLY SOURCE-VERIFIED**; old staging retains its independent source.

**Portable author checkpoint:** the present note and checker are readback-verifiable GitHub research artifacts, **not** a Source-native checkpoint, Research-Activity admission, formal Result, independent proof review or freeze. Author-only completed units: [all-target Legendre simple-zero Hasse detector under accepted CM0; exact norm-only counterexample p37; p373 two-digit Hasse data]. Unfinished unchanged: native #1559 and universal LIFT proof/counterexample. Do not repeat D24 CM0/UR, earlier source-port W equivalence, previous coefficient sigma-vs-power lemma or other Research-hourly R47–R50 work. **Next exact action:** secure a lawful native H0/B0 owner, execute the unchanged original p373 benchmark, preserve all signed ports and compare the present Hasse detector only after an authenticated original-E3 bridge. No further portable coefficient guards should be counted as completion of native evidence.

External background only, not a native proof: Chisholm–Deines–Long–Nebe–Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/π* (2013), Section 4.1, https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf . The actual finite polynomial identity and derivative argument are included above.