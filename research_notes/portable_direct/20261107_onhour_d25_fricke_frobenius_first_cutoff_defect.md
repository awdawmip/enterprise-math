# D25 — Fricke 6:8 two-leg first finite-cutoff / Frobenius-order defect

Date: 2026-11-07. Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; distinct from maintenance. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen science pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Consumes exact analytic Fricke correspondence / first jet from \`research_notes/portable_direct/20261107_onhour_d25_exact_weighted_216_2304_period_jet.md\` on canonical main (prior proof as author-side, unreviewed). Status: **AUTHOR_SIDE_PROVED / EXACT_MODULAR_CHECKED / UNREVIEWED / NOT_ADMITTED**. External formal parameter t belongs to the auxiliary analytic uniformization, not an Enterprise-native two-dimensional plane.

## Precise theorem (all p>3)

Write
\[
 U(z)=\sum_{k\ge0}c_kz^k,\quad c_k=\binom{2k}{k}^2\binom{3k}{k}/108^k,\qquad
 B(w)=\sum_{k\ge0}d_kw^k,\quad d_k=\binom{2k}{k}^2\binom{4k}{2k}/256^k.
\]
Let \(U_{<p}, B_{<p}\) denote sums over \(0\le k<p\). Take the verified rational Fricke maps
\[
 z(t)=\frac{108t^2(t+9)(t+8)^2}{(t+12)^6},\quad
 w(t)=\frac{256t^3(t+8)(t+9)^3}{(t^2+36t+216)^4},\quad
 H(t)=\frac{3(t+12)^2}{2(t^2+36t+216)}.
\]
Their normalized analytic identity near \(t=0\) is \(U(z(t))=H(t)B(w(t))\). Put
\[
 P(t)=H(t)+6z(t)\frac{H'(t)}{z'(t)},\qquad
 Q(t)=6z(t)H(t)\frac{w'(t)}{z'(t)},
\]
interpreting removable singularities via their \(\mathbb Z[1/6][[t]]\) Taylor expansions. Let
\[
 D_p(t)=\sum_{k=0}^{p-1}(6k+1)c_k z(t)^k -
          P(t) B_{<p}(w(t))-Q(t) B'_{<p}(w(t)).
\]
Then \(D_p(t)\) has zero coefficients below degree \(2p\), and
\[
 [t^{2p}]D_p(t)= -\frac{(6p+1)c_p}{48^p}\in\mathbb Z_{(p)},\qquad
 \boxed{D_p(t)\equiv-\frac{t^{2p}}{432}\pmod{(p,t^{2p+2})}.}
\]
Thus its first nonzero coefficient modulo p is **exactly** \(-432^{-1}\in\mathbb F_p\), and the next coefficient is zero.

## Proof

The full analytic derivative identity gives
\[
 \sum_{k\ge0}(6k+1)c_k z(t)^k=P(t)B(w(t))+Q(t)B'(w(t)).
\]
Around t=0, \(\operatorname{ord}_t z=2\), \(z(t)=t^2/48+O(t^3)\), \(\operatorname{ord}_t w=3\), and \(H(0)=1\). Since \(z/z'=O(t)\), \(P=O(1)\), \(Q=O(t^3)\). Subtracting the two finite sums from the exact identity gives
\[
 D_p(t)=-\sum_{k\ge p}(6k+1)c_k z(t)^k+
             P(t)\sum_{k\ge p}d_kw(t)^k+
             Q(t)\sum_{k\ge p}k d_kw(t)^{k-1}.
\]
The first omitted U term starts at order \(2p\), the next one at \(2p+2\); both B-terms start no earlier than \(3p\). As \(p\ge5\), \(3p>2p+1\), so the displayed first-coefficient formula and the zero through order \(2p-1\) follow without any modular computation.

For \(p>3\), all denominator constants 48,108,216,256 are p-units. Lucas' theorem gives
\[
 \binom{2p}{p}\equiv 2,\quad\binom{3p}{p}\equiv3\pmod p,
\]
hence \(c_p\equiv 12/108=1/9\pmod p\). Also \(6p+1\equiv1\) and \(48^p\equiv48\pmod p\). Frobenius shows \(z(t)^p\equiv z(t^p)\pmod p\), so there is no term of degree \(2p+1\). This proves \(D_p(t)\equiv-t^{2p}/432\bmod(p,t^{2p+2})\). All series manipulations are t-adic formal identities; absolute analytic convergence near zero is another valid interpretation.

## Discriminating finite-fiber certificate (distinct observer)

The frozen finite sums use \(z=1/2,w=1/9\), i.e. \(t=6\sqrt2\), a t-adic unit in the relevant p-adic extension. The t-adic theorem specifies the *first Frobenius/cutoff source* but cannot be substituted termwise at that unit. Keeping the two source streams separate, independently evaluate
\[
 W_p=\sum_{k<p}(6k+1)\binom{2k}{k}^2\binom{3k}{k}/216^k,\quad
 V_p=\sum_{k<p}(8k+1)\binom{2k}{k}^2\binom{4k}{2k}/2304^k.
\]
Integer modular calculation gives:

| p | \(W_p\bmod p^5\) | \(V_p\bmod p^5\) | \((2V_p-W_p-p)/p^4\bmod p\) |
|---:|---:|---:|---:|
| 19 | 603611 | 1865667 | 5 |
| 373 | 2934720761840 | 3393369805886 | 199 |

Here \((-3/p)=1\). In particular both inputs satisfy the conjectured p^4 cancellation and both have a **nonzero p^4 residual**; \(p=19\) already excludes universal p^5 for this target class. This is a finite exact certificate, not a universal proof of p^4 cancellation.

## Consequence / next exact unit

The analytic period/jet map has a **rigorously nonzero mod-p first omitted coefficient** in the common t-coordinate: the needed finite-fiber cancellation must involve further boundary/Frobenius information rather than equality of two naive truncated pullbacks. A useful next test is a Dwork/Frobenius continuation at \(t=6\sqrt2\), with explicit unit-root normalization and signed 216/2304 p-adic tails, comparing the resulting p^4 correction to 5 (p19), 199 (p373). Native p373 H0/B0 divided-power, Frobenius, Hesse κ and independent reproduction in issue #1559 remain separate unexecuted conditions.

Source identity: original native request \`onhour11-20261106-1400-exact-research-lane-continuation\` remains UNKNOWN; current em_status and exact receipt attempts return \`BACKEND_IDENTITY_OR_VERSION_MISMATCH\`, \`operation_sent=false\`. No session/CLAIM/run/Result asserted; \`REGISTER_PENDING\` / \`SYNC_DEBT\`. This record is GitHub-author-side preservation, not canonical Source admission.
