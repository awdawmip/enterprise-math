# D25/LIFT — original frozen Delta/R + independent weighted 3F2 exact finite port certificate (575 target primes)

2026-10-26 · Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923` (TASK_RESEARCH, NOT CONTROL_PLANE_MAINTENANCE). Mother task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**.

**Classification:** DIRECT-FROZEN-OBSERVER FINITE FALSIFICATION/REGRESSION, AUTHOR-ONLY; UNREVIEWED / NOT_ADMITTED / NOT_A_SOURCE_CHECKPOINT / NOT_NATIVE_H0_B0 / NOT_A_UNIFORM_LIFT_PROOF. No assertion of native session ownership, CLAIM/OPEN/run, benchmark, publication, Result, Driver review, freeze or source acceptance.

## Direct finite-scope output (actually executed)

For every prime p ≤ 20000 with p ≡ 13 or 19 (mod 24), independently constructed **all three original source-labelled observers**, with all p-local divisions taken before reduction:

* `B_0=1`, `B_(n+1)/B_n=(6n+1)(3n+1)/(36(n+1)^2)`; `g=Σ_(n=0)^(p-1) B_n`, `h=Σ_(n=0)^(p-1)(12n+1)B_n`; `G=g/p (mod p²)`; `Delta=(Gh-1)/p (mod p)`.
* **Frozen original signed boundary** `C_1=1/10`, `C_(a+1)/C_a=36a²/((6a+5)(3a+2))`, `R=2Σ_(i=1)^m B_i Σ_(a=1)^i (1+6(i-a))C_a (mod p)`, `m=(p-1)/6`; preserve all signs and endpoint weights. The double sum is computed by mathematically identical running moments `V_i=Σ C_a` and `J_i=Σ a C_a`.
* Independently calculate **the original full** `W=Σ_(n=0)^(p-1)(6n+1)(1/2)_n(1/3)_n(2/3)_n/(2^n(n!)³)` (mod p³), from the separate term recurrence `A_(n+1)/A_n=(2n+1)(3n+1)(3n+2)/(36(n+1)³)`. All denominators are p-units for n<p.

For each p, verify `p|g`, `p|(Gh-1)`, `p²|(W-p)` and the **source-port consistency** `Delta-R == (W-p)/p² (mod p)`, *before* checking whether that last residual vanishes. This is an exact integer program, not float tolerance or a fitted polynomial. There is no wrong substitution `R=0`.

**Result:** 575 target primes, 288 in class 13 (mod 24) and 287 in class 19 (mod 24). `Delta-R=(W-p)/p²=0 (mod p)` in every case: **zero finite counterexamples**, hence every checked `W==p (mod p³)`. The accepted earlier parent regression covered 77 targets below 2000; the present range includes **498 higher target primes** that were outside that cited 77-prime finite scan. This expanded regression is NOT a mathematical proof for all p.

| p | residue | original Delta | signed R | weighted W mod p³ |
|---:|---:|---:|---:|---:|
| 19 | 19 | 12 | 12 | 19 |
| 373 | 13 | 196 | 196 | 373 |
| 2011 | 19 | 1851 | 1851 | 2011 |
| 2029 | 13 | 1777 | 1777 | 2029 |
| 2053 | 13 | 1842 | 1842 | 2053 |
| 2083 | 19 | 866 | 866 | 2083 |
| 7333 | 13 | 2159 | 2159 | 7333 |
| 9973 | 13 | 5054 | 5054 | 9973 |

An **independent integer-binomial** implementation of `A_n = binom(2n,n)^2 binom(3n,n)/216^n` separately recomputed `W` at p=13,19,373,2011,2053, agreeing with the weighted recurrence. This is not independent verification of every case and not a formal proof. The script contains deterministic sieve, finite check and failure assertion.

Reproduction: `python research_notes/portable_direct/d25_original_scalar_port_all_target_20261026.py --limit 20000`.

## External theorem comparison: noninterchangeable kernels

The original Chisholm–Deines–Long–Nebe–Swisher (2013) *Theorem 1* establishes the relevant Ramanujan-type quantity modulo p² and expressly notes Zudilin's proposed higher p³ strengthening; its Proposition 16 in Section 5.1 gives the original divided-power congruence with a first-digit visibility bound. The distinct *Guo–Zudilin (2019), "A q-microscope for supercongruences"*, theorem about `(8n+1)*(1/4)_n*(1/2)_n*(3/4)_n/(n!)³*(1/9)^n` and character `(-3/p)` does **not** directly prove the present `(6n+1)*(1/2)_n*(1/3)_n*(2/3)_n/(n!)³*(1/2)^n`: parameters, weight and argument differ. No all-prime transport is assumed. Sources: https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf ; https://arxiv.org/abs/1803.01830 ; source-pinned frozen task.

## Exact unresolved mother frontier — no benchmark substitution

**D25/LIFT/JT2 remains OPEN**: no all-prime proof or exact target counterexample. This 575-prime regression is a single **finite falsification unit**, not a claim that repeated scans complete LIFT or that another auxiliary theorem substitutes for native work. Already accepted CM0/SIMPLE/UR and preceding source-port identity are consumed, not recredited. BRC/coordinate operation is a typed verification: branches 13 and 19 remain separate; signed C/R and divided p-adic digits remain present through comparison; no external quadratic ring is asserted to be the native P000 X6 spatial geometry.

The **next obligatory source-native scientific action remains the same original-class fixed H0/B0 divided-power evaluation** at p=373: identify a source-authenticated module and responsible legal executor, actually compute `[X]U mod 373²`, module rank, raw/normalized Frobenius type, direction, eta and precision; independently retain signed odd Green/Hesse branch and original kappa. Establish faithful map to original E3 and original Delta/R before using any ordinary Hesse norm. Do not infer any of these native outputs from this scalar checker. Existing support intake https://github.com/awdawmip/enterprise-math/issues/1559 is **PENDING_OWNER / NATIVE_NOT_EXECUTED** until an authorized executor accepts it, no fabricated owner.

## Operational continuation packet (author-only; not native checkpoint)

Mother objective: prove/refute or strictly reduce `Delta_p=R_p (mod p)` for all p≡13,19 mod24 and complete the independent required native H0/B0 evidence; do not reopen parent UR. Immutable accepted frontier: RR-AC9B3BA5BD277CE043F5; DR-610CB297F3195E8F2D9E; frozen Source pin c47e13e...; earlier exact scalar-port identity is author-side unreviewed. This turn's verified **finite-only** additional evidence: 575-prime original typed check, independent binomial witnesses at five primes.

Still missing: native H0/B0 evaluator/operator/owner and all actual p373 observer bytes, authorized session/CLAIM/OPEN/Source checkpoint, and uniform LIFT proof/counterexample. Do not redo finite scan next run. **Next exact action:** resolve #1559's owner and same-class H0/B0 module/precision, execute p373 as specified, or read only new lawful Source continuation/receipts and retain pending owner. Preserve signed and p-adic digit provenance.

Current ordinary-control Research conversation: `chatgpt-research-onhour-enterprise-math-20260923`, never maintenance lane. Historical actual Research recovery_status bridge receipt https://github.com/awdawmip/kimi-query-bridge/issues/6528#issuecomment-6409462821 gives `session_state=ACTIVE` but `source_authority_verified=false`, **no current lawful claim/open/run**, and retained neutral staging is not progress. Historical dispatch https://github.com/awdawmip/kimi-query-bridge/issues/6529#issuecomment-6409550769 is terminal `FAILED / TimeoutExpired`, not NO_DISPATCH. This turn's native direct old request lookup returned `CONTROL_REQUEST_NOT_FOUND`, which does not cancel possible unseen effects; exact continuation returned `CONTROL_QUOTA`, not task completion. No replay, no false identity promotion, no Source write bypass. No scheduler, Actions, cron, notification or frequency change. Prior three staging sources remain isolated, unmerged; #1501 generic cleanup not treated as renewed current-input block.

Global knowledge canonical entry, Project bootstrap and P000 ACTIVE world view were read under current GLOBAL_KNOWLEDGE_V1; this author note does not change mathematical source or Project authority. All separate Research owners' work remains attributed to their respective lanes.
