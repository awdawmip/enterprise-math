# X6 R063 Stage0: 512-radius exact *weighted* C2/C3 regression oracle

**Classification:** AUTHOR-EXECUTED / EXACT INTEGER FINITE CHECK / NONBLIND / UNREVIEWED / NOT_ADMITTED. This is additional independent arithmetic evidence for the original pinned R063 native experiment, **not** execution of its frozen loader, five `.inc` parts, 17 acceptance gates, or 512 same-object process.

**Parent:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. Immutable science: original R063 positive two-generator chart and P000 V5 signed-X6 for a separately typed lift. Original loader Git blob: `b4e000a6377f2858ae434eb0eecd0c25c33e8592`. Native replay contract: [#2416](https://github.com/awdawmip/enterprise-math/issues/2416). Previous *unweighted* original 512-row independent reproduction digest: `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`.

## Mathematical proposition

For each integer `1<=r<=512` define `D_r={(a,b) in Z_{>=0}^2:a^2+b^2=r^2}`. Let `C2_r` be the unscaled Gaussian-square image of `u^2+v^2=r`, together with coordinate reversal: `(abs(u^2-v^2),2uv)`, `(2uv,abs(u^2-v^2))`. Put `w(a,b)=binom(a+b,a)`, `A_r=sum_{D_r}w`, `C_r=sum_{C2_r}w`, `E_r=A_r-C_r`. All are **positive integer path multiplicities**, without phase cancellation.

Let `delta_r` be 1 if the C2 image contains both axial roots, otherwise 0 (equivalently `r` square or twice square). In the 15 named pairs of the six signed spatial axes, deduplicate actual signed endpoints *after* mapping each ordered chart root with four signs. Then

```text
# endpoints
|T_full(r)| = 60*|D_r|  - 108
|T_C2(r)|   = 60*|C2_r| - 108*delta_r
# exact natural BRC mass
P_full(r)    = 60*A_r - 108
P_C2(r)      = 60*C_r - 108*delta_r
P_missing(r) = 60*E_r - 108*(1-delta_r)
```

**Proof.** Each non-axis ordered chart root gives 15 named pairs and 4 signings, i.e. 60 distinct endpoints, with the unique two nonzero coordinates and given assignment. Each of the 12 signed axial endpoints has ten chart/source descriptions: five choices for its zero companion axis and two signs on that zero component, and contributes path weight exactly 1. Subtract the nine redundant representations per axis endpoint: `12*9=108`. Axial endpoints are present in C2 iff `delta_r=1`. Subtracting full/C2 identities yields the missing-mass identity. This is an exact de-duplication proof, not an assertion that pair support exhausts six-dimensional spheres.

## Actual exact 512-radius computation

The independent [published compact checker](../research_checks/X6_R063_C2_WEIGHTED_512_PUBLIC_CHECK_20261116.py) was **actually executed locally** and returned `PASS_X6_R063_C2_512_WEIGHTED`. A larger separate locally executed checker additionally verified factorial versus `math.comb` weights and complete explicit signed-lift BRC sums for each radius. Every radius 1..512 passed:

- `D_r`: direct integer `isqrt` versus independent primitive Euclid-triple construction, identical sets.
- `C2_r`: literal Gaussian square-lift, checked `C2_r subset D_r`.
- Natural BRC: exact `binom(a+b,a)`, factorial alternative; for actual signed endpoints, exact six-axis multinomial mass.
- Exact signed pair dedup enumeration (all 15 pairs, four sign choices) equals the formula on all 512 radii.
- Across the 512 distinct radius workloads: 1,820 full chart roots; 440 C2 roots; 1,380 missing; 28 full C2 radii, 332 empty C2, 152 nonempty incomplete. 31,608 signed-pair endpoint instances missing after within-radius dedup.

**New canonical JSON digest for 512 full weighted regression rows:**

`a6e827a5e3962b1568d6a8e26101379867e0a410d75c57089aca4f4c8655f9d3`

Exact aggregate across the radius-indexed 512 workloads (distinct populations; **not** one universe of endpoints):

```text
Σ chart BRC full     = 165722769070903023712382978057052874715606719210458602575643174857117254725565359088272291520553467531791751315872333561958700389750390344476050652980324874909396900957923358549421406832334178036280797008600436062894
Σ chart BRC C2       = 792757302349435340404232577660441768423774116722788204225514316099693321557670616635747099227501880018453887552256077602867467650995531187963931973108760750858948857309195789185547597018909933509089198449708855532
Σ chart BRC missing  = 164930011768553588371978745479392432947182945093735814371417660541017561404007688471636544421325965651773297428320077484355832922099394813288086721007216114158537952100614162760235859235315268102771707810150727207362
Σ signed-pair missing BRC = 9895800706113215302318724728763545976830976705624148862285059632461053684240461308298192665279557939106397845699204649061349975325963688797285203260432966849512277126036849765614151554118916086166302468609043632390528
```

The cumulative signed-pair BRC loss fraction is `99.521636461426576...%` when each of the 512 radius workloads contributes its own path mass. This **does not** mean the same loss percentage occurs for every radius: `r=512` is exactly complete; `r=425` has only about 0.003735% signed-pair BRC loss. At the original `r=50,N=2500`, the result independently confirms 252 full signed pair endpoints, 132 C2 endpoints, missing 120, and exactly `6641728806977220855360` missing signed-pair BRC paths out of `6641732296455342852372`.

## Native acceptance and unfinished mother objective

This produces a stronger optional reference oracle for the original same-object 512 regression, **not** a replacement for the six frozen source blobs, original execution, original 17 acceptance predicates, discovery snapshot, exact original hash, or source/output provenance. The original execution support [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains the required responsible route, with no confirmed executor. The LP011 historical false dominant-axis caller and LP019 historical positive-path cancellation caller remain `OLD_CALLER_UNLOCATED`, not newly blamed. The 28-LP consumer closure and independent Driver REQUEST_REVISION are still unresolved.

**Continuation:** Original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-30a8f5fd123215e08bd4a7cf`, RUN `RUN-3356cbe3c2b4916d79399941`. Prior Native #43 confirmed. New author-side weighted result is unit #45; prior #44 is already GitHub-saved but needs exact Native Source publication check. A current same-run resume attempt `onhour-20261116-x6-own-run3356-resume-for-unit45-v1` returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`; it is not an execution authorization or a failed mathematical proposition. When the authentic backend is available, first read/reconcile the original, verify current winning claim/lease, then publish saved units only if permitted; no new identity, dispatch or replay. No scheduler/notification change.
