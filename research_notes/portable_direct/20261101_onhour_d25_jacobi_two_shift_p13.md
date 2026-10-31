# D25: two-shift Jacobi first-jet reduction for the p≡13 branch

2026-11-01. **AUTHOR-SIDE / EXACT FINITE CONGRUENCE PROVED / COMPUTED REGRESSION / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_RUN.**

Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. The frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` is unchanged. Logical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\` is separate from maintenance \`chatgpt-hourly-enterprise-math-20260921\`.

## New theorem, exact for every prime p>7 with p≡5 (mod 8)

Let
\[
a=(5p-1)/8,\quad b=(7p-3)/8,\quad 0<a<b<p,
\]
\[
G_p=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{9^k(k!)^2},\qquad
K_n(x)=\sum_{k=0}^n {n\choose k}{x\choose k}9^{-k},\qquad
J_p=K_a(b)=K_b(a).
\]
All sums and congruences are in \(\mathbb Z_{(p)}\); every denominator is a p-unit. The **proved exact two-shift congruence** is
\[
\boxed{8G_p\equiv20J_p-5K_b(a+p)-7K_a(b+p)\pmod{p^2}.}\tag{T}
\]
The two independently labeled first-lift coordinates
\[
\Delta_a=[K_b(a+p)-J_p]/p\bmod p,\quad
\Delta_b=[K_a(b+p)-J_p]/p\bmod p
\]
are well-defined, and (T) is equivalently \(G_p\equiv J_p-p(5\Delta_a+7\Delta_b)/8\bmod p^2\).

The exact Jacobi polynomial interface is
\[
\boxed{K_n(x)=(8/9)^nP_n^{(0,x-n)}(5/4).}\tag{J}
\]
Thus the two integer shifts give an exact finite-arithmetic representation of *two different Jacobi parameter derivatives*, not a scalar-only cancellation argument.

## Proof, including the previously essential dual-tail source

The parameters satisfy \(1/8=-a+5p/8\), \(3/8=-b+7p/8\); hence
\[
\frac{(1/8)_k(3/8)_k}{(k!)^2}
={a-5p/8\choose k}{b-7p/8\choose k}
\]
exactly. For \(k<p\) each generalized binomial coefficient is a polynomial in its upper parameter with p-integral coefficients. Taylor expansion modulo \(p^2\) at \((a,b)\) yields the base sum \(J_p\) plus the directional derivatives \(-5pK_b'(a)/8\) and \(-7pK_a'(b)/8\). For \(k>b\), both integer-base factors vanish, so the original product and both first derivatives vanish modulo \(p^2\). For \(a<k\le b\), only the **first** directional derivative survives: this is exactly the nonzero dual-tail port previously isolated by a reflected recurrence; it has not been discarded. Since \(\deg K_n=n<p\),
\[
K_b(a+p)-J_p\equiv pK_b'(a),\quad
K_a(b+p)-J_p\equiv pK_a'(b)\pmod{p^2}.
\]
Substitution proves (T) without any assumption about \(G_p\bmod p^2\).

To prove (J), apply the exact binomial expansion
\[
P_n^{(0,\gamma)}(t)=\sum_{k=0}^n {n\choose k}{n+\gamma\choose k}
((t-1)/2)^k((t+1)/2)^{n-k}
\]
at \(t=5/4\), where the two factors equal \(1/8\) and \(9/8\). Multiplying by \((8/9)^n\) gives \(K_n(n+\gamma)\) term by term. QED.

## Exact next target and sharpness counterexample

For \(p\equiv13\bmod24\), earlier **mod-p** CM selection gives \(J_p\equiv G_p\equiv0\bmod p\). Therefore the still-unproved stronger statement \(G_p\equiv0\bmod p^2\) is **equivalent** to the single finite integer-binomial shift congruence
\[
\boxed{20J_p-5K_b(a+p)-7K_a(b+p)\equiv0\pmod{p^2}.}\tag{C}
\]
This provides a Jacobi contiguous-relation/CM target with two protected first-jet ports. No full-prime proof of (C) is claimed.

| p | J mod p² | K_b(a+p) mod p² | K_a(b+p) mod p² | Δa mod p | Δb mod p | G mod p² | G mod p³ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 104 | 91 | 39 | 12 | 8 | 0 | 169 |
| 37 | 555 | 740 | 666 | 5 | 3 | 0 | 2738 |
| 373 | 27975 | 30586 | 77957 | 7 | 134 | 0 | 1669548 |

At \(p=13\): \(20(104)-5(91)-7(39)=1352=8\cdot13^2\), and original \(\beta\) gives \(G_{13}\equiv169\pmod{13^3}\). Therefore the **universal \(p^3\) strengthening is false**, by a concrete exact counterexample. At \(p=373\), the three-binomial combination is \(-373^2\) and \(G_{373}\equiv12\cdot373^2\pmod{373^3}\).

## Executed evidence and boundary

The standard-library script \`research_notes/portable_direct/d25_jacobi_shift_cert_20261101.py\` executed exact modular arithmetic for all **109** primes \(p\le3000,\ p\equiv5\bmod8\), including **53** in the target \(p\equiv13\bmod24\) class. All 109 verified (T) and its distinct integer shifts; 53/53 had \(G\bmod p^2=0\) numerically, and 53/53 had nonzero next \(p^3\) digit. At p=13,37,373, independent factorial/Pochhammer numerator implementations corroborated the original recurrence modulo p³. These finite tests are not a universal proof of (C).

Typed BRC use: preserve the two labeled parameter-shift ports, exact binomial integers, p-adic valuations, original beta index and terminal observer modulo p². The two shifts cannot be replaced by an unlabeled total if a subsequent operation needs their separate derivatives or the weighted \(H_p\). No claim about native X6, genuine H0/B0 Frobenius or the signed 216/2304 original cutoff follows. **Reuse classification:** COMPOSE_APPLIED to existing exact integer/rational, valuation and provenance-preserving port substrate. New result is the all-prime two-shift arithmetic interface and a decisive \(p^3\)-precision kill case; the earlier three-source theorem, p19 p³ beta tail and 216 high ports are reused rather than rerun.

## Continuation

Mother remains \(A_p\equiv p\bmod p^3\) for primes \(p\equiv13,19\bmod24\), with the stronger affine 216/2304 bridge conjectural. Next mathematical action: attack (C) via Jacobi contiguous/CM first-jet identity preserving both \(\Delta\) ports, or seek a counterexample; then reconnect to the original signed 216 source. Do not infer the native p373 benchmark from any scalar check. Original H0/B0 divided-power \([X]U\bmod139129\), actual semilinear Frobenius, module rank, signed odd Green/Hesse, \(\kappa\), \(\Delta\)-R and independent check remain PENDING_OWNER/NOT_RUN, tracked at Enterprise Math Issue #1559.

Current Gateway status 0.6.11: \`research_authority_granted=false\`, \`executor_binding_configured=false\`. Own checkpoint read gave ACCESS_DENIED; original request \`research-onhour-20261031-0205-dispatch-r15\` lookup gave CONTROL_REQUEST_NOT_FOUND in this client scope, not evidence of an accepted claim. No formal Source session/claim/run, research activity registration, freeze, review, acceptance or checkpoint is asserted. Remain REGISTER_PENDING/SYNC_DEBT for that channel. Three old staging artifacts retain independent provenance. P000, ACTIVE worldview, frozen science pin and scheduler/notification settings unchanged.
