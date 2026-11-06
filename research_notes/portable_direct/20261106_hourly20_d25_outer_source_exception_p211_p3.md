# D25 — exceptional outer-source fiber at p=211 and a bounded p³ original-216 check

Date: 2026-11-06. Status: **AUTHOR-DERIVED / FINITE EXACT CERTIFICATES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; scientific input pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Ordinary Research lane: `chatgpt-research-hourly-enterprise-math-20260923`. This note reuses, but does not reattribute, the existing first/second source-jet Taylor formulas from `20261106_hourly20_d25_source_tangent_first_digit_fibers.md` and `20261106_hourly20_d25_source_fiber_second_digit_obstruction.md`.

## Exact finite finding: two individually invisible source directions at p=211

Write `p=6m+1`, `(a,b,c)=(2m,3m,4m)`, `w_j=6j+1`, and
[
 U_j(x_1,x_2,x_3)=(-1/2)^j\binom{a+x_1}{j}\binom{b+x_2}{j}\binom{c+x_3}{j},\quad
 \mathcal W_p(v)=\sum_{j=0}^{p-1}w_j U_j(pv).
]
Define `A_i=Σ w_j ∂_i U_j(0) (mod p²)`, `T_i=A_i mod p`, and `H_{ik}=Σ w_j ∂_i∂_kU_j(0) (mod p)`. All denominators through `j<p` are p-units. The established Taylor theorem is
[
 \mathcal W_p(v+\delta)-\mathcal W_p(v)\equiv
 p A\cdot\delta+p^2(v^T H\delta+\tfrac12\delta^T H\delta)\pmod{p^3}.
]
For `p=211`, `m=35`, `(a,b,c)=(70,105,140)`, **complete exact modular arithmetic** gives
[
 T=(0,151,0)\pmod{211},
 \qquad A=(28696,10279,42622)\pmod{44521},
]
[
 H\equiv\begin{pmatrix}22&170&29\\170&4&71\\29&71&182\end{pmatrix}\pmod{211}.
]
Since `151≠0`, the first-digit weighted scalar map has rank one and its kernel is **exactly** the source-plane `span(e_1,e_3)`. Thus, unlike p=13,19,373 where a correlated direction was exhibited, at p=211 **both outer directions are separately invisible at the first digit**. This is a finite exact example, not a claim of a uniform all-prime classification.

At the original 216 source tangent `v*=(-1/3,-1/2,-2/3)`, direct integer modular evaluation (independent of the jet formula) yields
[
 \mathcal W_{211}(v_*)\equiv211\pmod{211^3},\qquad211^2=44521,qquad211^3=9393931,
]
[
 \mathcal W_{211}(v_*+e_1)-\mathcal W_{211}(v_*)\equiv7835696
 =176\cdot44521\pmod{9393931},
]
[
 \mathcal W_{211}(v_*+e_3)-\mathcal W_{211}(v_*)\equiv934941
 =21\cdot44521\pmod{9393931}.
]
These are two distinct nonzero second-digit repair coordinates. The Hessian calculation independently gives `Q(e1)=136+29+11=176` and `Q(e3)=202+150+91≡21 (mod211)`; the three summands respectively represent `(A·δ)/p`, `v*^T Hδ`, and `δ^THδ/2`. The two independently computed paths agree exactly.

**BRC observer scope.** Population: three labelled source factors, index `0≤j<p` and signed weights `w_j(-1/2)^j`. Observer: complete weighted scalar modulo p² or p³, not the complete vector of labelled coefficient jets. Operation: `v→v+δ`. The scalar first digit erases `e1,e3` at p211; the next scalar digit separates the two displayed changes. Preserve the labels and lifted gradient/Hessian to support subsequent operations. This does not constitute a counterexample to the frozen native LIFT `Δ_p−R_p` target.

## Independent bounded scan: outer cancellation and stronger original-216 remainder

Two locally compiled C++17 modular-arithmetic programs were executed with the exact domain **all 2,556 primes** `p≤50,000` and `p≡1(mod6)`; there were **zero exceptions** in each scan:

* `T_1+T_3=0 (mod p)`. The derivative recurrence uses `B_{j+1}=(s-j)B_j/(j+1)`, `D_{j+1}=((s-j)D_j+B_j)/(j+1)` over `F_p`, including zero binomial positions, and the exact weighted three-source product for `0≤j≤3m`. Exactly two tested primes have `T_1=0` (7 and 211). In all 2,556 tested primes `T_2≠0`. These are finite-domain facts, not general theorems about primes beyond 50,000.
* Independently, the **original undeformed 216** sum `W_p=Σ_{j=0}^{p-1}(6j+1)(1/2)_j(1/3)_j(2/3)_j/[2^j(j!)^3]` satisfies `W_p≡p (mod p³)` for all 2,556 tested primes. Its rational term recurrence is `h_0=1` and
  `h_{j+1}=h_j(2j+1)(3j+1)(3j+2)/(36(j+1)^3)`;
  modular division is taken only by units for `j+1<p`. Computation uses exact `__int128` modular multiplication for `p³≤50000³`, with p-unit inverse lifting, without floating point.
* A separate independent Python exact arithmetic calculation at `p=7,13,19,211,373` checked the jet gradient, Hessian and direct full sum modulo `p³`; the p211 certificate above is fully reproduced.

No literature priority or universal proof is asserted for either broad congruence; in particular `T_1+T_3=0` remains **open as an all-prime statement**. The original 216 mod-p³ congruence should be checked against existing WZ/supercongruence literature before a novelty claim.

## Reproduction and continuation

The bounded checks were actually executed locally; source files are retained as portable run artifacts `d25_tangent_scan_20261106.cpp` and `d25_original_216_p3_scan_20261106.cpp`. Their stdout respectively reports `count=2556 exceptions=0 zero_T1=2 zero_T2=0` and `primes_checked=2556 exceptions=0`. The general Taylor formula is algebraic; the p211 numbers and bounded scans are exact computational certificates, not an independently reviewed theorem.

**Next discriminating unit:** derive a symbolic or WZ certificate for `T_1+T_3≡0` for all primes `p=6m+1`, or find an exact prime counterexample; if the identity holds, classify when `T_1=T_3=0` using the same observer and retain the lifted second-digit repair. In parallel, exploit the independently checked `W_p≡p mod p³` as a *scoped computational input* for the compensated `Θ_p` identity and pursue a full proof or properly sourced prior-art adoption. The frozen mother goal remains `Δ_p−R_p≡0 mod p` for `p≡13,19 mod24`; authentic p373 H0/B0, `[X]U mod p²`, Frobenius normalization, `η,κ` and independent review remain open.

**Control/frontier:** last returned D25 handoff was `HANDOFF_READY/NO_LIVE_CLAIM` with `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED` prior checkpoint, but no authenticated successor execution. Preserve pending read request IDs `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13`: both were reconciled to QUEUED after EVENT_COLLECTION_IO (as observed this turn), not SUCCEEDED. No new claim, OPEN, release, freeze, native checkpoint or mathematical acceptance was performed. Old session/staging and prior_contribution_ids must be recovered from real Source, not this author-side note. Project control support tracker: Enterprise Math #1558.
