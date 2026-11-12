# R96 — Nonstationary tariff acquisition and mixed historical source-profile experiments

Date 2026-11-12. Author-side exact theorem and reproducible finite experiments; independent review pending. Frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This continues R95's **finite auxiliary rational circular-source model**, not a native X6, Shor or physical-heartbeat claim. P000 remains unchanged.

## R96.1 — Nonstationary online acquisition theorem

Fix an immutable full source identity set (including time and branch), an observation signature, and a rational covering interval. Requests i each allow a lazy exact answer of nonnegative integer cost `L_i`; once an exact winner profile has been installed for one fixed nonnegative integer cost `P`, each request may instead use it at nonnegative integer cost `E_i`. Current request prices are revealed before routing it, but no future request or price is known. Once installed the profile is retained for this key; each request then uses `min(L_i,E_i)`. Any memory expense is included in P and the quoted per-use tariffs, with no uncharged time-dependent holding expense.

Let `g_i=max(0,L_i-E_i)` and H be the sum of foregone g_i on previously served lazy requests. If not yet built, build immediately **before** request i when `H+g_i>=P` and `g_i>0`. Otherwise answer lazily. After building, answer via the cheaper exact path.

**Theorem.** The online total cost is at most twice the offline minimum, even with arbitrarily varying known current tariffs `L_i,E_i`.

**Proof.** Set `A=Σ_i min(L_i,E_i)`, `G=Σ_i g_i`. Because g_i are nonnegative, any offline purchase at a later time is weakly dominated by buying before the first request. Thus `OPT=A+min(G,P)`. If online never buys, `G<P` (apart from the zero-gain tie) and `ONLINE=A+G=OPT`. Otherwise immediately before the first buy H<P, and the triggering request has positive gain, so G>=P. Online cost is `A+H+P`, whereas offline cost is `A+P`; therefore `ONLINE<=2 OPT`, with equality for P=0 and otherwise a strict inequality in the excess. Summing independent nonsharing keywise inequalities preserves the factor 2. QED.

The key includes the entire source identity version, complete observer signature and covering domain. A valid certified OUT edit changes pruning costs but not the winner function, so certificate-only changes preserve the profile. Historical revisits to the same exact key reuse it. Different source identities or observation signatures are distinct keys.

## R96.2 — Stale tariff counterexample

A stationary prediction `(P,L,E)=(100,120,1)` causes R95's fixed threshold to build immediately on a single query, costing 101. If actual current costs are `(100,1,1)`, the offline exact lazy answer costs only 1. Hence an unqualified transfer of the stationary 2-competitive guarantee to stale tariff estimates is false. The R96 theorem relies on accurate prices before routing each query, or a separately demonstrated error-bound contract.

## Exact validation, full-workload measures

The self-contained reproducibility bundle contains the executed `check_r96.py` plus unchanged R82/R86/R90–R95 dependencies and `verification_r96.json`. The GitHub text artifacts here contain lossless gzip/base64 versions of the executed R96 driver and the full JSON data. Decode: `base64 -d check_r96.py.gz.b64 | gzip -d > check_r96.py`; same for `verification_r96.json.gz.b64`.

Exactly 196,080 finite integer-tariff streams were exhausted: P in 0..9, n in 0..5, and 7 allowed (L,E) pairs. For every stream, the derived 2 bound holds and offline optimization agrees with explicit enumeration of every possible purchase time. Max observed ONLINE/OPT was 17/9: P=9 and requests (1,0),(7,0),(1,0), yielding online=17, offline=9.

One deterministic mixed history has 13 persistent versions, 6 certificate-only edits, 17 distinct source/signature/domain keys, and 200 queries. All three exact implementations — lazy certified-index search, eager exact profiles, and quote-driven adaptive selection — agree with an independent exact rational whole-interval reference. CHANGES produces two rational witnesses checked against exact original circular membership and full time/branch identity.

**Broad domain** `[-1/4,3/5]`: 98 CHANGES, 69 STABLE, 33 STABLE_NONE. In the recorded single CPython process: lazy query total **206.783 ms**; eager construction plus queries **2539.312 ms**; adaptive **1086.290 ms**. Eager retained profile graph ~833,796 Python bytes / 17 keys; adaptive ~330,564 bytes / 8 keys. This constructs a workload in which eager profile expansion is expensive.

**Narrow domain** `[1/16-1/1200,1/16+1/1200]`: 4 CHANGES and 196 stable classifications. With the same event structure: lazy **167.650 ms**; eager **20.494 ms**; adaptive **35.192 ms**. Eager retained profile graph ~6,500 bytes; adaptive ~2,480 bytes. This is a regime in which exact preprocessing is attractive.

Measured CPU numbers include profile construction and query costs, exclude the shared historical source/certificate construction and independent reference validation (both separately reported). The deterministic quote `(L,E,P)=(460000,12000,1800000)` cost units per key produces adaptive quoted cost 36,064,000 versus quoted offline optimum 21,728,000; the broad-domain *measured* build expense is far higher than quoted, explaining the divergence. CPU times are one-process sequential measurements, not hardware-universal bounds; graph bytes are recursively measured Python representation rather than peak RSS. Full rational and exact oracle counts are retained in JSON; integer bit-operation counts and predictive tariff calibration remain open.

Executed success prefix: `R96_PASS 196080 200 98 6`.

## R97 — next executable unit

Establish and test source/domain-aware build-cost estimation or certified tariff intervals, against the broad-profile blowup and narrow repeated-query cases. Account for retained-history memory, per-key invalidation, build work, exact rational bit operations and witness recovery. Keep the original closed-rational-interval boundary semantics, complete identity and verified certified-OUT pruning. Formal S23 claim, Source activity checkpoint and independent review are separate authority operations.
