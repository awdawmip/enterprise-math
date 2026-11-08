# D25 — Exact original-E3 2-isogeny on H¹_dR in the natural Weierstrass basis

Date: 2026-11-08. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged.

**AUTHOR-SIDE EXACT PROOF / SIX EXACT Q(sqrt2) TEST POINTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**. This is a new de Rham operator calculation on the previously established exact original-class 2-isogeny, not a second credit for construction or Frobenius point counting.

## Chosen mathematical unit

Determine the exact action of the prior original-class degree-two isogeny `Phi:E3 -> E3^sigma` on BOTH basis classes of H¹_dR, not merely on the invariant differential. This is a necessary Hodge-level comparison observable for any future native H0/B0 geometric identification; no current native crystalline identification is assumed.

Work over `K=Q(T), T²=2, sigma(T)=-T`. Original curve `E3: y²+xy+cy=x³`, `c=(2-T)/108`; define `omega=dx/(2y+x+c)`, `beta=x*omega` (standard second-kind de Rham class). The conjugate basis is `(omega_sigma,beta_sigma=x_sigma*omega_sigma)`.

Reuse, not reprove, the previous degree-two isogeny:
- `e=(2T-3)/36`, `u=x-e`, `z=y+(x+c)/2`.
- `z²=u³+a u²+b u`, `a=T/6`, `b=(3-2T)/432`.
- `U=u+a+b/u`, `Z=z(1-b/u²)`.
- `u_sigma=U/2`, `z_sigma=T Z/4`, `x_sigma=u_sigma+e_sigma`, with `e_sigma=(-2T-3)/36`.
- Prior result: `Phi^*omega_sigma=T omega`; `Phi^sigma Phi=[-2]`.

## New exact differential certificate

Write `f(u)=u³+a u²+b u=z²`. From `2z dz=f'(u)du`, a direct differentiation gives the exact rational differential

```text
d(z/u) = (u f'(u)-2f(u))/u² * du/(2z)
       = (u-b/u) omega.
```

The quotient expression yields, **as differentials on the common regular chart where u≠0**,

```text
Phi^*(beta_sigma) = T*(U/2+e_sigma)*omega
                  = T*beta + T*(a/2+e_sigma-e)*omega
                    - (T/2)*d(z/u).
```

Since `a/2+e_sigma-e=-T/36` and `T²=2`, this is

```text
Phi^*(beta_sigma) - T*beta + (1/18)*omega
    = -(T/2)*d(z/u).                    (★)
```

The last term is an exact rational differential. Therefore in algebraic de Rham cohomology (second-kind differential representatives, regular proper elliptic curve) the precise source-labelled operator, in the **natural original Weierstrass basis** `(omega,beta)`, is

```text
          [ T  -1/18 ]
    C  =  [ 0    T   ].
```

In the conjugate bases `C_sigma=[[-T,-1/18],[0,-T]]`. Direct matrix multiplication gives `C*C_sigma=-2 I`, agreeing with the existing geometric composite `Phi^sigma Phi=[-2]`; the nonzero mixed port `-1/18` is independently forced by exact-differential reduction, not by fitting a scalar norm.

Moreover, the *explicit Galois-compatible* basis shift

```text
    beta_tilde = beta - (T/72)*omega
```

satisfies `Phi^*(beta_tilde_sigma)=T*beta_tilde` **in H¹_dR** (the same exact differential term as in (★) persists before taking classes). Hence `C` can be diagonalized by a declared coordinate change, but **it is not already scalar T in the natural original basis**. The shift is integral at all primes `p>3`.

## Scope, source/observer information

This is an all-characteristic-zero identity and gives good-reduction comparison data for `p>3` (the map and coefficients have only 2,3 in denominators). It specifies the actual original curve, original Galois conjugation, differential basis, ordered isogeny direction, exact gauge and cohomological reduction. BRC: `COMPOSE_APPLIED` in the tagged source-operator/provenance sense; no positive branch-mass semantics, no native X6 plane claim. The invariant differential alone erases the off-diagonal source port; the declared `beta_tilde` basis supplies its reversible coordinate repair.

**Native acceptance is still open.** A genuine original-class crystalline H0/B0 comparison must first produce the authentic divided-power `[X]U mod 139129` at `p=373`, rank, semilinear direction, basis and normalization eta, plus signed Green/Hesse kappa and original Delta-R. If it admits reduction to this original de Rham realization, its claimed isogeny comparison must match `C` up to a **proved, explicit** base-change map, not just an equal norm or unlabelled scalar `T`. This de Rham computation does not measure, replace or authenticate H0/B0.

## Executed author check

Companion exact standard-library program `d25_e3_isogeny_de_rham_check_20261108.py` checks the six algebraic identities and evaluations at `u=1,2,-5,3+T,2+3T,1-2T` using rational pairs in `Q[T]/(T²-2)`, checks `C*C_sigma=-2I`, and checks the precise eigenbasis shift. Output: `PASS`. The proof is symbolic and does not rely on finite sampling; these are regression tests, not native computations.

## Durable parent continuation

Parent mother target `Delta_p-R_p≡0 modp` for `p≡13,19 mod24` remains open, and p373 native same-original-class H0/B0 divided-power benchmark is independently pending in existing support issue #1559. Do not redo frozen D24 UR, original E3 point count, degree-two isogeny proof, formal/Hasse difference, or historical Source units. Current native state: read-only Source continuation request `onhour11-20261108-2202-current-task-continuation` SUCCEEDED; historical session-start request `onhour11-20261108-2202-own-researcher-session-start` SUCCEEDED and persisted `MCP-ecbfd1c046864bb3bff1a2e04c87d207` / `RA-9553E027FD14223807511263`, but its private session key was not durably retained in this turn. No new claim/run, and this author result is **not** registered as that native session's checkpoint. Own recovery_status without capability returned `SESSION_CAPABILITY_REQUIRED`. Retain those exact original request IDs, do not replay the session-start operation or borrow maintenance identity. Source signed owner/frontier must be verified before any lawful future prepare/claim/open.

**Next executable native step:** service-side authorized session capability recovery if allowed, or lawful own session disposition and fresh registration only after current Source/pending effects reconcile; then exact canonical continuation/claim only as permitted. Scientific priority: locate native H0/B0 implementation/owner and execute unchanged p373 [X]U/rank/direction/eta/signed kappa/Delta-R with independent reproduction; only then use this de Rham matrix as a typed comparison.
