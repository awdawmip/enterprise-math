# D25 — certified complex-period/weighted-jet bridge and a p-adic normalization witness

Date 2026-11-05. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: **AUTHOR-PROVED EXACT FINITE INEQUALITY / EXECUTED RATIONAL CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

## Original models and question

Let
[
u_k=\frac{(2k)!(3k)!}{216^k(k!)^5},\qquad v_k=\frac{(4k)!}{2304^k(k!)^4}.
]
Define convergent real series (A=\sum_{k\ge0}u_k), (B=\sum_{k\ge0}v_k), (P=\sum_{k\ge0}(6k+1)u_k), and (Q=\sum_{k\ge0}(8k+1)v_k). The original finite arithmetic target is (W_p\equiv V_p\pmod{p^3}), with truncation at (p-1). The purpose of this unit is to test an algebraic *complex-period* transformation of the exact same coefficient families, retaining original source labels, signed difference, weight/derivative operators, truncation and arithmetic domain in the BRC observer.

## Proposition: exact-rational certified numerical closeness

[
\boxed{|8A^2-9B^2|<10^{-145}},\qquad
\boxed{|2P-3Q|<10^{-145}}.
]

These are rigorously bounded inequalities, **not** proofs that the expressions vanish. They identify the testable candidate (A/B=3/(2\sqrt2)) and its weighted first-jet relation at the two frozen hypergeometric arguments (1/2,1/9).

**Proof.** For all (k\ge0), direct factorial cancellation gives
[
\frac{u_{k+1}}{u_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}<\frac12,quad
\frac{v_{k+1}}{v_k}=\frac{(2k+1)(4k+1)(4k+3)}{288(k+1)^3}<\frac19.
]
For (N=500), write the four partial sums through (N-1) as (A_N,B_N,P_N,Q_N) and let (u_N,v_N) be the exact next terms. Then
(0<A-A_N<2u_N), (0<B-B_N<9v_N/8). Because weighted consecutive-term ratios are bounded by
(r_A=(6N+7)/(2(6N+1))<1) and (r_B=(8N+9)/(9(8N+1))<1), the weighted tails obey
(0<P-P_N<(6N+1)u_N/(1-r_A)),
(0<Q-Q_N<(8N+1)v_N/(1-r_B)).
Therefore
[
|8A^2-9B^2|<
|8A_N^2-9B_N^2|
+8(4A_Nu_N+4u_N^2)
+9((9/4)B_Nv_N+(81/64)v_N^2),
]
[
|2P-3Q|<
|2P_N-3Q_N|
+\frac{2(6N+1)u_N}{1-r_A}
+\frac{3(8N+1)v_N}{1-r_B}.
]
An executed Python `fractions.Fraction` program computes every term and **compares each full rational right-hand side with (10^{-145}) by integer arithmetic**: both strict comparisons succeed. The complete runnable checker is `d25_period_jet_bridge_certificate_20261105.py`, preserved as a separate research artifact. No floating point is used in either inequality.

## Exact original mod-p diagnostic: different normalizations

Direct original-binomial computation at (p=13) yields (W_{13}\equiv V_{13}\equiv13\pmod{13^3}). Thus
[
\boxed{2W_{13}-3V_{13}\equiv-13\equiv156\pmod{13^2}.}
]
This is an exact counterexample to carrying the *complex weighted* scalar (3/2) directly into the *truncated p-adic* arithmetic observer. Any productive p-dependent transform must account for its own unit/Frobenius normalization and unequal cutoff boundary, rather than substituting the analytic scalar. The mother (W_p-V_p\equiv0\pmod{p^3}) remains the target.

## Frontier / provenance / next discriminating operation

The candidate complex modular relation is **unproved**; the two closeness inequalities and the (p=13) normalization witness are proved exact finite/integer statements. Next science: seek an algebraic modular pullback proving or falsifying (8A^2=9B^2), and derive its **p-parameterized** terminating counterpart, then evaluate its unit and endpoints against the existing signed half-endpoint identity (W_p-V_p=(W_h-V_h)+p^2 C_A\pmod{p^3}). This is a candidate search route, not an adopted certificate.

Mother objective: (\Delta_p-R_p=0\pmod p) for (p\equiv13,19\pmod{24}); uniform proof open. Frozen (p=373) same-original-class native divided-power H0/B0 `[X]U mod 139129`, module rank, semilinear direction, eta/kappa and odd Green observer remain to execute and independently validate under the existing support Issue #1559. No native H0/B0 computation is claimed here.

Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` is separate from maintenance `chatgpt-hourly-enterprise-math-20260921`. Prior exact Source read `onhour11-20261105-1505-d25-own-read`: SUCCEEDED, `execution_authorized=false`. This report grants no session/CLAIM/run or formal Result. New source continuation request `onhour11-20261105-1757-d25-own-continuation` was still QUEUED at author checkpoint; later runs must read this exact request, not resubmit.
