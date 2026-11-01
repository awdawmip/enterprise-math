# D25: 216/2304 analytic-period candidate and p19 Galois truncation obstruction

Date 2026-11-01. Author-side research / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN. Not a native Result, Task dispatch, acceptance or independent review. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923; never the maintenance lane.

## 1. Real analytic candidate: independently certified interval, no equality theorem

Define two different complex-real Gauss periods:

\[
F_\alpha={}_2F_1(1/6,1/3;1;1/2),\quad
F_\beta={}_2F_1(1/8,3/8;1;1/9).
\]

A previously unrecorded relationship suggested by evaluation is

\[
4F_\alpha^2\stackrel{?}{=}3\sqrt2\,F_\beta^2. \tag{candidate only}
\]

This turn **did not prove the infinite-series equality**. It rigorously certified the distinct finite claim

\[
\boxed{\big|4F_\alpha^2-3\sqrt2 F_\beta^2\big|<10^{-115}.}
\]

The new standard-library exact-rational checker sums N=460 terms of each series, uses the bound \(0<R_N<t_N/(1-z)\) arising from \(t_{k+1}/t_k=z(k+a)(k+b)/(k+1)^2<z\) for \(a,b\in(0,1)\), and encloses \(\sqrt2\) between adjacent rational integers divided by \(10^{140}\) using integer isqrt. It certifies the final strict inequality by exact integer/Fraction comparisons. It does not infer exact zero from numerical agreement, and no transformation across the two signatures has been proven.

## 2. All-p19 theorem: naive truncated-period transport is impossible

Let p be **any prime p≡19 (mod 24)** and consider the unramified quadratic coefficient ring
\[
R_p=(\mathbb Z/p^3\mathbb Z)[\vartheta]/(\vartheta^2-2),\qquad
c=3\vartheta/4.
\]
Since p≡3 (mod 8), \((2/p)=-1\), so \(\vartheta\notin\mathbb F_p\), \(\vartheta^p=-\vartheta\) modulo p, and \(c^p=-c\), \(\operatorname{Norm}(c)=-9/8\) modulo p. These are ordinary algebraic finite-field facts, not native X6 operations.

Define the **original, unmodified** rational truncated Gauss factors in \(\mathbb Z_{(p)}\):
\[
M_{\alpha,p}=\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{2^k(k!)^2},\quad
M_{\beta,p}=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{9^k(k!)^2}.
\]

Consume precisely two already available predecessor inputs:
(1) Source CM0/UR for the original D25 target gives \(p\mid M_{\alpha,p}\), see the original D25 Source-return/Clausen port alignment noted in research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md.
(2) Published Guo–Zudilin 2304 supercongruence gives \(B_p\equiv p\pmod {p^3}\) for p19. Previously author-proved *original signed* Clausen identity and valuation bound give \(B_p=M_{\beta,p}H_{\beta,p}-T_{\beta,p}\) and \(T_{\beta,p}\equiv0\pmod {p^2}\) for p19; see research_notes/portable_direct/20261031_onhour_d25_two_sided_clausen_tail_asymmetry_gosper_nogo.md. Hence \(M_{\beta,p}H_{\beta,p}\equiv p\pmod {p^2}\), proving \(v_p(M_{\beta,p})\in\{0,1\}\) **without using a new CM selector or assuming beta has a specific first-digit valuation**.

**Theorem (conditional on these explicitly attributed predecessor results; all p19):**
\[
\boxed{M_{\alpha,p}^{\,2}\not\equiv
          c\,M_{\beta,p}^{\,2}\pmod {p^3R_p}.}\tag{NO-NAIVE-TRANSPORT}
\]
If \(v_p(M_\beta)=0\), the right side is a unit and the left side is zero modulo p. Otherwise \(v_p(M_\beta)=1\), and the putative identity after dividing by \(p^2\) and reducing modulo p would be
\[
(M_\alpha/p)^2=c(M_\beta/p)^2\quad\text{in }\mathbb F_{p^2}.
\]
The left side is in \(\mathbb F_p\), while the right side is not because \(c\notin\mathbb F_p\) and the second square is a nonzero element of \(\mathbb F_p\). Contradiction. This completes the proof. No assumption about a native H0/B0 rank or Frobenius is used.

The result rules out **only the exact naive operation of replacing each infinite real period by its original p-term truncated Gauss factor while retaining the same algebraic scalar c**. It does not disprove the real analytic candidate or any p-dependent, Frobenius-twisted, signed-boundary-aware relationship. Any such future comparison must explicitly declare its observer, quadratic coefficient ring, sigma/eta and original signed provenance. A norm-only quotient is not automatically lossless under further operations.

## 3. Independent exact finite evidence / sharp witness

The attached executable Python 3 standard-library program uses exact Fraction arithmetic and p-adic modular inverses, checking 46 primes \(p\le2500,\ p\equiv19\pmod{24}\). All pass the original alpha/beta numerator recurrences, p-divisibility, beta valuation 1, Legendre nonresiduosity, and impossible forced \(\sqrt2\bmod p\). At p=19 the independent readout is \(M_\alpha/p\equiv8\), \(M_\beta/p\equiv9\bmod19\). A naive p³ equality would force \(\vartheta\equiv12\bmod19\), but \(12^2\equiv11\ne2\bmod19\). A **separate fixed p=13** exact valuation witness is \(M_\alpha/p\equiv11\bmod13\), \(M_\beta\equiv0\bmod13^2\), so the squared p² quotients disagree (4 versus 0). No universal p13 conjecture is assumed.

BRC resolution COMPOSE_APPLIED: keep distinct alpha/beta coefficient ports, integer p-adic valuations, Frobenius action on quadratic extension, and the specified mod-p³ terminal readout. The elementary finite-field Frobenius and norm are external algebraic diagnostics and cannot be promoted to native Heartbeat X6/H0/B0 semilinear Frobenius.

## 4. Exact continuation and obligations

Original mother remains \(A_p\equiv p\pmod{p^3}\) for p≡13,19 mod24. Higher p⁴ affine relation and the p13 Jacobi dual-parameter-shift cancellation are open; previous 216 \(\Delta_p-R_p\) observer and signed six valuation ports are unchanged. Next exact theoretical action is a Frobenius-compatible period transport with *both* signed Clausen tails and true sigma/eta, or direct p13 Jacobi first-jet cancellation; **do not use the real candidate as a proven transformation**.

Native issue #1559 was read OPEN and unassigned on 2026-11-01. Fixed p=373 **same-original-class** H0/B0 divided-power [X]U mod139129, module rank, true semilinear Frobenius/eta, signed odd Green/Hesse, kappa and independent replication remain NOT_RUN / PENDING_OWNER. The native evaluator must be authenticated; these scalar certificates are not substitutes.

Gateway 0.6.11 reported research_authority_granted=false and executor_binding_configured=false. This client's own checkpoint read returned ACCESS_DENIED; original request research-onhour-20261031-0205-dispatch-r15 returned scoped CONTROL_REQUEST_NOT_FOUND. No new Source session/claim/open/run/checkpoint/Result/review, no replay, no maintenance impersonation. Old three staging sources stay independent. P000, ACTIVE worldview, frozen scientific pin, scheduler and notifications unchanged.
