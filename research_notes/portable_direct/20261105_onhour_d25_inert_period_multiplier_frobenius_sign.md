# D25 — Frobenius-odd inert period multiplier and exact descent normalization

2026-11-05. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923` (distinct from maintenance). Classification **AUTHOR-PROVED FINITE-FIELD LEMMA / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

## Selected question, source and BRC observer

The original weighted source sums are (W_p=\sum_{k=0}^{p-1}(6k+1)(2k)!(3k)!/(216^k(k!)^5)) and (V_p=\sum_{k=0}^{p-1}(8k+1)(4k)!/(2304^k(k!)^4)). The frozen target for (p\equiv13,19\pmod{24}) is (Δ_p-R_p=0\pmod p), source-aligned with (W_p=V_p\pmod{p^3}). Earlier source-labelled upper-shell transport and signed half-prefix carry are consumed without re-proving them. This unit tests a **quadratic-character/Frobenius observation**, motivated by the separately certified analytic proximity (|8A^2-9B^2|<10^{-145}) for the two *infinite* original coefficient sums (A,B). The analytic equality and any p-adic transformation remain open.

For each target prime (p>3), set (E_p=\mathbb F_p[T]/(T^2-2)) and (σ(x)=x^p). Since (p\equiv3,5\pmod8), (2) is a quadratic nonresidue and (E_p) is a field of order (p^2), with (σ(T)=-T). Define the *candidate analytic-ratio encoding*, not a native Frobenius coefficient,
[
s=\frac{3}{2T}=\frac34T.
]

## Theorem: signed Frobenius norm and descent criterion

For every prime (p\equiv13,19\pmod{24}):
[
\boxed{s^2=9/8,quad σ(s)=-s,quad N_{E_p/\mathbb F_p}(s)=-9/8.}
]
For any (t=a+bT\in E_p),
[
\boxed{ts\in\mathbb F_p\iff σ(t)=-t\iff a=0.}
]
More precisely, for each (c\in\mathbb F_p), the **unique** (t\in E_p) with (ts=c) is
[
\boxed{t=\frac{2c}{3}T.}
]
The unique first-digit descent normalization for scalar (c=1) is
[
\boxed{\eta_0=\frac23T,quad σ(\eta_0)=-\eta_0,quad \eta_0s=1,quad N(\eta_0)=-8/9,quad N(\eta_0)N(s)=1.}
]
All denominators are (p)-units.

**Proof.** Quadratic reciprocity gives ((2/p)=-1) because target (p\equiv 3,5\pmod8). Thus (σ(a+bT)=a-bT). The exact equation (T^2=2) yields (s=3T/4), (s^2=9/8), and (sσ(s)=-s^2=-9/8). Since (s\ne0), (ts) is fixed by (σ) iff (-σ(t)s=ts), iff (σ(t)=-t), iff (a=0). For (t=bT), (ts=3b/2), hence (b=2c/3). Norm identities follow by conjugation.

This provides a **discriminating requirement** for a future normalized source-preserving A/B transform: if a transform actually used the analytic scalar (s) in the inert extension yet had to descend to the original (mathbb F_p)-valued first digit (W_p/p=V_p/p=1\pmod p), its normalization must have an anti-invariant component; the purely scalar unit (1) cannot achieve descent. The specific candidate (η_0) is **not** the original-class native H0/B0 Frobenius normalization (η); identifying it would require a real authenticated source transfer and native experiment. The unnormalized naive scalar identity (W_p=sV_p\pmod{p^2}) contradicts the frozen first-digit scalar values: dividing both by (p) would demand (1=s) in (E_p).

## Exact independent finite check

A runnable pure-integer finite-field checker, `d25_inert_quadratic_period_factor_check_20261105.py`, checked all **312** target primes (5\le p<10000), with zero failures, asserting Frobenius sign, norm, reciprocal normalization and several test fibers for the descent condition. Selected ((p,s_T,s^2,N(s))): ((13,4,6,7)), ((19,15,13,6)), ((139,105,88,51)), ((373,94,141,232)). The universal lemma is proved algebraically; the finite scan is only independent checking.

BRC source/observer: labels original 216/2304 families, complex/infinite versus finite-field/truncated analytic route, signed (σ)-odd coordinate, norm port, invariant scalar readout, and original half-prefix/cutoff. The norm compression discards the anti-invariant sign; retain (T)-coefficient until the required future operations are done. Reuse status `COMPOSE_APPLIED` (pre-existing Hesse finite-field involution + source-labelled 216/2304 route), not native execution.

## Frontier, external benchmark and next exact action

This work completes an **algebraic descent classification**, not the mother p-adic finite-sum relation. Next: derive or falsify an algebraic pullback between the two original hypergeometric periods, then construct a finite (p)-parameter transform including cutoff correction and Frobenius-odd unit, comparing its descended scalar at (p=13,19) and relating to the existing half-endpoint signed (p^2)-carry certificate. The true fixed-373 original H0/B0 divided-power `[X]U mod139129`, module rank, semilinear direction, native eta/kappa, odd Green/Hesse observer and independent replication remain `NOT_RUN / PENDING_OWNER` under Issue #1559.

Previously verified Source request `onhour11-20261105-1505-d25-own-read` returned `SUCCEEDED / execution_authorized=false`. Fresh read-only continuation request `onhour11-20261105-1757-d25-own-continuation` remained QUEUED during this author work; reconcile that original ID before further native mutation. Researcher session/claim/run/result were not established in this run.
