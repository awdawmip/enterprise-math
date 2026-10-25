# D25/LIFT — Clausen-compatible Hasse cutoff ports and all-middle denominator drift

Date: 2026-10-25. Author: TASK_RESEARCH portable derivation (Research logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` is unchanged.

**Scope and admission:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. External finite hypergeometric algebra, not a CM experiment, an all-target-prime supercongruence, or a theorem transferred to native X6. No current Source CLAIM, authorized run, new native checkpoint, or independent reviewer is asserted.

## Question and genuinely new result

The previously established fixed-denominator cutoff Hasse forcing has mod-\(p\) support at orders \(2,p+1,2p\). The independently established Clausen-compatible parameterization introduces the denominator \(c(x)=1/2-3x\). Does that change the boundary ports, and how do its invisible intermediate Hasse orders leak at the next \(p\)-adic digit?

Let \(p=6m+1\ge7\) be prime, \(N=p-1\), and work in \(\mathbb Z_{(p)}[[t]]\) with \(x=m+t\). Define

\[
\widetilde\Phi_p(x,z)=\sum_{r=0}^{N}\frac{(-x)_r(-2x)_r}{(c(x))_r\,r!}z^r,\quad
c(x)=\tfrac12-3x,\quad\theta=z\frac{d}{dz}.
\]

Every denominator in this finite sum is a \(p\)-unit at \(x=m+t\). Its exact cutoff equation is

\[
\boxed{\left[\theta(\theta+c(x)-1)-z(\theta-x)(\theta-2x)\right]\widetilde\Phi_p(x,z)
=-\widetilde F_p(x)z^p,}
\tag{1}
\]

where

\[
\widetilde F_p(x)=\frac{(-x)_p(-2x)_p}{(c(x))_{p-1}(p-1)!},
\qquad \widetilde J_{k,p}=-[t^k]\widetilde F_p(m+t).
\]

Equation (1) is coefficientwise exact as a rational identity. It follows directly from the \( {}_2F_1\) coefficient recurrence, including the single retained \(z^p\) truncation term.

### Theorem A — corrected characteristic-\(p\) boundary support

As an equality in the formal power-series ring \(\mathbb F_p[[t]]\),

\[
\boxed{\sum_{k\ge0}\widetilde J_{k,p}t^k
\equiv -2t^2(1-t^{p-1})\pmod p.}
\tag{2}
\]

Thus only **two** corrected Hasse ports survive: \(\widetilde J_{2,p}\equiv-2\) and \(\widetilde J_{p+1,p}\equiv2\) modulo \(p\). In particular the former high cutoff port of order \(2p\) vanishes modulo \(p\) after the Clausen denominator is included. This is not the earlier three-port formula repeated: it changes the actual parameterized operator and its signed forcing.

**Proof.** Write

\[
F_p(x)=\frac{(-x)_p(-2x)_p}{(N!)^2},\qquad
D_p(x)=\frac{N!}{(c(x))_N},\quad \widetilde F_p=F_pD_p.
\]

Frobenius and \(m=(p-1)/6\) give
\(F_p(m+t)\equiv 2(t^p-t)^2=2t^2(1-t^{p-1})^2\bmod p\).
Further,

\[
D_p(m+t)=\prod_{j=1}^{p-1}\frac{j}{j-p/2-3t}
\equiv\prod_{j\in\mathbb F_p^\times}(1-3t/j)^{-1}
=(1-(3t)^{p-1})^{-1}=(1-t^{p-1})^{-1}.
\]

The last equality uses Fermat, and all inverses are valid in \(\mathbb F_p[[t]]\). Multiplying cancels exactly one factor \(1-t^{p-1}\), proving (2). \(\square\)

### Theorem B — every corrected intermediate Hasse port modulo \(p^2\)

Let \(H_a^{(s)}=\sum_{j=1}^{a}j^{-s}\in\mathbb Z_{(p)}\). For every integer \(1\le n\le p-2\),

\[
\boxed{
\widetilde J_{n+2,p}\equiv
\frac{2(1+2^n-3^n)}{n}H_{p-1}^{(n)}
-2(-1)^np\big(H_m^{(n+1)}+2^nH_{2m}^{(n+1)}\big)
-3^npH_{p-1}^{(n+1)}
\pmod{p^2}.}
\tag{3}
\]

This is a genuinely Clausen-compatible denominator correction to the preexisting all-middle fixed-denominator identity. Every RHS has valuation at least one. For \(n=p-2\), the final term **must be retained**:

\[
-3^{p-2}p H_{p-1}^{(p-1)}\equiv p/3\pmod{p^2}.
\tag{4}
\]

For \(1\le n\le p-3\) it vanishes modulo \(p^2\).

**Proof.** Put \(D_p(m+t)=\sum_{j\ge0}D_jt^j\).
Since \(D_0\equiv1\bmod p^2\), and
\[
\log\frac{D_p(m+t)}{D_0}
=\sum_{j\ge1}\frac{3^jS_j}{j}t^j,\quad
S_j=\sum_{h=1}^{p-1}(h-p/2)^{-j},
\]
we have, for \(1\le j\le p-2\),

\[
S_j\equiv H_{p-1}^{(j)}+\frac{jp}{2}H_{p-1}^{(j+1)}
\pmod{p^2},\qquad S_j\equiv0\pmod p.
\]

All degrees \(j\) considered are \(p\)-units. Products of distinct positive-degree logarithm terms are multiples of \(p^2\); hence coefficientwise

\[
\boxed{D_j\equiv
\frac{3^j}{j}H_{p-1}^{(j)}
+\frac{3^jp}{2}H_{p-1}^{(j+1)}
\pmod{p^2}.}
\tag{5}
\]

Let \(J_{k,p}=-[t^k]F_p(m+t)\) be the old fixed-denominator ports. Its characteristic-\(p\) support, from the preceding source, gives \(J_{2,p}\equiv-2\bmod p\) and \(J_{3,p},\ldots,J_{p,p}\equiv0\bmod p\). Also \(D_1,\ldots,D_{p-2}\equiv0\bmod p\). Multiplying \(F_pD_p\), for \(1\le n\le p-2\) all cross terms involving two intermediate ports vanish modulo \(p^2\), leaving

\[
\widetilde J_{n+2,p}\equiv J_{n+2,p}-2D_n\pmod{p^2}.
\tag{6}
\]

The previously proved normalized-product/Newton formula (linked below) states
\[
J_{n+2,p}\equiv2\left[
\frac{1+2^n}{n}H_{p-1}^{(n)}
-(-1)^np(H_m^{(n+1)}+2^nH_{2m}^{(n+1)})\right]\pmod{p^2}.
\]
Combining this with (5) and (6) proves (3). Finally \(\sum_{h=1}^{p-1}h^{-(p-1)}\equiv-1\bmod p\) and \(3^{p-2}\equiv3^{-1}\bmod p\), yielding (4). \(\square\)

### Corollary — fourth corrected jet and a measurable lost port

With the same notation, \(n=2\) in (3) gives

\[
\boxed{\widetilde J_{4,p}\equiv
-4H_{p-1}^{(2)}-2p(H_m^{(3)}+4H_{2m}^{(3)})\pmod{p^2}.}
\tag{7}
\]

In particular

\[
\boxed{\widetilde J_{4,p}-J_{4,p}\equiv-9H_{p-1}^{(2)}\pmod{p^2}.}
\tag{8}
\]

At \(p=7\), the old and corrected values are \(J_4=42,\widetilde J_4=14\bmod49\); at \(p=13\), \(J_4=0,\widetilde J_4=117\bmod169\). Therefore a zero fourth-port under the fixed-denominator observation does **not** justify discarding the Clausen denominator as a safe compression.

## Independent arithmetic routes and reproducibility

The adjacent \`20261025_hourly_d25_clausen_corrected_hasse_bridge_check.py\` reconstructs the signed cutoff numerators from their exact integer linear factors, computes the denominator-drift unit-product coefficients by modular series inversion, and independently evaluates the harmonic right-hand sides in \(\mathbb Z/p^2\mathbb Z\).

Author run: **310** full-range prime/order checks, for \(p=7,13,19,31,37,43,73,103\) and every \(1\le n\le p-2\), passed; complete finite-field support over degrees \(0,\ldots,2p\) checked for \(p=7,13,19,31,37,43\), **6** cases passed. These calculations are exact finite-ring author checks, not independent review or a substitute for the general derivation.

## Source, BRC semantics, and continuation

Consumed immutable prior source notes, without re-crediting their theorems:

- \`research_notes/portable_direct/20261025_hourly_d25_all_middle_hasse_p2_forcing.md\` at commit \`f271911b9eab9b101c6a48dbb195925589d75f03\`.
- \`research_notes/portable_direct/20261025_hourly_d25_clausen_denominator_drift_source_port.md\` at commit \`5897ddc49f22fe2480961cd0fb5c5fdd47ff54de\`.

BRC observer: keep **which** parameter family and denominator were used, signed cutoff, Hasse order, \(p\)-adic valuation, \(z^p\) operator forcing, and all permitted downstream differentiations. A two-port mod-\(p\) observation does not license deletion of mod-\(p^2\) middle leakage, and a fixed-denominator proof is not automatically a Clausen-family proof. No native X6 state/readout bridge is asserted.

Parent target D25/LIFT/JT2 remains OPEN, hard global congruence unproved. Next minimum mathematical action: insert the corrected *operator* jets (including the derivatives of \(c(x)\) in the operator, not solely its coefficient boundary term) and the separately signed Clausen reflected convolution tail into one rankwise exact certificate; investigate whether the \(2\)-port forcing cancels with the tail at \(z=1/2\). Authentic same-original-class CM \(H_0/B_0\), \([X]U\bmod p^2\), Frobenius direction/normalization and \(\kappa\) mapping remain absent; native CM experiment NOT_RUN.

Control as read this round: \`em_control_continuation\` returned \`INVALID_ARGUMENT / CONTROL_QUOTA\`; no fresh winning CLAIM, OPEN or Source checkpoint has been verified. Existing predecessor mismatch and support Issue #1558 remain unresolved until actual maintenance-side repair and Research-side Source verification. Preserve the old native immutable frontier and contribution history; nothing in this portable note revises them.
