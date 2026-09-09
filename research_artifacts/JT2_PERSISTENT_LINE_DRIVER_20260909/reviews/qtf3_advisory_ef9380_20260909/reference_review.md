# QTF3 reflection-degree lemma: bounded non-author review

**PASS at paper-review scope, conditional on the two explicitly consumed Q2 inputs.** No defect was found in the new finite reflection-degree proof or its stated specialization. This is a new advisory review of EM-DVR-57CCCE's argument, not a formal QTF3 Result or Driver acceptance.

Reviewer: **EM-JT2-EF9380 / RESEARCHER / TASK_RESEARCH**; existing activity **RA-513D918CB570B356EA4C94D4** and the same locally assigned session key were reused. Before reading this new mathematical packet, the current full activity record was read at main c2464a2154263815b6d1658e84d15045bf9dbc55, and the current runtime activity gate returned activity_allowed=true, persistence_allowed=true. The prior checkpoint remains intact.

Reviewed [candidate](https://github.com/awdawmip/enterprise-math/blob/08ad2fe0fac52949207ddc3559ad70a1b95b577a/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/research/qtf3_reflection_degree_57ccce_20260909/qtf3_reflection_degree_candidate.md): commit **08ad2fe0fac52949207ddc3559ad70a1b95b577a**, SHA256 **b01d1edba35e7e508dd7ff47523c1ef4ee7b1a137d8b59d880b1e0f00733c189**. Its two companion files were also read; the observer packet's separate LIFT organization is outside this review's proof claims. The author manifest discloses authoring registration after the argument arose; this review neither backdates that registration nor repairs it retroactively.

This execution did not contribute to the new argument before receiving it. I previously reviewed the old Q2 input and am source-exposed to it and the line's control context. Neither that older report nor this reused identity establishes clean/blind independence or automatic acceptance of the new lemma.

## Checked argument

1. **Input separation and exact truncation.** In R=Z_(p), the p-1 truncated F,L have p-integral coefficients and degree at most p-1. The old Q2 section supplies both D=L-F(4u(1-u)) in p^2 R[u] and the exact vanishing of every coefficient below degree p. The latter is a finite-prefix equality over R; it does not follow merely from reduction modulo p^2. I checked the cited input wording against the old frozen source and consumed the already reviewed facts without replaying its proof.

2. **Integral quotient and degree.** Coefficientwise divisibility first permits E=D/p^2 in R[u]. The exact zero prefix then permits E=u^p r with r in R[u]. Since deg D<=2p-2, deg r<=p-2, including the zero-polynomial case. Neither quotient assumes the new p^3 conclusion.

3. **Exact reflection before reduction.** With rho(u)=1-u and phi(u)=4u(1-u), phi composed with rho equals phi exactly. Hence
   \[
   E-E\circ\rho=(L-L\circ\rho)/p^2,\qquad
   \deg(E-E\circ\rho)\le p-1.
   \]
   Its integrality follows from the left side. No exact reflection identity for L is assumed.

4. **High coefficients after reduction only.** In F_p[u], the legitimate Frobenius identity is (1-u)^p=1-u^p. Therefore
   \[
   \bar E-\bar E\circ\rho
   =u^p(\bar r+\bar r\circ\rho)-\bar r\circ\rho.
   \]
   The last term has degree at most p-2. For j=0,...,p-2, the coefficient of u^(p+j) is consequently exactly the coefficient of u^j in the reflection sum. The left side has degree at most p-1, so every such coefficient is zero. These are all coefficients of the reflection sum; thus \(\bar r+\bar r\circ\rho=0\). No modulo-p^2 Frobenius substitution occurs.

5. **Fixed point and scope.** At u=1/2, reduction commutes with evaluation and 2 is a unit. The last identity gives \(\bar r(1/2)=0\), so E(1/2) is in pR and D(1/2) is in p^3 R. Thus L_p(1/2)=F_p(1) modulo p^3. The abstract lemma holds for odd primes under its explicit hypotheses. The supplied hypergeometric specialization establishes those hypotheses for p>3, p=1 modulo 6; it does not establish them for every prime. This includes p=13,19 modulo 24 without using CM0, SIMPLE or the external weighted theorem.

6. **What follows and what does not.** The new algebra supplies the current QTF3 book's permitted finite-invariant alternative: the extracted p^2 u^p factor, zero reflection component, fixed-point normalization, exact p-1 truncated congruence, and justified broader prime class. No residual differential equation is needed or newly validated; the conditional nonzero-scalar alternative is not triggered on this proved scope. The conclusion is a fixed-point p^3 statement, not a p^3 polynomial identity for all u. The CM ports have quadratic address 1/2, whereas this fixed point has address 1. No weighted/address-preserving implication to old LIFT, and no Sun adjacent-value elimination or minimal obstruction, is supplied.

The retained finite prefix, degree, sign and exact involution implement the already declared T0/T6 paper-level information discipline. No native BRC API, new general tool, mathematical program, numerical test or 77-prime replay was run. The existing formal Task/CLAIM/Result/audit/integration boundaries remain unchanged. This bounded review ends after its new source checkpoint and immutable readback; it does not close either mother objective.

Researcher-ID: EM-JT2-EF9380 / TASK_RESEARCH

Global-Knowledge-Sync: main@f4a5ea6 / GLOBAL_KNOWLEDGE_V1

