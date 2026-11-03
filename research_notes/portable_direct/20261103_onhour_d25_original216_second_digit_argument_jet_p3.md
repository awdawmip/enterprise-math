# D25 onhour — original 216 second-digit argument jet via finite Clausen/Gauss ODE

Date: 2026-11-03 (+08). TASK_RESEARCH, author-side mathematics, logical lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`. Status **AUTHOR-DERIVED / ALGEBRAICALLY-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. No native Claim/run/Result is inferred.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Mother objective: for all primes p ≡ 13 or 19 (mod 24), the ORIGINAL weighted 216 sum `W_p(1) ≡ p (mod p^3)`, equivalently frozen `Delta_p-R_p=0 (mod p)`; remains **OPEN**.

## Smallest unfinished unit selected

The prior argument-deformation lane proved the first derivative `W'_p(1) mod p` and recorded `W'_p(1) mod p^2` as the missing operand for an exact deformation at precision p^3. Here that operand is determined **without assuming the open mother congruence**. We consume the accepted D24 CM0/first-digit result, the already proved finite Clausen identity, the previously proved second derivative modulo p, and the existing original-index coefficient filtration, without recrediting them.

For p=6r+1 in the target classes, work over Z_(p). Put
```
B_k = (2k)!(3k)! / ((k!)^5 216^k),
F_p(t) = sum_{k=0}^{p-1} B_k t^k,
W_p(t) = (1+6 t d/dt)F_p(t).
c_k=(1/6)_k(1/3)_k/(k!)^2,
G_p(z)=sum_{k=0}^{p-1}c_k z^k,
z0=1/2, g=G_p(z0), d=G'_p(z0).
```
The inherited CM0 makes g divisible by p; the inherited first-carry proof gives d mod p a unit. Index, orientation, weights, and original integer valuations remain separately typed.

## Theorem A — full finite polynomial Clausen transfer at precision p²

**PROVED**, in `Z_(p)[t]/(p^2)`:
```
F_p(t) = G_p(t/2)^2  (mod p^2), coefficientwise.
```
Proof: The exact formal Clausen identity yields equality for all degrees <p, because the original `B_k/2^k` are the corresponding 3F2 coefficients. For 0≤k<p, `v_p(c_k)` is 0 on [0,r], 1 on [r+1,2r], 2 on [2r+1,p-1]. For a pair k+l≥p, both indices cannot lie in [0,2r] because 4r<p. Therefore every such product `c_k c_l` has valuation ≥2. Hence all extra degrees p..2p−2 of the finite square vanish modulo p², closing the full polynomial identity. QED.

## Theorem B — missing derivative digit as an explicit Gauss-jet observer

**PROVED**, for every prime p in the frozen classes:
```
W'_p(1) = 3d²+4gd  (mod p²).
```
Proof: the Gauss coefficient recurrence `(k+1)^2 c_{k+1}=(k+1/6)(k+1/3)c_k` gives the standard Gauss equation
```
z(1-z)G''+(1-3z/2)G'-(1/18)G=0 (mod p²).
```
Its only terminal coefficient is a p-unit multiple of `c_{p-1}`, divisible by p² (both parameter roots have been crossed). At z0=1/2, `G''(z0)+d-(2/9)g=0 (mod p²)`.

From Theorem A, with z=t/2,
```
W_p(t) = G(z)^2+12zG(z)G'(z)  (mod p²),
W'_p(1) = 7gd+3d²+3gG''(z0)
        = 3d²+4gd+(2/3)g²  (mod p²).
```
Since p divides g, `g²=0 (mod p²)`. All denominators 2,3,9 are p-units, so the statement is valid without a p-adic lift choice for the Gauss root. QED.

This lifts the previously proved first derivative `W'_p(1)=3d²=12j² (mod p)` and is NOT the original frozen second carry.

## Theorem C — exact signed p³ deformation and two-branch curvature

**PROVED** for all `lambda ∈ Z_(p)`:
```
W_p(1+p lambda)-W_p(1)
  = p lambda (3d²+4gd) + p² lambda² d² (mod p³).
```
Indeed the finite binomial Taylor formula is `p lambda W'_p(1)+p²lambda² W''_p(1)/2`, and the prior finite argument-jet theorem gives `W''_p(1)=2d² (mod p)`. Equivalently, the oriented two-branch difference obeys
```
W_p(1+p lambda)+W_p(1-p lambda)-2W_p(1)
  = 2p² lambda² d²  (mod p³).
```
This is a full-precision, signed BRC observer on two p-adic lift branches; the carrier retains original `k`, `v_p(B_k)`, `6k+1`, Gauss `g,d`, and lambda. It resolves the prior *deformation* digit at the stated precision, while `W_p(1)` (baseline) remains the separate frozen mother obligation.

## Executed exact arithmetic and source boundaries

The companion standard-library checker `d25_second_digit_argument_jet_20261103.py` actually ran on every one of 77 target primes p≤2000 with lift choices lambda=1,2,3 (231 evaluations). It independently computes original binomial coefficients for p=13,19,373, the Gauss polynomial and its first two derivatives, original weighted derivatives, the Gauss ODE modulo p², the full Taylor identity modulo p³ and signed two-branch curvature. All assertions PASS. These are regression evidence beside the all-prime algebraic proof; no native H0/B0 is run.

Selected exact readouts:
| p | g/p mod p² | d mod p² | W'(1) mod p² | W''(1) mod p | W(1+p) mod p³ | two-branch curvature mod p³ |
|---:|---:|---:|---:|---:|---:|---:|
|13|76|1|68|2|1066|338|
|19|84|344|278|8|6745|2888|
|373|65672|78545|84217|319|27656831|44382151|

These reproduce previously sourced p13/p373 argument jets but now specify the previously missing derivative modulo p² for all target primes.

## Exact continuation

**Mother:** `Delta_p-R_p=0 (mod p)` for p≡13,19 (mod24), equivalently original `W_p(1)=p (mod p³)`, OPEN. **Highest immutable preceding author frontier:** `51f7595dd131bb0b48f04f7c3be92e58201f5974`; this new unit consumes that and the independently sourced argument-jet sibling, without taking the sibling's identity/claim. **Done and not repeated:** accepted D24 UR/first digit, exact original 216 high mirror and full terminal 4F3 ODE, finite Clausen and first carry, Hensel three-strip ODE. **New proved:** p² derivative and p³ signed argument deformation as above. **Remaining science:** a fixed-baseline p³ identity coupling Gauss/Clausen defect, signed high 4F3 and original half-cutoff second carry; full proof or in-hypothesis counterexample. **Next exact action:** search for terminating parameter/argument contiguous or WZ certificate on the fixed t=1 baseline, preserve H2 and p13/p19/p373 signed second-carry checks, and do not substitute deformation-only control for the mother target.

Native experiment #1559 remains `NOT_EXECUTED / PENDING_OWNER`: fixed p373 original same-class H0/B0 divided-power `[X]U mod139129`, rank, actual semilinear Frobenius/eta, odd signed Green/Hesse κ, independent reproduction. Existing support #1558 is separate. Native Gateway 0.6.11 on 2026-11-03 reports `research_authority_granted=false`, Sites `write_relay_enabled=false`, native control quota active 5/5. Own onhour #6632 recovery status was a read-only projection with historical service session and neutral staging but no run/claim; original dispatch request `research-onhour-20261031-0205-dispatch-r15`, bridge #6633, definitively `FAILED/UPSTREAM_CODE_REVIEW_REQUIRED`; direct control_result returned `CONTROL_REQUEST_NOT_FOUND` today. No request replay, no maintenance identity, no new role-bound session, claim, run, Source checkpoint, Result/review/admission or scheduler/notification change. Author GitHub publication is independent evidence preservation, not native Source acceptance.
