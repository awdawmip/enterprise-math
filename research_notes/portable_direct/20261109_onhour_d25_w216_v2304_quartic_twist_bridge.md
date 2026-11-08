# D25 — 216/2304 CM-point explicit quadratic-twist and 2-isogeny bridge

Date 2026-11-09. **AUTHOR_SIDE_EXACT_PROOF / FIVE_EXHAUSTIVE_FP2_CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.**
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923; not the maintenance lane.

## Original arithmetic bridge and genuine geometric models

The unmodified weighted sums under study are

\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
V_p=\sum_{n=0}^{p-1}(8n+1)\frac{\binom{4n}{2n}\binom{2n}{n}^2}{2304^n}.
\]

In K=Q(T), T²=2, set t=(2-T)/4 and v=(3-2T)/6. Direct arithmetic gives 4t(1-t)=1/2 and 4v(1-v)=1/9. Thus the underlying unweighted 3F2 functions are the Clausen squares of the corresponding 2F1(1/3,2/3;1;t) and 2F1(1/4,3/4;1;v) analytic germs. The two *weighted finite truncations* retain different derivatives, cutoffs and signed source observers: this fact is not a proof that W and V agree modulo p³.

Reuse the frozen original 216 cubic model E3: y²+xy+cy=x³, c=(2-T)/108=t/27. At the exact 2304 parameter v take the quartic-hypergeometric j-family model

\[
E_4(v):\quad z^2=u^3+u^2+b u,\qquad b=(1-v)/4=(3+2T)/24.
\]

**Theorem 1 (exact twist and new cross-family isogeny).** E4(v) is the quadratic twist by d=-3T of the Galois conjugate original E3^sigma (sigma(T)=-T). In particular

\[
j(E_4(v))=j(E_3^\sigma)=2417472-1707264T.
\]

Proof: For E3^sigma, c_sigma=(2+T)/108, its invariants are c4,3=1-24c_sigma, c6,3=-1+36c_sigma-216c_sigma², Delta3=c_sigma³(1-27c_sigma). For E4 the invariants are c4,4=16-48b, c6,4=-64+288b, Delta4=16b²v. Substitution using T²=2 yields exactly

\[
c_{4,4}=d^2 c_{4,3}=18c_{4,3},\quad
c_{6,4}=d^3 c_{6,3}=-54T c_{6,3},\quad
\Delta_4=d^6\Delta_3=5832\Delta_3.
\]

The equality of j is a consequence but not the whole proof. Explicitly convert E3^sigma to short Weierstrass coordinates X3=x_sigma+1/12, Y3=y_sigma+(x_sigma+c_sigma)/2 and E4 to X4=u+1/3, Y4=z. Their short coefficient pairs satisfy A4=d² A3 and B4=d³ B3. With s²=d, the map (X3,Y3)->(dX3,s³Y3) is an isomorphism over K(s); on invariant differentials it pulls back omega4 to s^{-1} omega3sigma. Compose with the previously proved (and **not repeated**) degree-two isogeny Phi:E3->E3sigma, Phi*omega3sigma=T omega3. This gives a degree-two isogeny E3->E4 over K(s) with differential scalar **T/s**. The nontrivial twist and its normalization are essential observer data.

**Theorem 2 (all-target-prime signed q-Frobenius relation).** For every prime p≡13 or19 (mod24), T^p=-T and p>3 gives good reduction. The quadratic character of d over F_(p²) obeys

\[
\chi_{p^2}(d)=\left(\frac{N_{p^2/p}(-3T)}p\right)
=\left(\frac{-18}p\right)=\left(\frac{-2}p\right)
=\begin{cases}-1,&p\equiv13\pmod{24};\\+1,&p\equiv19\pmod{24}.\end{cases}
\]

By the standard twist trace identity (proved via the quadratic character of the defining cubic),

\[
\boxed{a_{p^2}(E_4)=\left(\frac{-2}p\right)a_{p^2}(E_3^\sigma).}
\]

This is a geometric Frobenius trace comparison, not a redefinition of the frozen Delta-R or identification with a native divided-power H0/B0 matrix.

## Independent exact computation and p373 consequence

The companion standard-library Python verifier performs rational K-algebra checks and two independent character computations: norm-Legendre and exhaustive square-set membership, on every x in F_(p²) for each curve and p=13,19,37,43,373 (142877 field elements per curve). Exact results:

| p | chi(d) | #E3sigma | #E4 |
|--:|--:|--:|--:|
| 13 | -1 | 144 | 196 |
| 19 | +1 | 324 | 324 |
| 37 | -1 | 1296 | 1444 |
| 43 | +1 | 1764 | 1764 |
| 373 | -1 | 138384 | **139876** |

At p373, the independently established original E3 point-count certificate gives Fr_(373²)(E3sigma)=[+373]. The exact new twist gives Fr_(373²)(E4)=[-373] and #E4(F_(373²))=(373+1)²=139876. The correct geometric sign is opposite even though the earlier directly computed weighted W373 and V373 both equal 373 modulo 373³. A comparison of these *weighted truncated* series now requires the actual transported differential and finite-cutoff corrections, not equating raw Frobenius signs.

## Highest scientific frontier and authority

The new actionable route is to transport the weighted period derivatives and p-adic finite-cutoff second-digit through the explicit Phi plus quadratic-twist isomorphism, retaining T/s, chi(d), and separate (6n+1)/(8n+1) weights. This is a geometric explanation of a necessary sign normalization and a candidate route, **not** the all-prime W=V congruence, and not a completed Theta cancellation.

The native exact benchmark #1559 remains OPEN/PENDING_OWNER/NOT_EXECUTED: same original H0/B0 divided-power [X]U mod139129 at p373, actual rank, semilinear Frobenius direction/eta, signed odd Green/Hesse kappa, original Delta-R and independent reproducer. No authorized native owner was confirmed. Historical Researcher EM-ENTERPRISE-4DEB43 and Source session MCP-ecbfd1c046864bb3bff1a2e04c87d207 are provenance only; own recovery returned SESSION_CAPABILITY_REQUIRED, so no authenticated current CLAIM/run/Source checkpoint or Result is represented by this note. Source frozen pin unchanged.
