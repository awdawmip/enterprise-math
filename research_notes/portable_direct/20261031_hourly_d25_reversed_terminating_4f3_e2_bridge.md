# D25/LIFT — reversed terminating hypergeometric certificate of the original signed E.2 middle strip

Date 2026-10-31 Asia/Hong_Kong. Research lane: chatgpt-research-hourly-enterprise-math-20260923; not CONTROL_PLANE_MAINTENANCE and not the onhour Research lane. Scope: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. No new native CLAIM, OPEN, Source checkpoint, Result or mathematical admission. Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen **scientific** Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged; P000 ACTIVE_LOCKED unchanged. External p-adic arithmetic, no native six-axis projection claimed.

## Exact source consumed and unfinished target

Consume, not recredit, the distinct onhour Research lane's all-prime middle-strip factorial transport in EM immutable commit 9aa17bb0c56a6f4cdd471a4ccaf99a5b7158df28, report research_notes/portable_direct/20261031_onhour_d25_inverse_moment_factorial_wz.md, together with its preceding 79a574c7bc6ce2ec8b2de65e99689e2d3d3254fc original-216/E.2 bridge. Those results were author-side and unreviewed. For every prime p=6l+1>=7, write m=2l, h=3l and let

\[
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3},\qquad
A_p=\sum_{n=0}^{p-1}(6n+1)a_n.
\]

The exact original signed second-valuation strip S2 = sum_{h<n<=2m}(6n+1)a_n, after p²-normalization and mod-p observation, equals the inverse moment

\[
\mathcal I_p=S_2/p^2
\equiv \frac1{12C_p}\sum_{j=1}^{l}(1-6m-6j)t_j\pmod p,
\quad C_p=(3l)!(4l)!(2l)!,
\]
\[
t_j=\frac{2^{2l+j}((2l+j-1)!)^3(l-j)!(2l-j)!}{(j-1)!}.
\tag{input}
\]

All denominators are p-units. The consumed exact rational recurrence is t_(j+1)/t_j=2(2l+j)^3/[j(l-j)(2l-j)], 1<=j<l. The original frozen target remains A_p≡p (mod p³) for all p≡13,19 (mod24), and is NOT established by this report.

## New theorem: a terminating bounded 4F3-type polynomial and signed differential readout

Define the explicit **finite polynomial**, never an unqualified infinite hypergeometric series:

\[
H_l(z)=\sum_{s=0}^{l-1}d_s z^s,\qquad
d_s=\frac{(1)_s(1-l)_s(1+l)_s}{(1-3l)_s^3}.
\tag{1}
\]

This is the finite terminating 4F3-type polynomial with top (1,1,1-l,1+l) and bottom (1-3l,1-3l,1-3l). Since the lower parameters are nonpositive integers, the **explicit degree bound and sum** are the definition; do not extend to an analytic infinite series. All lower factors are nonzero in the declared 0<=s<l support, and all are p-units.

Let θ=z d/dz and

\[
K_l=\frac{2^{3l}((3l-1)!)^2}{36(4l)!(2l)!}\in\mathbb F_p^\times.
\]

Then for every p=6l+1>=7,

\[
\boxed{\mathcal I_p\equiv K_l[(4+6\theta)H_l(z)]_{z=1/2}\pmod p.}
\tag{2}
\]

**Proof.** Exactly t_l=l 2^{3l}((3l-1)!)³. Reverse index s=l-j. The source recurrence gives

\[
\frac{t_{l-s-1}}{t_{l-s}}
=\frac{(s+1)(s+1-l)(s+1+l)}{2(s+1-3l)^3}.
\]

With initial ratio t_l/t_l=1, induction proves

\[
t_{l-s}/t_l=2^{-s}(1)_s(1-l)_s(1+l)_s/(1-3l)_s^3=2^{-s}d_s
\]
for 0<=s<l, without crossing any zero denominator. The signed weight is exactly 1-6m-6j=1-18l+6s=4-3p+6s ≡4+6s (mod p). Finally

\[
t_l/(12C_p)=2^{3l}((3l-1)!)^2/[36(4l)!(2l)!]=K_l.
\]

Substituting proves (2), retaining the original sign and weight. These are exact finite algebraic transformations followed by a justified mod-p observation, not finite-sample inference.

## New fourth-order holonomic certificate with a degree guard

The polynomial (1) obeys the **exact rational polynomial differential equation**

\[
\boxed{[\theta(\theta-3l)^3-z(\theta+1)^2(\theta+1-l)(\theta+1+l)]H_l(z)=0.}
\tag{3}
\]

Indeed, d_s/d_(s-1)=s(s-l)(s+l)/(s-3l)^3 for 1<=s<l; the coefficient at s=l vanishes by the numerator termination and d_l=0, and all higher coefficients vanish by the declared polynomial. The degree guard is essential: the differential operator alone may have additional resonant solutions at higher degrees. Formula (3) is a finite holonomic interface and a possible contiguous/WZ input, **not** a closed special-value evaluation of H_l(1/2).

## Independently executed exact checker

Executed accompanying Python standard-library program research_notes/portable_direct/d25_reversed_terminating_4f3_exact_20261031.py, with original 216 recurrence computed modulo p², extracting independently each once-divisible a_k/p in m<k<=h and forming the signed inverse moment. Independently computed factorial t_j from source and independently evaluated reversed H_l polynomial with modular coefficient recurrence at z=1/2; also checked its differential equation termwise and each reversal coefficient.

For **all 330** primes 7<=p<=5000, p≡1 (mod6), including **166** frozen p≡13 or 19 (mod24), the three paths agreed. Exactly **128715** reversed terms checked. Source-matched anchors p7=5, p13=10, p19=9, p37=20, p67=58, p157=98, p373=266; p1327=1070. Actual stdout:

PRIMES 330 D25_TARGETS 166 REVERSED_TERMS 128715
ANCHORS 7:5,13:10,19:9,37:20,67:58,157:98,373:266,1327:1070
PASS_D25_TERMINATING_REVERSED_4F3_SIGNED_E2_STRIP_EXACT

All arithmetic is finite integer modular arithmetic without floating point. Finite tests support implementation; equations (2),(3) are supported by the algebraic proof. No native H0/B0, [X]U mod p², Frobenius/eta, Lean formal checker or independent review was performed.

## BRC readout and honest continuation

BRC COMPOSE_APPLIED to the exact external p-local carrier: keep prime p, original 216 source, original summation index n, reflected index k=p-n, factorial j, reversed s=l-j, valuation, division by p², original weight 6n+1, z=1/2 evaluation and requested mod-p readout. Allowed operations are verified coefficient reversal, denominator-unit inversion, finite hypergeometric polynomial formation and signed differentiated evaluation. This representation is sufficient for the **single declared scalar strip**, not necessarily higher p-adic digits, other observers or native X6.

The E.2 bridge remains OPEN with separate unproved conditions D0+D1≡0 (mod p²) and, after that condition, (D0+D1)/p² + K_l[(4+6θ)H_l]_(z=1/2) ≡0 (mod p). These are NOT established. Next distinct research action: derive a **joint signed finite creative-telescoping/contiguous** identity linking the exact low/middle original-source difference D0+D1 to the bounded polynomial's weighted fixed-z special value. Preserve both conditions, avoid changing original X=1, do not repeat one-term Gosper obstruction. Do not claim a globally strict complexity reduction or settled LIFT.

Gateway 0.6.11 read during the turn: research_authority_granted=false, executor_binding_configured=false, native active 5/5; current connected client has no callable recovery_status and checkpoint_list returned ACCESS_DENIED. Existing EM #1558 control recovery and #1559 original-class native 373 benchmark remain the support routes. No service session, claim, run, transfer, native checkpoint or protected staging was modified; no maintenance identity used. This is a GitHub author-side portable research artifact, not native Source completed_units or formal math acceptance.
