# D25 — all-order reflected p-adic isometry and quadratic original-216 readout bridge

2026-11-03 (Asia/Hong_Kong). TASK_RESEARCH author-side; **ALGEBRAICALLY PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is portable evidence, not a native checkpoint or independent mathematical acceptance.

Frozen parent: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-hourly-enterprise-math-20260923` is distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`.

## Scope and inherited exact inputs

For any prime (p\ge 13) with (p\bmod24\in\{13,19\}), let
[
b_k=\frac{\binom{2k}k^2\binom{3k}k}{216^k}\ (0\le k<p),\quad
W_p(t)=\sum_{k<p}(6k+1)b_kt^k,
\quad C_p(t)=\sum_{k<p} b_kb_{p-1-k}t^{p-1}=C_p(1)t^{p-1}.
]
The ORIGINAL-216 reciprocal observer (C_p) differs from the frozen Clausen (Q_p). Previously proved author-side inputs (not recredited): (C_p(1)/p^2\equiv10\pmod p), (D_1=W'_p(1)\equiv12j^2\pmod p), (D_2=W''_p(1)\equiv8j^2\pmod p), where (j=(\theta\ell_r)(1/2)\not\equiv0\pmod p), (r=(p-1)/6). See `20261103_hourly20_d25_reflection_three_port_universal_measure.md` and `20261103_hourly20_d25_cm_quartic_jet_reflection_precision_repair.md`.

## Theorem A — all-precision isometry (proved)

For **all** distinct (t,u\in1+p\mathbf Z_p),
[
\boxed{v_p(C_p(t)-C_p(u))=v_p(t-u)+2,\qquad
v_p(W_p(t)-W_p(u))=v_p(t-u).}
]
Proof: the divided difference of (C_p) is (C_p(1)\sum_{i=0}^{p-2}t^{p-2-i}u^i); the sum is (p-1\equiv-1\pmod p), and (C_p(1)/p^2\equiv10\not\equiv0\pmod p). The divided difference of (W_p) reduces to (W'_p(1)=12j^2\not\equiv0\pmod p). Both are exact (p)-adic units after the indicated powers are removed. Consequently (C_p(t)\bmod p^{q+2}) recovers (t\bmod p^q) (with fixed (C_p(1)) and (q\ge2)); this precision is sharp, because changing (t) by (p^{q-1}) first alters (C_p) in degree (q+1).

## Theorem B — two explicit argument digits (proved)

Let (t=1+p\lambda+p^2\mu) with canonical integers (0\le\lambda,\mu<p). Form (s=C_p(t)/C_p(1)=t^{p-1}\bmod p^3) by dividing the actual observations modulo (p^5) by (p^2) and inverting the unit (C_p(1)/p^2). Let (A=(s-1)/p\bmod p^2) in ([0,p^2)). Then
[
\boxed{\lambda\equiv-A\pmod p,\quad
\mu\equiv\lambda+\lambda^2-(A+\lambda)/p\pmod p.}
]
Proof: (s=1-p\lambda+p^2(\lambda-\mu+\lambda^2)\pmod{p^3}). The last fraction is an integer.

## Theorem C — nonlinear BRC observer transfer (proved)

With (v=C_p(t)/C_p(1)-1\in p\mathbf Z_p), (\alpha=(p-1)^{-1}\in\mathbf Z_p), (D_1=W'_p(1)), (D_2=W''_p(1)), for (t\in1+p\mathbf Z_p):
[
\boxed{W_p(t)-W_p(1)\equiv
\alpha D_1v+
\frac{\alpha(\alpha-1)D_1+\alpha^2D_2}{2}v^2
\pmod{p^3}.}
]
This requires the reflected scalar through (p^5), (D_1\bmod p^2), and (D_2\bmod p). Proof: the unique (p)-adic root near one of (t^{p-1}=1+v) is (t=(1+v)^\alpha). Expand to order (v^2), then Taylor-expand the ORIGINAL weighted polynomial (W_p) about (1). Equivalently, for (t=1+p\lambda+p^2\mu), the right side equals (p\lambda D_1+p^2(\mu D_1+\lambda^2D_2/2)).

## Verified finite evidence and provenance

Ran the Python standard-library modular checker against the ORIGINAL 216 term recurrence for every one of 77 primes (13\le p\le2000), (p\bmod24\in\{13,19\}): five distinct two-digit lifts per prime, one same-first-digit comparison, inverse digits, source-unit and CM derivative conditions, both exact valuation assertions and the quadratic transfer all PASS. The checker computes all (b_k\bmod p^5), (C_p(1)), (W_p(t)), (D_1,D_2) directly. At (p=373), (j=294), (D_1\bmod p^2=84217), (D_2\bmod p=319), (C_p(1)/p^2\bmod p^3=50034230). For (t=1+2p+3p^2), (A=1117), recovered digits ((2,3)), and ((W_p(t)-W_p(1))/p\bmod p^2=37511). At p=13/p=19 the corresponding last values are 136/100. Program and selected witnesses are in the adjacent files; the complete 77-prime log was generated locally.

**BRC type:** source indices (k,p-1-k), exact coefficients and valuations, argument lift, reciprocal scalar and oriented derivatives; operation (1+p\mathbf Z_p), observed shift (q\mapsto q+2), signed original (W_p) displacement. This mathematical representation is auxiliary and does not claim native H0/B0 execution.

**Parent next unit:** fixed baseline (W_p(1)\equiv p\pmod{p^3}) remains OPEN, equivalent to (\Delta_p-R_p\equiv0\pmod p). Consume sibling `20261103_onhour_d25_original216_coupled_finite_hensel_ode.md` and construct a *fixed-argument* terminating WZ/contiguous identity controlling ((W_p(1)-p)/p^2\bmod p), including upper (H_2\ {}_4F_3) source and p13,p19,p373 signed tests. Avoid replay of argument-lift results as the baseline.

Old protected session provenance `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94`; original bridge Issues #6637/#6638 not replayed; protected staging retained. Control issue #1558 and native p373 experiment #1559 remain. Source Gateway 0.6.11 reported `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, active quota 5/5. No native session, CLAIM, OPEN, checkpoint, Result or review was created here; no scheduler changes.
