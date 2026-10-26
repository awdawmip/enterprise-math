# D25/LIFT — supersingular raw-Frobenius slope gate and p-adic precision audit

2026-10-26 · TASK_RESEARCH · logical conversation `chatgpt-research-onhour-enterprise-math-20260923` (NOT maintenance). Frozen science source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`.

**Status: AUTHOR-DERIVED CONDITIONAL NEGATIVE TYPE CERTIFICATE / NOT_NATIVE_BENCHMARK / NOT_RUN / UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINT.** This note changes the *interpretation gate* for the already pending native experiment, not the target or its owner. It does not repeat the Clausen, UR, Jacobi, Hilbert-90 or p=733 Ward work.

## 1. Exact source values retained

The accepted CM0/Deuring parent identifies the relevant Hesse CM discriminant -24 supersingular branch at primes p≡13,19 mod24. For p=373, the existing *ordinary Hesse* (not native) author calculation gives

\[
R_2=(\mathbb Z/139129\mathbb Z)[T]/(T^2-2),\quad
\sigma(T)=-T,\quad
\alpha=92060+21788T\pmod {139129},
\]
\[
N(\alpha)=92060^2-2(21788)^2=122102\pmod{139129},\qquad
N(\alpha)\equiv131\ne0\pmod{373}.
\]

This reuses the previously persisted candidate, not a newly inferred native Frobenius coefficient. Direct recurrence verification of the source ordinary Hesse polynomial `A_373((2-T)/4)` modulo 373³=51895117 gave `(34338380,8126924)`, divisible componentwise by 373, with quotient `(92060,21788)` modulo 373². **No native H0/B0 computation was performed.**

## 2. Conditional no-go: a unit-norm semilinear candidate cannot be raw supersingular H¹ Frobenius

**Proposition.** Let E be a supersingular elliptic curve over a finite extension of characteristic p; work over an unramified quadratic Witt coefficient ring, and let \(\varphi\) denote *unnormalized weight-one crystalline Frobenius* on \(H^1_{\rm cris}(E)\). No nonzero Frobenius-stable rational subobject or integral lattice segment of this isocrystal can be identified with a free rank-one semilinear module \(F_\beta(x)=\beta\sigma(x)\), \(\beta\in R_r^\times\), via a Frobenius-intertwining isomorphism preserving the unnormalized operator. In particular it cannot have \(F_\beta^2=N(\beta)\operatorname{id}\) with N(β) a p-adic unit.

**Proof.** The standard supersingular elliptic Dieudonné–Manin theorem says all Newton slopes of unnormalized \(H^1_{\rm cris}\) are exactly \(1/2\); equivalently its second Frobenius iterate has only slope-one eigenvalues. By direct composition, for a rank-one \(\sigma\)-semilinear coefficient \(\beta\), \(F_\beta^2(x)=\beta\sigma(\beta)x=N(\beta)x\). When β is a unit, N(β) is a unit, and the associated semilinear isocrystal has slope zero. A Frobenius-equivariant isomorphism preserves Newton slopes, and a Frobenius-stable subisocrystal of a slope-1/2 isocrystal cannot have slope zero. Contradiction. The argument remains valid after an unramified scalar extension or unit-valued basis change. QED.

**p=373 consequence.** For every candidate unit basis/normalization η∈R₂×,

\[
N(\eta\alpha)=N(\eta)\,122102\in R_2^\times.
\]

Thus the previously proposed conditional comparison \(F^2=N(\eta)\,122102\) **cannot be an identity for raw weight-one supersingular crystalline Frobenius**, irrespective of its unit-valued gauge η. Such a comparison is permitted only after the native source actually proves that its operator is a *different/normalized operator*, with a precise map, valuation shift and gauge convention; or when H0/B0 is not the raw weight-one isocrystal in the first place. This is a **type/normalization no-go**, NOT a contradiction of the original LIFT conjecture, and NOT evidence that the currently unspecified native H0/B0 module has any particular rank.

## 3. New precision gate if the comparison is with a normalized second iterate

If a native realization establishes that \(\varphi^2/p\) is integral on its chosen lattice and the intended observable is

\[
C=\varphi^2/p\pmod{p^2},
\]

then knowing the **raw** \(\varphi^2\) only modulo \(p^2\) does **not** determine C modulo p². Elementary exact arithmetic proves

\[
\varphi^2=pC,\quad
C\bmod p^2 \text{ requires }\varphi^2\bmod p^3.
\]

Indeed replacing \(C\) by \(C+pD\) leaves raw \(pC\) unchanged mod p², while altering C modulo p² whenever D is not zero mod p. For p=373: raw precision 139129 recovers only \(C\bmod373\); two normalized digits require raw precision 51895117. A direct normalized implementation can avoid this extra raw digit if it computes C itself with a proved precision contract.

This is **not** a request to change the frozen benchmark's original `[X]U mod p²`; rather the executor must *state the actual operator and normalizing map*, and either establish that the requested native [X]U already represents C at two-digit precision, or separately provide the higher-precision raw data needed to make the proposed comparison meaningful.

## 4. Highest-frontier operational consequence

Retain the original native **same-original-class fixed H0/B0 divided-power** object, [X]U mod p², H0/B0 rank, semilinear direction, η, signed odd Hesse/Green port, original κ, and frozen Δ_p−R_p. Before comparing the ordinary α norm with any native output, record:

1. Is the measured F the raw crystalline weight-one operator, a divided/normalized Frobenius, or an operator on an entirely different typed module? Give the exact source and its F-stable domain.
2. What are the native Newton-slope/determinant valuations, coefficient ring, rank, φ-semilinearity and normalization map? A raw supersingular F cannot pass a unit-norm square test: classify this outcome as `NORMALIZATION_TYPE_MISMATCH`, not `LIFT_REFUTED`.
3. If comparing \(F^2/p\), prove integrality and certify the required p³ raw precision or a direct normalized p² output. Keep the ordered sign/odd branch; norm alone does not reconstruct κ.

BRC/observer: the retained carrier is (source-labelled operator, Newton valuation, rank, σ, η, odd Green/Hesse signs, Δ/R); the norm reduction is safe only for the previously proved rank-one gauge question, not for raw supersingular slope or the future signed observer. The external quadratic coefficient ring is not the native X6 geometry or a complete 3D slice.

**Not done:** native H0/B0/[X]U run, actual F/η and κ, Source role/claim/open/checkpoint, independent review or all-prime LIFT/JT2 proof. Existing support Issue #1559 remains **PENDING_OWNER / SCIENTIFIC_BENCHMARK_NOT_EXECUTED**. This author no-go should be used as an extra acceptance discriminator, never to substitute another algebraic theory exercise for the missing original experiment.

## 5. Explicit arithmetic witness and references

For the precision claim at p=373, take two distinct integral normalized values `C=131` and `C'=504=131+373` modulo 139129. Their raw rescalings are identical:
`373*C = 48863 = 373*C' (mod 139129)`; nevertheless `C != C' (mod 139129)`. Thus this is an **exact precision-loss witness**, not a numerical tolerance estimate.

Standard external mathematical premise, NOT invented as a D25 axiom: supersingular elliptic first crystalline cohomology has Newton slopes `(1/2,1/2)` (ordinary slopes are `(0,1)`). See N. O. Nygaard, *Slopes of powers of Frobenius on crystalline cohomology*, Ann. Sci. ENS **14** (1981), 369–401, DOI 10.24033/asens.1411; M. D'Addezio, *Crystals and Parabolicity Conjecture* (2026), Example 2.3.2. This statement applies **only** if the measured native operator is actually the unnormalized H¹ crystalline Frobenius of the source supersingular elliptic curve.

## 6. Durable author-side continuation and operation boundary

Parent mother objective: D25/JT2 `Delta_p - R_p = 0 mod p` for both p≡13,19 mod24. Exact Task/publication remain as header; accepted UR/JT0, CM0/SIMPLE and original signed Clausen ports must be **consumed, not redone**. Frozen science Source pin above must NOT move when main/control changes.

Highest **author-side** immutable frontier: the present conditional raw-Frobenius normalization no-go and the precision-loss witness. This is an additional *native experiment acceptance discriminator*, not Source scientific checkpoint or progress toward an all-prime LIFT proof. Recent separate hourly lane p=733 three-channel Ward results at `20261026_hourly_d25_p733_three_channel_tangent_r11.md` belong to their original distinct logical conversation and are not claimed as this lane's contributions.

Still missing: **actual original-class native fixed H0/B0 divided-power computation** of `[X]U mod 373²`, module rank, native phi/Frobenius and eta, signed odd Green/Hesse and kappa readouts, comparison to original Delta-R, provenance/independent validation, and a uniform LIFT proof or counterexample. Support intake `https://github.com/awdawmip/enterprise-math/issues/1559` has no assigned executor as read this turn; its diagnostic acceptance refinement is comment `#issuecomment-6407983089`, not native acceptance.

This actual lane's ordinary-control ID remains `chatgpt-research-onhour-enterprise-math-20260923`. **Current executable native session_id / claim_id / run_id: NOT_RECOVERED; no ownership asserted**. Existing historical target request `research-onhour-20261026-1129-dispatch-v1` was reported as FAILED/TimeoutExpired by an earlier turn; the current direct control-result read returned `CONTROL_REQUEST_NOT_FOUND` and no Source effect was inferred or request replayed. Fresh exact native continuation returned `CONTROL_QUOTA`; own Site checkpoint list returned `ACCESS_DENIED`. Site connection reports static read-only scopes and disabled write relay. No `session_start/prepare/CLAIM/OPEN` was attempted without sufficient current authority; another lane's historical session is not reused.

**Next exact authorized scientific step:** original-class p=373 native executor must produce the source-pinned H0/B0 [X]U result under the original coefficients, report whether phi is raw/normalized and its Newton valuation, rank, eta and operator precision; apply the theorem above to discriminate a type mismatch before any conditional norm test. Accept independently reproducible signed kappa/Delta-R only after authenticated original class. If still no executor, the ticket remains PENDING_OWNER and the native experiment NOT_EXECUTED. In subsequent research turns read existing receipts/continuation first; preserve unique ownership; do not re-dispatch on a missing receipt or re-prove accepted auxiliary lemmas. The recurring automation remains untouched.
