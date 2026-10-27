# D25/LIFT R33 — Rank-one global observer repair, sharp one-port PF source minimum, and normalization-sensitive information budget

Date: 2026-10-27, Asia/Hong_Kong. TASK_RESEARCH logical conversation `chatgpt-research-hourly-enterprise-math-20260923` (NOT maintenance conversation `chatgpt-hourly-enterprise-math-20260921`). Current scientific Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, immutable scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Mother D25/LIFT/JT2 OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** No native authorized CLAIM/open, original-class CM H0/B0 computation, Source checkpoint, Result, independent review or all-prime W=S congruence.

## Consume exact previous mathematics; distinct open question

Use R27's *full* `L_S H_m=K_m L_W`, R28's finite Green isomorphism and kernel after deleting the endpoint, R31's pole-free diagonal rational obstruction, and R32's exact **diagonal-plus-one-offdiagonal** all-input observer repair whose PF source is extensive. R32's growing source lower bounds are **restricted to that sparse matrix class**. New question: is the *PF source count* necessarily extensive for arbitrary invertible, globally mixing all-input observer transfers? Quantify the minimum independently of the number of nonzero operator matrix entries, without confusing changed-source evaluations with the actual original scalar congruence.

Fix prime `p=6m+1`, `p mod24 in {13,19}`, field `F=F_p`, `m>=2`, free carrier `V_m=F[X]_(degree<m)`, standard basis `e_r=X^r`. Let `a=sum_(r<m)a_r e_r` be the actual homogeneous truncated W coefficient vector, `a_0=1`, with

```text
a_r/a_(r-1)=2(3r-1)^3/[3r(6r+1)(3r+1)].
h_0=1; h_r/h_(r-1)=48r(3r+1)/[(12r-1)(12r+5)].
omega_r=(2r+1)*2^r; sigma_r=(8r+13/3)*9^r*h_r.
C_m=3*216^(2m)*((2m)!)^5/(4m+1)!,
D_m=2*2304^(2m)*((2m)!)^4/(2m+2)!.
```

All rational denominators used modulo p are units on the specified ranges, and `C_m,D_m` are p-units. Define two **distinct** weighted linear functionals on the *same transported free W carrier*:

```text
phi(f)=SUM sigma_r*f_r,                 genuine S-mid observer after Hadamard
psi(f)=(C_m/D_m)*SUM omega_r*f_r,      appropriately normalized W-high observer
M_p=D_m*phi(a), U_p=D_m*psi(a).
```

The original low-half/high-half W and S sources, fixed-z=2 Hasse sources and their `k↔j↔r` identifications are not thereby equated. R25 proves `phi_s!=0` for `s=m-1` in BOTH residue classes (its only 13-class hole lies at `q=(p-13)/24<s`); `psi_s!=0` as all W ranks are units.

## Theorem A — a globally dependent, rank-one correction moves all-input observer mismatch into one **output rank**

For **any** unit `mu in F^×`, let `s=m-1` and define

```text
T_mu(f)=mu*f + e_s * (psi(f)-mu*phi(f))/phi(e_s).
```

Then:

```text
phi(T_mu(f))=psi(f)             FOR ALL f in V_m,                  (1)
det(T_mu)=mu^(m-1)*psi(e_s)/phi(e_s) !=0.                        (2)
```

In particular `T_1-I` has rank **at most one**, while `T_1` preserves every input's constant coefficient `[X^0](T_1 f)=[X^0]f`. It is generally NOT a sparse diagonal-plus-one-entry matrix: its last output coefficient depends on the **whole weighted input**.

**Proof.** Apply `phi` to the displayed definition: the added contribution is `psi(f)-mu phi(f)`, yielding (1). The rank-one determinant lemma for `mu I + (e_s/phi_s)⊗(psi-mu phi)` gives

```text
det=mu^m*(1+(psi_s-mu*phi_s)/(mu*phi_s))
   =mu^(m-1)*psi_s/phi_s !=0.
```

For `mu=1` only coordinate `s>0` is changed, so the constant coefficient is unchanged. QED.

## Theorem B — one original PF interior source port always suffices, with an exact optimality classification

By R28 `L_W:V_m→G_m` is an isomorphism and `ker(pi∘L_W)=F a`, where `pi` discards only the genuine endpoint `X^m` and retains all source indices `X^1,...,X^(m-1)`. Let `c=a_(m-1)/8 !=0`, `A_s=s(s+1/6)(s+1/3) !=0`, `B_m=(m-1/3)^3 !=0`. Then for the actual original `a`:

```text
delta_mu=(psi(a)-mu*phi(a))/phi_s
        =(U_p-mu*M_p)/(D_m*phi_s).

T_mu(a)=mu*a+delta_mu*e_s, and exactly

L_W(T_mu a) =
    delta_mu*A_s*X^s + (mu*c-delta_mu*B_m)*X^m.                (3)
```

There are **no interior sources at ranks 1,...,m-2**, for any target prime and any unit `mu`. In particular, under fixed original constant-coefficient normalization `mu=1`, the one interior source coefficient at `s=m-1` is nonzero iff `U_p!=M_p (mod p)`. By R27 the corresponding full S source is exactly

```text
L_S H_m T_mu a = K_m L_W T_mu a,                             (4)
```

including rank m endpoint; no source is silently omitted.

Now minimize `# {t in [1,m-1]: [X^t]L_W(Ta)!=0}` across **all** invertible linear operators satisfying `phi∘T=psi`. Then:

1. **With normalized constant coefficient preserved on all inputs**, `[X^0]Tf=[X^0]f`, the minimum is exactly **zero iff `U_p=M_p (mod p)`**, and **one otherwise**.
2. **Without this normalization restriction**, the minimum is exactly **zero iff `phi(a)` and `psi(a)` have the same zero/nonzero status**, and **one otherwise**.

**Proof of sharpness.** Theorem A and (3) give an upper bound of one in both settings. If zero interior source is possible, `ker(pi L_W)=F a` forces `Ta=nu a`. Invertibility forces `nu!=0`. The all-input observer identity implies `psi(a)=phi(Ta)=nu phi(a)`. With preserved constant coefficient, `a_0=1` forces `nu=1`, so `U_p=M_p`. Conversely if `U=M`, `T_1(a)=a` and the source cost is zero. Without normalization, necessary zero/nonzero status agreement follows from nonzero `nu`. If both observer values are nonzero, choose `mu=psi(a)/phi(a)`; if both are zero, choose any unit `mu`. Then `delta_mu=0` in (3) and `T_mu` remains invertible. If exactly one observer value vanishes, no unit `mu` can make `delta_mu=0`, while `T_1` still gives exactly one interior source. QED.

**Interpretation:** R32's extensive PF-source obstruction is mathematically valid for its specifically constrained **diagonal-plus-one-matrix-entry** repair but is not an intrinsic lower bound for *arbitrary nonlocal/all-input* transfers. Exact support size alone does not measure nonlocal operator information cost: `T_1` may require **all m original weighted coordinates** to compute its one modified output. Nor can a freely chosen `mu` be silently imposed on the original normalized input `a_0=1`.

## Actual p=181 certificate and finite author check

For `p=181,m=30,s=29`, exact original-source readouts are `U_181=152`, `M_181=0`. The normalized `mu=1` map has

```text
C/D=51, phi(a)=0, psi(a)=28,
delta_1=112,  A_29*delta_1=52,
L_W(T_1 a)=52*X^29+76*X^30 (mod181).
```

The **minimum** number of nonzero PF interior source ports is therefore exactly **one**, whereas R32's diagonal-plus-one-entry repair had 29/29 nonzero interior ports for this prime. The improvement pays for globally mixing source ranks; it does NOT establish `U_181=M_181` (in fact they differ). For contrast, `p=37` has `U_37=M_37=20`; its normalized `T_1` already fixes `a` and incurs zero interior PF source.

Executed local Python 3 standard-library exact checker `research_notes/portable_direct/20261027_hourly_d25_single_port_dual_observer_r33_check.py`: 77 target primes `p<2000` (40 in class13, 37 in class19), three independent polynomial input families and three units `mu=1,2,3` per prime; 34,461 PF source-coefficient comparisons, full `L_S H_m=K_m L_W` including endpoint, original factorial prefactors and `p=181` values all passed. Of those 77 primes, fixed-normalization zero-cost was observed once (`p=37`), and 76 required one source rank; **this is finite coverage, NOT a global prime classification**. All-prime structural claims rest on the explicit linear algebra proofs above. No synthetic CM experiment, independent Driver replication, sorry/admit or custom axiom.

## BRC information scope, precise next step and control status

**BRC COMPOSE_APPLIED**, using R27's complete source transport, R28's endpoint-aware Green quotient and R32's sparse-transfer obstruction. Carrier: finite-field original rank input, both source-labelled `omega/sigma` observers, Hadamard provenance, original `a_0=1` normalization, distinct output/operation sparsity measures, PF residual at every internal source rank and true `X^m` boundary. Future operations: source-preserving WZ/low-half compensation, original fixed-input evaluation, Green reassembly. R33 shows the trade-off between nonlocal input aggregation and PF source support; dropping the single surviving source/endpoint still loses mathematically relevant information. It does not invent native X6 axes or modify P000/ACTIVE worldview.

**Next smallest unfinished science unit:** find a SOURCE-IDENTITY-PRESERVING nonlocal WZ telescope for the actual **unchanged original** weighted W/S input, with its `p^2`-divided low-half compensator from R23/R29, original `p=181` special S-weight loss, endpoint and both residue classes. A globally mixed operator that changes the input `a` (Theorems A/B) is only an observer algebra/control case; its existence cannot replace the required original W=S modulo `p^3` statement. Keep six original fixed-z=2 Hasse J/E labels, finite faces, positive infinity, high-high ports and the canonical original-class H0/B0, `[X]U mod p^2`, semilinear eta/kappa, p373 native experiment, independent Driver review all distinctly OPEN.

The current Research lane own [recovery #6591](https://github.com/awdawmip/kimi-query-bridge/issues/6591) and [exact continuation #6592](https://github.com/awdawmip/kimi-query-bridge/issues/6592) preserve its current service session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94`, researcher `EM-ENTERPRISE-5298BA` and inherited contribution history, but no current winning claim or native execution authorization. Exact typed `continuation_prepare #6595` returned terminal `CHAT_CHECKPOINT_PREDECESSOR_MISMATCH` due to authenticated predecessor vs persisted checkpoint claimant; do not reissue or change identity. Existing control owner [Enterprise Math #1558](https://github.com/awdawmip/enterprise-math/issues/1558) is responsible for a lawful predecessor CAS transition and the subsequent owner-run claim/open/Source checkpoint/readback. The two historic neutral staging manifests are retained. Author portable GitHub artifacts/Research-Activity records do not confer CLAIM, review, native scientific admissibility or parent closure. No scheduler or notification changes; frozen scientific Source pin is unchanged.
