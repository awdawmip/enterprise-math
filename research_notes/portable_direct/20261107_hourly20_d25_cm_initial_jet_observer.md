# D25: conditional first signed Fricke jet and CM-class p² finite observation

Date: 2026-11-07. TASK_RESEARCH **AUTHOR-SIDE PROVED CONDITIONAL ALGEBRA / EXACT FINITE TESTED / UNREVIEWED / NOT_ADMITTED**. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This extends this lane's 216 p³ coefficient lift in commit `cb53f8b671f4b8ada7008aae235482a32ccd6f70` and separately consumes **science only**, not ownership, from the on-hour finite Fricke two-jet in commit `22538312c7d022d773dd09562273e724d23af290`.

## Definition and exact conditional theorem

For p>3 prime, let `a_n=(2n)!(3n)!/[216^n(n!)^5]`, `b_n=(4n)!/[2304^n(n!)^4]`, and in the p-local ring

`A=sum_(n=0)^(p-1) a_n,` `J=sum n a_n,` `B=sum b_n,` `K=sum n b_n.`

Set `chi=(-3/p)`. Work modulo p² and let `s²=2`. The exact finite Fricke pullback already provides, at `t_+=6s`, the **value/derivative** of the finite cutoff defect:

`E(t_+)=A-(3s/4)B`,
`E'(t_+)=(-2J+7B/8+4K) + s(3J/2-5B/8-3K)`.

**Conditional theorem:** Assume the two precise mod-p² hypotheses
(H1) `A=B=0`, and (H2) `A+6J=B+8K=p chi`.
Then the exact resulting first signed-branch jet is

`E(t_+)=0 mod p²`, `E'(t_+)=p chi(1/6-s/8) mod p²`.

For the conjugate port `t_-=-6s`, change `s -> -s`. In particular the **normalized** first-jet relative trace and norm modulo p are

`Tr(E'(t_+)/p)=chi/3`, `Norm(E'(t_+)/p)=-1/288`.

For both frozen target residue classes p=13,19 (mod24), `chi=1`, so this norm is a uniform nonzero residue and the trace is `1/3`. No assumption `s∈Fp` is made: these are quadratic-algebra trace/norm coordinates; split/inert behavior is kept separate. This is an explicit BRC **signed-port first-jet observer** that cannot be inferred from the scalar value alone.

**Proof:** (H1) gives `J=p chi/6`, `K=p chi/8` modulo p², by (H2); division by 6,8 is valid for p>3. Substitution into the exact derivative yields the stated real/signed components. The conjugate trace is twice `chi/6`, and norm `(chi/6)²-2(chi/8)²=1/36-1/32=-1/288`. All equalities are algebraic and universal *given H1 and H2*. They are not an unconditional proof that H1/H2 hold for every prime.

The independent exact finite weighted Fricke identity then implies
`W_p-(3/2)V_p=-p chi/2 (mod p²)`
under (H2), consistently with `E+(24+18s)E'`. This does **not** give its required p³/p⁴ extension without higher initial-value and coefficient-lift information.

## Exact finite test and unresolved proof obligation

Python standard-library modular recurrence checked **all 301 primes 5<=p<2000**: `A=B=0 (mod p²)` exactly in the **152 tested primes** in residue classes `13,17,19,23 (mod24)`, with zero combined observations in the other 149 tested primes. Both weighted mod-p² congruences in (H2) held for all 301 tested primes. Within the 152, the normalized signed first-jet formula held for all; 77 are in the two frozen target classes. Five separate selected primes p=13,19,43,67,373 had all coefficients independently recomputed with raw factorial/binomial formulas. This is a finite observation, **NOT** a proof of an all-prime CM-class iff, nor a native p373 H0/B0 experiment.

Selected exact residue witnesses, with `A/p=B/p=0 (mod p)` and `J/p,K/p` listed:
`p=13:(11,5)`, `p=19:(16,12)`, `p=43:(36,27)`, `p=67:(56,42)`, `p=373:(311,140)`.

**BRC application:** Preserve both original coefficient streams `a_n,b_n`, their signed Fricke conjugates and weighted moments `J,K`; the scalar projection `E(t)=0` loses the normalized first-jet `(1/6∓s/8)`. `COMPOSE_APPLIED` on the exact previously published two-jet, with independent modular coefficient evaluation.

**Next discriminating step:** seek a general CM/Dwork/Hasse argument for the *unweighted* `A=B=0 (mod p²)` in the two frozen target classes, or find a counterexample beyond the finite window. Then compute the normalized p² correction of `E'` from the separate 216 and 2304 exact p³ stratum lifts and test a finite WZ/Frobenius certificate for `W_p-V_p=0 (mod p³)`. Keep 216/2304 source ports and the complete native p373 experiment distinct; no proof of LIFT/JT2 or native checkpoint is claimed.

**Control:** Site `CONFIGURED_NOT_LIVE_VERIFIED`, native `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`, Researcher session/claim/run/staging `UNKNOWN_PRESERVE`, registration `REGISTER_PENDING`. Historical request IDs `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13`; support `awdawmip/enterprise-math#1558`. No new claim/session/Result/review.
