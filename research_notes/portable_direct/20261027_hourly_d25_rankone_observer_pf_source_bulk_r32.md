# D25/LIFT R32 — Exact one-shear observer repair and a growing Picard–Fuchs source budget

Date: 2026-10-27, Asia/Hong_Kong. TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923` (separate from maintenance `chatgpt-hourly-enterprise-math-20260921`). Exact task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Parent D25/LIFT/JT2 OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / ACTIVITY_SYNC_PENDING.** This is a finite-field source/observer theorem, NOT original W=S modulo p³, a WZ telescope on the original fixed input, a native H0/B0 experiment, an admitted Source checkpoint, a formal Result or independent review.

## Precise question, consumed source and carrier

R27 proved the *full* finite-field Picard–Fuchs source intertwiner `L_S H_m=K_m L_W`, including the `X^m` boundary, with unit/invertible `H_m,K_m`. R28 proved the Green isomorphism `L_W:V_m -> G_m` and its exact endpoint inverse. R31 proved that the genuine weighted W/S observer has no bounded-degree all-input rational *diagonal* rank-jet transfer, and for `p=13 mod24` even unrestricted regular diagonal rational jets fail because precisely one S weight vanishes. None of those results supplies an all-input rank-mixing repair, nor quantifies the genuine PF source cost of such a repair. Consume without recredit R25's Hadamard ratio and zero-weight classification and R31's exact weight-ratio recurrence.

Let `p=6m+1` be prime, `p mod24 in {13,19}`, `F=F_p`, and `V_m=F[X]_(degree<m)`. For `0<=r<m`, define

```text
a_0=h_0=1,
a_r/a_(r-1) = 2(3r-1)^3/[3r(6r+1)(3r+1)]  (1<=r<m),
h_r/h_(r-1) = 48r(3r+1)/[(12r-1)(12r+5)],
omega_r=(2r+1)2^r,
sigma_r=(8r+13/3)9^r h_r.
omega(f)=sum_(r<m) omega_r f_r, sigma(f)=sum_(r<m) sigma_r f_r.
```

All displayed recurrence denominators and `a_r,h_r,omega_r` are nonzero on the specified ranks. `sigma_r` is the *S evaluation weight after the genuine R25 Hadamard transport*, not an identification of the original scalar W and S series. R25's classification says all `sigma_r` are nonzero for `p=19 mod24`; for `p=13 mod24` the unique zero lies at `q=(p-13)/24`, and `s=q+1<m` has `sigma_s!=0`.

## Theorem A — one adjacent rank shear is necessary and sufficient to repair the weighted-hole observer

For `p=19 mod24`, put `d_r=omega_r/sigma_r` and let `T=diag(d_r)`. Then `T` is invertible and `sigma(Tf)=omega(f)` for every `f in V_m`.

For `p=13 mod24`, set

```text
q=(p-13)/24,  s=q+1;
d_q=1,  d_r=omega_r/sigma_r for r != q;
beta=omega_q/sigma_s;
T=diag(d_0,...,d_(m-1)) + beta*E_(s,q).
```

Equivalently, `(Tf)_r=d_r f_r` for `r!=s`, and `(Tf)_s=d_s f_s+beta f_q`. Then `T` is invertible and

```text
                 sigma(Tf)=omega(f) for ALL f in V_m.              (A)
```

**Proof.** Only the `s`-th output coordinate receives the off-diagonal term. The coefficient of `f_q` in the scalar output is `sigma_s beta=omega_q`; every other input coefficient is `sigma_r d_r=omega_r`. Since `s!=q` and all `d_r` are units, the matrix is triangular after ordering its two affected coordinates; its determinant is `product d_r !=0`. In the 19-class there is no hole and the diagonal argument suffices. For the 13-class, any entirely diagonal `T` has coefficient zero on `f_q` in `sigma(Tf)`, while `omega_q!=0`. Therefore *at least one* nonzero off-diagonal entry is necessary. The exhibited rank-one matrix correction `beta E_(s,q)` uses exactly one, so this lower bound is sharp. QED.

More generally, in the 13-class any all-input repair having exactly one off-diagonal entry must place it at `(s,q)` for some `s!=q` with `sigma_s!=0`, with coefficient `beta=omega_q/sigma_s`; its remaining `d_r=omega_r/sigma_r` for `r!=q`, and `d_q` is an arbitrary nonzero element for invertibility.

**Original weighted-port normalization.** R28's true W-high/S-mid prefactors `C_m,D_m` are nonzero p-units on these target classes (all factorial arguments are <p). Thus `T_original=(C_m/D_m)T` gives `D_m sigma(T_original f)=C_m omega(f)` for every free input. This is an exact *change of source input*, NOT the original-input identity `D_m sigma(f)=C_m omega(f)`.

## Theorem B — the exact induced PF source map and the unavoidable bulk source budget

Let `L_W`, `L_S`, `H_m`, `K_m` have precisely R27–R28's definitions; set `G_m=X F[X]_(degree<=m)`. Then

```text
C_T = K_m L_W T (L_W)^(-1): G_m -> G_m
L_S H_m T = C_T L_W.                                      (B)
```

`C_T` is an invertible, generally nonlocal, source map. This follows directly from R27–R28, since each factor is invertible. Unlike the mere scalar equality (A), (B) retains all source indices and the `X^m` endpoint.

For the *actual homogeneous truncated coefficient vector* `a=sum a_r X^r`, R28 gives

```text
L_W a = c X^m,  c=a_(m-1)/8 !=0.
```

Write `y=T a`, `u_r=y_r/a_r`, `A_t^PF=t(t+1/6)(t+1/3)`. By the full PF coefficient recurrence,

```text
[L_W y]_t=A_t^PF a_t (u_t-u_(t-1)),        1<=t<m,          (C)
[L_W y]_m=c u_(m-1),
[L_S H_m y]_t=t h_(t-1)[L_W y]_t,          1<=t<=m.          (D)
```

In particular source injection at rank `t` is nonzero exactly when `u_t!=u_(t-1)`. The endpoint is separately preserved and is not counted as an interior source.

R31's exact *weight* recurrence for `R_r=omega_r/sigma_r`, wherever both sides are defined, is

```text
R_t/R_(t-1)=B(t)/A(t),
A(t)=216t(2t-1)(3t+1)(24t+13),
B(t)=(2t+1)(24t-11)(12t-1)(12t+5).
```

Thus outside a modified coordinate and its neighboring source edges, `u_t=u_(t-1)` holds iff the explicitly nonzero quartic vanishes:

```text
Psi(t)=A(t)-B(t)
      =24192t^4+9072t^3-6264t^2-2270t-55.             (E)
```

Its leading coefficient `24192=2^7 3^3 7` is a p-unit for every `p mod24 in {13,19}`, so `Psi` has at most four roots in `F_p`.

Consequently, **on the actual `a` input**:

* In the `19 mod24` class, the forced diagonal transfer `T` creates at least `max(0,m-5)` nonzero **interior** PF source ranks.
* In the `13 mod24` class, **any** all-input observer repair that is a diagonal matrix plus exactly one off-diagonal entry (and invertible diagonal) creates at least `max(0,m-9)` nonzero interior PF source ranks. Indeed, its sole off-diagonal entry must occupy column `q` and a nonhole row `s`; only source edges `{q,q+1,s,s+1}` (at most four) can escape (E), while (E) itself can vanish at at most four other edges.
* For the **adjacent** shear of Theorem A, the exceptional edges reduce to `{q,q+1,q+2}`, at most three. The lower bound improves to `max(0,m-8)`.

This proves a *growing interior source budget* for the specified exact all-input minimal-rank repairs. The existence of a sparse rank-one coefficient repair therefore does **not** produce a sparse native PF/WZ compensation or original W/S congruence. The bounds do not rule out other nonlocal, multi-off-diagonal, original-low-half or source-specific WZ maps. QED.

## Actual exact author check

The local Python 3 standard-library finite-field checker was executed and returned `D25_R32_ONE_SHEAR_SOURCE_BULK_PASS`. It checked **77 target-class primes below 2000** (40 of residue 13 and 37 of residue 19), coefficientwise scalar equality on three independent polynomial input families per prime, and the FULL `L_S H_m T=K_m L_W T` including `X^m`: **34,461 exact residual-coefficient checks**. It separately rebuilt the genuine homogeneous `a_r`, checked `L_W a=cX^m`, checked (C)–(E) on every applicable strict edge and checked the source-count bounds. The universal theorems are proved above, not inferred from finite tests.

Representative exact residues (all counts concern `1<=t<m`, with `g_m=[L_W(Ta)]_m`):

| p | m | hole q | shear target s | beta | nonzero interior PF source ranks | g_m mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 0 | 1 | 1 | 1 | 7 |
| 19 | 3 | — | — | 0 | 2 | 12 |
| 43 | 7 | — | — | 0 | 6 | 29 |
| 181 | 30 | 7 | 8 | 71 | **29 of 29** | 104 |
| 373 | 62 | 15 | 16 | 62 | **61 of 61** | 177 |
| 733 | 122 | 30 | 31 | 155 | **121 of 121** | 447 |

At `p=181` the normalized original-input S port is zero, `sigma(a)=0`, while `omega(a)=178`. The repaired *different input* has `sigma(Ta)=178`; after R28's true prefactors, this is `U_181=152`, whereas the unmodified S-mid port is `M_181=0`. The example is therefore not a W=S proof or contradiction.

Verifier file: `research_notes/portable_direct/20261027_hourly_d25_rankone_observer_pf_source_bulk_r32_check.py`. All integer modular inverses are defined on the declared range; no floating point, unexecuted native experiment, sorry/admit or custom axiom is used. Independent review remains pending.

## BRC, source identity and next smallest unfinished unit

**BRC COMPOSE_APPLIED / OBSERVER-FACTORIZATION AND RESIDUAL-RETENTION TEST** using existing R27/R28/R31 interfaces. Carrier: two explicitly source-tagged W/S rank arrays, genuine `k↔j↔r` provenance, nonzero Hadamard `h_r`, unique S-weight hole, prime modulus, original homogeneous `a_r`, rank-one coefficient shear, full PF internal residuals and `X^m` endpoint. Future permitted operations: weighted readout, `L_W,L_S,H_m,K_m` and full source/adjoint observers. Quotienting the interior sources after a scalar observer repair demonstrably destroys information necessary to recover the next PF observation. These polynomial indices are external finite-field research coordinates, not native X6 directions, not a P000 or ACTIVE-worldview change.

**Do not repeat:** R25's source-hole classification, R27's full PF intertwiner, R28's Green inverse, R31's rational degree obstruction, or the already-author-checked finite data. **Next mathematical unit:** use the *actual original low-half p²-divided W/S discrepancy* (R23/R29) and its two genuine source tags to derive or exclude a **nonlocal original-input** telescoping compensator. A viable certificate must explicitly cancel the nonzero internal PF source distribution in (C)–(D), account for the endpoint, retain the `p=181` special S-port loss, and work in both `13/19 mod24` classes. Do not replace the original `f=a` by `Ta` and mistake (A) for the hard target. The six original fixed-z=2 Hasse J/E ports, finite faces, positive infinity, high-high terms, original H0/B0, `[X]U mod p²`, semilinear eta/kappa, original p=373 native experiment and independent Driver review remain separate unsatisfied obligations.

**Current control boundary:** The Research lane's own read-only [recovery #6591](https://github.com/awdawmip/kimi-query-bridge/issues/6591) returned a service-bound Researcher `EM-ENTERPRISE-5298BA`, session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94`, no own local pending writes/claim/run/unpublished uploads, preserved neutral staging, and no research authorization. Its [complete canonical continuation #6592–#6594](https://github.com/awdawmip/kimi-query-bridge/issues/6592) preserved a verified historical native checkpoint but found predecessor-claim mismatch. The once-only [continuation_prepare #6595](https://github.com/awdawmip/kimi-query-bridge/issues/6595) definitively returned `CHAT_CHECKPOINT_PREDECESSOR_MISMATCH`. This note does not retry it, rebind old IDs, post a CLAIM, OPEN, Source checkpoint or Result. Control acceptance/owner remains in [Enterprise Math issue #1558](https://github.com/awdawmip/enterprise-math/issues/1558). Any activity record update is separately `ACTIVITY_SYNC_PENDING` until exact source readback; Github portable proof is not formal admission.
